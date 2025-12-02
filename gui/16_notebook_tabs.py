import tkinter as tk
from tkinter import ttk

# Notebook widget - tabbed interface
root = tk.Tk()
root.title("Notebook Tabs Example")
root.geometry("500x400")

# Create notebook (tab container)
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Tab 1 - Text Editor
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Text Editor")

tk.Label(tab1, text="Simple Text Editor", font=("Arial", 12, "bold")).pack(pady=10)
text_area = tk.Text(tab1, height=15, width=50, font=("Arial", 10))
text_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
text_area.insert("1.0", "Type your text here...")

# Tab 2 - Calculator
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Calculator")

tk.Label(tab2, text="Simple Calculator", font=("Arial", 12, "bold")).pack(pady=10)

calc_var = tk.StringVar()
calc_entry = tk.Entry(tab2, textvariable=calc_var, font=("Arial", 14), width=20, justify="right")
calc_entry.pack(pady=10)

def calc_click(value):
    current = calc_var.get()
    calc_var.set(current + str(value))

def calc_clear():
    calc_var.set("")

def calc_equals():
    try:
        result = eval(calc_var.get())
        calc_var.set(str(result))
    except:
        calc_var.set("Error")

calc_frame = tk.Frame(tab2)
calc_frame.pack(pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        if btn_text == '=':
            cmd = calc_equals
        else:
            cmd = lambda x=btn_text: calc_click(x)
        
        tk.Button(calc_frame, text=btn_text, command=cmd, width=5, height=2).grid(row=i, column=j, padx=2, pady=2)

tk.Button(calc_frame, text="Clear", command=calc_clear, width=22, height=2).grid(row=4, column=0, columnspan=4, padx=2, pady=2)

# Tab 3 - Settings
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Settings")

tk.Label(tab3, text="Application Settings", font=("Arial", 12, "bold")).pack(pady=10)

# Theme selection
theme_var = tk.StringVar(value="Light")
tk.Label(tab3, text="Theme:", font=("Arial", 10)).pack(pady=5)
tk.Radiobutton(tab3, text="Light", variable=theme_var, value="Light").pack()
tk.Radiobutton(tab3, text="Dark", variable=theme_var, value="Dark").pack()

# Font size
font_var = tk.IntVar(value=12)
tk.Label(tab3, text="Font Size:", font=("Arial", 10)).pack(pady=(20, 5))
tk.Scale(tab3, from_=8, to=24, orient=tk.HORIZONTAL, variable=font_var).pack()

# Notifications
notify_var = tk.BooleanVar(value=True)
tk.Checkbutton(tab3, text="Enable Notifications", variable=notify_var).pack(pady=20)

def apply_settings():
    theme = theme_var.get()
    font_size = font_var.get()
    notifications = notify_var.get()
    settings_label.config(text=f"Applied: {theme} theme, Font: {font_size}, Notifications: {notifications}")

tk.Button(tab3, text="Apply Settings", command=apply_settings, bg="lightgreen").pack(pady=10)
settings_label = tk.Label(tab3, text="", font=("Arial", 10), fg="blue")
settings_label.pack(pady=10)

# Tab 4 - About
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="About")

tk.Label(tab4, text="About This Application", font=("Arial", 12, "bold")).pack(pady=20)
tk.Label(tab4, text="Tkinter Notebook Demo", font=("Arial", 14)).pack(pady=10)
tk.Label(tab4, text="Version 1.0", font=("Arial", 10)).pack(pady=5)
tk.Label(tab4, text="Created with Python & Tkinter", font=("Arial", 10)).pack(pady=5)

root.mainloop()