# crew/tools/mcq_tools.py

from pydantic import BaseModel, Field
from typing import List

# Define the structure for a single Multiple Choice Question
class MCQ(BaseModel):
    topic: str = Field(..., description="The specific topic of the question.")
    bloom_level: str = Field(..., description="The Bloom's Taxonomy level of the question.")
    question: str = Field(..., description="The question text, with LaTeX for math.")
    options: List[str] = Field(..., description="A list of 4 answer options.")
    correct_answer: str = Field(..., description="The correct answer from the options list.")
    rationale: str = Field(..., description="The explanation for the correct answer.")

# Define the structure for the list of MCQs, which is what the agent will return
class MCQList(BaseModel):
    """A list of multiple choice questions (MCQs) for a specific topic."""
    mcqs: List[MCQ]