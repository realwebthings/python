import tkinter as tk

# Entry widget - single-line text input field
root = tk.Tk()
root.title("Entry Widget")
root.geometry("400x300")

def submit_text():
    text = entry.get()
    result_label.config(text=f"You entered: {text}")
    entry.delete(0, tk.END)  # Clear the entry

def clear_text():
    entry.delete(0, tk.END)
    result_label.config(text="")

# Create entry widget
tk.Label(root, text="Enter your name:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root,
                font=("Arial", 14),
                width=20,
                bg="white",
                fg="black",
                bd=2)
entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

submit_btn = tk.Button(button_frame, text="Submit", command=submit_text, bg="lightgreen")
clear_btn = tk.Button(button_frame, text="Clear", command=clear_text, bg="lightcoral")

submit_btn.pack(side=tk.LEFT, padx=5)
clear_btn.pack(side=tk.LEFT, padx=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=20)

# Focus on entry when window opens
entry.focus()

root.mainloop()