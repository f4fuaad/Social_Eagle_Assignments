import streamlit as st

# App title
st.title("Simple Quiz App")

# Quiz questions
questions = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "Which language is this app built in?": "Python"
}

score = 0

# Display questions
for question, answer in questions.items():
    user_answer = st.text_input(question)
    if user_answer:
        if user_answer.strip().lower() == answer.lower():
            st.success("Correct!")
            score += 1
        else:
            st.error(f"Wrong! Correct answer: {answer}")

st.write(f"Your total score is: {score}/{len(questions)}")
