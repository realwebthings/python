import tkinter as tk
from tkinter import scrolledtext, messagebox
import subprocess
import threading

# PIP GUI - Package Manager Interface
root = tk.Tk()
root.title("PIP Package Manager")
root.geometry("700x600")

# Variables
current_process = None

# Header
header_frame = tk.Frame(root, bg="darkblue", height=60)
header_frame.pack(fill=tk.X)
header_frame.pack_propagate(False)

tk.Label(header_frame, text="PIP Package Manager", font=("Arial", 18, "bold"), 
         bg="darkblue", fg="white").pack(pady=15)

# Main content
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Package operations frame
ops_frame = tk.Frame(main_frame)
ops_frame.pack(fill=tk.X, pady=(0, 10))

# Install package
install_frame = tk.Frame(ops_frame, relief="raised", bd=1)
install_frame.pack(fill=tk.X, pady=5)

tk.Label(install_frame, text="Install Package:", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=5)

install_entry_frame = tk.Frame(install_frame)
install_entry_frame.pack(fill=tk.X, padx=5, pady=5)

install_entry = tk.Entry(install_entry_frame, font=("Arial", 11), width=40)
install_entry.pack(side=tk.LEFT, padx=(0, 10))

def install_package():
    package = install_entry.get().strip()
    if package:
        run_pip_command(f"install {package}")
        install_entry.delete(0, tk.END)

tk.Button(install_entry_frame, text="Install", command=install_package, 
         bg="lightgreen", font=("Arial", 10)).pack(side=tk.LEFT)

# Uninstall package
uninstall_frame = tk.Frame(ops_frame, relief="raised", bd=1)
uninstall_frame.pack(fill=tk.X, pady=5)

tk.Label(uninstall_frame, text="Uninstall Package:", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=5)

uninstall_entry_frame = tk.Frame(uninstall_frame)
uninstall_entry_frame.pack(fill=tk.X, padx=5, pady=5)

uninstall_entry = tk.Entry(uninstall_entry_frame, font=("Arial", 11), width=40)
uninstall_entry.pack(side=tk.LEFT, padx=(0, 10))

def uninstall_package():
    package = uninstall_entry.get().strip()
    if package:
        if messagebox.askyesno("Confirm", f"Uninstall {package}?"):
            run_pip_command(f"uninstall {package} -y")
            uninstall_entry.delete(0, tk.END)

tk.Button(uninstall_entry_frame, text="Uninstall", command=uninstall_package, 
         bg="lightcoral", font=("Arial", 10)).pack(side=tk.LEFT)

# Quick commands
quick_frame = tk.Frame(ops_frame, relief="raised", bd=1)
quick_frame.pack(fill=tk.X, pady=5)

tk.Label(quick_frame, text="Quick Commands:", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=5)

quick_buttons_frame = tk.Frame(quick_frame)
quick_buttons_frame.pack(fill=tk.X, padx=5, pady=5)

def list_packages():
    run_pip_command("list")

def list_outdated():
    run_pip_command("list --outdated")

def upgrade_pip():
    run_pip_command("install --upgrade pip")

def show_pip_version():
    run_pip_command("--version")

tk.Button(quick_buttons_frame, text="List Packages", command=list_packages, 
         bg="lightblue", width=12).pack(side=tk.LEFT, padx=2)
tk.Button(quick_buttons_frame, text="List Outdated", command=list_outdated, 
         bg="lightyellow", width=12).pack(side=tk.LEFT, padx=2)
tk.Button(quick_buttons_frame, text="Upgrade PIP", command=upgrade_pip, 
         bg="lightgreen", width=12).pack(side=tk.LEFT, padx=2)
tk.Button(quick_buttons_frame, text="PIP Version", command=show_pip_version, 
         bg="lightgray", width=12).pack(side=tk.LEFT, padx=2)

# Output area
output_frame = tk.Frame(main_frame)
output_frame.pack(fill=tk.BOTH, expand=True)

tk.Label(output_frame, text="Output:", font=("Arial", 12, "bold")).pack(anchor="w", pady=(0, 5))

output_text = scrolledtext.ScrolledText(output_frame, height=20, font=("Courier", 10), 
                                       bg="black", fg="white", wrap=tk.WORD)
output_text.pack(fill=tk.BOTH, expand=True)

# Status bar
status_frame = tk.Frame(root, relief="sunken", bd=1)
status_frame.pack(fill=tk.X, side=tk.BOTTOM)

status_label = tk.Label(status_frame, text="Ready", anchor="w", font=("Arial", 10))
status_label.pack(fill=tk.X, padx=5, pady=2)

def update_output(text):
    output_text.insert(tk.END, text)
    output_text.see(tk.END)
    root.update_idletasks()

def run_pip_command(command):
    global current_process
    
    if current_process and current_process.poll() is None:
        messagebox.showwarning("Warning", "Another command is already running!")
        return
    
    def execute_command():
        try:
            status_label.config(text=f"Running: pip {command}")
            output_text.delete("1.0", tk.END)
            update_output(f"$ pip {command}\n")
            update_output("-" * 50 + "\n")
            
            # Run pip command
            process = subprocess.Popen(
                ["pip"] + command.split(),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            global current_process
            current_process = process
            
            # Read output line by line
            for line in process.stdout:
                update_output(line)
            
            process.wait()
            
            if process.returncode == 0:
                update_output("\n✅ Command completed successfully!\n")
                status_label.config(text="Command completed successfully")
            else:
                update_output(f"\n❌ Command failed with return code {process.returncode}\n")
                status_label.config(text="Command failed")
                
        except FileNotFoundError:
            update_output("❌ Error: pip not found. Make sure Python and pip are installed.\n")
            status_label.config(text="Error: pip not found")
        except Exception as e:
            update_output(f"❌ Error: {str(e)}\n")
            status_label.config(text=f"Error: {str(e)}")
        finally:
            current_process = None
    
    # Run in separate thread to prevent GUI freezing
    thread = threading.Thread(target=execute_command)
    thread.daemon = True
    thread.start()

# Search packages
search_frame = tk.Frame(ops_frame, relief="raised", bd=1)
search_frame.pack(fill=tk.X, pady=5)

tk.Label(search_frame, text="Search Packages:", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=5)

search_entry_frame = tk.Frame(search_frame)
search_entry_frame.pack(fill=tk.X, padx=5, pady=5)

search_entry = tk.Entry(search_entry_frame, font=("Arial", 11), width=40)
search_entry.pack(side=tk.LEFT, padx=(0, 10))

def search_packages():
    query = search_entry.get().strip()
    if query:
        run_pip_command(f"search {query}")

tk.Button(search_entry_frame, text="Search", command=search_packages, 
         bg="lightcyan", font=("Arial", 10)).pack(side=tk.LEFT)

# Package info
info_frame = tk.Frame(ops_frame, relief="raised", bd=1)
info_frame.pack(fill=tk.X, pady=5)

tk.Label(info_frame, text="Package Information:", font=("Arial", 12, "bold")).pack(anchor="w", padx=5, pady=5)

info_entry_frame = tk.Frame(info_frame)
info_entry_frame.pack(fill=tk.X, padx=5, pady=5)

info_entry = tk.Entry(info_entry_frame, font=("Arial", 11), width=40)
info_entry.pack(side=tk.LEFT, padx=(0, 10))

def show_package_info():
    package = info_entry.get().strip()
    if package:
        run_pip_command(f"show {package}")

tk.Button(info_entry_frame, text="Show Info", command=show_package_info, 
         bg="lightpink", font=("Arial", 10)).pack(side=tk.LEFT)

# Control buttons
control_frame = tk.Frame(main_frame)
control_frame.pack(fill=tk.X, pady=10)

def clear_output():
    output_text.delete("1.0", tk.END)
    status_label.config(text="Output cleared")

def stop_command():
    global current_process
    if current_process and current_process.poll() is None:
        current_process.terminate()
        update_output("\n🛑 Command stopped by user\n")
        status_label.config(text="Command stopped")

tk.Button(control_frame, text="Clear Output", command=clear_output, 
         bg="lightyellow").pack(side=tk.LEFT, padx=5)
tk.Button(control_frame, text="Stop Command", command=stop_command, 
         bg="lightcoral").pack(side=tk.LEFT, padx=5)

# Keyboard shortcuts
def handle_shortcuts(event):
    if event.state & 0x4:  # Ctrl key
        if event.keysym == 'l':
            clear_output()

root.bind("<Control-Key>", handle_shortcuts)

# Initialize
output_text.insert("1.0", "PIP Package Manager Ready\n")
output_text.insert(tk.END, "Enter package names and use the buttons above to manage Python packages.\n")
output_text.insert(tk.END, "Commands will be executed in the background.\n\n")

root.mainloop()