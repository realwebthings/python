import tkinter as tk

# Checkbutton widget - checkbox for boolean selections
root = tk.Tk()
root.title("Checkbutton Widget")
root.geometry("400x300")

def show_selections():
    selections = []
    if var1.get():
        selections.append("Python")
    if var2.get():
        selections.append("Java")
    if var3.get():
        selections.append("JavaScript")
    
    if selections:
        result_label.config(text=f"Selected: {', '.join(selections)}")
    else:
        result_label.config(text="No languages selected")

# Create variables to store checkbox states
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

# Create checkbuttons
tk.Label(root, text="Select your favorite programming languages:", font=("Arial", 12)).pack(pady=10)

check1 = tk.Checkbutton(root,
                       text="Python",
                       variable=var1,
                       font=("Arial", 11),
                       command=show_selections)

check2 = tk.Checkbutton(root,
                       text="Java",
                       variable=var2,
                       font=("Arial", 11),
                       command=show_selections)

check3 = tk.Checkbutton(root,
                       text="JavaScript",
                       variable=var3,
                       font=("Arial", 11),
                       command=show_selections)

check1.pack(pady=5)
check2.pack(pady=5)
check3.pack(pady=5)

# Result label
result_label = tk.Label(root, text="No languages selected", font=("Arial", 12), fg="blue")
result_label.pack(pady=20)

root.mainloop()