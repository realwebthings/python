import tkinter as tk

# Radiobutton widget - single selection from multiple options
root = tk.Tk()
root.title("Radiobutton Widget")
root.geometry("400x300")

def show_selection():
    selection = var.get()
    if selection == 1:
        result_label.config(text="Selected: Small")
    elif selection == 2:
        result_label.config(text="Selected: Medium")
    elif selection == 3:
        result_label.config(text="Selected: Large")

# Create variable to store radio button selection
var = tk.IntVar()
var.set(2)  # Set default selection to Medium

# Create radio buttons
tk.Label(root, text="Select pizza size:", font=("Arial", 12)).pack(pady=10)

radio1 = tk.Radiobutton(root,
                       text="Small ($10)",
                       variable=var,
                       value=1,
                       font=("Arial", 11),
                       command=show_selection)

radio2 = tk.Radiobutton(root,
                       text="Medium ($15)",
                       variable=var,
                       value=2,
                       font=("Arial", 11),
                       command=show_selection)

radio3 = tk.Radiobutton(root,
                       text="Large ($20)",
                       variable=var,
                       value=3,
                       font=("Arial", 11),
                       command=show_selection)

radio1.pack(pady=5)
radio2.pack(pady=5)
radio3.pack(pady=5)

# Result label
result_label = tk.Label(root, text="Selected: Medium", font=("Arial", 12), fg="blue")
result_label.pack(pady=20)

root.mainloop()