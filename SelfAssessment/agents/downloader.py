# agents/downloader.py
from crewai import Agent
from core.tools import download_pdf_tool
from config.settings import llm

download_agent = Agent(
    role="Download Manager",
    goal="Download the final_output.pdf file to the user's device",
    backstory="You are responsible for handling the download of files. You don't use any language model — just ensure the user gets the file.",
    tools=[download_pdf_tool],
    llm=llm,
    allow_delegation=False,
    verbose=True,
)