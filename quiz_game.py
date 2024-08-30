import streamlit as st

def display_question(question, options):
    """Display a question with multiple-choice options."""
    st.write(f"**{question}**")
    user_answer = st.radio("Select your answer:", options)
    return user_answer

def main():
    st.title("Quiz Game")
    st.write("Welcome to the quiz! Answer the following questions:")

    # List of questions and their options
    questions = [
        {"question": "What is actually electricity? ", 
         "options": [" A flow of water", "A flow of air", "A flow of electrons", " A flow of atoms"], 
         "answer": "A flow of electrons"},

        {"question": "Which of the following is not an international organisation?", 
         "options": ["FIFA", "NATO", "ASEAN", "FBI"], 
         "answer": "FBI"},

        {"question": "Which of the following disorders is the fear of being alone?", 
         "options": ["Agoraphobia", "Aerophobia", "Acrophobia", "Arachnophobia"], 
         "answer": "Agoraphobia"},

        {"question": " In total, how many novels were written by the Bronte sisters?", 
         "options": ["4", "5", "6", "7"], 
         "answer": "7"},

        {"question": "What was the first country to use tanks in combat during World War I?", 
         "options": ["France", "Japan", "Britain", "Germany"], 
         "answer": "Britain"}

        


    ]

    # Track the number of correct answers
    correct_answers = 0

    # Loop through each question
    for i, q in enumerate(questions):
        user_answer = display_question(q["question"], q["options"])
        if user_answer == q["answer"]:
            st.success("Correct!")
            correct_answers += 1
        else:
            st.error(f"Wrong! The correct answer is {q['answer']}.")

    # Display the final score
        st.write("Your Score")
        st.write(f"You got {correct_answers} out of {len(questions)} correct!")

if __name__ == "__main__":
    main()

