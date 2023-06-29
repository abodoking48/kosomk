from flask import Flask, redirect, render_template, request, flash
# from flask import blueprint
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
db = SQL('sqlite:///home.db')
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["DEBUG"] = True



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
    if not name or not email or not pass1:
        flash('error')
        return render_template('register.html')
    if pass1 != pass2:
        flash('error')
        return render_template('register.html')

    users = db.execute(
        "SELECT * FROM users WHERE email LIKE ?;", email)
    if len(users) == 1:
        flash('email already register')
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
        flash('wrong details')
        return render_template('login.html', message='no1' )
    user = db.execute("SELECT * FROM users WHERE email LIKE ?;", email)
    if len(user) != 1 or not check_password_hash(user[0]['password_hash'], password):
        flash('wrong details')
        return render_template('login.html' , message='')
    
    Session['user_id'] = user[0]['id']
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)