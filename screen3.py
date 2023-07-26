import tkinter as tk
import time
import session
import datetime

def open_time_tracking_screen():
    # Create the time tracking screen window as a Toplevel window
    janela_time_tracking = tk.Toplevel()
    janela_time_tracking.title("Time Tracking")
    janela_time_tracking.geometry("400x300")

    # Center the time tracking screen window on the screen
    window_width = 400
    window_height = 300
    screen_width = janela_time_tracking.winfo_screenwidth()
    screen_height = janela_time_tracking.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    janela_time_tracking.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Start tracking button
    def start_tracking():
        start_time = time.time()
        session.set_start_time(start_time)

    start_button = tk.Button(janela_time_tracking, text="Start Tracking", command=start_tracking)
    start_button.pack()

    # Stop tracking button
    def stop_tracking():
        start_time = session.get_start_time()
        if start_time is not None:
            current_time = time.time()
            elapsed_time = current_time - start_time
            hours = int(elapsed_time / 3600)
            minutes = int((elapsed_time % 3600) / 60)
            seconds = int((elapsed_time % 3600) % 60)
            time_message = f"Elapsed Time: {hours:02d}:{minutes:02d}:{seconds:02d}"
            elapsed_time_label.config(text=time_message)
            session.clear_start_time()

    stop_button = tk.Button(janela_time_tracking, text="Stop Tracking", command=stop_tracking)
    stop_button.pack()

    # Elapsed time label
    elapsed_time_label = tk.Label(janela_time_tracking, text="Elapsed Time: 00:00:00")
    elapsed_time_label.pack()

    # Run the main loop for the time tracking screen
    janela_time_tracking.mainloop()
