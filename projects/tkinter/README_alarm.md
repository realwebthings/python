# 🔔 Alarm Clock with Music

Two versions of alarm clock applications with music support.

## Files:
- `alarm_clock.py` - Full GUI version with music selection
- `simple_alarm.py` - Command-line version

## Features:

### GUI Version (`alarm_clock.py`):
- ⏰ Set custom alarm time
- 🎵 Select custom music files (MP3, WAV, OGG)
- 😴 Snooze functionality
- 🕐 Real-time clock display
- 🎨 Modern dark theme UI
- ⏹️ Stop/Cancel alarm options

### Simple Version (`simple_alarm.py`):
- ⏰ Set alarm time via command line
- 🔔 System beep alarm sound
- ⏹️ Ctrl+C to stop alarm

## Usage:

### GUI Version:
```bash
python3 alarm_clock.py
```

1. Set alarm time using hour/minute spinboxes
2. Optionally select a music file
3. Click "Set Alarm"
4. When alarm goes off, choose Stop or Snooze

### Simple Version:
```bash
python3 simple_alarm.py
```

1. Enter alarm time in HH:MM format (24-hour)
2. Wait for alarm
3. Press Ctrl+C to stop

## Requirements:
- pygame (for music playback)
- tkinter (for GUI - usually included with Python)

## Installation:
```bash
# In your virtual environment
pip install pygame
```

## Music Files:
- Supports MP3, WAV, OGG formats
- Place music files anywhere and browse to select
- Falls back to system beep if no music selected

## Tips:
- Use short music files or they'll loop
- Test your music file first to ensure it works
- Set snooze time between 1-30 minutes
- GUI version stays on top when alarm triggers