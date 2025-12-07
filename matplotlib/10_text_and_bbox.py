import matplotlib.pyplot as plt
import numpy as np

print("="*60)
print("plt.text() and bbox EXPLAINED")
print("="*60)

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('plt.text() and bbox Examples', fontsize=16, fontweight='bold')

# 1. Basic text (no box)
axes[0, 0].plot(x, y)
axes[0, 0].text(5, 0.5, 'Basic Text (no box)', fontsize=14)
axes[0, 0].set_title('1. Basic plt.text()')
axes[0, 0].grid(True, alpha=0.3)

# 2. Text with simple box
axes[0, 1].plot(x, y)
axes[0, 1].text(5, 0.5, 'Text with Box', fontsize=14,
                bbox=dict(facecolor='yellow', alpha=0.5))
axes[0, 1].set_title('2. Text with bbox')
axes[0, 1].grid(True, alpha=0.3)

# 3. Different box styles
axes[1, 0].plot(x, y)
axes[1, 0].text(2, 0.7, 'Round Box', fontsize=12,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
axes[1, 0].text(5, 0.3, 'Square Box', fontsize=12,
                bbox=dict(boxstyle='square', facecolor='lightgreen', alpha=0.7))
axes[1, 0].text(8, -0.3, 'Round4 Box', fontsize=12,
                bbox=dict(boxstyle='round4', facecolor='lightcoral', alpha=0.7))
axes[1, 0].set_title('3. Different Box Styles')
axes[1, 0].grid(True, alpha=0.3)

# 4. Styled boxes with edges
axes[1, 1].plot(x, y)
axes[1, 1].text(3, 0.6, 'Thick Edge', fontsize=12,
                bbox=dict(boxstyle='round', facecolor='white', 
                         edgecolor='red', linewidth=3))
axes[1, 1].text(7, 0, 'Dashed Edge', fontsize=12,
                bbox=dict(boxstyle='round', facecolor='lightyellow',
                         edgecolor='blue', linestyle='--', linewidth=2))
axes[1, 1].text(5, -0.7, 'No Edge', fontsize=12,
                bbox=dict(boxstyle='round', facecolor='lightgray',
                         edgecolor='none'))
axes[1, 1].set_title('4. Box Edge Styles')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("plt.text() EXPLAINED")
print("="*60)

print("""
plt.text(x, y, 'text')
         ↑  ↑   ↑
         │  │   └─ The text to display
         │  └───── Y coordinate
         └──────── X coordinate

BASIC USAGE:
============
plt.text(5, 0.5, 'Hello')  # Put "Hello" at position (5, 0.5)

COMMON PARAMETERS:
==================
x, y          - Position coordinates
s             - Text string
fontsize      - Text size (default: 10)
color         - Text color
ha            - Horizontal alignment: 'left', 'center', 'right'
va            - Vertical alignment: 'top', 'center', 'bottom'
rotation      - Rotate text (degrees)
fontweight    - 'normal', 'bold'
bbox          - Box around text (see below)

EXAMPLES:
=========
# Centered text
plt.text(5, 0.5, 'Center', ha='center', va='center')

# Rotated text
plt.text(5, 0.5, 'Rotated', rotation=45)

# Styled text
plt.text(5, 0.5, 'Bold Red', fontsize=16, color='red', fontweight='bold')
""")

print("\n" + "="*60)
print("bbox (BOUNDING BOX) EXPLAINED")
print("="*60)

print("""
bbox = dict(...)  ← Dictionary of box properties

BASIC BOX:
==========
bbox=dict(facecolor='yellow')  # Yellow background

COMMON PROPERTIES:
==================
boxstyle      - Shape of box
facecolor     - Fill color
edgecolor     - Border color
alpha         - Transparency (0-1)
linewidth     - Border thickness
linestyle     - Border style: '-', '--', '-.', ':'
pad           - Padding inside box

BOX STYLES (boxstyle):
======================
'square'      - Square corners
'round'       - Rounded corners
'round4'      - Very rounded corners
'circle'      - Circular
'larrow'      - Left arrow
'rarrow'      - Right arrow
'darrow'      - Down arrow
'sawtooth'    - Sawtooth edges

EXAMPLES:
=========

# Simple yellow box
bbox=dict(facecolor='yellow', alpha=0.5)

# Rounded box with border
bbox=dict(boxstyle='round', facecolor='lightblue', 
          edgecolor='blue', linewidth=2)

# Transparent box
bbox=dict(facecolor='white', alpha=0.3)

# No border
bbox=dict(facecolor='lightgray', edgecolor='none')

# Dashed border
bbox=dict(boxstyle='round', facecolor='white',
          edgecolor='red', linestyle='--', linewidth=2)

# Arrow box
bbox=dict(boxstyle='rarrow', facecolor='yellow')
""")

print("\n" + "="*60)
print("COMPLETE EXAMPLE")
print("="*60)

# Comprehensive example
plt.figure(figsize=(12, 8))
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, linewidth=2, label='sin(x)')

# Different text annotations
plt.text(1, 0.8, 'Peak', fontsize=14, ha='center',
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

plt.text(5, -0.8, 'Trough', fontsize=14, ha='center',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

plt.text(7.5, 0.5, 'Important Point!', fontsize=12, color='red',
         bbox=dict(boxstyle='round', facecolor='white', 
                  edgecolor='red', linewidth=3))

plt.text(3, 0, 'Rotated Text', fontsize=11, rotation=45,
         bbox=dict(boxstyle='square', facecolor='lightgreen', alpha=0.5))

plt.xlabel('X axis', fontsize=12)
plt.ylabel('Y axis', fontsize=12)
plt.title('Text Annotations with Bounding Boxes', fontsize=16)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

print("""
WHEN TO USE:
============
✓ Annotate important points on plot
✓ Add labels to specific data points
✓ Highlight regions or features
✓ Add explanatory notes
✓ Mark peaks, troughs, or special values

TIPS:
=====
• Use ha='center' to center text on a point
• Use alpha for transparency
• Match box colors to your plot theme
• Don't overuse - too many boxes = cluttered plot
• Use rotation for diagonal labels
""")
