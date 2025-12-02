import tkinter as tk
import time
import math

# Digital and Analog Clock
root = tk.Tk()
root.title("Clock Program")
root.geometry("600x500")

# Digital Clock
digital_frame = tk.Frame(root, bg="black", relief="raised", bd=3)
digital_frame.pack(pady=20, padx=20, fill=tk.X)

time_label = tk.Label(digital_frame, font=("Digital-7", 36, "bold"), 
                     bg="black", fg="lime", text="00:00:00")
time_label.pack(pady=10)

date_label = tk.Label(digital_frame, font=("Arial", 14), 
                     bg="black", fg="white", text="Monday, January 1, 2024")
date_label.pack(pady=5)

# Analog Clock
analog_frame = tk.Frame(root, relief="raised", bd=3)
analog_frame.pack(pady=20, padx=20)

tk.Label(analog_frame, text="Analog Clock", font=("Arial", 14, "bold")).pack(pady=5)

canvas = tk.Canvas(analog_frame, width=300, height=300, bg="white", relief="sunken", bd=2)
canvas.pack(pady=10)

def draw_clock_face():
    canvas.delete("all")
    
    # Clock circle
    canvas.create_oval(50, 50, 250, 250, outline="black", width=3)
    
    # Hour markers
    for i in range(12):
        angle = math.radians(i * 30 - 90)  # -90 to start from 12 o'clock
        x1 = 150 + 85 * math.cos(angle)
        y1 = 150 + 85 * math.sin(angle)
        x2 = 150 + 95 * math.cos(angle)
        y2 = 150 + 95 * math.sin(angle)
        canvas.create_line(x1, y1, x2, y2, width=3, fill="black")
        
        # Hour numbers
        num_x = 150 + 75 * math.cos(angle)
        num_y = 150 + 75 * math.sin(angle)
        hour = 12 if i == 0 else i
        canvas.create_text(num_x, num_y, text=str(hour), font=("Arial", 12, "bold"))
    
    # Minute markers
    for i in range(60):
        if i % 5 != 0:  # Skip hour markers
            angle = math.radians(i * 6 - 90)
            x1 = 150 + 90 * math.cos(angle)
            y1 = 150 + 90 * math.sin(angle)
            x2 = 150 + 95 * math.cos(angle)
            y2 = 150 + 95 * math.sin(angle)
            canvas.create_line(x1, y1, x2, y2, width=1, fill="gray")

def draw_hands(hours, minutes, seconds):
    # Clear previous hands
    canvas.delete("hands")
    
    # Hour hand
    hour_angle = math.radians((hours % 12) * 30 + minutes * 0.5 - 90)
    hour_x = 150 + 50 * math.cos(hour_angle)
    hour_y = 150 + 50 * math.sin(hour_angle)
    canvas.create_line(150, 150, hour_x, hour_y, width=6, fill="black", tags="hands")
    
    # Minute hand
    minute_angle = math.radians(minutes * 6 - 90)
    minute_x = 150 + 70 * math.cos(minute_angle)
    minute_y = 150 + 70 * math.sin(minute_angle)
    canvas.create_line(150, 150, minute_x, minute_y, width=4, fill="blue", tags="hands")
    
    # Second hand
    second_angle = math.radians(seconds * 6 - 90)
    second_x = 150 + 80 * math.cos(second_angle)
    second_y = 150 + 80 * math.sin(second_angle)
    canvas.create_line(150, 150, second_x, second_y, width=2, fill="red", tags="hands")
    
    # Center dot
    canvas.create_oval(145, 145, 155, 155, fill="black", tags="hands")

def update_clock():
    current_time = time.localtime()
    
    # Digital clock
    time_str = time.strftime("%H:%M:%S", current_time)
    date_str = time.strftime("%A, %B %d, %Y", current_time)
    
    time_label.config(text=time_str)
    date_label.config(text=date_str)
    
    # Analog clock
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    draw_hands(hours, minutes, seconds)
    
    # Schedule next update
    root.after(1000, update_clock)

# Timezone display
tz_frame = tk.Frame(root)
tz_frame.pack(pady=10)

def show_timezone(tz_name, offset_hours):
    import datetime
    utc_time = datetime.datetime.now(datetime.timezone.utc)
    local_time = utc_time + datetime.timedelta(hours=offset_hours)
    return local_time.strftime("%H:%M:%S")

# World clocks
world_frame = tk.Frame(root, relief="raised", bd=2)
world_frame.pack(pady=10, padx=20, fill=tk.X)

tk.Label(world_frame, text="World Clocks", font=("Arial", 12, "bold")).pack(pady=5)

world_clocks_frame = tk.Frame(world_frame)
world_clocks_frame.pack()

# World time labels
ny_label = tk.Label(world_clocks_frame, text="New York: --:--:--", font=("Arial", 10))
ny_label.grid(row=0, column=0, padx=10, pady=2)

london_label = tk.Label(world_clocks_frame, text="London: --:--:--", font=("Arial", 10))
london_label.grid(row=0, column=1, padx=10, pady=2)

tokyo_label = tk.Label(world_clocks_frame, text="Tokyo: --:--:--", font=("Arial", 10))
tokyo_label.grid(row=1, column=0, padx=10, pady=2)

sydney_label = tk.Label(world_clocks_frame, text="Sydney: --:--:--", font=("Arial", 10))
sydney_label.grid(row=1, column=1, padx=10, pady=2)

def update_world_clocks():
    import datetime
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    
    # Calculate times for different timezones (simplified)
    ny_time = (utc_now + datetime.timedelta(hours=-5)).strftime("%H:%M:%S")
    london_time = (utc_now + datetime.timedelta(hours=0)).strftime("%H:%M:%S")
    tokyo_time = (utc_now + datetime.timedelta(hours=9)).strftime("%H:%M:%S")
    sydney_time = (utc_now + datetime.timedelta(hours=11)).strftime("%H:%M:%S")
    
    ny_label.config(text=f"New York: {ny_time}")
    london_label.config(text=f"London: {london_time}")
    tokyo_label.config(text=f"Tokyo: {tokyo_time}")
    sydney_label.config(text=f"Sydney: {sydney_time}")
    
    root.after(1000, update_world_clocks)

# Control buttons
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

def toggle_format():
    current = time_label.cget("text")
    if ":" in current and len(current.split(":")[0]) == 2:
        # Switch to 12-hour format
        time_label.config(text=time.strftime("%I:%M:%S %p"))
    else:
        # Switch to 24-hour format
        time_label.config(text=time.strftime("%H:%M:%S"))

tk.Button(control_frame, text="Toggle 12/24 Hour", command=toggle_format, bg="lightblue").pack(side=tk.LEFT, padx=5)

# Stopwatch
stopwatch_frame = tk.Frame(root, relief="raised", bd=2)
stopwatch_frame.pack(pady=10, padx=20, fill=tk.X)

tk.Label(stopwatch_frame, text="Stopwatch", font=("Arial", 12, "bold")).pack(pady=5)

stopwatch_time = 0
stopwatch_running = False

stopwatch_label = tk.Label(stopwatch_frame, text="00:00:00", font=("Arial", 16, "bold"), fg="red")
stopwatch_label.pack(pady=5)

def update_stopwatch():
    global stopwatch_time
    if stopwatch_running:
        stopwatch_time += 1
        minutes = stopwatch_time // 60
        seconds = stopwatch_time % 60
        hours = minutes // 60
        minutes = minutes % 60
        stopwatch_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        root.after(1000, update_stopwatch)

def start_stopwatch():
    global stopwatch_running
    stopwatch_running = True
    update_stopwatch()

def stop_stopwatch():
    global stopwatch_running
    stopwatch_running = False

def reset_stopwatch():
    global stopwatch_time, stopwatch_running
    stopwatch_running = False
    stopwatch_time = 0
    stopwatch_label.config(text="00:00:00")

stopwatch_controls = tk.Frame(stopwatch_frame)
stopwatch_controls.pack(pady=5)

tk.Button(stopwatch_controls, text="Start", command=start_stopwatch, bg="lightgreen").pack(side=tk.LEFT, padx=2)
tk.Button(stopwatch_controls, text="Stop", command=stop_stopwatch, bg="lightcoral").pack(side=tk.LEFT, padx=2)
tk.Button(stopwatch_controls, text="Reset", command=reset_stopwatch, bg="lightyellow").pack(side=tk.LEFT, padx=2)

# Initialize
draw_clock_face()
update_clock()
update_world_clocks()

root.mainloop()