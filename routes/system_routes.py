from flask import Blueprint, render_template, request, redirect, url_for, session,flash,  jsonify
from chatbot.chatbot import get_chatbot_response  # Import the chatbot function
# from models.user import User
# from app import db

home_bp = Blueprint("home", __name__)
gamestages_bp = Blueprint("gamestages", __name__)


@home_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':  # Chatbot logic
        data = request.get_json()
        user_message = data.get('message', '')

        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        bot_response = get_chatbot_response(user_message)
        return jsonify({"response": bot_response})

    return render_template('index.html')  # Normal page load

@gamestages_bp.route('/gamestages')
def game():
    if 'user_ID' in session:
        # User is logged in, show personalized experience
        return render_template('gamestages.html', user_logged_in=True)
    else:
        # Guest user, show limited features and a login prompt
        flash('Login for a personalized experience.', 'info')
        return render_template('gamestages.html', user_logged_in=False)
 

