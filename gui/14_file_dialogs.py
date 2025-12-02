import tkinter as tk
from tkinter import filedialog, messagebox

# File dialogs - open and save file dialogs
root = tk.Tk()
root.title("File Dialog Examples")
root.geometry("500x400")

def open_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[
            ("Text files", "*.txt"),
            ("Python files", "*.py"),
            ("All files", "*.*")
        ]
    )
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                text_area.delete("1.0", tk.END)
                text_area.insert("1.0", content)
                status_label.config(text=f"Opened: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}")

def save_file():
    file_path = filedialog.asksaveasfilename(
        title="Save file as",
        defaultextension=".txt",
        filetypes=[
            ("Text files", "*.txt"),
            ("Python files", "*.py"),
            ("All files", "*.*")
        ]
    )
    if file_path:
        try:
            content = text_area.get("1.0", tk.END)
            with open(file_path, 'w') as file:
                file.write(content)
            status_label.config(text=f"Saved: {file_path}")
            messagebox.showinfo("Success", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

def open_multiple():
    file_paths = filedialog.askopenfilenames(
        title="Select multiple files",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_paths:
        status_label.config(text=f"Selected {len(file_paths)} files")
        file_list = "\n".join(file_paths)
        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", f"Selected files:\n{file_list}")

def select_directory():
    dir_path = filedialog.askdirectory(title="Select a directory")
    if dir_path:
        status_label.config(text=f"Selected directory: {dir_path}")

# Create UI
tk.Label(root, text="File Dialog Examples", font=("Arial", 14, "bold")).pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Open File", command=open_file, bg="lightgreen").pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Save File", command=save_file, bg="lightblue").pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Open Multiple", command=open_multiple, bg="lightyellow").pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Select Directory", command=select_directory, bg="lightcoral").pack(side=tk.LEFT, padx=5)

# Text area
text_area = tk.Text(root, height=15, width=60, font=("Arial", 10))
text_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
text_area.insert("1.0", "Use the buttons above to open/save files.\nThis text area will show file contents.")

# Status label
status_label = tk.Label(root, text="Ready", relief="sunken", anchor="w")
status_label.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()