import matplotlib.pyplot as plt
import numpy as np

print("="*60)
print("SUBPLOTS IN MATPLOTLIB")
print("="*60)

print("\n" + "="*60)
print("METHOD 1: plt.subplots() - RECOMMENDED")
print("="*60)

# Create 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('2x2 Subplots Grid', fontsize=16, fontweight='bold')

x = np.linspace(0, 10, 100)

# Plot 1 (top-left)
axes[0, 0].plot(x, np.sin(x), 'r-')
axes[0, 0].set_title('Sine Wave')
axes[0, 0].grid(True, alpha=0.3)

# Plot 2 (top-right)
axes[0, 1].plot(x, np.cos(x), 'b-')
axes[0, 1].set_title('Cosine Wave')
axes[0, 1].grid(True, alpha=0.3)

# Plot 3 (bottom-left)
axes[1, 0].plot(x, np.tan(x), 'g-')
axes[1, 0].set_title('Tangent Wave')
axes[1, 0].set_ylim(-5, 5)
axes[1, 0].grid(True, alpha=0.3)

# Plot 4 (bottom-right)
axes[1, 1].plot(x, np.exp(-x/5), 'm-')
axes[1, 1].set_title('Exponential Decay')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("""
BASIC SUBPLOTS:
===============

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
                          ↑  ↑
                       rows cols

# Access individual plots:
axes[0, 0].plot(x, y)  # Top-left
axes[0, 1].plot(x, y)  # Top-right
axes[1, 0].plot(x, y)  # Bottom-left
axes[1, 1].plot(x, y)  # Bottom-right
""")

print("\n" + "="*60)
print("SINGLE ROW OR COLUMN")
print("="*60)

# Single row (1x3)
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle('1x3 Subplots (Single Row)', fontsize=16, fontweight='bold')

x = np.linspace(0, 10, 100)

axes[0].plot(x, x**2, 'r-')
axes[0].set_title('x²')
axes[0].grid(True, alpha=0.3)

axes[1].plot(x, x**3, 'b-')
axes[1].set_title('x³')
axes[1].grid(True, alpha=0.3)

axes[2].plot(x, np.sqrt(x), 'g-')
axes[2].set_title('√x')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("""
SINGLE ROW:
===========
fig, axes = plt.subplots(1, 3)  # 1 row, 3 columns

# Access with single index:
axes[0].plot(x, y)  # First plot
axes[1].plot(x, y)  # Second plot
axes[2].plot(x, y)  # Third plot
""")

# Single column (3x1)
fig, axes = plt.subplots(3, 1, figsize=(8, 10))
fig.suptitle('3x1 Subplots (Single Column)', fontsize=16, fontweight='bold')

axes[0].plot(x, np.sin(x), 'r-')
axes[0].set_title('Sine')
axes[0].grid(True, alpha=0.3)

axes[1].plot(x, np.cos(x), 'b-')
axes[1].set_title('Cosine')
axes[1].grid(True, alpha=0.3)

axes[2].plot(x, np.sin(x) * np.cos(x), 'g-')
axes[2].set_title('Sin × Cos')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("""
SINGLE COLUMN:
==============
fig, axes = plt.subplots(3, 1)  # 3 rows, 1 column

axes[0].plot(x, y)  # Top plot
axes[1].plot(x, y)  # Middle plot
axes[2].plot(x, y)  # Bottom plot
""")

print("\n" + "="*60)
print("METHOD 2: plt.subplot() - ALTERNATIVE")
print("="*60)

plt.figure(figsize=(12, 8))

# Subplot 1
plt.subplot(2, 2, 1)  # (rows, cols, position)
plt.plot(x, np.sin(x), 'r-')
plt.title('Subplot 1')
plt.grid(True, alpha=0.3)

# Subplot 2
plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x), 'b-')
plt.title('Subplot 2')
plt.grid(True, alpha=0.3)

# Subplot 3
plt.subplot(2, 2, 3)
plt.plot(x, np.tan(x), 'g-')
plt.title('Subplot 3')
plt.ylim(-5, 5)
plt.grid(True, alpha=0.3)

# Subplot 4
plt.subplot(2, 2, 4)
plt.plot(x, x, 'm-')
plt.title('Subplot 4')
plt.grid(True, alpha=0.3)

plt.suptitle('Using plt.subplot()', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print("""
ALTERNATIVE METHOD:
===================
plt.subplot(2, 2, 1)  # (rows, cols, position)
plt.plot(x, y)

plt.subplot(2, 2, 2)
plt.plot(x, y)

Position numbering:
┌───┬───┐
│ 1 │ 2 │
├───┼───┤
│ 3 │ 4 │
└───┴───┘
""")

print("\n" + "="*60)
print("DIFFERENT PLOT TYPES IN SUBPLOTS")
print("="*60)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Different Plot Types', fontsize=16, fontweight='bold')

# Line plot
x = np.linspace(0, 10, 100)
axes[0, 0].plot(x, np.sin(x), 'b-', linewidth=2)
axes[0, 0].set_title('Line Plot')
axes[0, 0].grid(True, alpha=0.3)

# Scatter plot
x_scatter = np.random.rand(50) * 10
y_scatter = np.random.rand(50) * 10
axes[0, 1].scatter(x_scatter, y_scatter, c='red', s=50, alpha=0.6)
axes[0, 1].set_title('Scatter Plot')
axes[0, 1].grid(True, alpha=0.3)

# Bar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]
axes[1, 0].bar(categories, values, color='green')
axes[1, 0].set_title('Bar Chart')
axes[1, 0].grid(True, alpha=0.3, axis='y')

# Histogram
data = np.random.randn(1000)
axes[1, 1].hist(data, bins=30, color='purple', alpha=0.7, edgecolor='black')
axes[1, 1].set_title('Histogram')
axes[1, 1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

print("""
MIX DIFFERENT PLOT TYPES:
==========================
fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(x, y)        # Line plot
axes[0, 1].scatter(x, y)     # Scatter plot
axes[1, 0].bar(x, y)         # Bar chart
axes[1, 1].hist(data)        # Histogram
""")

print("\n" + "="*60)
print("SHARING AXES")
print("="*60)

# Share X axis
fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
fig.suptitle('Shared X Axis', fontsize=16, fontweight='bold')

x = np.linspace(0, 10, 100)

axes[0].plot(x, np.sin(x), 'r-')
axes[0].set_ylabel('sin(x)')
axes[0].grid(True, alpha=0.3)

axes[1].plot(x, np.cos(x), 'b-')
axes[1].set_ylabel('cos(x)')
axes[1].grid(True, alpha=0.3)

axes[2].plot(x, np.tan(x), 'g-')
axes[2].set_ylabel('tan(x)')
axes[2].set_xlabel('x')
axes[2].set_ylim(-5, 5)
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("""
SHARED AXES:
============
# Share X axis (same X range for all)
fig, axes = plt.subplots(3, 1, sharex=True)

# Share Y axis (same Y range for all)
fig, axes = plt.subplots(1, 3, sharey=True)

# Share both
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
""")

print("\n" + "="*60)
print("SUBPLOT SUMMARY")
print("="*60)

print("""
CREATING SUBPLOTS:
==================

METHOD 1 (Recommended):
fig, axes = plt.subplots(rows, cols, figsize=(width, height))
axes[row, col].plot(x, y)

METHOD 2 (Alternative):
plt.subplot(rows, cols, position)
plt.plot(x, y)

ACCESSING SUBPLOTS:
===================
2D Grid (2x2):
  axes[0, 0]  axes[0, 1]
  axes[1, 0]  axes[1, 1]

Single Row (1x3):
  axes[0]  axes[1]  axes[2]

Single Column (3x1):
  axes[0]
  axes[1]
  axes[2]

COMMON PARAMETERS:
==================
nrows, ncols  - Grid dimensions
figsize       - Figure size (width, height)
sharex        - Share X axis
sharey        - Share Y axis
subplot_kw    - Dict of subplot parameters
gridspec_kw   - Dict for grid spacing

USEFUL FUNCTIONS:
=================
fig.suptitle()     - Overall title
plt.tight_layout() - Auto-adjust spacing
axes.flatten()     - Convert 2D to 1D array
axes.flat          - Iterate over all axes

TIPS:
=====
• Use plt.subplots() (plural) not plt.subplot()
• Always use plt.tight_layout() for better spacing
• Use sharex/sharey for comparing data
• figsize=(width, height) in inches
• Access: axes[row, col] for 2D, axes[i] for 1D
• Use fig.suptitle() for overall title
• Each subplot is independent (own labels, grid, etc.)

EXAMPLES:
=========
# 2x3 grid
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Single row
fig, axes = plt.subplots(1, 4, figsize=(16, 4))

# Single column
fig, axes = plt.subplots(5, 1, figsize=(8, 15))

# Shared axes
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
""")
