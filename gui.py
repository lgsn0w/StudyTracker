import tkinter as tk
from tkinter import messagebox

from app.database import signup, login, create_connection

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Study Tracker")
        self.root.geometry("400x300")

        # Create labels and entry fields
        self.label_username = tk.Label(self.root, text="Username:", font=("Helvetica", 12))
        self.entry_username = tk.Entry(self.root, font=("Helvetica", 12))

        self.label_password = tk.Label(self.root, text="Password:", font=("Helvetica", 12))
        self.entry_password = tk.Entry(self.root, show="*", font=("Helvetica", 12))

        # Create buttons
        self.button_signup = tk.Button(self.root, text="Sign Up", command=self.signup, font=("Helvetica", 12))
        self.button_login = tk.Button(self.root, text="Login", command=self.login, font=("Helvetica", 12))

        # Position the widgets using grid layout
        self.label_username.grid(row=0, column=0, padx=10, pady=10)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)
        self.label_password.grid(row=1, column=0, padx=10, pady=10)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)
        self.button_signup.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.button_login.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def signup(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        # Perform signup logic
        signup(conn, username, password)
        messagebox.showinfo("Sign Up", "You have successfully signed up!")

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        # Perform login logic
        login(conn, username, password)

    def run(self):
        self.root.mainloop()


# Create a database connection
conn = create_connection('users.db')

# Create an instance of the GUI class
gui = GUI()
gui.run()
