import time
import tkinter as tk
from tkinter import ttk, messagebox
from tqdm import tqdm
import threading

# Function to simulate reading text with a progress bar animation
def read_text_with_animation(text, delay):
    # Disable the start button while the animation is running
    start_button.config(state=tk.DISABLED)
    
    progress_label['text'] = "Reading..."
    
    for i in tqdm(range(len(text)), desc="Progress", ncols=100, ascii=True, colour="green"):
        time.sleep(delay)
    
    progress_label['text'] = "Finished reading!"

    # Re-enable the start button after finishing
    start_button.config(state=tk.NORMAL)

# Function to start the animation in a separate thread
def start_animation():
    text = text_input.get("1.0", tk.END).strip()
    try:
        delay = float(speed_input.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for speed.")
        return

    if not text:
        messagebox.showerror("No Text", "Please enter some text to read.")
        return

    # Start animation in a separate thread to avoid freezing the GUI
    threading.Thread(target=read_text_with_animation, args=(text, delay), daemon=True).start()

# Create the main window
root = tk.Tk()
root.title("Text Reader with Animation")
root.geometry("400x300")

# Text input label and box
text_label = tk.Label(root, text="Enter Text to Read:")
text_label.pack(pady=5)

text_input = tk.Text(root, height=5, width=40)
text_input.pack(pady=5)

# Speed input label and box
speed_label = tk.Label(root, text="Enter Speed (seconds per character):")
speed_label.pack(pady=5)

speed_input = ttk.Entry(root)
speed_input.pack(pady=5)

# Progress label
progress_label = tk.Label(root, text="")
progress_label.pack(pady=5)

# Start button
start_button = ttk.Button(root, text="Start Reading", command=start_animation)
start_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
