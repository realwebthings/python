import tkinter as tk

# Drag and drop simulation - moving widgets with mouse
root = tk.Tk()
root.title("Drag and Drop Example")
root.geometry("600x500")

class DraggableWidget:
    def __init__(self, canvas, x, y, width, height, color, text):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(x, y, x+width, y+height, fill=color, outline="black", width=2)
        self.text = canvas.create_text(x+width//2, y+height//2, text=text, font=("Arial", 10, "bold"))
        
        # Bind events
        canvas.tag_bind(self.rect, "<Button-1>", self.on_click)
        canvas.tag_bind(self.rect, "<B1-Motion>", self.on_drag)
        canvas.tag_bind(self.rect, "<ButtonRelease-1>", self.on_release)
        
        canvas.tag_bind(self.text, "<Button-1>", self.on_click)
        canvas.tag_bind(self.text, "<B1-Motion>", self.on_drag)
        canvas.tag_bind(self.text, "<ButtonRelease-1>", self.on_release)
        
        self.start_x = 0
        self.start_y = 0
        
    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y
        # Bring to front
        self.canvas.tag_raise(self.rect)
        self.canvas.tag_raise(self.text)
        
    def on_drag(self, event):
        dx = event.x - self.start_x
        dy = event.y - self.start_y
        
        self.canvas.move(self.rect, dx, dy)
        self.canvas.move(self.text, dx, dy)
        
        self.start_x = event.x
        self.start_y = event.y
        
    def on_release(self, event):
        # Snap to grid (optional)
        coords = self.canvas.coords(self.rect)
        x1, y1 = coords[0], coords[1]
        
        # Snap to 20px grid
        snap_x = round(x1 / 20) * 20
        snap_y = round(y1 / 20) * 20
        
        dx = snap_x - x1
        dy = snap_y - y1
        
        self.canvas.move(self.rect, dx, dy)
        self.canvas.move(self.text, dx, dy)

# Create canvas
tk.Label(root, text="Drag and Drop Demo", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="Drag the colored rectangles around (snaps to grid)", font=("Arial", 10)).pack(pady=5)

canvas = tk.Canvas(root, width=580, height=400, bg="white", relief="sunken", bd=2)
canvas.pack(pady=10)

# Draw grid
def draw_grid():
    for i in range(0, 580, 20):
        canvas.create_line(i, 0, i, 400, fill="lightgray", width=1)
    for i in range(0, 400, 20):
        canvas.create_line(0, i, 580, i, fill="lightgray", width=1)

draw_grid()

# Create draggable widgets
widgets = [
    DraggableWidget(canvas, 50, 50, 80, 60, "red", "Box 1"),
    DraggableWidget(canvas, 200, 100, 80, 60, "blue", "Box 2"),
    DraggableWidget(canvas, 350, 150, 80, 60, "green", "Box 3"),
    DraggableWidget(canvas, 100, 250, 80, 60, "yellow", "Box 4"),
    DraggableWidget(canvas, 300, 300, 80, 60, "purple", "Box 5")
]

# Control buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

def reset_positions():
    positions = [(50, 50), (200, 100), (350, 150), (100, 250), (300, 300)]
    for i, widget in enumerate(widgets):
        x, y = positions[i]
        current_coords = canvas.coords(widget.rect)
        dx = x - current_coords[0]
        dy = y - current_coords[1]
        canvas.move(widget.rect, dx, dy)
        canvas.move(widget.text, dx, dy)

def toggle_grid():
    if canvas.find_withtag("grid"):
        canvas.delete("grid")
    else:
        for i in range(0, 580, 20):
            canvas.create_line(i, 0, i, 400, fill="lightgray", width=1, tags="grid")
        for i in range(0, 400, 20):
            canvas.create_line(0, i, 580, i, fill="lightgray", width=1, tags="grid")

tk.Button(button_frame, text="Reset Positions", command=reset_positions, bg="lightblue").pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Toggle Grid", command=toggle_grid, bg="lightgreen").pack(side=tk.LEFT, padx=5)

# Instructions
instructions = tk.Label(root, 
    text="• Click and drag rectangles to move them\n• Rectangles snap to 20px grid when released\n• Try overlapping them!",
    font=("Arial", 9), fg="gray", justify=tk.LEFT)
instructions.pack(pady=5)

root.mainloop()