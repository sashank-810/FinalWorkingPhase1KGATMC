# agents/youtube.py
from crewai import Agent
from config.settings import llm

youtube_finder_agent = Agent(
    role="YouTube Search Agent",
    goal="Find the best educational videos related to the given topic.",
    backstory=(
        "You help students by finding relevant and high-quality educational videos on YouTube. "
        "You return short descriptions along with links that will help explain the topic in audio-visual form."
    ),
    llm=llm,
    allow_delegation=False,
    verbose=True,
)