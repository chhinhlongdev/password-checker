# Password Strength Checker

A web app built with HTML, JavaScript, and Python (Flask) that checks password strength in real time.

## Features

- Live strength meter (Weak / Fair / Strong / Very Strong)
- Detects common weak patterns (`password`, `123456`, `qwerty`, etc.)
- Suggests a cryptographically secure strong password
- Displays SHA-256 hash of the entered password
- One-click copy for suggested passwords

## Setup

```bash
# Clone the repo
git clone https://github.com/your-username/password-checker.git
cd password-checker

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Tech Stack

- Python / Flask
- HTML + CSS + Vanilla JS
- `hashlib` for SHA-256 hashing
- `secrets` for secure password generation
