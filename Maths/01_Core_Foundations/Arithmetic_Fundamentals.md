# 🔢 Arithmetic Fundamentals for ML/AI

## 📋 Table of Contents
- [Overview](#overview)
- [Basic Operations](#basic-operations)
- [Exponents and Powers](#exponents-and-powers)
- [Logarithms](#logarithms)
- [Growth Rates](#growth-rates)
- [Applications in ML/AI](#applications-in-mlai)
- [Practice Problems](#practice-problems)
- [Python Implementation](#python-implementation)

---

## Overview

Arithmetic forms the foundation of all mathematical operations in ML/AI. Understanding these concepts is crucial for:
- **Scaling data** (normalization, standardization)
- **Complexity analysis** (Big O notation)
- **Loss function calculations**
- **Gradient computations**

---

## Basic Operations

### Addition and Subtraction
- **Commutative**: a + b = b + a
- **Associative**: (a + b) + c = a + (b + c)
- **Identity**: a + 0 = a

### Multiplication and Division
- **Commutative**: a × b = b × a
- **Associative**: (a × b) × c = a × (b × c)
- **Distributive**: a × (b + c) = a × b + a × c
- **Identity**: a × 1 = a

### Order of Operations (PEMDAS)
1. **P**arentheses
2. **E**xponents
3. **M**ultiplication and **D**ivision (left to right)
4. **A**ddition and **S**ubtraction (left to right)

---

## Exponents and Powers

### Basic Rules
- **Product Rule**: a^m × a^n = a^(m+n)
- **Quotient Rule**: a^m ÷ a^n = a^(m-n)
- **Power Rule**: (a^m)^n = a^(m×n)
- **Zero Exponent**: a^0 = 1 (where a ≠ 0)
- **Negative Exponent**: a^(-n) = 1/a^n

### Special Cases
- **Square Root**: √a = a^(1/2)
- **Cube Root**: ∛a = a^(1/3)
- **Fractional Exponents**: a^(m/n) = ⁿ√(a^m)

### ML Applications
- **Activation Functions**: ReLU, Sigmoid use exponential operations
- **Loss Functions**: Mean Squared Error uses squares
- **Regularization**: L1 (absolute), L2 (squared) penalties

---

## Logarithms

### Definition
If a^x = b, then log_a(b) = x
- **Base**: a (common bases: 10, e, 2)
- **Argument**: b
- **Result**: x

### Properties
- **Product Rule**: log(ab) = log(a) + log(b)
- **Quotient Rule**: log(a/b) = log(a) - log(b)
- **Power Rule**: log(a^n) = n × log(a)
- **Change of Base**: log_a(b) = log_c(b) / log_c(a)

### Common Logarithms
- **Natural Log**: ln(x) = log_e(x), where e ≈ 2.718
- **Common Log**: log(x) = log_10(x)
- **Binary Log**: log_2(x) (used in information theory)

### ML Applications
- **Cross-Entropy Loss**: Uses natural logarithm
- **Information Theory**: Entropy calculations
- **Gradient Descent**: Log-likelihood optimization
- **Feature Scaling**: Log transformation for skewed data

---

## Growth Rates

### Linear Growth
- **Form**: f(x) = ax + b
- **Rate**: Constant rate of change
- **Example**: Simple linear regression

### Exponential Growth
- **Form**: f(x) = a × b^x
- **Rate**: Grows by constant factor
- **Example**: Compound interest, population growth

### Logarithmic Growth
- **Form**: f(x) = a × log(x) + b
- **Rate**: Decreasing rate of growth
- **Example**: Algorithm complexity, diminishing returns

### Polynomial Growth
- **Form**: f(x) = ax^n + bx^(n-1) + ... + c
- **Rate**: Depends on highest degree term
- **Example**: Feature interactions, polynomial regression

### ML Applications
- **Model Complexity**: Understanding overfitting vs underfitting
- **Training Time**: Algorithm complexity analysis
- **Learning Curves**: Performance vs training data size
- **Regularization**: Controlling model growth

---

## Applications in ML/AI

### 1. Data Preprocessing
```
Normalization: x_norm = (x - min) / (max - min)
Standardization: x_std = (x - mean) / std
Log Transform: x_log = log(x + 1)
```

### 2. Loss Functions
```
Mean Squared Error: MSE = (1/n) × Σ(y_true - y_pred)²
Cross-Entropy: CE = -Σ(y_true × log(y_pred))
```

### 3. Activation Functions
```
Sigmoid: σ(x) = 1 / (1 + e^(-x))
ReLU: f(x) = max(0, x)
Softmax: softmax(x_i) = e^(x_i) / Σ(e^(x_j))
```

### 4. Optimization
```
Learning Rate Decay: lr = lr_0 × decay_rate^(epoch/decay_steps)
Exponential Moving Average: v_t = β × v_(t-1) + (1-β) × gradient
```

---

## Practice Problems

### Problem 1: Basic Operations
Calculate: 3² + 4 × 5 - 2³ ÷ 4

**Solution:**
1. Exponents first: 3² = 9, 2³ = 8
2. Division: 8 ÷ 4 = 2
3. Multiplication: 4 × 5 = 20
4. Addition/Subtraction: 9 + 20 - 2 = 27

### Problem 2: Logarithms
If log₂(x) = 5, find x.

**Solution:**
log₂(x) = 5 means 2⁵ = x
Therefore, x = 32

### Problem 3: Growth Rates
Compare the growth of f(x) = x² and g(x) = 2^x for large x.

**Solution:**
- f(x) = x² is polynomial (quadratic)
- g(x) = 2^x is exponential
- For large x, exponential growth dominates polynomial growth
- g(x) grows much faster than f(x)

### Problem 4: ML Application
Calculate the sigmoid activation for x = 2.

**Solution:**
σ(2) = 1 / (1 + e^(-2))
σ(2) = 1 / (1 + 0.135)
σ(2) ≈ 0.881

---

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

# Basic arithmetic operations
def basic_operations():
    a, b = 10, 3
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b:.2f}")
    print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Logarithm functions
def logarithm_examples():
    x = 100
    print(f"Natural log of {x}: {np.log(x):.3f}")
    print(f"Base-10 log of {x}: {np.log10(x):.3f}")
    print(f"Base-2 log of {x}: {np.log2(x):.3f}")

# Growth rate comparison
def plot_growth_rates():
    x = np.linspace(1, 10, 100)
    
    linear = x
    quadratic = x**2
    exponential = 2**x
    logarithmic = np.log(x)
    
    plt.figure(figsize=(12, 8))
    plt.plot(x, linear, label='Linear: f(x) = x')
    plt.plot(x, quadratic, label='Quadratic: f(x) = x²')
    plt.plot(x, logarithmic, label='Logarithmic: f(x) = log(x)')
    plt.plot(x, exponential, label='Exponential: f(x) = 2^x')
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Comparison of Growth Rates')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # Log scale to see all functions
    plt.show()

# ML activation functions
def activation_functions():
    x = np.linspace(-5, 5, 100)
    
    # Sigmoid
    sigmoid = 1 / (1 + np.exp(-x))
    
    # ReLU
    relu = np.maximum(0, x)
    
    # Tanh
    tanh = np.tanh(x)
    
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 3, 1)
    plt.plot(x, sigmoid)
    plt.title('Sigmoid: σ(x) = 1/(1+e^(-x))')
    plt.grid(True)
    
    plt.subplot(1, 3, 2)
    plt.plot(x, relu)
    plt.title('ReLU: f(x) = max(0,x)')
    plt.grid(True)
    
    plt.subplot(1, 3, 3)
    plt.plot(x, tanh)
    plt.title('Tanh: f(x) = tanh(x)')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# Data normalization examples
def normalization_examples():
    # Sample data
    data = np.array([1, 5, 10, 15, 20, 25, 30])
    
    # Min-Max normalization
    min_max_norm = (data - data.min()) / (data.max() - data.min())
    
    # Z-score standardization
    z_score = (data - data.mean()) / data.std()
    
    # Log transformation
    log_transform = np.log(data + 1)  # +1 to avoid log(0)
    
    print("Original data:", data)
    print("Min-Max normalized:", min_max_norm.round(3))
    print("Z-score standardized:", z_score.round(3))
    print("Log transformed:", log_transform.round(3))

if __name__ == "__main__":
    print("=== Basic Operations ===")
    basic_operations()
    
    print("\n=== Logarithm Examples ===")
    logarithm_examples()
    
    print("\n=== Normalization Examples ===")
    normalization_examples()
    
    # Uncomment to see plots
    # plot_growth_rates()
    # activation_functions()
```

---

## 🎯 Key Takeaways

1. **Master the Basics**: Solid arithmetic foundation is essential
2. **Understand Exponents**: Critical for activation functions and loss calculations
3. **Learn Logarithms**: Essential for information theory and optimization
4. **Recognize Growth Patterns**: Helps in complexity analysis and model selection
5. **Practice with Code**: Implement concepts in Python for better understanding

---

## 📚 Next Steps

After mastering arithmetic fundamentals, proceed to:
1. **Algebra** - Equations and matrix operations
2. **Linear Algebra** - Vectors and matrices (most critical for ML)
3. **Calculus** - Derivatives and gradients
4. **Probability** - Random variables and distributions

---

## 🔗 Resources

- **Khan Academy**: Arithmetic basics
- **3Blue1Brown**: Visual mathematics
- **NumPy Documentation**: Python implementation
- **Wolfram Alpha**: Mathematical calculations and verification

---

*Remember: These arithmetic concepts appear everywhere in ML/AI. Master them well!*