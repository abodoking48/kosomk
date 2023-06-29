from flask import Flask, Blueprint, redirect, render_template, request, flash, session
from flask_session import Session
from cs50 import SQL
from home import home_page_router
from werkzeug.security import check_password_hash, generate_password_hash
from password_strength import PasswordPolicy, PasswordStats
from sell import sell_router

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
# app.config['SECRET_KEY'] = 'secret'
Session(app)

db = SQL('sqlite:///home.db')
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["DEBUG"] = True
app.register_blueprint(home_page_router, url_perfix='')
app.register_blueprint(sell_router, url_perfix='')

policy = PasswordPolicy.from_names(
    length=8,  # min length: 8
    uppercase=1,  # need min. 2 uppercase letters
    numbers=1,  # need min. 2 digits
    strength=0.66  # need a password that scores at least 0.5 with its entropy bits
)
# session['user_id'] = None


@app.route('/')
def index():
    if not session.get('user_id', None):
        return render_template('index.html')
    return render_template('test.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    name = request.form.get('name')
    email = request.form.get('email')
    pass1 = request.form.get('pass1')
    pass2 = request.form.get('pass2')
    phone = request.form.get('phone')
    birth = request.form.get('birth')

    stats = PasswordStats(pass1)
    checkpolicy = policy.test(pass1)
    if stats.strength() < 0.20:
        print(stats.strength())
        #flash("Password not strong enough. Avoid consecutive characters and easily guessed words.")
        return render_template('register.html')

    if not name or not email or not pass1:
        # flash('error')
        return render_template('register.html')

    if pass1 != pass2:
        # flash('error')
        return render_template('register.html')

    users = db.execute(
        "SELECT * FROM users WHERE email = ?;", email)
    if len(users) == 1:
        #flash('email already register')
        return render_template('register.html')

    user_id = db.execute(
        "INSERT INTO users (username ,email, password_hash , phone , birth ) VALUES (?,?,?,?,?);",
        name,
        email,
        generate_password_hash(pass1),
        phone,
        birth)
    return redirect('/login')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        #flash('wrong details')
        return render_template('login.html', message='write email/password')

    user = db.execute("SELECT * FROM users WHERE email LIKE ?;", email)
    if len(user) != 1 or not check_password_hash(user[0]['password_hash'], password):
        #flash('wrong details')
        return render_template('login.html', message='email/password INCORRECT')

    session['user_id'] = user[0]['id']
    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@app.route('/rent')
def rent():
    return render_template('rent.html')


@app.route('/buy')
def buy():
    return render_template('/buy.html')

@app.route('/details')
def details():
    return render_template('/details.html')

@app.route('/contact us')
def contact():
    return render_template('/contact us.html')


if __name__ == "__main__":
    app.run(debug=True)
