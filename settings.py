import sqlite3

banco = sqlite3.connect('bancodados.db')
cursor = banco.cursor()

#cursor.execute("CREATE TABLE users (username text,id integer primary key,password text)")
#cursor.execute("INSERT INTO users(username, password) VALUES('JND','JNDsenha')")
#banco.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

cursor.close()