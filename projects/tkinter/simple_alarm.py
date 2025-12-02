#!/usr/bin/env python3
"""
Simple Alarm Clock - Minimal version
"""

import datetime
import time
import pygame
import os

def play_alarm_sound():
    """Play alarm sound"""
    pygame.mixer.init()
    
    # Try to play a system sound or create a beep
    try:
        # Create a simple beep sound
        pygame.mixer.music.load("alarm_beep.wav") if os.path.exists("alarm_beep.wav") else None
        pygame.mixer.music.play(-1)  # Loop
        print("🔔 ALARM RINGING! Press Ctrl+C to stop")
        
        # Keep playing until user stops
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        print("\n⏹️  Alarm stopped!")
    except:
        # Fallback to system beep
        for _ in range(10):
            print("\a🔔 WAKE UP! 🔔")
            time.sleep(0.5)

def set_alarm():
    """Simple alarm setter"""
    print("🔔 Simple Alarm Clock")
    print("=" * 30)
    
    try:
        # Get alarm time
        alarm_time = input("Enter alarm time (HH:MM in 24-hour format): ")
        hour, minute = map(int, alarm_time.split(':'))
        
        # Validate time
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            print("❌ Invalid time format!")
            return
        
        print(f"⏰ Alarm set for {hour:02d}:{minute:02d}")
        print("💤 Waiting for alarm time...")
        
        # Wait for alarm time
        while True:
            now = datetime.datetime.now()
            current_time = f"{now.hour:02d}:{now.minute:02d}"
            
            print(f"\r🕐 Current time: {now.strftime('%H:%M:%S')}", end="", flush=True)
            
            if current_time == f"{hour:02d}:{minute:02d}":
                print(f"\n\n🔔 ALARM! It's {alarm_time}!")
                play_alarm_sound()
                break
                
            time.sleep(1)
            
    except ValueError:
        print("❌ Invalid time format! Use HH:MM")
    except KeyboardInterrupt:
        print("\n👋 Alarm cancelled!")

if __name__ == "__main__":
    set_alarm()