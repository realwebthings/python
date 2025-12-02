import tkinter as tk

# Grid layout manager - organize widgets in rows and columns
root = tk.Tk()
root.title("Grid Layout Example")
root.geometry("500x400")

# Grid layout example
tk.Label(root, text="Grid Layout Manager", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

# Form example using grid
tk.Label(root, text="Name:", font=("Arial", 10)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(root, width=20)
name_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Email:", font=("Arial", 10)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
email_entry = tk.Entry(root, width=20)
email_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Phone:", font=("Arial", 10)).grid(row=3, column=0, sticky="e", padx=5, pady=5)
phone_entry = tk.Entry(root, width=20)
phone_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    result_text.delete("1.0", tk.END)
    result_text.insert("1.0", f"Name: {name}\nEmail: {email}\nPhone: {phone}")

def clear_form():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    result_text.delete("1.0", tk.END)

tk.Button(root, text="Submit", command=submit_form, bg="lightgreen").grid(row=4, column=0, padx=5, pady=10)
tk.Button(root, text="Clear", command=clear_form, bg="lightcoral").grid(row=4, column=1, padx=5, pady=10)

# Text area spanning multiple columns
tk.Label(root, text="Result:", font=("Arial", 10)).grid(row=5, column=0, sticky="nw", padx=5, pady=5)
result_text = tk.Text(root, height=8, width=40)
result_text.grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

# Calculator grid example
calc_frame = tk.Frame(root, relief="raised", bd=2)
calc_frame.grid(row=1, column=2, rowspan=4, padx=20, pady=10, sticky="n")

tk.Label(calc_frame, text="Grid Calculator", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=3, pady=5)

calc_display = tk.Entry(calc_frame, width=15, justify="right", font=("Arial", 12))
calc_display.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

def calc_button_click(value):
    current = calc_display.get()
    calc_display.delete(0, tk.END)
    calc_display.insert(0, current + str(value))

def calc_clear():
    calc_display.delete(0, tk.END)

def calc_equals():
    try:
        result = eval(calc_display.get())
        calc_display.delete(0, tk.END)
        calc_display.insert(0, str(result))
    except:
        calc_display.delete(0, tk.END)
        calc_display.insert(0, "Error")

# Calculator buttons in grid
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),
    ('0', 5, 0), ('+', 5, 1), ('-', 5, 2),
    ('*', 6, 0), ('/', 6, 1), ('=', 6, 2)
]

for (text, row, col) in buttons:
    if text == '=':
        cmd = calc_equals
    else:
        cmd = lambda x=text: calc_button_click(x)
    
    tk.Button(calc_frame, text=text, command=cmd, width=3, height=2).grid(row=row, column=col, padx=1, pady=1)

tk.Button(calc_frame, text="Clear", command=calc_clear, width=10).grid(row=7, column=0, columnspan=3, padx=1, pady=5)

# Configure grid weights for resizing
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(5, weight=1)

root.mainloop()