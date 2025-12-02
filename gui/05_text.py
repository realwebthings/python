import tkinter as tk
from tkinter import scrolledtext

# Text widget - multi-line text input/display area
root = tk.Tk()
root.title("Text Widget")
root.geometry("500x400")

def get_text():
    content = text_area.get("1.0", tk.END)
    print("Text content:", content)

def clear_text():
    text_area.delete("1.0", tk.END)

def insert_sample():
    sample_text = "This is sample text.\nIt has multiple lines.\nYou can edit this!"
    text_area.insert(tk.END, sample_text)

# Create text widget with scrollbar
tk.Label(root, text="Multi-line Text Area:", font=("Arial", 12)).pack(pady=5)

text_area = scrolledtext.ScrolledText(root,
                                     width=50,
                                     height=15,
                                     font=("Arial", 11),
                                     bg="white",
                                     fg="black",
                                     wrap=tk.WORD)
text_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Get Text", command=get_text, bg="lightblue").pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Clear", command=clear_text, bg="lightcoral").pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Insert Sample", command=insert_sample, bg="lightgreen").pack(side=tk.LEFT, padx=5)

root.mainloop()