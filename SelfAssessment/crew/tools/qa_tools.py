# crew/tools/qa_tools.py

from pydantic import BaseModel, Field

class QuestionAnswer(BaseModel):
    """A single question, its correct answer, and the rationale behind it."""
    topic: str = Field(..., description="The original topic for the question.")
    bloom_level: str = Field(..., description="The Bloom's Taxonomy level.")
    question: str = Field(..., description="The generated question text.")
    correct_answer: str = Field(..., description="The correct answer to the question.")
    rationale: str = Field(..., description="The pedagogical rationale for this question and answer.")