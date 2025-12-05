# NumPy Learning Index - Complete Guide
"""
NUMPY LEARNING PATH - ORGANIZED BY DIFFICULTY AND TOPIC

This index provides a structured learning path through NumPy concepts,
organized from basic to advanced topics.

LEARNING PROGRESSION:
==================

FUNDAMENTALS (Start Here):
01_basics_and_creation.py          - Array creation and basic properties
02_data_types.py                   - Data types, overflow, memory optimization
03_multidimensional_arrays.py      - 2D, 3D arrays and dimensions
04_array_reshaping.py              - Reshape, flatten, transpose
05_array_slicing.py                - Indexing and slicing arrays

BASIC OPERATIONS:
06_basic_operations.py             - Arithmetic with scalars
07_math_functions.py               - Mathematical functions (sin, cos, sqrt, etc.)
08_element_wise_operations.py      - Element-wise arithmetic between arrays
09_comparison_operations.py        - Comparison operators and boolean arrays
10_broadcasting.py                 - Broadcasting rules and examples

INTERMEDIATE CONCEPTS:
11_statistical_functions.py       - Mean, std, min, max, percentiles
12_boolean_indexing.py            - Filtering arrays with conditions
13_random_arrays.py               - Random number generation
14_advanced_indexing.py           - Fancy indexing, integer arrays
15_array_manipulation.py          - Concatenate, split, stack arrays

ADVANCED TOPICS:
16_linear_algebra.py              - Matrix operations, eigenvalues, SVD
17_array_creation_detailed.py     - Advanced array creation methods
18_array_copying.py               - Views vs copies, memory management
19_stacking_splitting.py          - Stack, split, concatenate operations
20_sorting.py                     - Sorting, searching, partitioning
21_file_io.py                     - Save/load arrays, text/binary formats
22_set_operations.py              - Unique, intersection, union operations
23_universal_functions.py         - Ufuncs, vectorization, custom functions
24_performance_tips.py            - Optimization, best practices

RECOMMENDED LEARNING ORDER:
=========================
Week 1 - Fundamentals: Files 01-05
Week 2 - Basic Operations: Files 06-10  
Week 3 - Intermediate: Files 11-15
Week 4 - Advanced: Files 16-24

QUICK REFERENCE:
===============
• Array Creation: Files 01, 17
• Data Types: File 02
• Indexing/Slicing: Files 05, 12, 14
• Math Operations: Files 06-09, 23
• Statistics: File 11
• Linear Algebra: File 16
• Performance: File 24
• File I/O: File 21

PRACTICE SUGGESTIONS:
===================
1. Run each file and understand the output
2. Modify examples with your own data
3. Combine concepts from multiple files
4. Focus on files 02, 10, 16, 24 for deep understanding
5. Use file 24 for optimization techniques

PREREQUISITES:
=============
- Basic Python knowledge
- Understanding of lists and loops
- Basic mathematics (for linear algebra sections)

NEXT STEPS AFTER NUMPY:
======================
- Pandas (data manipulation)
- Matplotlib (plotting)
- Scikit-learn (machine learning)
- SciPy (scientific computing)
"""

import numpy as np

print("=" * 70)
print("NUMPY LEARNING INDEX")
print("=" * 70)

print("\n🎯 LEARNING PATH OVERVIEW:")
print("=" * 50)

topics = [
    ("FUNDAMENTALS", [
        "01_basics_and_creation.py - Array creation basics",
        "02_data_types.py - Data types and memory",
        "03_multidimensional_arrays.py - 2D/3D arrays",
        "04_array_reshaping.py - Shape manipulation",
        "05_array_slicing.py - Indexing and slicing"
    ]),
    ("BASIC OPERATIONS", [
        "06_basic_operations.py - Scalar arithmetic",
        "07_math_functions.py - Mathematical functions",
        "08_element_wise_operations.py - Array arithmetic",
        "09_comparison_operations.py - Comparisons",
        "10_broadcasting.py - Broadcasting rules"
    ]),
    ("INTERMEDIATE", [
        "11_statistical_functions.py - Statistics",
        "12_boolean_indexing.py - Boolean filtering",
        "13_random_arrays.py - Random numbers",
        "14_advanced_indexing.py - Fancy indexing",
        "15_array_manipulation.py - Array manipulation"
    ]),
    ("ADVANCED", [
        "16_linear_algebra.py - Matrix operations",
        "17_array_creation_detailed.py - Advanced creation",
        "18_array_copying.py - Views vs copies",
        "19_stacking_splitting.py - Stack/split arrays",
        "20_sorting.py - Sorting and searching",
        "21_file_io.py - File input/output",
        "22_set_operations.py - Set operations",
        "23_universal_functions.py - Ufuncs",
        "24_performance_tips.py - Optimization"
    ])
]

for category, files in topics:
    print(f"\n{category}:")
    print("-" * len(category))
    for file_desc in files:
        print(f"  • {file_desc}")

print("\n" + "=" * 50)
print("🚀 QUICK START GUIDE")
print("=" * 50)
print("1. Start with file 01 for basics")
print("2. Master file 02 for data types")
print("3. Practice with files 03-05 for array manipulation")
print("4. Learn operations with files 06-10")
print("5. Explore advanced topics files 16, 24")

print("\n" + "=" * 50)
print("📚 KEY CONCEPTS TO MASTER")
print("=" * 50)
key_concepts = {
    "Array Creation": "Files 01, 17",
    "Data Types": "File 02",
    "Broadcasting": "File 10", 
    "Boolean Indexing": "File 12",
    "Linear Algebra": "File 16",
    "Performance": "File 24",
    "Views vs Copies": "File 18"
}

for concept, files in key_concepts.items():
    print(f"• {concept:.<20} {files}")

print("\n" + "=" * 50)
print("💡 LEARNING TIPS")
print("=" * 50)
print("✅ Run each example and modify it")
print("✅ Focus on understanding, not memorizing")
print("✅ Practice with real data")
print("✅ Read file 02 (data types) carefully")
print("✅ Master broadcasting (file 10)")
print("✅ Study performance tips (file 24)")

# Quick demo
print("\n" + "=" * 50)
print("🔥 NUMPY POWER DEMO")
print("=" * 50)

# Show NumPy's power with a quick example
arr = np.random.random((3, 4))
print(f"Random 3x4 array:\n{arr}")
print(f"Mean: {arr.mean():.3f}")
print(f"Max in each column: {arr.max(axis=0)}")
print(f"Boolean mask (>0.5):\n{arr > 0.5}")

print("\n🎉 Ready to start your NumPy journey!")
print("Begin with file: 01_basics_and_creation.py")