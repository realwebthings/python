import matplotlib.pyplot as plt
import numpy as np

print("="*60)
print("ALL POSSIBLE plt.plot() ARGUMENTS")
print("="*60)

# Sample data
x = np.linspace(0, 10, 20)
y = np.sin(x)

# Create figure with multiple subplots
fig, axes = plt.subplots(3, 3, figsize=(15, 12))
fig.suptitle('Complete plt.plot() Arguments Reference', fontsize=16, fontweight='bold')

# 1. Basic line
axes[0, 0].plot(x, y)
axes[0, 0].set_title('1. Basic: plot(x, y)')
axes[0, 0].grid(True, alpha=0.3)

# 2. Color
axes[0, 1].plot(x, y, color='red')
axes[0, 1].plot(x, y-0.5, color='#00FF00')  # Hex color
axes[0, 1].plot(x, y-1, color=(0, 0, 1))    # RGB tuple
axes[0, 1].set_title('2. color="red" / "#00FF00" / (0,0,1)')
axes[0, 1].grid(True, alpha=0.3)

# 3. Line style
axes[0, 2].plot(x, y, linestyle='-', label='solid')
axes[0, 2].plot(x, y-0.5, linestyle='--', label='dashed')
axes[0, 2].plot(x, y-1, linestyle='-.', label='dashdot')
axes[0, 2].plot(x, y-1.5, linestyle=':', label='dotted')
axes[0, 2].set_title('3. linestyle="-" / "--" / "-." / ":"')
axes[0, 2].legend(fontsize=8)
axes[0, 2].grid(True, alpha=0.3)

# 4. Line width
axes[1, 0].plot(x, y, linewidth=1, label='lw=1')
axes[1, 0].plot(x, y-0.5, linewidth=3, label='lw=3')
axes[1, 0].plot(x, y-1, linewidth=5, label='lw=5')
axes[1, 0].set_title('4. linewidth=1/3/5 (or lw)')
axes[1, 0].legend(fontsize=8)
axes[1, 0].grid(True, alpha=0.3)

# 5. Markers
axes[1, 1].plot(x, y, marker='o', label='circle')
axes[1, 1].plot(x, y-0.5, marker='s', label='square')
axes[1, 1].plot(x, y-1, marker='^', label='triangle')
axes[1, 1].plot(x, y-1.5, marker='*', label='star')
axes[1, 1].set_title('5. marker="o"/"s"/"^"/"*"')
axes[1, 1].legend(fontsize=8)
axes[1, 1].grid(True, alpha=0.3)

# 6. Marker size
axes[1, 2].plot(x, y, marker='o', markersize=3, label='ms=3')
axes[1, 2].plot(x, y-0.5, marker='o', markersize=8, label='ms=8')
axes[1, 2].plot(x, y-1, marker='o', markersize=15, label='ms=15')
axes[1, 2].set_title('6. markersize=3/8/15 (or ms)')
axes[1, 2].legend(fontsize=8)
axes[1, 2].grid(True, alpha=0.3)

# 7. Marker colors
axes[2, 0].plot(x, y, marker='o', markersize=10, 
                markerfacecolor='red', markeredgecolor='blue', 
                markeredgewidth=2, label='Custom colors')
axes[2, 0].set_title('7. markerfacecolor / markeredgecolor')
axes[2, 0].legend(fontsize=8)
axes[2, 0].grid(True, alpha=0.3)

# 8. Alpha (transparency)
axes[2, 1].plot(x, y, linewidth=5, alpha=1.0, label='alpha=1.0')
axes[2, 1].plot(x, y-0.5, linewidth=5, alpha=0.5, label='alpha=0.5')
axes[2, 1].plot(x, y-1, linewidth=5, alpha=0.2, label='alpha=0.2')
axes[2, 1].set_title('8. alpha=1.0/0.5/0.2 (transparency)')
axes[2, 1].legend(fontsize=8)
axes[2, 1].grid(True, alpha=0.3)

# 9. Combined format string
axes[2, 2].plot(x, y, 'ro-', label='ro- (red, circle, solid)')
axes[2, 2].plot(x, y-0.5, 'bs--', label='bs-- (blue, square, dashed)')
axes[2, 2].plot(x, y-1, 'g^:', label='g^: (green, triangle, dotted)')
axes[2, 2].set_title('9. Format string: "ro-" / "bs--" / "g^:"')
axes[2, 2].legend(fontsize=8)
axes[2, 2].grid(True, alpha=0.3)



print("\n" + "="*60)
print("COMPLETE ARGUMENT REFERENCE")
print("="*60)

print("""
ALL plt.plot() ARGUMENTS:
========================

1. DATA:
   x, y                    - Data arrays

2. COLOR:
   color='red'             - Named color
   color='#FF0000'         - Hex color
   color=(1, 0, 0)         - RGB tuple (0-1)
   c='red'                 - Short form

3. LINE STYLE:
   linestyle='-'           - Solid line
   linestyle='--'          - Dashed line
   linestyle='-.'          - Dash-dot line
   linestyle=':'           - Dotted line
   linestyle='None'        - No line
   ls='-'                  - Short form

4. LINE WIDTH:
   linewidth=2             - Line width in points
   lw=2                    - Short form

5. MARKER:
   marker='o'              - Circle
   marker='s'              - Square
   marker='^'              - Triangle up
   marker='v'              - Triangle down
   marker='*'              - Star
   marker='+'              - Plus
   marker='x'              - X
   marker='D'              - Diamond
   marker='.'              - Point
   marker=','              - Pixel

6. MARKER SIZE:
   markersize=10           - Marker size in points
   ms=10                   - Short form

7. MARKER COLORS:
   markerfacecolor='red'   - Fill color
   mfc='red'               - Short form
   markeredgecolor='blue'  - Edge color
   mec='blue'              - Short form
   markeredgewidth=2       - Edge width
   mew=2                   - Short form

8. TRANSPARENCY:
   alpha=0.5               - 0 (transparent) to 1 (opaque)

9. LABEL:
   label='My Line'         - For legend

10. Z-ORDER:
    zorder=1               - Drawing order (higher = on top)

11. FORMAT STRING (combines color, marker, linestyle):
    'ro-'                  - Red, circle, solid
    'bs--'                 - Blue, square, dashed
    'g^:'                  - Green, triangle, dotted
    
    Format: [color][marker][linestyle]
    
    Colors: 'r' 'g' 'b' 'c' 'm' 'y' 'k' 'w'
    Markers: 'o' 's' '^' 'v' '*' '+' 'x' 'D' '.'
    Lines: '-' '--' '-.' ':'

12. OTHER:
    drawstyle='steps'      - Step plot style
    fillstyle='full'       - Marker fill style
    antialiased=True       - Smooth lines
    dash_capstyle='round'  - Line cap style
    solid_capstyle='round' - Solid line cap
    dash_joinstyle='round' - Line join style
    solid_joinstyle='round'- Solid line join

EXAMPLE WITH ALL ARGUMENTS:
===========================
plt.plot(x, y,
         color='red',
         linestyle='--',
         linewidth=2,
         marker='o',
         markersize=8,
         markerfacecolor='blue',
         markeredgecolor='green',
         markeredgewidth=2,
         alpha=0.7,
         label='My Line',
         zorder=10)

SHORTHAND EXAMPLE:
==================
plt.plot(x, y, 'ro--', lw=2, ms=8, alpha=0.7, label='My Line')
""")

plt.tight_layout()
plt.show()
