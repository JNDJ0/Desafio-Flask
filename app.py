from flask import Flask, render_template, redirect, url_for, request, session, flash
#from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from flask_sqlalchemy import sqlalchemy, SQLAlchemy
from sqlalchemy import create_engine
import sqlite3

db = SQLAlchemy()
app = Flask(__name__)
app.secret_key = 'jnd chave secreta'
app.config.update({
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///C:\\Users\\joaot\\Desktop\\Projeto\\bancodados.db',
    'SQLALCHEMY_POOL_SIZE': None,
    'SQLALCHEMY_POOL_TIMEOUT': None
})
db.init_app(app)

class users(db.Model):
    username = db.Column(db.String(100))
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Voce precisa estar logado para acessar essa pagina.')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    return render_template('index.html')  

@app.route('/welcome')
def welcome():
    return render_template('welcome.html') 

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        inputEmail = request.form.get('email')
        inputUsername = request.form.get('username')
        inputPassword = request.form.get('password')

        login = users.query.filter_by(email=inputEmail).first()
        if not login.password == inputPassword:
            error = 'Senha invalida, tente novamente.'
        else:
            session['logged_in'] = True
            flash('Voce logou na pagina!')
            return redirect(url_for('home'))
       
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('Voce saiu da pagina!')
    return redirect(url_for('welcome'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    defaultUsername = 'username-doido'
    defaulEmail = 'doido@email.com'
    defaultPassword = 'senha-doida'
    if request.method == 'POST':
        inputUsername = request.form.get('username', defaultUsername)
        inputEmail = request.form.get('email',defaulEmail)
        inputPassword = request.form.get('password', defaultPassword)
        inputRepassword = request.form.get('repassword', defaultPassword)

        usuario = users.query.filter_by(email=inputEmail).first()
        if usuario:
            error = 'Email ja cadastrado!'
            return render_template('register.html', error=error)
        if inputRepassword != inputPassword:
            error = 'As senhas nao coincidem.'
        else: 
            register = users(username = inputUsername, email = inputEmail, password = inputPassword)
            db.session.add(register)
            db.session.commit()
            flash('Cadastrado com sucesso!')
    
    return render_template('register.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)