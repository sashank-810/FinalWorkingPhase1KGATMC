from crewai import Agent
from config.settings import llm_hf_pipeline # Import the Hugging Face LLM

quiz_taker_agent = Agent(
    role="Expert Quiz Taker",
    goal="""Analyze a given multiple-choice question and its options, and determine the most likely correct answer. 
    Your final answer must be only the full text of the chosen option, with no extra commentary or preamble.""",
    backstory="""You are a highly knowledgeable and analytical AI. You are designed to understand and answer questions across various domains by carefully reading the question and evaluating the provided options to find the single best fit.""",
    llm=llm_hf_pipeline,
    allow_delegation=False,
    verbose=True
)