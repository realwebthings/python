import matplotlib.pyplot as plt
import numpy as np

print("="*60)
print("plt.grid() EXPLAINED")
print("="*60)

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create subplots to show different grid options
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('plt.grid() Examples', fontsize=16, fontweight='bold')

# 1. No grid
axes[0, 0].plot(x, y, linewidth=2)
axes[0, 0].set_title('1. No Grid')

# 2. Basic grid
axes[0, 1].plot(x, y, linewidth=2)
axes[0, 1].grid(True)
axes[0, 1].set_title('2. Basic Grid: grid(True)')

# 3. Grid with transparency
axes[0, 2].plot(x, y, linewidth=2)
axes[0, 2].grid(True, alpha=0.3)
axes[0, 2].set_title('3. Transparent: grid(alpha=0.3)')

# 4. Styled grid
axes[1, 0].plot(x, y, linewidth=2)
axes[1, 0].grid(True, color='red', linestyle='--', linewidth=1)
axes[1, 0].set_title('4. Styled: color, linestyle, linewidth')

# 5. Grid on specific axis only
axes[1, 1].plot(x, y, linewidth=2)
axes[1, 1].grid(True, axis='x', alpha=0.5)
axes[1, 1].set_title('5. X-axis only: grid(axis="x")')

# 6. Different grid styles
axes[1, 2].plot(x, y, linewidth=2)
axes[1, 2].grid(True, which='major', color='gray', linestyle='-', linewidth=0.8)
axes[1, 2].grid(True, which='minor', color='lightgray', linestyle=':', linewidth=0.5)
axes[1, 2].minorticks_on()
axes[1, 2].set_title('6. Major + Minor grids')

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("WHAT IS plt.grid()?")
print("="*60)

print("""
plt.grid() adds grid lines to your plot

WITHOUT GRID:          WITH GRID:
    1.0                    1.0 ┼─────────────
    0.5                    0.5 ┼─────────────
    0.0  ∿∿∿∿              0.0 ┼─∿─∿─∿─∿─∿─∿─
   -0.5                   -0.5 ┼─────────────
   -1.0                   -1.0 ┼─────────────
        0  5  10               0  5  10

Grid lines help you read exact values from the plot!

BASIC USAGE:
============
plt.grid(True)   # Turn grid ON
plt.grid(False)  # Turn grid OFF
plt.grid()       # Toggle grid

COMMON PARAMETERS:
==================
visible    - True/False (show/hide grid)
alpha      - Transparency (0=invisible, 1=solid)
color      - Grid line color
linestyle  - Line style: '-', '--', '-.', ':'
linewidth  - Line thickness
axis       - 'both', 'x', 'y' (which axis)
which      - 'major', 'minor', 'both' (tick type)

EXAMPLES:
=========

# Basic grid
plt.grid(True)

# Transparent grid (recommended)
plt.grid(True, alpha=0.3)

# Styled grid
plt.grid(True, color='gray', linestyle='--', linewidth=0.5)

# X-axis only
plt.grid(True, axis='x')

# Y-axis only
plt.grid(True, axis='y')

# Dashed grid
plt.grid(True, linestyle='--')

# Dotted grid
plt.grid(True, linestyle=':')

# Colored grid
plt.grid(True, color='red', alpha=0.5)
""")

print("\n" + "="*60)
print("GRID LINE STYLES")
print("="*60)

print("""
LINESTYLE OPTIONS:
==================
'-'   or 'solid'     ────────  Solid line
'--'  or 'dashed'    ─ ─ ─ ─  Dashed line
'-.'  or 'dashdot'   ─·─·─·─  Dash-dot line
':'   or 'dotted'    ········  Dotted line

EXAMPLES:
plt.grid(True, linestyle='-')   # Solid
plt.grid(True, linestyle='--')  # Dashed
plt.grid(True, linestyle='-.')  # Dash-dot
plt.grid(True, linestyle=':')   # Dotted
""")

print("\n" + "="*60)
print("MAJOR vs MINOR GRIDS")
print("="*60)

print("""
MAJOR GRID: Lines at major tick marks (0, 2, 4, 6, 8, 10)
MINOR GRID: Lines at minor tick marks (1, 3, 5, 7, 9)

# Enable minor ticks first
plt.minorticks_on()

# Major grid (thick, solid)
plt.grid(True, which='major', color='gray', linestyle='-', linewidth=0.8)

# Minor grid (thin, dotted)
plt.grid(True, which='minor', color='lightgray', linestyle=':', linewidth=0.5)
""")

# Practical example
print("\n" + "="*60)
print("PRACTICAL EXAMPLE")
print("="*60)

plt.figure(figsize=(12, 6))

# Left plot - without grid
plt.subplot(1, 2, 1)
plt.plot(x, y, linewidth=2, color='blue')
plt.title('Without Grid - Hard to Read Values', fontsize=14)
plt.xlabel('X axis')
plt.ylabel('Y axis')

# Right plot - with grid
plt.subplot(1, 2, 2)
plt.plot(x, y, linewidth=2, color='blue')
plt.title('With Grid - Easy to Read Values', fontsize=14)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.7)

plt.tight_layout()
plt.show()

print("""
COMPARISON:
===========
Without grid: Hard to tell exact values
With grid:    Easy to see that peak is at y ≈ 1.0

WHEN TO USE GRID:
=================
✓ When you need to read exact values
✓ Scientific/technical plots
✓ Data analysis plots
✓ When precision matters

WHEN NOT TO USE:
================
✗ Presentation plots (can look cluttered)
✗ Simple plots with few data points
✗ When aesthetics > precision

BEST PRACTICES:
===============
• Use alpha=0.3 for subtle grid (recommended)
• Use dashed/dotted lines (less distracting)
• Match grid color to plot theme
• Don't make grid too prominent
• Consider using only major grid

RECOMMENDED SETTINGS:
=====================
plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.7)
                ↑         ↑              ↑
            Transparent  Dashed      Thin line
            
This creates a subtle, professional-looking grid!
""")
