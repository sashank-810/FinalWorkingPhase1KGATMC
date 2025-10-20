import streamlit as st, json, plotly.graph_objects as go
from scripts.utils import load_cfg

cfg = load_cfg("configs/nim_config.yaml")
st.set_page_config(page_title="LfT Evaluation Dashboard", layout="wide")
st.title("📊 Learning-from-Teacher (LfT) Evaluation Dashboard")

path = "data/final/eval_report.json"
try:
    data = json.load(open(path))
except FileNotFoundError:
    st.error("Evaluation report not found. Run evaluate_models.py first.")
    st.stop()

st.subheader("Models Used")
st.json({
    "Teacher": cfg["TEACHER_MODEL"],
    "Student (Fine-tuned)": cfg["STUDENT_MODEL"],
    "Evaluator": cfg["EVALUATOR_MODEL"]
})

st.header("Model Performance Metrics")
cols = st.columns(2)
cols[0].metric("Student BLEU", round(data["student_bleu"]["bleu"], 4))
cols[0].metric("Teacher BLEU", round(data["teacher_bleu"]["bleu"], 4))
cols[1].metric("Student ROUGE-L", round(data["student_rouge"]["rougeL"]["mid"]["fmeasure"], 4))
cols[1].metric("Teacher ROUGE-L", round(data["teacher_rouge"]["rougeL"]["mid"]["fmeasure"], 4))

# Radar chart comparison
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[data["student_bleu"]["bleu"]*100,
       data["student_rouge"]["rougeL"]["mid"]["fmeasure"]*100],
    theta=["BLEU","ROUGE-L"], fill="toself", name="Student Model"
))
fig.add_trace(go.Scatterpolar(
    r=[data["teacher_bleu"]["bleu"]*100,
       data["teacher_rouge"]["rougeL"]["mid"]["fmeasure"]*100],
    theta=["BLEU","ROUGE-L"], fill="toself", name="Teacher Model"
))
fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0,100])),
    showlegend=True,
    title="Student vs Teacher Performance"
)
st.plotly_chart(fig, use_container_width=True)
