# agents/summarizer.py
from crewai import Agent
from config.settings import llm

summarizer_agent = Agent(
    role="Summarization Expert",
    goal="Summarize academic PDFs efficiently",
    backstory="You specialize in extracting summaries from technical content.",
    llm=llm,
    allow_delegation=False,
    verbose=True,
)