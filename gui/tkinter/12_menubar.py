import tkinter as tk
from tkinter import messagebox

# Menu widget - creates menu bars and context menus
root = tk.Tk()
root.title("Menu Widget")
root.geometry("500x400")

def new_file():
    messagebox.showinfo("Menu", "New File clicked")

def open_file():
    messagebox.showinfo("Menu", "Open File clicked")

def save_file():
    messagebox.showinfo("Menu", "Save File clicked")

def exit_app():
    root.quit()

def cut_text():
    messagebox.showinfo("Menu", "Cut clicked")

def copy_text():
    messagebox.showinfo("Menu", "Copy clicked")

def paste_text():
    messagebox.showinfo("Menu", "Paste clicked")

def about():
    messagebox.showinfo("About", "Tkinter Menu Demo\nVersion 1.0")

# Create menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# File menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app, accelerator="Ctrl+Q")

# Edit menu
edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text, accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=copy_text, accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", command=paste_text, accelerator="Ctrl+V")

# Help menu
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# Context menu (right-click menu)
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Cut", command=cut_text)
context_menu.add_command(label="Copy", command=copy_text)
context_menu.add_command(label="Paste", command=paste_text)

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

# Main content
text_area = tk.Text(root, font=("Arial", 12), bg="white")
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
text_area.insert("1.0", "This is a text area.\nTry the menu options above.\nRight-click for context menu.")

# Bind right-click to show context menu
text_area.bind("<Button-3>", show_context_menu)  # Button-3 is right-click

# Status bar
status_bar = tk.Label(root, text="Ready", relief="sunken", anchor="w")
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()