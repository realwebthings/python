import tkinter as tk
import math

# Move image with keyboard and mouse
root = tk.Tk()
root.title("Move Image Example")
root.geometry("600x500")

# Create canvas
canvas = tk.Canvas(root, width=580, height=400, bg="lightblue", relief="sunken", bd=2)
canvas.pack(pady=10)

# Create a simple image using canvas (since we might not have image files)
def create_player():
    # Create a simple character using shapes
    x, y = 290, 200  # Center position
    
    # Body (rectangle)
    body = canvas.create_rectangle(x-15, y-20, x+15, y+20, fill="red", outline="black", width=2)
    
    # Head (circle)
    head = canvas.create_oval(x-10, y-35, x+10, y-15, fill="yellow", outline="black", width=2)
    
    # Eyes
    left_eye = canvas.create_oval(x-7, y-30, x-3, y-26, fill="black")
    right_eye = canvas.create_oval(x+3, y-30, x+7, y-26, fill="black")
    
    # Legs
    left_leg = canvas.create_line(x-10, y+20, x-10, y+35, fill="black", width=3)
    right_leg = canvas.create_line(x+10, y+20, x+10, y+35, fill="black", width=3)
    
    return [body, head, left_eye, right_eye, left_leg, right_leg]

player_parts = create_player()
player_x, player_y = 290, 200
speed = 5

def move_player(dx, dy):
    global player_x, player_y
    
    # Check boundaries
    new_x = player_x + dx
    new_y = player_y + dy
    
    if 20 <= new_x <= 560 and 40 <= new_y <= 360:
        for part in player_parts:
            canvas.move(part, dx, dy)
        player_x = new_x
        player_y = new_y
        
        # Update position label
        pos_label.config(text=f"Position: ({player_x}, {player_y})")

def on_key_press(event):
    if event.keysym == "Up" or event.keysym == "w":
        move_player(0, -speed)
    elif event.keysym == "Down" or event.keysym == "s":
        move_player(0, speed)
    elif event.keysym == "Left" or event.keysym == "a":
        move_player(-speed, 0)
    elif event.keysym == "Right" or event.keysym == "d":
        move_player(speed, 0)
    elif event.keysym == "space":
        # Jump (temporary upward movement)
        jump()

def jump():
    # Simple jump animation
    for i in range(10):
        root.after(i * 20, lambda i=i: move_player(0, -2 if i < 5 else 2))

# Mouse movement
def on_mouse_click(event):
    target_x, target_y = event.x, event.y
    
    # Calculate direction
    dx = target_x - player_x
    dy = target_y - player_y
    
    # Normalize and scale
    distance = math.sqrt(dx*dx + dy*dy)
    if distance > 0:
        dx = (dx / distance) * speed
        dy = (dy / distance) * speed
        
        # Move towards target
        move_towards_target(target_x, target_y, dx, dy)

def move_towards_target(target_x, target_y, dx, dy):
    current_distance = math.sqrt((target_x - player_x)**2 + (target_y - player_y)**2)
    
    if current_distance > speed:
        move_player(int(dx), int(dy))
        root.after(50, lambda: move_towards_target(target_x, target_y, dx, dy))

# Bind events
root.bind("<KeyPress>", on_key_press)
canvas.bind("<Button-1>", on_mouse_click)
root.focus_set()

# Control panel
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Button(control_frame, text="↑", command=lambda: move_player(0, -speed), width=3).grid(row=0, column=1)
tk.Button(control_frame, text="←", command=lambda: move_player(-speed, 0), width=3).grid(row=1, column=0)
tk.Button(control_frame, text="↓", command=lambda: move_player(0, speed), width=3).grid(row=1, column=1)
tk.Button(control_frame, text="→", command=lambda: move_player(speed, 0), width=3).grid(row=1, column=2)
tk.Button(control_frame, text="Jump", command=jump, bg="yellow").grid(row=0, column=3, padx=10)

# Speed control
speed_frame = tk.Frame(root)
speed_frame.pack(pady=5)

tk.Label(speed_frame, text="Speed:").pack(side=tk.LEFT)
speed_scale = tk.Scale(speed_frame, from_=1, to=20, orient=tk.HORIZONTAL, 
                      command=lambda v: globals().update(speed=int(v)))
speed_scale.set(speed)
speed_scale.pack(side=tk.LEFT, padx=10)

# Position display
pos_label = tk.Label(root, text=f"Position: ({player_x}, {player_y})", font=("Arial", 10))
pos_label.pack(pady=5)

# Instructions
instructions = tk.Label(root, 
    text="Use arrow keys or WASD to move • Click to move to mouse position • Space to jump",
    font=("Arial", 9), fg="gray")
instructions.pack(pady=5)

# Reset button
def reset_position():
    global player_x, player_y
    dx = 290 - player_x
    dy = 200 - player_y
    for part in player_parts:
        canvas.move(part, dx, dy)
    player_x, player_y = 290, 200
    pos_label.config(text=f"Position: ({player_x}, {player_y})")

tk.Button(root, text="Reset Position", command=reset_position, bg="lightcoral").pack(pady=5)

root.mainloop()