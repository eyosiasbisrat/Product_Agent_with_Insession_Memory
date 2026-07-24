import os
import streamlit as st
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

st.set_page_config(
    page_title="Blood Work Analysis",
    page_icon="🩺",
    layout="wide",
)

st.markdown(
    """
    <div style="background: linear-gradient(90deg, #0f4c81 0%, #1f78c1 100%); padding: 24px 28px; border-radius: 18px; color: white; margin-bottom: 24px;">
        <h1 style="margin:0; font-size:2.4rem;">🩺 Blood Work Analysis Assistant</h1>
        <p style="margin:10px 0 0 0; font-size:1rem; opacity:0.92;">Paste or upload a blood report, then let Anthropic generate structured findings and a practical diet recommendation.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    st.error("Please set ANTHROPIC_API_KEY in your .env file before running the analysis.")
    st.stop()

llm = ChatAnthropic(
    model="claude-sonnet-4-5",
    api_key=api_key,
    temperature=0,
)


def get_text(response):
    if hasattr(response, "content"):
        return response.content
    if hasattr(response, "text"):
        return response.text
    return str(response)

with st.sidebar:
    st.header("Input")
    st.write("Upload a blood report file or paste the full text below.")
    uploaded_file = st.file_uploader("Upload blood report", type=["txt"])
    st.divider()
    st.markdown("**Tip:** A complete report with reference ranges yields the best extraction results.")

sample_report = """
Patient Name: Ravi Sharma
Age: 42
Gender: Male

Complete Blood Count (CBC):
Hemoglobin: 13.2 g/dL (Reference: 13.5 - 17.5)
WBC Count: 7800 /uL (Reference: 4000 - 10000)
Platelets: 180000 /uL (Reference: 150000 - 450000)

Lipid Profile:
Total Cholesterol: 240 mg/dL (Reference: <200)
Triglycerides: 180 mg/dL (Reference: <150)
HDL: 38 mg/dL (Reference: >40)
LDL: 155 mg/dL (Reference: <100)

Blood Sugar:
Fasting Glucose: 118 mg/dL (Reference: 70 - 100)
HbA1c: 6.8% (Reference: 4.0 - 5.6)
"""

if uploaded_file is not None:
    blood_report = uploaded_file.read().decode("utf-8")
else:
    blood_report = st.text_area(
        "Blood report",
        value=sample_report,
        height=300,
        placeholder="Paste the blood report content here...",
    )

if not blood_report or not blood_report.strip():
    st.warning("Please provide a blood report before running the analysis.")

run_analysis = st.button("Run Analysis", type="primary")

if run_analysis and blood_report and blood_report.strip():
    with st.spinner("Analyzing the blood report..."):
        extraction_prompt = f"""
You are a medical data extraction assistant.

From the blood report below, extract ALL test values and classify each one as HIGH, LOW, or NORMAL
based on the reference ranges provided in the report.

Format your response as:
- Test Name: value | Status: HIGH/LOW/NORMAL | Reference: range

Blood Report:
{blood_report}
"""

        extraction_response = llm.invoke(extraction_prompt)
        extracted_values = get_text(extraction_response)

        diet_prompt = f"""
You are a clinical nutritionist specializing in Indian dietary habits.

Based on the blood work analysis below, write:
1. A short health summary in 4-5 lines explaining the patient's condition in simple language
2. A short, practical Indian diet plan having only two sections:
   (1) Foods to avoid
   (2) Foods to eat more of
Do not include any other sections in the diet plan.

Blood Work Analysis:
{extracted_values}
"""

        diet_response = llm.invoke(diet_prompt)
        diet_plan = get_text(diet_response)

    st.success("Analysis completed successfully.")
    st.markdown("---")

    left, right = st.columns([1, 1])
    with left:
        st.subheader("Stage 1 — Extracted Findings")
        st.write("Structured values extracted from the blood report, including status and reference ranges.")
        st.text_area("Structured analysis", value=extracted_values, height=300)

    with right:
        st.subheader("Stage 2 — Health Summary & Diet Plan")
        st.write("A concise summary and practical Indian diet recommendation.")
        st.text_area("Health summary and diet guidance", value=diet_plan, height=300)
