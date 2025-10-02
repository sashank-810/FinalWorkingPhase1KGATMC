# # crew/crew_factory.py (Final, Final Corrected Version) for pdfs

# from crewai import Task, Crew, Agent
# from agents.summarizer import summarizer_agent
# from agents.notes import notes_agent
# from agents.mcq import mcq_agent
# from agents.explainer import explainer_agent
# from agents.websearch import web_research_agent
# from agents.youtube import youtube_finder_agent

# # Import the new tool classes
# from core.tools import RAGQueryTool, WebSearchTool, YouTubeSearchTool
# from core.prompts import SUMMARY_PROMPT, NOTES_PROMPT, MCQ_PROMPT, EXPLAIN_PROMPT

# def get_crew(module: str, vector_index):
    
#     tools_map = {
#         "Summarization": RAGQueryTool(name="Summarizer", description="Summarizes PDF content", vector_index=vector_index, prompt_template=SUMMARY_PROMPT),
#         "Notes": RAGQueryTool(name="NoteMaker", description="Generates bullet-point notes", vector_index=vector_index, prompt_template=NOTES_PROMPT),
#         "MCQs": RAGQueryTool(name="MCQGenerator", description="Creates multiple-choice questions", vector_index=vector_index, prompt_template=MCQ_PROMPT),
#         "Explanation": RAGQueryTool(name="Simplifier", description="Simplifies complex content", vector_index=vector_index, prompt_template=EXPLAIN_PROMPT),
#         "Web Search": WebSearchTool(vector_index=vector_index),
#         "YouTube": YouTubeSearchTool(vector_index=vector_index)
#     }
    
#     task_map = {
#         "Summarization": {"description": "Summarize the document.", "expected_output": "A concise summary.", "agent": summarizer_agent},
#         "Notes": {"description": "Create revision notes.", "expected_output": "Detailed, bulleted notes.", "agent": notes_agent},
#         "MCQs": {"description": "Generate MCQs.", "expected_output": "A list of multiple-choice questions with answers.", "agent": mcq_agent},
#         "Explanation": {"description": "Explain complex topics simply.", "expected_output": "A simple explanation.", "agent": explainer_agent},
#         "Web Search": {"description": "Find related web resources.", "expected_output": "A list of topics and relevant links.", "agent": web_research_agent},
#         "YouTube": {"description": "Find related YouTube videos.", "expected_output": "A list of topics and YouTube links.", "agent": youtube_finder_agent}
#     }

#     task_details = task_map.get(module)
#     tool = tools_map.get(module)

#     if not task_details or not tool:
#         raise ValueError(f"Invalid module selected: {module}")

#     task = Task(
#         description=task_details["description"],
#         expected_output=task_details["expected_output"],
#         agent=task_details["agent"],
#         tools=[tool]
#     )

#     return Crew(
#         tasks=[task],
#         agents=[task_details["agent"]],
#         verbose=True # Corrected from '2' to 'True'
#     )



# # crew/crew_factory.py (Modified for MCQ Formatting)
# # crew/crew_factory.py

# from crewai import Task, Crew, Agent
# from agents.summarizer import summarizer_agent
# from agents.notes import notes_agent
# from agents.mcq import mcq_agent
# from agents.explainer import explainer_agent

# # --- THIS IS THE FIRST CHANGE: Update the function signature ---
# def get_crew(module: str, markdown_text: str, num_mcqs: int = 5): # Default value is 5
    
#     agents = {
#         "Summarization": summarizer_agent,
#         "Notes": notes_agent,
#         "MCQs": mcq_agent,
#         "Explanation": explainer_agent,
#     }

#     task_definitions = {
#         "Summarization": {
#             "description": f"Summarize the key points and main arguments of the following document:\n\n---\n{markdown_text}\n---",
#             "expected_output": "A concise and easy-to-read summary of the document.",
#         },
#         "Notes": {
#             "description": f"Analyze the following document and create detailed, structured revision notes in bullet-point format:\n\n---\n{markdown_text}\n---",
#             "expected_output": "Well-organized, hierarchical notes that are perfect for studying.",
#         },
#         "MCQs": {
#             # --- THIS IS THE SECOND CHANGE: Use the num_mcqs variable in the prompt ---
#             "description": f"""
# Generate exactly {num_mcqs} multiple-choice questions based on the document provided below.
# **Crucially, you MUST follow the formatting instructions in the 'expected_output' precisely.**
# Each question, its options, and its explanation MUST be formatted as shown in the example.

# --- DOCUMENT ---
# {markdown_text}
# --- END DOCUMENT ---
# """,
#             "expected_output": """
# A numbered list of multiple-choice questions.
# - Each question must be followed by four options (a, b, c, d), each on its own new line.
# - You MUST mark the single correct option by starting its line with a star (*).
# - You MUST provide a brief, one-sentence explanation for why the answer is correct, prefixed with 'Explanation:'.

# **EXAMPLE FORMAT:**

# 1. What is the capital of France?
# a) London
# *b) Paris
# c) Berlin
# d) Madrid
# Explanation: Paris is the capital and largest city of France.

# 2. What is 2 + 2?
# *a) 4
# b) 3
# c) 5
# d) 6
# Explanation: This is a fundamental arithmetic operation.
# """,
#         },
#         "Explanation": {
#             "description": f"Take the complex topics in the following document and explain them in simple, easy-to-understand terms:\n\n---\n{markdown_text}\n---",
#             "expected_output": "A simplified explanation of the core concepts, suitable for a beginner.",
#         }
#     }

#     task_details = task_definitions.get(module)
#     agent = agents.get(module)

#     if not task_details or not agent:
#         raise ValueError(f"Invalid module selected: {module}")

#     task = Task(
#         description=task_details["description"],
#         expected_output=task_details["expected_output"],
#         agent=agent,
#     )

#     return Crew(
#         tasks=[task],
#         agents=[agent],
#         verbose=True
#     )

# crew/crew_factory.py (difficulty)

# from crewai import Task, Crew, Agent
# from agents.summarizer import summarizer_agent
# from agents.notes import notes_agent
# from agents.mcq import mcq_agent
# from agents.explainer import explainer_agent

# # --- CHANGE #1: Update the function signature to accept difficulty ---
# def get_crew(module: str, markdown_text: str, num_mcqs: int = 5, difficulty: str = "Medium"):
    
#     agents = {
#         "Summarization": summarizer_agent,
#         "Notes": notes_agent,
#         "MCQs": mcq_agent,
#         "Explanation": explainer_agent,
#     }

#     task_definitions = {
#         "Summarization": {
#             "description": f"Summarize the key points and main arguments of the following document:\n\n---\n{markdown_text}\n---",
#             "expected_output": "A concise and easy-to-read summary of the document.",
#         },
#         "Notes": {
#             "description": f"Analyze the following document and create detailed, structured revision notes in bullet-point format:\n\n---\n{markdown_text}\n---",
#             "expected_output": "Well-organized, hierarchical notes that are perfect for studying.",
#         },
#         "MCQs": {
#             # --- CHANGE #2: Inject the difficulty into the prompt ---
#             "description": f"""
# Generate exactly {num_mcqs} multiple-choice questions of **{difficulty}** difficulty based on the document provided below.
# **Crucially, you MUST follow the formatting instructions in the 'expected_output' precisely.**
# Each question, its options, and its explanation MUST be formatted as shown in the example.

# --- DOCUMENT ---
# {markdown_text}
# --- END DOCUMENT ---
# """,
#             "expected_output": """
# A numbered list of multiple-choice questions.
# - Each question must be followed by four options (a, b, c, d), each on its own new line.
# - You MUST mark the single correct option by starting its line with a star (*).
# - You MUST provide a brief, one-sentence explanation for why the answer is correct, prefixed with 'Explanation:'.

# **EXAMPLE FORMAT:**

# 1. What is the capital of France?
# a) London
# *b) Paris
# c) Berlin
# d) Madrid
# Explanation: Paris is the capital and largest city of France.

# 2. What is 2 + 2?
# *a) 4
# b) 3
# c) 5
# d) 6
# Explanation: This is a fundamental arithmetic operation.
# """,
#         },
#         "Explanation": {
#             "description": f"Take the complex topics in the following document and explain them in simple, easy-to-understand terms:\n\n---\n{markdown_text}\n---",
#             "expected_output": "A simplified explanation of the core concepts, suitable for a beginner.",
#         }
#     }

#     task_details = task_definitions.get(module)
#     agent = agents.get(module)

#     if not task_details or not agent:
#         raise ValueError(f"Invalid module selected: {module}")

#     task = Task(
#         description=task_details["description"],
#         expected_output=task_details["expected_output"],
#         agent=agent,
#     )

#     return Crew(
#         tasks=[task],
#         agents=[agent],
#         verbose=True
#     )



# # Knowledge Graph

# from crewai import Task, Crew, Agent
# from agents.summarizer import summarizer_agent
# from agents.notes import notes_agent
# from agents.mcq import mcq_agent
# from agents.explainer import explainer_agent
# from agents.knowledge_graph import knowledge_graph_agent

# def get_crew(module: str, markdown_text: str, num_mcqs: int = 5, difficulty: str = "Medium"):
    
#     agents = {
#         "Summarization": summarizer_agent, "Notes": notes_agent,
#         "MCQs": mcq_agent, "Explanation": explainer_agent,
#         "Knowledge Graph": knowledge_graph_agent,
#     }
    
#     difficulty_instructions = {
#         "Easy": "focus on direct, factual recall questions from the text.",
#         "Medium": "focus on questions that require understanding and application of concepts.",
#         "Hard": "focus on questions that require synthesis, analysis, or evaluation of the information."
#     }

#     task_definitions = {
#         "Summarization": {
#             "description": f"Summarize the key points of the document below.\n\n---\n{markdown_text}\n---",
#             "expected_output": "A concise, easy-to-read summary.",
#         },
#         "Notes": {
#             "description": f"Create detailed, structured revision notes from the document below.\n\n---\n{markdown_text}\n---",
#             "expected_output": "Well-organized, hierarchical notes perfect for studying.",
#         },
#         "MCQs": {
#             "description": f"""
# Generate exactly {num_mcqs} multiple-choice questions of **{difficulty}** difficulty based on the document below.
# When creating the questions, {difficulty_instructions[difficulty]}
# **Crucially, you MUST follow the formatting instructions in the 'expected_output' precisely.**
# --- DOCUMENT ---
# {markdown_text}
# --- END DOCUMENT ---
# """,
#             "expected_output": """
# A numbered list of questions. Each question must have four options (a, b, c, d) on new lines.
# You MUST mark the correct option by starting its line with a star (*).
# You MUST provide a brief explanation for the answer, prefixed with 'Explanation:'.
# **EXAMPLE FORMAT:**
# 1. What is the capital of France?
# a) London
# *b) Paris
# c) Berlin
# d) Madrid
# Explanation: Paris is the capital and largest city of France.
# """,
#         },
#         "Explanation": {
#             "description": f"Explain the complex topics in the document below in simple terms.\n\n---\n{markdown_text}\n---",
#             "expected_output": "A simplified explanation of the core concepts.",
#         },
#         "Knowledge Graph": {
#             "description": f"""
# Analyze the document to create a curriculum flowchart showing the logical order to learn the topics.
# The final output MUST be only a valid flowchart in Graphviz DOT language, starting with `digraph LearningPath {{` and ending with `}}`.
# --- DOCUMENT ---
# {markdown_text}
# --- END DOCUMENT ---
# """,
#             "expected_output": """
# A string containing ONLY the Graphviz DOT language code.
# **EXAMPLE OF THE ONLY VALID OUTPUT FORMAT:**
# digraph LearningPath {
#   rankdir="TB";
#   node [shape=box, style=rounded];
#   A [label="Introduction"]; B [label="Core Concept"]; C [label="Advanced Topic"];
#   A -> B -> C;
# }
# """,
#         },
#     }

#     task_details = task_definitions.get(module)
#     agent = agents.get(module)
#     if not task_details or not agent:
#         raise ValueError(f"Invalid module selected: {module}")

#     task = Task(description=task_details["description"], expected_output=task_details["expected_output"], agent=agent)
#     return Crew(tasks=[task], agents=[agent], verbose=True)

# Planner

# # crew/crew_factory.py

# from crewai import Task, Crew, Agent, Process
# from agents.summarizer import summarizer_agent
# from agents.notes import notes_agent
# from agents.explainer import explainer_agent
# from agents.planner import planner_agent
# from agents.critic import critic_agent
# from agents.refiner import refiner_agent
# from agents.knowledge_graph import knowledge_graph_agent

# def get_crew(module: str, markdown_text: str):
    
#     # --- This block handles the "Strategic Plan" workflow ---
#     if module == "Strategic Plan":
        
#         task_plan = Task(
#             description=f"""
# Analyze the document below and create a comprehensive pedagogical plan.
# 1.  Identify every distinct topic and sub-topic.
# 2.  For each topic, you must provide scores for 'relevance' and 'completeness' based on the strict rubric in the expected output.
# 3.  For each topic, devise a draft 'teaching_strategy' and a draft 'rationale' explaining it.

# --- DOCUMENT ---
# {markdown_text}
# --- END DOCUMENT ---
# """,
#             expected_output="""
# A single JSON list of objects. The output MUST be only the raw JSON.
# Each object MUST contain 'topic', 'relevance', 'completeness', 'teaching_strategy', and 'rationale'.

# **STRICT SCORING RUBRIC:**
# Relevance (1-5): 1-Trivial, 2-Peripheral, 3-Supporting, 4-Core, 5-Foundational.
# Completeness (1-5): 1-Hinted, 2-Mentioned, 3-Sufficient, 4-Thorough, 5-Exhaustive.

# **EXAMPLE FORMAT:**
# [
#   {
#     "topic": "Definition of a Complex Number",
#     "relevance": 5,
#     "completeness": 5,
#     "teaching_strategy": "Start with the equation x^2 = -1 to motivate the need for 'i', then introduce the a+ib form.",
#     "rationale": "This contextual approach enhances student engagement."
#   }
# ]
# """,
#             agent=planner_agent
#         )

#         task_critique = Task(
#             description="Rigorously critique the received JSON teaching plan. Evaluate scores, strategies, and rationales.",
#             expected_output="A bulleted list of specific, actionable critiques for the strategic plan.",
#             agent=critic_agent,
#             context=[task_plan]
#         )

#         task_refine_plan = Task(
#             description="Take the draft teaching plan and the critiques. Produce a final, perfected JSON plan, including a 'refined_rationale' for each item.",
#             expected_output="The final, polished JSON list of objects, incorporating all feedback.",
#             agent=refiner_agent,
#             context=[task_plan, task_critique]
#         )

#         crew = Crew(
#             agents=[planner_agent, critic_agent, refiner_agent],
#             tasks=[task_plan, task_critique, task_refine_plan],
#             process=Process.sequential,
#             verbose=True
#         )
#         return crew, None

#     # --- This block handles all other single-agent modules, including the Knowledge Graph ---
#     else:
#         agents = {
#             "Summarization": summarizer_agent,
#             "Notes": notes_agent,
#             "Explanation": explainer_agent,
#             "Knowledge Graph": knowledge_graph_agent,
#         }
#         task_definitions = {
#             "Summarization": {
#                 "description": f"Summarize the document.\n\n---\n{markdown_text}\n---",
#                 "expected_output": "A concise summary.",
#             },
#             "Notes": {
#                 "description": f"Create revision notes.\n\n---\n{markdown_text}\n---",
#                 "expected_output": "Well-organized notes.",
#             },
#             "Explanation": {
#                 "description": f"Explain the topics simply.\n\n---\n{markdown_text}\n---",
#                 "expected_output": "A simple explanation.",
#             },
#             "Knowledge Graph": {
#                 "description": f"""
# You are an expert curriculum designer. Your task is to create a high-level, easy-to-follow learning path flowchart from the provided document.
# Focus on major topics and group minor concepts. Use short, clear labels.
# The final output MUST be only a valid Graphviz DOT language code.

# --- DOCUMENT ---
# {markdown_text}
# --- END DOCUMENT ---
# """,
#                 "expected_output": """
# A string containing ONLY the Graphviz DOT language code.
# **EXAMPLE FORMAT:**
# digraph LearningPath {
#   rankdir="TB";
#   node [shape=box, style="rounded,filled", fillcolor="#aaffaa"];
#   A [label="Introduction"];
#   B [label="Core Concepts"];
#   C [label="Advanced Topics"];
#   A -> B -> C;
# }
# """,
#             },
#         }

#         agent = agents.get(module)
#         task_details = task_definitions.get(module)
        
#         if not agent or not task_details:
#             raise ValueError(f"Invalid module selected: {module}")

#         task = Task(description=task_details["description"], expected_output=task_details["expected_output"], agent=agent)
        
#         return Crew(tasks=[task], agents=[agent], verbose=True), None

# Planner based questions
# # crew/crew_factory.py

# from crewai import Task, Crew, Agent, Process
# from agents.summarizer import summarizer_agent
# from agents.notes import notes_agent
# from agents.explainer import explainer_agent
# from agents.planner import planner_agent
# from agents.critic import critic_agent
# from agents.refiner import refiner_agent
# from agents.knowledge_graph import knowledge_graph_agent
# from agents.mcq import mcq_generator_agent # Import the new agent

# def get_crew(module: str, input_data: str, difficulty: str = None):
    
#     # --- This block handles the "Strategic Plan" workflow ---
#     if module == "Strategic Plan":
#         markdown_text = input_data # Rename for clarity within this block
#         task_plan = Task(
#             description=f"""
# Analyze the document below and create a comprehensive pedagogical plan.
# 1.  Identify every distinct topic and sub-topic.
# 2.  For each topic, you must provide scores for 'relevance' and 'completeness' based on the strict rubric in the expected output.
# 3.  For each topic, devise a draft 'teaching_strategy' and a draft 'rationale' explaining it.

# --- DOCUMENT ---
# {markdown_text}
# --- END DOCUMENT ---
# """,
#             expected_output="""
# A single JSON list of objects. The output MUST be only the raw JSON.
# Each object MUST contain 'topic', 'relevance', 'completeness', 'teaching_strategy', and 'rationale'.

# **STRICT SCORING RUBRIC:**
# Relevance (1-5): 1-Trivial, 2-Peripheral, 3-Supporting, 4-Core, 5-Foundational.
# Completeness (1-5): 1-Hinted, 2-Mentioned, 3-Sufficient, 4-Thorough, 5-Exhaustive.

# **EXAMPLE FORMAT:**
# [
#   {
#     "topic": "Definition of a Complex Number",
#     "relevance": 5,
#     "completeness": 5,
#     "teaching_strategy": "Start with the equation x^2 = -1 to motivate the need for 'i', then introduce the a+ib form.",
#     "rationale": "This contextual approach enhances student engagement."
#   }
# ]
# """,
#             agent=planner_agent
#         )

#         task_critique = Task(
#             description="Rigorously critique the received JSON teaching plan. Evaluate scores, strategies, and rationales.",
#             expected_output="A bulleted list of specific, actionable critiques for the strategic plan.",
#             agent=critic_agent,
#             context=[task_plan]
#         )

#         task_refine_plan = Task(
#             description="Take the draft teaching plan and the critiques. Produce a final, perfected JSON plan, including a 'refined_rationale' for each item.",
#             expected_output="The final, polished JSON list of objects, incorporating all feedback.",
#             agent=refiner_agent,
#             context=[task_plan, task_critique]
#         )

#         crew = Crew(
#             agents=[planner_agent, critic_agent, refiner_agent],
#             tasks=[task_plan, task_critique, task_refine_plan],
#             process=Process.sequential,
#             verbose=True
#         )
#         return crew, None

#     # --- New block for MCQ Generation workflow with Bloom's Taxonomy ---
#     elif module == "MCQ Generation":
#         json_plan_string = input_data

#         difficulty_instruction = ""
#         if difficulty:
#             difficulty_instruction = f"The overall difficulty of the questions should be **{difficulty.upper()}**.\n"

#         task_generate_mcqs = Task(
#             description="""
# You have been provided with a JSON list, where each object represents a topic from a pedagogical plan, including a 'refined_rationale'.

# Your task is to generate **ONE (1) multiple-choice question for EACH of the SIX (6) Bloom's Taxonomy levels** for EACH topic in the provided JSON list.
# The Bloom's Taxonomy levels are: **Remember, Understand, Apply, Analyze, Evaluate, Create.**
# Ensure the questions progressively increase in cognitive complexity.
# For each topic, you will generate 6 questions, one for each level.

# For each question, ensure it tests understanding of that specific topic, taking into account the 'refined_rationale' to inform its complexity and type.
# {difficulty_instruction}
# **IMPORTANT:** For any mathematical equations, scientific formulas, or symbols (e.g., variables, fractions, integrals, Greek letters), you MUST use LaTeX formatting.
# -   Use single dollar signs `$` for inline LaTeX (e.g., `$\\pi r^2$`).
# -   Use double dollar signs `$$` for block LaTeX equations (e.g., `$$\\int x^2 dx$$`).
# Ensure the LaTeX is correctly escaped (e.g., `\\\\sqrt{{}}` instead of `\\sqrt{}`) within JSON strings.

# Each question object must follow this strict JSON format and should include:
# -   'topic': The original topic name.
# -   'bloom_level': The Bloom's Taxonomy level for this specific question (must be one of: "Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create").
# -   'question': The text of the multiple-choice question (with LaTeX if applicable).
# -   'options': An array of strings representing the answer choices (at least 4, including the correct one, with LaTeX if applicable).
# -   'correct_answer': The exact string of the correct option (with LaTeX if applicable).
# -   'rationale': A brief explanation of why the correct answer is correct, referencing the 'refined_rationale' if appropriate (with LaTeX if applicable).

# **The final output MUST be a single JSON list of ALL these MCQ objects.** (i.e., if there are 2 topics, and 6 questions per topic, the list will contain 12 objects).

# --- JSON PLAN ---
# {json_plan_string}
# --- END JSON PLAN ---
# """, #line 555
#             expected_output="""
# A single JSON list of MCQ objects, where each object represents a single question.
# The output MUST be only the raw JSON.

# **EXAMPLE FORMAT (showing 2 questions for one topic as an example):**
# [[
#   {{
#     "topic": "Definition of a Complex Number",
#     "bloom_level": "Remember",
#     "question": "What is the primary characteristic of an imaginary number?",
#     "options": ["It can be plotted on a number line.", "Its square is a negative real number.", "It is always a whole number.", "It is a synonym for irrational numbers."],
#     "correct_answer": "Its square is a negative real number.",
#     "rationale": "This question tests the foundational definition of an imaginary number, requiring direct recall."
#   }},
#   {{
#     "topic": "Definition of a Complex Number",
#     "bloom_level": "Understand",
#     "question": "Which of the following best describes the purpose of introducing the imaginary unit '$i$' in mathematics?",
#     "options": ["To simplify calculations with real numbers.", "To allow solutions for equations like $x^2 = -1$.", "To represent quantities that are not numbers.", "To create a new number system entirely separate from real numbers."],
#     "correct_answer": "To allow solutions for equations like $x^2 = -1$.",
#     "rationale": "This question requires understanding the conceptual reason for '$i$'s existence, moving beyond simple recall of its definition ($i^2 = -1$). The refined rationale emphasizes motivating the need for '$i$'."
#   }},
#   {{
#     "topic": "Definition of a Complex Number",
#     "bloom_level": "Apply",
#     "question": "Given the equation $z^2 = -25$, which of the following is a possible value for $z$?",
#     "options": ["$5$", "$-5$", "$5i$", "$25i$"],
#     "correct_answer": "$5i$",
#     "rationale": "This question requires applying the definition of imaginary numbers ($i = \\sqrt{-1}$) to solve a simple quadratic equation, demonstrating practical use of the concept."
#   }},
#   {{
#     "topic": "Definition of a Complex Number",
#     "bloom_level": "Analyze",
#     "question": "Consider the statement: 'Every complex number can be uniquely represented as $a + bi$, where $a$ and $b$ are real numbers.' Which component of this statement highlights the distinction between real and imaginary parts?",
#     "options": ["'Every complex number'", "'uniquely represented'", "'$a$ and $b$ are real numbers'", "'$a + bi$'"],
#     "correct_answer": "'$a + bi$'",
#     "rationale": "This question requires analyzing the structure of a complex number's definition to identify the part that explicitly separates its real and imaginary components, aligning with understanding the composition of complex numbers."
#   }},
#   {{
#     "topic": "Definition of a Complex Number",
#     "bloom_level": "Evaluate",
#     "question": "A student claims that since $i = \\sqrt{-1}$, then $i^4 = (\\sqrt{-1})^4 = ((-1)^{1/2})^4 = (-1)^2 = 1$. Evaluate the correctness of this student's reasoning.",
#     "options": ["The reasoning is correct.", "The reasoning is incorrect because $i^4 = -1$.", "The reasoning is incorrect because $i^4 = i$.", "The reasoning is incorrect because $i^4$ is undefined."],
#     "correct_answer": "The reasoning is correct.",
#     "rationale": "This question requires evaluating a given line of reasoning about powers of $i$, demanding critical assessment of mathematical steps rather than just calculation. It aligns with evaluating the properties and operations of imaginary numbers."
#   }},
#   {{
#     "topic": "Definition of a Complex Number",
#     "bloom_level": "Create",
#     "question": "Imagine you are developing a new number system that extends complex numbers to include a 'hyper-imaginary' unit 'j' such that $j^2 = -i$. Formulate a simple quadratic equation that would necessitate the introduction of 'j', similar to how $x^2 = -1$ necessitated 'i'.",
#     "options": ["$y^2 = i$", "$y^2 = 1$", "$y^2 = -1$", "$y^2 = -i$"],
#     "correct_answer": "$y^2 = -i$",
#     "rationale": "This question pushes to the 'Create' level by asking the student to formulate a problem that requires a new concept, mirroring the historical development of complex numbers. It assesses the ability to generalize and design."
#   }}
# ]]
# """,
#             agent=mcq_generator_agent
#         )

#         crew = Crew(
#             agents=[mcq_generator_agent],
#             tasks=[task_generate_mcqs],
#             process=Process.sequential,
#             verbose=True
#         )
#         return crew, None

#     # --- This block handles all other single-agent modules, including the Knowledge Graph ---
#     else:
#         markdown_text = input_data # Rename for clarity within this block
#         agents = {
#             "Summarization": summarizer_agent,
#             "Notes": notes_agent,
#             "Explanation": explainer_agent,
#             "Knowledge Graph": knowledge_graph_agent,
#         }
#         task_definitions = {
#             "Summarization": {
#                 "description": f"Summarize the document.\n\n---\n{markdown_text}\n---",
#                 "expected_output": "A concise summary.",
#             },
#             "Notes": {
#                 "description": f"Create revision notes.\n\n---\n{markdown_text}\n---",
#                 "expected_output": "Well-organized notes.",
#             },
#             "Explanation": {
#                 "description": f"Explain the topics simply.\n\n---\n{markdown_text}\n---",
#                 "expected_output": "A simple explanation.",
#             },
#             "Knowledge Graph": {
#                 "description": f"""
# You are an expert curriculum designer. Your task is to create a high-level, easy-to-follow learning path flowchart from the provided document.
# Focus on major topics and group minor concepts. Use short, clear labels.
# The final output MUST be only a valid Graphviz DOT language code.

# --- DOCUMENT ---
# {markdown_text}
# --- END DOCUMENT ---
# """,
#                 "expected_output": """
# A string containing ONLY the Graphviz DOT language code.
# **EXAMPLE FORMAT:**
# digraph LearningPath {{
#   rankdir="TB";
#   node [shape=box, style="rounded,filled", fillcolor="#aaffaa"];
#   A [label="Introduction"];
#   B [label="Core Concepts"];
#   C [label="Advanced Topics"];
#   A -> B -> C;
# }}
# """,
#             },
#         }

#         agent = agents.get(module)
#         task_details = task_definitions.get(module)
        
#         if not agent or not task_details:
#             raise ValueError(f"Invalid module selected: {module}")

#         task = Task(description=task_details["description"], expected_output=task_details["expected_output"], agent=agent)
        
#         return Crew(tasks=[task], agents=[agent], verbose=True), None

# Bloom's Taxonomy
# # crew/crew_factory.py

# from crewai import Task, Crew, Agent, Process
# from agents.summarizer import summarizer_agent
# from agents.notes import notes_agent
# from agents.explainer import explainer_agent
# from agents.planner import planner_agent
# from agents.critic import critic_agent
# from agents.refiner import refiner_agent
# from agents.knowledge_graph import knowledge_graph_agent
# from agents.mcq import mcq_generator_agent
# import json5 as json
# from crew.tools.mcq_tools import MCQList

# def get_crew(module: str, input_data: str, difficulty: str = None, bloom_q_counts: dict = None, strategic_plan_data: list = None):
    
#     if module == "Strategic Plan":
#         # ... (This section is correct, no changes needed)
#         markdown_text = input_data
#         task_plan = Task(
#             description=f"""
# Analyze the document below and create a comprehensive pedagogical plan.
# 1.  Identify every distinct topic and sub-topic.
# 2.  For each topic, you must provide scores for 'relevance' and 'completeness' based on the strict rubric in the expected output.
# 3.  For each topic, devise a draft 'teaching_strategy' and a draft 'rationale' explaining it.

# --- DOCUMENT ---
# {markdown_text}
# --- END DOCUMENT ---
# """,
#             expected_output="""
# A single JSON list of objects. The output MUST be only the raw JSON.
# Each object MUST contain 'topic', 'relevance', 'completeness', 'teaching_strategy', and 'rationale'.

# **STRICT SCORING RUBRIC:**
# Relevance (1-5): 1-Trivial, 2-Peripheral, 3-Supporting, 4-Core, 5-Foundational.
# Completeness (1-5): 1-Hinted, 2-Mentioned, 3-Sufficient, 4-Thorough, 5-Exhaustive.

# **EXAMPLE FORMAT:**
# [
#   {
#     "topic": "Definition of a Complex Number",
#     "relevance": 5,
#     "completeness": 5,
#     "teaching_strategy": "Start with the equation x^2 = -1 to motivate the need for 'i', then introduce the a+ib form.",
#     "rationale": "This contextual approach enhances student engagement."
#   }
# ]
# """,
#             agent=planner_agent
#         )
#         task_critique = Task(description="Rigorously critique the received JSON teaching plan. Evaluate scores, strategies, and rationales.", expected_output="A bulleted list of specific, actionable critiques for the strategic plan.", agent=critic_agent, context=[task_plan])
#         task_refine_plan = Task(description="Take the draft teaching plan and the critiques. Produce a final, perfected JSON plan, including a 'refined_rationale' for each item.", expected_output="The final, polished JSON list of objects, incorporating all feedback.", agent=refiner_agent, context=[task_plan, task_critique])
#         crew = Crew(agents=[planner_agent, critic_agent, refiner_agent], tasks=[task_plan, task_critique, task_refine_plan], process=Process.sequential, verbose=True)
#         return crew, None

#     elif module == "MCQ Generation":
#         topics_data = json.loads(input_data)
#         if not isinstance(topics_data, list): topics_data = [topics_data]

#         mcq_tasks = []
#         for topic_obj in topics_data:
#             single_topic_json_string = json.dumps(topic_obj)
            
#             difficulty_instruction = f"The overall difficulty of the questions should be **{difficulty.upper()}**.\n" if difficulty else ""
#             bloom_counts_instruction = ""
#             if bloom_q_counts:
#                 bloom_counts_instruction = "\nGenerate the following number of questions for each Bloom's Taxonomy level (per topic):\n"
#                 for level, count in bloom_q_counts.items():
#                     if count > 0: bloom_counts_instruction += f"-   **{level}**: {count} question(s)\n"
#                 bloom_counts_instruction += "Ensure that if a count is 0, no question is generated for that level.\n"

#             task_description = f"""
# You are an expert at generating educational content. Based on the single topic JSON provided below, create a set of multiple-choice questions.

# **CRITICAL INSTRUCTIONS:**
# 1.  Generate questions for this ONE topic across the six Bloom's Taxonomy levels: **Remember, Understand, Apply, Analyze, Evaluate, Create.**
# {bloom_counts_instruction}
# 2.  For any mathematical equations or symbols, you MUST use LaTeX formatting (e.g., `$z = a + ib$`).
# 3.  Each question object MUST contain all the fields described in the format example.
# 4.  The `correct_answer` MUST be the full text of the option, not just a letter like 'A' or 'B'.

# **CRITICAL OUTPUT FORMAT:**
# Your final output MUST be a single JSON object with a single key named "mcqs". The value of "mcqs" MUST be a JSON list of the question objects you generate.

# **EXAMPLE OF THE REQUIRED FINAL OUTPUT STRUCTURE:**
# {{
#   "mcqs": [
#     {{
#       "topic": "Topic Name from Input",
#       "bloom_level": "Remember",
#       "question": "What is the formula for...?",
#       "options": ["Option A", "Option B", "Option C", "Option D"],
#       "correct_answer": "Option C",
#       "rationale": "This is the correct answer because it directly follows the definition."
#     }}
#   ]
# }}

# --- SINGLE TOPIC JSON ---
# {single_topic_json_string}
# --- END SINGLE TOPIC JSON ---
# """
            
#             mcq_tasks.append(
#                 Task(
#                     description=task_description,
#                     expected_output='A single JSON object with the key "mcqs" containing a list of question objects.',
#                     agent=mcq_generator_agent,
#                 )
#             )

#         crew = Crew(agents=[mcq_generator_agent], tasks=mcq_tasks, process=Process.sequential, verbose=True)
#         return crew, "pydantic_mcq_generation"

#     else:
#         # ... (This section for other modules is correct, no changes needed)
#         markdown_text = input_data
#         agents = {"Summarization": summarizer_agent, "Notes": notes_agent, "Explanation": explainer_agent, "Knowledge Graph": knowledge_graph_agent}
#         task_definitions = {
#             "Summarization": {"description": f"Summarize the document.\n\n---\n{markdown_text}\n---", "expected_output": "A concise summary."},
#             "Notes": {"description": f"Create revision notes.\n\n---\n{markdown_text}\n---", "expected_output": "Well-organized notes."},
#             "Explanation": {"description": f"Explain the topics simply.\n\n---\n{markdown_text}\n---", "expected_output": "A simple explanation."},
#             "Knowledge Graph": {
#                 "description": """
# You are an expert curriculum designer. Your task is to create a high-level, easy-to-follow learning path flowchart from the provided document. Focus on major topics and group minor concepts.
# **CRITICAL INSTRUCTION:** When defining nodes, for any topics you identify from the Strategic Plan (provided below if available), you MUST use their EXACT topic names as your node IDs and labels.
# **Strategic Plan Topics to Use as Node Labels (if available):**
# {strategic_plan_topics_list}
# The final output MUST be ONLY a valid Graphviz DOT language code.
# --- DOCUMENT ---
# {markdown_text}
# --- END DOCUMENT ---
# """,
#                 "expected_output": """A string containing ONLY the Graphviz DOT language code."""
#             },
#         }
#         agent = agents.get(module)
#         task_details = task_definitions.get(module)
#         if not agent or not task_details: raise ValueError(f"Invalid module selected: {module}")
#         final_description = task_details["description"]
#         if module == "Knowledge Graph":
#             topics_list_str = "\\n".join([f'- "{item["topic"]}"' for item in strategic_plan_data]) if strategic_plan_data else "No strategic plan topics provided."
#             final_description = final_description.format(strategic_plan_topics_list=topics_list_str, markdown_text=markdown_text)
#         task = Task(description=final_description, expected_output=task_details["expected_output"], agent=agent)
#         return Crew(tasks=[task], agents=[agent], verbose=True), None

# Refined Bloom
# # crew/crew_factory.py
# from crewai import Task, Crew, Agent, Process
# from agents.summarizer import summarizer_agent
# from agents.notes import notes_agent
# from agents.explainer import explainer_agent
# from agents.planner import planner_agent
# from agents.critic import critic_agent
# from agents.refiner import refiner_agent
# from agents.knowledge_graph import knowledge_graph_agent
# from agents.mcq import mcq_generator_agent
# from agents.mcq_critic import mcq_critic_agent
# from agents.mcq_refiner import mcq_refiner_agent
# import json5 as json
# from crew.tools.mcq_tools import MCQList

# def get_crew(module: str, input_data: str, difficulty: str = None, bloom_q_counts: dict = None, strategic_plan_data: list = None):

#     if module == "Strategic Plan":
#         # ... (This section is correct, no changes needed)
#         markdown_text = input_data
#         task_plan = Task(
#             description=f"""
# Analyze the document below and create a comprehensive pedagogical plan.
# 1.  Identify every distinct topic and sub-topic.
# 2.  For each topic, you must provide scores for 'relevance' and 'completeness' based on the strict rubric in the expected output.
# 3.  For each topic, devise a draft 'teaching_strategy' and a draft 'rationale' explaining it.

# --- DOCUMENT ---
# {markdown_text}
# --- END DOCUMENT ---
# """,
#             expected_output="""
# A single JSON list of objects. The output MUST be only the raw JSON.
# Each object MUST contain 'topic', 'relevance', 'completeness', 'teaching_strategy', and 'rationale'.

# **STRICT SCORING RUBRIC:**
# Relevance (1-5): 1-Trivial, 2-Peripheral, 3-Supporting, 4-Core, 5-Foundational.
# Completeness (1-5): 1-Hinted, 2-Mentioned, 3-Sufficient, 4-Thorough, 5-Exhaustive.

# **EXAMPLE FORMAT:**
# [
#   {
#     "topic": "Definition of a Complex Number",
#     "relevance": 5,
#     "completeness": 5,
#     "teaching_strategy": "Start with the equation x^2 = -1 to motivate the need for 'i', then introduce the a+ib form.",
#     "rationale": "This contextual approach enhances student engagement."
#   }
# ]
# """,
#             agent=planner_agent
#         )
#         task_critique = Task(description="Rigorously critique the received JSON teaching plan. Evaluate scores, strategies, and rationales.", expected_output="A bulleted list of specific, actionable critiques for the strategic plan.", agent=critic_agent, context=[task_plan])
#         task_refine_plan = Task(description="Take the draft teaching plan and the critiques. Produce a final, perfected JSON plan, including a 'refined_rationale' for each item.", expected_output="The final, polished JSON list of objects, incorporating all feedback.", agent=refiner_agent, context=[task_plan, task_critique])
#         crew = Crew(agents=[planner_agent, critic_agent, refiner_agent], tasks=[task_plan, task_critique, task_refine_plan], process=Process.sequential, verbose=True)
#         return crew, None

#     elif module == "MCQ Generation":
#         topics_data = json.loads(input_data)
#         if not isinstance(topics_data, list): topics_data = [topics_data]

#         mcq_tasks = []
#         for topic_obj in topics_data:
#             single_topic_json_string = json.dumps(topic_obj)

#             difficulty_instruction = f"The overall difficulty of the questions should be **{difficulty.upper()}**.\n" if difficulty else ""
#             bloom_counts_instruction = ""
#             if bloom_q_counts:
#                 bloom_counts_instruction = "\nGenerate the following number of questions for each Bloom's Taxonomy level (per topic):\n"
#                 for level, count in bloom_q_counts.items():
#                     if count > 0: bloom_counts_instruction += f"-   **{level}**: {count} question(s)\n"
#                 bloom_counts_instruction += "Ensure that if a count is 0, no question is generated for that level.\n"

#             # Task 1: Generate initial MCQs
#             task_generate = Task(
#                 description=f"""
# You are an expert at generating educational content. Based on the single topic JSON provided below, create a set of multiple-choice questions.

# **CRITICAL INSTRUCTIONS:**
# 1.  Generate questions for this ONE topic across the six Bloom's Taxonomy levels: **Remember, Understand, Apply, Analyze, Evaluate, Create.**
# {bloom_counts_instruction}
# 2.  For any mathematical equations or symbols, you MUST use LaTeX formatting (e.g., `$z = a + ib$`).
# 3.  Each question object MUST contain all the fields described in the format example.
# 4.  The `correct_answer` MUST be the full text of the option, not just a letter like 'A' or 'B'.

# **CRITICAL OUTPUT FORMAT:**
# Your final output MUST be a single JSON object with a single key named "mcqs". The value of "mcqs" MUST be a JSON list of the question objects you generate.

# **EXAMPLE OF THE REQUIRED FINAL OUTPUT STRUCTURE:**
# {{
#   "mcqs": [
#     {{
#       "topic": "Topic Name from Input",
#       "bloom_level": "Remember",
#       "question": "What is the formula for...?",
#       "options": ["Option A", "Option B", "Option C", "Option D"],
#       "correct_answer": "Option C",
#       "rationale": "This is the correct answer because it directly follows the definition."
#     }}
#   ]
# }}

# --- SINGLE TOPIC JSON ---
# {single_topic_json_string}
# --- END SINGLE TOPIC JSON ---
# """,
#                 expected_output='A single JSON object with the key "mcqs" containing a list of draft question objects.',
#                 agent=mcq_generator_agent,
#             )

#             # Task 2: Critique the generated MCQs
#             task_critique = Task(
#                 description="""Rigorously review the provided MCQs.
#                 Check for:
#                 - Clarity and unambiguity in the question and options.
#                 - Factual accuracy of the question and the correct answer.
#                 - Plausibility of the distractor options.
#                 - Strict alignment of the question with its stated Bloom's Taxonomy level.
#                 - Quality and helpfulness of the rationale. It should explain WHY the correct answer is right.
#                 Provide a bulleted list of specific, actionable feedback for improvement. If a question is good, state that.
#                 """,
#                 expected_output="""A bulleted list of actionable critiques and feedback for the generated MCQs.
#                 Example:
#                 - The question for 'Analyze' level is more of a 'Remember' level. It should ask to compare or deconstruct elements.
#                 - Option C in the first question is too obviously wrong.
#                 - The rationale for the third question is weak; it just restates the answer. It should explain the underlying principle.
#                 """,
#                 agent=mcq_critic_agent,
#                 context=[task_generate]
#             )

#             # Task 3: Refine the MCQs based on critique
#             task_refine = Task(
#                 description="""Revise and refine the initial set of MCQs based on the provided critique.
#                 Carefully address every point in the critique to improve the questions.
#                 The final output MUST be a single, clean JSON object containing the perfected MCQs.
#                 Ensure the format is exactly as requested in the initial generation task.""",
#                 expected_output='''The final, polished JSON object. This object MUST have two keys:
# 1.  `"status"`: with the string value `"refined"`.
# 2.  `"mcqs"`: containing the list of the refined question objects.
# THIS IS THE ONLY THING YOU MUST OUTPUT.''', # <-- MODIFIED EXPECTED OUTPUT
#                 agent=mcq_refiner_agent,
#                 context=[task_generate, task_critique]
#             )

#             mcq_tasks.extend([task_generate, task_critique, task_refine])

#         crew = Crew(
#             agents=[mcq_generator_agent, mcq_critic_agent, mcq_refiner_agent],
#             tasks=mcq_tasks,
#             process=Process.sequential,
#             verbose=True
#         )
#         return crew, "pydantic_mcq_generation"

#     else:
#         markdown_text = input_data
#         agents = {"Summarization": summarizer_agent, "Notes": notes_agent, "Explanation": explainer_agent, "Knowledge Graph": knowledge_graph_agent}
#         task_definitions = {
#             "Summarization": {"description": f"Summarize the document.\n\n---\n{markdown_text}\n---", "expected_output": "A concise summary."},
#             "Notes": {"description": f"Create revision notes.\n\n---\n{markdown_text}\n---", "expected_output": "Well-organized notes."},
#             "Explanation": {"description": f"Explain the topics simply.\n\n---\n{markdown_text}\n---", "expected_output": "A simple explanation."},
#             "Knowledge Graph": {
#                 "description": """
# You are an expert curriculum designer. Your task is to create a high-level, easy-to-follow learning path flowchart from the provided document. Focus on major topics and group minor concepts.
# **CRITICAL INSTRUCTION:** When defining nodes, for any topics you identify from the Strategic Plan (provided below if available), you MUST use their EXACT topic names as your node IDs and labels.
# **Strategic Plan Topics to Use as Node Labels (if available):**
# {strategic_plan_topics_list}
# The final output MUST be ONLY a valid Graphviz DOT language code.
# --- DOCUMENT ---
# {markdown_text}
# --- END DOCUMENT ---
# """,
#                 "expected_output": """A string containing ONLY the Graphviz DOT language code."""
#             },
#         }
#         agent = agents.get(module)
#         task_details = task_definitions.get(module)
#         if not agent or not task_details: raise ValueError(f"Invalid module selected: {module}")
#         final_description = task_details["description"]
#         if module == "Knowledge Graph":
#             topics_list_str = "\\n".join([f'- "{item["topic"]}"' for item in strategic_plan_data]) if strategic_plan_data else "No strategic plan topics provided."
#             final_description = final_description.format(strategic_plan_topics_list=topics_list_str, markdown_text=markdown_text)
#         task = Task(description=final_description, expected_output=task_details["expected_output"], agent=agent)
#         return Crew(tasks=[task], agents=[agent], verbose=True), None

# Distractions
# # crew/crew_factory.py
# # Import the static agent INSTANCES.
# from crewai import Task, Crew, Agent, Process
# import json5 as json

# # Import the static agent INSTANCES.
# from agents.summarizer import summarizer_agent
# from agents.notes import notes_agent
# from agents.explainer import explainer_agent
# from agents.planner import planner_agent
# from agents.critic import critic_agent
# from agents.refiner import refiner_agent
# from agents.knowledge_graph import knowledge_graph_agent
# from agents.mcq import mcq_generator_agent
# from agents.mcq_critic import mcq_critic_agent
# from agents.mcq_refiner import mcq_refiner_agent
# from agents.distractor_generator import distractor_agent
# from agents.distractor_critic import distractor_critic_agent
# from agents.distractor_refiner import distractor_refiner_agent

# def get_crew(module: str, input_data: str, difficulty: str = None, bloom_q_counts: dict = None, strategic_plan_data: list = None):

#     if module == "Strategic Plan":
#         markdown_text = input_data
#         task_plan = Task(
#             description=f"""
# Analyze the document below and create a comprehensive pedagogical plan.
# 1.  Identify every distinct topic and sub-topic.
# 2.  For each topic, you must provide scores for 'relevance' and 'completeness' based on the strict rubric in the expected output.
# 3.  For each topic, devise a draft 'teaching_strategy' and a draft 'rationale' explaining it.

# --- DOCUMENT ---
# {markdown_text}
# --- END DOCUMENT ---
# """,
#             expected_output="""
# A single JSON list of objects. The output MUST be only the raw JSON.
# Each object MUST contain 'topic', 'relevance', 'completeness', 'teaching_strategy', and 'rationale'.

# **STRICT SCORING RUBRIC:**
# Relevance (1-5): 1-Trivial, 2-Peripheral, 3-Supporting, 4-Core, 5-Foundational.
# Completeness (1-5): 1-Hinted, 2-Mentioned, 3-Sufficient, 4-Thorough, 5-Exhaustive.

# **EXAMPLE FORMAT:**
# [
#   {
#     "topic": "Definition of a Complex Number",
#     "relevance": 5,
#     "completeness": 5,
#     "teaching_strategy": "Start with the equation x^2 = -1 to motivate the need for 'i', then introduce the a+ib form.",
#     "rationale": "This contextual approach enhances student engagement."
#   }
# ]
# """,
#             agent=planner_agent
#         )
#         task_critique = Task(description="Rigorously critique the received JSON teaching plan. Evaluate scores, strategies, and rationales.", expected_output="A bulleted list of specific, actionable critiques for the strategic plan.", agent=critic_agent, context=[task_plan])
#         task_refine_plan = Task(description="Take the draft teaching plan and the critiques. Produce a final, perfected JSON plan, including a 'refined_rationale' for each item.", expected_output="The final, polished JSON list of objects, incorporating all feedback.", agent=refiner_agent, context=[task_plan, task_critique])
#         crew = Crew(agents=[planner_agent, critic_agent, refiner_agent], tasks=[task_plan, task_critique, task_refine_plan], process=Process.sequential)
#         return crew, None

#     elif module == "MCQ Generation":
#         topics_data = json.loads(input_data)
#         mcq_tasks = []
#         for topic_obj in topics_data:
#             single_topic_json_string = json.dumps(topic_obj)
#             difficulty_instruction = f"The overall difficulty of the questions should be **{difficulty.upper()}**.\n" if difficulty else ""
            
#             bloom_counts_instruction = ""
#             if bloom_q_counts:
#                 bloom_counts_instruction = "\nGenerate the following number of questions for each Bloom's Taxonomy level:\n"
#                 for level, count in bloom_q_counts.items():
#                     if count > 0:
#                         bloom_counts_instruction += f"-   **{level}**: {count} question(s)\n"
#                 bloom_counts_instruction += "If a count for a level is 0, you MUST NOT generate a question for that level.\n"
            
#             task_generate = Task(
#                 description=f"""
# You are an expert at generating educational content. Based on the single topic JSON provided below, create a set of multiple-choice questions.
# {difficulty_instruction}
# {bloom_counts_instruction}
# **CRITICAL INSTRUCTIONS:**
# 1.  You MUST identify and include a specific `domain` and `bloom_level` for each question.
# 2.  Each question object MUST contain all the fields described in the format example.
# 3.  The `correct_answer` MUST be the full text of the option, not just a letter like 'A' or 'B'.
# 4.  For any mathematical equations or symbols, you MUST use LaTeX formatting (e.g., `$z = a + ib$`).

# **EXAMPLE OF THE REQUIRED FINAL OUTPUT STRUCTURE:**
# {{
#   "mcqs": [
#     {{
#       "domain": "Complex Numbers",
#       "bloom_level": "Remember",
#       "topic": "Topic Name from Input",
#       "question": "What is the definition of an imaginary unit?",
#       "options": ["$i^2 = 1$", "$i^2 = -1$", "$i = -1$", "$i = 1$"],
#       "correct_answer": "$i^2 = -1$",
#       "rationale": "The imaginary unit 'i' is fundamentally defined by the property that its square is -1."
#     }}
#   ]
# }}

# --- SINGLE TOPIC JSON ---
# {single_topic_json_string}
# --- END SINGLE TOPIC JSON ---
# """,
#                 expected_output='A single JSON object with the key "mcqs" containing a list of draft question objects, where each object includes a "domain" and "bloom_level".',
#                 agent=mcq_generator_agent,
#             )
#             task_critique = Task(
#                 description="Rigorously review the provided MCQs. Check for domain accuracy, Bloom's level alignment, clarity, and correctness.",
#                 expected_output="A bulleted list of actionable critiques for the generated MCQs.",
#                 agent=mcq_critic_agent,
#                 context=[task_generate]
#             )
#             task_refine = Task(
#                 description="Refine the MCQs based on the provided critique.",
#                 expected_output='''The final, polished JSON object. This object MUST have two keys:
# 1.  `"status"`: with the string value `"refined"`.
# 2.  `"mcqs"`: containing the list of the refined question objects.
# THIS IS THE ONLY THING YOU MUST OUTPUT.''',
#                 agent=mcq_refiner_agent,
#                 context=[task_generate, task_critique]
#             )
#             mcq_tasks.extend([task_generate, task_critique, task_refine])

#         crew = Crew(agents=[mcq_generator_agent, mcq_critic_agent, mcq_refiner_agent], tasks=mcq_tasks, process=Process.sequential)
#         return crew, "mcq_generation"

#     elif module == "Distractor Generation":
#         q_obj = json.loads(input_data)
        
#         task_generate_distractors = Task(
#             description=f"""
#             For the question '{q_obj['question']}' and its correct answer '{q_obj['answer']}', you must generate 3 distinct, plausible, and compellingly incorrect answer options (distractors).
#             For each of the 3 distractors, you MUST provide a "misleading_rationale" that explains the specific misconception or error a student would make to choose that option.
            
#             **CRITICAL INSTRUCTION:** For any mathematical equations or symbols in the options or rationales, you MUST use LaTeX formatting (e.g., `$z = a + ib$`).
#             """,
#             expected_output="""A single JSON list of exactly 3 objects. Each object must have two keys: "option" (the distractor text) and "misleading_rationale".
            
#             Example:
#             [
#               {
#                 "option": "The value is $x^2$",
#                 "misleading_rationale": "This is tempting because it forgets to take the square root, $\\sqrt{x^2}$."
#               }
#             ]
#             """,
#             agent=distractor_agent
#         )

#         task_critique_distractors = Task(
#             description=f"""
#             Rigorously evaluate the generated distractors and their rationales for the question: '{q_obj['question']}'.
#             Ensure they are plausible but unambiguously incorrect. Critique any options that are too obvious, poorly worded, or could be argued as correct.
#             Provide a bulleted list of actionable feedback for improvement.
#             """,
#             expected_output="A concise, bulleted list of feedback for improving the distractors.",
#             agent=distractor_critic_agent,
#             context=[task_generate_distractors]
#         )

#         task_refine_distractors = Task(
#             description="""
#             Based on the initial distractors and the expert critique provided, produce a final, high-quality set of three incorrect answer options.
#             You must refine the "option" text based on the feedback, but PRESERVE the original "misleading_rationale" for each option.
#             """,
#             expected_output='''A single JSON list of exactly 3 objects. Each object must have two keys: "option" (the refined distractor text) and "misleading_rationale".
            
#             Example:
#             [
#               {"option": "Final Refined Option A", "misleading_rationale": "This option is tempting because..."},
#               {"option": "Final Refined Option B", "misleading_rationale": "This is a common mistake..."}
#             ]
#             ''',
#             agent=distractor_refiner_agent,
#             context=[task_generate_distractors, task_critique_distractors]
#         )
        
#         crew = Crew(
#             agents=[distractor_agent, distractor_critic_agent, distractor_refiner_agent],
#             tasks=[task_generate_distractors, task_critique_distractors, task_refine_distractors],
#             process=Process.sequential
#         )
#         return crew, "distractor_generation"

#     else: # Handles Summarization, Notes, Explanation, Knowledge Graph
#         markdown_text = input_data
#         agents = {"Summarization": summarizer_agent, "Notes": notes_agent, "Explanation": explainer_agent, "Knowledge Graph": knowledge_graph_agent}
#         task_definitions = {
#             "Summarization": {"description": f"Summarize the document.\n\n---\n{markdown_text}\n---", "expected_output": "A concise summary."},
#             "Notes": {"description": f"Create revision notes.\n\n---\n{markdown_text}\n---", "expected_output": "Well-organized notes."},
#             "Explanation": {"description": f"Explain the topics simply.\n\n---\n{markdown_text}\n---", "expected_output": "A simple explanation."},
#             "Knowledge Graph": {"description": f"Create a Graphviz DOT flowchart from the document.\n\n---\n{markdown_text}\n---", "expected_output": "A string containing ONLY the Graphviz DOT language code."}
#         }
#         agent = agents[module]
#         task_details = task_definitions[module]
#         task = Task(description=task_details['description'], expected_output=task_details['expected_output'], agent=agent)
#         return Crew(tasks=[task], agents=[agent]), None

# Numeric and Theoretical Classification
# # crew_factory.py
# from crewai import Task, Crew, Agent, Process
# import json5 as json

# # Import the static agent INSTANCES.
# from agents.summarizer import summarizer_agent
# from agents.notes import notes_agent
# from agents.explainer import explainer_agent
# from agents.planner import planner_agent
# from agents.critic import critic_agent
# from agents.refiner import refiner_agent
# from agents.knowledge_graph import knowledge_graph_agent
# from agents.mcq import mcq_generator_agent
# from agents.mcq_critic import mcq_critic_agent
# from agents.mcq_refiner import mcq_refiner_agent
# from agents.distractor_generator import distractor_agent
# from agents.distractor_critic import distractor_critic_agent
# from agents.distractor_refiner import distractor_refiner_agent
# from agents.question_classifier import question_classifier_agent

# def get_crew(module: str, input_data: str, difficulty: str = None, bloom_q_counts: dict = None, strategic_plan_data: list = None):

#     if module == "Strategic Plan":
#         markdown_text = input_data
#         task_plan = Task(
#             description=f"""
# Analyze the document below and create a comprehensive pedagogical plan.
# 1.  Identify every distinct topic and sub-topic.
# 2.  For each topic, you must provide scores for 'relevance' and 'completeness' based on the strict rubric in the expected output.
# 3.  For each topic, devise a draft 'teaching_strategy' and a draft 'rationale' explaining it.

# --- DOCUMENT ---
# {markdown_text}
# --- END DOCUMENT ---
# """,
#             expected_output="""
# A single JSON list of objects. The output MUST be only the raw JSON.
# Each object MUST contain 'topic', 'relevance', 'completeness', 'teaching_strategy', and 'rationale'.

# **STRICT SCORING RUBRIC:**
# Relevance (1-5): 1-Trivial, 2-Peripheral, 3-Supporting, 4-Core, 5-Foundational.
# Completeness (1-5): 1-Hinted, 2-Mentioned, 3-Sufficient, 4-Thorough, 5-Exhaustive.

# **EXAMPLE FORMAT:**
# [
#   {
#     "topic": "Definition of a Complex Number",
#     "relevance": 5,
#     "completeness": 5,
#     "teaching_strategy": "Start with the equation x^2 = -1 to motivate the need for 'i', then introduce the a+ib form.",
#     "rationale": "This contextual approach enhances student engagement."
#   }
# ]
# """,
#             agent=planner_agent
#         )
#         task_critique = Task(description="Rigorously critique the received JSON teaching plan. Evaluate scores, strategies, and rationales.", expected_output="A bulleted list of specific, actionable critiques for the strategic plan.", agent=critic_agent, context=[task_plan])
#         task_refine_plan = Task(description="Take the draft teaching plan and the critiques. Produce a final, perfected JSON plan, including a 'refined_rationale' for each item.", expected_output="The final, polished JSON list of objects, incorporating all feedback.", agent=refiner_agent, context=[task_plan, task_critique])
#         crew = Crew(agents=[planner_agent, critic_agent, refiner_agent], tasks=[task_plan, task_critique, task_refine_plan], process=Process.sequential)
#         return crew, None

#     elif module == "MCQ Generation":
#         topic_obj = json.loads(input_data)
#         difficulty_instruction = f"The overall difficulty of the questions should be **{difficulty.upper()}**.\n" if difficulty else ""
        
#         bloom_counts_instruction = ""
#         if bloom_q_counts:
#             bloom_counts_instruction = "\nGenerate the following number of questions for each Bloom's Taxonomy level:\n"
#             for level, count in bloom_q_counts.items():
#                 if count > 0:
#                     bloom_counts_instruction += f"-   **{level}**: {count} question(s)\n"
#             bloom_counts_instruction += "If a count for a level is 0, you MUST NOT generate a question for that level.\n"
        
#         task_generate = Task(
#             description=f"""
# You are an expert at generating educational content. Based on the single topic JSON provided below, create a set of multiple-choice questions.
# {difficulty_instruction}
# {bloom_counts_instruction}
# **CRITICAL INSTRUCTIONS:**
# 1.  You MUST identify and include a specific `domain` and `bloom_level` for each question.
# 2.  Each question object MUST contain all the fields described in the format example.
# 3.  The `correct_answer` MUST be the full text of the option, not just a letter like 'A' or 'B'.
# 4.  For any mathematical equations or symbols, you MUST use LaTeX formatting (e.g., `$z = a + ib$`).

# **EXAMPLE OF THE REQUIRED FINAL OUTPUT STRUCTURE:**
# {{
#   "mcqs": [
#     {{
#       "domain": "Complex Numbers",
#       "bloom_level": "Remember",
#       "topic": "Topic Name from Input",
#       "question": "What is the definition of an imaginary unit?",
#       "options": ["$i^2 = 1$", "$i^2 = -1$", "$i = -1$", "$i = 1$"],
#       "correct_answer": "$i^2 = -1$",
#       "rationale": "The imaginary unit 'i' is fundamentally defined by the property that its square is -1."
#     }}
#   ]
# }}

# --- SINGLE TOPIC JSON ---
# {input_data}
# --- END SINGLE TOPIC JSON ---
# """,
#             expected_output='A single JSON object with the key "mcqs" containing a list of draft question objects, where each object includes a "domain" and "bloom_level".',
#             agent=mcq_generator_agent,
#         )
#         task_critique = Task(
#             description="Rigorously review the provided MCQs. Check for domain accuracy, Bloom's level alignment, clarity, and correctness.",
#             expected_output="A bulleted list of actionable critiques for the generated MCQs.",
#             agent=mcq_critic_agent,
#             context=[task_generate]
#         )
#         task_refine = Task(
#             description="Refine the MCQs based on the provided critique.",
#             expected_output='''The final, polished JSON object. This object MUST have two keys:
# 1.  `"status"`: with the string value `"refined"`.
# 2.  `"mcqs"`: containing the list of the refined question objects.
# THIS IS THE ONLY THING YOU MUST OUTPUT.''',
#             agent=mcq_refiner_agent,
#             context=[task_generate, task_critique]
#         )

#         crew = Crew(agents=[mcq_generator_agent, mcq_critic_agent, mcq_refiner_agent], tasks=[task_generate, task_critique, task_refine], process=Process.sequential)
#         return crew, "mcq_generation"

#     elif module == "Filter Questions":
#         q_obj = json.loads(input_data)
#         task_classify_question = Task(
#             description=f"""
#             Analyze the following question and classify it as either 'Numeric' or 'Theoretical'.
#             - 'Numeric' questions involve math, formulas, or calculations.
#             - 'Theoretical' questions are about definitions, concepts, or qualitative facts.

#             Question: "{q_obj['question']}"
#             """,
#             expected_output="A single word response: either 'Numeric' or 'Theoretical'.",
#             agent=question_classifier_agent
#         )
#         crew = Crew(
#             agents=[question_classifier_agent],
#             tasks=[task_classify_question],
#             process=Process.sequential
#         )
#         return crew, "question_classification"

#     elif module == "Distractor Generation":
#         q_obj = json.loads(input_data)
        
#         task_generate_distractors = Task(
#             description=f"""
#             For the question '{q_obj['question']}' and its correct answer '{q_obj['answer']}', you must generate 3 distinct, plausible, and compellingly incorrect answer options (distractors).
#             For each of the 3 distractors, you MUST provide a "misleading_rationale" that explains the specific misconception or error a student would make to choose that option.
            
#             **CRITICAL INSTRUCTION:** For any mathematical equations or symbols in the options or rationales, you MUST use LaTeX formatting (e.g., `$z = a + ib$`).
#             """,
#             expected_output="""A single JSON list of exactly 3 objects. Each object must have two keys: "option" (the distractor text) and "misleading_rationale".
            
#             Example:
#             [
#               {
#                 "option": "The value is $x^2$",
#                 "misleading_rationale": "This is tempting because it forgets to take the square root, $\\sqrt{x^2}$."
#               }
#             ]
#             """,
#             agent=distractor_agent
#         )

#         task_critique_distractors = Task(
#             description=f"""
#             Rigorously evaluate the generated distractors and their rationales for the question: '{q_obj['question']}'.
#             Ensure they are plausible but unambiguously incorrect. Critique any options that are too obvious, poorly worded, or could be argued as correct.
#             Provide a bulleted list of actionable feedback for improvement.
#             """,
#             expected_output="A concise, bulleted list of feedback for improving the distractors.",
#             agent=distractor_critic_agent,
#             context=[task_generate_distractors]
#         )

#         task_refine_distractors = Task(
#             description="""
#             Based on the initial distractors and the expert critique provided, produce a final, high-quality set of three incorrect answer options.
#             You must refine the "option" text based on the feedback, but PRESERVE the original "misleading_rationale" for each option.
#             """,
#             expected_output='''A single JSON list of exactly 3 objects. Each object must have two keys: "option" (the refined distractor text) and "misleading_rationale".
            
#             Example:
#             [
#               {"option": "Final Refined Option A", "misleading_rationale": "This option is tempting because..."},
#               {"option": "Final Refined Option B", "misleading_rationale": "This is a common mistake..."}
#             ]
#             ''',
#             agent=distractor_refiner_agent,
#             context=[task_generate_distractors, task_critique_distractors]
#         )
        
#         crew = Crew(
#             agents=[distractor_agent, distractor_critic_agent, distractor_refiner_agent],
#             tasks=[task_generate_distractors, task_critique_distractors, task_refine_distractors],
#             process=Process.sequential
#         )
#         return crew, "distractor_generation"

#     else: # Handles Summarization, Notes, Explanation, Knowledge Graph
#         markdown_text = input_data
#         agents = {"Summarization": summarizer_agent, "Notes": notes_agent, "Explanation": explainer_agent, "Knowledge Graph": knowledge_graph_agent}
#         task_definitions = {
#             "Summarization": {"description": f"Summarize the document.\n\n---\n{markdown_text}\n---", "expected_output": "A concise summary."},
#             "Notes": {"description": f"Create revision notes.\n\n---\n{markdown_text}\n---", "expected_output": "Well-organized notes."},
#             "Explanation": {"description": f"Explain the topics simply.\n\n---\n{markdown_text}\n---", "expected_output": "A simple explanation."},
#             "Knowledge Graph": {"description": f"Create a Graphviz DOT flowchart from the document.\n\n---\n{markdown_text}\n---", "expected_output": "A string containing ONLY the Graphviz DOT language code."}
#         }
#         agent = agents[module]
#         task_details = task_definitions[module]
#         task = Task(description=task_details['description'], expected_output=task_details['expected_output'], agent=agent)
#         return Crew(tasks=[task], agents=[agent]), None

# HFAIQUIZ
# # crew/crew_factory.py
# from crewai import Task, Crew, Agent, Process
# import json5 as json

# # Import the static agent INSTANCES.
# from agents.summarizer import summarizer_agent
# from agents.notes import notes_agent
# from agents.explainer import explainer_agent
# from agents.planner import planner_agent
# from agents.critic import critic_agent
# from agents.refiner import refiner_agent
# from agents.knowledge_graph import knowledge_graph_agent
# from agents.mcq import mcq_generator_agent
# from agents.mcq_critic import mcq_critic_agent
# from agents.mcq_refiner import mcq_refiner_agent
# from agents.distractor_generator import distractor_agent
# from agents.distractor_critic import distractor_critic_agent
# from agents.distractor_refiner import distractor_refiner_agent
# from agents.quiz_taker_agent import quiz_taker_agent

# def get_crew(module: str, input_data: str, difficulty: str = None, bloom_q_counts: dict = None, strategic_plan_data: list = None):

#     if module == "Strategic Plan":
#         markdown_text = input_data
#         task_plan = Task(
#             description=f"""
# Analyze the document below and create a comprehensive pedagogical plan.
# 1.  Identify every distinct topic and sub-topic.
# 2.  For each topic, you must provide scores for 'relevance' and 'completeness' based on the strict rubric in the expected output.
# 3.  For each topic, devise a draft 'teaching_strategy' and a draft 'rationale' explaining it.

# --- DOCUMENT ---
# {markdown_text}
# --- END DOCUMENT ---
# """,
#             expected_output="""
# A single JSON list of objects. The output MUST be only the raw JSON.
# Each object MUST contain 'topic', 'relevance', 'completeness', 'teaching_strategy', and 'rationale'.

# **STRICT SCORING RUBRIC:**
# Relevance (1-5): 1-Trivial, 2-Peripheral, 3-Supporting, 4-Core, 5-Foundational.
# Completeness (1-5): 1-Hinted, 2-Mentioned, 3-Sufficient, 4-Thorough, 5-Exhaustive.

# **EXAMPLE FORMAT:**
# [
#   {
#     "topic": "Definition of a Complex Number",
#     "relevance": 5,
#     "completeness": 5,
#     "teaching_strategy": "Start with the equation x^2 = -1 to motivate the need for 'i', then introduce the a+ib form.",
#     "rationale": "This contextual approach enhances student engagement."
#   }
# ]
# """,
#             agent=planner_agent
#         )
#         task_critique = Task(description="Rigorously critique the received JSON teaching plan. Evaluate scores, strategies, and rationales.", expected_output="A bulleted list of specific, actionable critiques for the strategic plan.", agent=critic_agent, context=[task_plan])
#         task_refine_plan = Task(description="Take the draft teaching plan and the critiques. Produce a final, perfected JSON plan, including a 'refined_rationale' for each item.", expected_output="The final, polished JSON list of objects, incorporating all feedback.", agent=refiner_agent, context=[task_plan, task_critique])
#         crew = Crew(agents=[planner_agent, critic_agent, refiner_agent], tasks=[task_plan, task_critique, task_refine_plan], process=Process.sequential)
#         return crew, None

#     elif module == "MCQ Generation":
#         topic_obj = json.loads(input_data)
#         difficulty_instruction = f"The overall difficulty of the questions should be **{difficulty.upper()}**.\n" if difficulty else ""
        
#         bloom_counts_instruction = ""
#         if bloom_q_counts:
#             bloom_counts_instruction = "\nGenerate the following number of questions for each Bloom's Taxonomy level:\n"
#             for level, count in bloom_q_counts.items():
#                 if count > 0:
#                     bloom_counts_instruction += f"-   **{level}**: {count} question(s)\n"
#             bloom_counts_instruction += "If a count for a level is 0, you MUST NOT generate a question for that level.\n"
        
#         task_generate = Task(
#             description=f"""
# You are an expert at generating educational content. Based on the single topic JSON provided below, create a set of multiple-choice questions.
# {difficulty_instruction}
# {bloom_counts_instruction}
# **CRITICAL INSTRUCTIONS:**
# 1.  You MUST identify and include a specific `domain` and `bloom_level` for each question.
# 2.  Each question object MUST contain all the fields described in the format example.
# 3.  The `correct_answer` MUST be the full text of the option, not just a letter like 'A' or 'B'.
# 4.  For any mathematical equations or symbols, you MUST use LaTeX formatting (e.g., `$z = a + ib$`).

# **EXAMPLE OF THE REQUIRED FINAL OUTPUT STRUCTURE:**
# {{
#   "mcqs": [
#     {{
#       "domain": "Complex Numbers",
#       "bloom_level": "Remember",
#       "topic": "Topic Name from Input",
#       "question": "What is the definition of an imaginary unit?",
#       "options": ["$i^2 = 1$", "$i^2 = -1$", "$i = -1$", "$i = 1$"],
#       "correct_answer": "$i^2 = -1$",
#       "rationale": "The imaginary unit 'i' is fundamentally defined by the property that its square is -1."
#     }}
#   ]
# }}

# --- SINGLE TOPIC JSON ---
# {input_data}
# --- END SINGLE TOPIC JSON ---
# """,
#             expected_output='A single JSON object with the key "mcqs" containing a list of draft question objects, where each object includes a "domain" and "bloom_level".',
#             agent=mcq_generator_agent,
#         )
#         task_critique = Task(
#             description="Rigorously review the provided MCQs. Check for domain accuracy, Bloom's level alignment, clarity, and correctness.",
#             expected_output="A bulleted list of actionable critiques for the generated MCQs.",
#             agent=mcq_critic_agent,
#             context=[task_generate]
#         )
#         task_refine = Task(
#             description="Refine the MCQs based on the provided critique.",
#             expected_output='''The final, polished JSON object. This object MUST have two keys:
# 1.  `"status"`: with the string value `"refined"`.
# 2.  `"mcqs"`: containing the list of the refined question objects.
# THIS IS THE ONLY THING YOU MUST OUTPUT.''',
#             agent=mcq_refiner_agent,
#             context=[task_generate, task_critique]
#         )

#         crew = Crew(agents=[mcq_generator_agent, mcq_critic_agent, mcq_refiner_agent], tasks=[task_generate, task_critique, task_refine], process=Process.sequential)
#         return crew, "mcq_generation"

#     elif module == "Distractor Generation":
#         q_obj = json.loads(input_data)
        
#         task_generate_distractors = Task(
#             description=f"""
#             For the question '{q_obj['question']}' and its correct answer '{q_obj['answer']}', you must generate 3 distinct, plausible, and compellingly incorrect answer options (distractors).
#             For each of the 3 distractors, you MUST provide a "misleading_rationale" that explains the specific misconception or error a student would make to choose that option.
            
#             **CRITICAL INSTRUCTION:** For any mathematical equations or symbols in the options or rationales, you MUST use LaTeX formatting (e.g., `$z = a + ib$`).
#             """,
#             expected_output="""A single JSON list of exactly 3 objects. Each object must have two keys: "option" (the distractor text) and "misleading_rationale".
            
#             Example:
#             [
#               {
#                 "option": "The value is $x^2$",
#                 "misleading_rationale": "This is tempting because it forgets to take the square root, $\\sqrt{x^2}$."
#               }
#             ]
#             """,
#             agent=distractor_agent
#         )

#         task_critique_distractors = Task(
#             description=f"""
#             Rigorously evaluate the generated distractors and their rationales for the question: '{q_obj['question']}'.
#             Ensure they are plausible but unambiguously incorrect. Critique any options that are too obvious, poorly worded, or could be argued as correct.
#             Provide a bulleted list of actionable feedback for improvement.
#             """,
#             expected_output="A concise, bulleted list of feedback for improving the distractors.",
#             agent=distractor_critic_agent,
#             context=[task_generate_distractors]
#         )

#         task_refine_distractors = Task(
#             description="""
#             Based on the initial distractors and the expert critique provided, produce a final, high-quality set of three incorrect answer options.
#             You must refine the "option" text based on the feedback, but PRESERVE the original "misleading_rationale" for each option.
#             """,
#             expected_output='''A single JSON list of exactly 3 objects. Each object must have two keys: "option" (the refined distractor text) and "misleading_rationale".
            
#             Example:
#             [
#               {"option": "Final Refined Option A", "misleading_rationale": "This option is tempting because..."},
#               {"option": "Final Refined Option B", "misleading_rationale": "This is a common mistake..."}
#             ]
#             ''',
#             agent=distractor_refiner_agent,
#             context=[task_generate_distractors, task_critique_distractors]
#         )
        
#         crew = Crew(
#             agents=[distractor_agent, distractor_critic_agent, distractor_refiner_agent],
#             tasks=[task_generate_distractors, task_critique_distractors, task_refine_distractors],
#             process=Process.sequential
#         )
#         return crew, "distractor_generation"

#     elif module == "AI Quiz Taker":
#         q_obj = json.loads(input_data)
        
#         options_list = "\n".join([f"- {opt}" for opt in q_obj['options']])
        
#         task_answer_question = Task(
#             description=f"""
#             Attempt the following multiple-choice question. Read the question and the options carefully.
#             Your final answer MUST be ONLY the full text of the option you believe is correct. Do not add any extra words or explanation.

#             --- QUESTION ---
#             {q_obj['question']}

#             --- OPTIONS ---
#             {options_list}
#             """,
#             expected_output="The full text of the single best answer option.",
#             agent=quiz_taker_agent
#         )

#         crew = Crew(
#             agents=[quiz_taker_agent],
#             tasks=[task_answer_question],
#             process=Process.sequential
#         )
#         return crew, "ai_quiz_taker"

#     else: # Handles Summarization, Notes, Explanation, Knowledge Graph
#         markdown_text = input_data
#         agents = {"Summarization": summarizer_agent, "Notes": notes_agent, "Explanation": explainer_agent, "Knowledge Graph": knowledge_graph_agent}
#         task_definitions = {
#             "Summarization": {"description": f"Summarize the document.\n\n---\n{markdown_text}\n---", "expected_output": "A concise summary."},
#             "Notes": {"description": f"Create revision notes.\n\n---\n{markdown_text}\n---", "expected_output": "Well-organized notes."},
#             "Explanation": {"description": f"Explain the topics simply.\n\n---\n{markdown_text}\n---", "expected_output": "A simple explanation."},
#             "Knowledge Graph": {"description": f"Create a Graphviz DOT flowchart from the document.\n\n---\n{markdown_text}\n---", "expected_output": "A string containing ONLY the Graphviz DOT language code."}
#         }
#         agent = agents[module]
#         task_details = task_definitions[module]
#         task = Task(description=task_details['description'], expected_output=task_details['expected_output'], agent=agent)
#         return Crew(tasks=[task], agents=[agent]), None
# Local Loading of model

# crew_factory.py
from crewai import Task, Crew, Agent, Process
import json5 as json

# Import the static agent INSTANCES.
from agents.summarizer import summarizer_agent
from agents.notes import notes_agent
from agents.explainer import explainer_agent
from agents.planner import planner_agent
from agents.critic import critic_agent
from agents.refiner import refiner_agent
from agents.knowledge_graph import knowledge_graph_agent
from agents.mcq import mcq_generator_agent
from agents.mcq_critic import mcq_critic_agent
from agents.mcq_refiner import mcq_refiner_agent
from agents.distractor_generator import distractor_agent
from agents.distractor_critic import distractor_critic_agent
from agents.distractor_refiner import distractor_refiner_agent


def get_crew(module: str, input_data: str, difficulty: str = None, bloom_q_counts: dict = None):
    """
    Factory function to create and configure a crewai Crew for a specific task.
    """
    # --- STRATEGIC PLAN MODULE ---
    if module == "Strategic Plan":
        markdown_text = input_data
        task_plan = Task(
            description=f"""
As an expert Pedagogical Content Analyst, your task is to create a comprehensive pedagogical plan from the document below.
Your plan must be a JSON list of topics. For each topic, you must:
1.  Identify the topic name precisely.
2.  Critically evaluate the topic against the five RACAR metrics, providing a score from 1-5 based on the strict rubric. Be realistic; not every topic will be a 5.
3.  Devise a creative and effective 'teaching_strategy'.
4.  Write a clear 'rationale' explaining why your proposed strategy is pedagogically sound for that topic.

--- DOCUMENT ---
{markdown_text}
--- END DOCUMENT ---
""",
            expected_output="""
A single JSON list of objects. Each object MUST contain all 8 specified keys.

**STRICT RACAR SCORING RUBRIC (1-5 Scale):**
- **Relevance**: 5: Foundational, 4: Core, 3: Supporting, 2: Peripheral, 1: Trivial.
- **Accuracy**: 5: Authoritative, 4: Verified, 3: Plausible, 2: Questionable, 1: Inaccurate.
- **Completeness**: 5: Exhaustive, 4: Thorough, 3: Sufficient, 2: Mentioned, 1: Hinted.
- **Adaptability**: 5: Versatile, 4: Flexible, 3: Adaptable, 2: Inflexible, 1: Rigid.
- **Rigour**: 5: Expert, 4: Advanced, 3: Intermediate, 2: Basic, 1: Simplistic.

**FEW-SHOT EXAMPLES:**
[
  {
    "topic": "Introduction to Differential Equations",
    "relevance": 5,
    "accuracy": 5,
    "completeness": 3,
    "adaptability": 5,
    "rigour": 2,
    "teaching_strategy": "Start with a relatable real-world analogy, like modeling the cooling of a cup of coffee, to introduce the concept of rates of change.",
    "rationale": "An introductory topic is foundational (Relevance 5) but often not exhaustive (Completeness 3). The goal is to build intuition, not mastery, so the rigour is basic."
  },
  {
    "topic": "Solving Homogeneous Differential Equations",
    "relevance": 4,
    "accuracy": 5,
    "completeness": 4,
    "adaptability": 3,
    "rigour": 4,
    "teaching_strategy": "Use a guided-discovery worksheet where students first verify a function's homogeneity, then apply the y=vx substitution to a pre-solved problem, and finally solve a new problem themselves.",
    "rationale": "This is a core, advanced topic (Rigour 4) that requires a specific procedural skill, making it less adaptable to other contexts (Adaptability 3)."
  }
]
""",
            agent=planner_agent
        )
        task_critique = Task(
            description="""As a skeptical Instructional Plan Reviewer, your job is to find flaws in the proposed plan.
Be extremely critical of the RACAR scores. Is a score of 5 truly justified? An "Introduction" topic should NOT have a completeness of 5. Challenge every high score and demand justification.
Assess if the teaching strategies are creative and genuinely effective or just generic. Provide direct, constructive feedback.""", 
            expected_output="A bulleted list of sharp, actionable critiques. For each point, state the topic and the specific issue (e.g., 'Topic X: Completeness score is inflated from 5 to 3 because...').", 
            agent=critic_agent, 
            context=[task_plan]
        )
        task_refine_plan = Task(
            description="As the Lead Curriculum Strategist, synthesize the draft plan and the skeptical critiques. You MUST adjust scores and strategies based on valid points from the critique. Produce a final, perfected JSON plan, including a 'refined_rationale' that explains the improvements.",
            expected_output="A single, complete, and valid JSON list of objects wrapped in a markdown block (```json ... ```). Your entire response MUST be ONLY this markdown block.",
            agent=refiner_agent,
            context=[task_plan, task_critique]
        )
        return Crew(agents=[planner_agent, critic_agent, refiner_agent], tasks=[task_plan, task_critique, task_refine_plan], process=Process.sequential, share_crew=False), None

    # --- MCQ GENERATION MODULE ---
    elif module == "MCQ Generation":
        topic_obj = json.loads(input_data)
        difficulty_instruction = f"The overall difficulty of the questions should be **{difficulty.upper()}**."
        bloom_counts_instruction = "\nGenerate exactly the following number of questions for each Bloom's Taxonomy level:\n" + "".join([f"- **{level}**: {count} question(s)\n" for level, count in bloom_q_counts.items() if count > 0]) + "If a count for a level is 0, do not generate a question for that level."
        
        task_generate = Task(
            description=f"""
As an expert in educational assessment, generate a set of multiple-choice questions for the topic provided below.
{difficulty_instruction}
{bloom_counts_instruction}

**CRITICAL INSTRUCTIONS:**
1.  You MUST include the `domain` and `bloom_level` for each question.
2.  The `options` list must contain exactly four strings. **DO NOT** include labels like 'a)', 'b)', etc.
3.  The `correct_answer` MUST be the full text of the option.
4.  All mathematical notation MUST use LaTeX formatting (e.g., `$z = a + ib$`).

--- TOPIC DATA ---
{input_data}
--- END TOPIC DATA ---
""",
            expected_output='''A single JSON object with a key "mcqs" containing a list of question objects.

**FEW-SHOT EXAMPLE OF A QUESTION OBJECT:**
{
  "domain": "Complex Numbers",
  "bloom_level": "Remember",
  "topic": "Introduction to Complex Numbers",
  "question": "What is the value of $i^2$?",
  "options": [
    "1",
    "-1",
    "i",
    "-i"
  ],
  "correct_answer": "-1",
  "rationale": "The imaginary unit 'i' is defined by the property that its square is -1."
}
''',
            agent=mcq_generator_agent,
        )
        task_critique = Task(
            description="As an MCQ Quality Reviewer, rigorously review the generated questions. Check for clarity, accuracy, pedagogical soundness, and correct alignment with the specified Bloom's level. Provide specific, actionable feedback.",
            expected_output="A bulleted list of actionable critiques. For each point, specify which question it refers to.",
            agent=mcq_critic_agent,
            context=[task_generate]
        )
        task_refine = Task(
            description="As an MCQ Content Polisher, refine the questions based on the critique. Your final output MUST be a single JSON object wrapped in a markdown block.",
            expected_output='''A final JSON object with two keys: "status": "refined", and "mcqs": [...].
The entire response MUST be a single JSON markdown block: ```json ... ```
''',
            agent=mcq_refiner_agent,
            context=[task_generate, task_critique]
        )
        return Crew(agents=[mcq_generator_agent, mcq_critic_agent, mcq_refiner_agent], tasks=[task_generate, task_critique, task_refine], process=Process.sequential, share_crew=False), "mcq_generation"
    
    # --- DISTRACTOR GENERATION MODULE ---
    elif module == "Distractor Generation":
        q_obj = json.loads(input_data)
        task_generate = Task(
            description=f"""
As a Cunning Educational Saboteur, create 3 compellingly incorrect answer options (distractors) for the question below.
For each distractor, provide a 'misleading_rationale' that targets a specific, common student misconception. All math must use LaTeX.

--- QUESTION & ANSWER ---
Question: {q_obj['question']}
Correct Answer: {q_obj['answer']}
""",
            expected_output='''A JSON list of exactly 3 objects. Each object must have "option" and "misleading_rationale" keys.

**FEW-SHOT EXAMPLES:**
[
  {
    "option": "The value is $x^2$",
    "misleading_rationale": "This is tempting because it forgets the final step of taking the square root, a common procedural error."
  },
  {
    "option": "An equation with only one variable",
    "misleading_rationale": "This confuses the concept of an 'unknown function' with a simple 'variable', targeting a foundational misunderstanding."
  }
]
''',
            agent=distractor_agent
        )
        task_critique = Task(
            description="As a Quality Assurance Expert, rigorously evaluate the 3 generated distractors. Are they genuinely plausible? Is the misleading rationale targeting a valid misconception? Provide a concise, bulleted list of feedback.",
            expected_output="A concise, bulleted list of actionable feedback.",
            agent=distractor_critic_agent,
            context=[task_generate]
        )
        task_refine = Task(
            description="As an Assessment Editor, refine the distractors based on the critique. Preserve the 'misleading_rationale'. Your final output must be a single JSON list of objects wrapped in a markdown block.",
            expected_output='''A single JSON list of exactly 3 objects wrapped in a markdown block (```json ... ```). Each object must have "option" and "misleading_rationale" keys.
''',
            agent=distractor_refiner_agent,
            context=[task_generate, task_critique]
        )
        return Crew(agents=[distractor_agent, distractor_critic_agent, distractor_refiner_agent], tasks=[task_generate, task_critique, task_refine], process=Process.sequential, share_crew=False), "distractor_generation"


    # --- SIMPLE MODULES ---
    else:
        markdown_text = input_data
        agents = {"Summarization": summarizer_agent, "Notes": notes_agent, "Explanation": explainer_agent, "Knowledge Graph": knowledge_graph_agent}
        task_definitions = {
            "Summarization": {
                "description": f"As an Expert Technical Writer, create a professional summary of the document below. Start with a single-sentence overview, followed by a bulleted list of the 3-5 most important key points.\n\n---\n{markdown_text}\n---", 
                "expected_output": "A well-structured summary with an overview sentence and a bulleted list of key points. DO NOT include minor details."
            },
            "Notes": {
                "description": f"As a Master Student, create detailed, structured revision notes from the document below. Use markdown for headings, subheadings, and nested bullet points to create a clear information hierarchy.\n\n---\n{markdown_text}\n---", 
                "expected_output": "Well-organized, hierarchical notes in markdown format. DO NOT write long paragraphs."
            },
            "Explanation": {
                "description": f"As a skilled Science Communicator, take the complex topics in the document below and explain them in simple terms suitable for a complete beginner. Use analogies and define any essential jargon.\n\n---\n{markdown_text}\n---", 
                "expected_output": "A simplified explanation of the core concepts. DO NOT assume any prior knowledge."
            },
            "Knowledge Graph": {
                "description": f"As a Curriculum Architect, create a learning path flowchart from the document below. The output MUST be only valid Graphviz DOT language code. Use short, clear labels for nodes.\n\n---\n{markdown_text}\n---", 
                "expected_output": "A string containing ONLY valid Graphviz DOT language code, starting with `digraph` and ending with `}`. DO NOT include any explanation, preamble, or markdown fences."
            }
        }
        agent = agents.get(module)
        task_details = task_definitions.get(module)
        if not agent or not task_details:
             raise ValueError(f"Invalid module: {module}")
        task = Task(description=task_details['description'], expected_output=task_details['expected_output'], agent=agent)
        return Crew(tasks=[task], agents=[agent], share_crew=False), None