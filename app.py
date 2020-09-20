from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'my precious'

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
        if request.form['username'] != 'JND' or request.form['password'] != 'JNDsenha':
            error = 'Dados invalidos, tente novamente.'
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
    defaultPassword = 'senha-doida'
    if request.method == 'POST':
        inputUsername = request.form.get('username', defaultUsername)
        inputPassword = request.form.get('password', defaultPassword)
        inputRepassword = request.form.get('repassword', defaultPassword)
        if inputRepassword != inputPassword:
            error = 'As senhas nao coincidem.'
        else: 
            flash('Cadastrado com sucesso!')
    
    return render_template('register.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)