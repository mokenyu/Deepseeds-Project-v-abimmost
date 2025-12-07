import streamlit as st
import random

# Quiz data structure
questions = {
    # Science category
    "Science": {
        # Easy science questions
        "easy": [
            {"question": "What planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": 1},            {"question": "What is the chemical symbol for water?", "options": ["O2", "H2O", "CO2", "N2"], "answer": 1},

            {"question": "What gas do plants breathe in?", "options": ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"], "answer": 2},
            # More easy science questions
            {"question": "Water freezes at what temperature (C)?", "options": ["0", "100", "50", "10"], "answer": 0},
            {"question": "How many legs does a spider have?", "options": ["6", "8", "10", "12"], "answer": 1},
            {"question": "Sun is a...", "options": ["Planet", "Comet", "Star", "Asteroid"], "answer": 2}
        ],
        "hard": [
            {"question": "What is the atomic number of Carbon?", "options": ["4", "6", "8", "12"], "answer": 1},
            {"question": "Speed of light?", "options": ["300,000 km/s", "150,000 km/s", "3,000 km/s", "1,000 km/s"], "answer": 0},
            {"question": "Avogadro's number?", "options": ["6.02e23", "3.14", "1.61", "2.71"], "answer": 0},
            {"question": "What organ produces insulin?", "options": ["Liver", "Pancreas", "Heart", "Lung"], "answer": 1},
            {"question": "Gas used in light bulbs?", "options": ["Oxygen", "Neon", "Helium", "Argon"], "answer": 3}
        ]
    },
    # History category
    "History": {
        # Easy history questions
        "easy": [
            {"question": "Who was the first president of the USA?", "options": ["Lincoln", "Jefferson", "Washington", "Adams"], "answer": 2},
            {"question": "What year did WWII end?", "options": ["1945", "1939", "1950", "1960"], "answer": 0},
            {"question": "Where is the Great Wall?", "options": ["India", "China", "Korea", "Japan"], "answer": 1},
            # More easy history questions
            {"question": "Pyramids built by?", "options": ["Romans", "Greeks", "Egyptians", "Aztecs"], "answer": 2},
            {"question": "What ship sank in 1912?", "options": ["Olympic", "Carpathia", "Titanic", "Lusitania"], "answer": 2}
        ],
        "hard": [
            {"question": "Napoleon exiled to?", "options": ["Elba", "Malta", "Crete", "Corsica"], "answer": 0},
            {"question": "Berlin Wall fell in?", "options": ["1989", "1991", "1980", "1975"], "answer": 0},
            {"question": "Magna Carta signed?", "options": ["1215", "1315", "1415", "1515"], "answer": 0},
            {"question": "Start of WWI?", "options": ["1914", "1920", "1905", "1939"], "answer": 0},
            {"question": "First printing press?", "options": ["Gutenberg", "Tesla", "Newton", "Da Vinci"], "answer": 0}
        ]
    }
}

# Initialize session state variables
if 'quiz_started' not in st.session_state:
    # Set initial state for the quiz
    st.session_state.quiz_started = False
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.selected_category = None
    st.session_state.selected_difficulty = None
    st.session_state.quiz_questions = []
    st.session_state.answer_submitted = False
    st.session_state.user_answer = None

# Function to start the quiz
def start_quiz():
    st.session_state.selected_category = st.session_state.category_select
    st.session_state.selected_difficulty = st.session_state.difficulty_select
    if st.session_state.selected_category and st.session_state.selected_difficulty:
        # Filter questions based on selected category and difficulty
        st.session_state.quiz_questions = questions[st.session_state.selected_category][st.session_state.selected_difficulty]
        random.shuffle(st.session_state.quiz_questions) # Shuffle questions
        st.session_state.quiz_started = True
        st.session_state.current_question_index = 0
        st.session_state.score = 0
        st.session_state.answer_submitted = False
        st.session_state.user_answer = None
    else:
        st.error("Please select both a category and a difficulty.")

# Function to handle answer submission
def submit_answer_callback():
    current_q = st.session_state.quiz_questions[st.session_state.current_question_index]
    correct_answer_index = current_q["answer"]

    if st.session_state.user_answer is not None:
        if st.session_state.user_answer == correct_answer_index:
            # Increment score if answer is correct
            st.session_state.score += 1
            st.success("Correct!")
        else:
            st.error(f"Wrong! The correct answer was: {current_q["options"][correct_answer_index]}")
        st.session_state.answer_submitted = True
    else:
        st.warning("Please select an answer.")

# Function to move to the next question
def next_question_callback():
    st.session_state.current_question_index += 1
    st.session_state.answer_submitted = False
    st.session_state.user_answer = None

# Function to restart the quiz
def restart_quiz():
    st.session_state.quiz_started = False
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.selected_category = None
    st.session_state.selected_difficulty = None
    st.session_state.quiz_questions = []
    st.session_state.answer_submitted = False
    st.session_state.user_answer = None

# Title of the Streamlit app
st.title("Quiz Master")

# Display quiz settings if the quiz hasn't started
if not st.session_state.quiz_started:
    st.header("Select Quiz Settings")
    with st.form("quiz_settings"):
        st.selectbox("Select Category", options=list(questions.keys()), key="category_select")
        st.selectbox("Select Difficulty", options=["easy", "hard"], key="difficulty_select")
        st.form_submit_button("Start Quiz", on_click=start_quiz)
else:
    total_questions = len(st.session_state.quiz_questions)
    if st.session_state.current_question_index < total_questions:
        current_q = st.session_state.quiz_questions[st.session_state.current_question_index]
        
        st.subheader(f"Question {st.session_state.current_question_index + 1}/{total_questions}")
        st.write(current_q["question"])

        # Display options as radio buttons
        user_choice = st.radio("Your Answer:", current_q["options"], key=f"q_{st.session_state.current_question_index}", index=None)
        
        # Store user's choice in session_state for callback
        if user_choice is not None:
            st.session_state.user_answer = current_q["options"].index(user_choice)

        col1, col2 = st.columns(2)
        with col1:
            st.button("Submit Answer", on_click=submit_answer_callback, disabled=st.session_state.answer_submitted)
        with col2:
            if st.session_state.answer_submitted:
                st.button("Next Question", on_click=next_question_callback)

    else:
        st.header("Quiz Finished!")
        st.write(f"You scored {st.session_state.score} out of {total_questions} correct answers.")
        st.button("Restart Quiz", on_click=restart_quiz)
