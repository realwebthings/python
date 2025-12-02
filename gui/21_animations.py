import tkinter as tk
import math
import random

# Animations - moving objects with smooth motion
root = tk.Tk()
root.title("Animations Example")
root.geometry("700x600")

canvas = tk.Canvas(root, width=680, height=400, bg="black", relief="sunken", bd=2)
canvas.pack(pady=10)

# Animation objects
animations = []

class BouncingBall:
    def __init__(self, x, y, dx, dy, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color
        self.ball = canvas.create_oval(x-radius, y-radius, x+radius, y+radius, 
                                     fill=color, outline="white")
        
    def update(self):
        # Move ball
        self.x += self.dx
        self.y += self.dy
        
        # Bounce off walls
        if self.x - self.radius <= 0 or self.x + self.radius >= 680:
            self.dx = -self.dx
        if self.y - self.radius <= 0 or self.y + self.radius >= 400:
            self.dy = -self.dy
            
        # Update position on canvas
        canvas.coords(self.ball, 
                     self.x - self.radius, self.y - self.radius,
                     self.x + self.radius, self.y + self.radius)

class RotatingSquare:
    def __init__(self, center_x, center_y, size, color):
        self.center_x = center_x
        self.center_y = center_y
        self.size = size
        self.color = color
        self.angle = 0
        self.square = canvas.create_polygon(0, 0, 0, 0, 0, 0, 0, 0, fill=color, outline="white")
        
    def update(self):
        self.angle += 0.05
        
        # Calculate rotated square corners
        half_size = self.size / 2
        corners = []
        
        for dx, dy in [(-half_size, -half_size), (half_size, -half_size), 
                      (half_size, half_size), (-half_size, half_size)]:
            # Rotate point
            rotated_x = dx * math.cos(self.angle) - dy * math.sin(self.angle)
            rotated_y = dx * math.sin(self.angle) + dy * math.cos(self.angle)
            
            corners.extend([self.center_x + rotated_x, self.center_y + rotated_y])
        
        canvas.coords(self.square, *corners)

class SineWave:
    def __init__(self, start_x, y, amplitude, frequency, color):
        self.start_x = start_x
        self.y = y
        self.amplitude = amplitude
        self.frequency = frequency
        self.color = color
        self.phase = 0
        self.circle = canvas.create_oval(0, 0, 10, 10, fill=color, outline="white")
        
    def update(self):
        self.phase += 0.1
        x = self.start_x + self.phase * 50
        y = self.y + self.amplitude * math.sin(self.frequency * self.phase)
        
        # Wrap around screen
        if x > 680:
            self.phase = 0
            x = self.start_x
            
        canvas.coords(self.circle, x-5, y-5, x+5, y+5)

class Spiral:
    def __init__(self, center_x, center_y, color):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color
        self.angle = 0
        self.radius = 0
        self.dot = canvas.create_oval(0, 0, 6, 6, fill=color, outline="white")
        
    def update(self):
        self.angle += 0.2
        self.radius += 0.5
        
        if self.radius > 100:
            self.radius = 0
            
        x = self.center_x + self.radius * math.cos(self.angle)
        y = self.center_y + self.radius * math.sin(self.angle)
        
        canvas.coords(self.dot, x-3, y-3, x+3, y+3)

# Create animations
def create_bouncing_balls():
    for _ in range(3):
        x = random.randint(50, 630)
        y = random.randint(50, 350)
        dx = random.uniform(-5, 5)
        dy = random.uniform(-5, 5)
        radius = random.randint(10, 25)
        color = random.choice(["red", "blue", "green", "yellow", "purple", "orange"])
        animations.append(BouncingBall(x, y, dx, dy, radius, color))

def create_rotating_squares():
    for i in range(2):
        x = 150 + i * 300
        y = 200
        size = 40 + i * 20
        color = ["cyan", "magenta"][i]
        animations.append(RotatingSquare(x, y, size, color))

def create_sine_waves():
    for i in range(2):
        y = 100 + i * 200
        amplitude = 30 + i * 20
        frequency = 0.5 + i * 0.3
        color = ["lime", "pink"][i]
        animations.append(SineWave(0, y, amplitude, frequency, color))

def create_spirals():
    animations.append(Spiral(500, 150, "white"))
    animations.append(Spiral(200, 300, "gold"))

# Animation control
is_running = False

def animate():
    if is_running:
        for animation in animations:
            animation.update()
        root.after(20, animate)  # 50 FPS

def start_animation():
    global is_running
    is_running = True
    animate()

def stop_animation():
    global is_running
    is_running = False

def clear_animations():
    global animations
    canvas.delete("all")
    animations.clear()

def reset_animations():
    clear_animations()
    create_bouncing_balls()
    create_rotating_squares()
    create_sine_waves()
    create_spirals()

# Control panel
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Button(control_frame, text="Start", command=start_animation, bg="lightgreen").pack(side=tk.LEFT, padx=5)
tk.Button(control_frame, text="Stop", command=stop_animation, bg="lightcoral").pack(side=tk.LEFT, padx=5)
tk.Button(control_frame, text="Reset", command=reset_animations, bg="lightblue").pack(side=tk.LEFT, padx=5)
tk.Button(control_frame, text="Clear", command=clear_animations, bg="lightyellow").pack(side=tk.LEFT, padx=5)

# Individual animation controls
anim_frame = tk.Frame(root)
anim_frame.pack(pady=10)

tk.Button(anim_frame, text="Add Bouncing Balls", 
         command=lambda: create_bouncing_balls(), width=15).pack(side=tk.LEFT, padx=2)
tk.Button(anim_frame, text="Add Rotating Squares", 
         command=lambda: create_rotating_squares(), width=15).pack(side=tk.LEFT, padx=2)
tk.Button(anim_frame, text="Add Sine Waves", 
         command=lambda: create_sine_waves(), width=15).pack(side=tk.LEFT, padx=2)
tk.Button(anim_frame, text="Add Spirals", 
         command=lambda: create_spirals(), width=15).pack(side=tk.LEFT, padx=2)

# Status
status_label = tk.Label(root, text="Click 'Reset' to create animations, then 'Start' to begin", 
                       font=("Arial", 10), fg="blue")
status_label.pack(pady=5)

# Initialize with some animations
reset_animations()

root.mainloop()