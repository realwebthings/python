import matplotlib.pyplot as plt
import numpy as np

print("="*60)
print("LINE STYLES AND COLORS REFERENCE")
print("="*60)

x = np.linspace(0, 10, 100)

# LINE STYLES
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Line Styles Reference', fontsize=16, fontweight='bold')

# Solid, dashed, dashdot, dotted
axes[0, 0].plot(x, np.sin(x), '-', label='solid', linewidth=2)
axes[0, 0].plot(x, np.sin(x)-0.5, '--', label='dashed', linewidth=2)
axes[0, 0].plot(x, np.sin(x)-1, '-.', label='dashdot', linewidth=2)
axes[0, 0].plot(x, np.sin(x)-1.5, ':', label='dotted', linewidth=2)
axes[0, 0].set_title('Line Styles')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# COLORS - Named
axes[0, 1].plot(x, np.sin(x), 'r-', label='red', linewidth=2)
axes[0, 1].plot(x, np.sin(x)-0.5, 'g-', label='green', linewidth=2)
axes[0, 1].plot(x, np.sin(x)-1, 'b-', label='blue', linewidth=2)
axes[0, 1].plot(x, np.sin(x)-1.5, 'k-', label='black', linewidth=2)
axes[0, 1].set_title('Basic Colors')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# COLORS - Hex
axes[1, 0].plot(x, np.sin(x), color='#FF6B6B', label='#FF6B6B', linewidth=2)
axes[1, 0].plot(x, np.sin(x)-0.5, color='#4ECDC4', label='#4ECDC4', linewidth=2)
axes[1, 0].plot(x, np.sin(x)-1, color='#45B7D1', label='#45B7D1', linewidth=2)
axes[1, 0].set_title('Hex Colors')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# COMBINED
axes[1, 1].plot(x, np.sin(x), 'r-', label='red solid', linewidth=2)
axes[1, 1].plot(x, np.sin(x)-0.5, 'b--', label='blue dashed', linewidth=2)
axes[1, 1].plot(x, np.sin(x)-1, 'g-.', label='green dashdot', linewidth=2)
axes[1, 1].plot(x, np.sin(x)-1.5, 'm:', label='magenta dotted', linewidth=2)
axes[1, 1].set_title('Combined Styles')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("""
LINE STYLES:
'-'  or 'solid'
'--' or 'dashed'
'-.' or 'dashdot'
':'  or 'dotted'

COLORS (short):
'r' - red, 'g' - green, 'b' - blue
'c' - cyan, 'm' - magenta, 'y' - yellow
'k' - black, 'w' - white

COLORS (named):
'red', 'blue', 'green', 'orange', 'purple', etc.

COLORS (hex):
'#FF0000' - red, '#00FF00' - green, '#0000FF' - blue

COMBINED FORMAT:
'ro-'  = red, circle marker, solid line
'bs--' = blue, square marker, dashed line
'g^:'  = green, triangle marker, dotted line
""")
