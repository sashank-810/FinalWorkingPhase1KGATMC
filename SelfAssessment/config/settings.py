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

# --- Hugging Face Token Configuration ---
# IMPORTANT: Paste your Hugging Face token here.
# This is required to download models from the Hub.
HUGGING_FACE_HUB_TOKEN = "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"
os.environ["HUGGING_FACE_HUB_TOKEN"] = HUGGING_FACE_HUB_TOKEN


# --- Main vLLM Client Configuration ---
OPENAI_API_KEY = "EMPTY"
OPENAI_API_BASE = "http://localhost:8000/v1"
MODEL_NAME = "Valdemardi/DeepSeek-R1-Distill-Llama-70B-AWQ"
SERPER_API_KEY = "" 

# Set the environment variables so all libraries can see them
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["OPENAI_API_BASE"] = OPENAI_API_BASE
os.environ["SERPER_API_KEY"] = SERPER_API_KEY

# This client will now work, as will any hidden clients created by your libraries
main_llm = ChatOpenAI(
    model=MODEL_NAME, 
    base_url=OPENAI_API_BASE, 
    api_key=OPENAI_API_KEY
)

# Assign this client to your main agents
llm = main_llm
llm_1 = main_llm
llm_2 = main_llm
llm_3 = main_llm
llm_4 = main_llm

# --- Original AI Quiz Taker (Qwen-4B Base Model) ---
@st.cache_resource(show_spinner="Loading Qwen-4B model...")
def load_qwen_4b_pipeline():
    pipe = pipeline("text-generation", model="Qwen/Qwen3-4B-Thinking-2507", dtype=torch.bfloat16, device_map="auto")
    return pipe
llm_hf_pipeline = load_qwen_4b_pipeline()

# --- NEW: Fine-tuned AI Quiz Taker (from local directory) ---
@st.cache_resource(show_spinner="Loading your fine-tuned model...")
def load_finetuned_pipeline():
    """Loads the base model and applies your fine-tuned adapter weights."""
    base_model_id = "Qwen/Qwen3-4B-Thinking-2507"
    adapter_path = "/home/resiliente2003/vishnu/KGAFT/results_qwen4b_finetuned3/final_model"
    
    base_model = AutoModelForCausalLM.from_pretrained(base_model_id, torch_dtype=torch.bfloat16, device_map="auto")
    model = PeftModel.from_pretrained(base_model, adapter_path)
    tokenizer = AutoTokenizer.from_pretrained(adapter_path)
    
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
    return pipe

llm_finetuned_pipeline = load_finetuned_pipeline()