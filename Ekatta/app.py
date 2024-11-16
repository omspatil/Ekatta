from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define quiz questions
questions = [
    {"question": "What is the capital of France?", "options": {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"}, "answer": "C"},
    {"question": "Which planet is known as the Red Planet?", "options": {"A": "Earth", "B": "Mars", "C": "Venus", "D": "Jupiter"}, "answer": "B"},
    {"question": "What is the largest ocean on Earth?", "options": {"A": "Atlantic Ocean", "B": "Indian Ocean", "C": "Arctic Ocean", "D": "Pacific Ocean"}, "answer": "D"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": {"A": "Charles Dickens", "B": "J.K. Rowling", "C": "William Shakespeare", "D": "Mark Twain"}, "answer": "C"},
    {"question": "What is the square root of 64?", "options": {"A": "6", "B": "7", "C": "8", "D": "9"}, "answer": "C"},
    {"question": "Which country is known as the Land of the Rising Sun?", "options": {"A": "China", "B": "Japan", "C": "Thailand", "D": "South Korea"}, "answer": "B"},
    {"question": "Who painted the Mona Lisa?", "options": {"A": "Vincent van Gogh", "B": "Pablo Picasso", "C": "Leonardo da Vinci", "D": "Claude Monet"}, "answer": "C"},
    {"question": "What is the chemical symbol for water?", "options": {"A": "O2", "B": "CO2", "C": "H2O", "D": "NaCl"}, "answer": "C"},
    {"question": "Which country hosted the 2016 Summer Olympics?", "options": {"A": "China", "B": "Brazil", "C": "United Kingdom", "D": "Russia"}, "answer": "B"},
    {"question": "What is the largest mammal on Earth?", "options": {"A": "Elephant", "B": "Great White Shark", "C": "Blue Whale", "D": "Giraffe"}, "answer": "C"},
    {"question": "Who was the first man to step on the moon?", "options": {"A": "Buzz Aldrin", "B": "Yuri Gagarin", "C": "Michael Collins", "D": "Neil Armstrong"}, "answer": "D"},
    {"question": "How many continents are there?", "options": {"A": "5", "B": "6", "C": "7", "D": "8"}, "answer": "C"},
    {"question": "What is the smallest prime number?", "options": {"A": "1", "B": "2", "C": "3", "D": "5"}, "answer": "B"},
    {"question": "What is the capital of Australia?", "options": {"A": "Sydney", "B": "Melbourne", "C": "Canberra", "D": "Perth"}, "answer": "C"},
    {"question": "Which element has the atomic number 1?", "options": {"A": "Oxygen", "B": "Nitrogen", "C": "Hydrogen", "D": "Helium"}, "answer": "C"}
]

@app.route('/')
def quiz():
    # Passing the enumerated questions to the template
    enumerated_questions = list(enumerate(questions))
    return render_template('quiz.html', enumerated_questions=enumerated_questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    user_answers = []
    correct_answers = []

    for i, question in enumerate(questions):
        user_answer = request.form.get(f"question-{i}")
        correct_answer = question["answer"]
        user_answers.append(user_answer)
        correct_answers.append(correct_answer)
        if user_answer == correct_answer:
            score += 1

    return render_template('result.html', score=score, total=len(questions), user_answers=user_answers, correct_answers=correct_answers, enumerated_questions=list(enumerate(questions)))

if __name__ == '__main__':
    app.run(debug=True)
