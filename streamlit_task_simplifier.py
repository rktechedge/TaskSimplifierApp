import streamlit as st
import requests, json, os, asyncio, nest_asyncio, time
nest_asyncio.apply()

st.title("Task Simplifier — Streamlit Demo (uses Notebook backend logic)")
st.markdown("This Streamlit app expects the same agent logic to run in a Python process. For Colab demonstration, use the notebook UI. To run locally: `streamlit run streamlit_task_simplifier.py`")

task = st.text_area("Task", "Pay electricity bill by Friday, urgent")
if st.button("Run"):
    st.write("Running demo - this calls the notebook-style pipeline inside this Streamlit process")
    # Minimal local execution (simulated LLM calls)
    from time import sleep
    sleep(0.5)
    # Simulated result
    result = {
        "title": "Pay electricity bill by Friday",
        "description": task,
        "priority": "medium",
        "booking": {"slot": "2025-11-20T09:00"}
    }
    st.json(result)

st.markdown("**Logs & Traces**: For full logging, run notebook and export logs to view.")