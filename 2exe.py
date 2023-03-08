import os
import tkinter as tk
from tkinter import filedialog
import PyInstaller.__main__
import webbrowser
import tkinter.ttk as ttk
from tkinter import messagebox
import threading

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.title("Python2Exe By Btt")
        self.geometry("400x150")
        self.iconbitmap('btt.ico')
        # Create a file browser section
        self.file_path = tk.StringVar()
        self.file_path.set("Select a file...")
        self.file_label = tk.Label(self, textvariable=self.file_path)
        self.file_label.pack()
        self.browse_button = tk.Button(self, text="Browse...", command=self.browse_file)
        self.browse_button.pack()

        # Create a "Convert to exe" button and a progress bar
        self.convert_button = tk.Button(self, text="Convert to exe", command=self.convert_to_exe)
        self.convert_button.pack()
        self.progress_bar = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack()

        # Create a GitHub button
        github_button = tk.Button(self, text="GitHub", command=self.open_github)
        github_button.pack(side=tk.LEFT, padx=10, pady=10)
        btt_button = tk.Button(self, text="My Website", command=self.open_btt)
        btt_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def browse_file(self):
        # Open a file dialog to select a file
        file_selected = filedialog.askopenfilename()
        self.file_path.set(file_selected)

    def convert_to_exe(self):
        # Disable the convert button while the conversion process is running
        self.convert_button.config(state=tk.DISABLED)

        # Create a new thread to run the conversion process
        thread = threading.Thread(target=self.convert_to_exe_thread)
        thread.start()

    def convert_to_exe_thread(self):
        # Get the path of the selected file
        file_path = self.file_path.get()

        # Convert the Python project to an executable file using PyInstaller
        spec_file = os.path.join(os.path.dirname(file_path), "main.spec")
        PyInstaller.__main__.run([
            "--name=MyApp",
            "--onefile",
            file_path
        ])

        # Show an alert message after the conversion is completed
        self.show_alert("Conversion is completed.")

        # Enable the convert button
        self.convert_button.config(state=tk.NORMAL)

    def show_alert(self, message):
        # Show an alert message using the messagebox module
        messagebox.showinfo("Alert", message)

    def open_github(self):
        webbrowser.open('https://github.com/btt1996')

    def open_btt(self):
        webbrowser.open('https://btt1996.github.io')

if __name__ == "__main__":
    app = App()
    app.mainloop()
