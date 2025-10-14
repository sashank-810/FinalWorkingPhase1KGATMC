# import os
# import streamlit as st
# import torch
# from langchain_openai import ChatOpenAI
# from transformers import pipeline
# from langchain_huggingface import HuggingFacePipeline # Import the wrapper

# # --- Main vLLM Client Configuration ---
# OPENAI_API_KEY = "not-needed" 
# OPENAI_API_BASE = "http://localhost:8000/v1"
# MODEL_NAME = "huggingface/cpatonn/Qwen3-30B-A3B-Thinking-2507-AWQ-4bit" # Or your AWQ version
# SERPER_API_KEY = "" 

# os.environ["SERPER_API_KEY"] = SERPER_API_KEY

# main_llm = ChatOpenAI(
#     model=MODEL_NAME, 
#     base_url=OPENAI_API_BASE, 
#     api_key=OPENAI_API_KEY
# )

# # Assign this client to your main agents
# llm = main_llm
# llm_1 = main_llm
# llm_2 = main_llm
# llm_3 = main_llm
# llm_4 = main_llm


# # --- Custom Local LLM for AI Quiz Taker ---

# @st.cache_resource(show_spinner="Loading Qwen-4B model (this can take a moment)...")
# def load_qwen_4b_pipeline():
#     """Loads and caches the local Qwen-4B model pipeline."""
#     pipe = pipeline(
#         "text-generation",
#         model="Qwen/Qwen3-4B-Thinking-2507",
#         torch_dtype=torch.bfloat16,
#         device_map="auto"
#     )
#     # FIXED: Wrap the pipeline in the LangChain object that crewai expects
#     return HuggingFacePipeline(pipeline=pipe)

# # FIXED: Actually call the function to load and cache the pipeline.
# # Note the parentheses () at the end.
# llm_hf_pipeline = load_qwen_4b_pipeline()

import os
import streamlit as st
import torch
from langchain_openai import ChatOpenAI
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer # FIXED: Added missing import
from langchain_huggingface import HuggingFacePipeline
from peft import PeftModel
from langchain_nvidia_ai_endpoints import ChatNVIDIA


# --- Hugging Face Token Configuration ---
# IMPORTANT: Paste your Hugging Face token here.
# This is required to download models from the Hub.
HUGGING_FACE_HUB_TOKEN = "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"
os.environ["HUGGING_FACE_HUB_TOKEN"] = HUGGING_FACE_HUB_TOKEN


NVIDIA_API_KEY = "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"
os.environ["NVIDIA_NIM_API_KEY"] = NVIDIA_API_KEY
main_llm = ChatNVIDIA(
    model="qwen/qwen3-235b-a22b",
    max_tokens=16384
    )

# Assign this client to your main agents
llm = main_llm
llm_1, llm_2, llm_3, llm_4 = llm, llm, llm, llm

# --- Original AI Quiz Taker (Qwen-4B Base Model) ---
@st.cache_resource(show_spinner="Loading Llama-8B model...")
def student_pipeline():
    pipe = pipeline("text-generation", model="meta-llama/Llama-3.1-8B", dtype=torch.bfloat16, device_map="auto")
    return pipe
llm_hf_pipeline = student_pipeline()

# # --- NEW: Fine-tuned AI Quiz Taker (from local directory) ---
# @st.cache_resource(show_spinner="Loading your fine-tuned model...")
# def load_finetuned_pipeline():
#     """Loads the base model and applies your fine-tuned adapter weights."""
#     base_model_id = "Qwen/Qwen3-4B-Thinking-2507"
#     adapter_path = "/home/resiliente2003/vishnu/KGAFT/results_qwen4b_finetuned3/final_model"
    
#     base_model = AutoModelForCausalLM.from_pretrained(base_model_id, torch_dtype=torch.bfloat16, device_map="auto")
#     model = PeftModel.from_pretrained(base_model, adapter_path)
#     tokenizer = AutoTokenizer.from_pretrained(adapter_path)
    
#     pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
#     return pipe

# llm_finetuned_pipeline = load_finetuned_pipeline()