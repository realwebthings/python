import matplotlib.pyplot as plt 
import matplotlib.markers as mmarkers
import numpy as np

print("="*50)
print(f"{"MULTIPLE GRAPHS WITH MARKER EXAMPLES":^60}")
print("="*50)

# Create sample data
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Different marker styles
fig, axes = plt.subplots(2, 3, figsize=(12, 8))
fig.suptitle('Different Marker Styles', fontsize=16)

# Marker examples
markers = ['o', 's', '^', '*', 'D', 'x']
titles = ['Circle (o)', 'Square (s)', 'Triangle (^)', 'Star (*)', 'Diamond (D)', 'X (x)']

for ax, marker, title in zip(axes.flat, markers, titles):
    ax.plot(x, y, marker=marker, markersize=10, linestyle='-', linewidth=2)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n" + "="*50)
print("COMMON MARKERS")
print("="*50)
print("""
MARKER STYLES:
'o'  - Circle
's'  - Square
'^'  - Triangle up
'v'  - Triangle down
'*'  - Star
'+'  - Plus
'x'  - X
'D'  - Diamond
'.'  - Point
','  - Pixel

USAGE:
plt.plot(x, y, marker='o')           # With line
plt.plot(x, y, 'o')                  # Marker only (no line)
plt.plot(x, y, marker='o', ms=10)    # Custom marker size
plt.plot(x, y, 'ro-')                # Red color, circle marker, solid line
""")
