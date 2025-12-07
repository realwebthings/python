import matplotlib.pyplot as plt
import numpy as np
import os

print("="*60)
print("SAVING FIGURES IN MATPLOTLIB")
print("="*60)

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2)
plt.xlabel('X axis', fontsize=12)
plt.ylabel('Y axis', fontsize=12)
plt.title('Sine Wave', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)

# Save in different formats
plt.savefig('plot.png')  # PNG (default)
plt.savefig('plot.pdf')  # PDF
plt.savefig('plot.svg')  # SVG
plt.savefig('plot.jpg', dpi=300)  # High resolution JPG

plt.show()

print("""
SAVING FIGURES:
===============

BASIC:
plt.savefig('filename.png')

FORMATS:
- PNG: plt.savefig('plot.png')  # Raster, good for web
- PDF: plt.savefig('plot.pdf')  # Vector, good for print
- SVG: plt.savefig('plot.svg')  # Vector, good for web
- JPG: plt.savefig('plot.jpg')  # Raster, smaller size

PARAMETERS:
- dpi=300: High resolution (default: 100)
- bbox_inches='tight': Remove extra whitespace
- transparent=True: Transparent background
- facecolor='white': Background color

EXAMPLE:
plt.savefig('plot.png', dpi=300, bbox_inches='tight', transparent=True)

TIPS:
• Save before plt.show()
• Use PNG for web, PDF for print
• Use dpi=300 for high quality
• Use bbox_inches='tight' to remove margins
""")

# Cleanup
for file in ['plot.png', 'plot.pdf', 'plot.svg', 'plot.jpg']:
    if os.path.exists(file):
        os.remove(file)
        print(f"Cleaned up {file}")
