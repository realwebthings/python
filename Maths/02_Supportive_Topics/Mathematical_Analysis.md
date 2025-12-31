# 📈 Mathematical Analysis for ML/AI

## 📋 Table of Contents
- [Overview](#overview)
- [Limits and Continuity](#limits-and-continuity)
- [Sequences and Series](#sequences-and-series)
- [Convergence Theory](#convergence-theory)
- [Metric Spaces](#metric-spaces)
- [Functional Analysis Basics](#functional-analysis-basics)
- [Real Analysis Foundations](#real-analysis-foundations)
- [Applications in ML/AI](#applications-in-mlai)
- [Practice Problems](#practice-problems)
- [Python Implementation](#python-implementation)

---

## Overview

Mathematical analysis provides the **rigorous foundation** for calculus and optimization theory, essential for understanding ML/AI algorithms:

### 🎯 **Critical Applications:**
- **Convergence Analysis**: Understanding when algorithms converge
- **Optimization Theory**: Rigorous foundations for gradient descent
- **Function Approximation**: Neural networks as universal approximators
- **Regularization**: Understanding smoothness and continuity
- **Probability Theory**: Measure-theoretic foundations
- **Signal Processing**: Fourier analysis and wavelets

---

## Limits and Continuity

### Epsilon-Delta Definition of Limits
lim_{x→a} f(x) = L if for every ε > 0, there exists δ > 0 such that:
|x - a| < δ ⟹ |f(x) - L| < ε

```python
import numpy as np
import matplotlib.pyplot as plt

def visualize_epsilon_delta(f, a, L, epsilon, delta):
    """Visualize epsilon-delta definition of limits"""
    x = np.linspace(a - 2*delta, a + 2*delta, 1000)
    y = f(x)
    
    plt.figure(figsize=(10, 8))
    plt.plot(x, y, 'b-', linewidth=2, label=f'f(x)')
    
    # Point of interest
    plt.plot(a, L, 'ro', markersize=8, label=f'({a}, {L})')
    
    # Epsilon band
    plt.axhline(y=L + epsilon, color='r', linestyle='--', alpha=0.7, label=f'L ± ε')
    plt.axhline(y=L - epsilon, color='r', linestyle='--', alpha=0.7)
    
    # Delta interval
    plt.axvline(x=a - delta, color='g', linestyle='--', alpha=0.7, label=f'a ± δ')
    plt.axvline(x=a + delta, color='g', linestyle='--', alpha=0.7)
    
    # Shaded regions
    plt.fill_between([a - delta, a + delta], L - epsilon, L + epsilon, 
                     alpha=0.2, color='yellow', label='ε-δ region')
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Epsilon-Delta Definition: ε = {epsilon}, δ = {delta}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

# Example: f(x) = x²
f = lambda x: x**2
visualize_epsilon_delta(f, a=2, L=4, epsilon=0.5, delta=0.1)
```

### Types of Discontinuities

#### **Removable Discontinuity**
lim_{x→a} f(x) exists but f(a) is undefined or different.

#### **Jump Discontinuity**
Left and right limits exist but are different.

#### **Essential Discontinuity**
At least one one-sided limit doesn't exist.

```python
def analyze_discontinuities():
    """Analyze different types of discontinuities"""
    x = np.linspace(-3, 3, 1000)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Removable discontinuity: f(x) = (x²-1)/(x-1) for x≠1, f(1)=3
    def f1(x):
        result = np.where(np.abs(x - 1) < 1e-10, 3, (x**2 - 1) / (x - 1))
        return result
    
    y1 = f1(x)
    axes[0].plot(x, y1, 'b-', linewidth=2)
    axes[0].plot(1, 3, 'ro', markersize=8, label='f(1) = 3')
    axes[0].plot(1, 2, 'go', markersize=8, fillstyle='none', label='lim = 2')
    axes[0].set_title('Removable Discontinuity')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Jump discontinuity: step function
    def f2(x):
        return np.where(x < 0, -1, 1)
    
    y2 = f2(x)
    axes[1].plot(x, y2, 'b-', linewidth=2)
    axes[1].plot(0, -1, 'ro', markersize=8, fillstyle='none', label='left limit = -1')
    axes[1].plot(0, 1, 'go', markersize=8, fillstyle='none', label='right limit = 1')
    axes[1].set_title('Jump Discontinuity')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    # Essential discontinuity: sin(1/x)
    def f3(x):
        return np.where(np.abs(x) < 1e-10, 0, np.sin(1/x))
    
    x3 = np.linspace(-0.5, 0.5, 1000)
    x3 = x3[x3 != 0]  # Remove x=0
    y3 = f3(x3)
    axes[2].plot(x3, y3, 'b-', linewidth=1)
    axes[2].set_title('Essential Discontinuity: sin(1/x)')
    axes[2].set_ylim(-1.5, 1.5)
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

analyze_discontinuities()
```

---

## Sequences and Series

### Sequence Convergence
A sequence {aₙ} converges to L if for every ε > 0, there exists N such that:
n > N ⟹ |aₙ - L| < ε

### Common Convergent Sequences
- **Geometric**: aₙ = rⁿ converges to 0 if |r| < 1
- **Harmonic**: aₙ = 1/n converges to 0
- **Exponential**: aₙ = (1 + 1/n)ⁿ converges to e

```python
def analyze_sequence_convergence():
    """Analyze convergence of various sequences"""
    n_values = np.arange(1, 101)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Geometric sequence: (1/2)^n
    geometric = (0.5)**n_values
    axes[0, 0].plot(n_values, geometric, 'bo-', markersize=3)
    axes[0, 0].axhline(y=0, color='r', linestyle='--', label='Limit = 0')
    axes[0, 0].set_title('Geometric: aₙ = (1/2)ⁿ')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # Harmonic sequence: 1/n
    harmonic = 1/n_values
    axes[0, 1].plot(n_values, harmonic, 'go-', markersize=3)
    axes[0, 1].axhline(y=0, color='r', linestyle='--', label='Limit = 0')
    axes[0, 1].set_title('Harmonic: aₙ = 1/n')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # Exponential: (1 + 1/n)^n
    exponential = (1 + 1/n_values)**n_values
    axes[1, 0].plot(n_values, exponential, 'mo-', markersize=3)
    axes[1, 0].axhline(y=np.e, color='r', linestyle='--', label=f'Limit = e ≈ {np.e:.3f}')
    axes[1, 0].set_title('Exponential: aₙ = (1 + 1/n)ⁿ')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # Alternating: (-1)^n / n
    alternating = ((-1)**n_values) / n_values
    axes[1, 1].plot(n_values, alternating, 'co-', markersize=3)
    axes[1, 1].axhline(y=0, color='r', linestyle='--', label='Limit = 0')
    axes[1, 1].set_title('Alternating: aₙ = (-1)ⁿ/n')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

analyze_sequence_convergence()
```

### Series Convergence Tests

#### **Ratio Test**
For series Σaₙ, if lim |aₙ₊₁/aₙ| = L:
- L < 1: converges
- L > 1: diverges
- L = 1: inconclusive

#### **Root Test**
If lim ⁿ√|aₙ| = L:
- L < 1: converges
- L > 1: diverges
- L = 1: inconclusive

```python
def series_convergence_tests():
    """Implement and demonstrate series convergence tests"""
    
    def ratio_test(a_func, n_terms=100):
        """Apply ratio test to series"""
        ratios = []
        for n in range(1, n_terms):
            ratio = abs(a_func(n+1) / a_func(n))
            ratios.append(ratio)
        
        limit = np.mean(ratios[-10:])  # Approximate limit
        return limit, ratios
    
    def root_test(a_func, n_terms=100):
        """Apply root test to series"""
        roots = []
        for n in range(1, n_terms):
            root = abs(a_func(n))**(1/n)
            roots.append(root)
        
        limit = np.mean(roots[-10:])  # Approximate limit
        return limit, roots
    
    # Test series: aₙ = 1/n!
    factorial_series = lambda n: 1/np.math.factorial(n)
    
    ratio_limit, ratios = ratio_test(factorial_series, 20)
    print(f"Factorial series 1/n!:")
    print(f"Ratio test limit: {ratio_limit:.6f} (< 1, converges)")
    
    # Test series: aₙ = n/2ⁿ
    geometric_series = lambda n: n / (2**n)
    
    ratio_limit, ratios = ratio_test(geometric_series, 50)
    print(f"\nGeometric series n/2ⁿ:")
    print(f"Ratio test limit: {ratio_limit:.6f} (< 1, converges)")
    
    # Visualize convergence
    n_values = range(1, 21)
    factorial_terms = [factorial_series(n) for n in n_values]
    geometric_terms = [geometric_series(n) for n in n_values]
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.semilogy(n_values, factorial_terms, 'bo-', label='1/n!')
    plt.xlabel('n')
    plt.ylabel('aₙ (log scale)')
    plt.title('Factorial Series Terms')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.plot(n_values, geometric_terms, 'ro-', label='n/2ⁿ')
    plt.xlabel('n')
    plt.ylabel('aₙ')
    plt.title('Geometric Series Terms')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

series_convergence_tests()
```

---

## Convergence Theory

### Types of Convergence

#### **Pointwise Convergence**
fₙ(x) → f(x) for each fixed x.

#### **Uniform Convergence**
fₙ → f uniformly if sup|fₙ(x) - f(x)| → 0.

#### **L² Convergence**
∫|fₙ(x) - f(x)|² dx → 0.

```python
def demonstrate_convergence_types():
    """Demonstrate different types of function convergence"""
    x = np.linspace(0, 1, 1000)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Pointwise but not uniform: fₙ(x) = x^n on [0,1]
    for n in [1, 2, 5, 10, 20]:
        fn = x**n
        axes[0].plot(x, fn, label=f'n={n}')
    
    # Limit function
    limit_func = np.where(x == 1, 1, 0)
    axes[0].plot(x, limit_func, 'k--', linewidth=2, label='Limit')
    axes[0].set_title('Pointwise Convergence: xⁿ')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Uniform convergence: fₙ(x) = x/n
    for n in [1, 2, 5, 10, 20]:
        fn = x/n
        axes[1].plot(x, fn, label=f'n={n}')
    
    axes[1].axhline(y=0, color='k', linestyle='--', linewidth=2, label='Limit')
    axes[1].set_title('Uniform Convergence: x/n')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    # L² convergence example
    for n in [1, 2, 5, 10]:
        fn = np.sin(n * np.pi * x) / n
        axes[2].plot(x, fn, label=f'n={n}')
    
    axes[2].axhline(y=0, color='k', linestyle='--', linewidth=2, label='Limit')
    axes[2].set_title('L² Convergence: sin(nπx)/n')
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

demonstrate_convergence_types()
```

---

## Metric Spaces

### Definition
A metric space (X, d) consists of a set X and a distance function d: X × X → ℝ satisfying:
1. d(x, y) ≥ 0 (non-negativity)
2. d(x, y) = 0 ⟺ x = y (identity)
3. d(x, y) = d(y, x) (symmetry)
4. d(x, z) ≤ d(x, y) + d(y, z) (triangle inequality)

### Common Metrics
- **Euclidean**: d(x, y) = √Σ(xᵢ - yᵢ)²
- **Manhattan**: d(x, y) = Σ|xᵢ - yᵢ|
- **Chebyshev**: d(x, y) = max|xᵢ - yᵢ|
- **Hamming**: Number of differing positions

```python
def compare_metrics():
    """Compare different metrics in 2D space"""
    # Generate points
    np.random.seed(42)
    points = np.random.randn(20, 2)
    center = np.array([0, 0])
    
    # Calculate distances using different metrics
    euclidean_dist = np.sqrt(np.sum((points - center)**2, axis=1))
    manhattan_dist = np.sum(np.abs(points - center), axis=1)
    chebyshev_dist = np.max(np.abs(points - center), axis=1)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Euclidean metric
    scatter = axes[0].scatter(points[:, 0], points[:, 1], c=euclidean_dist, 
                             cmap='viridis', s=50)
    axes[0].plot(0, 0, 'r*', markersize=15, label='Center')
    circle = plt.Circle((0, 0), 1, fill=False, color='red', linestyle='--')
    axes[0].add_patch(circle)
    axes[0].set_title('Euclidean Distance')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    axes[0].set_aspect('equal')
    plt.colorbar(scatter, ax=axes[0])
    
    # Manhattan metric
    scatter = axes[1].scatter(points[:, 0], points[:, 1], c=manhattan_dist, 
                             cmap='viridis', s=50)
    axes[1].plot(0, 0, 'r*', markersize=15, label='Center')
    # Manhattan distance unit "circle" (diamond)
    diamond_x = [1, 0, -1, 0, 1]
    diamond_y = [0, 1, 0, -1, 0]
    axes[1].plot(diamond_x, diamond_y, 'r--', label='Unit distance')
    axes[1].set_title('Manhattan Distance')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    axes[1].set_aspect('equal')
    plt.colorbar(scatter, ax=axes[1])
    
    # Chebyshev metric
    scatter = axes[2].scatter(points[:, 0], points[:, 1], c=chebyshev_dist, 
                             cmap='viridis', s=50)
    axes[2].plot(0, 0, 'r*', markersize=15, label='Center')
    # Chebyshev distance unit "circle" (square)
    square_x = [1, 1, -1, -1, 1]
    square_y = [1, -1, -1, 1, 1]
    axes[2].plot(square_x, square_y, 'r--', label='Unit distance')
    axes[2].set_title('Chebyshev Distance')
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)
    axes[2].set_aspect('equal')
    plt.colorbar(scatter, ax=axes[2])
    
    plt.tight_layout()
    plt.show()
    
    return euclidean_dist, manhattan_dist, chebyshev_dist

distances = compare_metrics()
```

---

## Functional Analysis Basics

### Normed Vector Spaces
A norm ||·|| on vector space V satisfies:
1. ||x|| ≥ 0, ||x|| = 0 ⟺ x = 0
2. ||αx|| = |α|||x||
3. ||x + y|| ≤ ||x|| + ||y|| (triangle inequality)

### Common Norms
- **L¹ norm**: ||x||₁ = Σ|xᵢ|
- **L² norm**: ||x||₂ = √Σxᵢ²
- **L∞ norm**: ||x||∞ = max|xᵢ|
- **Lᵖ norm**: ||x||ₚ = (Σ|xᵢ|ᵖ)^(1/p)

```python
def visualize_norms():
    """Visualize different norms and their unit balls"""
    # Create unit balls for different norms
    theta = np.linspace(0, 2*np.pi, 1000)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    
    # L1 norm (diamond)
    x1 = np.sign(np.cos(theta)) * np.abs(np.cos(theta))
    y1 = np.sign(np.sin(theta)) * np.abs(np.sin(theta))
    axes[0, 0].plot(x1, y1, 'b-', linewidth=2, label='L¹ unit ball')
    axes[0, 0].set_title('L¹ Norm: ||x||₁ = |x₁| + |x₂|')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_aspect('equal')
    axes[0, 0].legend()
    
    # L2 norm (circle)
    x2 = np.cos(theta)
    y2 = np.sin(theta)
    axes[0, 1].plot(x2, y2, 'r-', linewidth=2, label='L² unit ball')
    axes[0, 1].set_title('L² Norm: ||x||₂ = √(x₁² + x₂²)')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_aspect('equal')
    axes[0, 1].legend()
    
    # L∞ norm (square)
    square_theta = np.linspace(0, 2*np.pi, 1000)
    x_inf = np.where((square_theta >= 0) & (square_theta < np.pi/2), 1,
                     np.where((square_theta >= np.pi/2) & (square_theta < np.pi), -1,
                              np.where((square_theta >= np.pi) & (square_theta < 3*np.pi/2), -1, 1)))
    y_inf = np.where((square_theta >= 0) & (square_theta < np.pi/2), np.tan(square_theta),
                     np.where((square_theta >= np.pi/2) & (square_theta < np.pi), 1,
                              np.where((square_theta >= np.pi) & (square_theta < 3*np.pi/2), -np.tan(square_theta-np.pi), -1)))
    
    # Simplified square
    x_inf = [1, 1, -1, -1, 1]
    y_inf = [1, -1, -1, 1, 1]
    axes[1, 0].plot(x_inf, y_inf, 'g-', linewidth=2, label='L∞ unit ball')
    axes[1, 0].set_title('L∞ Norm: ||x||∞ = max(|x₁|, |x₂|)')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_aspect('equal')
    axes[1, 0].legend()
    
    # Lp norms for different p values
    p_values = [0.5, 1, 2, 4, 8]
    for p in p_values:
        if p == 0.5:
            # Special case for p < 1 (not actually a norm)
            x_p = np.sign(np.cos(theta)) * np.abs(np.cos(theta))**(1/p)
            y_p = np.sign(np.sin(theta)) * np.abs(np.sin(theta))**(1/p)
        else:
            # General Lp unit ball
            x_p = np.sign(np.cos(theta)) * np.abs(np.cos(theta))**(2/p)
            y_p = np.sign(np.sin(theta)) * np.abs(np.sin(theta))**(2/p)
        
        axes[1, 1].plot(x_p, y_p, linewidth=2, label=f'L^{p}')
    
    axes[1, 1].set_title('Lᵖ Norms for Different p')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].set_aspect('equal')
    axes[1, 1].legend()
    
    plt.tight_layout()
    plt.show()

visualize_norms()
```

---

## Applications in ML/AI

### 1. **Convergence Analysis of Gradient Descent**
```python
def analyze_gradient_descent_convergence():
    """Analyze convergence properties of gradient descent"""
    
    # Quadratic function: f(x) = x^T A x + b^T x + c
    A = np.array([[2, 0.5], [0.5, 1]])
    b = np.array([1, 2])
    c = 1
    
    def f(x):
        return 0.5 * x.T @ A @ x + b.T @ x + c
    
    def grad_f(x):
        return A @ x + b
    
    # Analytical solution
    x_opt = -np.linalg.solve(A, b)
    f_opt = f(x_opt)
    
    # Gradient descent with different learning rates
    learning_rates = [0.1, 0.3, 0.5, 0.8]
    
    plt.figure(figsize=(15, 10))
    
    for i, lr in enumerate(learning_rates):
        x = np.array([3.0, 3.0])  # Starting point
        trajectory = [x.copy()]
        function_values = [f(x)]
        
        for _ in range(50):
            grad = grad_f(x)
            x = x - lr * grad
            trajectory.append(x.copy())
            function_values.append(f(x))
        
        trajectory = np.array(trajectory)
        
        # Plot trajectory
        plt.subplot(2, 2, i+1)
        
        # Contour plot
        x_range = np.linspace(-3, 4, 100)
        y_range = np.linspace(-3, 4, 100)
        X, Y = np.meshgrid(x_range, y_range)
        Z = np.zeros_like(X)
        
        for j in range(X.shape[0]):
            for k in range(X.shape[1]):
                point = np.array([X[j, k], Y[j, k]])
                Z[j, k] = f(point)
        
        plt.contour(X, Y, Z, levels=20, alpha=0.6)
        plt.plot(trajectory[:, 0], trajectory[:, 1], 'ro-', markersize=3, 
                linewidth=1, label=f'lr={lr}')
        plt.plot(x_opt[0], x_opt[1], 'g*', markersize=15, label='Optimum')
        plt.title(f'Learning Rate = {lr}')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Check convergence rate
        errors = [np.linalg.norm(traj - x_opt) for traj in trajectory]
        print(f"Learning rate {lr}: Final error = {errors[-1]:.6f}")
    
    plt.tight_layout()
    plt.show()

analyze_gradient_descent_convergence()
```

### 2. **Function Approximation Theory**
```python
def universal_approximation_demo():
    """Demonstrate universal approximation with neural networks"""
    
    # Target function
    def target_function(x):
        return np.sin(2*np.pi*x) + 0.5*np.sin(6*np.pi*x)
    
    # Simple neural network approximation
    def neural_network(x, weights, biases):
        """Simple 1-hidden layer network"""
        # Hidden layer
        z1 = np.tanh(weights[0] * x + biases[0])
        z2 = np.tanh(weights[1] * x + biases[1])
        z3 = np.tanh(weights[2] * x + biases[2])
        
        # Output layer
        output = weights[3] * z1 + weights[4] * z2 + weights[5] * z3 + biases[3]
        return output
    
    x = np.linspace(0, 1, 1000)
    y_target = target_function(x)
    
    # Different network complexities
    network_sizes = [3, 10, 50]
    
    plt.figure(figsize=(15, 5))
    
    for i, n_neurons in enumerate(network_sizes):
        plt.subplot(1, 3, i+1)
        
        # Random weights for demonstration
        np.random.seed(42)
        weights = np.random.randn(n_neurons + 1) * 2
        biases = np.random.randn(n_neurons + 1)
        
        # Simple approximation (not trained, just for illustration)
        if n_neurons == 3:
            y_approx = neural_network(x, weights[:6], biases[:4])
        else:
            # Simplified approximation using Fourier-like basis
            y_approx = np.zeros_like(x)
            for j in range(min(n_neurons, 10)):
                y_approx += np.sin(2*np.pi*(j+1)*x) / (j+1)
            y_approx *= 0.5
        
        plt.plot(x, y_target, 'b-', linewidth=2, label='Target')
        plt.plot(x, y_approx, 'r--', linewidth=2, label=f'{n_neurons} neurons')
        plt.title(f'Approximation with {n_neurons} Neurons')
        plt.legend()
        plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

universal_approximation_demo()
```

### 3. **Regularization and Smoothness**
```python
def regularization_analysis():
    """Analyze effect of regularization on function smoothness"""
    
    # Generate noisy data
    np.random.seed(42)
    x_data = np.linspace(0, 1, 20)
    y_true = np.sin(2*np.pi*x_data)
    y_data = y_true + 0.3*np.random.randn(len(x_data))
    
    # Polynomial fitting with different regularization
    x_fine = np.linspace(0, 1, 1000)
    degrees = [9]  # High degree polynomial
    lambdas = [0, 0.01, 0.1, 1.0]
    
    plt.figure(figsize=(15, 10))
    
    for i, lam in enumerate(lambdas):
        plt.subplot(2, 2, i+1)
        
        # Ridge regression (L2 regularization)
        from sklearn.preprocessing import PolynomialFeatures
        from sklearn.linear_model import Ridge
        from sklearn.pipeline import Pipeline
        
        poly_ridge = Pipeline([
            ('poly', PolynomialFeatures(degree=degrees[0])),
            ('ridge', Ridge(alpha=lam))
        ])
        
        poly_ridge.fit(x_data.reshape(-1, 1), y_data)
        y_pred = poly_ridge.predict(x_fine.reshape(-1, 1))
        
        plt.scatter(x_data, y_data, color='red', alpha=0.7, label='Data')
        plt.plot(x_fine, np.sin(2*np.pi*x_fine), 'g-', linewidth=2, label='True function')
        plt.plot(x_fine, y_pred, 'b-', linewidth=2, label=f'λ = {lam}')
        plt.title(f'Regularization: λ = {lam}')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Calculate smoothness (second derivative)
        if i == 0:
            print(f"Regularization λ = {lam}: High variance, overfitting")
        else:
            print(f"Regularization λ = {lam}: Smoother function")
    
    plt.tight_layout()
    plt.show()

regularization_analysis()
```

---

## Practice Problems

### Problem 1: Limit Calculation
Find lim_{x→0} (sin(x) - x)/x³

**Solution:**
Using L'Hôpital's rule three times:
lim_{x→0} (sin(x) - x)/x³ = lim_{x→0} (cos(x) - 1)/(3x²) = lim_{x→0} (-sin(x))/(6x) = lim_{x→0} (-cos(x))/6 = -1/6

### Problem 2: Series Convergence
Determine convergence of Σ(n²/3ⁿ)

**Solution:**
Using ratio test: lim |aₙ₊₁/aₙ| = lim |(n+1)²/3ⁿ⁺¹| × |3ⁿ/n²| = lim (n+1)²/(3n²) = 1/3 < 1
Therefore, the series converges.

### Problem 3: Metric Space
Verify that d(x,y) = |x-y|/(1+|x-y|) is a metric on ℝ.

**Solution:**
1. Non-negativity: Clear since |x-y| ≥ 0
2. Identity: d(x,y) = 0 ⟺ |x-y| = 0 ⟺ x = y
3. Symmetry: d(x,y) = |x-y|/(1+|x-y|) = |y-x|/(1+|y-x|) = d(y,x)
4. Triangle inequality: Requires careful verification using properties of the function f(t) = t/(1+t)

---

## 🎯 Key Takeaways

1. **Rigor Matters**: Analysis provides the rigorous foundation for calculus and optimization
2. **Convergence is Central**: Understanding when and how algorithms converge
3. **Continuity is Key**: Smooth functions are easier to optimize
4. **Norms Measure Size**: Different norms give different geometric intuitions
5. **Approximation Theory**: Neural networks as universal function approximators
6. **Regularization Creates Smoothness**: Mathematical justification for regularization techniques

---

## 📚 Next Steps

After mastering mathematical analysis, proceed to:
1. **Measure Theory** - Foundation for advanced probability
2. **Functional Analysis** - Infinite-dimensional spaces
3. **Harmonic Analysis** - Fourier transforms and wavelets
4. **Operator Theory** - Linear operators on function spaces

---

## 🔗 Resources

- **Rudin**: "Principles of Mathematical Analysis" (classic text)
- **Apostol**: "Mathematical Analysis" (comprehensive)
- **Folland**: "Real Analysis" (modern approach)
- **SciPy**: Numerical analysis functions
- **SymPy**: Symbolic mathematics for exact calculations

---

*Mathematical analysis provides the rigorous foundation for understanding convergence, continuity, and approximation in ML/AI. Master it to understand the theoretical guarantees behind optimization algorithms!*