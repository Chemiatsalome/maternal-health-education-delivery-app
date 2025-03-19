from flask import Blueprint, jsonify
from chatbot.modelintergration import get_chatbot_response_preconception , get_chatbot_response_birth, get_chatbot_response_postnatal, get_chatbot_response_prenatal  # Import the function that generates the quiz

quiz_bp = Blueprint("quiz", __name__)

@quiz_bp.route("/get_quiz_preconception", methods=["GET"])
def get_quiz_preconception():
    """API Endpoint to fetch AI-generated quiz"""
    quiz = get_chatbot_response_preconception()
    return jsonify(quiz)

@quiz_bp.route("/get_quiz_prenatal", methods=["GET"])
def get_quiz_prenatal():
    """API Endpoint to fetch AI-generated quiz"""
    quiz = get_chatbot_response_prenatal()
    return jsonify(quiz)

@quiz_bp.route("/get_quiz_birth", methods=["GET"])
def get_quiz_birth():
    """API Endpoint to fetch AI-generated quiz"""
    quiz = get_chatbot_response_birth()
    return jsonify(quiz)

@quiz_bp.route("/get_quiz_postnatal", methods=["GET"])
def get_quiz_postanatal():
    """API Endpoint to fetch AI-generated quiz"""
    quiz = get_chatbot_response_postnatal()
    return jsonify(quiz)