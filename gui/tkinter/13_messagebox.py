import tkinter as tk
from tkinter import messagebox

# Messagebox - dialog boxes for user interaction
root = tk.Tk()
root.title("Messagebox Examples")
root.geometry("400x300")

def show_info():
    messagebox.showinfo("Information", "This is an info message!")

def show_warning():
    messagebox.showwarning("Warning", "This is a warning message!")

def show_error():
    messagebox.showerror("Error", "This is an error message!")

def ask_question():
    result = messagebox.askquestion("Question", "Do you like Python?")
    label.config(text=f"Answer: {result}")

def ask_yes_no():
    result = messagebox.askyesno("Yes/No", "Continue with operation?")
    label.config(text=f"Result: {result}")

def ask_ok_cancel():
    result = messagebox.askokcancel("OK/Cancel", "Save changes?")
    label.config(text=f"Result: {result}")

def ask_retry_cancel():
    result = messagebox.askretrycancel("Retry/Cancel", "Operation failed. Retry?")
    label.config(text=f"Result: {result}")

# Create buttons
tk.Label(root, text="Messagebox Examples", font=("Arial", 14, "bold")).pack(pady=10)

tk.Button(root, text="Show Info", command=show_info, width=15).pack(pady=5)
tk.Button(root, text="Show Warning", command=show_warning, width=15).pack(pady=5)
tk.Button(root, text="Show Error", command=show_error, width=15).pack(pady=5)
tk.Button(root, text="Ask Question", command=ask_question, width=15).pack(pady=5)
tk.Button(root, text="Ask Yes/No", command=ask_yes_no, width=15).pack(pady=5)
tk.Button(root, text="Ask OK/Cancel", command=ask_ok_cancel, width=15).pack(pady=5)
tk.Button(root, text="Ask Retry/Cancel", command=ask_retry_cancel, width=15).pack(pady=5)

label = tk.Label(root, text="Click buttons to see messageboxes", font=("Arial", 10), fg="blue")
label.pack(pady=10)

root.mainloop()