from flask_sqlalchemy import SQLAlchemy
from . import db 
from werkzeug.security import generate_password_hash, check_password_hash




# Users Table
class User(db.Model):
    __tablename__ = 'users'
    user_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    second_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)  # Store hashed password

    # Hash password before saving
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Check password validity
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



# Badges Table
class Badge(db.Model):
    __tablename__ = 'badges'
    badge_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_ID = db.Column(db.Integer, db.ForeignKey('users.user_ID'), nullable=False)
    badge_name = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    number_of_attempts = db.Column(db.Integer, default=0)
    progress = db.Column(db.Float, nullable=False)

# Game Stages Table
class GameStage(db.Model):
    __tablename__ = 'game_stages'
    stage_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_ID = db.Column(db.Integer, db.ForeignKey('users.user_ID'), nullable=False)
    stage_name = db.Column(db.Enum('Preconception', 'Antenatal', 'Birth', 'Postnatal'), nullable=False)
    number_of_attempts = db.Column(db.Integer, default=0)
    overall_score = db.Column(db.Integer, nullable=False)

# AI Responses Table
class AIResponse(db.Model):
    __tablename__ = 'ai_responses'
    response_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_ID = db.Column(db.Integer, db.ForeignKey('users.user_ID'), nullable=False)
    scenario_ID = db.Column(db.Integer, nullable=False)
    IS_correct = db.Column(db.Boolean, nullable=False)
    attempt_number = db.Column(db.Integer, nullable=False)
