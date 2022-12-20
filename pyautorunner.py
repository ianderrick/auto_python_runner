import os
import tkinter as tk
from tkinter import ttk

# Create the GUI window
root = tk.Tk()

# Create a progress bar that will be updated as the scripts are run
progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack()

# Function to run all the Python scripts in the directory
def run_scripts():
# Get a list of all the Python scripts in the current directory
    scripts = [f for f in os.listdir() if f.endswith(".py")]
    progress["maximum"] = len(scripts)

# Loop through the scripts and run them one by one
    for i, script in enumerate(scripts):
# Update the progress bar
        progress["value"] = i+1
        progress.update()

# Try to run the script and log any errors
        try:
            exec(open(script).read())
        except Exception as e:
            with open("error.log", "a") as log:
                log.write(f"Error running script {script}: {e}\n")

# Create a button to start running the scripts
button = tk.Button(root, text="Run Scripts", command=run_scripts)
button.pack()

# Start the GUI event loop
root.mainloop()
