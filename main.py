import tkinter as tk
import sqlite3
import bcrypt
import os


# Create the 'data' folder (not working properly, supposed to make a dir inside the StudyTracker folder, not inside app)
data_folder = os.path.join(os.path.dirname(__file__), 'data')

# make a file called database.db inside the 'data' folder
if not os.path.exists(data_folder):
    os.mkdir(data_folder)

# Create the path to the users.db file inside the 'data' folder
db_path = os.path.join(data_folder, 'users.db')

# creating the window
root = tk.Tk()
root.title("Login")

# create database and connect it to the data folder
conn = sqlite3.connect(db_path)
c = conn.cursor()

# create the tables: for username:string and password:string
c.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,
             username TEXT NOT NULL, password TEXT NOT NULL)""")


# creating the signup function
def signup():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    password2 = input("Enter your password again: ")
    if password == password2:
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
        conn.commit()
        print("You have successfully signed up!")
    else:
        print("The passwords do not match! Try again.")


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    c.execute("SELECT username, password FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    if user is not None:
        if bcrypt.checkpw(password.encode('utf-8'), user[1]):
            print("You have successfully logged in!")
        else:
            print("The password is incorrect! Try again.")
    else:
        print("The username is incorrect! Try again.")

signup()
login()
