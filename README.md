# Password Strength Checker

A web app built with HTML, JavaScript, and Python (Flask) that checks password strength in real time.

## Features

- Live strength meter (Weak / Fair / Strong / Very Strong)
- Detects common weak patterns (`password`, `123456`, `qwerty`, etc.)
- Suggests a cryptographically secure strong password
- Displays SHA-256 hash of the entered password
- One-click copy for suggested passwords

## Deploy to Vercel

1. Push this repo to GitHub
2. Go to [vercel.com](https://vercel.com) → New Project → Import your repo
3. Vercel auto-detects the config — just click **Deploy**

## Run Locally

```bash
# Clone the repo
git clone https://github.com/chhinhlongdev/password-checker.git
cd password-checker

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python -c "from api.index import app; app.run(debug=True)"
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Tech Stack

- Python / Flask
- HTML + CSS + Vanilla JS
- `hashlib` for SHA-256 hashing
- `secrets` for secure password generation
