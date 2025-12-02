import tkinter as tk

# Scale widget - slider for selecting numeric values
root = tk.Tk()
root.title("Scale Widget")
root.geometry("400x350")

def update_value(val):
    result_label.config(text=f"Volume: {val}%")

def update_color(val):
    # Convert scale value to RGB color
    red_val = int(float(val) * 255 / 100)
    color = f"#{red_val:02x}0000"  # Red gradient
    color_label.config(bg=color, text=f"Red: {red_val}")

# Volume scale (horizontal)
tk.Label(root, text="Volume Control:", font=("Arial", 12)).pack(pady=10)

volume_scale = tk.Scale(root,
                       from_=0,
                       to=100,
                       orient=tk.HORIZONTAL,
                       length=300,
                       command=update_value,
                       bg="lightgray",
                       font=("Arial", 10))
volume_scale.set(50)  # Default value
volume_scale.pack(pady=10)

result_label = tk.Label(root, text="Volume: 50%", font=("Arial", 12), fg="blue")
result_label.pack(pady=5)

# Color scale (vertical)
tk.Label(root, text="Color Intensity:", font=("Arial", 12)).pack(pady=(20, 5))

# Create color label first
color_label = tk.Label(root, text="Red: 127", font=("Arial", 12), 
                      bg="#7f0000", fg="white", width=15, height=2)
color_label.pack(pady=10)

color_scale = tk.Scale(root,
                      from_=0,
                      to=100,
                      orient=tk.VERTICAL,
                      length=150,
                      command=update_color,
                      bg="lightgray",
                      font=("Arial", 10))
color_scale.set(50)
color_scale.pack(pady=10)

# Initialize color display
update_color(50)

root.mainloop()