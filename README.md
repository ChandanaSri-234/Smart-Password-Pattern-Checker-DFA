
# 🔐 Smart Password Pattern Checker Using DFA

## 🌐 Live Demo

**Try the application here:**

https://smart-password-pattern-checker-dfa.onrender.com

## 📌 Project Overview

Smart Password Pattern Checker Using DFA is a web-based password validation system developed using Python and Flask.

It uses Deterministic Finite Automata (DFA) concepts to analyze passwords against multiple security requirements and classify them as valid or invalid.

The application also displays DFA state transitions diagrammatically and identifies violated password rules.

## 🎯 Objectives

- Validate minimum password length.
- Check uppercase and lowercase characters.
- Identify numerical digits.
- Verify special characters.
- Detect prohibited password patterns.
- Display DFA state transitions.
- Classify passwords as valid or invalid.
- Identify the rules violated by an invalid password.

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- DFA (Automata Theory)
- Gunicorn
- Render (Cloud Deployment)

## ⚙️ Features

1. Smart Password Validation
2. Multiple Security Rule Checking
3. Prohibited Pattern Detection
4. Graphical DFA State Transition Diagram
5. Character-by-Character Transition Details
6. Valid and Invalid Password Classification
7. Responsive Web Interface

## 📂 Project Structure

Smart-Password-Pattern-Checker-DFA/
│
├── screenshots/
│   ├── homepage.png
│   ├── validpassword1.png
│   ├── Invalidpassword.png
│   ├── DFA_Diagram.png
│   └── state_transition.png
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── dfa.py
├── main.py
├── password_rules.py
├── requirements.txt
└── README.md

## 📸 Application Screenshots

### Homepage
screenshots/Home_Page.png

### Valid Password


### Invalid Password
![Invalid Password](screenshots/Invalidpassword.png)

### DFA Diagram
![DFA Diagram](screenshots/DFA_Diagram.png)

### State Transition Details
![State Transitions](screenshots/state_transition.png)

## 🧪 Sample Test Cases

| Test Case | Password | Expected Result |
|---|---|---|
| TC01 | Hello@123 | Valid |
| TC02 | hello123 | Invalid |
| TC03 | HELLO@123 | Invalid |
| TC04 | Abc@12 | Invalid |
| TC05 | Pass@123456 | Invalid |
| TC06 | Welcome#2026 | Valid |
| TC07 | Abcdefg@ | Invalid |
| TC08 | Abcdef12 | Invalid |

## 🚀 Installation and Execution

### 1. Clone the repository

git clone https://github.com/ChandanaSri-234/Smart-Password-Pattern-Checker-DFA.git

### 2. Navigate to the project folder

cd Smart-Password-Pattern-Checker-DFA

### 3. Create a virtual environment

python -m venv .venv

### 4. Activate the environment

Windows:

.venv\Scripts\activate

### 5. Install dependencies

pip install -r requirements.txt

### 6. Run the application

python main.py

### 7. Open in browser

http://127.0.0.1:5000

## ☁️ Deployment

The application is deployed using Render.

Live Application:
https://smart-password-pattern-checker-dfa.onrender.com

## 🎓 Academic Project

**Project Title:** Smart Password Pattern Checker Using DFA

**Domain:** Theory of Computation / Automata Theory

**Implementation:** Python and Flask

## 👩‍💻 Author

Developed as an academic case study project.

