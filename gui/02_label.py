import tkinter as tk
# label = an area widget that holds text and/or an image within a window

root = tk.Tk()

# Load and resize image
try:
    original_image = tk.PhotoImage(file='/Users/mukeshkumar/MyRepo/python/concepts/icon.png')
    # Resize image to smaller size (subsample makes it smaller)
    image = original_image.subsample(2, 2)  # Makes image 1/4 the size
    print(f"Image loaded and resized: {image.width()}x{image.height()}")
except Exception as e:
    print(f"Error loading image: {e}")
    image = None

# Create label with text first (removed relief="raised" - it interferes with compound)
label = tk.Label(root, 
                text="Hello, Tkinter!", 
                font=("Arial", 18), 
                fg="blue", 
                bg="lightgray", 
                bd=2,  # Keep border but without raised relief
                padx=20, 
                pady=20)

# Add image if available
if image:
    label.config(image=image, compound="bottom")
    print("✅ Label created with BOTH text and image")
else:
    print("⚠️ Label created with text only")
# label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 24, 'bold'), fg="black", bg="white", relief="raised", bd=10, padx=16, pady=12)
root.title("My First GUI")
root.geometry("500x500")
root.config(bg="white")
# Pack the label widget into the window
label.pack()

root.mainloop()  # place window on computer screen, listen for events
