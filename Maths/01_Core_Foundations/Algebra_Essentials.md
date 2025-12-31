# 📐 Algebra Essentials for ML/AI

## 📋 Table of Contents
- [Overview](#overview)
- [Basic Equations](#basic-equations)
- [Inequalities](#inequalities)
- [Polynomials](#polynomials)
- [Matrix Algebra Basics](#matrix-algebra-basics)
- [Systems of Equations](#systems-of-equations)
- [Functions and Relations](#functions-and-relations)
- [Applications in ML/AI](#applications-in-mlai)
- [Practice Problems](#practice-problems)
- [Python Implementation](#python-implementation)

---

## Overview

Algebra is the language of mathematical relationships and transformations. In ML/AI, algebra is essential for:
- **Linear models** (regression, classification)
- **Feature transformations** (scaling, encoding)
- **Matrix operations** (neural networks)
- **Optimization** (gradient descent)

---

## Basic Equations

### Linear Equations
**Form**: ax + b = c

**Solving Steps:**
1. Isolate the variable term: ax = c - b
2. Divide by coefficient: x = (c - b) / a

**Example**: 3x + 5 = 14
- 3x = 14 - 5 = 9
- x = 9 / 3 = 3

### Quadratic Equations
**Form**: ax² + bx + c = 0

**Quadratic Formula**: x = (-b ± √(b² - 4ac)) / (2a)

**Discriminant**: Δ = b² - 4ac
- Δ > 0: Two real solutions
- Δ = 0: One real solution
- Δ < 0: No real solutions

### ML Applications
- **Linear Regression**: y = mx + b
- **Logistic Regression**: Uses linear combinations in sigmoid
- **Neural Networks**: Linear transformations followed by activations

---

## Inequalities

### Basic Inequalities
- **Addition/Subtraction**: If a < b, then a + c < b + c
- **Multiplication/Division**: 
  - If c > 0: a < b ⟹ ac < bc
  - If c < 0: a < b ⟹ ac > bc (flip the sign!)

### Absolute Value Inequalities
- |x| < a ⟺ -a < x < a
- |x| > a ⟺ x < -a or x > a

### ML Applications
- **Constraints**: Optimization with bounds
- **Regularization**: L1 penalty uses absolute values
- **Activation Functions**: ReLU uses max(0, x)
- **Loss Functions**: Hinge loss in SVM

---

## Polynomials

### Definition
**Form**: P(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀

### Key Properties
- **Degree**: Highest power of x
- **Leading Coefficient**: Coefficient of highest degree term
- **Roots**: Values where P(x) = 0

### Operations
- **Addition**: Add corresponding coefficients
- **Multiplication**: Use distributive property
- **Factoring**: Express as product of simpler polynomials

### ML Applications
- **Polynomial Features**: x, x², x³, ... for non-linear relationships
- **Kernel Methods**: Polynomial kernels in SVM
- **Regularization**: Higher-order terms in Ridge regression

---

## Matrix Algebra Basics

### Matrix Definition
A matrix is a rectangular array of numbers:
```
A = [a₁₁  a₁₂  a₁₃]
    [a₂₁  a₂₂  a₂₃]
```

### Basic Operations
**Addition**: Add corresponding elements
```
[1 2] + [5 6] = [6  8]
[3 4]   [7 8]   [10 12]
```

**Scalar Multiplication**: Multiply each element
```
2 × [1 2] = [2 4]
    [3 4]   [6 8]
```

**Matrix Multiplication**: Row × Column
```
[1 2] × [5 6] = [1×5+2×7  1×6+2×8] = [19 22]
[3 4]   [7 8]   [3×5+4×7  3×6+4×8]   [43 50]
```

### Special Matrices
- **Identity Matrix**: I (diagonal of 1s)
- **Zero Matrix**: O (all zeros)
- **Transpose**: Aᵀ (flip rows and columns)
- **Inverse**: A⁻¹ (if exists, AA⁻¹ = I)

### ML Applications
- **Data Representation**: Each row is a sample, columns are features
- **Linear Transformations**: Weight matrices in neural networks
- **Dimensionality Reduction**: PCA uses matrix decomposition

---

## Systems of Equations

### Linear Systems
**Form**:
```
a₁x + b₁y = c₁
a₂x + b₂y = c₂
```

### Solution Methods

**1. Substitution Method**
- Solve one equation for one variable
- Substitute into the other equation

**2. Elimination Method**
- Add/subtract equations to eliminate a variable

**3. Matrix Method**
- Write as Ax = b
- Solve using x = A⁻¹b (if A is invertible)

### ML Applications
- **Normal Equations**: Analytical solution for linear regression
- **Optimization**: Finding critical points
- **Neural Networks**: Forward and backward propagation

---

## Functions and Relations

### Function Definition
A function f: X → Y assigns each input x ∈ X exactly one output y ∈ Y.

### Types of Functions
- **Linear**: f(x) = mx + b
- **Quadratic**: f(x) = ax² + bx + c
- **Exponential**: f(x) = aᵇˣ
- **Logarithmic**: f(x) = log(x)

### Function Properties
- **Domain**: Set of valid inputs
- **Range**: Set of possible outputs
- **One-to-One**: Each output has unique input
- **Onto**: Every element in codomain is mapped

### Composition
(f ∘ g)(x) = f(g(x))

### ML Applications
- **Activation Functions**: Non-linear transformations
- **Loss Functions**: Measure prediction error
- **Feature Engineering**: Transform input variables

---

## Applications in ML/AI

### 1. Linear Regression
```
Hypothesis: h(x) = θ₀ + θ₁x₁ + θ₂x₂ + ... + θₙxₙ
Matrix Form: h(x) = Xθ
Normal Equation: θ = (XᵀX)⁻¹Xᵀy
```

### 2. Logistic Regression
```
Linear Combination: z = θ₀ + θ₁x₁ + ... + θₙxₙ
Sigmoid: σ(z) = 1 / (1 + e⁻ᶻ)
```

### 3. Neural Networks
```
Layer Output: a = σ(Wx + b)
Where: W = weight matrix, x = input, b = bias
```

### 4. Principal Component Analysis (PCA)
```
Covariance Matrix: C = (1/n)XᵀX
Eigenvalue Problem: Cv = λv
```

---

## Practice Problems

### Problem 1: Linear Equation
Solve: 2x - 7 = 3x + 5

**Solution:**
- 2x - 3x = 5 + 7
- -x = 12
- x = -12

### Problem 2: Quadratic Equation
Solve: x² - 5x + 6 = 0

**Solution:**
Using factoring: (x - 2)(x - 3) = 0
Therefore: x = 2 or x = 3

### Problem 3: Matrix Multiplication
Calculate: [2 1] × [3]
          [4 3]   [1]

**Solution:**
[2×3 + 1×1] = [7]
[4×3 + 3×1]   [15]

### Problem 4: System of Equations
Solve:
```
2x + y = 7
x - y = 2
```

**Solution:**
Adding equations: 3x = 9, so x = 3
Substituting: 2(3) + y = 7, so y = 1

---

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

# Solving linear equations
def solve_linear_equation(a, b, c):
    """Solve ax + b = c"""
    if a == 0:
        return "No unique solution" if b != c else "Infinite solutions"
    return (c - b) / a

# Quadratic equation solver
def solve_quadratic(a, b, c):
    """Solve ax² + bx + c = 0"""
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return "No real solutions"
    elif discriminant == 0:
        return -b / (2*a)
    else:
        sqrt_d = np.sqrt(discriminant)
        x1 = (-b + sqrt_d) / (2*a)
        x2 = (-b - sqrt_d) / (2*a)
        return x1, x2

# Matrix operations
def matrix_operations():
    # Define matrices
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    
    # Addition
    print("\nA + B:")
    print(A + B)
    
    # Multiplication
    print("\nA × B:")
    print(A @ B)  # or np.dot(A, B)
    
    # Transpose
    print("\nA transpose:")
    print(A.T)
    
    # Inverse (if exists)
    try:
        print("\nA inverse:")
        print(np.linalg.inv(A))
    except np.linalg.LinAlgError:
        print("Matrix is not invertible")

# System of equations solver
def solve_system():
    # System: 2x + y = 7, x - y = 2
    # Matrix form: Ax = b
    A = np.array([[2, 1], [1, -1]])
    b = np.array([7, 2])
    
    # Solve using numpy
    solution = solve(A, b)
    print(f"Solution: x = {solution[0]}, y = {solution[1]}")
    
    # Verify
    print(f"Verification: {A @ solution} should equal {b}")

# Polynomial operations
def polynomial_operations():
    # Represent polynomial as coefficients (highest degree first)
    # p(x) = 2x² + 3x + 1
    p = np.poly1d([2, 3, 1])
    
    print(f"Polynomial: {p}")
    print(f"p(2) = {p(2)}")
    
    # Find roots
    roots = np.roots([2, 3, 1])
    print(f"Roots: {roots}")
    
    # Plot polynomial
    x = np.linspace(-3, 1, 100)
    y = p(x)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'b-', linewidth=2)
    plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='--', alpha=0.3)
    plt.grid(True, alpha=0.3)
    plt.title('Polynomial: 2x² + 3x + 1')
    plt.xlabel('x')
    plt.ylabel('p(x)')
    plt.show()

# ML application: Linear regression
def linear_regression_example():
    # Generate sample data
    np.random.seed(42)
    X = np.random.randn(100, 1)
    y = 2 * X.flatten() + 1 + 0.1 * np.random.randn(100)
    
    # Add bias term (intercept)
    X_with_bias = np.column_stack([np.ones(X.shape[0]), X])
    
    # Normal equation: θ = (X^T X)^(-1) X^T y
    theta = np.linalg.inv(X_with_bias.T @ X_with_bias) @ X_with_bias.T @ y
    
    print(f"Learned parameters: θ₀ = {theta[0]:.3f}, θ₁ = {theta[1]:.3f}")
    print("True parameters: θ₀ = 1.000, θ₁ = 2.000")
    
    # Plot results
    plt.figure(figsize=(8, 6))
    plt.scatter(X, y, alpha=0.6)
    plt.plot(X, X_with_bias @ theta, 'r-', linewidth=2, label='Fitted line')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Linear Regression using Normal Equation')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    print("=== Linear Equation ===")
    result = solve_linear_equation(2, -7, 3*(-12) + 5)
    print(f"Solution: x = {result}")
    
    print("\n=== Quadratic Equation ===")
    roots = solve_quadratic(1, -5, 6)
    print(f"Roots: {roots}")
    
    print("\n=== Matrix Operations ===")
    matrix_operations()
    
    print("\n=== System of Equations ===")
    solve_system()
    
    print("\n=== Polynomial Operations ===")
    polynomial_operations()
    
    print("\n=== Linear Regression Example ===")
    linear_regression_example()
```

---

## 🎯 Key Takeaways

1. **Master Linear Equations**: Foundation for all ML models
2. **Understand Matrix Operations**: Essential for neural networks
3. **Practice Systems of Equations**: Used in optimization
4. **Learn Function Composition**: Critical for deep learning
5. **Connect to ML**: See algebra in every algorithm

---

## 📚 Next Steps

After mastering algebra essentials, proceed to:
1. **Set Theory** - Functions and relations
2. **Linear Algebra** - Advanced matrix operations (MOST IMPORTANT)
3. **Calculus** - Derivatives for optimization
4. **Probability** - Statistical foundations

---

## 🔗 Resources

- **Khan Academy**: Algebra fundamentals
- **MIT OpenCourseWare**: Linear algebra course
- **NumPy Documentation**: Matrix operations
- **SciPy Documentation**: Advanced mathematical functions

---

*Algebra is the bridge between arithmetic and advanced mathematics. Master it to unlock ML/AI!*