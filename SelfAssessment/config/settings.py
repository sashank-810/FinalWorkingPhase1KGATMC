import os
import streamlit as st
from langchain_nvidia_ai_endpoints import ChatNVIDIA

# --- NVIDIA API Configuration ---
# IMPORTANT: Paste your NVIDIA API key here. It will be used for all models.
NVIDIA_API_KEY = "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"
os.environ["NVIDIA_API_KEY"] = NVIDIA_API_KEY
os.environ["NVIDIA_NIM_API_KEY"] = NVIDIA_API_KEY
# --- Main "Teacher" LLM Client (Kimi K2 Instruct) ---
main_llm = ChatNVIDIA(
    model="moonshotai/kimi-k2-instruct-0905",
    temperature=0.2,
    max_tokens=16392,
    top_p=0.7,
)

student_llm = ChatNVIDIA(
    model="meta/llama-3.1-8b-instruct",
    temperature=0.1,
    max_tokens=1024,
    top_p=0.7,
)

# Assign the main client to your crew agents
llm = main_llm
llm_1, llm_2, llm_3, llm_4 = llm, llm, llm, llm
