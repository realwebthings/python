import matplotlib.pyplot as plt
import numpy as np

print("="*60)
print("SCATTER PLOTS IN MATPLOTLIB")
print("="*60)

# Create subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Scatter Plot Examples', fontsize=16, fontweight='bold')

# Sample data
x = np.random.rand(50) * 10
y = np.random.rand(50) * 10

# 1. Basic scatter plot
axes[0, 0].scatter(x, y)
axes[0, 0].set_title('1. Basic Scatter Plot')
axes[0, 0].grid(True, alpha=0.3)

# 2. Colored scatter plot
axes[0, 1].scatter(x, y, c='red')
axes[0, 1].set_title('2. Colored Points')
axes[0, 1].grid(True, alpha=0.3)

# 3. Different sizes
sizes = np.random.rand(50) * 200
axes[0, 2].scatter(x, y, s=sizes, alpha=0.5)
axes[0, 2].set_title('3. Variable Sizes')
axes[0, 2].grid(True, alpha=0.3)

# 4. Color by value
colors = y  # Color based on y values
axes[1, 0].scatter(x, y, c=colors, cmap='viridis', s=100)
axes[1, 0].set_title('4. Color by Value (colormap)')
axes[1, 0].grid(True, alpha=0.3)

# 5. With edge colors
axes[1, 1].scatter(x, y, s=100, c='lightblue', edgecolors='blue', linewidths=2)
axes[1, 1].set_title('5. With Edge Colors')
axes[1, 1].grid(True, alpha=0.3)

# 6. Different markers
axes[1, 2].scatter(x[:25], y[:25], marker='o', s=100, label='Circle')
axes[1, 2].scatter(x[25:], y[25:], marker='s', s=100, label='Square')
axes[1, 2].set_title('6. Different Markers')
axes[1, 2].legend()
axes[1, 2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("SCATTER PLOT BASICS")
print("="*60)

print("""
WHAT IS A SCATTER PLOT?
=======================
Shows individual data points as dots on X-Y axes.
Used to show relationships between two variables.

VISUAL:
    Y
    │     •
    │  •    •
    │    •     •
    │ •   •  •
    └──────────── X

BASIC USAGE:
============
plt.scatter(x, y)

COMMON PARAMETERS:
==================
x, y        - Data coordinates
s           - Size of points (default: 20)
c           - Color (single color or array)
marker      - Marker style ('o', 's', '^', etc.)
alpha       - Transparency (0-1)
cmap        - Colormap for color array
edgecolors  - Edge color of points
linewidths  - Edge width
label       - Legend label

EXAMPLES:
=========

# Basic scatter
x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 5, 6]
plt.scatter(x, y)

# Colored points
plt.scatter(x, y, c='red')

# Larger points
plt.scatter(x, y, s=100)

# Variable sizes
sizes = [20, 50, 100, 150, 200]
plt.scatter(x, y, s=sizes)

# Color by value
colors = [1, 2, 3, 4, 5]
plt.scatter(x, y, c=colors, cmap='viridis')

# With edges
plt.scatter(x, y, c='lightblue', edgecolors='blue', linewidths=2)

# Transparent
plt.scatter(x, y, alpha=0.5)

# Different marker
plt.scatter(x, y, marker='s')  # Square
""")

print("\n" + "="*60)
print("SCATTER WITH COLORBAR")
print("="*60)

# Scatter with colorbar
plt.figure(figsize=(10, 6))
x = np.random.rand(100) * 10
y = np.random.rand(100) * 10
colors = x + y  # Color based on sum

scatter = plt.scatter(x, y, c=colors, cmap='plasma', s=100, alpha=0.6, edgecolors='black')
plt.colorbar(scatter, label='X + Y Value')
plt.xlabel('X axis', fontsize=12)
plt.ylabel('Y axis', fontsize=12)
plt.title('Scatter Plot with Colorbar', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("""
ADD COLORBAR:

scatter = plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar(scatter, label='Value')
""")

print("\n" + "="*60)
print("SCATTER WITH TREND LINE")
print("="*60)

# Scatter with trend line
plt.figure(figsize=(10, 6))
x = np.linspace(0, 10, 50)
y = 2 * x + 1 + np.random.randn(50) * 2  # Linear with noise

# Scatter plot
plt.scatter(x, y, s=50, alpha=0.6, label='Data points')

# Trend line
z = np.polyfit(x, y, 1)  # Linear fit
p = np.poly1d(z)
plt.plot(x, p(x), 'r--', linewidth=2, label=f'Trend: y={z[0]:.2f}x+{z[1]:.2f}')

plt.xlabel('X axis', fontsize=12)
plt.ylabel('Y axis', fontsize=12)
plt.title('Scatter Plot with Trend Line', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("""
ADD TREND LINE:

# Fit polynomial (degree 1 = linear)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

# Plot trend line
plt.plot(x, p(x), 'r--', label='Trend')
""")

print("\n" + "="*60)
print("BUBBLE CHART (SCATTER WITH SIZE)")
print("="*60)

# Bubble chart
plt.figure(figsize=(10, 6))
x = np.random.rand(30) * 10
y = np.random.rand(30) * 10
sizes = np.random.rand(30) * 1000  # Bubble sizes
colors = np.random.rand(30)  # Bubble colors

plt.scatter(x, y, s=sizes, c=colors, cmap='coolwarm', alpha=0.6, edgecolors='black', linewidths=1.5)
plt.colorbar(label='Value')
plt.xlabel('X axis', fontsize=12)
plt.ylabel('Y axis', fontsize=12)
plt.title('Bubble Chart - Size and Color Represent Data', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("""
BUBBLE CHART: Scatter plot where size represents a third variable

sizes = [100, 200, 300, 400, 500]  # Third variable
plt.scatter(x, y, s=sizes, alpha=0.6)
""")

print("\n" + "="*60)
print("MULTIPLE SCATTER GROUPS")
print("="*60)

# Multiple groups
plt.figure(figsize=(10, 6))

# Group 1
x1 = np.random.randn(50) + 2
y1 = np.random.randn(50) + 2
plt.scatter(x1, y1, s=80, c='red', alpha=0.6, edgecolors='darkred', label='Group A')

# Group 2
x2 = np.random.randn(50) + 5
y2 = np.random.randn(50) + 5
plt.scatter(x2, y2, s=80, c='blue', alpha=0.6, edgecolors='darkblue', label='Group B')

# Group 3
x3 = np.random.randn(50) + 3.5
y3 = np.random.randn(50) + 6
plt.scatter(x3, y3, s=80, c='green', alpha=0.6, edgecolors='darkgreen', label='Group C')

plt.xlabel('Feature 1', fontsize=12)
plt.ylabel('Feature 2', fontsize=12)
plt.title('Multiple Groups Scatter Plot', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("""
MULTIPLE GROUPS:

plt.scatter(x1, y1, c='red', label='Group A')
plt.scatter(x2, y2, c='blue', label='Group B')
plt.scatter(x3, y3, c='green', label='Group C')
plt.legend()
""")

print("\n" + "="*60)
print("WHEN TO USE SCATTER PLOTS")
print("="*60)

print("""
USE SCATTER PLOTS FOR:
======================
✓ Showing relationships between two variables
✓ Identifying correlations
✓ Detecting patterns or clusters
✓ Finding outliers
✓ Comparing groups

EXAMPLES:
• Height vs Weight
• Study time vs Test scores
• Temperature vs Ice cream sales
• Age vs Income
• Price vs Demand

SCATTER vs LINE PLOT:
=====================
SCATTER PLOT:
• Individual data points
• Shows distribution
• No connection between points
• Good for correlation

LINE PLOT:
• Connected points
• Shows trends over time
• Continuous data
• Good for time series

TIPS:
=====
• Use alpha for overlapping points
• Add trend line to show correlation
• Use colors to show groups
• Use size for third variable (bubble chart)
• Add colorbar for continuous color values
• Use grid for easier reading
• Label axes clearly
• Add legend for multiple groups

COLORMAPS:
==========
'viridis'   - Blue to yellow (default)
'plasma'    - Purple to yellow
'coolwarm'  - Blue to red
'RdYlGn'    - Red to green
'rainbow'   - Full spectrum
'gray'      - Grayscale

MARKER STYLES:
==============
'o'  - Circle (default)
's'  - Square
'^'  - Triangle up
'v'  - Triangle down
'*'  - Star
'+'  - Plus
'x'  - X
'D'  - Diamond
'.'  - Point
""")
