import tkinter as tk

# Listbox widget - scrollable list of items for selection
root = tk.Tk()
root.title("Listbox Widget")
root.geometry("400x350")

def on_select(event):
    selection = listbox.curselection()
    if selection:
        selected_item = listbox.get(selection[0])
        result_label.config(text=f"Selected: {selected_item}")

def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)

def remove_item():
    selection = listbox.curselection()
    if selection:
        listbox.delete(selection[0])
        result_label.config(text="")

# Create listbox
tk.Label(root, text="Select a fruit:", font=("Arial", 12)).pack(pady=5)

listbox = tk.Listbox(root,
                    height=8,
                    font=("Arial", 11),
                    bg="white",
                    selectbackground="lightblue")

# Add initial items
fruits = ["Apple", "Banana", "Orange", "Grape", "Mango", "Pineapple", "Strawberry"]
for fruit in fruits:
    listbox.insert(tk.END, fruit)

listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
listbox.bind("<<ListboxSelect>>", on_select)

# Add/Remove functionality
frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, font=("Arial", 11), width=15)
entry.pack(side=tk.LEFT, padx=5)

tk.Button(frame, text="Add", command=add_item, bg="lightgreen").pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Remove", command=remove_item, bg="lightcoral").pack(side=tk.LEFT, padx=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

root.mainloop()