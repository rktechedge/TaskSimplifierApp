import streamlit as st
import os
import nest_asyncio
import time

# Allow async operations in Streamlit
nest_asyncio.apply()

# -----------------------------
# 🔐 Load API key securely
# -----------------------------
try:
    os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
    GEMINI_KEY_AVAILABLE = True
except Exception:
    GEMINI_KEY_AVAILABLE = False

# -----------------------------
# Gemini Setup
# -----------------------------
import google.generativeai as genai

if GEMINI_KEY_AVAILABLE:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
else:
    st.warning("⚠ No Gemini API key found in Streamlit Secrets. Running in simulated mode.")

# Minimal Gemini helper
def gemini_call(prompt: str):
    if not GEMINI_KEY_AVAILABLE:
        return "(SIMULATED RESPONSE — No API key configured)"
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        resp = model.generate_content(prompt)
        return resp.text or "(No output)"
    except Exception as e:
        return f"(ERROR calling Gemini: {e})"

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🧠 Task Simplifier — Streamlit Demo")
st.write("This demo uses Gemini to generate a task title, summary, and priority score.")

task = st.text_area("Enter your task:", "Pay electricity bill by Friday, urgent")

if st.button("Run Task Simplifier"):
    st.write("### Running pipeline...")
    time.sleep(0.4)

    title = gemini_call(f"Generate a short task title for: {task}")
    summary = gemini_call(f"Summarize this task: {task}")
    score = gemini_call(f"Give a priority score (0–100) for: {task}. Return only the number.")

    try:
        score_val = float("".join([c for c in score if c.isdigit() or c == "."]))
    except:
        score_val = 50.0

    priority = (
        "high" if score_val > 70 else
        "medium" if score_val > 40 else
        "low"
    )

    st.subheader("✨ Task Details")
    st.json({
        "title": title,
        "description": task,
        "summary": summary,
        "priority_score": score_val,
        "priority": priority
    })

st.markdown("---")
st.caption("Built with Streamlit + Gemini 2.0 Flash")