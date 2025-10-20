"""
PromptKD Distillation Script (LfT - NIM Native)
-----------------------------------------------
This script performs Prompt-based Knowledge Distillation (PromptKD) using NVIDIA NIM models.

Process:
  1. Reads the knowledge-gap seed dataset (questions, reasoning, final answers)
  2. Uses two NIM models:
       - Teacher (e.g. meta/llama-3.1-70b-instruct)
       - Student (e.g. meta/llama-3.1-8b-instruct)
  3. Teacher rewrites answers clearly using reasoning
  4. Student attempts to answer the same question
  5. Saves teacher–student pairs → data/kd_generation/distilled.json
"""

import os
import json
import time
from tqdm import tqdm
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.messages import HumanMessage, SystemMessage
from scripts.utils import load_cfg


# -------------------------------------------------------------------------
# Teacher and Student Generation Functions
# -------------------------------------------------------------------------

def generate_teacher_output(teacher, question, answer, reasoning):
    """Ask the teacher to rewrite the answer using reasoning in a simple way."""
    messages = [
        SystemMessage(content="You are a patient, clear teacher who explains step-by-step."),
        HumanMessage(content=(
            f"Question: {question}\n\n"
            f"Provided Answer: {answer}\n\n"
            f"Reasoning Steps: {reasoning}\n\n"
            f"Now rewrite this clearly and pedagogically for a beginner student."
        )),
    ]
    response = teacher.invoke(messages)
    return response.content.strip()


def sample_student(student, question):
    """Ask the student model to attempt the same question."""
    messages = [HumanMessage(content=question)]
    response = student.invoke(messages)
    return response.content.strip()


# -------------------------------------------------------------------------
# Main Execution Function
# -------------------------------------------------------------------------

def main():
    # Create output directory
    os.makedirs("data/kd_generation", exist_ok=True)

    # Load NIM configuration
    cfg = load_cfg("configs/nim_config.yaml")
    api_key = cfg.get("NIM_API_KEY")

    teacher_model_id = cfg.get("TEACHER_MODEL")
    student_model_id = cfg.get("STUDENT_MODEL")

    print("🔗 Initializing NVIDIA NIM models...")
    teacher = ChatNVIDIA(model=teacher_model_id, api_key=api_key)
    student = ChatNVIDIA(model=student_model_id, api_key=api_key)

    # Load knowledge-gap dataset
    data_path = "data/raw/knowledge_gap_seed.json"
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"❌ Dataset not found at {data_path}")

    data = json.load(open(data_path))
    results = []

    print(f"🚀 Starting distillation for {len(data)} examples...\n")

    for ex in tqdm(data, desc="Distilling"):
        q = ex.get("question", "")
        a = ex.get("answer") or ex.get("final_answer", "")
        r = ex.get("answer_reasoning") or ex.get("chain_of_thought_reasoning", "")

        if not q:
            continue

        try:
            teacher_output = generate_teacher_output(teacher, q, a, r)
        except Exception as e:
            print(f"[WARN] Teacher generation failed: {e}")
            teacher_output = ""

        try:
            student_output = sample_student(student, q)
        except Exception as e:
            print(f"[WARN] Student generation failed: {e}")
            student_output = ""

        results.append({
            "topic": ex.get("topic", ""),
            "question": q,
            "teacher": teacher_output,
            "student": student_output
        })

        # Respect API rate limits slightly
        time.sleep(0.05)

    # Save results to JSON
    out_path = "data/kd_generation/distilled.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print("\n✅ Distillation completed successfully!")
    print(f"💾 Output saved to: {out_path}")
    print(f"📊 Total pairs generated: {len(results)}")


if __name__ == "__main__":
    main()
