# agents/qa_generator.py
from crewai import Agent
from config.settings import llm

# This agent's role is to generate the initial question and its correct answer.
qa_generator_agent = Agent(
    role="Question and Answer Generation Specialist",
    goal="Generate a clear, challenging question for a specific topic and provide the single correct answer, along with a rationale.",
    backstory=(
        "You are an expert in curriculum design, focusing on crafting precise questions that test a student's core understanding."
    ),
    llm=llm,
    allow_delegation=False,
    verbose=True
)