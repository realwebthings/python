import matplotlib.pyplot as plt
import numpy as np

print("="*60)
print("LABELS vs TICKS - Understanding the Difference")
print("="*60)

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(12, 8))
plt.plot(x, y, linewidth=3, color='blue')

# LABELS - Describe what the axis represents
plt.xlabel('Time (seconds)', fontsize=16, color='red', fontweight='bold')
plt.ylabel('Amplitude', fontsize=16, color='red', fontweight='bold')
plt.title('Sine Wave Over Time', fontsize=20, color='darkblue', fontweight='bold')

# TICKS - The actual numbers on the axis
plt.xticks([0, 2, 4, 6, 8, 10], 
           fontsize=14, color='green', fontweight='bold')
plt.yticks([-1, -0.5, 0, 0.5, 1],
           fontsize=14, color='green', fontweight='bold')

# Add annotations to show the difference
plt.text(5, 1.3, 'TITLE (describes the plot)', 
         fontsize=12, ha='center', color='darkblue',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

plt.text(-2, 0, 'Y-AXIS\nLABEL\n(describes\nwhat Y is)', 
         fontsize=10, ha='center', color='red', rotation=90,
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))

plt.text(5, -1.5, 'X-AXIS LABEL (describes what X is)', 
         fontsize=10, ha='center', color='red',
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))

plt.text(-1.5, -0.5, 'Y-TICKS\n(numbers)', 
         fontsize=9, ha='center', color='green',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

plt.text(5, -1.8, 'X-TICKS (numbers)', 
         fontsize=9, ha='center', color='green',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("SUMMARY: LABELS vs TICKS")
print("="*60)

print("""
┌─────────────────────────────────────────────────────────┐
│                    TITLE                                │
│              "Sine Wave Over Time"                      │
│                                                         │
│  Y-LABEL    1.0  ←─ Y-TICK                             │
│    ↓        0.5  ←─ Y-TICK                             │
│ "Amplitude" 0.0  ←─ Y-TICK                             │
│            -0.5  ←─ Y-TICK                             │
│            -1.0  ←─ Y-TICK                             │
│              |                                          │
│              └──────────────────────                    │
│                0   2   4   6   8   10                   │
│                ↑   ↑   ↑   ↑   ↑   ↑                    │
│              X-TICKS (numbers)                          │
│                                                         │
│              X-LABEL: "Time (seconds)"                  │
└─────────────────────────────────────────────────────────┘

LABELS:
=======
• plt.xlabel('Time (seconds)')  ← Describes X-axis
• plt.ylabel('Amplitude')       ← Describes Y-axis  
• plt.title('Sine Wave')        ← Describes plot
• Purpose: Tell WHAT the data represents
• Location: Outside the plot area

TICKS:
======
• plt.xticks([0, 2, 4, 6, 8, 10])  ← Numbers on X-axis
• plt.yticks([-1, 0, 1])           ← Numbers on Y-axis
• Purpose: Show SCALE/VALUES
• Location: Along the axis line

ANALOGY:
========
Think of a thermometer:
• LABEL: "Temperature (°C)" ← What it measures
• TICKS: 0, 10, 20, 30, 40  ← The scale marks

BOTH ARE NEEDED:
================
✓ LABELS tell you what you're looking at
✓ TICKS tell you the specific values

Example:
--------
Without LABEL: You see numbers 0-10, but what do they mean?
Without TICKS: You know it's "Time", but what are the values?

TOGETHER: "Time (seconds)" with marks at 0, 2, 4, 6, 8, 10
          Now you know WHAT (time) and the VALUES (0-10 seconds)!
""")

print("\n" + "="*60)
print("CODE COMPARISON")
print("="*60)

print("""
# LABELS - Describe the axes
plt.xlabel('Temperature (°C)')     # What X represents
plt.ylabel('Pressure (Pa)')        # What Y represents
plt.title('Temperature vs Pressure') # What the plot shows

# TICKS - The scale values
plt.xticks([0, 20, 40, 60, 80, 100])  # Numbers on X-axis
plt.yticks([0, 50, 100, 150, 200])    # Numbers on Y-axis

# TICKS with custom labels
plt.xticks([1, 2, 3, 4], ['Q1', 'Q2', 'Q3', 'Q4'])  # Replace numbers with words
""")
