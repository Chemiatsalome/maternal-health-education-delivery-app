from flask import Blueprint, render_template, request, redirect, url_for, session,flash

# from models.user import User
# from app import db

preconceptionstage_bp = Blueprint("preconception", __name__)
prenatalstage_bp = Blueprint("prenatal", __name__)
birthstage_bp = Blueprint("birth", __name__)
postnatalstage_bp = Blueprint("postnatal", __name__)


@preconceptionstage_bp.route('/preconception')
def preconception():
    if 'user_ID' in session:
        # User is logged in, show personalized experience
        return render_template('preconception.html', user_logged_in=True)
    else:
        # Guest user, show limited features and a login prompt
        flash('Login for a personalized experience.', 'info')
        return render_template('preconception.html', user_logged_in=False)
    
    

@prenatalstage_bp.route('/prenatal')
def prenatal():
    if 'user_ID' in session:
        # User is logged in, show personalized experience
        return render_template('prenatal.html', user_logged_in=True)
    else:
        # Guest user, show limited features and a login prompt
        flash('Login for a personalized experience.', 'info')
        return render_template('prenatal.html', user_logged_in=False)
    
   

@birthstage_bp.route('/birth')
def birth():
    if 'user_ID' in session:
        # User is logged in, show personalized experience
        return render_template('birth.html', user_logged_in=True)
    else:
        # Guest user, show limited features and a login prompt
        flash('Login for a personalized experience.', 'info')
        return render_template('birth.html', user_logged_in=False)

@postnatalstage_bp.route('/postnatal')
def postnatal():
    if 'user_ID' in session:
        # User is logged in, show personalized experience
        return render_template('postnatal.html', user_logged_in=True)
    else:
        # Guest user, show limited features and a login prompt
        flash('Login for a personalized experience.', 'info')
        return render_template('postnatal.html', user_logged_in=False)