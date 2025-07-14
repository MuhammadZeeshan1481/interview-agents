# ui/app.py
import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import run_interview

st.set_page_config(page_title="Interview Agent System", layout="wide")

st.title("🧠 AI-Powered Job Interview Agents")
st.write("Enter a job role and watch the agents simulate an interview.")

role = st.text_input("Job Role", value="React Developer")
num_q = st.slider("Number of Questions", 1, 5, 3)

if st.button("Run Interview"):
    with st.spinner("Agents at work..."):
        try:
            results = run_interview(role, num_q)
            for item in results:
                st.subheader("💬 Question")
                st.write(item["question"])
                
                st.subheader("🧑‍💻 Answer")
                st.write(item["answer"])
                
                st.subheader("🧾 Evaluation")
                st.write(item["feedback"])
        except Exception as e:
            st.error(f"Something went wrong: {e}")
