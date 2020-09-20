import sqlite3
#from werkzeug.security import generate_password_hash

banco = sqlite3.connect('bancodados.db')
cursor = banco.cursor()

#senha = generate_password_hash('admin', method='sha256')
#cursor.execute("CREATE TABLE users (username text,id integer primary key,email text, password text)")
#cursor.execute("INSERT INTO users(username, password, email) VALUES('JND','JND','JND@email.com')")
#cursor.execute("INSERT INTO users(username, password, email) VALUES('admin','admin','admin@email.com')")
banco.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

cursor.close()