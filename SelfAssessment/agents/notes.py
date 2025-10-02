# agents/notes.py
from crewai import Agent
from config.settings import llm

notes_agent = Agent(
    role="Note Making Assistant",
    goal="Generate clear and concise notes for revision",
    backstory="You turn complex PDFs into easy notes for students.",
    llm=llm,
    allow_delegation=False,
    verbose=True,
)