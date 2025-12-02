#!/usr/bin/env python3
"""
Alarm Clock without pygame - Uses system beep
"""

import datetime
import time
import os
import subprocess
import platform
from tkinter import *
from tkinter import messagebox

class AlarmClock:
    def __init__(self):
        self.root = Tk()
        self.root.title("🔔 Alarm Clock")
        self.root.geometry("350x400")
        self.root.configure(bg="#2c3e50")
        
        # Variables
        self.alarm_time = None
        self.alarm_active = False
        self.snooze_minutes = 5
        
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
                               font=("Arial", 24, "bold"), 
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
        
        messagebox.showinfo("Alarm Cancelled", "Alarm has been cancelled")
    
    def play_alarm_sound(self):
        """Play alarm sound using system methods"""
        try:
            system = platform.system()
            if system == "Darwin":  # macOS
                # Use text-to-speech as it's more reliable
                os.system("say 'Wake up! Alarm time!' &")
            elif system == "Windows":
                try:
                    import winsound
                    winsound.Beep(1000, 1000)  # 1000Hz for 1 second
                except ImportError:
                    self.fallback_beep()
            else:  # Linux
                os.system("echo -e '\a' &")
        except:
            self.fallback_beep()
    
    def fallback_beep(self):
        """Fallback beep method"""
        for _ in range(5):
            print("\a🔔 WAKE UP! 🔔")
            time.sleep(0.3)
    
    def trigger_alarm(self):
        """Trigger the alarm"""
        self.alarm_active = False  # Prevent multiple triggers
        
        # Play alarm sound
        self.play_alarm_sound()
        
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
            alarm_window.destroy()
            self.status_label.config(text="Alarm stopped", fg="#95a5a6")
        
        def snooze_alarm():
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
    alarm = AlarmClock()
    alarm.run()

if __name__ == "__main__":
    main()