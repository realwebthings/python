# Tkinter : Tkinter is a python binding to the Tk GUI toolkit. 
# It is the standard Python interface to the Tk GUI toolkit, 
# and is automatically installed on many system. 
# Python with tkinter is the fastest way to create the GUI applications. 
# Tkinter is a powerful GUI application programming interface which is available in all platforms.

# widgets = GUI elements : buttons, textboxes, labels, images
# windows = servers as container to hold or contain these widgets
 
import tkinter as tk
import os

root = tk.Tk()
root.title("My First GUI")
root.geometry("500x500")

# Optional: Set icon if file exists
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, 'icon.png')

try:
    icon = tk.PhotoImage(file=icon_path)
    # root.iconphoto(True, icon)
    root.iconbitmap(icon_path)
    root.config(bg="white")
    print(f"Icon loaded from: {icon_path}")
except tk.TclError:
    print(f"Icon file not found at: {icon_path}")
    print("Using default icon.")
except Exception as e:
    print(f"Error loading icon: {e}")
    print("Using default icon.")

root.mainloop()  # place window on computer screen, listen for events
