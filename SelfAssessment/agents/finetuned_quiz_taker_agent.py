from crewai import Agent
from config.settings import llm_finetuned # Import the new fine-tuned LLM

finetuned_quiz_taker_agent = Agent(
    role="Specialized Fine-tuned Quiz Taker",
    goal="""Analyze and answer a multiple-choice question based on the specific knowledge from your fine-tuning dataset.""",
    backstory="""You are an AI model that has undergone specialized training on a curated dataset of questions and answers. Your purpose is to leverage this training to answer questions with high accuracy, demonstrating the knowledge gained during the fine-tuning process.""",
    llm=llm_finetuned,
    allow_delegation=False,
    verbose=True
)