import tkinter as tk

# Canvas widget - drawing area for graphics, shapes, and images
root = tk.Tk()
root.title("Canvas Widget")
root.geometry("600x500")

def draw_shapes():
    # Clear canvas
    canvas.delete("all")
    
    # Draw rectangle
    canvas.create_rectangle(50, 50, 150, 100, fill="red", outline="black", width=2)
    canvas.create_text(100, 75, text="Rectangle", fill="white", font=("Arial", 10))
    
    # Draw oval/circle
    canvas.create_oval(200, 50, 300, 150, fill="blue", outline="black", width=2)
    canvas.create_text(250, 100, text="Circle", fill="white", font=("Arial", 10))
    
    # Draw line
    canvas.create_line(350, 50, 450, 150, fill="green", width=3)
    canvas.create_text(400, 170, text="Line", fill="green", font=("Arial", 10))
    
    # Draw polygon (triangle)
    canvas.create_polygon(500, 150, 450, 50, 550, 50, fill="yellow", outline="black", width=2)
    canvas.create_text(500, 90, text="Triangle", fill="black", font=("Arial", 10))
    
    # Draw arc
    canvas.create_arc(50, 200, 150, 300, start=0, extent=180, fill="purple", outline="black", width=2)
    canvas.create_text(100, 330, text="Arc", fill="purple", font=("Arial", 10))

def clear_canvas():
    canvas.delete("all")

def draw_on_click(event):
    x, y = event.x, event.y
    canvas.create_oval(x-5, y-5, x+5, y+5, fill="orange", outline="red")

# Create canvas
canvas = tk.Canvas(root,
                  width=580,
                  height=350,
                  bg="white",
                  relief="sunken",
                  bd=2)
canvas.pack(pady=10)

# Bind mouse click to draw
canvas.bind("<Button-1>", draw_on_click)

# Control buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Draw Shapes", command=draw_shapes, bg="lightgreen").pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Clear Canvas", command=clear_canvas, bg="lightcoral").pack(side=tk.LEFT, padx=5)

# Instructions
tk.Label(root, text="Click 'Draw Shapes' to see examples, or click on canvas to draw dots", 
         font=("Arial", 10), fg="gray").pack(pady=5)

root.mainloop()