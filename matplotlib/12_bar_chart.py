import matplotlib.pyplot as plt
import numpy as np

print("="*60)
print("BAR CHARTS IN MATPLOTLIB")
print("="*60)

# Create subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Bar Chart Examples', fontsize=16, fontweight='bold')

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

# 1. Basic vertical bar chart
axes[0, 0].bar(categories, values)
axes[0, 0].set_title('1. Basic Vertical Bar Chart')
axes[0, 0].set_ylabel('Values')
axes[0, 0].grid(True, alpha=0.3, axis='y')

# 2. Horizontal bar chart
axes[0, 1].barh(categories, values)
axes[0, 1].set_title('2. Horizontal Bar Chart')
axes[0, 1].set_xlabel('Values')
axes[0, 1].grid(True, alpha=0.3, axis='x')

# 3. Colored bars
colors = ['red', 'blue', 'green', 'orange', 'purple']
axes[0, 2].bar(categories, values, color=colors)
axes[0, 2].set_title('3. Colored Bars')
axes[0, 2].set_ylabel('Values')
axes[0, 2].grid(True, alpha=0.3, axis='y')

# 4. Bar chart with edge color
axes[1, 0].bar(categories, values, color='lightblue', 
               edgecolor='blue', linewidth=2)
axes[1, 0].set_title('4. Bars with Edge Color')
axes[1, 0].set_ylabel('Values')
axes[1, 0].grid(True, alpha=0.3, axis='y')

# 5. Bar chart with custom width
axes[1, 1].bar(categories, values, width=0.5, color='coral')
axes[1, 1].set_title('5. Custom Width (width=0.5)')
axes[1, 1].set_ylabel('Values')
axes[1, 1].grid(True, alpha=0.3, axis='y')

# 6. Grouped bar chart
x = np.arange(len(categories))
values1 = [23, 45, 56, 78, 32]
values2 = [34, 55, 48, 65, 40]
width = 0.35

axes[1, 2].bar(x - width/2, values1, width, label='Group 1', color='skyblue')
axes[1, 2].bar(x + width/2, values2, width, label='Group 2', color='lightcoral')
axes[1, 2].set_title('6. Grouped Bar Chart')
axes[1, 2].set_ylabel('Values')
axes[1, 2].set_xticks(x)
axes[1, 2].set_xticklabels(categories)
axes[1, 2].legend()
axes[1, 2].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("BAR CHART BASICS")
print("="*60)

print("""
WHAT IS A BAR CHART?
====================
A bar chart displays data using rectangular bars.
Height/length of bar represents the value.

VISUAL:
       ┌───┐
       │   │     ┌───┐
   ┌───┤   ├───┬─┤   │
   │ A │ B │ C │ D │ E │
   └───┴───┴───┴─┴───┘

BASIC USAGE:
============

# Vertical bars
plt.bar(x, height)

# Horizontal bars
plt.barh(y, width)

COMMON PARAMETERS:
==================
x, y        - Position of bars
height      - Height of bars (vertical)
width       - Width of bars (horizontal) or bar width
color       - Bar color
edgecolor   - Border color
linewidth   - Border thickness
alpha       - Transparency
label       - Legend label

EXAMPLES:
=========

# Basic vertical bar
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]
plt.bar(categories, values)

# Horizontal bar
plt.barh(categories, values)

# Colored bars
plt.bar(categories, values, color='red')

# Multiple colors
colors = ['red', 'blue', 'green', 'orange']
plt.bar(categories, values, color=colors)

# With edge
plt.bar(categories, values, color='lightblue', 
        edgecolor='blue', linewidth=2)

# Custom width
plt.bar(categories, values, width=0.5)

# Transparent
plt.bar(categories, values, alpha=0.7)
""")

print("\n" + "="*60)
print("GROUPED BAR CHARTS")
print("="*60)

print("""
GROUPED BARS: Compare multiple groups side by side

x = np.arange(len(categories))
width = 0.35

plt.bar(x - width/2, values1, width, label='Group 1')
plt.bar(x + width/2, values2, width, label='Group 2')
plt.xticks(x, categories)
plt.legend()

VISUAL:
   ┌─┐┌─┐
   │ ││ │  ┌─┐┌─┐
   │1││2│  │1││2│
   └─┘└─┘  └─┘└─┘
     A       B
""")

print("\n" + "="*60)
print("STACKED BAR CHARTS")
print("="*60)

# Stacked bar chart example
plt.figure(figsize=(10, 6))
categories = ['Q1', 'Q2', 'Q3', 'Q4']
product_a = [20, 35, 30, 35]
product_b = [25, 32, 34, 20]
product_c = [15, 18, 22, 25]

plt.bar(categories, product_a, label='Product A', color='skyblue')
plt.bar(categories, product_b, bottom=product_a, label='Product B', color='lightcoral')
plt.bar(categories, product_c, bottom=np.array(product_a)+np.array(product_b), 
        label='Product C', color='lightgreen')

plt.xlabel('Quarter', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.title('Stacked Bar Chart - Quarterly Sales', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

print("""
STACKED BARS: Stack bars on top of each other

plt.bar(x, values1, label='A')
plt.bar(x, values2, bottom=values1, label='B')
plt.bar(x, values3, bottom=values1+values2, label='C')

VISUAL:
   ┌───┐
   │ C │
   ├───┤
   │ B │
   ├───┤
   │ A │
   └───┘
""")

print("\n" + "="*60)
print("BAR CHART WITH VALUES ON TOP")
print("="*60)

# Bar chart with value labels
plt.figure(figsize=(10, 6))
categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [150, 230, 180, 290, 210]

bars = plt.bar(categories, sales, color='steelblue', edgecolor='navy', linewidth=2)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.xlabel('Products', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.title('Product Sales with Value Labels', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

print("""
ADD VALUES ON TOP OF BARS:

bars = plt.bar(x, values)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom')
""")

print("\n" + "="*60)
print("WHEN TO USE BAR CHARTS")
print("="*60)

print("""
USE BAR CHARTS FOR:
===================
✓ Comparing categories (sales by product)
✓ Showing discrete data (not continuous)
✓ Comparing values across groups
✓ Showing rankings or frequencies

EXAMPLES:
• Sales by month
• Population by country
• Survey results
• Product comparisons
• Test scores by student

VERTICAL vs HORIZONTAL:
=======================
VERTICAL (plt.bar):
• Default choice
• Good for time series (months, years)
• Better for many categories

HORIZONTAL (plt.barh):
• Long category names
• Easier to read labels
• Better for rankings

TIPS:
=====
• Use consistent colors for same category
• Add grid for easier reading (axis='y')
• Sort bars by value for rankings
• Add value labels for precision
• Use grouped bars to compare groups
• Use stacked bars to show composition
""")
