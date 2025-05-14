import streamlit as st
import openai
import os
import time

# =============================
# Securely load OpenAI API Key
# =============================
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    st.error("OpenAI API Key not found. Set it with 'export OPENAI_API_KEY=your_api_key' in your terminal.")
else:
    openai.api_key = api_key

# =============================
# Generate Quiz Function
# =============================
def generate_quiz(topic, difficulty, num_questions, include_explanations, prompt):
    """
    Generates a quiz based on the specified parameters using OpenAI's GPT model.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Change to "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a quiz generator."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,   # Increased max tokens for more questions
            temperature=0.7,
            n=1,
            stop=None
        )
        quiz_content = response['choices'][0]['message']['content']
        return quiz_content
    except openai.error.RateLimitError as e:
        st.error(f"Rate limit error: {e}. Please try again later.")
    except openai.error.APIError as e:
        st.error(f"API error: {e}. Please contact support.")
    except openai.error.OpenAIError as e:
        st.error(f"Error generating quiz: {e}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
    return None

# =============================
# Streamlit Interface
# =============================
st.title("Interactive Quiz Generator")
st.write("Create custom quizzes interactively with the power of LLMs!")

# =============================
# Quiz Input Fields
# =============================
topic = st.text_input("Topic (e.g., Quantum Physics)", "Quantum Physics")
difficulty = st.selectbox("Difficulty Level", ["easy", "medium", "hard"], index=0)
num_questions = st.slider("Number of Questions", 1, 20, 5)
question_type = st.selectbox("Question Types", ["Multiple Choice", "True/False", "Short Answer"])
sub_topics = st.text_input("Specific Sub-topics (Optional)", "Wave-particle duality")
context_keywords = st.text_input("Context Keywords (Optional)", "theory")
audience = st.text_input("Target Audience (Optional)", "Undergraduate Physics Students")
language = st.selectbox("Language", ["English", "Other"], index=0)
include_explanations = st.radio("Include Explanations?", ["Yes", "No"], index=0)
max_length = st.slider("Maximum Length per Question (in words)", 10, 100, 20)

# =============================
# Generate Quiz
# =============================
if st.button("Generate Quiz"):
    st.write("Generating quiz...")

    # Create the prompt dynamically
    prompt = f"""
    Generate a {difficulty} {num_questions}-question {question_type} quiz on the topic of '{topic}'.
    """

    if context_keywords:
        prompt += f" Focus on the following keywords: {context_keywords}."
    if sub_topics:
        prompt += f" Include sub-topics such as {sub_topics}."
    if audience:
        prompt += f" The target audience is {audience}."
    if include_explanations == "Yes":
        prompt += " Include explanations for each answer."
    prompt += f" Limit each question and answer to a maximum of {max_length} words."

    # =============================
    # Generate and Display Quiz
    # =============================
    quiz = None
    while not quiz:
        quiz = generate_quiz(topic, difficulty, num_questions, include_explanations == "Yes", prompt)
        if not quiz:
            time.sleep(10)  # Retry after waiting 10 seconds (adjust as necessary)
