from flask import Blueprint, render_template, request, jsonify
from .openai_service import ask_ai, summarize_email

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/ask', methods=['POST'])
def ask():
    question = request.form.get('question')
    answer = ask_ai(question)
    return jsonify({'response': answer})

@main.route('/summarize', methods=['POST'])
def summarize():
    email_text = request.form.get('email')
    summary = summarize_email(email_text)
    return jsonify({'response': summary})