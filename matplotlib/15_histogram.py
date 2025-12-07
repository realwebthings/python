import matplotlib.pyplot as plt
import numpy as np

print("="*60)
print("HISTOGRAMS IN MATPLOTLIB")
print("="*60)

# Create subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Histogram Examples', fontsize=16, fontweight='bold')

# Sample data - normal distribution
data = np.random.randn(1000)

# 1. Basic histogram
axes[0, 0].hist(data)
axes[0, 0].set_title('1. Basic Histogram')
axes[0, 0].set_xlabel('Value')
axes[0, 0].set_ylabel('Frequency')

# 2. Custom number of bins
axes[0, 1].hist(data, bins=30)
axes[0, 1].set_title('2. Custom Bins (bins=30)')
axes[0, 1].set_xlabel('Value')
axes[0, 1].set_ylabel('Frequency')

# 3. Colored histogram
axes[0, 2].hist(data, bins=20, color='red', alpha=0.7)
axes[0, 2].set_title('3. Colored & Transparent')
axes[0, 2].set_xlabel('Value')
axes[0, 2].set_ylabel('Frequency')

# 4. With edges
axes[1, 0].hist(data, bins=20, color='lightblue', edgecolor='blue', linewidth=1.2)
axes[1, 0].set_title('4. With Edge Colors')
axes[1, 0].set_xlabel('Value')
axes[1, 0].set_ylabel('Frequency')

# 5. Cumulative histogram
axes[1, 1].hist(data, bins=30, cumulative=True, color='green', alpha=0.7)
axes[1, 1].set_title('5. Cumulative Histogram')
axes[1, 1].set_xlabel('Value')
axes[1, 1].set_ylabel('Cumulative Frequency')

# 6. Density (normalized)
axes[1, 2].hist(data, bins=30, density=True, alpha=0.7)
axes[1, 2].set_title('6. Density (Normalized)')
axes[1, 2].set_xlabel('Value')
axes[1, 2].set_ylabel('Density')

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("HISTOGRAM BASICS")
print("="*60)

print("""
WHAT IS A HISTOGRAM?
====================
Shows the distribution of data by grouping values into bins.
Height of each bar shows frequency (count) of values in that range.

VISUAL:
    Frequency
       │  ┌─┐
       │  │ │  ┌─┐
       │┌─┤ ├─┐│ │┌─┐
       ││ │ │ ││ ││ │
       └┴─┴─┴─┴┴─┴┴─┴─── Value
        0  1  2  3  4

BASIC USAGE:
============
plt.hist(data)

COMMON PARAMETERS:
==================
data        - Array of values
bins        - Number of bins (default: 10)
color       - Bar color
alpha       - Transparency (0-1)
edgecolor   - Edge color of bars
linewidth   - Edge width
density     - Normalize to show probability density
cumulative  - Show cumulative distribution
range       - (min, max) range of bins
orientation - 'vertical' or 'horizontal'

EXAMPLES:
=========

# Basic histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
plt.hist(data)

# Custom bins
plt.hist(data, bins=20)

# Colored
plt.hist(data, color='red', alpha=0.7)

# With edges
plt.hist(data, edgecolor='black', linewidth=1.2)

# Density (normalized)
plt.hist(data, density=True)

# Cumulative
plt.hist(data, cumulative=True)

# Horizontal
plt.hist(data, orientation='horizontal')

# Custom range
plt.hist(data, range=(0, 10))
""")

print("\n" + "="*60)
print("MULTIPLE HISTOGRAMS")
print("="*60)

# Multiple distributions
plt.figure(figsize=(10, 6))

data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1.5, 1000)
data3 = np.random.normal(-2, 0.8, 1000)

plt.hist(data1, bins=30, alpha=0.5, label='Group A', color='red')
plt.hist(data2, bins=30, alpha=0.5, label='Group B', color='blue')
plt.hist(data3, bins=30, alpha=0.5, label='Group C', color='green')

plt.xlabel('Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Multiple Histograms - Comparing Distributions', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

print("""
MULTIPLE HISTOGRAMS:

plt.hist(data1, bins=30, alpha=0.5, label='Group A')
plt.hist(data2, bins=30, alpha=0.5, label='Group B')
plt.hist(data3, bins=30, alpha=0.5, label='Group C')
plt.legend()

Note: Use alpha for transparency when overlapping
""")

print("\n" + "="*60)
print("HISTOGRAM WITH NORMAL CURVE")
print("="*60)

# Histogram with normal distribution curve
plt.figure(figsize=(10, 6))

data = np.random.randn(1000)
n, bins, patches = plt.hist(data, bins=30, density=True, alpha=0.7, color='skyblue', edgecolor='black')

# Add normal distribution curve
mu = np.mean(data)
sigma = np.std(data)
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
plt.plot(x, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mu)**2 / (2 * sigma**2)),
         'r-', linewidth=2, label=f'Normal(μ={mu:.2f}, σ={sigma:.2f})')

plt.xlabel('Value', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title('Histogram with Normal Distribution Curve', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

print("""
ADD NORMAL CURVE:

n, bins, patches = plt.hist(data, bins=30, density=True)

mu = np.mean(data)
sigma = np.std(data)
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
y = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2/(2*sigma**2))
plt.plot(x, y, 'r-', linewidth=2)
""")

print("\n" + "="*60)
print("HISTOGRAM TYPES")
print("="*60)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
data = np.random.randn(1000)

# Regular histogram
axes[0].hist(data, bins=30, color='steelblue', edgecolor='black')
axes[0].set_title('Regular Histogram')
axes[0].set_xlabel('Value')
axes[0].set_ylabel('Frequency')

# Cumulative histogram
axes[1].hist(data, bins=30, cumulative=True, color='coral', edgecolor='black')
axes[1].set_title('Cumulative Histogram')
axes[1].set_xlabel('Value')
axes[1].set_ylabel('Cumulative Frequency')

# Density histogram
axes[2].hist(data, bins=30, density=True, color='lightgreen', edgecolor='black')
axes[2].set_title('Density Histogram (Normalized)')
axes[2].set_xlabel('Value')
axes[2].set_ylabel('Density')

plt.tight_layout()
plt.show()

print("""
HISTOGRAM TYPES:

1. REGULAR: Shows frequency (count)
   plt.hist(data, bins=30)

2. CUMULATIVE: Shows running total
   plt.hist(data, bins=30, cumulative=True)

3. DENSITY: Normalized (area = 1)
   plt.hist(data, bins=30, density=True)
""")

print("\n" + "="*60)
print("WHEN TO USE HISTOGRAMS")
print("="*60)

print("""
USE HISTOGRAMS FOR:
===================
✓ Showing distribution of data
✓ Understanding data spread
✓ Identifying patterns (normal, skewed, bimodal)
✓ Finding outliers
✓ Comparing distributions

EXAMPLES:
• Test scores distribution
• Age distribution
• Income distribution
• Response times
• Measurement errors

HISTOGRAM vs BAR CHART:
========================
HISTOGRAM:
• Continuous data (numbers)
• Shows distribution
• Bins group ranges
• No gaps between bars
• X-axis is numeric

BAR CHART:
• Categorical data (categories)
• Shows comparison
• Each bar is a category
• Gaps between bars
• X-axis is categories

EXAMPLE:
--------
HISTOGRAM: Ages (0-10, 10-20, 20-30, ...)
BAR CHART: Countries (USA, UK, Canada, ...)

CHOOSING BINS:
==============
Too few bins:  Lose detail
Too many bins: Too noisy

RULES OF THUMB:
• Square root: bins = √n
• Sturges: bins = log₂(n) + 1
• Default: bins = 10
• Try different values!

For 1000 data points:
• √1000 ≈ 32 bins
• log₂(1000) + 1 ≈ 11 bins

TIPS:
=====
• Use 20-50 bins for most data
• Add edgecolor for clarity
• Use alpha when overlapping
• Add grid for easier reading
• Label axes clearly
• Use density for comparing different sized datasets
• Consider cumulative for percentiles
""")

print("\n" + "="*60)
print("PRACTICAL EXAMPLE - EXAM SCORES")
print("="*60)

# Realistic example
plt.figure(figsize=(12, 6))

# Generate exam scores (0-100)
scores = np.random.normal(75, 12, 200)  # Mean=75, Std=12
scores = np.clip(scores, 0, 100)  # Clip to 0-100 range

plt.hist(scores, bins=20, color='steelblue', edgecolor='black', alpha=0.7)

# Add vertical lines for mean and median
mean_score = np.mean(scores)
median_score = np.median(scores)
plt.axvline(mean_score, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_score:.1f}')
plt.axvline(median_score, color='green', linestyle='--', linewidth=2, label=f'Median: {median_score:.1f}')

plt.xlabel('Exam Score', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.title('Exam Score Distribution (200 Students)', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

print(f"""
EXAM SCORE ANALYSIS:
====================
Total Students: 200
Mean Score: {mean_score:.2f}
Median Score: {median_score:.2f}
Std Deviation: {np.std(scores):.2f}
Min Score: {np.min(scores):.2f}
Max Score: {np.max(scores):.2f}

The histogram shows the distribution is approximately normal,
with most students scoring around 75.
""")
