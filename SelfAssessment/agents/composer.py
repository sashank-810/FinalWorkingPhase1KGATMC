# agents/composer.py
from crewai import Agent
from config.settings import llm

composer_agent = Agent(
    role="Final Composer",
    goal=(
        "Take the outputs from the summary, notes, MCQs, simplification, YouTube, and web search agents, "
        "and combine them into a single structured markdown report. Do not call any tools."
    ),
    backstory=(
        "You are skilled at organizing and formatting diverse content into a clean, readable study guide. "
        "You will use the provided outputs and combine them into a single markdown document."
    ),
    llm=llm,
    allow_delegation=False,
    verbose=True,
)