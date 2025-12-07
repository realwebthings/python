import matplotlib.pyplot as plt
import numpy as np

print("="*60)
print("BOX PLOTS IN MATPLOTLIB")
print("="*60)

# Sample data
data1 = np.random.normal(100, 10, 200)
data2 = np.random.normal(90, 20, 200)
data3 = np.random.normal(80, 5, 200)
data4 = np.random.normal(70, 15, 200)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Box Plot Examples', fontsize=16, fontweight='bold')

# Basic box plot
axes[0].boxplot([data1, data2, data3, data4])
axes[0].set_xticklabels(['Group A', 'Group B', 'Group C', 'Group D'])
axes[0].set_ylabel('Values')
axes[0].set_title('Basic Box Plot')
axes[0].grid(True, alpha=0.3, axis='y')

# Styled box plot
bp = axes[1].boxplot([data1, data2, data3, data4], 
                      patch_artist=True,
                      notch=True,
                      showmeans=True)

# Color the boxes
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

axes[1].set_xticklabels(['Group A', 'Group B', 'Group C', 'Group D'])
axes[1].set_ylabel('Values')
axes[1].set_title('Styled Box Plot')
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

print("""
BOX PLOT BASICS:
================

WHAT IT SHOWS:
• Median (middle line)
• Q1 and Q3 (box edges)
• Min and Max (whiskers)
• Outliers (dots)

BASIC USAGE:
plt.boxplot([data1, data2, data3])

PARAMETERS:
- patch_artist=True: Fill boxes with color
- notch=True: Show confidence interval
- showmeans=True: Show mean as well
- vert=False: Horizontal boxes

WHEN TO USE:
✓ Compare distributions
✓ Show statistical summary
✓ Identify outliers
✓ Show data spread
""")
