# from crewai import Agent
# from config.settings import llm # Assuming you have this configured

# mcq_agent = Agent(
#     role="AI-Powered Educational Designer",
#     goal=(
#         "Create a comprehensive learning module from a given text, consisting of a conceptual learning path and a quiz "
#         "structured according to Bloom's Taxonomy."
#     ),
#     backstory=(
#         "You are an expert in instructional design and cognitive science, inspired by the work of Elkins et al. (2024). "
#         "You first map out the logical flow of topics in a document to create a clear learning path. Then, you craft "
#         "targeted multiple-choice questions for each level of Bloom's Taxonomy (Remembering, Understanding, Applying, "
#         "Analyzing, Evaluating, Creating) to ensure a deep and multi-faceted assessment of the material."
#     ),
#     llm=llm,
#     allow_delegation=False,
#     verbose=True,
# )

# Strategy and plan based generation
# # agents/mcq.py
# from crewai import Agent
# from config.settings import llm # Assuming llm is configured here

# mcq_generator_agent = Agent(
#     role="Multiple Choice Question Generator",
#     goal="Generate a challenging and clear multiple-choice question based on a given topic and its pedagogical rationale, ensuring plausible distractors and a single correct answer.",
#     backstory=(
#         "You are an expert in educational assessment, skilled at transforming learning objectives into effective evaluation tools. "
#         "Your questions are designed to test deep understanding, not just rote memorization. "
#         "You craft well-formed questions, plausible incorrect options (distractors), and clearly identify the correct answer, all while considering the intended teaching strategy."
#     ),
#     llm=llm,
#     allow_delegation=False,
#     verbose=True,
# )

# agents/mcq.py
from crewai import Agent
from config.settings import llm_2
from crew.tools.mcq_tools import MCQList # ✨ IMPORT THE TOOL

mcq_generator_agent = Agent(
    role="Multiple Choice Question Generator",
    goal="Generate a challenging and clear set of multiple-choice questions based on a given topic and its pedagogical rationale, ensuring plausible distractors and single correct answers for each question.",
    backstory=(
        "You are an expert in educational assessment, skilled at transforming learning objectives into effective evaluation tools. "
        "Your questions are designed to test deep understanding, not just rote memorization. "
        "You craft well-formed questions, plausible incorrect options (distractors), and clearly identify the correct answer, all while considering the intended teaching strategy."
    ),
    llm=llm_2,
    allow_delegation=False,
    verbose=True,
    # ✨ FORCE THE AGENT TO USE THE TOOL FOR ITS FINAL OUTPUT
    output_pydantic=MCQList 
)