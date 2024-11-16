# Quiz Application – Multiple-Choice Questions

![Quiz Application](https://img.shields.io/badge/Quiz%20Application-Python%20%7C%20Flask%20%7C%20Interactive-brightgreen)

## Overview

This repository contains two implementations of a quiz application:  
1. **Command-line Quiz Application**: A Python-based interactive multiple-choice quiz for the terminal.  
2. **Web-based Quiz Application**: A Flask-powered web application that delivers a similar quiz experience through a browser.  

The quiz includes 15 questions spanning general knowledge topics, providing feedback for each answer and a final score summary.  

---

## Features

### Command-line Quiz Application:
- Text-based user interface for simple interaction.  
- Displays questions and options sequentially.  
- Validates user input to accept only valid choices (A, B, C, or D).  
- Shows feedback for each question, including the correct answer and the user's choice.  
- Summarizes the total score at the end of the quiz.  

### Web-based Quiz Application:
- Modern interface with HTML templates for easy accessibility.  
- Dynamic feedback through POST requests for form submissions.  
- Final results are displayed on a separate results page with detailed answer breakdown.  
- Score calculation and user feedback on performance.  

---

## Prerequisites

### For Command-line Quiz:
- Python 3.x installed on your system.  

### For Web-based Quiz:
- Python 3.x  
- Flask library (`pip install flask`)  
- Basic knowledge of running Flask applications.  

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/quiz-application.git
   cd quiz-application

2. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows

3. Install dependencies for the Flask app:

   ```bash
   Copy code
   pip install flask
   
---

## Usage

1. Run the script:
  ```bash
   python quiz_cli.py
  ```
2. Follow the on-screen instructions to answer questions by typing A, B, C, or D. 
3. Review the feedback provided after each question and check your final score at the end.

---

## Web-based Quiz:

1. Start the Flask server:
  ```bash
    python quiz_flask.py
  ```
2. Open your browser and navigate to http://127.0.0.1:5000/.
3. Answer the questions on the displayed form and click "Submit" to view your score and answer breakdown.

---

## File Structure
```bash
quiz-application/
│
├── quiz_cli.py           # Command-line quiz implementation
├── quiz_flask.py         # Web-based quiz using Flask
├── templates/
│   ├── quiz.html         # HTML template for displaying questions
│   └── result.html       # HTML template for showing quiz results
├── static/               # Optional: Store CSS/JS files if needed for Flask app
├── README.md             # Project documentation
└── requirements.txt      # Dependencies for the Flask app
```

---

## Templates Details

### **quiz.html**:
- Displays all questions in a form.  
- Uses radio buttons for options.  
- Submits answers to the `/submit` endpoint.  

### **result.html**:
- Displays the score and the correct answers vs. user's answers.  
- Highlights correct and incorrect responses.  

---

## Dependencies

Install the required Python packages using:  
```bash
pip install -r requirements.txt
```

---

## Libraries Used:

Flask: For building the web-based application.

---

## Customization

### Adding/Editing Questions:
- In the command-line quiz, edit the `get_questions` function in `quiz_cli.py`.  
- In the Flask app, update the `questions` list in `quiz_flask.py`.  

### Styling the Web App:
- Add CSS files in the `static/` folder.  
- Modify HTML in the `templates/` folder.  

---

## License

This project is open-source under the MIT License. Contributions are welcome!  
