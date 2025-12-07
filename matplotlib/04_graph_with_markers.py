import matplotlib.pyplot as plt 
import matplotlib.markers as mmarkers
import numpy as np

print("="*60)
print(f"{'MATPLOTLIB MARKERS':^60}")
print("="*60)

# Show all available markers
print("\nAvailable markers:")
for marker in mmarkers.MarkerStyle.markers:
    print(f"{marker}: {mmarkers.MarkerStyle.markers[marker]}")

print("\n" + "="*50)
print(f"{'MARKER EXAMPLES':^50}")
print("="*50)

# Create sample data
x = np.linspace(0, 10, 10)
y = np.sin(x)

xx = np.linspace(0, 20, 10)
yy = np.sin(xx)

# # Valid linestyles: '-', '--', '-.', ':', 'solid', 'dashed', 'dashdot', 'dotted'
# plt.plot(x, y, marker="o", markersize=10, markerfacecolor="red", linestyle="-", linewidth=2, label="Circle", markeredgecolor="purple")
# plt.plot(xx, yy, marker="s", markersize=10, markerfacecolor="blue", linestyle="--", linewidth=2, label="Square",  markeredgecolor="red")

line_style = {"marker": "o", "markersize": 10, "markerfacecolor": "red", "linestyle": "-", "linewidth": 2, "label": "Circle", "markeredgecolor": "purple", "color": '#1c5bfc'}
line_style2 = {"marker": "s", "markersize": 10, "markerfacecolor": "blue", "linestyle": "--", "linewidth": 2, "label": "Square", "markeredgecolor": "red", "color": "#21c033"}
#dict() not working giving warning so used. {}
plt.plot(x, y, **line_style)
plt.plot(xx, yy, **line_style2)
plt.legend() # show labels for each line means graph
plt.grid(True, alpha=0.3)
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
