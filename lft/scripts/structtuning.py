"""
Struct-Aware Knowledge Injection (LfT-Part 2, NIM + Recursive + KGA-Hybrid)
----------------------------------------------------------------------------
• Reads domain_textbook.md → hierarchical mindmap
• Flattens all nodes (sections, subsections, exercises)
• Loads KGA seed questions for topic weighting & hybrid QA expansion
• Generates diversified & difficulty-graded synthetic QAs (SSFT)
• Saves checkpoints so nothing is lost mid-run
"""

import os, json, time, signal, sys, argparse, re, random, html, itertools
from tqdm import tqdm
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.messages import HumanMessage, SystemMessage
from scripts.utils import load_cfg

# -----------------------------------------------------------------
# Paths
# -----------------------------------------------------------------
CHECKPOINT_FILE = "data/structured/struct_ckpt.json"
MINDMAP_FILE    = "data/structured/mindmap.json"
SSFT_FILE       = "data/sft/ssft.json"
KGA_FILE        = "data/raw/knowledge_gap_seed.json"

os.makedirs("data/structured", exist_ok=True)
os.makedirs("data/sft", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# -----------------------------------------------------------------
# Logging
# -----------------------------------------------------------------
def log(msg: str):
    print(msg)
    with open("logs/structtuning.log", "a") as f:
        f.write(msg + "\n")

# -----------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------
def clean_json(text):
    text = text.replace("```json", "").replace("```", "").strip()
    text = re.sub(r",(\s*[}\]])", r"\1", text)
    return text

def normalize_mindmap(mindmap):
    def recurse(node):
        node.setdefault("summary", "")
        if isinstance(node.get("children"), dict):
            node["children"] = [
                {"id": f"{node['id']}.{i+1}", "title": k, "summary": v}
                for i,(k,v) in enumerate(node["children"].items())
            ]
        elif not isinstance(node.get("children"), list):
            node["children"] = []
        for c in node["children"]: recurse(c)
    for n in mindmap.get("nodes", []): recurse(n)
    return mindmap

def flatten_nodes(node_list):
    flat=[]
    for n in node_list:
        flat.append(n)
        if "children" in n and isinstance(n["children"],list) and n["children"]:
            flat.extend(flatten_nodes(n["children"]))
    return flat

# -----------------------------------------------------------------
# Mindmap extraction
# -----------------------------------------------------------------
def extract_structure(evaluator, text):
    sys_msg = SystemMessage(content=
        "You are an expert curriculum designer. "
        "Extract a hierarchical JSON mindmap (chapters→sections→subsections) "
        "with keys: id, title, summary, children[].")
    user_msg = HumanMessage(content=
        f"TEXTBOOK CONTENT:\n{text[:12000]}\n\n"
        "Return strictly valid JSON like "
        "{\"nodes\":[{\"id\":\"1\",\"title\":\"...\",\"summary\":\"...\",\"children\":[...] }]}."
    )
    resp = evaluator.invoke([sys_msg, user_msg])
    raw = clean_json(resp.content)
    try: mindmap=json.loads(raw)
    except Exception: mindmap={"nodes":[{"id":"root","title":"Domain","summary":raw}]}
    return normalize_mindmap(mindmap)

# -----------------------------------------------------------------
# QA utilities
# -----------------------------------------------------------------
QA_TYPE_PROMPTS = {
    "definition":  "Write a definition-style question and short answer.",
    "explain":     "Write a conceptual explanation question and clear answer.",
    "example_problem": "Create a worked numerical example and solution.",
    "derivation":  "Pose a derivation/proof-style question and detailed answer.",
    "application": "Ask a real-world applied question and answer.",
    "mcq":         "Create a 4-option MCQ with correct answer and reasoning.",
    "multi_step":  "Pose a multi-step reasoning question and detailed solution.",
    "comparison":  "Ask to compare this concept with a related one.",
    "debug":       "Give a wrong statement and ask 'what is wrong'; answer correctly."
}
DIFFICULTY_LEVELS = ["easy","medium","hard"]

def _call_teacher_for_qas(teacher,title,summary,prompt_suffix):
    prompt=(f"Topic: {title}\nSummary: {summary}\n\n{prompt_suffix}\n\n"
            "Return strictly JSON: [{\"question\":\"...\",\"answer\":\"...\"}].")
    return teacher.invoke([HumanMessage(content=prompt)]).content.strip()

def _paraphrase_text(llm,text,n=1):
    outs=[]
    for _ in range(n):
        p=f"Paraphrase this text keeping meaning same:\n{text}\nReturn only paraphrased text."
        try: outs.append(llm.invoke([HumanMessage(content=p)]).content.strip())
        except Exception: outs.append(text)
    return outs

def _extract_numbers_from_string(s:str): return [float(x) for x in re.findall(r"[-+]?\d*\.?\d+",s)]

def generate_parameterized_variants(qa,variants=3):
    q,a=qa.get("question",""),qa.get("answer","")
    nums=_extract_numbers_from_string(q+" "+a)
    if not nums: return [qa]
    outs=[]
    for _ in range(variants):
        new_q,new_a=q,a
        for n in nums:
            newv=round(n*(1+random.uniform(-0.2,0.2)),3)
            new_q=re.sub(str(n),str(newv),new_q,1)
            new_a=re.sub(str(n),str(newv),new_a,1)
        outs.append({"question":new_q,"answer":new_a})
    return outs

# -----------------------------------------------------------------
# QA generation
# -----------------------------------------------------------------
def synthesize_qas_v2(teacher,paraphraser,title,summary,total_q=30):
    """Generate diversified QAs for one node."""
    types=list(QA_TYPE_PROMPTS.keys())
    base=total_q//len(types)
    alloc={t:base for t in types}
    for t in random.sample(types,total_q-base*len(types)): alloc[t]+=1
    all_qas=[]
    for qtype,count in alloc.items():
        prompt=f"[{qtype}] {QA_TYPE_PROMPTS[qtype]}"
        try:
            raw=_call_teacher_for_qas(teacher,title,summary,prompt)
            js=json.loads(clean_json(raw))
            if not isinstance(js,list): raise ValueError
        except Exception:
            js=[{"question":f"{title} ({qtype})","answer":"Auto fallback"}]
        for qa in js[:count]:
            qa={"question":qa.get("question","").strip(),
                "answer":qa.get("answer","").strip(),
                "meta":{"type":qtype}}
            all_qas.append(qa)
    # expand + paraphrase
    expanded=[]
    for qa in all_qas:
        if qa["meta"]["type"] in ("example_problem","multi_step","derivation"):
            expanded+=generate_parameterized_variants(qa,3)
        else: expanded.append(qa)
    final=[]
    for qa in expanded:
        final.append(qa)
        try:
            qp=_paraphrase_text(paraphraser,qa["question"],1)[0]
            ap=_paraphrase_text(paraphraser,qa["answer"],1)[0]
            final.append({"question":qp,"answer":ap,
                          "meta":{"type":qa["meta"]["type"],"paraphrase":True}})
        except Exception: continue
    random.shuffle(final)
    return final[:total_q]

# -----------------------------------------------------------------
# Hybrid KGA-guided expansion (Option C + D)
# -----------------------------------------------------------------
def _compose_hybrid_prompt(base_q,base_a,reasoning,topic,difficulty,variant,cross_ref=None):
    cross=f" Relate it also to {cross_ref}." if cross_ref else ""
    return (f"Topic: {topic}\nExisting question: {base_q}\nAnswer: {base_a}\nReasoning: {reasoning}\n\n"
            f"Generate a new {variant} question about this topic at **{difficulty}** level."
            f"{cross}\nReturn JSON: [{{\"question\":\"...\",\"answer\":\"...\"}}].")

def generate_hybrid_qas(teacher,paraphraser,kga_seeds,nodes,per_seed=10):
    node_titles=[n.get("title","") for n in nodes]
    results=[]
    for seed in tqdm(kga_seeds,desc="🌱 Expanding KGA seeds"):
        topic=seed.get("topic","General")
        bq=seed.get("question","")
        ba=seed.get("final_answer",seed.get("answer",""))
        reason=seed.get("chain_of_thought_reasoning",seed.get("answer_reasoning",""))
        cross=random.choice([t for t in node_titles if t!=topic]) if node_titles else None
        combos=list(itertools.product(DIFFICULTY_LEVELS,list(QA_TYPE_PROMPTS.keys())))
        random.shuffle(combos); combos=combos[:per_seed]
        for diff,var in combos:
            prompt=_compose_hybrid_prompt(bq,ba,reason,topic,diff,var,cross)
            try:
                raw=teacher.invoke([HumanMessage(content=prompt)]).content
                qas=json.loads(clean_json(raw))
            except Exception:
                qas=[{"question":f"{topic} ({diff}/{var})","answer":"Auto fallback"}]
            for qa in qas:
                qa["meta"]={"topic":topic,"difficulty":diff,"variant":var,"source":"KGA-Hybrid"}
                qa["node_id"]=topic; results.append(qa)
        # paraphrase newest block
        for qa in results[-len(combos):]:
            try:
                qp=_paraphrase_text(paraphraser,qa["question"],1)[0]
                ap=_paraphrase_text(paraphraser,qa["answer"],1)[0]
                results.append({"question":qp,"answer":ap,
                                "meta":{**qa["meta"],"paraphrase":True},
                                "node_id":topic})
            except Exception: continue
    return results

# -----------------------------------------------------------------
# Checkpoint helpers
# -----------------------------------------------------------------
def save_checkpoint(results,processed):
    json.dump({"results":results,"processed":list(processed),"time":time.ctime()},
              open(CHECKPOINT_FILE,"w"),indent=2)
    log(f"[CKPT] saved ({len(processed)} nodes done)")

def qa_count_for_node(node,base,weak):
    depth=node["id"].count(".")
    title=node.get("title","")
    mult=1.0
    if title in weak: mult*=3
    if depth>=2: mult*=0.5
    return max(3,int(base*mult))

# -----------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--domain_file",default="data/raw/domain_textbook.md")
    parser.add_argument("--qa_per_node",type=int,default=30)
    args=parser.parse_args()

    cfg=load_cfg("configs/nim_config.yaml")
    api_key=cfg["NIM_API_KEY"]

    log("🔗 Initializing NIM models ...")
    evaluator=ChatNVIDIA(model=cfg["EVALUATOR_MODEL"],api_key=api_key)
    teacher=ChatNVIDIA(model=cfg["TEACHER_MODEL"],api_key=api_key)
    paraphraser=teacher

    # KGA topics
    weak=set(); kga=[]
    if os.path.exists(KGA_FILE):
        try:
            kga=json.load(open(KGA_FILE))
            weak={ex.get("topic","").strip() for ex in kga if ex.get("topic")}
            log(f"🧠 Loaded {len(weak)} weak topics from KGA.")
        except Exception as e: log(f"[WARN] KGA read fail: {e}")

    # Mindmap
    text=open(args.domain_file).read()
    if not os.path.exists(MINDMAP_FILE):
        log("📘 Extracting mindmap ...")
        mm=extract_structure(evaluator,text)
        json.dump(mm,open(MINDMAP_FILE,"w"),indent=2)
    else: mm=json.load(open(MINDMAP_FILE))
    nodes=flatten_nodes(mm.get("nodes",[]))
    log(f"📚 Total nodes (with children): {len(nodes)}")

    results,processed=[],set()
    if os.path.exists(CHECKPOINT_FILE):
        ck=json.load(open(CHECKPOINT_FILE))
        results=ck.get("results",[]); processed=set(ck.get("processed",[]))
        log(f"♻️ Resumed ({len(processed)} nodes done)")

    signal.signal(signal.SIGINT,lambda s,f:(save_checkpoint(results,processed),sys.exit(0)))

    # Struct-aware generation
    for node in tqdm(nodes,desc="🏗️ Struct-Aware Generation"):
        nid=node.get("id",node.get("title",""))
        if nid in processed: continue
        title=node.get("title","Untitled")
        summ=node.get("summary",title)
        qcount=qa_count_for_node(node,args.qa_per_node,weak)
        if title in weak: log(f"🔥 Boosting weak topic: {title} → {qcount} QAs")
        try: qas=synthesize_qas_v2(teacher,paraphraser,title,summ,total_q=qcount)
        except Exception as e:
            log(f"[WARN] {nid} failed: {e}")
            qas=[{"question":title,"answer":str(e),"meta":{"type":"fallback"}}]
        for qa in qas: qa["node_id"]=nid; results.append(qa)
        processed.add(nid)
        if len(processed)%3==0: save_checkpoint(results,processed)
        time.sleep(0.05)

    json.dump(results,open(SSFT_FILE,"w"),indent=2)
    save_checkpoint(results,processed)
    log(f"✅ Struct-based QAs: {len(results)}")

    # Hybrid KGA expansion
    if kga:
        log("🌱 Starting KGA-guided hybrid expansion ...")
        hybrid=generate_hybrid_qas(teacher,paraphraser,kga,nodes,per_seed=10)
        results.extend(hybrid)
        log(f"✅ Added {len(hybrid)} hybrid QAs.")

    json.dump(results,open(SSFT_FILE,"w"),indent=2)
    save_checkpoint(results,processed)
    log(f"🏁 TOTAL {len(results)} QAs → {SSFT_FILE}")

if __name__=="__main__": main()
