import customtkinter as ctk
import subprocess
import time
from datetime import datetime


ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()
# app.attributes("-fullscreen", True)
app.geometry("600x300")
app.title("Test02")

class ScriptRunner:
    def __init__(self):
        self.process = None
        self.start_time = None

    def start_script(self):
        # script_path = "path/to/your/script.py"  # Replace with the actual path to your script
        self.start_time = time.time()
        # self.process = subprocess.Popen(["python", script_path])
        self.process = True # !
        btn.configure(text="Stop")
        btn.configure(state="normal", command=script_runner.stop_script, fg_color="red", hover_color="dark red")
        self.update_timer()

    def stop_script(self):
        if self.process:
            # self.process.terminate()
            self.process = None
            elapsed_time = round(time.time() - self.start_time, 2)
            print("Script stopped. Elapsed time:", elapsed_time, "seconds")
            btn.configure(text="Start", state="normal", command=script_runner.start_script, fg_color="green", hover_color="dark green")

    def update_timer(self):
        if self.process:
            elapsed_time = time.time() - self.start_time
            timer_label.configure(text=datetime.fromtimestamp(elapsed_time).strftime('%M:%S'))
            app.after(100, self.update_timer)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

script_runner = ScriptRunner()

timer_label = ctk.CTkLabel(frame, text="00:00", justify=ctk.CENTER, height=100, font=ctk.CTkFont(size=50, weight="bold"))
timer_label.pack(pady=10, padx=10)

btn = ctk.CTkButton(frame, text="Start", command=script_runner.start_script, compound="bottom", fg_color="green", hover_color="dark green")
btn.pack(pady=10, padx=10)

app.mainloop()
