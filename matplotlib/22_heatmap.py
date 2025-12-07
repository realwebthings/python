import matplotlib.pyplot as plt
import numpy as np

print("="*60)
print("HEATMAPS IN MATPLOTLIB")
print("="*60)

# Sample data - correlation matrix
data = np.random.rand(10, 10)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Heatmap Examples', fontsize=16, fontweight='bold')

# Basic heatmap
im1 = axes[0].imshow(data, cmap='viridis')
axes[0].set_title('Basic Heatmap')
plt.colorbar(im1, ax=axes[0])

# Styled heatmap with annotations
im2 = axes[1].imshow(data, cmap='coolwarm')
axes[1].set_title('Heatmap with Annotations')

# Add text annotations
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        text = axes[1].text(j, i, f'{data[i, j]:.2f}',
                           ha="center", va="center", color="black", fontsize=8)

plt.colorbar(im2, ax=axes[1])
plt.tight_layout()
plt.show()

print("""
HEATMAP BASICS:
===============

BASIC USAGE:
plt.imshow(data, cmap='viridis')
plt.colorbar()

COLORMAPS:
- 'viridis': Blue to yellow
- 'plasma': Purple to yellow
- 'coolwarm': Blue to red
- 'hot': Black to white
- 'gray': Grayscale

WHEN TO USE:
✓ Show 2D data
✓ Correlation matrices
✓ Confusion matrices
✓ Density plots
""")
