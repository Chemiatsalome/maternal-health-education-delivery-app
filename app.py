from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/preconception')
def preconception():
    return render_template('preconception.html')

@app.route('/prenatal')
def prenatal():
    return render_template('prenatal.html')

@app.route('/birth')
def birth():
    return render_template('birth.html')

@app.route('/postnatal')
def postnatal():
    return render_template('postnatal.html')


if __name__ == '__main__':
    app.run(debug=True)
