from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db  # Import db from models/__init__.py
from models.models import User, Badge, GameStage, AIResponse  # Import models

app = Flask(__name__)

app.config.from_object('config.Config')

db.init_app(app)
migrate = Migrate(app, db)


# Import models to register them
with app.app_context():
    from models.models import *


from routes.auth_routes import Login_bp, signup_bp
from routes.system_routes import home_bp, gamestages_bp
from routes.gamestage_routes import preconceptionstage_bp, prenatalstage_bp , birthstage_bp , postnatalstage_bp
# Register Blueprints (modular routes)
app.register_blueprint(Login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(home_bp)
app.register_blueprint(gamestages_bp)
app.register_blueprint(preconceptionstage_bp)
app.register_blueprint(prenatalstage_bp)
app.register_blueprint(birthstage_bp )
app.register_blueprint(postnatalstage_bp)



if __name__ == '__main__':
    app.run(debug=True)
