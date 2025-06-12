import streamlit as st
from src.summary_generator import summarize_text
from src.quiz_generator import generate_quiz

st.title("📚 AI-Powered Learning Assistant")

option = st.selectbox("Choose an option", ["Summarize Topic", "Generate Quiz"])

text_input = st.text_area("Paste lesson content here:")

if st.button("Run"):
    if option == "Summarize Topic":
        summary = summarize_text(text_input)
        st.subheader("Summary")
        st.write(summary)
    else:
        quiz = generate_quiz(text_input)
        st.subheader("Generated Quiz")
        st.write(quiz)
