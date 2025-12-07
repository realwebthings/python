import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

print("="*60)
print("PIE CHARTS IN MATPLOTLIB")
print("="*60)

# Create subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Pie Chart Examples', fontsize=16, fontweight='bold')

# Sample data
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [15, 30, 45, 10, 20]

# 1. Basic pie chart
axes[0, 0].pie(sizes, labels=labels)
axes[0, 0].set_title('1. Basic Pie Chart')

# 2. Pie chart with percentages
axes[0, 1].pie(sizes, labels=labels, autopct='%1.1f%%')
axes[0, 1].set_title('2. With Percentages')

# 3. Colored pie chart
colors = ['red', 'blue', 'green', 'orange', 'purple']
axes[0, 2].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
axes[0, 2].set_title('3. Custom Colors')

# 4. Exploded pie chart (pull out slices)
explode = (0, 0.1, 0, 0, 0)  # Pull out 2nd slice
axes[1, 0].pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%')
axes[1, 0].set_title('4. Exploded Slice')

# 5. Pie chart with shadow
axes[1, 1].pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
axes[1, 1].set_title('5. With Shadow')

# 6. Styled pie chart
axes[1, 2].pie(sizes, labels=labels, autopct='%1.1f%%', 
               startangle=90, colors=colors, 
               wedgeprops={'edgecolor': 'black', 'linewidth': 2})
axes[1, 2].set_title('6. Styled (startangle + edges)')

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("PIE CHART BASICS")
print("="*60)

print("""
WHAT IS A PIE CHART?
====================
A pie chart shows data as slices of a circle.
Each slice represents a proportion of the whole.

VISUAL:
      ┌─────┐
    ╱   B   ╲
   │    30%  │
   │ A       │ C
   │15%     45%│
    ╲   D   ╱
      └─────┘

BASIC USAGE:
============
plt.pie(sizes, labels=labels)

COMMON PARAMETERS:
==================
sizes       - Values for each slice
labels      - Labels for each slice
autopct     - Format for percentages (e.g., '%1.1f%%')
colors      - List of colors for slices
explode     - Tuple to pull out slices (0=normal, 0.1=pulled)
shadow      - Add shadow (True/False)
startangle  - Rotate chart (degrees)
wedgeprops  - Dictionary of slice properties

EXAMPLES:
=========

# Basic pie
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels)

# With percentages
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Custom colors
colors = ['red', 'blue', 'green', 'orange']
plt.pie(sizes, labels=labels, colors=colors)

# Explode a slice
explode = (0, 0.1, 0, 0)  # Pull out 2nd slice
plt.pie(sizes, labels=labels, explode=explode)

# With shadow
plt.pie(sizes, labels=labels, shadow=True)

# Rotate chart
plt.pie(sizes, labels=labels, startangle=90)

# Add edges
plt.pie(sizes, labels=labels, 
        wedgeprops={'edgecolor': 'black', 'linewidth': 2})
""")

print("\n" + "="*60)
print("DONUT CHART (PIE WITH HOLE)")
print("="*60)

# Donut chart
plt.figure(figsize=(8, 8))
sizes = [25, 35, 20, 20]
labels = ['Product A', 'Product B', 'Product C', 'Product D']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
        startangle=90, wedgeprops={'edgecolor': 'white', 'linewidth': 2})

# Draw circle in center to make it a donut
centre_circle = mpatches.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Donut Chart - Market Share', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print("""
DONUT CHART: Pie chart with hole in center

plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Add white circle in center
import matplotlib.patches as mpatches
centre_circle = mpatches.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
""")

print("\n" + "="*60)
print("PIE CHART WITH LEGEND")
print("="*60)

# Pie chart with legend
plt.figure(figsize=(10, 6))
sizes = [30, 25, 20, 15, 10]
labels = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'plum']
explode = (0.1, 0, 0, 0, 0)  # Explode 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.legend(labels, loc='best', bbox_to_anchor=(1, 0, 0.5, 1))
plt.title('Pie Chart with Legend', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print("""
ADD LEGEND TO PIE CHART:

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.legend(labels, loc='best')
""")

print("\n" + "="*60)
print("AUTOPCT FORMATS")
print("="*60)

print("""
AUTOPCT: Format for displaying percentages

'%1.1f%%'  → 25.5%  (1 decimal place)
'%1.0f%%'  → 26%    (no decimals)
'%1.2f%%'  → 25.50% (2 decimal places)
'%.0f%%'   → 26%    (no decimals, shorter)

CUSTOM FUNCTION:
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return f'{pct:.1f}%\\n({val:d})'
    return my_autopct

plt.pie(sizes, autopct=make_autopct(sizes))
# Shows: 25.5%
#        (50)
""")

print("\n" + "="*60)
print("COMPLETE EXAMPLE")
print("="*60)

# Complete styled pie chart
plt.figure(figsize=(12, 8))

# Data
categories = ['Electronics', 'Clothing', 'Food', 'Books', 'Other']
sales = [35, 25, 20, 12, 8]
colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#f9ca24', '#95afc0']
explode = (0.1, 0, 0, 0, 0)  # Explode largest slice

# Create pie chart
result = plt.pie(sales, labels=categories, colors=colors,
                 autopct='%1.1f%%', explode=explode,
                 shadow=True, startangle=90,
                 wedgeprops={'edgecolor': 'white', 'linewidth': 2})

# Unpack based on what's returned
if len(result) == 3:
    wedges, texts, autotexts = result
else:
    wedges, texts = result
    autotexts = []

# Style the text
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

if autotexts:
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(11)
        autotext.set_fontweight('bold')

plt.title('Sales Distribution by Category', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()

print("""
STYLED PIE CHART:

wedges, texts, autotexts = plt.pie(sizes, labels=labels, 
                                     autopct='%1.1f%%')

# Style labels
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

# Style percentages
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
""")

print("\n" + "="*60)
print("WHEN TO USE PIE CHARTS")
print("="*60)

print("""
USE PIE CHARTS FOR:
===================
✓ Showing parts of a whole (percentages)
✓ Comparing proportions
✓ 5-7 categories maximum
✓ When total = 100%

EXAMPLES:
• Market share
• Budget breakdown
• Survey results
• Time allocation
• Resource distribution

DON'T USE PIE CHARTS FOR:
==========================
✗ Comparing many categories (>7)
✗ Showing trends over time
✗ Precise comparisons (use bar chart)
✗ When values are similar

PIE vs BAR CHART:
=================
PIE CHART:
• Shows proportions/percentages
• Parts of a whole
• Visual impact
• Limited categories

BAR CHART:
• Shows exact values
• Easy to compare
• Many categories OK
• More precise

TIPS:
=====
• Limit to 5-7 slices
• Order slices by size (largest first)
• Use contrasting colors
• Add percentages (autopct)
• Explode important slices
• Consider donut chart for modern look
• Use legend if labels are long
• Avoid 3D pie charts (hard to read)
""")
