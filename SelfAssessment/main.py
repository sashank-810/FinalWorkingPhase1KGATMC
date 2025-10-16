# import streamlit as st
# import tempfile
# from core.indexing import load_and_index
# from crew.crew_factory import get_crew
# from utils.pdf_export import convert_markdown_to_pdf
# For pdfs
# # Initialize session state variables
# if "markdown_content" not in st.session_state:
#     st.session_state.markdown_content = None

# if "pipeline_ran" not in st.session_state:
#     st.session_state.pipeline_ran = False

# if "pdf_path" not in st.session_state:
#     st.session_state.pdf_path = None


# st.set_page_config(page_title="StudyForge", layout="wide")
# st.title("📚 StudyForge: Modular Exam Assistant")
# st.markdown("Choose a module and upload a PDF to get started!")

# module = st.sidebar.selectbox(
#     "Select a module",
#     ["Summarization", "Notes", "MCQs", "Explanation", "Web Search", "YouTube"]
# )

# uploaded_pdf = st.sidebar.file_uploader("Upload PDF", type=["pdf"])

# if uploaded_pdf and st.sidebar.button("Run"):
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
#         tmp_file.write(uploaded_pdf.read())
#         pdf_path = tmp_file.name

#     with st.spinner(f"Running {module} agent..."):
#         vector_index = load_and_index(pdf_path)
#         crew = get_crew(module, vector_index)
#         result = crew.kickoff()

#         # --- THIS IS THE CORRECTED PART ---
#         # We check if the result exists and then extract the raw string from the CrewOutput object.
#         if result:
#             st.session_state.markdown_content = result.raw
#         else:
#             st.session_state.markdown_content = "Error: The crew did not return a result."
#             st.error("Crew execution failed to produce an output. Please check the logs.")
#         # ------------------------------------
        
#         st.success("Done!")

# # This block now handles the output correctly because markdown_content is a string.
# if st.session_state.get("markdown_content"):
#     st.subheader("📝 Output")
#     st.markdown(st.session_state.markdown_content, unsafe_allow_html=True)
    
#     st.download_button(
#         label="📥 Download Markdown",
#         data=st.session_state.markdown_content,
#         file_name="study_guide.md",
#         mime="text/markdown"
#     )

#     # Adding a try-except block for PDF conversion is good practice
#     try:
#         pdf_bytes = convert_markdown_to_pdf(st.session_state.markdown_content)
#         st.download_button(
#             label="📥 Download as PDF (.pdf)",
#             data=pdf_bytes,
#             file_name="study_guide.pdf",
#             mime="application/pdf",
#             use_container_width=True
#         )
#     except Exception as e:
#         st.warning(f"Could not generate PDF. Error: {e}")

# else:
#     st.info("Upload a PDF and run a module to see the output.")



# main.py (Modified for Markdown)
# # main.py

# import streamlit as st
# import re
# from crew.crew_factory import get_crew
# from utils.pdf_export import convert_markdown_to_pdf # Assuming you have this utility

# # --- Helper Function to Parse MCQs ---
# def parse_mcqs(raw_text):
#     """Parses the raw text from the AI to extract MCQs and explanations."""
#     questions = []
#     question_blocks = re.split(r'\n(?=\d+\.\s)', raw_text.strip())
    
#     for block in question_blocks:
#         if not block.strip(): continue
            
#         lines = [line.strip() for line in block.strip().split('\n') if line.strip()]
#         if not lines: continue

#         question_text = lines[0]
#         options = []
#         correct_answer = None
#         explanation = "No explanation was provided." # Default text

#         remaining_lines = []
#         for line in lines[1:]:
#             if line.lower().startswith("explanation:"):
#                 explanation = line[12:].strip()
#             else:
#                 remaining_lines.append(line)
        
#         for line in remaining_lines:
#             is_correct = line.startswith('*')
#             clean_option = re.sub(r'^\*?\s*[a-d][.)]\s*', '', line).strip()
#             options.append(clean_option)
#             if is_correct: correct_answer = clean_option
        
#         if question_text and len(options) == 4 and correct_answer:
#             questions.append({
#                 "question": question_text,
#                 "options": options,
#                 "correct_answer": correct_answer,
#                 "explanation": explanation
#             })
#     return questions

# # --- Session State Initialization ---
# def init_session_state():
#     if "module_ran" not in st.session_state:
#         reset_all_state()

# def reset_all_state():
#     """Hard resets the state for a new run."""
#     st.session_state.module_ran = None
#     st.session_state.markdown_output = None
#     st.session_state.questions = []
#     st.session_state.user_answers = {}
#     st.session_state.quiz_submitted = False

# # --- UI Rendering ---
# st.set_page_config(page_title="StudyForge", layout="wide")
# st.title("📚 StudyForge: Your Content Assistant")

# init_session_state()

# # --- Sidebar Controls ---
# with st.sidebar:
#     st.header("Controls")
#     module = st.sidebar.selectbox("Select a module", ["Summarization", "Notes", "MCQs", "Explanation"])
    
#     # --- THIS IS THE MODIFIED SECTION ---
#     num_mcqs = 5 # Default value
#     if module == "MCQs":
#         num_mcqs = st.number_input(
#             "Number of MCQs", 
#             min_value=1, 
#             # max_value=20,  <-- THIS LINE HAS BEEN REMOVED
#             value=5, 
#             step=1,
#             help="Select how many questions to generate. Note: large numbers may take longer."
#         )

#     uploaded_md = st.file_uploader("Upload Markdown", type=["md", "txt"])

#     if st.button("Run"):
#         if uploaded_md:
#             with st.spinner(f"Running {module} module..."):
#                 reset_all_state()
#                 st.session_state.module_ran = module
#                 markdown_text = uploaded_md.read().decode("utf-8")
#                 crew = get_crew(module, markdown_text, num_mcqs)
#                 result = crew.kickoff()
#                 if result:
#                     st.session_state.markdown_output = result.raw
#                     if module == "MCQs":
#                         st.session_state.questions = parse_mcqs(result.raw)
#                         st.session_state.user_answers = {i: None for i in range(len(st.session_state.questions))}
#             st.success("Content Generated!")
#         else:
#             st.warning("Please upload a Markdown file first.")

# # --- Main Page Logic (No changes in this section) ---

# if not st.session_state.module_ran:
#     st.info("Upload a Markdown file and click 'Run' to begin.")

# elif st.session_state.module_ran == "MCQs":
#     if not st.session_state.questions:
#         st.error("Failed to generate or parse the quiz. Please check the uploaded file or try again.")
#     elif not st.session_state.quiz_submitted:
#         st.header("Attempt the Quiz")
#         for i, q in enumerate(st.session_state.questions):
#             st.markdown(f"**{q.get('question', 'Error: Question not found.')}**")
#             st.session_state.user_answers[i] = st.radio("Options", q.get('options', []), key=f"q_{i}", label_visibility="collapsed", index=None)
#             st.markdown("---")
        
#         all_answered = all(st.session_state.user_answers.get(i) is not None for i in range(len(st.session_state.questions)))
#         if st.button("Submit Answers", type="primary", disabled=not all_answered):
#             st.session_state.quiz_submitted = True
#             st.rerun()
#         if not all_answered:
#             st.warning("Please answer all questions before submitting.")

#     else: # Quiz has been submitted
#         st.header("Quiz Results")
#         score = sum(1 for i, q in enumerate(st.session_state.questions) if st.session_state.user_answers.get(i) == q.get('correct_answer'))
#         total_questions = len(st.session_state.questions)
#         st.success(f"**Your final score: {score} out of {total_questions}**")
#         st.markdown("---")

#         for i, q in enumerate(st.session_state.questions):
#             st.markdown(f"**{q.get('question', 'Error: Question not found.')}**")
#             user_answer, correct_answer = st.session_state.user_answers.get(i), q.get('correct_answer')
            
#             for option in q.get('options', []):
#                 label = f"- {option}"
#                 if option == correct_answer:
#                     st.success(f"✅ {label} (Correct Answer)")
#                 elif option == user_answer:
#                     st.error(f"❌ {label} (Your Answer)")
#                 else:
#                     st.write(label)
            
#             explanation = q.get('explanation', "No explanation was provided for this question.")
#             st.info(f"💡 **Explanation:** {explanation}")
#             st.markdown("---")

#         if st.button("Try Another Module"):
#             reset_all_state()
#             st.rerun()
# else:
#     if st.session_state.markdown_output:
#         st.header(f"Output for {st.session_state.module_ran}")
#         st.markdown(st.session_state.markdown_output, unsafe_allow_html=True)
#         st.download_button(label="📥 Download Markdown", data=st.session_state.markdown_output, file_name=f"{st.session_state.module_ran.lower()}_output.md", mime="text/markdown")
#     else:
#         st.info("Click 'Run' to generate content for the selected module.")

# crew/crew_factory.py

# main.py

# import streamlit as st
# import re
# from crew.crew_factory import get_crew
# from utils.pdf_export import convert_markdown_to_pdf # Assuming you have this utility

# # --- Helper Function to Parse MCQs ---
# def parse_mcqs(raw_text):
#     """Parses the raw text from the AI to extract MCQs and explanations."""
#     questions = []
#     question_blocks = re.split(r'\n(?=\d+\.\s)', raw_text.strip())
    
#     for block in question_blocks:
#         if not block.strip(): continue
        
#         lines = [line.strip() for line in block.strip().split('\n') if line.strip()]
#         if not lines: continue

#         question_text = lines[0]
#         options = []
#         correct_answer = None
#         explanation = "No explanation was provided." # Default text

#         remaining_lines = []
#         for line in lines[1:]:
#             if line.lower().startswith("explanation:"):
#                 explanation = line[12:].strip()
#             else:
#                 remaining_lines.append(line)
        
#         for line in remaining_lines:
#             is_correct = line.startswith('*')
#             clean_option = re.sub(r'^\*?\s*[a-d][.)]\s*', '', line).strip()
#             options.append(clean_option)
#             if is_correct: correct_answer = clean_option
        
#         if question_text and len(options) == 4 and correct_answer:
#             questions.append({
#                 "question": question_text,
#                 "options": options,
#                 "correct_answer": correct_answer,
#                 "explanation": explanation
#             })
#     return questions

# # --- Session State Initialization ---
# def init_session_state():
#     if "module_ran" not in st.session_state:
#         reset_all_state()

# def reset_all_state():
#     """Hard resets the state for a new run."""
#     st.session_state.module_ran = None
#     st.session_state.markdown_output = None
#     st.session_state.questions = []
#     st.session_state.user_answers = {}
#     st.session_state.quiz_submitted = False

# # --- UI Rendering ---
# st.set_page_config(page_title="Spirit", layout="wide")
# st.title("Spirit MCQ")

# init_session_state()

# # --- Sidebar Controls ---
# with st.sidebar:
#     st.header("Controls")
#     module = st.sidebar.selectbox("Select a Module", ["Summarization", "Notes", "MCQs", "Explanation"])
    
#     # --- MCQ Specific Controls ---
#     num_mcqs = 5
#     difficulty = "Medium" # Default value
#     if module == "MCQs":
#         difficulty = st.selectbox(
#             "Question Difficulty",
#             ("Easy", "Medium", "Hard"),
#             index=1, # Default to Medium
#             help="Easy: Factual recall. Medium: Application. Hard: Synthesis & Analysis."
#         )
#         num_mcqs = st.number_input(
#             "Number of MCQs", 
#             min_value=1, 
#             value=5, 
#             step=1,
#             help="Select how many questions you want to generate."
#         )

#     uploaded_md = st.file_uploader("Upload Markdown", type=["md", "txt"])

#     if st.button("Run"):
#         if uploaded_md:
#             with st.spinner(f"Running {module} module..."):
#                 reset_all_state()
#                 st.session_state.module_ran = module
#                 markdown_text = uploaded_md.read().decode("utf-8")
#                 # Pass all relevant parameters to the factory
#                 crew = get_crew(module, markdown_text, num_mcqs, difficulty)
#                 result = crew.kickoff()
#                 if result:
#                     st.session_state.markdown_output = result.raw
#                     if module == "MCQs":
#                         st.session_state.questions = parse_mcqs(result.raw)
#                         st.session_state.user_answers = {i: None for i in range(len(st.session_state.questions))}
#             st.success("Content Generated!")
#         else:
#             st.warning("Please upload a Markdown file first.")

# # --- Main Page Logic ---

# if not st.session_state.module_ran:
#     st.info("Upload a Markdown file and click 'Run' to begin.")

# elif st.session_state.module_ran == "MCQs":
#     if not st.session_state.questions:
#         st.error("Failed to generate or parse the quiz. Please check the uploaded file or try again.")
#     elif not st.session_state.quiz_submitted:
#         st.header("Attempt the Quiz")
#         for i, q in enumerate(st.session_state.questions):
#             st.markdown(f"**{q.get('question', 'Error: Question not found.')}**")
#             st.session_state.user_answers[i] = st.radio("Options", q.get('options', []), key=f"q_{i}", label_visibility="collapsed", index=None)
#             st.markdown("---")
        
#         all_answered = all(st.session_state.user_answers.get(i) is not None for i in range(len(st.session_state.questions)))
#         if st.button("Submit Answers", type="primary", disabled=not all_answered):
#             st.session_state.quiz_submitted = True
#             st.rerun()
#         if not all_answered:
#             st.warning("Please answer all questions before submitting.")

#     else: # Quiz has been submitted
#         st.header("Quiz Results")
#         score = sum(1 for i, q in enumerate(st.session_state.questions) if st.session_state.user_answers.get(i) == q.get('correct_answer'))
#         total_questions = len(st.session_state.questions)
#         st.success(f"**Your final score: {score} out of {total_questions}**")
#         st.markdown("---")

#         for i, q in enumerate(st.session_state.questions):
#             st.markdown(f"**{q.get('question', 'Error: Question not found.')}**")
#             user_answer, correct_answer = st.session_state.user_answers.get(i), q.get('correct_answer')
            
#             for option in q.get('options', []):
#                 label = f"- {option}"
#                 if option == correct_answer:
#                     st.success(f"✅ {label} (Correct Answer)")
#                 elif option == user_answer:
#                     st.error(f"❌ {label} (Your Answer)")
#                 else:
#                     st.write(label)
            
#             explanation = q.get('explanation', "No explanation was provided for this question.")
#             st.info(f"💡 **Explanation:** {explanation}")
#             st.markdown("---")

#         if st.button("Try Another Module"):
#             reset_all_state()
#             st.rerun()
# else:
#     if st.session_state.markdown_output:
#         st.header(f"Output for {st.session_state.module_ran}")
#         st.markdown(st.session_state.markdown_output, unsafe_allow_html=True)
#         st.download_button(label="📥 Download Markdown", data=st.session_state.markdown_output, file_name=f"{st.session_state.module_ran.lower()}_output.md", mime="text/markdown")
#     else:
#         st.info("Click 'Run' to generate content for the selected module.")


# Knowledge Graph
# # main.py
# import streamlit as st
# import re
# import urllib.parse
# from crew.crew_factory import get_crew

# def parse_mcqs(raw_text):
#     questions = []
#     question_matches = re.finditer(r"(?s)(\d+\.\s)(.*?)(?=\n\d+\.\s|\Z)", raw_text)
#     for match in question_matches:
#         question_number = match.group(1).strip()
#         question_block = match.group(2).strip()
#         lines = [line.strip() for line in question_block.split('\n') if line.strip()]
#         if not lines: continue
#         question_text, options, explanation = lines[0], [], "No explanation was provided."
#         correct_answer, remaining_lines = None, []
#         for line in lines[1:]:
#             if line.lower().startswith("explanation:"): explanation = line[12:].strip()
#             else: remaining_lines.append(line)
#         for line in remaining_lines:
#             is_correct = line.startswith('*')
#             clean_option = re.sub(r'^\*?\s*[a-d][.)]\s*', '', line).strip()
#             options.append(clean_option)
#             if is_correct: correct_answer = clean_option
#         if question_text and len(options) == 4 and correct_answer:
#             full_question_text = f"{question_number} {question_text}"
#             questions.append({
#                 "question": full_question_text, "options": options,
#                 "correct_answer": correct_answer, "explanation": explanation
#             })
#     return questions

# def init_session_state():
#     if "module_ran" not in st.session_state:
#         reset_all_state()

# def reset_all_state():
#     st.session_state.module_ran, st.session_state.markdown_output = None, None
#     st.session_state.questions, st.session_state.user_answers = [], {}
#     st.session_state.quiz_submitted = False

# st.set_page_config(page_title="StudyForge", layout="wide")
# st.title("📚 StudyForge: Your Content Assistant")
# init_session_state()

# with st.sidebar:
#     st.header("Controls")
#     module = st.sidebar.selectbox("Select a module", ["Summarization", "Notes", "MCQs", "Explanation", "Knowledge Graph"])
#     num_mcqs, difficulty = 5, "Medium"
#     if module == "MCQs":
#         difficulty = st.selectbox("Question Difficulty", ("Easy", "Medium", "Hard"), index=1)
#         num_mcqs = st.number_input("Number of MCQs", min_value=1, value=5, step=1)
#     uploaded_md = st.file_uploader("Upload Markdown", type=["md", "txt"])
#     if st.button("Run"):
#         if uploaded_md:
#             with st.spinner(f"Running {module} module..."):
#                 reset_all_state()
#                 st.session_state.module_ran = module
#                 markdown_text = uploaded_md.read().decode("utf-8")
#                 crew = get_crew(module, markdown_text, num_mcqs, difficulty)
#                 result = crew.kickoff()
#                 if result:
#                     st.session_state.markdown_output = result.raw
#                     if module == "MCQs":
#                         st.session_state.questions = parse_mcqs(result.raw)
#                         st.session_state.user_answers = {i: None for i in range(len(st.session_state.questions))}
#             st.success("Content Generated!")
#         else:
#             st.warning("Please upload a Markdown file first.")

# if not st.session_state.module_ran:
#     st.info("Upload a Markdown file and click 'Run' to begin.")
# elif st.session_state.module_ran == "MCQs":
#     if not st.session_state.questions:
#         st.error("Failed to generate or parse quiz. The AI's output may be malformed. Please try again.")
#     elif not st.session_state.quiz_submitted:
#         st.header("Attempt the Quiz")
#         for i, q in enumerate(st.session_state.questions):
#             st.markdown(f"**{q.get('question')}**")
#             st.session_state.user_answers[i] = st.radio("Options", q.get('options', []), key=f"q_{i}", label_visibility="collapsed", index=None)
#             st.markdown("---")
#         all_answered = all(st.session_state.user_answers.get(i) is not None for i in range(len(st.session_state.questions)))
#         if st.button("Submit Answers", type="primary", disabled=not all_answered):
#             st.session_state.quiz_submitted = True
#             st.rerun()
#         if not all_answered: st.warning("Please answer all questions before submitting.")
#     else:
#         st.header("Quiz Results")
#         score = sum(1 for i, q in enumerate(st.session_state.questions) if st.session_state.user_answers.get(i) == q.get('correct_answer'))
#         total_questions = len(st.session_state.questions)
#         st.success(f"**Your final score: {score} out of {total_questions}**")
#         st.markdown("---")
#         for i, q in enumerate(st.session_state.questions):
#             st.markdown(f"**{q.get('question')}**")
#             user_answer, correct_answer = st.session_state.user_answers.get(i), q.get('correct_answer')
#             for option in q.get('options', []):
#                 if option == correct_answer: st.success(f"✅ {option} (Correct Answer)")
#                 elif option == user_answer: st.error(f"❌ {option} (Your Answer)")
#                 else: st.write(f"- {option}")
#             st.info(f"💡 **Explanation:** {q.get('explanation')}")
#             st.markdown("---")
#         if st.button("Try Another Module"):
#             reset_all_state()
#             st.rerun()
# elif st.session_state.module_ran == "Knowledge Graph":
#     st.header("Learning Path Flowchart")
#     if st.session_state.markdown_output:
#         match = re.search(r"digraph\s+\w+\s*\{.*\}", st.session_state.markdown_output, re.DOTALL)
#         if match:
#             dot_code = match.group(0)
#             st.write("### Flowchart Diagram")
#             try:
#                 st.graphviz_chart(dot_code)
#             except Exception:
#                 st.error("Could not render the diagram. Please ensure Graphviz is installed on your system.")
#                 st.code(dot_code, language='dot')
#         else:
#             st.error("Could not find a valid flowchart in the AI's output.")
#             st.code(st.session_state.markdown_output)
# else: 
#     if st.session_state.markdown_output:
#         st.header(f"Output for {st.session_state.module_ran}")
#         st.markdown(st.session_state.markdown_output, unsafe_allow_html=True)
#         st.download_button(f"📥 Download {st.session_state.module_ran}", st.session_state.markdown_output, f"{st.session_state.module_ran.lower().replace(' ', '_')}_output.md")

# Planner

# # main.py

# import streamlit as st
# import re
# import json5 as json
# from crew.crew_factory import get_crew

# def init_session_state():
#     if "module_ran" not in st.session_state:
#         reset_all_state()

# def reset_all_state():
#     st.session_state.module_ran = None
#     st.session_state.text_output = None

# # UI Rendering
# st.set_page_config(page_title="Spirit", layout="wide")
# st.title("Spirit")
# init_session_state()

# # Sidebar Controls
# with st.sidebar:
#     st.header("Controls")
#     # --- THIS IS THE CORRECTED DROPDOWN MENU ---
#     module = st.sidebar.selectbox(
#         "Select a module",
#         ["Summarization", "Notes", "Explanation", "Knowledge Graph", "Strategic Plan"]
#     )
#     uploaded_md = st.file_uploader("Upload Markdown", type=["md", "txt"])
#     if st.button("Run"):
#         if uploaded_md:
#             with st.spinner(f"Running {module} module..."):
#                 reset_all_state()
#                 st.session_state.module_ran = module
#                 markdown_text = uploaded_md.read().decode("utf-8")
                
#                 # The factory now handles all crew creation logic internally
#                 crew, _ = get_crew(module, markdown_text)
                
#                 result = crew.kickoff()
                
#                 # The final result is always the text output we want to display
#                 if result and hasattr(result, 'raw'):
#                     st.session_state.text_output = result.raw
                        
#             st.success("Content Generation Complete!")
#         else:
#             st.warning("Please upload a Markdown file first.")

# # Main Page Logic
# if not st.session_state.module_ran:
#     st.info("Upload a Markdown file and click 'Run' to begin.")

# # Block for displaying the JSON plan
# elif st.session_state.module_ran == "Strategic Plan":
#     st.header("Refined Strategic Plan")
#     if st.session_state.text_output:
#         match = re.search(r'\[.*\]', st.session_state.text_output, re.DOTALL)
#         if match:
#             json_string = match.group(0)
#             try:
#                 plan_data = json.loads(json_string)
#                 st.dataframe(plan_data)
#                 with st.expander("View Raw JSON"):
#                     st.json(plan_data)
#             except Exception as e:
#                 st.error(f"Could not parse the JSON plan. Error: {e}")
#                 st.code(json_string)
#         else:
#             st.error("The AI did not return a recognizable JSON plan.")
#             st.code(st.session_state.text_output)

# # Block for displaying the visual flowchart
# elif st.session_state.module_ran == "Knowledge Graph":
#     st.header("Learning Path Flowchart")
#     if st.session_state.text_output:
#         dot_code = st.session_state.text_output
#         # Use regex to find the DOT code, ignoring any extra text
#         match = re.search(r"digraph\s+\w*\s*\{.*\}", dot_code, re.DOTALL)
#         if match:
#             clean_dot_code = match.group(0)
#             try:
#                 st.graphviz_chart(clean_dot_code)
#             except Exception as e:
#                 st.error(f"Could not render the diagram directly. Error: {e}")
            
#             st.subheader("Final DOT Code")
#             st.code(clean_dot_code, language='dot')
#         else:
#             st.warning("The final output was not a valid flowchart. Displaying raw output:")
#             st.code(dot_code, language='text')

# # Block for all other standard text modules
# else: 
#     if st.session_state.text_output:
#         st.header(f"Output for {st.session_state.module_ran}")
#         st.markdown(st.session_state.text_output, unsafe_allow_html=True)
#         st.download_button(
#             label=f"📥 Download {st.session_state.module_ran}",
#             data=st.session_state.text_output,
#             file_name=f"{st.session_state.module_ran.lower().replace(' ', '_')}_output.md"
#         )
#     else:
#         st.info("Click 'Run' to generate content for the selected module.")

# Planner based questions
# # main.py

# import streamlit as st
# import re
# import json5 as json
# from crew.crew_factory import get_crew

# def init_session_state():
#     if "module_ran" not in st.session_state:
#         reset_all_state()
#     if "strategic_plan_output" not in st.session_state:
#         st.session_state.strategic_plan_output = None
#     if "mcq_output" not in st.session_state:
#         st.session_state.mcq_output = None
#     if "selected_difficulty" not in st.session_state:
#         st.session_state.selected_difficulty = "medium"
#     if "user_answers" not in st.session_state:
#         st.session_state.user_answers = {}
#     if "quiz_submitted" not in st.session_state:
#         st.session_state.quiz_submitted = False
#     if "mcq_data_parsed" not in st.session_state:
#         st.session_state.mcq_data_parsed = []
#     if "strategic_plan_parsed" not in st.session_state:
#         st.session_state.strategic_plan_parsed = []

# def reset_all_state():
#     st.session_state.module_ran = None
#     st.session_state.text_output = None
#     st.session_state.strategic_plan_output = None
#     st.session_state.user_answers = {}
#     st.session_state.quiz_submitted = False
#     st.session_state.mcq_data_parsed = []
#     st.session_state.strategic_plan_parsed = []
#     # st.session_state.selected_difficulty is intentionally not reset here

# # UI Rendering
# st.set_page_config(page_title="Spirit", layout="wide")
# st.title("Spirit")
# init_session_state()

# # Sidebar Controls
# with st.sidebar:
#     st.header("Controls")
    
#     module = st.sidebar.selectbox(
#         "Select a module",
#         ["Summarization", "Notes", "Explanation", "Knowledge Graph", "Strategic Plan", "MCQ Generation"]
#     )
    
#     if module == "MCQ Generation":
#         st.session_state.selected_difficulty = st.selectbox(
#             "Select Difficulty",
#             ["easy", "medium", "hard"],
#             index=["easy", "medium", "hard"].index(st.session_state.selected_difficulty)
#         )
    
#     uploaded_md = st.file_uploader("Upload Markdown", type=["md", "txt"])
    
#     mcq_from_plan_button = False
#     if module == "MCQ Generation":
#         if st.session_state.strategic_plan_output:
#             mcq_from_plan_button = st.button("Generate MCQs from Strategic Plan")
#         else:
#             st.info("Run 'Strategic Plan' first to generate MCQs.")

#     run_normal_module_button = st.button("Run Selected Module")

#     if run_normal_module_button:
#         if uploaded_md:
#             with st.spinner(f"Running {module} module..."):
#                 if module != "Strategic Plan":
#                     st.session_state.text_output = None
#                     st.session_state.mcq_output = None
#                     st.session_state.user_answers = {}
#                     st.session_state.quiz_submitted = False
#                     st.session_state.mcq_data_parsed = []

#                 st.session_state.module_ran = module
#                 markdown_text = uploaded_md.read().decode("utf-8")
                
#                 crew_difficulty = st.session_state.selected_difficulty if module == "MCQ Generation" else None
#                 crew, _ = get_crew(module, markdown_text, difficulty=crew_difficulty)
                
#                 result = crew.kickoff()
                
#                 if result and hasattr(result, 'raw'):
#                     raw_output = result.raw
#                     st.session_state.text_output = raw_output
                    
#                     if module == "Strategic Plan":
#                         match = re.search(r'\[.*\]', raw_output, re.DOTALL)
#                         if match:
#                             st.session_state.strategic_plan_output = match.group(0)
#                         else:
#                             st.error("Strategic Plan did not return a valid JSON format.")
#                             st.session_state.strategic_plan_output = None
                        
#             st.success("Content Generation Complete!")
#         else:
#             st.warning("Please upload a Markdown file first.")

#     if mcq_from_plan_button:
#         if st.session_state.strategic_plan_output:
#             with st.spinner("Generating MCQs from Strategic Plan..."):
#                 st.session_state.module_ran = "MCQ Generation"
#                 st.session_state.mcq_output = None
#                 st.session_state.user_answers = {}
#                 st.session_state.quiz_submitted = False
#                 st.session_state.mcq_data_parsed = []
                
#                 crew_difficulty = st.session_state.selected_difficulty
#                 crew, _ = get_crew("MCQ Generation", st.session_state.strategic_plan_output, difficulty=crew_difficulty)
                
#                 result = crew.kickoff()
                
#                 if result and hasattr(result, 'raw'):
#                     st.session_state.mcq_output = result.raw
                
#             st.success("MCQ Generation Complete!")
#         else:
#             st.warning("No Strategic Plan found to generate MCQs from. Please run 'Strategic Plan' first.")


# # Main Page Logic
# if not st.session_state.module_ran:
#     st.info("Upload a Markdown file and click 'Run Selected Module' to begin.")

# elif st.session_state.module_ran == "Strategic Plan":
#     st.header("Refined Strategic Plan")
#     if st.session_state.strategic_plan_output:
#         try:
#             plan_data = json.loads(st.session_state.strategic_plan_output)
#             st.dataframe(plan_data)
#             with st.expander("View Raw JSON"):
#                 st.json(plan_data)
            
#             st.session_state.strategic_plan_parsed = plan_data 
            
#             if st.button(f"Generate {st.session_state.selected_difficulty.capitalize()} MCQs from this Plan"):
#                 st.session_state.module_ran = "MCQ Generation"
#                 st.session_state.mcq_output = None
#                 st.session_state.user_answers = {}
#                 st.session_state.quiz_submitted = False
#                 st.session_state.mcq_data_parsed = []
                
#                 if st.session_state.strategic_plan_output:
#                     with st.spinner(f"Generating {st.session_state.selected_difficulty.capitalize()} MCQs from Strategic Plan..."):
#                         crew, _ = get_crew("MCQ Generation", st.session_state.strategic_plan_output, difficulty=st.session_state.selected_difficulty)
#                         result = crew.kickoff()
#                         if result and hasattr(result, 'raw'):
#                             st.session_state.mcq_output = result.raw
#                         st.success("MCQ Generation Complete!")
#                 st.rerun()
#         except Exception as e:
#             st.error(f"Could not parse the JSON plan. Error: {e}")
#             st.code(st.session_state.strategic_plan_output)
#     else:
#         st.info("Run 'Strategic Plan' module to see the output here.")


# elif st.session_state.module_ran == "MCQ Generation":
#     st.header(f"Generated Multiple Choice Questions (Difficulty: {st.session_state.selected_difficulty.capitalize()})")
    
#     if st.session_state.mcq_output:
#         if not st.session_state.mcq_data_parsed:
#             match = re.search(r'\[.*\]', st.session_state.mcq_output, re.DOTALL)
#             if match:
#                 json_string = match.group(0)
#                 try:
#                     st.session_state.mcq_data_parsed = json.loads(json_string)
#                 except Exception as e:
#                     st.error(f"Could not parse the JSON MCQs. Error: {e}")
#                     st.code(json_string)
#                     st.session_state.mcq_output = None
#                     st.session_state.mcq_data_parsed = []
#             else:
#                 st.error("The AI did not return a recognizable JSON list for MCQs.")
#                 st.code(st.session_state.mcq_output)
#                 st.session_state.mcq_output = None
#                 st.session_state.mcq_data_parsed = []

#         mcq_data = st.session_state.mcq_data_parsed

#         if not mcq_data:
#             st.warning("No MCQs were generated for the given input and difficulty.")
#         else:
#             with st.form("mcq_quiz_form"):
#                 current_topic = None
#                 for i, mcq in enumerate(mcq_data):
#                     # Display topic header only once for consecutive questions on the same topic
#                     if mcq.get('topic') != current_topic:
#                         st.subheader(f"Topic: {mcq.get('topic', 'N/A')}")
#                         current_topic = mcq.get('topic')
                    
#                     st.markdown(f"##### Q{i+1} (Bloom's: {mcq.get('bloom_level', 'N/A')}):") # Display question number and Bloom's level
#                     st.markdown(f"**Question:** {mcq.get('question', 'N/A')}")
                    
#                     options = mcq.get('options', [])
#                     display_options = [f"{chr(65 + idx)}. {opt}" for idx, opt in enumerate(options)]

#                     user_choice_text = st.radio(
#                         "Select your answer:",
#                         display_options,
#                         key=f"q{i}_answer",
#                         index=display_options.index(st.session_state.user_answers.get(f"q{i}_answer_display")) if f"q{i}_answer_display" in st.session_state.user_answers and st.session_state.user_answers.get(f"q{i}_answer_display") in display_options else None,
#                         disabled=st.session_state.quiz_submitted
#                     )
                    
#                     if user_choice_text:
#                         st.session_state.user_answers[f"q{i}_answer_display"] = user_choice_text
#                         st.session_state.user_answers[f"q{i}_answer_content"] = user_choice_text[3:]
#                     else:
#                         st.session_state.user_answers[f"q{i}_answer_display"] = None
#                         st.session_state.user_answers[f"q{i}_answer_content"] = None
                    
#                     st.markdown("---")
                
#                 submit_button = st.form_submit_button("Submit Answers", disabled=st.session_state.quiz_submitted)

#             if submit_button:
#                 st.session_state.quiz_submitted = True
#                 st.rerun()

#             if st.session_state.quiz_submitted:
#                 st.subheader("Quiz Results")
#                 score = 0
#                 total_questions = len(mcq_data)

#                 for i, mcq in enumerate(mcq_data):
#                     question_key_display = f"q{i}_answer_display"
#                     question_key_content = f"q{i}_answer_content"

#                     user_answer_display = st.session_state.user_answers.get(question_key_display)
#                     user_answer_content = st.session_state.user_answers.get(question_key_content)
#                     correct_answer = mcq.get('correct_answer', 'N/A')
                    
#                     st.markdown(f"#### Q{i+1} (Bloom's: {mcq.get('bloom_level', 'N/A')}): {mcq.get('topic', 'N/A')}")
#                     st.markdown(f"**Question:** {mcq.get('question', 'N/A')}")
                    
#                     st.markdown(f"Your Answer: **{user_answer_display if user_answer_display else 'No answer chosen'}**")
#                     st.markdown(f"Correct Answer: **{correct_answer}**")

#                     is_correct = (user_answer_content == correct_answer) # Compare the raw content
#                     if is_correct:
#                         st.success("Correct!")
#                         score += 1
#                     else:
#                         st.error("Incorrect!")
                    
#                     st.markdown(f"**Explanation:** {mcq.get('rationale', 'No explanation provided.')}")

#                     original_rationale = "N/A"
#                     if st.session_state.get('strategic_plan_parsed'):
#                         for plan_item in st.session_state.strategic_plan_parsed:
#                             if plan_item.get('topic') == mcq.get('topic'): # Match by topic
#                                 original_rationale = plan_item.get('refined_rationale', 'N/A')
#                                 break

#                     if not is_correct:
#                         st.warning(f"**Concepts to Improve:** Based on the teaching rationale for this topic ('{original_rationale}'), you might want to review: **{mcq.get('topic', 'this topic')}.** Specifically focus on the `{mcq.get('bloom_level', 'N/A')}` level of understanding for this concept.")
#                     st.markdown("---")
                
#                 st.markdown(f"### Your Score: {score}/{total_questions}")
                
#                 if st.button("Retake Quiz"):
#                     st.session_state.user_answers = {}
#                     st.session_state.quiz_submitted = False
#                     st.rerun()

#             with st.expander("View Raw JSON MCQs"):
#                 st.json(mcq_data)
            
#             st.download_button(
#                 label="📥 Download MCQs as JSON",
#                 data=json.dumps(mcq_data, indent=2),
#                 file_name=f"generated_mcqs_{st.session_state.selected_difficulty}.json",
#                 mime="application/json"
#             )
#     else:
#         st.info("Run 'MCQ Generation' module to see the output here.")


# elif st.session_state.module_ran == "Knowledge Graph":
#     st.header("Learning Path Flowchart")
#     if st.session_state.text_output:
#         dot_code = st.session_state.text_output
#         match = re.search(r"digraph\s+\w*\s*\{.*\}", dot_code, re.DOTALL)
#         if match:
#             clean_dot_code = match.group(0)
#             try:
#                 st.graphviz_chart(clean_dot_code)
#             except Exception as e:
#                 st.error(f"Could not render the diagram directly. Error: {e}")
            
#             st.subheader("Final DOT Code")
#             st.code(clean_dot_code, language='dot')
#         else:
#             st.warning("The final output was not a valid flowchart. Displaying raw output:")
#             st.code(dot_code, language='text')

# else: 
#     if st.session_state.text_output:
#         st.header(f"Output for {st.session_state.module_ran}")
#         st.markdown(st.session_state.text_output, unsafe_allow_html=True)
#         st.download_button(
#             label=f"📥 Download {st.session_state.module_ran}",
#             data=st.session_state.text_output,
#             file_name=f"{st.session_state.module_ran.lower().replace(' ', '_')}_output.md"
#         )
#     else:
#         st.info("Click 'Run Selected Module' to generate content for the selected module.")

# Bloom's Taxonomy
# # main.py

# import streamlit as st
# import re
# import json5 as json
# from crew.crew_factory import get_crew
# import graphviz
# from litellm import exceptions as litellm_exceptions

# # Helper function to parse DOT graph and find connected nodes
# def parse_dot_graph(dot_code):
#     nodes, edges, node_labels = set(), [], {}
#     node_definition_pattern = re.compile(r'^\s*(\w+|"[^"]+")\s*\[label="([^"]+)"\];')
#     edge_definition_pattern = re.compile(r'^\s*(\w+|"[^"]+")\s*->\s*(\w+|"[^"]+")\s*(?:\[[^\]]*\])?;')
#     id_to_label_map = {}
#     for line in dot_code.split('\n'):
#         line = line.strip()
#         node_match = node_definition_pattern.match(line)
#         if node_match:
#             raw_id, label = node_match.groups()
#             nodes.add(label)
#             node_labels[label] = label
#             id_to_label_map[raw_id] = label
#     adj = {label: set() for label in nodes}
#     for line in dot_code.split('\n'):
#         line = line.strip()
#         edge_match = edge_definition_pattern.match(line)
#         if edge_match:
#             source_raw_id, target_raw_id = edge_match.groups()
#             source_label, target_label = id_to_label_map.get(source_raw_id), id_to_label_map.get(target_raw_id)
#             if source_label in nodes and target_label in nodes:
#                 edges.append((source_label, target_label))
#                 adj[source_label].add(target_label)
#     label_to_id = {label: label for label in nodes}
#     return nodes, edges, adj, node_labels, label_to_id

# def init_session_state():
#     defaults = {
#         "module_ran": None, "text_output": None, "strategic_plan_output": None,
#         "mcq_output": None, "selected_difficulty": "medium", "user_answers": {},
#         "quiz_submitted": False, "mcq_data_parsed": [], "strategic_plan_parsed": [],
#         "knowledge_graph_dot": None,
#         "bloom_q_counts": {"Remember": 1, "Understand": 1, "Apply": 1, "Analyze": 1, "Evaluate": 1, "Create": 1},
#         "parsed_graph_data": None
#     }
#     for key, value in defaults.items():
#         if key not in st.session_state:
#             st.session_state[key] = value

# # --- UI Rendering ---
# st.set_page_config(page_title="Spirit", layout="wide")
# st.title("Spirit")
# init_session_state()

# # --- Sidebar Controls ---
# with st.sidebar:
#     st.header("Controls")
#     module = st.sidebar.selectbox("Select a module", ["Summarization", "Notes", "Explanation", "Knowledge Graph", "Strategic Plan", "MCQ Generation"])
#     if module == "MCQ Generation":
#         st.session_state.selected_difficulty = st.selectbox("Select Difficulty", ["easy", "medium", "hard"], index=["easy", "medium", "hard"].index(st.session_state.selected_difficulty))
#         st.markdown("---")
#         st.subheader("Questions per Bloom's Level:")
#         bloom_levels = ["Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"]
#         for level in bloom_levels:
#             st.session_state.bloom_q_counts[level] = st.number_input(f"Number of '{level}' Questions", min_value=0, max_value=2, value=st.session_state.bloom_q_counts.get(level, 1), key=f"num_{level}_q")
#         st.markdown("---")
#     uploaded_md = st.file_uploader("Upload Markdown", type=["md", "txt"])
#     run_selected_module_button = st.button("Run Selected Module")

#     if run_selected_module_button:
#         if uploaded_md:
#             with st.spinner(f"Running {module}..."):
#                 st.session_state.module_ran = module
#                 markdown_text = uploaded_md.read().decode("utf-8")
#                 if module == "MCQ Generation":
#                     st.warning("Please use the 'Generate MCQs' button from the main panel after running 'Strategic Plan'.")
#                     st.session_state.module_ran = None
#                     st.stop()
#                 try:
#                     crew, crew_type_flag = get_crew(module, markdown_text, strategic_plan_data=st.session_state.strategic_plan_parsed)
#                     result = crew.kickoff()
#                     if result and hasattr(result, 'raw'):
#                         raw_output = result.raw
#                         st.session_state.text_output = raw_output
#                         if module == "Strategic Plan":
#                             match = re.search(r'\[.*\]', raw_output, re.DOTALL)
#                             if match:
#                                 json_string = match.group(0)
#                                 st.session_state.strategic_plan_output = json_string
#                                 st.session_state.strategic_plan_parsed = json.loads(json_string)
#                             else:
#                                 st.error("Strategic Plan did not return a valid JSON format.")
#                         elif module == "Knowledge Graph":
#                             match = re.search(r"digraph\s+.*\{[\s\S]*\}", raw_output, re.DOTALL)
#                             if match:
#                                 st.session_state.knowledge_graph_dot = match.group(0)
#                                 st.session_state.parsed_graph_data = parse_dot_graph(st.session_state.knowledge_graph_dot)
#                             else:
#                                 st.warning("Knowledge Graph did not return valid DOT code.")
#                     st.success("Content Generation Complete!")
#                 except litellm_exceptions.InternalServerError:
#                     st.error("The AI model is currently overloaded or unavailable. Please wait a moment and try again.")
#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")
#         else:
#             st.warning("Please upload a Markdown file first.")

#     mcq_generation_button = False
#     if module == "MCQ Generation":
#         if st.session_state.strategic_plan_output:
#             mcq_generation_button = st.button("Generate MCQs")
#         else:
#             st.info("Please generate a 'Strategic Plan' first.")

#     if mcq_generation_button:
#         if st.session_state.strategic_plan_parsed:
#             with st.spinner("Generating MCQs..."):
#                 st.session_state.module_ran = "MCQ Generation"
#                 st.session_state.mcq_data_parsed = []
#                 st.session_state.user_answers = {}
#                 st.session_state.quiz_submitted = False
                
#                 crew, crew_type_flag = get_crew("MCQ Generation", json.dumps(st.session_state.strategic_plan_parsed), difficulty=st.session_state.selected_difficulty, bloom_q_counts=st.session_state.bloom_q_counts)
#                 try:
#                     results = crew.kickoff()
#                     all_mcqs = []
#                     if results and hasattr(results, 'tasks_output') and results.tasks_output:
#                         for task_output in results.tasks_output:
#                             if task_output and task_output.raw:
#                                 json_match = re.search(r'(\{.*\}|\[.*\])', task_output.raw, re.DOTALL)
#                                 if json_match:
#                                     json_string = json_match.group(0)
#                                     try:
#                                         parsed_data = json.loads(json_string)
#                                         if isinstance(parsed_data, list):
#                                             all_mcqs.extend(parsed_data)
#                                         elif isinstance(parsed_data, dict) and 'mcqs' in parsed_data:
#                                             all_mcqs.extend(parsed_data.get('mcqs', []))
#                                     except Exception as e:
#                                         st.warning(f"Could not parse a batch of MCQs. Error: {e}")
#                                         st.code(json_string)
#                     st.session_state.mcq_data_parsed = all_mcqs
#                     st.session_state.mcq_output = json.dumps(all_mcqs, indent=2)
#                     st.success("MCQ Generation Complete!")
#                 except litellm_exceptions.InternalServerError:
#                     st.error("The AI model is overloaded. Please try again.")
#                     st.session_state.module_ran = "Strategic Plan"
#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")
#                     st.session_state.module_ran = "Strategic Plan"
#         else:
#             st.warning("Please run 'Strategic Plan' first.")

# # --- Main Page Content Display ---
# if not st.session_state.module_ran:
#     st.info("Upload a Markdown file and click 'Run Selected Module' to begin.")

# elif st.session_state.module_ran == "Strategic Plan":
#     st.header("Refined Strategic Plan")
#     if st.session_state.strategic_plan_parsed:
#         st.dataframe(st.session_state.strategic_plan_parsed)
#         with st.expander("View Raw JSON"):
#             st.json(st.session_state.strategic_plan_parsed)
#     else:
#         st.info("Run 'Strategic Plan' module to see the output here.")

# elif st.session_state.module_ran == "MCQ Generation":
#     st.header(f"Generated MCQs (Difficulty: {st.session_state.selected_difficulty.capitalize()})")
#     mcq_data = st.session_state.get('mcq_data_parsed', [])

#     if not mcq_data:
#         st.warning("No MCQs were parsed correctly. Please check logs or try again.")
#     else:
#         with st.form("mcq_quiz_form"):
#             current_topic = None
#             for i, mcq in enumerate(mcq_data):
#                 if mcq.get('topic') != current_topic:
#                     st.subheader(f"Topic: {mcq.get('topic', 'N/A')}")
#                     current_topic = mcq.get('topic')
                
#                 st.markdown(f"##### Q{i+1} (Bloom's: {mcq.get('bloom_level', 'N/A')}):")
#                 st.markdown(f"**Question:** {mcq.get('question', 'N/A')}")
                
#                 options = mcq.get('options', [])
#                 display_options = [f"{chr(65 + idx)}. {opt}" for idx, opt in enumerate(options)]
#                 user_choice_text = st.radio("Select your answer:", display_options, key=f"q_{i}", index=None, disabled=st.session_state.quiz_submitted)
                
#                 if user_choice_text:
#                     st.session_state.user_answers[i] = {"display": user_choice_text, "content": user_choice_text[3:]}
#                 st.markdown("---")
            
#             submit_button = st.form_submit_button("Submit Answers", disabled=st.session_state.quiz_submitted)

#         if submit_button:
#             st.session_state.quiz_submitted = True
#             st.rerun()

#         if st.session_state.quiz_submitted:
#             st.subheader("Quiz Results")
#             score = 0
#             for i, mcq in enumerate(mcq_data):
#                 user_answer = st.session_state.user_answers.get(i, {})
#                 user_answer_content = user_answer.get('content')
#                 correct_answer = mcq.get('correct_answer')
                
#                 st.markdown(f"#### Q{i+1} (Bloom's: {mcq.get('bloom_level', 'N/A')}): {mcq.get('topic', 'N/A')}")
#                 st.markdown(f"**Question:** {mcq.get('question', 'N/A')}")
#                 st.markdown(f"Your Answer: **{user_answer.get('display', 'No answer chosen')}**")
#                 st.markdown(f"Correct Answer: **{correct_answer}**")

#                 if user_answer_content == correct_answer:
#                     st.success("Correct!")
#                     score += 1
#                 else:
#                     st.error("Incorrect!")
                
#                 st.markdown(f"**Explanation:** {mcq.get('rationale', 'No explanation provided.')}")
#                 st.markdown("---")
            
#             st.markdown(f"### Your Score: {score}/{len(mcq_data)}")
            
#             if st.button("Retake Quiz"):
#                 st.session_state.user_answers = {}
#                 st.session_state.quiz_submitted = False
#                 st.rerun()

#         with st.expander("View Raw JSON MCQs"):
#             st.json(mcq_data)
#         st.download_button("📥 Download MCQs as JSON", st.session_state.mcq_output, f"generated_mcqs_{st.session_state.selected_difficulty}.json", "application/json")

# elif st.session_state.module_ran == "Knowledge Graph":
#     st.header("Learning Path Flowchart")
#     if st.session_state.knowledge_graph_dot:
#         st.graphviz_chart(st.session_state.knowledge_graph_dot)
#         st.subheader("Final DOT Code")
#         st.code(st.session_state.knowledge_graph_dot, language='dot')
#     else:
#         st.info("Run 'Knowledge Graph' module to see the flowchart here.")

# else: 
#     if st.session_state.text_output:
#         st.header(f"Output for {st.session_state.module_ran}")
#         st.markdown(st.session_state.text_output, unsafe_allow_html=True)
#         st.download_button(f"📥 Download {st.session_state.module_ran}", st.session_state.text_output, f"{st.session_state.module_ran.lower().replace(' ', '_')}_output.md")
#     else:
#         st.info("Click 'Run Selected Module' to generate content for the selected module.")

# # Bloom's Taxonomy
# # main.py
# import streamlit as st
# import re
# import json5 as json
# from crew.crew_factory import get_crew
# import graphviz
# from litellm import exceptions as litellm_exceptions
# import os

# # Helper function to parse DOT graph and find connected nodes
# def parse_dot_graph(dot_code):
#     nodes, edges, node_labels = set(), [], {}
#     node_definition_pattern = re.compile(r'^\s*(\w+|"[^"]+")\s*\[label="([^"]+)"\];')
#     edge_definition_pattern = re.compile(r'^\s*(\w+|"[^"]+")\s*->\s*(\w+|"[^"]+")\s*(?:\[[^\]]*\])?;')
#     id_to_label_map = {}
#     for line in dot_code.split('\n'):
#         line = line.strip()
#         node_match = node_definition_pattern.match(line)
#         if node_match:
#             raw_id, label = node_match.groups()
#             nodes.add(label)
#             node_labels[label] = label
#             id_to_label_map[raw_id] = label
#     adj = {label: set() for label in nodes}
#     for line in dot_code.split('\n'):
#         line = line.strip()
#         edge_match = edge_definition_pattern.match(line)
#         if edge_match:
#             source_raw_id, target_raw_id = edge_match.groups()
#             source_label, target_label = id_to_label_map.get(source_raw_id), id_to_label_map.get(target_raw_id)
#             if source_label in nodes and target_label in nodes:
#                 edges.append((source_label, target_label))
#                 adj[source_label].add(target_label)
#     label_to_id = {label: label for label in nodes}
#     return nodes, edges, adj, node_labels, label_to_id

# def init_session_state():
#     defaults = {
#         "module_ran": None, "text_output": None, "strategic_plan_output": None,
#         "selected_difficulty": "medium", "strategic_plan_parsed": [],
#         "knowledge_graph_dot": None,
#         "bloom_q_counts": {"Remember": 1, "Understand": 1, "Apply": 1, "Analyze": 1, "Evaluate": 1, "Create": 1},
#         "parsed_graph_data": None
#     }
#     for key, value in defaults.items():
#         if key not in st.session_state:
#             st.session_state[key] = value

# # --- UI Rendering ---
# st.set_page_config(page_title="Spirit", layout="wide")
# st.title("Spirit")
# init_session_state()

# # --- Sidebar Controls ---
# with st.sidebar:
#     st.header("Controls")
#     module = st.sidebar.selectbox("Select a module", ["Summarization", "Notes", "Explanation", "Knowledge Graph", "Strategic Plan", "MCQ Generation"])
#     if module == "MCQ Generation":
#         st.session_state.selected_difficulty = st.selectbox("Select Difficulty", ["easy", "medium", "hard"], index=["easy", "medium", "hard"].index(st.session_state.selected_difficulty))
#         st.markdown("---")
#         st.subheader("Questions per Bloom's Level:")
#         bloom_levels = ["Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"]
#         for level in bloom_levels:
#             st.session_state.bloom_q_counts[level] = st.number_input(f"Number of '{level}' Questions", min_value=0, max_value=2, value=st.session_state.bloom_q_counts.get(level, 1), key=f"num_{level}_q")
#         st.markdown("---")
#     uploaded_md = st.file_uploader("Upload Markdown", type=["md", "txt"])
#     run_selected_module_button = st.button("Run Selected Module")

#     if run_selected_module_button:
#         if uploaded_md:
#             with st.spinner(f"Running {module}..."):
#                 st.session_state.module_ran = module
#                 markdown_text = uploaded_md.read().decode("utf-8")
#                 if module == "MCQ Generation":
#                     st.warning("Please use the 'Generate & Save MCQs' button from the main panel after running 'Strategic Plan'.")
#                     st.session_state.module_ran = None
#                     st.stop()
#                 try:
#                     crew, crew_type_flag = get_crew(module, markdown_text, strategic_plan_data=st.session_state.strategic_plan_parsed)
#                     result = crew.kickoff()
#                     if result and hasattr(result, 'raw'):
#                         raw_output = result.raw
#                         st.session_state.text_output = raw_output
#                         if module == "Strategic Plan":
#                             match = re.search(r'\[.*\]', raw_output, re.DOTALL)
#                             if match:
#                                 json_string = match.group(0)
#                                 st.session_state.strategic_plan_output = json_string
#                                 st.session_state.strategic_plan_parsed = json.loads(json_string)
#                             else:
#                                 st.error("Strategic Plan did not return a valid JSON format.")
#                         elif module == "Knowledge Graph":
#                             match = re.search(r"digraph\s+.*\{[\s\S]*\}", raw_output, re.DOTALL)
#                             if match:
#                                 st.session_state.knowledge_graph_dot = match.group(0)
#                                 st.session_state.parsed_graph_data = parse_dot_graph(st.session_state.knowledge_graph_dot)
#                             else:
#                                 st.warning("Knowledge Graph did not return valid DOT code.")
#                     st.success("Content Generation Complete!")
#                 except litellm_exceptions.InternalServerError:
#                     st.error("The AI model is currently overloaded or unavailable. Please wait a moment and try again.")
#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")
#         else:
#             st.warning("Please upload a Markdown file first.")

#     mcq_generation_button = False
#     if module == "MCQ Generation":
#         if st.session_state.strategic_plan_output:
#             mcq_generation_button = st.button("Generate & Save MCQs")
#         else:
#             st.info("Please generate a 'Strategic Plan' first.")

#     if mcq_generation_button:
#         if st.session_state.strategic_plan_parsed:
#             with st.spinner("Generating and saving MCQs..."):
#                 st.session_state.module_ran = "MCQ Generation"
                
#                 crew, crew_type_flag = get_crew("MCQ Generation", json.dumps(st.session_state.strategic_plan_parsed), difficulty=st.session_state.selected_difficulty, bloom_q_counts=st.session_state.bloom_q_counts)
#                 try:
#                     results = crew.kickoff()
#                     all_mcqs = []
#                     if results and hasattr(results, 'tasks_output') and results.tasks_output:
#                         for task_output in results.tasks_output:
#                             if task_output and task_output.raw:
#                                 json_match = re.search(r'(\{.*\}|\[.*\])', task_output.raw, re.DOTALL)
#                                 if json_match:
#                                     json_string = json_match.group(0)
#                                     try:
#                                         parsed_data = json.loads(json_string)
#                                         if isinstance(parsed_data, dict) and parsed_data.get('status') == 'refined':
#                                             all_mcqs.extend(parsed_data.get('mcqs', []))
#                                     except Exception:
#                                         pass # Ignore parsing errors from non-final outputs
                    
#                     # New logic: Save the essential data to a JSON file
#                     if all_mcqs:
#                         data_to_save = []
#                         for mcq in all_mcqs:
#                             data_to_save.append({
#                                 "question": mcq.get("question", "N/A"),
#                                 "answer": mcq.get("correct_answer", "N/A"),
#                                 "rationale": mcq.get("rationale", "N/A")
#                             })
                        
#                         output_filename = "mcqs.json"
#                         with open(output_filename, 'w', encoding='utf-8') as f:
#                             json.dump(data_to_save, f, indent=4, ensure_ascii=False)
                        
#                         st.success(f"✅ MCQs successfully generated and saved to `{output_filename}`!")
#                         st.session_state.text_output = f"MCQs were saved to `{output_filename}`."
#                     else:
#                         st.warning("No MCQs were generated or parsed correctly.")

#                 except litellm_exceptions.InternalServerError:
#                     st.error("The AI model is overloaded. Please try again.")
#                     st.session_state.module_ran = "Strategic Plan"
#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")
#                     st.session_state.module_ran = "Strategic Plan"
#         else:
#             st.warning("Please run 'Strategic Plan' first.")

# # --- Main Page Content Display ---
# if not st.session_state.module_ran:
#     st.info("Upload a Markdown file and click 'Run Selected Module' to begin.")

# elif st.session_state.module_ran == "Strategic Plan":
#     st.header("Refined Strategic Plan")
#     if st.session_state.strategic_plan_parsed:
#         st.dataframe(st.session_state.strategic_plan_parsed)
#         with st.expander("View Raw JSON"):
#             st.json(st.session_state.strategic_plan_parsed)
#     else:
#         st.info("Run 'Strategic Plan' module to see the output here.")

# elif st.session_state.module_ran == "Knowledge Graph":
#     st.header("Learning Path Flowchart")
#     if st.session_state.knowledge_graph_dot:
#         st.graphviz_chart(st.session_state.knowledge_graph_dot)
#         st.subheader("Final DOT Code")
#         st.code(st.session_state.knowledge_graph_dot, language='dot')
#     else:
#         st.info("Run 'Knowledge Graph' module to see the flowchart here.")

# # All other modules will now fall through to this final 'else' block
# else: 
#     if st.session_state.text_output:
#         st.header(f"Output for {st.session_state.module_ran}")
#         st.markdown(st.session_state.text_output, unsafe_allow_html=True)
#         # For non-MCQ modules, offer a download button
#         if st.session_state.module_ran != "MCQ Generation":
#             st.download_button(f"📥 Download {st.session_state.module_ran}", st.session_state.text_output, f"{st.session_state.module_ran.lower().replace(' ', '_')}_output.md")
#     else:
#         st.info("Click 'Run Selected Module' to generate content for the selected module.")

# Distactions
# # main.py
# import streamlit as st
# import re
# import json5 as json
# from crew.crew_factory import get_crew
# import graphviz
# from litellm import exceptions as litellm_exceptions
# import os
# import random
# import time

# def parse_dot_graph(dot_code):
#     nodes, edges, node_labels = set(), [], {}
#     node_definition_pattern = re.compile(r'^\s*(\w+|"[^"]+")\s*\[label="([^"]+)"\];')
#     edge_definition_pattern = re.compile(r'^\s*(\w+|"[^"]+")\s*->\s*(\w+|"[^"]+")\s*(?:\[[^\]]*\])?;')
#     id_to_label_map = {}
#     for line in dot_code.split('\n'):
#         line = line.strip()
#         node_match = node_definition_pattern.match(line)
#         if node_match:
#             raw_id, label = node_match.groups()
#             nodes.add(label)
#             node_labels[label] = label
#             id_to_label_map[raw_id] = label
#     adj = {label: set() for label in nodes}
#     for line in dot_code.split('\n'):
#         line = line.strip()
#         edge_match = edge_definition_pattern.match(line)
#         if edge_match:
#             source_raw_id, target_raw_id = edge_match.groups()
#             source_label, target_label = id_to_label_map.get(source_raw_id), id_to_label_map.get(target_raw_id)
#             if source_label in nodes and target_label in nodes:
#                 edges.append((source_label, target_label))
#                 adj[source_label].add(target_label)
#     label_to_id = {label: label for label in nodes}
#     return nodes, edges, adj, node_labels, label_to_id

# def init_session_state():
#     defaults = {
#         "module_ran": None, "text_output": None, "strategic_plan_output": None,
#         "selected_difficulty": "medium", "strategic_plan_parsed": [],
#         "knowledge_graph_dot": None,
#         "bloom_q_counts": {"Remember": 1, "Understand": 1, "Apply": 1, "Analyze": 1, "Evaluate": 1, "Create": 1},
#         "final_quiz_data": [],
#         "final_quiz_json_output": None,
#         "user_answers": {},
#         "quiz_submitted": False
#     }
#     for key, value in defaults.items():
#         if key not in st.session_state:
#             st.session_state[key] = value

# # --- UI Rendering ---
# st.set_page_config(page_title="Spirit", layout="wide")
# st.title("Spirit")
# init_session_state()

# # --- Sidebar Controls ---
# with st.sidebar:
#     st.header("Controls")
#     module_options = ["Summarization", "Notes", "Explanation", "Knowledge Graph", "Strategic Plan", "MCQ Generation", "Distractor Generation"]
#     module = st.sidebar.selectbox("Select a module", module_options)

#     uploaded_md = None
#     if module not in ["Distractor Generation"]:
#         uploaded_md = st.file_uploader("Upload Source Document", type=["md", "txt"])

#     if module == "MCQ Generation":
#         st.markdown("---")
#         st.session_state.selected_difficulty = st.selectbox("Select Difficulty", ["easy", "medium", "hard"], index=["easy", "medium", "hard"].index(st.session_state.selected_difficulty))
    
#     st.markdown("---")

#     if module in ["Summarization", "Notes", "Explanation", "Knowledge Graph", "Strategic Plan"]:
#         if st.button(f"Run {module}"):
#             if uploaded_md:
#                 with st.spinner(f"Running {module}..."):
#                     st.session_state.module_ran = module
#                     markdown_text = uploaded_md.read().decode("utf-8")
#                     try:
#                         crew, _ = get_crew(module, markdown_text, strategic_plan_data=st.session_state.strategic_plan_parsed)
#                         result = crew.kickoff()
#                         st.session_state.text_output = str(result.raw) if hasattr(result, 'raw') else str(result)
#                         if module == "Strategic Plan":
#                             match = re.search(r'\[.*\]', st.session_state.text_output, re.DOTALL)
#                             if match:
#                                 json_string = match.group(0)
#                                 st.session_state.strategic_plan_output = json_string
#                                 st.session_state.strategic_plan_parsed = json.loads(json_string)
#                             else: st.error("Strategic Plan did not return valid JSON.")
#                         elif module == "Knowledge Graph":
#                             match = re.search(r"digraph\s+.*\{[\s\S]*\}", st.session_state.text_output, re.DOTALL)
#                             if match: st.session_state.knowledge_graph_dot = match.group(0)
#                             else: st.warning("Knowledge Graph did not return valid DOT code.")
#                         st.success("Generation Complete!")
#                     except Exception as e:
#                         st.error(f"An unexpected error occurred: {e}")
#             else:
#                 st.warning("Please upload a source document first.")

#     elif module == "MCQ Generation":
#         if st.session_state.strategic_plan_parsed:
#             if st.button("Generate & Save MCQs (Core)"):
#                  with st.spinner("Generating and saving core MCQs..."):
#                     st.session_state.module_ran = "MCQ Generation"
#                     try:
#                         crew, _ = get_crew("MCQ Generation", json.dumps(st.session_state.strategic_plan_parsed), difficulty=st.session_state.selected_difficulty, bloom_q_counts=st.session_state.bloom_q_counts)
#                         results = crew.kickoff()
#                         all_mcqs = []
#                         if hasattr(results, 'tasks_output') and results.tasks_output:
#                             for task_output in results.tasks_output:
#                                 if hasattr(task_output, 'raw') and 'refined' in str(task_output.raw):
#                                     json_match = re.search(r'(\{.*\}|\[.*\])', task_output.raw, re.DOTALL)
#                                     if json_match:
#                                         try:
#                                             parsed_data = json.loads(json_match.group(0))
#                                             if isinstance(parsed_data, dict) and parsed_data.get('status') == 'refined':
#                                                 all_mcqs.extend(parsed_data.get('mcqs', []))
#                                         except Exception: pass
#                         if all_mcqs:
#                             data_to_save = [{"question": mcq.get("question"), "answer": mcq.get("correct_answer"), "rationale": mcq.get("rationale")} for mcq in all_mcqs]
#                             output_filename = "mcqs.json"
#                             with open(output_filename, 'w', encoding='utf-8') as f:
#                                 json.dump(data_to_save, f, indent=4, ensure_ascii=False)
#                             st.success(f"✅ Core MCQs saved to `{output_filename}`!")
#                             st.session_state.text_output = f"Core questions and answers were saved to `{output_filename}`. You can now run 'Distractor Generation'."
#                         else:
#                             st.warning("No MCQs were generated.")
#                     except Exception as e:
#                         st.error(f"An unexpected error occurred: {e}")
#         else:
#             st.info("Please run 'Strategic Plan' first.")

#     elif module == "Distractor Generation":
#         if os.path.exists("mcqs.json"):
#              if st.button("Generate Final Quiz"):
#                 st.session_state.module_ran = "Distractor Generation"
#                 st.session_state.user_answers = {}
#                 st.session_state.quiz_submitted = False
#                 try:
#                     with open("mcqs.json", 'r', encoding='utf-8') as f:
#                         questions_data = json.load(f)
                    
#                     final_quiz_data = []
#                     progress_bar = st.progress(0, text="Initializing...")

#                     for i, q_obj in enumerate(questions_data):
#                         progress_text = f"Generating options for question {i+1}/{len(questions_data)}..."
#                         with st.spinner(progress_text):
#                             crew, _ = get_crew("Distractor Generation", json.dumps(q_obj))
#                             result = crew.kickoff()
                            
#                             distractors_with_rationales = []
#                             if result and hasattr(result, 'raw'):
#                                 json_match = re.search(r'(\[.*\])', result.raw, re.DOTALL)
#                                 if json_match:
#                                     try:
#                                         parsed_options = json.loads(json_match.group(0))
#                                         if isinstance(parsed_options, list):
#                                             distractors_with_rationales = parsed_options
#                                     except Exception: pass
                            
#                             options = [d.get('option', f'Invalid Option {i+1}') for d in distractors_with_rationales] + [q_obj['answer']]
#                             random.shuffle(options)
                            
#                             distractor_rationales_map = {d.get('option'): d.get('misleading_rationale') for d in distractors_with_rationales}

#                             final_quiz_data.append({
#                                 "question": q_obj['question'],
#                                 "options": options,
#                                 "correct_answer": q_obj['answer'],
#                                 "correct_rationale": q_obj['rationale'],
#                                 "distractor_rationales": distractor_rationales_map
#                             })
                        
#                         progress_bar.progress((i + 1) / len(questions_data))
#                         time.sleep(5)

#                     st.session_state.final_quiz_data = final_quiz_data
#                     st.session_state.final_quiz_json_output = json.dumps(final_quiz_data, indent=4)
#                     st.success("✅ Final quiz generated! Attempt it now.")
#                     progress_bar.empty()
#                     st.rerun()

#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")
#         else:
#             st.info("Please run 'MCQ Generation' first to create 'mcqs.json'.")


# # --- Main Page Content Display ---
# if not st.session_state.module_ran:
#     st.info("Upload a document and select a module from the sidebar to begin.")

# elif st.session_state.module_ran == "Distractor Generation":
#     st.header("Final Quiz")
#     quiz_data = st.session_state.get('final_quiz_data', [])

#     if not quiz_data:
#         st.warning("No quiz data found. Please run 'Distractor Generation' first.")
#     else:
#         with st.form("final_quiz_form"):
#             for i, mcq in enumerate(quiz_data):
#                 st.markdown(f"##### Q{i+1}: {mcq.get('question', 'N/A')}")
#                 options = mcq.get('options', [])
#                 user_choice = st.radio("Select your answer:", options, key=f"q_{i}", index=None, disabled=st.session_state.quiz_submitted)
#                 if user_choice:
#                     st.session_state.user_answers[i] = user_choice
#                 st.markdown("---")
#             submit_button = st.form_submit_button("Submit Answers", disabled=st.session_state.quiz_submitted)

#         if submit_button:
#             st.session_state.quiz_submitted = True
#             st.rerun()

#         if st.session_state.quiz_submitted:
#             st.subheader("Quiz Results")
#             score = 0
#             for i, mcq in enumerate(quiz_data):
#                 user_answer = st.session_state.user_answers.get(i)
#                 correct_answer = mcq.get('correct_answer')
                
#                 st.markdown(f"**Q{i+1}: {mcq.get('question')}**")
#                 st.write(f"Your Answer: **{user_answer if user_answer else 'No answer chosen'}**")
#                 st.write(f"Correct Answer: **{correct_answer}**")

#                 if user_answer == correct_answer:
#                     st.success("Correct!")
#                     score += 1
#                     with st.expander("View Rationale"):
#                         st.markdown(mcq.get('correct_rationale', 'No rationale provided.'))
#                 else:
#                     st.error("Incorrect!")
#                     with st.expander("View Explanation"):
#                         explanation = mcq.get('distractor_rationales', {}).get(user_answer, "No specific explanation for this option is available.")
#                         st.markdown(explanation)
#                 st.markdown("---")
            
#             st.markdown(f"### Your Final Score: {score}/{len(quiz_data)}")
            
#             if st.button("Retake Quiz"):
#                 st.session_state.user_answers = {}
#                 st.session_state.quiz_submitted = False
#                 st.rerun()
        
#         st.download_button("📥 Download Quiz as JSON", st.session_state.final_quiz_json_output, "final_quiz.json", "application/json")


# elif st.session_state.module_ran == "Strategic Plan":
#     st.header("Refined Strategic Plan")
#     if st.session_state.strategic_plan_parsed:
#         st.dataframe(st.session_state.strategic_plan_parsed)
#         with st.expander("View Raw JSON"):
#             st.json(st.session_state.strategic_plan_parsed)
# elif st.session_state.module_ran == "Knowledge Graph":
#     st.header("Learning Path Flowchart")
#     if st.session_state.knowledge_graph_dot:
#         st.graphviz_chart(st.session_state.knowledge_graph_dot)
#         st.subheader("Final DOT Code")
#         st.code(st.session_state.knowledge_graph_dot, language='dot')
# else:
#     if st.session_state.text_output:
#         st.header(f"Output for {st.session_state.module_ran}")
#         st.markdown(st.session_state.text_output, unsafe_allow_html=True)
#         if st.session_state.module_ran not in ["MCQ Generation", "Distractor Generation"]:
#             st.download_button(f"📥 Download {st.session_state.module_ran}", st.session_state.text_output, f"{st.session_state.module_ran.lower().replace(' ', '_')}_output.md")

# token counter
# main.py
# import streamlit as st
# import re
# import json5 as json
# from crew.crew_factory import get_crew
# import graphviz
# import litellm
# from litellm import exceptions as litellm_exceptions
# import os
# import random
# import time
# from utils.token_tracker import token_tracker, track_token_usage_callback

# # Register the callback with litellm at the start of the app
# litellm.success_callback = [track_token_usage_callback]

# def parse_dot_graph(dot_code):
#     nodes, edges, node_labels = set(), [], {}
#     node_definition_pattern = re.compile(r'^\s*(\w+|"[^"]+")\s*\[label="([^"]+)"\];')
#     edge_definition_pattern = re.compile(r'^\s*(\w+|"[^"]+")\s*->\s*(\w+|"[^"]+")\s*(?:\[[^\]]*\])?;')
#     id_to_label_map = {}
#     for line in dot_code.split('\n'):
#         line = line.strip()
#         node_match = node_definition_pattern.match(line)
#         if node_match:
#             raw_id, label = node_match.groups()
#             nodes.add(label)
#             node_labels[label] = label
#             id_to_label_map[raw_id] = label
#     adj = {label: set() for label in nodes}
#     for line in dot_code.split('\n'):
#         line = line.strip()
#         edge_match = edge_definition_pattern.match(line)
#         if edge_match:
#             source_raw_id, target_raw_id = edge_match.groups()
#             source_label, target_label = id_to_label_map.get(source_raw_id), id_to_label_map.get(target_raw_id)
#             if source_label in nodes and target_label in nodes:
#                 edges.append((source_label, target_label))
#                 adj[source_label].add(target_label)
#     label_to_id = {label: label for label in nodes}
#     return nodes, edges, adj, node_labels, label_to_id

# def init_session_state():
#     defaults = {
#         "module_ran": None, "text_output": None, "strategic_plan_output": None,
#         "selected_difficulty": "medium", "strategic_plan_parsed": [],
#         "knowledge_graph_dot": None,
#         "bloom_q_counts": {"Remember": 1, "Understand": 1, "Apply": 1, "Analyze": 1, "Evaluate": 1, "Create": 1},
#         "final_quiz_data": [],
#         "final_quiz_json_output": None,
#         "user_answers": {},
#         "quiz_submitted": False
#     }
#     for key, value in defaults.items():
#         if key not in st.session_state:
#             st.session_state[key] = value

# # --- UI Rendering ---
# st.set_page_config(page_title="Spirit", layout="wide")
# st.title("Spirit")
# init_session_state()

# # --- Sidebar Controls ---
# with st.sidebar:
#     st.header("Controls")
#     module_options = ["Summarization", "Notes", "Explanation", "Knowledge Graph", "Strategic Plan", "MCQ Generation", "Distractor Generation"]
#     module = st.sidebar.selectbox("Select a module", module_options)

#     uploaded_md = None
#     if module not in ["Distractor Generation"]:
#         uploaded_md = st.file_uploader("Upload Source Document", type=["md", "txt"])

#     if module == "MCQ Generation":
#         st.markdown("---")
#         st.session_state.selected_difficulty = st.selectbox("Select Difficulty", ["easy", "medium", "hard"])
        
#         st.subheader("Questions per Bloom's Level:")
#         bloom_levels = ["Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"]
#         for level in bloom_levels:
#             st.session_state.bloom_q_counts[level] = st.number_input(
#                 f"'{level}' Questions", 
#                 min_value=0, 
#                 max_value=2, 
#                 value=st.session_state.bloom_q_counts.get(level, 1), 
#                 key=f"num_{level}_q"
#             )
    
#     st.markdown("---")

#     # --- Action Buttons & Logic ---
#     if module in ["Summarization", "Notes", "Explanation", "Knowledge Graph", "Strategic Plan"]:
#         if st.button(f"Run {module}"):
#             if uploaded_md:
#                 with st.spinner(f"Running {module}..."):
#                     token_tracker.reset()
#                     st.session_state.module_ran = module
#                     markdown_text = uploaded_md.read().decode("utf-8")
#                     try:
#                         crew, _ = get_crew(module, markdown_text, strategic_plan_data=st.session_state.strategic_plan_parsed)
#                         result = crew.kickoff()
#                         st.session_state.text_output = str(result.raw) if hasattr(result, 'raw') else str(result)
#                         if module == "Strategic Plan":
#                             match = re.search(r'\[.*\]', st.session_state.text_output, re.DOTALL)
#                             if match:
#                                 json_string = match.group(0)
#                                 st.session_state.strategic_plan_output = json_string
#                                 st.session_state.strategic_plan_parsed = json.loads(json_string)
#                             else: st.error("Strategic Plan did not return valid JSON.")
#                         elif module == "Knowledge Graph":
#                             match = re.search(r"digraph\s+.*\{[\s\S]*\}", st.session_state.text_output, re.DOTALL)
#                             if match: st.session_state.knowledge_graph_dot = match.group(0)
#                             else: st.warning("Knowledge Graph did not return valid DOT code.")
#                         st.success("Generation Complete!")
#                     except Exception as e:
#                         st.error(f"An unexpected error occurred: {e}")
#                     token_tracker.display()
#             else:
#                 st.warning("Please upload a source document first.")

#     elif module == "MCQ Generation":
#         if st.session_state.strategic_plan_parsed:
#             if st.button("Generate & Save MCQs (Core)"):
#                  with st.spinner("Generating and saving core MCQs..."):
#                     token_tracker.reset()
#                     st.session_state.module_ran = "MCQ Generation"
#                     try:
#                         crew, _ = get_crew("MCQ Generation", json.dumps(st.session_state.strategic_plan_parsed), 
#                                            difficulty=st.session_state.selected_difficulty, 
#                                            bloom_q_counts=st.session_state.bloom_q_counts)
#                         results = crew.kickoff()
#                         all_mcqs = []
#                         if hasattr(results, 'tasks_output') and results.tasks_output:
#                             for task_output in results.tasks_output:
#                                 if hasattr(task_output, 'raw') and 'refined' in str(task_output.raw):
#                                     json_match = re.search(r'(\{.*\}|\[.*\])', task_output.raw, re.DOTALL)
#                                     if json_match:
#                                         try:
#                                             parsed_data = json.loads(json_match.group(0))
#                                             if isinstance(parsed_data, dict) and parsed_data.get('status') == 'refined':
#                                                 all_mcqs.extend(parsed_data.get('mcqs', []))
#                                         except Exception: pass
#                         if all_mcqs:
#                             data_to_save = []
#                             for mcq in all_mcqs:
#                                 data_to_save.append({
#                                     "domain": mcq.get("domain", "General"),
#                                     "bloom_level": mcq.get("bloom_level", "N/A"),
#                                     "question": mcq.get("question"), 
#                                     "answer": mcq.get("correct_answer"), 
#                                     "rationale": mcq.get("rationale")
#                                 })

#                             output_filename = "mcqs.json"
#                             with open(output_filename, 'w', encoding='utf-8') as f:
#                                 json.dump(data_to_save, f, indent=4, ensure_ascii=False)
#                             st.success(f"✅ Core MCQs saved to `{output_filename}`!")
#                             st.session_state.text_output = f"Core questions and answers were saved to `{output_filename}`. You can now run 'Distractor Generation'."
#                         else:
#                             st.warning("No MCQs were generated.")
#                     except Exception as e:
#                         st.error(f"An unexpected error occurred: {e}")
#                     token_tracker.display()
#         else:
#             st.info("Please run 'Strategic Plan' first.")

#     elif module == "Distractor Generation":
#         if os.path.exists("mcqs.json"):
#              if st.button("Generate Final Quiz"):
#                 token_tracker.reset()
#                 st.session_state.module_ran = "Distractor Generation"
#                 st.session_state.user_answers = {}
#                 st.session_state.quiz_submitted = False
#                 try:
#                     with open("mcqs.json", 'r', encoding='utf-8') as f:
#                         questions_data = json.load(f)
                    
#                     final_quiz_data = []
#                     progress_bar = st.progress(0, text="Initializing...")

#                     for i, q_obj in enumerate(questions_data):
#                         with st.spinner(f"Generating options for question {i+1}/{len(questions_data)}..."):
#                             crew, _ = get_crew("Distractor Generation", json.dumps(q_obj))
#                             result = crew.kickoff()
                            
#                             distractors_with_rationales = []
#                             if result and hasattr(result, 'raw'):
#                                 json_match = re.search(r'(\[.*\])', result.raw, re.DOTALL)
#                                 if json_match:
#                                     try:
#                                         parsed_options = json.loads(json_match.group(0))
#                                         if isinstance(parsed_options, list):
#                                             distractors_with_rationales = parsed_options
#                                     except Exception: pass
                            
#                             options = [d.get('option', f'Invalid Option {i+1}') for d in distractors_with_rationales] + [q_obj['answer']]
#                             random.shuffle(options)
                            
#                             distractor_rationales_map = {d.get('option'): d.get('misleading_rationale') for d in distractors_with_rationales}

#                             final_quiz_data.append({
#                                 "question": q_obj['question'],
#                                 "options": options,
#                                 "correct_answer": q_obj['answer'],
#                                 "correct_rationale": q_obj['rationale'],
#                                 "distractor_rationales": distractor_rationales_map,
#                                 "domain": q_obj.get("domain", "General"),
#                                 "bloom_level": q_obj.get("bloom_level", "N/A")
#                             })
                        
#                         progress_bar.progress((i + 1) / len(questions_data))
#                         time.sleep(1)

#                     st.session_state.final_quiz_data = final_quiz_data
#                     st.session_state.final_quiz_json_output = json.dumps(final_quiz_data, indent=4)
#                     st.success("✅ Final quiz generated!")
#                     progress_bar.empty()
#                     token_tracker.display()
#                     st.rerun()

#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")
#                     token_tracker.display()
#         else:
#             st.info("Please run 'MCQ Generation' first to create 'mcqs.json'.")


# # --- Main Page Content Display ---
# if not st.session_state.module_ran:
#     st.info("Upload a document and select a module from the sidebar to begin.")

# elif st.session_state.module_ran == "Distractor Generation":
#     st.header("Final Quiz")
#     quiz_data = st.session_state.get('final_quiz_data', [])

#     if not quiz_data:
#         st.warning("No quiz data found. Please run 'Distractor Generation' first.")
#     else:
#         with st.form("final_quiz_form"):
#             for i, mcq in enumerate(quiz_data):
#                 st.markdown(f"##### Q{i+1} ({mcq.get('bloom_level', '')}): {mcq.get('question', 'N/A')}")
#                 options = mcq.get('options', [])
#                 user_choice = st.radio("Select your answer:", options, key=f"q_{i}", index=None, disabled=st.session_state.quiz_submitted)
#                 if user_choice:
#                     st.session_state.user_answers[i] = user_choice
#                 st.markdown("---")
#             submit_button = st.form_submit_button("Submit Answers", disabled=st.session_state.quiz_submitted)

#         if submit_button:
#             st.session_state.quiz_submitted = True
#             st.rerun()

#         if st.session_state.quiz_submitted:
#             st.subheader("Quiz Results")
#             score = 0
#             for i, mcq in enumerate(quiz_data):
#                 user_answer = st.session_state.user_answers.get(i)
#                 correct_answer = mcq.get('correct_answer')
                
#                 st.markdown(f"**Q{i+1} ({mcq.get('bloom_level', '')}): {mcq.get('question')}**")
#                 st.write(f"Your Answer: **{user_answer if user_answer else 'No answer chosen'}**")
#                 st.write(f"Correct Answer: **{correct_answer}**")

#                 if user_answer == correct_answer:
#                     st.success("Correct!")
#                     score += 1
#                     with st.expander("View Rationale"):
#                         st.markdown(mcq.get('correct_rationale', 'No rationale provided.'))
#                 else:
#                     st.error("Incorrect!")
#                     with st.expander("View Explanation"):
#                         explanation = mcq.get('distractor_rationales', {}).get(user_answer, "No specific explanation for this option is available.")
#                         st.markdown(explanation)
#                 st.markdown("---")
            
#             st.markdown(f"### Your Final Score: {score}/{len(quiz_data)}")
            
#             if st.button("Retake Quiz"):
#                 st.session_state.user_answers = {}
#                 st.session_state.quiz_submitted = False
#                 st.rerun()
        
#         st.download_button("📥 Download Quiz as JSON", st.session_state.final_quiz_json_output, "final_quiz.json", "application/json")


# elif st.session_state.module_ran == "Strategic Plan":
#     st.header("Refined Strategic Plan")
#     if st.session_state.strategic_plan_parsed:
#         st.dataframe(st.session_state.strategic_plan_parsed)
#         with st.expander("View Raw JSON"):
#             st.json(st.session_state.strategic_plan_parsed)
# elif st.session_state.module_ran == "Knowledge Graph":
#     st.header("Learning Path Flowchart")
#     if st.session_state.knowledge_graph_dot:
#         st.graphviz_chart(st.session_state.knowledge_graph_dot)
#         st.subheader("Final DOT Code")
#         st.code(st.session_state.knowledge_graph_dot, language='dot')
# else:
#     if st.session_state.text_output:
#         st.header(f"Output for {st.session_state.module_ran}")
#         st.markdown(st.session_state.text_output, unsafe_allow_html=True)
#         if st.session_state.module_ran not in ["MCQ Generation", "Distractor Generation"]:
#             st.download_button(f"📥 Download {st.session_state.module_ran}", st.session_state.text_output, f"{st.session_state.module_ran.lower().replace(' ', '_')}_output.md")

# Numeric and Theoretical Classification
# # main.py
# import streamlit as st
# import re
# import json5 as json
# from crew.crew_factory import get_crew
# import graphviz
# import litellm
# from litellm import exceptions as litellm_exceptions
# import os
# import random
# import time
# from utils.token_tracker import token_tracker, track_token_usage_callback

# # Register the callback with litellm at the start of the app
# litellm.success_callback = [track_token_usage_callback]

# def parse_dot_graph(dot_code):
#     nodes, edges, node_labels = set(), [], {}
#     node_definition_pattern = re.compile(r'^\s*(\w+|"[^"]+")\s*\[label="([^"]+)"\];')
#     edge_definition_pattern = re.compile(r'^\s*(\w+|"[^"]+")\s*->\s*(\w+|"[^"]+")\s*(?:\[[^\]]*\])?;')
#     id_to_label_map = {}
#     for line in dot_code.split('\n'):
#         line = line.strip()
#         node_match = node_definition_pattern.match(line)
#         if node_match:
#             raw_id, label = node_match.groups()
#             nodes.add(label)
#             node_labels[label] = label
#             id_to_label_map[raw_id] = label
#     adj = {label: set() for label in nodes}
#     for line in dot_code.split('\n'):
#         line = line.strip()
#         edge_match = edge_definition_pattern.match(line)
#         if edge_match:
#             source_raw_id, target_raw_id = edge_match.groups()
#             source_label, target_label = id_to_label_map.get(source_raw_id), id_to_label_map.get(target_raw_id)
#             if source_label in nodes and target_label in nodes:
#                 edges.append((source_label, target_label))
#                 adj[source_label].add(target_label)
#     label_to_id = {label: label for label in nodes}
#     return nodes, edges, adj, node_labels, label_to_id

# def init_session_state():
#     defaults = {
#         "module_ran": None, "text_output": None, "strategic_plan_output": None,
#         "selected_difficulty": "medium", "strategic_plan_parsed": [],
#         "knowledge_graph_dot": None,
#         "bloom_q_counts": {"Remember": 1, "Understand": 1, "Apply": 1, "Analyze": 1, "Evaluate": 1, "Create": 1},
#         "final_quiz_data": [],
#         "final_quiz_json_output": None,
#         "user_answers": {},
#         "quiz_submitted": False
#     }
#     for key, value in defaults.items():
#         if key not in st.session_state:
#             st.session_state[key] = value

# # --- UI Rendering ---
# st.set_page_config(page_title="Spirit", layout="wide")
# st.title("Spirit")
# init_session_state()

# # --- Sidebar Controls ---
# with st.sidebar:
#     st.header("Controls")
#     module_options = ["Summarization", "Notes", "Explanation", "Knowledge Graph", "Strategic Plan", "MCQ Generation", "Filter Questions", "Distractor Generation"]
#     module = st.sidebar.selectbox("Select a module", module_options)

#     uploaded_md = None
#     if module not in ["Filter Questions", "Distractor Generation"]:
#         uploaded_md = st.file_uploader("Upload Source Document", type=["md", "txt"])

#     if module == "MCQ Generation":
#         st.markdown("---")
#         st.session_state.selected_difficulty = st.selectbox("Select Difficulty", ["easy", "medium", "hard"])
        
#         st.subheader("Questions per Bloom's Level:")
#         bloom_levels = ["Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"]
#         for level in bloom_levels:
#             st.session_state.bloom_q_counts[level] = st.number_input(
#                 f"'{level}' Questions", 
#                 min_value=0, 
#                 max_value=2, 
#                 value=st.session_state.bloom_q_counts.get(level, 1), 
#                 key=f"num_{level}_q"
#             )
    
#     st.markdown("---")

#     # --- Action Buttons & Logic ---
#     if module in ["Summarization", "Notes", "Explanation", "Knowledge Graph", "Strategic Plan"]:
#         if st.button(f"Run {module}"):
#             if uploaded_md:
#                 with st.spinner(f"Running {module}..."):
#                     token_tracker.reset()
#                     st.session_state.module_ran = module
#                     markdown_text = uploaded_md.read().decode("utf-8")
#                     try:
#                         crew, _ = get_crew(module, markdown_text, strategic_plan_data=st.session_state.strategic_plan_parsed)
#                         result = crew.kickoff()
#                         st.session_state.text_output = str(result.raw) if hasattr(result, 'raw') else str(result)
#                         if module == "Strategic Plan":
#                             match = re.search(r'\[.*\]', st.session_state.text_output, re.DOTALL)
#                             if match:
#                                 json_string = match.group(0)
#                                 st.session_state.strategic_plan_output = json_string
#                                 st.session_state.strategic_plan_parsed = json.loads(json_string)
#                             else: st.error("Strategic Plan did not return valid JSON.")
#                         elif module == "Knowledge Graph":
#                             match = re.search(r"digraph\s+.*\{[\s\S]*\}", st.session_state.text_output, re.DOTALL)
#                             if match: st.session_state.knowledge_graph_dot = match.group(0)
#                             else: st.warning("Knowledge Graph did not return valid DOT code.")
#                         st.success("Generation Complete!")
#                     except Exception as e:
#                         st.error(f"An unexpected error occurred: {e}")
#                     token_tracker.display()
#             else:
#                 st.warning("Please upload a source document first.")

#     elif module == "MCQ Generation":
#         if st.session_state.strategic_plan_parsed:
#             if st.button("Generate & Save MCQs (Core)"):
#                 token_tracker.reset()
#                 st.session_state.module_ran = "MCQ Generation"
#                 try:
#                     all_mcqs = []
#                     topics = st.session_state.strategic_plan_parsed
#                     progress_bar = st.progress(0, text="Initializing MCQ generation...")

#                     for i, topic_obj in enumerate(topics):
#                         with st.spinner(f"Processing topic {i+1}/{len(topics)}: '{topic_obj.get('topic')}'..."):
#                             crew, _ = get_crew("MCQ Generation", json.dumps(topic_obj), 
#                                                difficulty=st.session_state.selected_difficulty, 
#                                                bloom_q_counts=st.session_state.bloom_q_counts)
#                             result = crew.kickoff()
                            
#                             if result and hasattr(result, 'raw') and 'refined' in str(result.raw):
#                                 json_match = re.search(r'(\{.*\}|\[.*\])', result.raw, re.DOTALL)
#                                 if json_match:
#                                     try:
#                                         parsed_data = json.loads(json_match.group(0))
#                                         if isinstance(parsed_data, dict) and parsed_data.get('status') == 'refined':
#                                             all_mcqs.extend(parsed_data.get('mcqs', []))
#                                     except Exception: pass
                        
#                         progress_bar.progress((i + 1) / len(topics), text=f"Completed topic {i+1}/{len(topics)}. Pausing...")
#                         time.sleep(7)

#                     if all_mcqs:
#                         data_to_save = []
#                         for mcq in all_mcqs:
#                             data_to_save.append({
#                                 "domain": mcq.get("domain", "General"),
#                                 "bloom_level": mcq.get("bloom_level", "N/A"),
#                                 "question": mcq.get("question"), 
#                                 "answer": mcq.get("correct_answer"), 
#                                 "rationale": mcq.get("rationale")
#                             })

#                         output_filename = "mcqs.json"
#                         with open(output_filename, 'w', encoding='utf-8') as f:
#                             json.dump(data_to_save, f, indent=4, ensure_ascii=False)
#                         st.success(f"✅ Core MCQs saved to `{output_filename}`!")
#                         st.session_state.text_output = f"Core questions and answers were saved to `{output_filename}`. You can now run 'Filter Questions'."
#                     else:
#                         st.warning("No MCQs were generated.")
                    
#                     progress_bar.empty()
#                     token_tracker.display()
#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")
#                     token_tracker.display()
#         else:
#             st.info("Please run 'Strategic Plan' first.")

#     elif module == "Filter Questions":
#         if os.path.exists("mcqs.json"):
#             if st.button("Filter for Numeric Questions"):
#                 token_tracker.reset()
#                 st.session_state.module_ran = "Filter Questions"
#                 try:
#                     with open("mcqs.json", 'r', encoding='utf-8') as f:
#                         questions_data = json.load(f)
                    
#                     numeric_questions = []
#                     progress_bar = st.progress(0, text="Analyzing questions...")

#                     for i, q_obj in enumerate(questions_data):
#                         with st.spinner(f"Classifying question {i+1}/{len(questions_data)}..."):
#                             crew, _ = get_crew("Filter Questions", json.dumps(q_obj))
#                             result = crew.kickoff()
                            
#                             classification = result.raw.strip() if hasattr(result, 'raw') else str(result).strip()
#                             if "Numeric" in classification:
#                                 numeric_questions.append(q_obj)
                        
#                         progress_bar.progress((i + 1) / len(questions_data))
#                         time.sleep(1)
                    
#                     output_filename = "mcqs_filtered.json"
#                     with open(output_filename, 'w', encoding='utf-8') as f:
#                         json.dump(numeric_questions, f, indent=4, ensure_ascii=False)
                    
#                     st.success(f"✅ Filtering complete! Kept {len(numeric_questions)} of {len(questions_data)} questions.")
#                     st.session_state.text_output = f"Filtered questions saved to `{output_filename}`. You can now run 'Distractor Generation'."
#                     progress_bar.empty()
#                     token_tracker.display()

#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")
#                     token_tracker.display()
#         else:
#             st.info("Please run 'MCQ Generation' first to create 'mcqs.json'.")

#     elif module == "Distractor Generation":
#         if os.path.exists("mcqs_filtered.json"):
#              if st.button("Generate Final Quiz"):
#                 token_tracker.reset()
#                 st.session_state.module_ran = "Distractor Generation"
#                 st.session_state.user_answers = {}
#                 st.session_state.quiz_submitted = False
#                 try:
#                     with open("mcqs_filtered.json", 'r', encoding='utf-8') as f:
#                         questions_data = json.load(f)
                    
#                     final_quiz_data = []
#                     progress_bar = st.progress(0, text="Initializing...")

#                     for i, q_obj in enumerate(questions_data):
#                         with st.spinner(f"Generating options for question {i+1}/{len(questions_data)}..."):
#                             crew, _ = get_crew("Distractor Generation", json.dumps(q_obj))
#                             result = crew.kickoff()
                            
#                             distractors_with_rationales = []
#                             if result and hasattr(result, 'raw'):
#                                 json_match = re.search(r'(\[.*\])', result.raw, re.DOTALL)
#                                 if json_match:
#                                     try:
#                                         parsed_options = json.loads(json_match.group(0))
#                                         if isinstance(parsed_options, list):
#                                             distractors_with_rationales = parsed_options
#                                     except Exception: pass
                            
#                             options = [d.get('option', f'Invalid Option {i+1}') for d in distractors_with_rationales] + [q_obj['answer']]
#                             random.shuffle(options)
                            
#                             distractor_rationales_map = {d.get('option'): d.get('misleading_rationale') for d in distractors_with_rationales}

#                             final_quiz_data.append({
#                                 "question": q_obj['question'],
#                                 "options": options,
#                                 "correct_answer": q_obj['answer'],
#                                 "correct_rationale": q_obj['rationale'],
#                                 "distractor_rationales": distractor_rationales_map,
#                                 "domain": q_obj.get("domain", "General"),
#                                 "bloom_level": q_obj.get("bloom_level", "N/A")
#                             })
                        
#                         progress_bar.progress((i + 1) / len(questions_data))
#                         time.sleep(1)

#                     st.session_state.final_quiz_data = final_quiz_data
#                     st.session_state.final_quiz_json_output = json.dumps(final_quiz_data, indent=4)
#                     st.success("✅ Final quiz generated!")
#                     progress_bar.empty()
#                     token_tracker.display()
#                     st.rerun()

#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")
#                     token_tracker.display()
#         else:
#             st.info("Please run 'Filter Questions' first to create 'mcqs_filtered.json'.")


# # --- Main Page Content Display ---
# if not st.session_state.module_ran:
#     st.info("Upload a document and select a module from the sidebar to begin.")

# elif st.session_state.module_ran == "Distractor Generation":
#     st.header("Final Quiz")
#     quiz_data = st.session_state.get('final_quiz_data', [])

#     if not quiz_data:
#         st.warning("No quiz data found. Please run 'Distractor Generation' first.")
#     else:
#         with st.form("final_quiz_form"):
#             for i, mcq in enumerate(quiz_data):
#                 st.markdown(f"##### Q{i+1} ({mcq.get('bloom_level', '')}): {mcq.get('question', 'N/A')}")
#                 options = mcq.get('options', [])
#                 user_choice = st.radio("Select your answer:", options, key=f"q_{i}", index=None, disabled=st.session_state.quiz_submitted)
#                 if user_choice:
#                     st.session_state.user_answers[i] = user_choice
#                 st.markdown("---")
#             submit_button = st.form_submit_button("Submit Answers", disabled=st.session_state.quiz_submitted)

#         if submit_button:
#             st.session_state.quiz_submitted = True
#             st.rerun()

#         if st.session_state.quiz_submitted:
#             st.subheader("Quiz Results")
#             score = 0
#             for i, mcq in enumerate(quiz_data):
#                 user_answer = st.session_state.user_answers.get(i)
#                 correct_answer = mcq.get('correct_answer')
                
#                 st.markdown(f"**Q{i+1} ({mcq.get('bloom_level', '')}): {mcq.get('question')}**")
#                 st.write(f"Your Answer: **{user_answer if user_answer else 'No answer chosen'}**")
#                 st.write(f"Correct Answer: **{correct_answer}**")

#                 if user_answer == correct_answer:
#                     st.success("Correct!")
#                     score += 1
#                     with st.expander("View Rationale"):
#                         st.markdown(mcq.get('correct_rationale', 'No rationale provided.'))
#                 else:
#                     st.error("Incorrect!")
#                     with st.expander("View Explanation"):
#                         explanation = mcq.get('distractor_rationales', {}).get(user_answer, "No specific explanation for this option is available.")
#                         st.markdown(explanation)
#                 st.markdown("---")
            
#             st.markdown(f"### Your Final Score: {score}/{len(quiz_data)}")
            
#             if st.button("Retake Quiz"):
#                 st.session_state.user_answers = {}
#                 st.session_state.quiz_submitted = False
#                 st.rerun()
        
#         st.download_button("📥 Download Quiz as JSON", st.session_state.final_quiz_json_output, "final_quiz.json", "application/json")


# elif st.session_state.module_ran == "Strategic Plan":
#     st.header("Refined Strategic Plan")
#     if st.session_state.strategic_plan_parsed:
#         st.dataframe(st.session_state.strategic_plan_parsed)
#         with st.expander("View Raw JSON"):
#             st.json(st.session_state.strategic_plan_parsed)
# elif st.session_state.module_ran == "Knowledge Graph":
#     st.header("Learning Path Flowchart")
#     if st.session_state.knowledge_graph_dot:
#         st.graphviz_chart(st.session_state.knowledge_graph_dot)
#         st.subheader("Final DOT Code")
#         st.code(st.session_state.knowledge_graph_dot, language='dot')
# else:
#     if st.session_state.text_output:
#         st.header(f"Output for {st.session_state.module_ran}")
#         st.markdown(st.session_state.text_output, unsafe_allow_html=True)
#         if st.session_state.module_ran not in ["MCQ Generation", "Distractor Generation", "Filter Questions"]:
#             st.download_button(f"📥 Download {st.session_state.module_ran}", st.session_state.text_output, f"{st.session_state.module_ran.lower().replace(' ', '_')}_output.md")

# main.py
# # HFAIQUIZ
# import streamlit as st
# import re
# import json5 as json
# from crew.crew_factory import get_crew
# import graphviz
# import litellm
# from litellm import exceptions as litellm_exceptions
# import os
# import random
# import time
# from utils.token_tracker import token_tracker, track_token_usage_callback

# # Register the callback with litellm at the start of the app
# litellm.success_callback = [track_token_usage_callback]

# def parse_dot_graph(dot_code):
#     nodes, edges, node_labels = set(), [], {}
#     node_definition_pattern = re.compile(r'^\s*(\w+|"[^"]+")\s*\[label="([^"]+)"\];')
#     edge_definition_pattern = re.compile(r'^\s*(\w+|"[^"]+")\s*->\s*(\w+|"[^"]+")\s*(?:\[[^\]]*\])?;')
#     id_to_label_map = {}
#     for line in dot_code.split('\n'):
#         line = line.strip()
#         node_match = node_definition_pattern.match(line)
#         if node_match:
#             raw_id, label = node_match.groups()
#             nodes.add(label)
#             node_labels[label] = label
#             id_to_label_map[raw_id] = label
#     adj = {label: set() for label in nodes}
#     for line in dot_code.split('\n'):
#         line = line.strip()
#         edge_match = edge_definition_pattern.match(line)
#         if edge_match:
#             source_raw_id, target_raw_id = edge_match.groups()
#             source_label, target_label = id_to_label_map.get(source_raw_id), id_to_label_map.get(target_raw_id)
#             if source_label in nodes and target_label in nodes:
#                 edges.append((source_label, target_label))
#                 adj[source_label].add(target_label)
#     label_to_id = {label: label for label in nodes}
#     return nodes, edges, adj, node_labels, label_to_id

# def init_session_state():
#     defaults = {
#         "module_ran": None, "text_output": None, "strategic_plan_output": None,
#         "selected_difficulty": "medium", "strategic_plan_parsed": [],
#         "knowledge_graph_dot": None,
#         "bloom_q_counts": {"Remember": 1, "Understand": 1, "Apply": 1, "Analyze": 1, "Evaluate": 1, "Create": 1},
#         "final_quiz_data": [],
#         "final_quiz_json_output": None,
#         "user_answers": {},
#         "quiz_submitted": False,
#         "ai_answers": []
#     }
#     for key, value in defaults.items():
#         if key not in st.session_state:
#             st.session_state[key] = value

# # --- UI Rendering ---
# st.set_page_config(page_title="Spirit", layout="wide")
# st.title("Spirit")
# init_session_state()

# # --- Sidebar Controls ---
# with st.sidebar:
#     st.header("Controls")
#     module_options = ["Summarization", "Notes", "Explanation", "Knowledge Graph", "Strategic Plan", "MCQ Generation", "Distractor Generation", "AI Quiz Taker"]
#     module = st.sidebar.selectbox("Select a module", module_options)

#     uploaded_md = None
#     if module not in ["Distractor Generation", "AI Quiz Taker"]:
#         uploaded_md = st.file_uploader("Upload Source Document", type=["md", "txt"])

#     if module == "MCQ Generation":
#         st.markdown("---")
#         st.session_state.selected_difficulty = st.selectbox("Select Difficulty", ["easy", "medium", "hard"])
        
#         st.subheader("Questions per Bloom's Level:")
#         bloom_levels = ["Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"]
#         for level in bloom_levels:
#             st.session_state.bloom_q_counts[level] = st.number_input(
#                 f"'{level}' Questions", 
#                 min_value=0, 
#                 max_value=2, 
#                 value=st.session_state.bloom_q_counts.get(level, 1), 
#                 key=f"num_{level}_q"
#             )
    
#     st.markdown("---")

#     # --- Action Buttons & Logic ---
#     if module in ["Summarization", "Notes", "Explanation", "Knowledge Graph", "Strategic Plan"]:
#         if st.button(f"Run {module}"):
#             if uploaded_md:
#                 with st.spinner(f"Running {module}..."):
#                     token_tracker.reset()
#                     st.session_state.module_ran = module
#                     markdown_text = uploaded_md.read().decode("utf-8")
#                     try:
#                         crew, _ = get_crew(module, markdown_text, strategic_plan_data=st.session_state.strategic_plan_parsed)
#                         result = crew.kickoff()
#                         st.session_state.text_output = str(result.raw) if hasattr(result, 'raw') else str(result)
#                         if module == "Strategic Plan":
#                             match = re.search(r'\[.*\]', st.session_state.text_output, re.DOTALL)
#                             if match:
#                                 json_string = match.group(0)
#                                 st.session_state.strategic_plan_output = json_string
#                                 st.session_state.strategic_plan_parsed = json.loads(json_string)
#                             else: st.error("Strategic Plan did not return valid JSON.")
#                         elif module == "Knowledge Graph":
#                             match = re.search(r"digraph\s+.*\{[\s\S]*\}", st.session_state.text_output, re.DOTALL)
#                             if match: st.session_state.knowledge_graph_dot = match.group(0)
#                             else: st.warning("Knowledge Graph did not return valid DOT code.")
#                         st.success("Generation Complete!")
#                     except Exception as e:
#                         st.error(f"An unexpected error occurred: {e}")
#                     token_tracker.display()
#             else:
#                 st.warning("Please upload a source document first.")

#     elif module == "MCQ Generation":
#         if st.session_state.strategic_plan_parsed:
#             if st.button("Generate & Save MCQs (Core)"):
#                 token_tracker.reset()
#                 st.session_state.module_ran = "MCQ Generation"
#                 try:
#                     all_mcqs = []
#                     topics = st.session_state.strategic_plan_parsed
#                     progress_bar = st.progress(0, text="Initializing MCQ generation...")

#                     for i, topic_obj in enumerate(topics):
#                         with st.spinner(f"Processing topic {i+1}/{len(topics)}: '{topic_obj.get('topic')}'..."):
#                             crew, _ = get_crew("MCQ Generation", json.dumps(topic_obj), 
#                                                difficulty=st.session_state.selected_difficulty, 
#                                                bloom_q_counts=st.session_state.bloom_q_counts)
#                             result = crew.kickoff()
                            
#                             if result and hasattr(result, 'raw') and 'refined' in str(result.raw):
#                                 json_match = re.search(r'(\{.*\}|\[.*\])', result.raw, re.DOTALL)
#                                 if json_match:
#                                     try:
#                                         parsed_data = json.loads(json_match.group(0))
#                                         if isinstance(parsed_data, dict) and parsed_data.get('status') == 'refined':
#                                             all_mcqs.extend(parsed_data.get('mcqs', []))
#                                     except Exception: pass
                        
#                         progress_bar.progress((i + 1) / len(topics), text=f"Completed topic {i+1}/{len(topics)}. Pausing...")
#                         time.sleep(7)

#                     if all_mcqs:
#                         data_to_save = []
#                         for mcq in all_mcqs:
#                             data_to_save.append({
#                                 "domain": mcq.get("domain", "General"),
#                                 "bloom_level": mcq.get("bloom_level", "N/A"),
#                                 "question": mcq.get("question"), 
#                                 "answer": mcq.get("correct_answer"), 
#                                 "rationale": mcq.get("rationale")
#                             })

#                         output_filename = "mcqs.json"
#                         with open(output_filename, 'w', encoding='utf-8') as f:
#                             json.dump(data_to_save, f, indent=4, ensure_ascii=False)
#                         st.success(f"✅ Core MCQs saved to `{output_filename}`!")
#                         st.session_state.text_output = f"Core questions saved to `{output_filename}`. You can now run 'Distractor Generation'."
#                     else:
#                         st.warning("No MCQs were generated.")
                    
#                     progress_bar.empty()
#                     token_tracker.display()
#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")
#                     token_tracker.display()
#         else:
#             st.info("Please run 'Strategic Plan' first.")

#     elif module == "Distractor Generation":
#         if os.path.exists("mcqs.json"):
#              if st.button("Generate Final Quiz"):
#                 token_tracker.reset()
#                 st.session_state.module_ran = "Distractor Generation"
#                 st.session_state.user_answers = {}
#                 st.session_state.quiz_submitted = False
#                 try:
#                     with open("mcqs.json", 'r', encoding='utf-8') as f:
#                         questions_data = json.load(f)
                    
#                     final_quiz_data = []
#                     progress_bar = st.progress(0, text="Initializing...")

#                     for i, q_obj in enumerate(questions_data):
#                         with st.spinner(f"Generating options for question {i+1}/{len(questions_data)}..."):
#                             crew, _ = get_crew("Distractor Generation", json.dumps(q_obj))
#                             result = crew.kickoff()
                            
#                             distractors_with_rationales = []
#                             if result and hasattr(result, 'raw'):
#                                 json_match = re.search(r'(\[.*\])', result.raw, re.DOTALL)
#                                 if json_match:
#                                     try:
#                                         parsed_options = json.loads(json_match.group(0))
#                                         if isinstance(parsed_options, list):
#                                             distractors_with_rationales = parsed_options
#                                     except Exception: pass
                            
#                             options = [d.get('option', f'Invalid Option {i+1}') for d in distractors_with_rationales] + [q_obj['answer']]
#                             random.shuffle(options)
                            
#                             distractor_rationales_map = {d.get('option'): d.get('misleading_rationale') for d in distractors_with_rationales}

#                             final_quiz_data.append({
#                                 "question": q_obj['question'],
#                                 "options": options,
#                                 "correct_answer": q_obj['answer'],
#                                 "correct_rationale": q_obj['rationale'],
#                                 "distractor_rationales": distractor_rationales_map,
#                                 "domain": q_obj.get("domain", "General"),
#                                 "bloom_level": q_obj.get("bloom_level", "N/A")
#                             })
                        
#                         progress_bar.progress((i + 1) / len(questions_data))
#                         time.sleep(1)

#                     st.session_state.final_quiz_data = final_quiz_data
                    
#                     output_filename = "final_quiz.json"
#                     with open(output_filename, 'w', encoding='utf-8') as f:
#                         json.dump(final_quiz_data, f, indent=4, ensure_ascii=False)
                    
#                     st.session_state.final_quiz_json_output = json.dumps(final_quiz_data, indent=4)
#                     st.success(f"✅ Final quiz generated and saved to `{output_filename}`!")
#                     progress_bar.empty()
#                     token_tracker.display()
#                     st.rerun()

#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")
#                     token_tracker.display()
#         else:
#             st.info("Please run 'MCQ Generation' first to create 'mcqs.json'.")

#     elif module == "AI Quiz Taker":
#         if os.path.exists("final_quiz.json"):
#             if st.button("Start AI Quiz Attempt"):
#                 token_tracker.reset()
#                 st.session_state.module_ran = "AI Quiz Taker"
#                 try:
#                     with open("final_quiz.json", 'r', encoding='utf-8') as f:
#                         quiz_data = json.load(f)
                    
#                     ai_answers = []
#                     progress_bar = st.progress(0, text="AI is starting the quiz...")

#                     for i, q_obj in enumerate(quiz_data):
#                         with st.spinner(f"AI is answering question {i+1}/{len(quiz_data)}..."):
                            
#                             sanitized_q_obj = {
#                                 "question": q_obj.get("question"),
#                                 "options": q_obj.get("options")
#                             }
                            
#                             crew, _ = get_crew("AI Quiz Taker", json.dumps(sanitized_q_obj))
#                             result = crew.kickoff()
#                             ai_answer = result.raw.strip() if hasattr(result, 'raw') else str(result).strip()
#                             ai_answers.append(ai_answer)
                        
#                         progress_bar.progress((i + 1) / len(quiz_data))
#                         time.sleep(1)
                    
#                     st.session_state.final_quiz_data = quiz_data
#                     st.session_state.ai_answers = ai_answers
#                     st.success("✅ AI has completed the quiz!")
#                     progress_bar.empty()
#                     token_tracker.display()
#                     st.rerun()

#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")
#                     token_tracker.display()
#         else:
#             st.info("Please run 'Distractor Generation' first to create 'final_quiz.json'.")


# # --- Main Page Content Display ---
# if not st.session_state.module_ran:
#     st.info("Upload a document and select a module from the sidebar to begin.")

# elif st.session_state.module_ran == "AI Quiz Taker":
#     st.header("🤖 AI Quiz Taker Results")
#     quiz_data = st.session_state.get('final_quiz_data', [])
#     ai_answers = st.session_state.get('ai_answers', [])

#     if not quiz_data or not ai_answers:
#         st.warning("No AI quiz results found. Please run the 'AI Quiz Taker' module.")
#     else:
#         score = 0
#         for i, mcq in enumerate(quiz_data):
#             ai_answer = ai_answers[i]
#             correct_answer = mcq.get('correct_answer')
            
#             st.markdown(f"**Q{i+1}: {mcq.get('question')}**")
#             st.write(f"Correct Answer: **{correct_answer}**")
            
#             if ai_answer == correct_answer:
#                 st.success(f"AI's Answer: **{ai_answer}** (Correct!)")
#                 score += 1
#             else:
#                 st.error(f"AI's Answer: **{ai_answer}** (Incorrect!)")
#             st.markdown("---")
        
#         st.markdown(f"### AI's Final Score: {score}/{len(quiz_data)}")

# elif st.session_state.module_ran == "Distractor Generation":
#     st.header("Final Quiz")
#     quiz_data = st.session_state.get('final_quiz_data', [])

#     if not quiz_data:
#         st.warning("No quiz data found. Please run 'Distractor Generation' first.")
#     else:
#         with st.form("final_quiz_form"):
#             for i, mcq in enumerate(quiz_data):
#                 st.markdown(f"##### Q{i+1} ({mcq.get('bloom_level', '')}): {mcq.get('question', 'N/A')}")
#                 options = mcq.get('options', [])
#                 user_choice = st.radio("Select your answer:", options, key=f"q_{i}", index=None, disabled=st.session_state.quiz_submitted)
#                 if user_choice:
#                     st.session_state.user_answers[i] = user_choice
#                 st.markdown("---")
#             submit_button = st.form_submit_button("Submit Answers", disabled=st.session_state.quiz_submitted)

#         if submit_button:
#             st.session_state.quiz_submitted = True
#             st.rerun()

#         if st.session_state.quiz_submitted:
#             st.subheader("Quiz Results")
#             score = 0
#             for i, mcq in enumerate(quiz_data):
#                 user_answer = st.session_state.user_answers.get(i)
#                 correct_answer = mcq.get('correct_answer')
                
#                 st.markdown(f"**Q{i+1} ({mcq.get('bloom_level', '')}): {mcq.get('question')}**")
#                 st.write(f"Your Answer: **{user_answer if user_answer else 'No answer chosen'}**")
#                 st.write(f"Correct Answer: **{correct_answer}**")

#                 if user_answer == correct_answer:
#                     st.success("Correct!")
#                     score += 1
#                     with st.expander("View Rationale"):
#                         st.markdown(mcq.get('correct_rationale', 'No rationale provided.'))
#                 else:
#                     st.error("Incorrect!")
#                     with st.expander("View Explanation"):
#                         explanation = mcq.get('distractor_rationales', {}).get(user_answer, "No specific explanation for this option is available.")
#                         st.markdown(explanation)
#                 st.markdown("---")
            
#             st.markdown(f"### Your Final Score: {score}/{len(quiz_data)}")
            
#             if st.button("Retake Quiz"):
#                 st.session_state.user_answers = {}
#                 st.session_state.quiz_submitted = False
#                 st.rerun()
        
#         st.download_button("📥 Download Quiz as JSON", st.session_state.final_quiz_json_output, "final_quiz.json", "application/json")


# elif st.session_state.module_ran == "Strategic Plan":
#     st.header("Refined Strategic Plan")
#     if st.session_state.strategic_plan_parsed:
#         st.dataframe(st.session_state.strategic_plan_parsed)
#         with st.expander("View Raw JSON"):
#             st.json(st.session_state.strategic_plan_parsed)
# elif st.session_state.module_ran == "Knowledge Graph":
#     st.header("Learning Path Flowchart")
#     if st.session_state.knowledge_graph_dot:
#         st.graphviz_chart(st.session_state.knowledge_graph_dot)
#         st.subheader("Final DOT Code")
#         st.code(st.session_state.knowledge_graph_dot, language='dot')
# else:
#     if st.session_state.text_output:
#         st.header(f"Output for {st.session_state.module_ran}")
#         st.markdown(st.session_state.text_output, unsafe_allow_html=True)
#         if st.session_state.module_ran not in ["MCQ Generation", "Distractor Generation", "Filter Questions", "AI Quiz Taker"]:
#             st.download_button(f"📥 Download {st.session_state.module_ran}", st.session_state.text_output, f"{st.session_state.module_ran.lower().replace(' ', '_')}_output.md")

# # RACAR and local loading
# import streamlit as st
# import re
# import json5 as json
# from crew.crew_factory import get_crew
# import graphviz
# import os
# import random
# import time
# from thefuzz import fuzz
# # Import the loaded pipeline from settings
# from config.settings import llm_hf_pipeline

# # REMOVED: The local model loading function is no longer needed here.

# def parse_dot_graph(dot_code):
#     """
#     Parses Graphviz DOT code to extract nodes and edges.
#     """
#     nodes, edges, node_labels = set(), [], {}
#     node_definition_pattern = re.compile(r'^\s*(\w+|"[^"]+")\s*\[label="([^"]+)"\];')
#     edge_definition_pattern = re.compile(r'^\s*(\w+|"[^"]+")\s*->\s*(\w+|"[^"]+")\s*(?:\[[^\]]*\])?;')
#     id_to_label_map = {}
#     for line in dot_code.split('\n'):
#         line = line.strip()
#         node_match = node_definition_pattern.match(line)
#         if node_match:
#             raw_id, label = node_match.groups()
#             nodes.add(label)
#             node_labels[label] = label
#             id_to_label_map[raw_id] = label
#     adj = {label: set() for label in nodes}
#     for line in dot_code.split('\n'):
#         line = line.strip()
#         edge_match = edge_definition_pattern.match(line)
#         if edge_match:
#             source_raw_id, target_raw_id = edge_match.groups()
#             source_label, target_label = id_to_label_map.get(source_raw_id), id_to_label_map.get(target_raw_id)
#             if source_label in nodes and target_label in nodes:
#                 edges.append((source_label, target_label))
#                 adj[source_label].add(target_label)
#     label_to_id = {label: label for label in nodes}
#     return nodes, edges, adj, node_labels, label_to_id

# def init_session_state():
#     """Initializes the Streamlit session state with default values."""
#     defaults = {
#         "module_ran": None, "text_output": None, "strategic_plan_output": None,
#         "selected_difficulty": "medium", "strategic_plan_parsed": [],
#         "knowledge_graph_dot": None,
#         "bloom_q_counts": {"Remember": 1, "Understand": 1, "Apply": 1, "Analyze": 1, "Evaluate": 1, "Create": 1},
#         "final_quiz_data": [], "final_quiz_json_output": None,
#         "user_answers": {}, "quiz_submitted": False, "ai_answers": []
#     }
#     for key, value in defaults.items():
#         if key not in st.session_state:
#             st.session_state[key] = value

# # --- UI Rendering ---
# st.set_page_config(page_title="Spirit", layout="wide")
# st.title("Spirit")
# init_session_state()

# # --- Sidebar Controls ---
# with st.sidebar:
#     st.header("Controls")
#     module_options = ["Summarization", "Notes", "Explanation", "Knowledge Graph", "Strategic Plan", "MCQ Generation", "Filter Questions", "Distractor Generation", "AI Quiz Taker"]
#     module = st.sidebar.selectbox("Select a module", module_options)

#     uploaded_md = None
#     if module not in ["Filter Questions", "Distractor Generation", "AI Quiz Taker"]:
#         uploaded_md = st.file_uploader("Upload Source Document", type=["md", "txt"])

#     if module == "MCQ Generation":
#         st.markdown("---")
#         st.session_state.selected_difficulty = st.selectbox("Select Difficulty", ["easy", "medium", "hard"])
#         st.subheader("Questions per Bloom's Level:")
#         bloom_levels = ["Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"]
#         for level in bloom_levels:
#             st.session_state.bloom_q_counts[level] = st.number_input(
#                 f"'{level}' Questions", 
#                 min_value=0, 
#                 max_value=2, 
#                 value=st.session_state.bloom_q_counts.get(level, 1), 
#                 key=f"num_{level}_q"
#             )
    
#     st.markdown("---")

#     # --- Action Buttons & Logic ---
#     if module in ["Summarization", "Notes", "Explanation", "Knowledge Graph", "Strategic Plan"]:
#         if st.button(f"Run {module}"):
#             if uploaded_md:
#                 with st.spinner(f"Running {module}..."):
#                     st.session_state.module_ran = module
#                     markdown_text = uploaded_md.read().decode("utf-8")
#                     try:
#                         crew, _ = get_crew(module, markdown_text, strategic_plan_data=st.session_state.strategic_plan_parsed)
#                         result = crew.kickoff()
#                         st.session_state.text_output = str(result.raw) if hasattr(result, 'raw') else str(result)
#                         if module == "Strategic Plan":
#                             match = re.search(r'\[.*\]', st.session_state.text_output, re.DOTALL)
#                             if match:
#                                 json_string = match.group(0)
#                                 st.session_state.strategic_plan_output = json_string
#                                 st.session_state.strategic_plan_parsed = json.loads(json_string)
#                             else: st.error("Strategic Plan did not return valid JSON.")
#                         elif module == "Knowledge Graph":
#                             match = re.search(r"digraph\s+.*\{[\s\S]*\}", st.session_state.text_output, re.DOTALL)
#                             if match: st.session_state.knowledge_graph_dot = match.group(0)
#                             else: st.warning("Knowledge Graph did not return valid DOT code.")
#                         st.success("Generation Complete!")
#                     except Exception as e:
#                         st.error(f"An unexpected error occurred: {e}")
#             else:
#                 st.warning("Please upload a source document first.")

#     elif module == "MCQ Generation":
#         if st.session_state.strategic_plan_parsed:
#             if st.button("Generate & Save MCQs (Core)"):
#                 st.session_state.module_ran = "MCQ Generation"
#                 try:
#                     all_mcqs = []
#                     topics = st.session_state.strategic_plan_parsed
#                     progress_bar = st.progress(0, text="Initializing MCQ generation...")
#                     for i, topic_obj in enumerate(topics):
#                         with st.spinner(f"Processing topic {i+1}/{len(topics)}..."):
#                             crew, _ = get_crew("MCQ Generation", json.dumps(topic_obj), 
#                                                difficulty=st.session_state.selected_difficulty, 
#                                                bloom_q_counts=st.session_state.bloom_q_counts)
#                             result = crew.kickoff()
#                             if result and hasattr(result, 'raw') and 'refined' in str(result.raw):
#                                 json_match = re.search(r'(\{.*\}|\[.*\])', result.raw, re.DOTALL)
#                                 if json_match:
#                                     try:
#                                         parsed_data = json.loads(json_match.group(0))
#                                         if isinstance(parsed_data, dict) and parsed_data.get('status') == 'refined':
#                                             all_mcqs.extend(parsed_data.get('mcqs', []))
#                                     except Exception: pass
#                         progress_bar.progress((i + 1) / len(topics))
#                         time.sleep(7)
#                     if all_mcqs:
#                         data_to_save = []
#                         for mcq in all_mcqs:
#                             mcq['topic'] = topic_obj.get('topic', 'Unknown')
#                             data_to_save.append({
#                                 "domain": mcq.get("domain", "General"), "bloom_level": mcq.get("bloom_level", "N/A"),
#                                 "question": mcq.get("question"), "answer": mcq.get("correct_answer"), 
#                                 "rationale": mcq.get("rationale"), "topic": mcq.get("topic")
#                             })
#                         output_filename = "mcqs.json"
#                         with open(output_filename, 'w', encoding='utf-8') as f:
#                             json.dump(data_to_save, f, indent=4, ensure_ascii=False)
#                         st.success(f"✅ Core MCQs saved to `{output_filename}`!")
#                         st.session_state.text_output = f"Core questions saved. You can now run 'Filter Questions'."
#                     else:
#                         st.warning("No MCQs were generated.")
#                     progress_bar.empty()
#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")
#         else:
#             st.info("Please run 'Strategic Plan' first.")

#     elif module == "Filter Questions":
#         if os.path.exists("mcqs.json"):
#             if st.button("Filter for Numeric Questions"):
#                 st.session_state.module_ran = "Filter Questions"
#                 try:
#                     with open("mcqs.json", 'r', encoding='utf-8') as f:
#                         questions_data = json.load(f)
#                     numeric_questions = []
#                     progress_bar = st.progress(0, text="Analyzing questions...")
#                     for i, q_obj in enumerate(questions_data):
#                         with st.spinner(f"Classifying question {i+1}/{len(questions_data)}..."):
#                             crew, _ = get_crew("Filter Questions", json.dumps(q_obj))
#                             result = crew.kickoff()
#                             classification = result.raw.strip() if hasattr(result, 'raw') else str(result).strip()
#                             if "Numeric" in classification:
#                                 numeric_questions.append(q_obj)
#                         progress_bar.progress((i + 1) / len(questions_data))
#                         time.sleep(1)
#                     output_filename = "mcqs_filtered.json"
#                     with open(output_filename, 'w', encoding='utf-8') as f:
#                         json.dump(numeric_questions, f, indent=4, ensure_ascii=False)
#                     st.success(f"✅ Filtering complete! Kept {len(numeric_questions)} of {len(questions_data)} questions.")
#                     st.session_state.text_output = f"Filtered questions saved. You can now run 'Distractor Generation'."
#                     progress_bar.empty()
#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")
#         else:
#             st.info("Please run 'MCQ Generation' first to create 'mcqs.json'.")

#     elif module == "Distractor Generation":
#         if os.path.exists("mcqs_filtered.json"):
#              if st.button("Generate Final Quiz"):
#                 st.session_state.module_ran = "Distractor Generation"
#                 st.session_state.user_answers, st.session_state.quiz_submitted = {}, False
#                 try:
#                     with open("mcqs_filtered.json", 'r', encoding='utf-8') as f:
#                         questions_data = json.load(f)
#                     final_quiz_data = []
#                     progress_bar = st.progress(0, text="Initializing...")
#                     for i, q_obj in enumerate(questions_data):
#                         with st.spinner(f"Generating options for question {i+1}/{len(questions_data)}..."):
#                             crew, _ = get_crew("Distractor Generation", json.dumps(q_obj))
#                             result = crew.kickoff()
#                             distractors_with_rationales = []
#                             if result and hasattr(result, 'raw'):
#                                 json_match = re.search(r'(\[.*\])', result.raw, re.DOTALL)
#                                 if json_match:
#                                     try:
#                                         parsed_options = json.loads(json_match.group(0))
#                                         if isinstance(parsed_options, list): distractors_with_rationales = parsed_options
#                                     except Exception: pass
#                             options = [d.get('option', f'Invalid Option {i+1}') for d in distractors_with_rationales] + [q_obj['answer']]
#                             random.shuffle(options)
#                             distractor_rationales_map = {d.get('option'): d.get('misleading_rationale') for d in distractors_with_rationales}
#                             final_quiz_data.append({
#                                 "question": q_obj['question'], "options": options, "correct_answer": q_obj['answer'],
#                                 "correct_rationale": q_obj['rationale'], "distractor_rationales": distractor_rationales_map,
#                                 "domain": q_obj.get("domain", "General"), "bloom_level": q_obj.get("bloom_level", "N/A"),
#                                 "topic": q_obj.get("topic", "Unknown")
#                             })
#                         progress_bar.progress((i + 1) / len(questions_data))
#                         time.sleep(1)
#                     st.session_state.final_quiz_data = final_quiz_data
#                     data_for_json_file = [ {k: v for k, v in mcq.items() if k != 'options'} for mcq in final_quiz_data ]
#                     output_filename = "final_quiz.json"
#                     with open(output_filename, 'w', encoding='utf-8') as f:
#                         json.dump(data_for_json_file, f, indent=4, ensure_ascii=False)
#                     st.session_state.final_quiz_json_output = json.dumps(data_for_json_file, indent=4)
#                     st.success(f"✅ Final quiz generated and saved to `{output_filename}`!")
#                     progress_bar.empty()
#                     st.rerun()
#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")
#         else:
#             st.info("Please run 'Filter Questions' first.")

#     elif module == "AI Quiz Taker":
#         if os.path.exists("final_quiz.json"):
#             if st.button("Start AI Quiz Attempt"):
#                 st.session_state.module_ran = "AI Quiz Taker"
#                 try:
#                     # Use the imported pipeline from settings
#                     qwen_pipeline = llm_hf_pipeline
#                     with open("final_quiz.json", 'r', encoding='utf-8') as f:
#                         quiz_data = json.load(f)
                    
#                     ai_answers = []
#                     progress_bar = st.progress(0, text="AI is starting the quiz...")

#                     for i, q_obj in enumerate(quiz_data):
#                         with st.spinner(f"AI is answering question {i+1}/{len(quiz_data)}..."):
#                             options_str = "\n".join([f"- {opt}" for opt in q_obj.get('options', [])])
#                             prompt = f"Question: {q_obj['question']}\nOptions:\n{options_str}\nRespond with only the text of the correct option."
#                             response = qwen_pipeline(prompt, max_new_tokens=100, do_sample=False)
#                             ai_raw_output = response[0]['generated_text'].replace(prompt, '').strip()
#                             ai_chosen_option = "AI failed to select an option."
#                             current_options = q_obj.get("options", [])
#                             if current_options:
#                                 best_match = max(current_options, key=lambda option: fuzz.partial_ratio(option, ai_raw_output))
#                                 ai_chosen_option = best_match
#                             ai_answers.append(ai_chosen_option)
#                         progress_bar.progress((i + 1) / len(quiz_data))
                    
#                     st.session_state.final_quiz_data = quiz_data
#                     st.session_state.ai_answers = ai_answers
#                     st.success("✅ AI has completed the quiz!")
#                     progress_bar.empty()
#                     st.rerun()

#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")
#         else:
#             st.info("Please run 'Distractor Generation' first.")

# # --- Main Page Content Display ---
# if not st.session_state.module_ran:
#     st.info("Upload a document and select a module from the sidebar to begin.")

# elif st.session_state.module_ran == "AI Quiz Taker":
#     st.header("🤖 AI Quiz Taker Results")
#     quiz_data = st.session_state.get('final_quiz_data', [])
#     ai_answers = st.session_state.get('ai_answers', [])
#     if not quiz_data or not ai_answers:
#         st.warning("No AI quiz results found.")
#     else:
#         score = 0
#         for i, mcq in enumerate(quiz_data):
#             ai_answer = ai_answers[i]
#             correct_answer = mcq.get('correct_answer')
#             st.markdown(f"**Q{i+1}: {mcq.get('question')}**")
#             st.write(f"Correct Answer: **{correct_answer}**")
#             if ai_answer == correct_answer:
#                 st.success(f"AI's Answer: **{ai_answer}** (Correct!)")
#                 score += 1
#             else:
#                 st.error(f"AI's Answer: **{ai_answer}** (Incorrect!)")
#             st.markdown("---")
#         st.markdown(f"### AI's Final Score: {score}/{len(quiz_data)}")

# elif st.session_state.module_ran == "Distractor Generation":
#     st.header("Final Quiz")
#     quiz_data = st.session_state.get('final_quiz_data', [])
#     if not quiz_data:
#         st.warning("No quiz data found.")
#     else:
#         with st.form("final_quiz_form"):
#             for i, mcq in enumerate(quiz_data):
#                 st.markdown(f"##### Q{i+1} ({mcq.get('bloom_level', '')}): {mcq.get('question', 'N/A')}")
#                 options = mcq.get('options', [])
#                 user_choice = st.radio("Select your answer:", options, key=f"q_{i}", index=None, disabled=st.session_state.quiz_submitted)
#                 if user_choice:
#                     st.session_state.user_answers[i] = user_choice
#                 st.markdown("---")
#             submit_button = st.form_submit_button("Submit Answers")
#         if submit_button:
#             st.session_state.quiz_submitted = True
#             st.rerun()
#         if st.session_state.quiz_submitted:
#             st.subheader("Quiz Results")
#             score = 0
#             for i, mcq in enumerate(quiz_data):
#                 user_answer = st.session_state.user_answers.get(i)
#                 correct_answer = mcq.get('correct_answer')
#                 st.markdown(f"**Q{i+1} ({mcq.get('bloom_level', '')}): {mcq.get('question')}**")
#                 st.write(f"Your Answer: **{user_answer if user_answer else 'No answer chosen'}**")
#                 st.write(f"Correct Answer: **{correct_answer}**")
#                 if user_answer == correct_answer:
#                     st.success("Correct!")
#                     score += 1
#                     with st.expander("View Rationale"):
#                         st.markdown(mcq.get('correct_rationale', 'No rationale provided.'))
#                 else:
#                     st.error("Incorrect!")
#                     with st.expander("View Explanation"):
#                         explanation = mcq.get('distractor_rationales', {}).get(user_answer, "No specific explanation available.")
#                         st.markdown(explanation)
#                 st.markdown("---")
#             st.markdown(f"### Your Final Score: {score}/{len(quiz_data)}")
#             if st.button("Retake Quiz"):
#                 st.session_state.user_answers, st.session_state.quiz_submitted = {}, False
#                 st.rerun()
#         st.download_button("📥 Download Quiz as JSON", st.session_state.final_quiz_json_output, "final_quiz.json", "application/json")

# elif st.session_state.module_ran == "Strategic Plan":
#     st.header("Refined Strategic Plan")
#     if st.session_state.strategic_plan_parsed:
#         st.dataframe(st.session_state.strategic_plan_parsed)
#         with st.expander("View Raw JSON"):
#             st.json(st.session_state.strategic_plan_parsed)
# elif st.session_state.module_ran == "Knowledge Graph":
#     st.header("Learning Path Flowchart")
#     if st.session_state.knowledge_graph_dot:
#         st.graphviz_chart(st.session_state.knowledge_graph_dot)
#         st.subheader("Final DOT Code")
#         st.code(st.session_state.knowledge_graph_dot, language='dot')
# elif st.session_state.module_ran == "Subjective Q&A":
#     st.header("📝 Subjective Questions & Answers")
#     qa_data = st.session_state.get('subjective_qa_data', [])
#     if not qa_data:
#         st.warning("No subjective questions were generated.")
#     else:
#         for i, item in enumerate(qa_data):
#             st.subheader(f"Question {i+1}")
#             st.info(item.get('question', 'N/A'))
#             with st.expander("View Ground Truth Answer"):
#                 st.success(item.get('answer', 'N/A'))
#         st.download_button("📥 Download Q&A as JSON", json.dumps(qa_data, indent=4), "subjective_qna.json", "application/json")
# elif st.session_state.module_ran == "Level 2 Evaluation":
#     st.header("📝 Level 2 Subjective Evaluation Results")
#     eval_data = st.session_state.get('level_2_evaluations', [])
#     if not eval_data:
#         st.warning("No evaluation data found.")
#     else:
#         for i, evaluation in enumerate(eval_data):
#             st.subheader(f"Analysis of Topic: {evaluation['topic']}")
#             with st.container(border=True):
#                 st.markdown("**Subjective Question:**"); st.info(evaluation['subjective_question'])
#                 st.markdown("**Student LLM's Answer:**"); st.warning(evaluation['student_llm_answer'])
#                 st.markdown("**Grader AI's Evaluation (What was missing):**"); st.error(evaluation['evaluation'])
#                 with st.expander("View Ground Truth Answer"):
#                     st.success(evaluation['ground_truth_answer'])
#             st.markdown("---")
# else:
#     if st.session_state.text_output:
#         st.header(f"Output for {st.session_state.module_ran}")
#         st.markdown(st.session_state.text_output, unsafe_allow_html=True)
#         if st.session_state.module_ran not in ["MCQ Generation", "Distractor Generation", "AI Quiz Taker", "Subjective Q&A"]:
#             st.download_button(f"📥 Download {st.session_state.module_ran}", st.session_state.text_output, f"{st.session_state.module_ran.lower().replace(' ', '_')}_output.md")

# Storing Answers
import streamlit as st
import re
import json5 as json
from crew.crew_factory import get_crew
import graphviz
import os
import random
import time
from thefuzz import fuzz
import asyncio
from datetime import datetime, timedelta
from config.settings import student_llm
import litellm

# ===============================================
# GLOBAL RESILIENCE HELPERS
# ===============================================

# ✅ ASYNC WRAPPER FOR CREW.KICKOFF WITH JITTER
async def kickoff_async_jittered(crew, min_delay=0.5, max_delay=1.5):
    """Runs Crew.kickoff() asynchronously with slight random delay."""
    await asyncio.sleep(random.uniform(min_delay, max_delay))
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, crew.kickoff)

# ✅ RETRY LOGIC WITH EXPONENTIAL BACKOFF
def invoke_with_retry(llm, prompt, retries=6):
    """Invoke LLM with exponential backoff retry on RateLimitError."""
    for attempt in range(retries):
        try:
            return llm.invoke(prompt)
        except litellm.RateLimitError:
            wait = min(30, (2 ** attempt) + random.uniform(0, 1))
            st.warning(f"⚠️ Rate limit hit (attempt {attempt+1}/{retries}). Retrying in {wait:.1f}s...")
            time.sleep(wait)
    raise RuntimeError("❌ Rate limit exceeded even after multiple retries.")

# ✅ GENERIC THROTTLED ASYNC RUNNER
async def run_async_tasks_with_progress(status_box, tasks, task_labels, max_concurrency=2):
    """Runs asyncio tasks with concurrency control and ETA tracking."""
    start_time = time.time()
    results = []
    semaphore = asyncio.Semaphore(max_concurrency)

    async def run_with_semaphore(task, label):
        async with semaphore:
            res = await task
            return label, res

    for i, coro in enumerate(
        asyncio.as_completed([run_with_semaphore(t, task_labels[i]) for i, t in enumerate(tasks)])
    ):
        label, result = await coro
        results.append(result)
        elapsed = time.time() - start_time
        avg = elapsed / (i + 1)
        remaining = len(tasks) - (i + 1)
        eta = timedelta(seconds=int(avg * remaining))
        status_box.write(f"✅ Completed '{label}' (ETA: {eta})")
    return results

# ===============================================
# SESSION STATE & UTILITIES
# ===============================================

def init_session_state():
    defaults = {
        "pipeline_running": False,
        "pipeline_complete": False,
        "strategic_plan_parsed": [],
        "knowledge_graph_dot": None,
        "final_quiz_data": [],
        "ai_answers": [],
        "bulk_dataset": [],
        "source_material": "",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def run_crew_and_parse_json(crew, expected_format='list'):
    """Runs crew.kickoff() and parses JSON/JSON5 robustly with error correction."""
    result = crew.kickoff()
    if not (result and hasattr(result, 'raw')):
        return None

    raw_text = result.raw
    regex = (
        r"```json\s*(\[[\s\S]*\])\s*```" if expected_format == 'list'
        else r"```json\s*(\{[\s\S]*\})\s*```"
    )
    match = re.search(regex, raw_text, re.DOTALL)
    if not match:
        return None

    json_text = match.group(1).strip()

    try:
        return json.loads(json_text)
    except Exception as e:
        # Log malformed JSON for debugging
        with open("bad_outputs.log", "a") as f:
            f.write(f"\n\n=== Malformed JSON Detected ===\n{datetime.now()}\n{json_text}\nError: {e}\n")

        # Attempt to auto-repair: quote keys, remove trailing commas
        repaired = re.sub(r'([{,]\s*)([A-Za-z_][A-Za-z0-9_]*)(\s*:)', r'\1"\2"\3', json_text)
        repaired = re.sub(r',(\s*[}\]])', r'\1', repaired)  # remove trailing commas

        try:
            return json.loads(repaired)
        except Exception as e2:
            # Final fallback: return None but log
            with open("bad_outputs.log", "a") as f:
                f.write(f"\nRepair failed: {e2}\nRepaired text:\n{repaired}\n")
            return None


# ===============================================
# STREAMLIT UI
# ===============================================

st.set_page_config(page_title="Spirit", layout="wide")
st.title("Spirit")
init_session_state()

with st.sidebar:
    st.header("Controls")
    uploaded_md = st.file_uploader("Upload Source Document", type=["md", "txt"])
    st.markdown("---")
    st.subheader("Pipeline Settings")
    selected_difficulty = st.selectbox("MCQ Difficulty", ["easy", "medium", "hard"], index=1)
    num_total_questions = st.number_input("Total Bulk Dataset Questions (approx.)", min_value=50, max_value=1000, value=200, step=50)
    st.markdown("---")
    if st.button("Run Full Pipeline", type="primary"):
        if uploaded_md:
            st.session_state.pipeline_running = True
            st.session_state.pipeline_complete = False
            st.session_state.source_material = uploaded_md.read().decode("utf-8")
        else:
            st.warning("Please upload a source document first.")

# ===============================================
# PIPELINE EXECUTION
# ===============================================

if st.session_state.pipeline_running:
    try:
        start_time = time.time()

        # ---------- STEP 1: STRATEGIC PLAN ----------
        with st.status("Step 1: Generating Strategic Plan...", expanded=True) as status:
            crew, _ = get_crew("Strategic Plan", st.session_state.source_material)
            parsed_data = run_crew_and_parse_json(crew, expected_format='list')
            if not parsed_data:
                status.update(label="Strategic Plan Failed!", state="error")
                st.stop()

            # ✅ Normalize parsed data to list of dicts
            if all(isinstance(item, str) for item in parsed_data):
                parsed_data = [{"topic": item} for item in parsed_data]

            st.session_state.strategic_plan_parsed = parsed_data

            # Uncomment for debugging:
            # st.json(parsed_data)

            status.update(label=f"Strategic Plan Complete! ({len(parsed_data)} topics found)", state="complete")

        # ---------- STEP 2: KNOWLEDGE GRAPH ----------
        with st.status("Step 2: Generating Knowledge Graph...", expanded=True) as status:
            crew, _ = get_crew("Knowledge Graph", st.session_state.source_material)
            result = crew.kickoff()
            match = re.search(r"digraph\s+.*\{[\s\S]*\}", str(result.raw), re.DOTALL)
            if not match:
                status.update(label="Knowledge Graph Failed!", state="error")
                st.stop()
            st.session_state.knowledge_graph_dot = match.group(0)
            with open("knowledge_graph.dot", "w") as f:
                f.write(st.session_state.knowledge_graph_dot)
            status.update(label="Knowledge Graph Complete!", state="complete")

        # ---------- STEP 3: MCQ GENERATION ----------
        async def run_mcq_step():
            with st.status("Step 3: Generating MCQs (adaptive throttling)...", expanded=True) as status:
                mcq_crews = [
                    get_crew("MCQ Generation", json.dumps(topic),
                             difficulty=selected_difficulty,
                             bloom_q_counts={"Remember": 1, "Understand": 1, "Apply": 1, "Analyze": 1,"Evaluate": 1, "Create": 1})[0]
                    for topic in st.session_state.strategic_plan_parsed
                ]

                # ✅ Safe label extraction
                mcq_labels = [
                    f"MCQs for '{t.get('topic', 'N/A')}'" if isinstance(t, dict) else f"MCQs for '{t}'"
                    for t in st.session_state.strategic_plan_parsed
                ]

                # ⚙️ Throttled & jittered
                mcq_results = await run_async_tasks_with_progress(status, [kickoff_async_jittered(c) for c in mcq_crews], mcq_labels, max_concurrency=2)
                all_mcqs = []
                for res in mcq_results:
                    if res and hasattr(res, 'raw'):
                        match = re.search(r"```json\s*(\{[\s\S]*\})\s*```", res.raw, re.DOTALL)
                        if match:
                            data = json.loads(match.group(1).strip())
                            all_mcqs.extend(data.get('mcqs', []))
                with open("mcqs.json", "w") as f:
                    json.dump(all_mcqs, f, indent=4)
                status.update(label=f"MCQ Generation Complete! ({len(all_mcqs)} questions)", state="complete")
                return all_mcqs

        all_mcqs = asyncio.run(run_mcq_step())

        # ---------- STEP 4: DISTRACTOR GENERATION ----------
        async def run_distractor_step():
            with st.status("Step 4: Generating Distractors (ultra-safe mode)...", expanded=True) as status:
                distractor_crews = [get_crew("Distractor Generation", json.dumps(q_obj))[0] for q_obj in all_mcqs]
                distractor_labels = [f"Distractors for Q{i+1}" for i in range(len(all_mcqs))]

                # Lowest concurrency for NIM safety
                distractor_results = await run_async_tasks_with_progress(
                    status,
                    [kickoff_async_jittered(c) for c in distractor_crews],
                    distractor_labels,
                    max_concurrency=1
                )

                final_quiz_data = []
                for i, result in enumerate(distractor_results):
                    q_obj = all_mcqs[i]
                    distractors = []
                    if result and hasattr(result, 'raw'):
                        match = re.search(r"```json\s*(\[[\s\S]*\])\s*```", result.raw, re.DOTALL)
                        if match:
                            distractors = json.loads(match.group(1).strip())
                    options = [d.get("option", "") for d in distractors] + [q_obj["correct_answer"]]
                    random.shuffle(options)
                    final_quiz_data.append({
                        "question": q_obj["question"],
                        "options": options,
                        "correct_answer": q_obj["correct_answer"],
                        "rationale": q_obj["rationale"],
                        "topic": q_obj.get("topic"),
                    })
                st.session_state.final_quiz_data = final_quiz_data
                status.update(label="Distractor Generation Complete!", state="complete")

        asyncio.run(run_distractor_step())

        # ---------- STEP 5: AI QUIZ TAKER ----------
        with st.status("Step 5: Running AI Quiz Taker (retry protected)...", expanded=True) as status:
            ai_answers = []
            for i, q_obj in enumerate(st.session_state.final_quiz_data):
                st.write(f"🤖 AI answering question {i+1}/{len(st.session_state.final_quiz_data)}...")
                options_str = "\n".join([f"- {opt}" for opt in q_obj.get("options", [])])
                prompt = f"Question: {q_obj['question']}\nOptions:\n{options_str}\nRespond with only the text of the correct option."
                response = invoke_with_retry(student_llm, prompt)
                ai_raw_output = response.content.strip()
                ai_chosen_option = max(
                    q_obj.get("options", []),
                    key=lambda opt: fuzz.partial_ratio(opt, ai_raw_output)
                ) if q_obj.get("options") else "AI failed"
                ai_answers.append(ai_chosen_option)
            st.session_state.ai_answers = ai_answers
            status.update(label="AI Quiz Taker Complete!", state="complete")

        # ---------- STEP 6: BULK DATASET GENERATION ----------
        async def run_bulk_dataset_step():
            with st.status(f"Step 6: Generating {num_total_questions} triplets (adaptive throttling)...", expanded=True) as status:
                num_per_topic = num_total_questions // len(st.session_state.strategic_plan_parsed)
                bulk_crews = [
                    get_crew("Bulk Dataset Generator", json.dumps(topic),
                             num_questions=num_per_topic,
                             source_material=st.session_state.source_material)[0]
                    for topic in st.session_state.strategic_plan_parsed
                ]

                # ✅ Safe label extraction
                bulk_labels = [
                    f"Bulk questions for '{t.get('topic', 'N/A')}'" if isinstance(t, dict) else f"Bulk questions for '{t}'"
                    for t in st.session_state.strategic_plan_parsed
                ]

                bulk_results = await run_async_tasks_with_progress(status, [kickoff_async_jittered(c) for c in bulk_crews], bulk_labels, max_concurrency=2)
                all_triplets = []
                for result in bulk_results:
                    if result and hasattr(result, "raw"):
                        match = re.search(r"```json\s*(\[[\s\S]*\])\s*```", result.raw, re.DOTALL)
                        if match:
                            all_triplets.extend(json.loads(match.group(1).strip()))
                st.session_state.bulk_dataset = all_triplets
                with open("bulk_dataset.json", "w") as f:
                    json.dump(all_triplets, f, indent=4)
                status.update(label=f"Bulk Dataset Generation Complete! ({len(all_triplets)} triplets)", state="complete")

        asyncio.run(run_bulk_dataset_step())

        # ---------- FINALIZE ----------
        st.session_state.pipeline_running = False
        st.session_state.pipeline_complete = True
        st.rerun()

    except Exception as e:
        st.error(f"❌ The pipeline failed with an error: {e}")
        st.session_state.pipeline_running = False

# ===============================================
# OUTPUT DISPLAY
# ===============================================

if st.session_state.pipeline_complete:
    st.header("✅ Pipeline Finished")
    st.success("All processes completed successfully. You can now review the outputs.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Strategic Plan")
        st.dataframe(st.session_state.strategic_plan_parsed, height=300)
        st.subheader("AI Quiz Taker Results")
        score = sum(
            1 for i, mcq in enumerate(st.session_state.final_quiz_data)
            if st.session_state.ai_answers[i] == mcq.get("correct_answer")
        )
        st.metric("AI Score", f"{score} / {len(st.session_state.final_quiz_data)}")

    with col2:
        st.subheader("Knowledge Graph")
        if st.session_state.knowledge_graph_dot:
            st.graphviz_chart(st.session_state.knowledge_graph_dot)

    st.subheader("Bulk Dataset Generated")
    st.info(f"Generated a total of {len(st.session_state.bulk_dataset)} question-answer-reasoning triplets.")
    st.dataframe(st.session_state.bulk_dataset)
    st.download_button("📥 Download Bulk Dataset",
                       json.dumps(st.session_state.bulk_dataset, indent=4),
                       "bulk_dataset.json",
                       "application/json")
else:
    st.info("Upload a document and configure your settings in the sidebar, then click 'Run Full Pipeline'.")
