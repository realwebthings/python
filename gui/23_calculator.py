import tkinter as tk
import math

# Advanced Calculator
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.resizable(False, False)

# Variables
current = "0"
operator = ""
operand = 0
result_var = tk.StringVar(value="0")

# Display
display_frame = tk.Frame(root, bg="black", height=80)
display_frame.pack(fill=tk.X, padx=5, pady=5)
display_frame.pack_propagate(False)

display = tk.Entry(display_frame, textvariable=result_var, font=("Arial", 24), 
                  justify="right", state="readonly", bg="black", fg="white", bd=0)
display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

def button_click(value):
    global current
    if current == "0" or current == "Error":
        current = str(value)
    else:
        current += str(value)
    result_var.set(current)

def operator_click(op):
    global current, operator, operand
    try:
        operand = float(current)
        operator = op
        current = "0"
    except:
        result_var.set("Error")

def equals_click():
    global current, operator, operand
    try:
        if operator == "+":
            result = operand + float(current)
        elif operator == "-":
            result = operand - float(current)
        elif operator == "*":
            result = operand * float(current)
        elif operator == "/":
            if float(current) == 0:
                result_var.set("Error")
                return
            result = operand / float(current)
        elif operator == "^":
            result = operand ** float(current)
        else:
            return
        
        current = str(result)
        result_var.set(current)
        operator = ""
    except:
        result_var.set("Error")

def clear():
    global current, operator, operand
    current = "0"
    operator = ""
    operand = 0
    result_var.set("0")

def clear_entry():
    global current
    current = "0"
    result_var.set("0")

def backspace():
    global current
    if len(current) > 1:
        current = current[:-1]
    else:
        current = "0"
    result_var.set(current)

def decimal():
    global current
    if "." not in current:
        current += "."
        result_var.set(current)

def percent():
    global current
    try:
        current = str(float(current) / 100)
        result_var.set(current)
    except:
        result_var.set("Error")

def square_root():
    global current
    try:
        result = math.sqrt(float(current))
        current = str(result)
        result_var.set(current)
    except:
        result_var.set("Error")

def square():
    global current
    try:
        result = float(current) ** 2
        current = str(result)
        result_var.set(current)
    except:
        result_var.set("Error")

def reciprocal():
    global current
    try:
        if float(current) == 0:
            result_var.set("Error")
            return
        result = 1 / float(current)
        current = str(result)
        result_var.set(current)
    except:
        result_var.set("Error")

def negate():
    global current
    try:
        if current != "0":
            if current.startswith("-"):
                current = current[1:]
            else:
                current = "-" + current
            result_var.set(current)
    except:
        result_var.set("Error")

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Button configuration
btn_config = {"font": ("Arial", 14), "width": 5, "height": 2}
num_config = {**btn_config, "bg": "white", "fg": "black"}
op_config = {**btn_config, "bg": "orange", "fg": "white"}
func_config = {**btn_config, "bg": "lightgray", "fg": "black"}

# Row 0 - Function buttons
tk.Button(button_frame, text="C", command=clear, **func_config).grid(row=0, column=0, padx=2, pady=2)
tk.Button(button_frame, text="CE", command=clear_entry, **func_config).grid(row=0, column=1, padx=2, pady=2)
tk.Button(button_frame, text="⌫", command=backspace, **func_config).grid(row=0, column=2, padx=2, pady=2)
tk.Button(button_frame, text="÷", command=lambda: operator_click("/"), **op_config).grid(row=0, column=3, padx=2, pady=2)

# Row 1 - Advanced functions
tk.Button(button_frame, text="√", command=square_root, **func_config).grid(row=1, column=0, padx=2, pady=2)
tk.Button(button_frame, text="x²", command=square, **func_config).grid(row=1, column=1, padx=2, pady=2)
tk.Button(button_frame, text="1/x", command=reciprocal, **func_config).grid(row=1, column=2, padx=2, pady=2)
tk.Button(button_frame, text="×", command=lambda: operator_click("*"), **op_config).grid(row=1, column=3, padx=2, pady=2)

# Row 2 - Numbers 7,8,9
tk.Button(button_frame, text="7", command=lambda: button_click("7"), **num_config).grid(row=2, column=0, padx=2, pady=2)
tk.Button(button_frame, text="8", command=lambda: button_click("8"), **num_config).grid(row=2, column=1, padx=2, pady=2)
tk.Button(button_frame, text="9", command=lambda: button_click("9"), **num_config).grid(row=2, column=2, padx=2, pady=2)
tk.Button(button_frame, text="−", command=lambda: operator_click("-"), **op_config).grid(row=2, column=3, padx=2, pady=2)

# Row 3 - Numbers 4,5,6
tk.Button(button_frame, text="4", command=lambda: button_click("4"), **num_config).grid(row=3, column=0, padx=2, pady=2)
tk.Button(button_frame, text="5", command=lambda: button_click("5"), **num_config).grid(row=3, column=1, padx=2, pady=2)
tk.Button(button_frame, text="6", command=lambda: button_click("6"), **num_config).grid(row=3, column=2, padx=2, pady=2)
tk.Button(button_frame, text="+", command=lambda: operator_click("+"), **op_config).grid(row=3, column=3, padx=2, pady=2)

# Row 4 - Numbers 1,2,3
tk.Button(button_frame, text="1", command=lambda: button_click("1"), **num_config).grid(row=4, column=0, padx=2, pady=2)
tk.Button(button_frame, text="2", command=lambda: button_click("2"), **num_config).grid(row=4, column=1, padx=2, pady=2)
tk.Button(button_frame, text="3", command=lambda: button_click("3"), **num_config).grid(row=4, column=2, padx=2, pady=2)
tk.Button(button_frame, text="=", command=equals_click, **op_config).grid(row=4, column=3, rowspan=2, padx=2, pady=2, sticky="ns")

# Row 5 - Zero and decimal
tk.Button(button_frame, text="±", command=negate, **func_config).grid(row=5, column=0, padx=2, pady=2)
tk.Button(button_frame, text="0", command=lambda: button_click("0"), **num_config).grid(row=5, column=1, padx=2, pady=2)
tk.Button(button_frame, text=".", command=decimal, **num_config).grid(row=5, column=2, padx=2, pady=2)

# Configure grid weights
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)
for i in range(6):
    button_frame.grid_rowconfigure(i, weight=1)

# Keyboard bindings
def key_press(event):
    key = event.char
    if key.isdigit():
        button_click(key)
    elif key == ".":
        decimal()
    elif key in "+-*/":
        operator_click(key)
    elif key == "\r":  # Enter
        equals_click()
    elif key == "\x08":  # Backspace
        backspace()
    elif key == "c" or key == "C":
        clear()

root.bind("<KeyPress>", key_press)
root.focus_set()

root.mainloop()