"""
Evaluation Script (Config Integrated)
------------------------------------
Compares teacher vs student on BLEU & ROUGE metrics.
"""
import json, torch
from tqdm import tqdm
from datasets import load_metric
from transformers import AutoTokenizer, AutoModelForCausalLM
from scripts.utils import load_cfg

def generate_answers(model, tokenizer, questions):
    answers = []
    for q in tqdm(questions):
        inputs = tokenizer(q, return_tensors="pt").to(model.device)
        output = model.generate(**inputs, max_new_tokens=200, temperature=0.7)
        ans = tokenizer.decode(output[0], skip_special_tokens=True)
        answers.append(ans)
    return answers

def main():
    cfg = load_cfg("configs/nim_config.yaml")
    eval_model_path = cfg["MODEL_OUTPUT"]
    teacher_model = cfg["TEACHER_MODEL"]
    eval_data = cfg["DATA_PATHS"]["COMBINED"]

    print(f"📘 Loading evaluation dataset → {eval_data}")
    data = json.load(open(eval_data))
    data = data[:200]
    questions = [f"Question: {d['question']}" for d in data]
    refs = [d["answer"] for d in data]

    print("🧠 Loading models (student + teacher)...")
    stu_tok = AutoTokenizer.from_pretrained(eval_model_path)
    stu_mod = AutoModelForCausalLM.from_pretrained(eval_model_path, device_map="auto")

    tea_tok = AutoTokenizer.from_pretrained(teacher_model)
    tea_mod = AutoModelForCausalLM.from_pretrained(teacher_model, device_map="auto")

    print("📗 Generating student answers ...")
    stu_ans = generate_answers(stu_mod, stu_tok, questions)
    print("📙 Generating teacher answers ...")
    tea_ans = generate_answers(tea_mod, tea_tok, questions)

    print("📈 Computing BLEU and ROUGE ...")
    bleu = load_metric("bleu")
    rouge = load_metric("rouge")

    bleu.add_batch(predictions=[p.split() for p in stu_ans], references=[[r.split()] for r in refs])
    rouge.add_batch(predictions=stu_ans, references=refs)
    stu_bleu = bleu.compute()
    stu_rouge = rouge.compute()

    bleu.add_batch(predictions=[p.split() for p in tea_ans], references=[[r.split()] for r in refs])
    rouge.add_batch(predictions=tea_ans, references=refs)
    tea_bleu = bleu.compute()
    tea_rouge = rouge.compute()

    out = {
        "student_bleu": stu_bleu,
        "student_rouge": stu_rouge,
        "teacher_bleu": tea_bleu,
        "teacher_rouge": tea_rouge
    }
    json.dump(out, open("data/final/eval_report.json", "w"), indent=2)
    print("✅ Evaluation complete → data/final/eval_report.json")

if __name__ == "__main__":
    main()
