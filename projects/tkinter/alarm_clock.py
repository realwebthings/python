#!/usr/bin/env python3
"""
Alarm Clock with Music
Features: Set alarm time, plays music when alarm goes off, snooze function
"""

import datetime
import time
import pygame
import threading
from tkinter import *
from tkinter import messagebox, filedialog
import os

class AlarmClock:
    def __init__(self):
        self.root = Tk()
        self.root.title("🔔 Alarm Clock with Music")
        self.root.geometry("400x500")
        self.root.configure(bg="#2c3e50")
        
        # Variables
        self.alarm_time = None
        self.alarm_active = False
        self.music_file = None
        self.snooze_minutes = 5
        
        # Initialize pygame mixer (with error handling)
        try:
            pygame.mixer.init()
            self.has_pygame = True
        except:
            self.has_pygame = False
            print("⚠️  Pygame mixer not available, using system beep")
        
        self.setup_ui()
        self.update_clock()
        
    def setup_ui(self):
        """Create the user interface"""
        
        # Title
        title = Label(self.root, text="🔔 ALARM CLOCK", 
                     font=("Arial", 20, "bold"), 
                     bg="#2c3e50", fg="#ecf0f1")
        title.pack(pady=10)
        
        # Current time display
        self.time_label = Label(self.root, text="", 
                               font=("Digital-7", 24, "bold"), 
                               bg="#2c3e50", fg="#e74c3c")
        self.time_label.pack(pady=10)
        
        # Alarm time setting
        alarm_frame = Frame(self.root, bg="#2c3e50")
        alarm_frame.pack(pady=20)
        
        Label(alarm_frame, text="Set Alarm Time:", 
              font=("Arial", 12), bg="#2c3e50", fg="#ecf0f1").pack()
        
        time_frame = Frame(alarm_frame, bg="#2c3e50")
        time_frame.pack(pady=10)
        
        # Hour
        Label(time_frame, text="Hour:", bg="#2c3e50", fg="#ecf0f1").grid(row=0, column=0, padx=5)
        self.hour_var = StringVar(value="07")
        hour_spin = Spinbox(time_frame, from_=0, to=23, width=5, 
                           textvariable=self.hour_var, format="%02.0f")
        hour_spin.grid(row=0, column=1, padx=5)
        
        # Minute
        Label(time_frame, text="Minute:", bg="#2c3e50", fg="#ecf0f1").grid(row=0, column=2, padx=5)
        self.minute_var = StringVar(value="00")
        minute_spin = Spinbox(time_frame, from_=0, to=59, width=5, 
                             textvariable=self.minute_var, format="%02.0f")
        minute_spin.grid(row=0, column=3, padx=5)
        
        # Music selection
        music_frame = Frame(self.root, bg="#2c3e50")
        music_frame.pack(pady=20)
        
        Label(music_frame, text="🎵 Select Alarm Music:", 
              font=("Arial", 12), bg="#2c3e50", fg="#ecf0f1").pack()
        
        Button(music_frame, text="Browse Music File", 
               command=self.select_music, bg="#3498db", fg="white",
               font=("Arial", 10), width=20).pack(pady=5)
        
        self.music_label = Label(music_frame, text="No music selected", 
                                font=("Arial", 9), bg="#2c3e50", fg="#95a5a6")
        self.music_label.pack()
        
        # Control buttons
        button_frame = Frame(self.root, bg="#2c3e50")
        button_frame.pack(pady=20)
        
        self.set_button = Button(button_frame, text="⏰ Set Alarm", 
                                command=self.set_alarm, bg="#27ae60", fg="white",
                                font=("Arial", 12, "bold"), width=12)
        self.set_button.pack(pady=5)
        
        self.cancel_button = Button(button_frame, text="❌ Cancel Alarm", 
                                   command=self.cancel_alarm, bg="#e74c3c", fg="white",
                                   font=("Arial", 12, "bold"), width=12)
        self.cancel_button.pack(pady=5)
        
        # Alarm status
        self.status_label = Label(self.root, text="No alarm set", 
                                 font=("Arial", 11), bg="#2c3e50", fg="#f39c12")
        self.status_label.pack(pady=10)
        
        # Snooze setting
        snooze_frame = Frame(self.root, bg="#2c3e50")
        snooze_frame.pack(pady=10)
        
        Label(snooze_frame, text="Snooze (minutes):", 
              bg="#2c3e50", fg="#ecf0f1").pack(side=LEFT)
        self.snooze_var = StringVar(value="5")
        snooze_spin = Spinbox(snooze_frame, from_=1, to=30, width=5, 
                             textvariable=self.snooze_var)
        snooze_spin.pack(side=LEFT, padx=5)
    
    def play_system_beep(self):
        """Play system beep as fallback"""
        import platform
        try:
            system = platform.system()
            if system == "Darwin":  # macOS
                os.system("say 'Wake up! Alarm!' &")
            else:
                # Fallback to terminal beep
                for _ in range(5):
                    print("\a", end="", flush=True)
                    import time
                    time.sleep(0.3)
        except:
            # Ultimate fallback
            for _ in range(10):
                print("\a", end="", flush=True)
    
    def update_clock(self):
        """Update the current time display"""
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        
        # Check if alarm should go off
        if self.alarm_active and self.alarm_time:
            now = datetime.datetime.now().strftime("%H:%M")
            if now == self.alarm_time:
                self.trigger_alarm()
        
        # Update every second
        self.root.after(1000, self.update_clock)
    
    def select_music(self):
        """Select music file for alarm"""
        file_path = filedialog.askopenfilename(
            title="Select Alarm Music",
            filetypes=[
                ("Audio Files", "*.mp3 *.wav *.ogg"),
                ("MP3 Files", "*.mp3"),
                ("WAV Files", "*.wav"),
                ("All Files", "*.*")
            ]
        )
        
        if file_path:
            self.music_file = file_path
            filename = os.path.basename(file_path)
            self.music_label.config(text=f"🎵 {filename}")
    
    def set_alarm(self):
        """Set the alarm"""
        try:
            hour = int(self.hour_var.get())
            minute = int(self.minute_var.get())
            
            self.alarm_time = f"{hour:02d}:{minute:02d}"
            self.alarm_active = True
            self.snooze_minutes = int(self.snooze_var.get())
            
            self.status_label.config(text=f"⏰ Alarm set for {self.alarm_time}", fg="#27ae60")
            self.set_button.config(text="✅ Alarm Set", state="disabled")
            
            messagebox.showinfo("Alarm Set", f"Alarm set for {self.alarm_time}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid time values")
    
    def cancel_alarm(self):
        """Cancel the alarm"""
        self.alarm_active = False
        self.alarm_time = None
        self.status_label.config(text="No alarm set", fg="#f39c12")
        self.set_button.config(text="⏰ Set Alarm", state="normal")
        
        # Stop music if playing
        if self.has_pygame:
            try:
                pygame.mixer.music.stop()
            except:
                pass
        
        messagebox.showinfo("Alarm Cancelled", "Alarm has been cancelled")
    
    def trigger_alarm(self):
        """Trigger the alarm"""
        self.alarm_active = False  # Prevent multiple triggers
        
        # Play music
        if self.has_pygame and self.music_file and os.path.exists(self.music_file):
            try:
                pygame.mixer.music.load(self.music_file)
                pygame.mixer.music.play(-1)  # Loop indefinitely
            except:
                self.play_system_beep()
        else:
            self.play_system_beep()
        
        # Show alarm dialog
        self.show_alarm_dialog()
    
    def show_alarm_dialog(self):
        """Show alarm notification dialog"""
        alarm_window = Toplevel(self.root)
        alarm_window.title("🔔 ALARM!")
        alarm_window.geometry("300x200")
        alarm_window.configure(bg="#e74c3c")
        alarm_window.attributes("-topmost", True)
        
        # Center the window
        alarm_window.transient(self.root)
        alarm_window.grab_set()
        
        Label(alarm_window, text="⏰ ALARM!", 
              font=("Arial", 24, "bold"), 
              bg="#e74c3c", fg="white").pack(pady=20)
        
        Label(alarm_window, text=f"Time: {datetime.datetime.now().strftime('%H:%M:%S')}", 
              font=("Arial", 14), 
              bg="#e74c3c", fg="white").pack(pady=10)
        
        button_frame = Frame(alarm_window, bg="#e74c3c")
        button_frame.pack(pady=20)
        
        def stop_alarm():
            if self.has_pygame:
                try:
                    pygame.mixer.music.stop()
                except:
                    pass
            alarm_window.destroy()
            self.status_label.config(text="Alarm stopped", fg="#95a5a6")
        
        def snooze_alarm():
            if self.has_pygame:
                try:
                    pygame.mixer.music.stop()
                except:
                    pass
            alarm_window.destroy()
            
            # Set new alarm time (current time + snooze minutes)
            now = datetime.datetime.now()
            snooze_time = now + datetime.timedelta(minutes=self.snooze_minutes)
            self.alarm_time = snooze_time.strftime("%H:%M")
            self.alarm_active = True
            
            self.status_label.config(text=f"😴 Snoozed until {self.alarm_time}", fg="#f39c12")
        
        Button(button_frame, text="⏹️ Stop", command=stop_alarm,
               bg="#c0392b", fg="white", font=("Arial", 12, "bold"), width=8).pack(side=LEFT, padx=5)
        
        Button(button_frame, text="😴 Snooze", command=snooze_alarm,
               bg="#f39c12", fg="white", font=("Arial", 12, "bold"), width=8).pack(side=LEFT, padx=5)
    
    def run(self):
        """Start the alarm clock"""
        self.root.mainloop()

def main():
    """Create and run the alarm clock"""
    print("🔔 Starting Alarm Clock...")
    
    # Create sample alarm sound if no music file exists
    def create_sample_beep():
        """Create a simple beep sound file"""
        import numpy as np
        import wave
        
        # Generate a simple beep
        sample_rate = 44100
        duration = 1.0
        frequency = 800
        
        t = np.linspace(0, duration, int(sample_rate * duration))
        beep = np.sin(2 * np.pi * frequency * t) * 0.3
        
        # Convert to 16-bit integers
        beep_int = (beep * 32767).astype(np.int16)
        
        # Save as WAV file
        with wave.open("alarm_beep.wav", "w") as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(sample_rate)
            wav_file.writeframes(beep_int.tobytes())
    
    # Create sample beep if needed
    if not os.path.exists("alarm_beep.wav"):
        try:
            create_sample_beep()
            print("✅ Created sample alarm sound")
        except ImportError:
            print("⚠️  numpy not available, will use system beep")
    
    # Start the alarm clock
    alarm = AlarmClock()
    alarm.run()

if __name__ == "__main__":
    main()