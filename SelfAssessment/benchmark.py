# benchmark.py (Final Version - Simplified & Correct)

# --- Force Telemetry OFF for ALL libraries at the very start ---
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
trace.set_tracer_provider(TracerProvider())

# --- Load API keys from the .env file ---
from dotenv import load_dotenv
load_dotenv()

import os
import torch
import evaluate
import traceback
from transformers import pipeline
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq

# --- Define the LLM directly ---
llm = None
try:
    if os.getenv("GROQ_API_KEY"):
        llm = ChatGroq(
            model="llama3-8b-8192",
            api_key=os.getenv("GROQ_API_KEY")
        )
        print("✅ LLM configured directly with Groq Llama 3.")
    else:
        print("❌ CRITICAL: GROQ_API_KEY not found in .env file or environment.")
except Exception as e:
    print(f"❌ CRITICAL: Could not initialize LLM. Error: {e}")


# --- Configuration ---
SOURCE_TEXT = """
The solar system is a gravitationally bound system of the Sun and the objects that orbit it, either directly or indirectly. Of the objects that orbit the Sun directly, the largest are the eight planets, with the remainder being smaller objects, the dwarf planets and small Solar System bodies. Of the objects that orbit the Sun indirectly—the natural satellites—two are larger than the smallest planet, Mercury.

The solar system formed 4.6 billion years ago from the gravitational collapse of a giant interstellar molecular cloud. The vast majority of the system's mass is in the Sun, with most of the remaining mass contained in Jupiter. The four smaller inner planets, Mercury, Venus, Earth and Mars, are terrestrial planets, being primarily composed of rock and metal. The four outer planets are giant planets, being substantially more massive than the terrestrials. The two largest planets, Jupiter and Saturn, are gas giants, being composed mainly of hydrogen and helium; the two outermost planets, Uranus and Neptune, are ice giants, being composed mostly of substances with relatively high melting points compared with hydrogen and helium, called volatiles, such as water, ammonia and methane. All eight planets have almost circular orbits that lie within a nearly flat disc called the ecliptic.
"""
REFERENCE_SUMMARY = "The solar system, formed 4.6 billion years ago, consists of the Sun and orbiting objects. Most of the system's mass is the Sun, followed by Jupiter. It has four terrestrial inner planets (Mercury, Venus, Earth, Mars) made of rock and metal, and four giant outer planets. The two largest, Jupiter and Saturn, are gas giants, while the two furthest, Uranus and Neptune, are ice giants composed of volatiles."


# --- Model Definitions ---
def get_crewai_summarizer(text):
    if not llm:
        raise ValueError("LLM not initialized. Cannot run CrewAI agent.")
    summarizer_agent = Agent(
        role="Summarization Expert",
        goal="Summarize academic and technical documents efficiently.",
        backstory="You specialize in extracting the most critical information from complex content.",
        allow_delegation=False, llm=llm, verbose=True
    )
    task = Task(
        description=f"Summarize the key points of the following document:\n\n---\n{text}\n---",
        expected_output="A concise and easy-to-read summary of the document.", agent=summarizer_agent
    )
    crew = Crew(tasks=[task], agents=[summarizer_agent])
    result = crew.kickoff()
    if isinstance(result, str): return result
    if hasattr(result, 'raw'): return result.raw
    return f"CrewAI failed to produce a valid summary. Result: {result}"

def get_huggingface_summarizer(model_name):
    print(f"Loading model: {model_name}...")
    summarizer = pipeline("summarization", model=model_name, device=0 if torch.cuda.is_available() else -1)
    return summarizer

# --- Main Benchmark Logic ---
def run_benchmark():
    rouge, bertscore = evaluate.load('rouge'), evaluate.load('bertscore')
    models_to_test = {
        "Your CrewAI Agent (Llama 3 on Groq)": None,
        "t5-base (Local)": "t5-base",
        "bart-large-cnn (Local)": "facebook/bart-large-cnn",
    }
    results = {}
    print("\n--- Starting Summarization Benchmark ---")
    print(f"Reference Summary:\n'{REFERENCE_SUMMARY}'\n")

    for name, model_path in models_to_test.items():
        print(f"--- Testing Model: {name} ---")
        try:
            if "CrewAI" in name:
                if not llm or not os.getenv("GROQ_API_KEY"):
                    raise ValueError("Skipping CrewAI Agent because Groq LLM/API key is not configured.")
                generated_summary = get_crewai_summarizer(SOURCE_TEXT)
            else:
                summarizer_pipeline = get_huggingface_summarizer(model_path)
                output = summarizer_pipeline(SOURCE_TEXT, max_length=100, min_length=30, do_sample=False)
                generated_summary = output[0]['summary_text']
            
            print(f"Generated Summary:\n'{generated_summary}'\n")
            rouge_scores = rouge.compute(predictions=[generated_summary], references=[REFERENCE_SUMMARY])
            bert_scores = bertscore.compute(predictions=[generated_summary], references=[REFERENCE_SUMMARY], lang="en")
            results[name] = {"summary": generated_summary, "rougeL": round(rouge_scores['rougeL'], 4), "bert_f1": round(bert_scores['f1'][0], 4)}
        
        except Exception as e:
            print(f"\n--- A REAL ERROR OCCURRED IN MODEL: {name} ---")
            traceback.print_exc()
            print("--------------------------------------------------\n")
            results[name] = {"summary": "Error", "rougeL": 0, "bert_f1": 0}

    print("\n--- Benchmark Results ---")
    print(f"{'Model':<40} | {'ROUGE-L (Overlap)':<20} | {'BERTScore F1 (Semantic)':<25}")
    print("-" * 90)
    for name, scores in results.items():
        print(f"{name:<40} | {scores['rougeL']:<20} | {scores['bert_f1']:<25}")

if __name__ == "__main__":
    run_benchmark()