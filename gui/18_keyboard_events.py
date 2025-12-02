import tkinter as tk

# Keyboard events - handling key presses and combinations
root = tk.Tk()
root.title("Keyboard Events Example")
root.geometry("500x400")

# Variables to track state
key_log = []

def on_key_press(event):
    key_info = f"Key pressed: '{event.keysym}' (keycode: {event.keycode})"
    key_log.append(key_info)
    
    # Update display
    log_text.delete("1.0", tk.END)
    log_text.insert("1.0", "\n".join(key_log[-10:]))  # Show last 10 keys
    
    # Handle special keys
    if event.keysym == "Escape":
        status_label.config(text="Escape pressed - clearing log", fg="red")
        key_log.clear()
        log_text.delete("1.0", tk.END)
    elif event.keysym == "Return":
        status_label.config(text="Enter pressed", fg="green")
    elif event.keysym == "space":
        status_label.config(text="Space pressed", fg="blue")
    else:
        status_label.config(text=f"Last key: {event.keysym}", fg="black")

def on_key_release(event):
    release_label.config(text=f"Released: {event.keysym}")

def handle_ctrl_combinations(event):
    if event.state & 0x4:  # Ctrl key is pressed
        if event.keysym == 'c':
            status_label.config(text="Ctrl+C pressed", fg="purple")
        elif event.keysym == 'v':
            status_label.config(text="Ctrl+V pressed", fg="purple")
        elif event.keysym == 's':
            status_label.config(text="Ctrl+S pressed", fg="purple")
        elif event.keysym == 'q':
            root.quit()

def clear_log():
    key_log.clear()
    log_text.delete("1.0", tk.END)
    status_label.config(text="Log cleared")

# Create UI
tk.Label(root, text="Keyboard Events Demo", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="Click in the window and press any keys", font=("Arial", 10)).pack(pady=5)

# Text entry for testing
tk.Label(root, text="Type here:", font=("Arial", 10)).pack(pady=(10, 5))
entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=5)

# Key log display
tk.Label(root, text="Key Press Log (last 10 keys):", font=("Arial", 10)).pack(pady=(20, 5))
log_text = tk.Text(root, height=8, width=50, font=("Courier", 10))
log_text.pack(pady=5, padx=10)

# Status labels
status_label = tk.Label(root, text="Press any key...", font=("Arial", 10), fg="gray")
status_label.pack(pady=5)

release_label = tk.Label(root, text="", font=("Arial", 10), fg="gray")
release_label.pack(pady=5)

# Clear button
tk.Button(root, text="Clear Log", command=clear_log, bg="lightcoral").pack(pady=10)

# Instructions
instructions = tk.Label(root, 
    text="Special keys: ESC (clear), Enter, Space, Ctrl+C/V/S, Ctrl+Q (quit)",
    font=("Arial", 9), fg="blue")
instructions.pack(pady=5)

# Bind keyboard events
root.bind("<KeyPress>", on_key_press)
root.bind("<KeyRelease>", on_key_release)
root.bind("<Control-Key>", handle_ctrl_combinations)

# Make sure window can receive focus
root.focus_set()

# Arrow key handling
def handle_arrows(event):
    if event.keysym in ['Up', 'Down', 'Left', 'Right']:
        status_label.config(text=f"Arrow key: {event.keysym}", fg="orange")

root.bind("<Key>", handle_arrows)

root.mainloop()