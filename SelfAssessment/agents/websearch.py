# agents/websearch.py
from crewai import Agent
from config.settings import llm

web_research_agent = Agent(
    role="Web Research Assistant",
    goal="Search the internet to gather supplementary information related to the academic topic.",
    backstory=(
        "You are a digital research assistant with access to real-time web tools. "
        "Your goal is to enhance academic topics by finding relevant articles, blogs, documentation, and real-world examples "
        "to give students broader context and deeper understanding."
    ),
    llm=llm,
    allow_delegation=False,
    verbose=True,
)