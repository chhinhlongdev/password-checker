from flask import Flask, render_template, request, jsonify
import hashlib
import re
import secrets
import string

app = Flask(__name__, template_folder='../templates', static_folder='../static')

def check_strength(password):
    score = 0
    issues = []
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        issues.append("Too short (min 8 characters)")
        suggestions.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        issues.append("No uppercase letters")
        suggestions.append("Add uppercase letters (A-Z)")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        issues.append("No lowercase letters")
        suggestions.append("Add lowercase letters (a-z)")

    if re.search(r'\d', password):
        score += 1
    else:
        issues.append("No numbers")
        suggestions.append("Add numbers (0-9)")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        issues.append("No special characters")
        suggestions.append("Add special characters (!@#$%...)")

    weak_patterns = ['password', '123456', 'qwerty', 'abc123', 'letmein', 'admin', '111111']
    if any(p in password.lower() for p in weak_patterns):
        score = max(0, score - 2)
        issues.append("Contains a common weak pattern")
        suggestions.append("Avoid common words like 'password', '123456', etc.")

    if score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Fair"
    elif score <= 5:
        label = "Strong"
    else:
        label = "Very Strong"

    return {"score": score, "max": 6, "label": label, "issues": issues, "suggestions": suggestions}


def generate_strong_password(length=16):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()"
    while True:
        pwd = ''.join(secrets.choice(alphabet) for _ in range(length))
        if check_strength(pwd)["label"] in ("Strong", "Very Strong"):
            return pwd


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    password = data.get('password', '')
    result = check_strength(password)
    result['hash'] = hash_password(password)
    result['suggestion'] = generate_strong_password()
    return jsonify(result)
