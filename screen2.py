import tkinter as tk
import session
from screen3 import open_time_tracking_screen


def open_second_screen(username):
    # Create the second screen window as a Toplevel window
    janela_second_screen = tk.Toplevel()
    janela_second_screen.title("Second Screen")
    janela_second_screen.geometry("400x300")

    # Retrieve the current user
    current_user = session.get_current_user()

    # Center the second screen window on the screen
    window_width = 400
    window_height = 300
    screen_width = janela_second_screen.winfo_screenwidth()
    screen_height = janela_second_screen.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    janela_second_screen.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Welcome message
    welcome_message = tk.Label(janela_second_screen, text=f"Welcome, {username}!")
    welcome_message.pack()

    # Time Tracking button
    def open_time_tracking():
        janela_second_screen.withdraw()  # Hide the current screen
        open_time_tracking_screen()

    time_tracking_button = tk.Button(janela_second_screen, text="Time Tracking", command=open_time_tracking)
    time_tracking_button.pack()

    # Add other elements or functionality to the second screen as needed

    # Run the main loop for the second screen
    janela_second_screen.mainloop()


    # Time Tracking button
    def open_time_tracking():
        janela_second_screen.withdraw()  # Hide the current screen
        open_time_tracking_screen()

    time_tracking_button = tk.Button(janela_second_screen, text="Time Tracking", command=open_time_tracking)
    time_tracking_button.pack()

    # Add other elements or functionality to the second screen as needed

    # Run the main loop for the second screen
    janela_second_screen.mainloop()
