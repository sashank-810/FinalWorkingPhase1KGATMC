# agents/explainer.py
from crewai import Agent
from config.settings import llm

explainer_agent = Agent(
    role="Simplification Agent",
    goal="Simplify academic content for better understanding",
    backstory="You are great at explaining complex topics in simple language.",
    llm=llm,
    allow_delegation=False,
    max_iter=1,
    verbose=True,
)