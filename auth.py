import tkinter as tk
import bcrypt
from UI.screen2 import open_second_screen
from database.banco import verify_user, save_user, check_username_exists
import session

# Create the main window
janela = tk.Tk()
janela.title("Login/Signup")
janela.geometry("300x250")

# Center the window on the screen
window_width = 300
window_height = 250
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
janela.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Labels
label_username = tk.Label(janela, text="Username:")
label_username.grid(row=0, column=0, sticky=tk.E)

label_password = tk.Label(janela, text="Password:")
label_password.grid(row=1, column=0, sticky=tk.E)

# Entry fields
entry_username = tk.Entry(janela)
entry_username.grid(row=0, column=1)

entry_password = tk.Entry(janela, show="*")
entry_password.grid(row=1, column=1)

# Signup button
def handle_signup():
    username = entry_username.get()
    password = entry_password.get()

    if check_username_exists(username):
        signup_message.config(text="Username already exists. Please choose a different username.")
    else:
        save_user(username, bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))
        signup_message.config(text="Signup successful!")

signup_button = tk.Button(janela, text="Signup", command=handle_signup)
signup_button.grid(row=2, column=0, columnspan=2, pady=10)

# Login button
def handle_login():
    username = entry_username.get()
    password = entry_password.get()

    if verify_user(username, password):
        login_message.config(text="Login successful!")
        session.set_current_user(username)  # Set the current user
        janela.withdraw()  # Hide the main window
        open_second_screen(username)  # Open the second screen
    else:
        login_message.config(text="Invalid username or password.")

login_button = tk.Button(janela, text="Login", command=handle_login)
login_button.grid(row=3, column=0, columnspan=2)

# Signup and login messages
signup_message = tk.Label(janela, text="")
signup_message.grid(row=4, column=0, columnspan=2)

login_message = tk.Label(janela, text="")
login_message.grid(row=5, column=0, columnspan=2)

# Run the main loop
janela.mainloop()
