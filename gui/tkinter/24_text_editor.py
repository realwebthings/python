import tkinter as tk
from tkinter import filedialog, messagebox, font, colorchooser
from tkinter import scrolledtext

# Text Editor
root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")

# Variables
current_file = None
text_changed = False

# Text area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), undo=True)
text_area.pack(fill=tk.BOTH, expand=True)

def mark_changed(event=None):
    global text_changed
    text_changed = True
    update_title()

def update_title():
    title = "Text Editor"
    if current_file:
        title += f" - {current_file}"
    if text_changed:
        title += " *"
    root.title(title)

text_area.bind("<KeyPress>", mark_changed)

# Menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# File menu
def new_file():
    global current_file, text_changed
    if text_changed:
        if messagebox.askyesno("Save", "Save current file?"):
            save_file()
    text_area.delete("1.0", tk.END)
    current_file = None
    text_changed = False
    update_title()

def open_file():
    global current_file, text_changed
    if text_changed:
        if messagebox.askyesno("Save", "Save current file?"):
            save_file()
    
    file_path = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                text_area.delete("1.0", tk.END)
                text_area.insert("1.0", content)
                current_file = file_path
                text_changed = False
                update_title()
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}")

def save_file():
    global current_file, text_changed
    if current_file:
        try:
            content = text_area.get("1.0", tk.END)
            with open(current_file, 'w') as file:
                file.write(content)
            text_changed = False
            update_title()
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")
    else:
        save_as_file()

def save_as_file():
    global current_file, text_changed
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")]
    )
    if file_path:
        try:
            content = text_area.get("1.0", tk.END)
            with open(file_path, 'w') as file:
                file.write(content)
            current_file = file_path
            text_changed = False
            update_title()
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

def exit_app():
    if text_changed:
        if messagebox.askyesno("Save", "Save before exit?"):
            save_file()
    root.quit()

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save As", command=save_as_file, accelerator="Ctrl+Shift+S")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app, accelerator="Ctrl+Q")

# Edit menu
def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def select_all():
    text_area.tag_add(tk.SEL, "1.0", tk.END)

def find_text():
    find_window = tk.Toplevel(root)
    find_window.title("Find")
    find_window.geometry("300x100")
    
    tk.Label(find_window, text="Find:").pack(pady=5)
    find_entry = tk.Entry(find_window, width=30)
    find_entry.pack(pady=5)
    find_entry.focus()
    
    def find_next():
        search_text = find_entry.get()
        if search_text:
            start_pos = text_area.search(search_text, tk.INSERT, tk.END)
            if start_pos:
                end_pos = f"{start_pos}+{len(search_text)}c"
                text_area.tag_remove(tk.SEL, "1.0", tk.END)
                text_area.tag_add(tk.SEL, start_pos, end_pos)
                text_area.mark_set(tk.INSERT, end_pos)
                text_area.see(start_pos)
    
    tk.Button(find_window, text="Find Next", command=find_next).pack(pady=5)

edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text, accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=copy_text, accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", command=paste_text, accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all, accelerator="Ctrl+A")
edit_menu.add_command(label="Find", command=find_text, accelerator="Ctrl+F")

# Format menu
def change_font():
    current_font = font.Font(font=text_area['font'])
    font_dialog = tk.Toplevel(root)
    font_dialog.title("Font")
    font_dialog.geometry("400x300")
    
    # Font family
    tk.Label(font_dialog, text="Font:").pack(pady=5)
    font_var = tk.StringVar(value=current_font.actual()['family'])
    font_listbox = tk.Listbox(font_dialog, height=8)
    for family in font.families():
        font_listbox.insert(tk.END, family)
    font_listbox.pack(pady=5)
    
    # Font size
    tk.Label(font_dialog, text="Size:").pack(pady=5)
    size_var = tk.IntVar(value=current_font.actual()['size'])
    size_spinbox = tk.Spinbox(font_dialog, from_=8, to=72, textvariable=size_var)
    size_spinbox.pack(pady=5)
    
    def apply_font():
        try:
            selection = font_listbox.curselection()
            if selection:
                family = font_listbox.get(selection[0])
                size = size_var.get()
                text_area.config(font=(family, size))
                font_dialog.destroy()
        except:
            pass
    
    tk.Button(font_dialog, text="Apply", command=apply_font).pack(pady=10)

def change_color():
    color = colorchooser.askcolor(title="Choose text color")
    if color[1]:
        text_area.config(fg=color[1])

def change_bg_color():
    color = colorchooser.askcolor(title="Choose background color")
    if color[1]:
        text_area.config(bg=color[1])

format_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Font", command=change_font)
format_menu.add_command(label="Text Color", command=change_color)
format_menu.add_command(label="Background Color", command=change_bg_color)

# View menu
def toggle_word_wrap():
    current_wrap = text_area.cget("wrap")
    new_wrap = tk.NONE if current_wrap == tk.WORD else tk.WORD
    text_area.config(wrap=new_wrap)

def zoom_in():
    current_font = font.Font(font=text_area['font'])
    new_size = current_font.actual()['size'] + 2
    text_area.config(font=(current_font.actual()['family'], new_size))

def zoom_out():
    current_font = font.Font(font=text_area['font'])
    new_size = max(8, current_font.actual()['size'] - 2)
    text_area.config(font=(current_font.actual()['family'], new_size))

view_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Toggle Word Wrap", command=toggle_word_wrap)
view_menu.add_separator()
view_menu.add_command(label="Zoom In", command=zoom_in, accelerator="Ctrl++")
view_menu.add_command(label="Zoom Out", command=zoom_out, accelerator="Ctrl+-")

# Status bar
status_bar = tk.Label(root, text="Ready", relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

def update_status(event=None):
    line, col = text_area.index(tk.INSERT).split('.')
    char_count = len(text_area.get("1.0", tk.END)) - 1
    word_count = len(text_area.get("1.0", tk.END).split())
    status_bar.config(text=f"Line: {line} | Column: {col} | Characters: {char_count} | Words: {word_count}")

text_area.bind("<KeyRelease>", update_status)
text_area.bind("<ButtonRelease>", update_status)

# Keyboard shortcuts
def handle_shortcuts(event):
    if event.state & 0x4:  # Ctrl key
        if event.keysym == 'n':
            new_file()
        elif event.keysym == 'o':
            open_file()
        elif event.keysym == 's':
            save_file()
        elif event.keysym == 'q':
            exit_app()
        elif event.keysym == 'f':
            find_text()
        elif event.keysym == 'plus':
            zoom_in()
        elif event.keysym == 'minus':
            zoom_out()

root.bind("<Control-Key>", handle_shortcuts)

# Initialize
update_title()
update_status()

root.mainloop()