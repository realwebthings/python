import tkinter as tk
from tkinter import colorchooser

# Color chooser - color selection dialog
root = tk.Tk()
root.title("Color Chooser Example")
root.geometry("400x300")

def choose_color():
    color = colorchooser.askcolor(title="Choose a color")
    if color[1]:  # color[1] is the hex value
        color_label.config(bg=color[1], text=f"Selected: {color[1]}")
        rgb_label.config(text=f"RGB: {color[0]}")
        root.config(bg=color[1])

def choose_background():
    color = colorchooser.askcolor(title="Choose background color")
    if color[1]:
        root.config(bg=color[1])
        bg_label.config(text=f"Background: {color[1]}")

def choose_text_color():
    color = colorchooser.askcolor(title="Choose text color")
    if color[1]:  # Check if a color was selected
        text_label.config(fg=color[1])
        text_color_label.config(text=f"Text color: {color[1]}")
        # Also update the sample text to make it more visible
        text_label.config(text=f"Sample text in {color[1]} color")

def reset_colors():
    root.config(bg="white")
    color_label.config(bg="lightgray", text="No color selected")
    rgb_label.config(text="RGB: None")
    bg_label.config(text="Background: white")
    text_label.config(fg="black", text="Sample text with changeable color")
    text_color_label.config(text="Text color: black")

# Create UI
tk.Label(root, text="Color Chooser Examples", font=("Arial", 14, "bold")).pack(pady=10)

tk.Button(root, text="Choose Color", command=choose_color, bg="lightblue").pack(pady=5)
tk.Button(root, text="Choose Background", command=choose_background, bg="lightgreen").pack(pady=5)
tk.Button(root, text="Choose Text Color", command=choose_text_color, bg="lightyellow").pack(pady=5)
tk.Button(root, text="Reset Colors", command=reset_colors, bg="lightcoral").pack(pady=5)

# Color display
color_label = tk.Label(root, text="No color selected", font=("Arial", 12), 
                      bg="lightgray", width=20, height=3)
color_label.pack(pady=10)

rgb_label = tk.Label(root, text="RGB: None", font=("Arial", 10))
rgb_label.pack(pady=5)

bg_label = tk.Label(root, text="Background: white", font=("Arial", 10))
bg_label.pack(pady=5)

text_label = tk.Label(root, text="Sample text with changeable color", 
                     font=("Arial", 14, "bold"), bg="white")
text_label.pack(pady=10)

text_color_label = tk.Label(root, text="Text color: black", font=("Arial", 10))
text_color_label.pack(pady=5)

root.mainloop()