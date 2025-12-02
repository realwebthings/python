import tkinter as tk

# Button widget - clickable element that triggers actions
root = tk.Tk()
root.title("Button Widget")
root.geometry("400x300")

def button_click():
    print("Button clicked!")
    label.config(text="Button was clicked!")

def button_hover_enter(event):
    button.config(bg="lightblue")

def button_hover_leave(event):
    button.config(bg="lightgray")

# Create button
button = tk.Button(root,
                  text="Click Me!",
                  font=("Arial", 14),
                  fg="black",
                  bg="lightgray",
                  command=button_click,
                  padx=20,
                  pady=10)

# Bind hover events
button.bind("<Enter>", button_hover_enter)
button.bind("<Leave>", button_hover_leave)

# Status label
label = tk.Label(root, text="Click the button above", font=("Arial", 12))

button.pack(pady=20)
label.pack(pady=10)

root.mainloop()