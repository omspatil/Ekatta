# Quiz Application – Multiple-Choice Questions

def display_instructions():
    """Display instructions for the quiz."""
    print("Welcome to the Quiz!")
    print("You will be presented with 15 multiple-choice questions.")
    print("Type the letter corresponding to your chosen answer (A, B, C, or D).")
    print("The correct answer will be shown after each question.")
    print("Good luck!\n")

def get_questions():
    """Define questions, options, and answers."""
    return [
        {"question": "What is the capital of France?",
         "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
         "answer": "C"},
        {"question": "Which planet is known as the Red Planet?",
         "options": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
         "answer": "B"},
        {"question": "Who wrote 'Romeo and Juliet'?",
         "options": ["A) Charles Dickens", "B) J.K. Rowling", "C) William Shakespeare", "D) Mark Twain"],
         "answer": "C"},
        {"question": "What is the largest mammal in the world?",
         "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Polar Bear"],
         "answer": "B"},
        {"question": "What is the square root of 64?",
         "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
         "answer": "C"},
        {"question": "Who discovered gravity?",
         "options": ["A) Albert Einstein", "B) Isaac Newton", "C) Galileo Galilei", "D) Nikola Tesla"],
         "answer": "B"},
        {"question": "What is the capital city of Japan?",
         "options": ["A) Tokyo", "B) Kyoto", "C) Osaka", "D) Nagoya"],
         "answer": "A"},
        {"question": "Which element has the chemical symbol O?",
         "options": ["A) Gold", "B) Oxygen", "C) Hydrogen", "D) Iron"],
         "answer": "B"},
        {"question": "Who painted the Mona Lisa?",
         "options": ["A) Michelangelo", "B) Vincent van Gogh", "C) Pablo Picasso", "D) Leonardo da Vinci"],
         "answer": "D"},
        {"question": "What is the largest desert in the world?",
         "options": ["A) Sahara", "B) Gobi", "C) Antarctic Desert", "D) Kalahari"],
         "answer": "C"},
        {"question": "How many continents are there?",
         "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
         "answer": "C"},
        {"question": "What is the chemical symbol for water?",
         "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
         "answer": "A"},
        {"question": "Who was the first President of the United States?",
         "options": ["A) George Washington", "B) Abraham Lincoln", "C) Thomas Jefferson", "D) John Adams"],
         "answer": "A"},
        {"question": "What is the smallest prime number?",
         "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
         "answer": "C"},
        {"question": "What is the freezing point of water in Celsius?",
         "options": ["A) 0", "B) 32", "C) 100", "D) -10"],
         "answer": "A"}
    ]

def quiz():
    """Conduct the quiz."""
    questions = get_questions()
    score = 0
    
    for idx, q in enumerate(questions, start=1):
        print(f"Question {idx}: {q['question']}")
        for option in q['options']:
            print(option)
        
        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
        while user_answer not in ['A', 'B', 'C', 'D']:
            print("Invalid input. Please enter A, B, C, or D.")
            user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
        
        correct_answer_text = q['options'][ord(q['answer']) - ord('A')]
        user_answer_text = q['options'][ord(user_answer) - ord('A')] if user_answer in ['A', 'B', 'C', 'D'] else "Invalid Answer"
        
        if user_answer == q['answer']:
            print("Correct!")
        else:
            print("Wrong.")
        
        print(f"User's Answer: {user_answer_text}")
        print(f"Correct Answer: {correct_answer_text}\n")
        
        if user_answer == q['answer']:
            score += 1
    
    print(f"Quiz complete! Your final score is {score}/{len(questions)}.")
    if score == len(questions):
        print("Excellent work! You got a perfect score!")
    elif score >= len(questions) * 0.7:
        print("Great job! You passed!")
    else:
        print("Keep practicing! You'll do better next time!")

if __name__ == "__main__":
    display_instructions()
    quiz()
