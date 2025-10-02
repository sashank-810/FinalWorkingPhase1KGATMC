from crewai import Agent
from config.settings import llm_2 # Import the function

def one_shot_distractor_agent():
    return Agent(
        role="Expert Assessment Creator",
        goal="""For a given question and correct answer, generate three final, high-quality, and plausible incorrect options (distractors).
        Internally, you must first brainstorm potential distractors, critically evaluate them for plausibility and fairness, and then refine them into a final list.
        The final output must be only a single JSON list of the three refined distractor strings.""",
        backstory="""You are a highly efficient and experienced educational content designer. You have a deep understanding of pedagogy and cognitive biases, allowing you to mentally simulate a multi-step quality assurance process in a single, fluid workflow. 
        You excel at creating challenging but fair test questions by first generating ideas, then immediately critiquing and refining them to produce a polished, final product without needing external feedback.""",
        llm=get_llm(), # Call the function to get an LLM from the pool
        allow_delegation=False,
        verbose=True
    )