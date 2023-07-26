import sqlite3
import bcrypt
import os

# Get the absolute path of the directory containing this script
dir_atual = os.path.dirname(os.path.abspath(__file__))

# Database file path
db_file = os.path.join(dir_atual, 'info.db')

def create_table():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS usuarios (
              username TEXT NOT NULL,
              password TEXT NOT NULL)""")

    conn.commit()
    conn.close()

def check_username_exists(username):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute("SELECT COUNT(username) FROM usuarios WHERE username = ?", (username,))
    count = c.fetchone()[0]

    conn.close()

    return count > 0

def save_user(username, password):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute("INSERT INTO usuarios VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def verify_user(username, password):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute("SELECT password FROM usuarios WHERE username = ?", (username,))
    result = c.fetchone()

    conn.close()

    if result is not None:
        hashed_password = result[0]
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

    return False

create_table()  # Create the table if it doesn't exist