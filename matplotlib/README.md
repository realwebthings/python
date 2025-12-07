# Matplotlib Learning Guide

## 📚 Complete File Structure (22 Files)

### WEEK 1: FUNDAMENTALS (Files 01-06)
**Goal: Learn basic plotting and setup**

- `00_matplotlib_index.py` - **START HERE** - Complete learning guide
- `01_intro.py` - First plot, basic concepts
- `02_using_numpy_with_matplotlib.py` - NumPy integration
- `03_array_performance_comparison_python_vs_numpy.py` - Performance comparison
- `04_graph_with_markers.py` - Markers and point styles
- `05_plot_arguments_reference.py` - Complete plot() arguments reference
- `06_multiple_subplots.py` - Creating multiple plots basics

### WEEK 2: CUSTOMIZATION (Files 07-11, 19-20)
**Goal: Master plot customization**

- `07_labels.py` - Labels, titles, fonts
- `08_ticks_explained.py` - Tick marks and axis customization
- `09_labels_vs_ticks.py` - Understanding the difference
- `10_text_and_bbox.py` - Text annotations and bounding boxes
- `11_grid_explained.py` - Grid lines for readability
- `19_line_styles_colors_reference.py` - **NEW** - Complete color/style reference
- `20_saving_figures.py` - **NEW** - Save plots in different formats

### WEEK 3: PLOT TYPES (Files 12-15, 21-22)
**Goal: Learn different visualization types**

- `12_bar_chart.py` - Bar charts (vertical, horizontal, grouped, stacked)
- `13_pie_chart.py` - Pie charts and donut charts
- `14_scatter_plot.py` - Scatter plots and bubble charts
- `15_histogram.py` - Histograms and distributions
- `21_box_plot.py` - **NEW** - Box plots for statistical data
- `22_heatmap.py` - **NEW** - Heatmaps for 2D data

### WEEK 4: ADVANCED (Files 16-18)
**Goal: Work with real data and advanced features**

- `16_subplots.py` - Advanced subplot layouts and shared axes
- `17_csv_plotting_comparison.py` - Reading CSV with/without pandas
- `18_numpy_vs_pandas_comparison.py` - NumPy vs Pandas comparison

---

## 🎯 Quick Start Guide

### Day 1: Getting Started
```bash
python 00_matplotlib_index.py  # Overview
python 01_intro.py             # First plot
python 02_using_numpy_with_matplotlib.py  # NumPy basics
```

### Day 2: Customization
```bash
python 04_graph_with_markers.py  # Markers
python 05_plot_arguments_reference.py  # All options
python 19_line_styles_colors_reference.py  # Colors
```

### Day 3: Plot Types
```bash
python 12_bar_chart.py    # Bar charts
python 13_pie_chart.py    # Pie charts
python 14_scatter_plot.py # Scatter plots
```

---

## 📖 Learning by Topic

### Basic Plotting
- Start: `01_intro.py`
- With NumPy: `02_using_numpy_with_matplotlib.py`
- Customization: `04_graph_with_markers.py`, `05_plot_arguments_reference.py`

### Customization
- Labels: `07_labels.py`, `09_labels_vs_ticks.py`
- Ticks: `08_ticks_explained.py`
- Text: `10_text_and_bbox.py`
- Grid: `11_grid_explained.py`
- Colors: `19_line_styles_colors_reference.py`

### Plot Types
- Line: `01_intro.py`, `04_graph_with_markers.py`
- Bar: `12_bar_chart.py`
- Pie: `13_pie_chart.py`
- Scatter: `14_scatter_plot.py`
- Histogram: `15_histogram.py`
- Box: `21_box_plot.py`
- Heatmap: `22_heatmap.py`

### Layout
- Multiple plots: `06_multiple_subplots.py`, `16_subplots.py`

### Data Sources
- CSV files: `17_csv_plotting_comparison.py`
- NumPy vs Pandas: `18_numpy_vs_pandas_comparison.py`

### Output
- Saving: `20_saving_figures.py`

---

## 🔑 Key Concepts Covered

✅ **Fundamentals**
- Basic plotting
- NumPy integration
- Performance optimization

✅ **Customization**
- Labels, titles, fonts
- Ticks and axes
- Colors and styles
- Text annotations
- Grid lines

✅ **Plot Types**
- Line plots
- Bar charts (vertical, horizontal, grouped, stacked)
- Pie charts (regular, donut)
- Scatter plots (regular, bubble)
- Histograms (regular, cumulative, density)
- Box plots
- Heatmaps

✅ **Layout**
- Single plots
- Multiple subplots
- Shared axes

✅ **Data Handling**
- Python lists
- NumPy arrays
- Pandas DataFrames
- CSV files

✅ **Output**
- Display plots
- Save in multiple formats (PNG, PDF, SVG, JPG)
- Resolution control

---

## 💡 Learning Tips

1. **Run every file** - See the output, don't just read code
2. **Modify examples** - Change values, colors, styles
3. **Combine concepts** - Use multiple techniques together
4. **Use real data** - Apply to your own datasets
5. **Refer to reference files** - Files 05, 08, 09, 19 are references
6. **Practice daily** - 30 minutes per day is better than 3 hours once

---

## 🎓 After Matplotlib

Once you master Matplotlib, explore:
- **Seaborn** - Statistical visualization (built on Matplotlib)
- **Plotly** - Interactive plots
- **Bokeh** - Web-based visualization
- **Dash** - Interactive dashboards

---

## 📝 File Naming Convention

- `00-09`: Fundamentals and basics
- `10-18`: Core concepts and plot types
- `19-22`: Additional concepts
- `00_*_index.py`: Learning guide (start here!)

---

## ✅ Checklist

Track your progress:

### Week 1: Fundamentals
- [ ] 00 - Index and overview
- [ ] 01 - Basic plotting
- [ ] 02 - NumPy integration
- [ ] 03 - Performance
- [ ] 04 - Markers
- [ ] 05 - Plot arguments
- [ ] 06 - Multiple plots

### Week 2: Customization
- [ ] 07 - Labels
- [ ] 08 - Ticks
- [ ] 09 - Labels vs Ticks
- [ ] 10 - Text annotations
- [ ] 11 - Grid
- [ ] 19 - Colors and styles
- [ ] 20 - Saving figures

### Week 3: Plot Types
- [ ] 12 - Bar charts
- [ ] 13 - Pie charts
- [ ] 14 - Scatter plots
- [ ] 15 - Histograms
- [ ] 21 - Box plots
- [ ] 22 - Heatmaps

### Week 4: Advanced
- [ ] 16 - Advanced subplots
- [ ] 17 - CSV plotting
- [ ] 18 - NumPy vs Pandas

---

## 🚀 Quick Reference

### Create a basic plot
```python
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.show()
```

### Customize plot
```python
plt.plot(x, y, 'ro-', linewidth=2, markersize=8)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('My Plot')
plt.grid(True, alpha=0.3)
plt.show()
```

### Save plot
```python
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
```

---

**Start your journey: `python 00_matplotlib_index.py`**
