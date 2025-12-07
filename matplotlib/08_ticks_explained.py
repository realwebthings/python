import matplotlib.pyplot as plt
import numpy as np

print("="*60)
print("MATPLOTLIB TICKS EXPLAINED")
print("="*60)

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create subplots to show different tick examples
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Understanding plt.xticks() and plt.yticks()', fontsize=16, fontweight='bold')

# 1. Default ticks (no customization)
axes[0, 0].plot(x, y)
axes[0, 0].set_title('1. Default Ticks')
axes[0, 0].grid(True, alpha=0.3)

# 2. Custom tick positions
axes[0, 1].plot(x, y)
axes[0, 1].set_xticks([0, 2, 4, 6, 8, 10])  # Set specific positions
axes[0, 1].set_yticks([-1, -0.5, 0, 0.5, 1])
axes[0, 1].set_title('2. Custom Tick Positions')
axes[0, 1].grid(True, alpha=0.3)

# 3. Custom tick labels
axes[1, 0].plot(x, y)
axes[1, 0].set_xticks([0, 2, 4, 6, 8, 10])
axes[1, 0].set_xticklabels(['Zero', 'Two', 'Four', 'Six', 'Eight', 'Ten'])
axes[1, 0].set_title('3. Custom Tick Labels')
axes[1, 0].grid(True, alpha=0.3)

# 4. Rotated and styled ticks
axes[1, 1].plot(x, y)
axes[1, 1].set_xticks([0, 2, 4, 6, 8, 10])
axes[1, 1].set_xticklabels(['Start', 'Q1', 'Q2', 'Q3', 'Q4', 'End'], 
                           rotation=45, fontsize=10, color='red')
axes[1, 1].set_title('4. Rotated & Styled Ticks')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("TICKS REFERENCE")
print("="*60)

print("""
WHAT ARE TICKS?
===============
Ticks are the marks and numbers on the X and Y axes.

Example X-axis: 0----2----4----6----8----10
                ↑    ↑    ↑    ↑    ↑    ↑
              Ticks (marks + labels)

BASIC USAGE:
============

1. SET TICK POSITIONS:
   plt.xticks([0, 2, 4, 6, 8, 10])
   plt.yticks([-1, 0, 1])

2. SET TICK LABELS:
   plt.xticks([0, 5, 10], ['Start', 'Middle', 'End'])
   
3. ROTATE LABELS:
   plt.xticks(rotation=45)
   
4. STYLE LABELS:
   plt.xticks(fontsize=12, color='red')

USING SUBPLOTS (axes):
======================
   ax.set_xticks([0, 2, 4, 6])           # Set positions
   ax.set_xticklabels(['A', 'B', 'C', 'D'])  # Set labels
   ax.set_yticks([0, 0.5, 1])
   
COMMON PARAMETERS:
==================
   ticks      - List of tick positions
   labels     - List of tick labels
   rotation   - Rotate labels (degrees)
   fontsize   - Label font size
   color      - Label color
   fontweight - 'normal', 'bold'

EXAMPLES:
=========

# Every 2 units
plt.xticks(np.arange(0, 11, 2))

# Custom labels
plt.xticks([0, 5, 10], ['Low', 'Medium', 'High'])

# Rotated 45 degrees
plt.xticks(rotation=45)

# Styled
plt.xticks(fontsize=14, color='blue', fontweight='bold')

# Hide ticks
plt.xticks([])  # Empty list = no ticks

# Pi multiples
plt.xticks([0, np.pi, 2*np.pi], ['0', 'π', '2π'])

WHY USE TICKS?
==============
✓ Make axes more readable
✓ Show specific important values
✓ Use custom labels (words instead of numbers)
✓ Control spacing between marks
✓ Improve plot clarity
""")

# Additional example with plt.xticks() and plt.yticks()
print("\n" + "="*60)
print("PRACTICAL EXAMPLE")
print("="*60)

plt.figure(figsize=(10, 6))
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y, linewidth=2)
plt.title('Sine Wave with Custom Ticks', fontsize=16)
plt.xlabel('Angle (radians)', fontsize=12)
plt.ylabel('sin(x)', fontsize=12)

# Custom X ticks at pi intervals
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           ['0', 'π/2', 'π', '3π/2', '2π'],
           fontsize=12)

# Custom Y ticks
plt.yticks([-1, -0.5, 0, 0.5, 1],
           ['-1', '-0.5', '0', '0.5', '1'],
           fontsize=12)

plt.grid(True, alpha=0.3)
plt.show()

print("\nTicks customized: X-axis shows π multiples, Y-axis shows decimal values")
