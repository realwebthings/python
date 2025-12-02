import tkinter as tk

# Frame widget - container for organizing other widgets
root = tk.Tk()
root.title("Frame Widget")
root.geometry("500x400")

# Main title
tk.Label(root, text="Frame Widget Demo", font=("Arial", 16, "bold")).pack(pady=10)

# Top frame - horizontal layout
top_frame = tk.Frame(root, bg="lightblue", relief="raised", bd=2)
top_frame.pack(fill=tk.X, padx=10, pady=5)

tk.Label(top_frame, text="Top Frame", bg="lightblue", font=("Arial", 12)).pack(side=tk.LEFT, padx=10, pady=5)
tk.Button(top_frame, text="Button 1").pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(top_frame, text="Button 2").pack(side=tk.LEFT, padx=5, pady=5)

# Middle frame - contains left and right frames
middle_frame = tk.Frame(root)
middle_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Left frame
left_frame = tk.Frame(middle_frame, bg="lightgreen", relief="sunken", bd=2)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))

tk.Label(left_frame, text="Left Frame", bg="lightgreen", font=("Arial", 12)).pack(pady=10)
tk.Entry(left_frame, width=20).pack(pady=5)
tk.Button(left_frame, text="Submit").pack(pady=5)

# Right frame
right_frame = tk.Frame(middle_frame, bg="lightyellow", relief="groove", bd=2)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))

tk.Label(right_frame, text="Right Frame", bg="lightyellow", font=("Arial", 12)).pack(pady=10)

# Radio buttons in right frame
var = tk.IntVar()
tk.Radiobutton(right_frame, text="Option 1", variable=var, value=1, bg="lightyellow").pack(pady=2)
tk.Radiobutton(right_frame, text="Option 2", variable=var, value=2, bg="lightyellow").pack(pady=2)
tk.Radiobutton(right_frame, text="Option 3", variable=var, value=3, bg="lightyellow").pack(pady=2)

# Bottom frame
bottom_frame = tk.Frame(root, bg="lightcoral", relief="ridge", bd=2)
bottom_frame.pack(fill=tk.X, padx=10, pady=5)

tk.Label(bottom_frame, text="Bottom Frame - Status Bar", bg="lightcoral", font=("Arial", 10)).pack(pady=5)

root.mainloop()