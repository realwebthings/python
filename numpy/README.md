# NumPy Learning Guide

Complete guide to mastering NumPy from basics to advanced concepts.

## 📁 Folder Structure

The numpy folder contains **24 well-organized files** covering all essential NumPy concepts:

```
numpy/
├── 00_numpy_index.py                  # Learning roadmap and quick reference
│
├── WEEK 1: FUNDAMENTALS (01-05)
├── 01_basics_and_creation.py          # Array creation, properties, basic operations
├── 02_data_types.py                   # Data types, overflow, memory, astype()
├── 03_multidimensional_arrays.py      # 2D, 3D arrays and dimensions
├── 04_array_reshaping.py              # Reshape, flatten, transpose
├── 05_array_slicing.py                # Indexing and slicing arrays
│
├── WEEK 2: BASIC OPERATIONS (06-10)
├── 06_basic_operations.py             # Arithmetic with scalars
├── 07_math_functions.py               # Mathematical functions (sin, cos, sqrt)
├── 08_element_wise_operations.py      # Element-wise arithmetic between arrays
├── 09_comparison_operations.py        # Comparison operators, boolean arrays
├── 10_broadcasting.py                 # Broadcasting rules and examples
│
├── WEEK 3: INTERMEDIATE (11-15)
├── 11_statistical_functions.py        # Mean, std, min, max, percentiles
├── 12_boolean_indexing.py             # Filtering arrays with conditions
├── 13_random_arrays.py                # Random number generation
├── 14_advanced_indexing.py            # Fancy indexing, integer arrays
├── 15_array_manipulation.py           # Concatenate, split, stack arrays
│
└── WEEK 4: ADVANCED (16-24)
    ├── 16_linear_algebra.py           # Matrix operations, eigenvalues, SVD
    ├── 17_array_creation_detailed.py  # Advanced array creation methods
    ├── 18_array_copying.py            # Views vs copies, memory management
    ├── 19_stacking_splitting.py       # Stack, split, concatenate operations
    ├── 20_sorting.py                  # Sorting, searching, partitioning
    ├── 21_file_io.py                  # Save/load arrays, text/binary formats
    ├── 22_set_operations.py           # Unique, intersection, union operations
    ├── 23_universal_functions.py      # Ufuncs, vectorization, custom functions
    └── 24_performance_tips.py         # Optimization, best practices
```

## 🎯 Learning Path

### Week 1: Fundamentals (Files 01-05)
Master the basics of NumPy arrays and their properties.

**Topics:**
- Array creation and basic properties
- Data types and memory optimization
- Multidimensional arrays (2D, 3D)
- Reshaping and transposing
- Indexing and slicing

**Key Concepts:**
```python
# Create arrays
arr = np.array([1, 2, 3])
zeros = np.zeros((3, 4))
ones = np.ones(5)
arange = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)

# Data types
arr_int8 = np.array([1, 2, 3], dtype=np.int8)
arr_float = arr.astype(np.float32)

# Reshaping
reshaped = arr.reshape(3, 1)
flattened = arr.flatten()
transposed = arr.T
```

### Week 2: Basic Operations (Files 06-10)
Learn to perform operations on arrays efficiently.

**Topics:**
- Arithmetic operations with scalars
- Mathematical functions
- Element-wise operations between arrays
- Comparison operations
- Broadcasting rules

**Key Concepts:**
```python
# Operations
arr + 5              # Scalar arithmetic
arr * 2
np.sqrt(arr)         # Math functions
np.sin(arr)

# Element-wise
arr1 + arr2
arr1 * arr2

# Broadcasting
arr_2d + arr_1d      # Automatic shape matching
```

### Week 3: Intermediate (Files 11-15)
Explore intermediate NumPy features for data analysis.

**Topics:**
- Statistical functions
- Boolean indexing and filtering
- Random number generation
- Advanced indexing techniques
- Array manipulation

**Key Concepts:**
```python
# Statistics
arr.mean()
arr.std()
np.percentile(arr, 75)

# Boolean indexing
arr[arr > 5]
arr[(arr > 5) & (arr < 10)]

# Random
np.random.random((3, 4))
np.random.randint(0, 10, size=5)

# Manipulation
np.concatenate([arr1, arr2])
np.split(arr, 3)
```

### Week 4: Advanced (Files 16-24)
Master advanced NumPy features and optimization.

**Topics:**
- Linear algebra operations
- Advanced array creation
- Views vs copies
- Stacking and splitting
- Sorting and searching
- File I/O
- Set operations
- Universal functions
- Performance optimization

**Key Concepts:**
```python
# Linear algebra
np.dot(A, B)
A @ B
np.linalg.inv(A)
np.linalg.eig(A)

# Views vs copies
view = arr[::2]      # View (no copy)
copy = arr.copy()    # Explicit copy

# File I/O
np.save('array.npy', arr)
arr = np.load('array.npy')

# Performance
# Use vectorization, not loops
result = arr * 2     # Fast
# for i in range(len(arr)): arr[i] * 2  # Slow
```

## 📚 Quick Reference

### Array Creation
```python
np.array([1, 2, 3])              # From list
np.zeros((3, 4))                 # Zeros
np.ones(5)                       # Ones
np.full((2, 3), 7)               # Filled with value
np.arange(0, 10, 2)              # Range with step
np.linspace(0, 1, 5)             # Evenly spaced
np.eye(3)                        # Identity matrix
np.random.random((3, 4))         # Random floats
np.random.randint(0, 10, 5)      # Random integers
```

### Array Properties
```python
arr.shape                        # Dimensions
arr.size                         # Total elements
arr.ndim                         # Number of dimensions
arr.dtype                        # Data type
arr.itemsize                     # Bytes per element
arr.nbytes                       # Total bytes
```

### Indexing & Slicing
```python
arr[0]                           # Single element
arr[1:4]                         # Slice
arr[::2]                         # Every other element
arr[-1]                          # Last element
arr_2d[0, 1]                     # 2D indexing
arr_2d[:, 1]                     # All rows, column 1
arr[arr > 5]                     # Boolean indexing
```

### Reshaping
```python
arr.reshape(3, 4)                # Reshape
arr.flatten()                    # Flatten to 1D
arr.ravel()                      # Flatten (view if possible)
arr.T                            # Transpose
arr.resize((3, 4))               # Resize in-place
```

### Operations
```python
arr + 5                          # Scalar arithmetic
arr * 2
arr ** 2
arr1 + arr2                      # Element-wise
arr1 * arr2
np.sqrt(arr)                     # Math functions
np.sin(arr)
np.exp(arr)
```

### Statistics
```python
arr.mean()                       # Mean
arr.std()                        # Standard deviation
arr.min(), arr.max()             # Min/max
arr.sum()                        # Sum
arr.cumsum()                     # Cumulative sum
np.median(arr)                   # Median
np.percentile(arr, 75)           # Percentile
```

### Linear Algebra
```python
np.dot(A, B)                     # Matrix multiplication
A @ B                            # Matrix multiplication (Python 3.5+)
np.linalg.inv(A)                 # Matrix inverse
np.linalg.det(A)                 # Determinant
np.linalg.eig(A)                 # Eigenvalues/vectors
np.linalg.solve(A, b)            # Solve Ax = b
```

### Array Manipulation
```python
np.concatenate([arr1, arr2])     # Concatenate
np.vstack([arr1, arr2])          # Vertical stack
np.hstack([arr1, arr2])          # Horizontal stack
np.split(arr, 3)                 # Split into 3
np.append(arr, values)           # Append
np.insert(arr, index, values)    # Insert
np.delete(arr, index)            # Delete
```

### Boolean Operations
```python
arr > 5                          # Boolean array
arr[arr > 5]                     # Filter
(arr > 5) & (arr < 10)           # Multiple conditions
np.where(arr > 5, 1, 0)          # Conditional values
np.any(arr > 5)                  # Any element True
np.all(arr > 0)                  # All elements True
```

### File I/O
```python
np.save('file.npy', arr)         # Save binary
arr = np.load('file.npy')        # Load binary
np.savetxt('file.txt', arr)      # Save text
arr = np.loadtxt('file.txt')     # Load text
np.savez('file.npz', a=arr1, b=arr2)  # Save multiple
```

## 💡 Best Practices

### Performance
```python
# ✅ DO: Use vectorization
result = arr * 2

# ❌ DON'T: Use loops
for i in range(len(arr)):
    arr[i] = arr[i] * 2

# ✅ DO: Use built-in functions
mean = np.mean(arr)

# ❌ DON'T: Implement manually
mean = arr.sum() / len(arr)
```

### Memory Efficiency
```python
# ✅ DO: Use appropriate data types
ages = np.array([25, 30, 45], dtype=np.uint8)  # 0-255

# ❌ DON'T: Use default int64 for small values
ages = np.array([25, 30, 45])  # Uses 8 bytes per element

# ✅ DO: Use views when possible
view = arr[::2]

# ❌ DON'T: Create unnecessary copies
copy = arr[::2].copy()
```

### Code Clarity
```python
# ✅ DO: Use meaningful variable names
temperatures = np.array([20, 25, 30])

# ❌ DON'T: Use cryptic names
t = np.array([20, 25, 30])

# ✅ DO: Check shapes before operations
print(f"Shape: {arr.shape}")

# ✅ DO: Handle errors
try:
    result = np.linalg.inv(matrix)
except np.linalg.LinAlgError:
    print("Matrix is singular")
```

## 🎓 Learning Tips

1. **Start with the index**: Run `00_numpy_index.py` for overview
2. **Follow the sequence**: Files are numbered for smooth progression
3. **Run and modify**: Execute each file and experiment with the code
4. **Focus on key files**: 02 (data types), 10 (broadcasting), 16 (linear algebra), 24 (performance)
5. **Practice regularly**: Use NumPy with real data
6. **Understand broadcasting**: Master file 10 for efficient operations
7. **Optimize memory**: Study file 02 for data type selection
8. **Learn performance**: File 24 is crucial for efficient code

## 📈 Progress Tracker

- [ ] Week 1: Fundamentals (01-05)
  - [ ] 01_basics_and_creation.py
  - [ ] 02_data_types.py
  - [ ] 03_multidimensional_arrays.py
  - [ ] 04_array_reshaping.py
  - [ ] 05_array_slicing.py

- [ ] Week 2: Basic Operations (06-10)
  - [ ] 06_basic_operations.py
  - [ ] 07_math_functions.py
  - [ ] 08_element_wise_operations.py
  - [ ] 09_comparison_operations.py
  - [ ] 10_broadcasting.py

- [ ] Week 3: Intermediate (11-15)
  - [ ] 11_statistical_functions.py
  - [ ] 12_boolean_indexing.py
  - [ ] 13_random_arrays.py
  - [ ] 14_advanced_indexing.py
  - [ ] 15_array_manipulation.py

- [ ] Week 4: Advanced (16-24)
  - [ ] 16_linear_algebra.py
  - [ ] 17_array_creation_detailed.py
  - [ ] 18_array_copying.py
  - [ ] 19_stacking_splitting.py
  - [ ] 20_sorting.py
  - [ ] 21_file_io.py
  - [ ] 22_set_operations.py
  - [ ] 23_universal_functions.py
  - [ ] 24_performance_tips.py

## 🚀 Getting Started

```bash
# Navigate to numpy folder
cd /Users/mukeshkumar/MyRepo/python/numpy

# Start with the index
python 00_numpy_index.py

# Follow the learning path
python 01_basics_and_creation.py
python 02_data_types.py
# ... and so on
```

## 🔑 Key Concepts to Master

| Concept | Files | Priority |
|---------|-------|----------|
| Array Creation | 01, 17 | ⭐⭐⭐ |
| Data Types | 02 | ⭐⭐⭐ |
| Broadcasting | 10 | ⭐⭐⭐ |
| Boolean Indexing | 12 | ⭐⭐⭐ |
| Linear Algebra | 16 | ⭐⭐ |
| Views vs Copies | 18 | ⭐⭐⭐ |
| Performance | 24 | ⭐⭐⭐ |

## 📖 Additional Resources

- [NumPy Official Documentation](https://numpy.org/doc/)
- [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy for MATLAB Users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)
- [From Python to NumPy](https://www.labri.fr/perso/nrougier/from-python-to-numpy/)

## 🎯 Next Steps After NumPy

Once you've mastered NumPy, move on to:
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization
- **SciPy**: Scientific computing
- **Scikit-learn**: Machine learning

---

**Happy Learning! 🚀**
