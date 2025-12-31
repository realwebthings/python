# 📈 Calculus for ML/AI - Optimization Foundation

## 📋 Table of Contents
- [Why Calculus is Critical for ML](#why-calculus-is-critical-for-ml)
- [Limits and Continuity](#limits-and-continuity)
- [Derivatives](#derivatives)
- [Multivariable Calculus](#multivariable-calculus)
- [Gradients and Optimization](#gradients-and-optimization)
- [Chain Rule](#chain-rule)
- [Integration](#integration)
- [Applications in ML/AI](#applications-in-mlai)
- [Practice Problems](#practice-problems)
- [Python Implementation](#python-implementation)

---

## Why Calculus is Critical for ML

Calculus is the **mathematical engine** behind ML optimization:

### 🎯 **Critical Applications:**
- **Gradient Descent**: Finding minimum of loss functions
- **Backpropagation**: Training neural networks
- **Optimization**: Minimizing/maximizing objective functions
- **Probability Densities**: Maximum likelihood estimation
- **Regularization**: Adding penalty terms to prevent overfitting
- **Variational Methods**: Variational autoencoders, variational inference

---

## Limits and Continuity

### Limits
**Definition**: lim_{x→a} f(x) = L means f(x) approaches L as x approaches a

**Properties**:
- lim_{x→a} [f(x) + g(x)] = lim_{x→a} f(x) + lim_{x→a} g(x)
- lim_{x→a} [f(x) × g(x)] = lim_{x→a} f(x) × lim_{x→a} g(x)
- lim_{x→a} [f(x) / g(x)] = lim_{x→a} f(x) / lim_{x→a} g(x) (if denominator ≠ 0)

### Continuity
A function f is continuous at x = a if:
1. f(a) exists
2. lim_{x→a} f(x) exists
3. lim_{x→a} f(x) = f(a)

### ML Applications
- **Activation Functions**: Smooth functions for gradient flow
- **Loss Functions**: Continuous functions for optimization
- **Convergence**: Ensuring algorithms converge to solutions

---

## Derivatives

### Definition
The derivative of f(x) at x = a is:
f'(a) = lim_{h→0} [f(a+h) - f(a)] / h

**Geometric Interpretation**: Slope of tangent line
**Physical Interpretation**: Rate of change

### Basic Derivative Rules

#### Power Rule
d/dx [x^n] = n × x^(n-1)

#### Product Rule
d/dx [f(x) × g(x)] = f'(x) × g(x) + f(x) × g'(x)

#### Quotient Rule
d/dx [f(x) / g(x)] = [f'(x) × g(x) - f(x) × g'(x)] / [g(x)]²

#### Chain Rule
d/dx [f(g(x))] = f'(g(x)) × g'(x)

### Common Derivatives
- d/dx [e^x] = e^x
- d/dx [ln(x)] = 1/x
- d/dx [sin(x)] = cos(x)
- d/dx [cos(x)] = -sin(x)
- d/dx [tan(x)] = sec²(x)

### Higher-Order Derivatives
- **Second Derivative**: f''(x) = d²f/dx²
- **Concavity**: f''(x) > 0 (concave up), f''(x) < 0 (concave down)
- **Inflection Points**: Where f''(x) = 0

---

## Multivariable Calculus

### Partial Derivatives
For f(x, y), the partial derivative with respect to x:
∂f/∂x = lim_{h→0} [f(x+h, y) - f(x, y)] / h

**Notation**: ∂f/∂x, f_x, or ∂_x f

### Gradient Vector
∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]ᵀ

**Properties**:
- Points in direction of steepest increase
- Magnitude = rate of steepest increase
- Perpendicular to level curves/surfaces

### Directional Derivative
Rate of change of f in direction of unit vector u:
D_u f = ∇f · u = ||∇f|| × cos(θ)

### Hessian Matrix
Matrix of second partial derivatives:
H = [∂²f/∂xᵢ∂xⱼ]

**Properties**:
- Symmetric if mixed partials are continuous
- Positive definite → local minimum
- Negative definite → local maximum
- Indefinite → saddle point

---

## Gradients and Optimization

### Critical Points
Points where ∇f = 0 (gradient is zero vector)

### Types of Critical Points
1. **Local Minimum**: f(x) ≥ f(x₀) in neighborhood
2. **Local Maximum**: f(x) ≤ f(x₀) in neighborhood
3. **Saddle Point**: Neither minimum nor maximum

### Second Derivative Test
For f(x, y) at critical point (a, b):
- D = f_xx × f_yy - (f_xy)²
- If D > 0 and f_xx > 0: local minimum
- If D > 0 and f_xx < 0: local maximum
- If D < 0: saddle point
- If D = 0: test inconclusive

### Gradient Descent Algorithm
```
x_{k+1} = x_k - α × ∇f(x_k)
```
Where α is the learning rate.

### Constrained Optimization - Lagrange Multipliers
To optimize f(x, y) subject to g(x, y) = 0:
∇f = λ∇g at optimal point

**Lagrangian**: L(x, y, λ) = f(x, y) - λg(x, y)
Set ∇L = 0 to find critical points.

---

## Chain Rule

### Single Variable
If y = f(u) and u = g(x), then:
dy/dx = (dy/du) × (du/dx)

### Multivariable
If z = f(x, y), x = g(t), y = h(t), then:
dz/dt = (∂z/∂x) × (dx/dt) + (∂z/∂y) × (dy/dt)

### General Form
If z = f(x₁, x₂, ..., xₙ) and each xᵢ = gᵢ(t₁, t₂, ..., tₘ), then:
∂z/∂tⱼ = Σᵢ (∂z/∂xᵢ) × (∂xᵢ/∂tⱼ)

### ML Applications
- **Backpropagation**: Chain rule through neural network layers
- **Automatic Differentiation**: Computing gradients efficiently
- **Composite Functions**: Derivatives of nested operations

---

## Integration

### Indefinite Integral
∫ f(x) dx = F(x) + C, where F'(x) = f(x)

### Definite Integral
∫ₐᵇ f(x) dx = F(b) - F(a)

**Geometric Interpretation**: Area under curve

### Fundamental Theorem of Calculus
If F(x) = ∫ₐˣ f(t) dt, then F'(x) = f(x)

### Integration Techniques
- **Substitution**: ∫ f(g(x))g'(x) dx = ∫ f(u) du
- **Integration by Parts**: ∫ u dv = uv - ∫ v du
- **Partial Fractions**: For rational functions

### Multiple Integrals
- **Double Integral**: ∫∫_R f(x,y) dA
- **Triple Integral**: ∫∫∫_V f(x,y,z) dV

### ML Applications
- **Probability**: Normalizing constants, expectations
- **Bayesian Inference**: Computing marginal probabilities
- **Variational Methods**: Optimizing functionals

---

## Applications in ML/AI

### 1. Linear Regression - Gradient Descent
```python
# Loss function: J(θ) = (1/2m) Σ(h_θ(x^i) - y^i)²
# Gradient: ∇J(θ) = (1/m) X^T (Xθ - y)
# Update: θ = θ - α × ∇J(θ)
```

### 2. Logistic Regression
```python
# Sigmoid: σ(z) = 1 / (1 + e^(-z))
# Derivative: σ'(z) = σ(z)(1 - σ(z))
# Cost function: J(θ) = -(1/m) Σ[y log(h_θ(x)) + (1-y) log(1-h_θ(x))]
```

### 3. Neural Networks - Backpropagation
```python
# Forward pass: a^(l+1) = σ(W^(l+1) a^(l) + b^(l+1))
# Backward pass: δ^(l) = (W^(l+1))^T δ^(l+1) ⊙ σ'(z^(l))
# Weight update: W^(l) = W^(l) - α × δ^(l+1) (a^(l))^T
```

### 4. Support Vector Machines
```python
# Objective: minimize (1/2)||w||² + C Σ ξᵢ
# Constraint: yᵢ(w^T xᵢ + b) ≥ 1 - ξᵢ
# Lagrangian optimization with KKT conditions
```

### 5. Principal Component Analysis
```python
# Maximize variance: max w^T Σ w subject to ||w|| = 1
# Solution: eigenvectors of covariance matrix Σ
# Lagrangian: L = w^T Σ w - λ(w^T w - 1)
```

---

## Practice Problems

### Problem 1: Basic Derivatives
Find the derivative of f(x) = 3x⁴ - 2x³ + 5x - 1

**Solution:**
f'(x) = 12x³ - 6x² + 5

### Problem 2: Chain Rule
Find the derivative of f(x) = e^(x² + 1)

**Solution:**
Let u = x² + 1, then f(x) = e^u
f'(x) = e^u × du/dx = e^(x² + 1) × 2x = 2x × e^(x² + 1)

### Problem 3: Partial Derivatives
For f(x, y) = x²y + 3xy² - 2y, find ∂f/∂x and ∂f/∂y

**Solution:**
∂f/∂x = 2xy + 3y²
∂f/∂y = x² + 6xy - 2

### Problem 4: Gradient Descent
Given f(x) = x² - 4x + 3, find the minimum using gradient descent.

**Solution:**
f'(x) = 2x - 4
Set f'(x) = 0: 2x - 4 = 0 → x = 2
f(2) = 4 - 8 + 3 = -1
Minimum at (2, -1)

### Problem 5: Lagrange Multipliers
Minimize f(x, y) = x² + y² subject to x + y = 1

**Solution:**
L(x, y, λ) = x² + y² - λ(x + y - 1)
∂L/∂x = 2x - λ = 0 → x = λ/2
∂L/∂y = 2y - λ = 0 → y = λ/2
∂L/∂λ = -(x + y - 1) = 0 → x + y = 1
Substituting: λ/2 + λ/2 = 1 → λ = 1
Therefore: x = y = 1/2, minimum value = 1/2

---

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import sympy as sp
from mpl_toolkits.mplot3d import Axes3D

# Numerical derivatives
def numerical_derivative(f, x, h=1e-7):
    """Compute numerical derivative using finite differences"""
    return (f(x + h) - f(x - h)) / (2 * h)

def numerical_gradient(f, x, h=1e-7):
    """Compute numerical gradient for multivariable function"""
    x = np.array(x, dtype=float)
    grad = np.zeros_like(x)
    
    for i in range(len(x)):
        x_plus = x.copy()
        x_minus = x.copy()
        x_plus[i] += h
        x_minus[i] -= h
        grad[i] = (f(x_plus) - f(x_minus)) / (2 * h)
    
    return grad

# Symbolic derivatives using SymPy
def symbolic_derivatives():
    x, y = sp.symbols('x y')
    
    # Single variable function
    f1 = x**3 - 2*x**2 + 5*x - 1
    f1_prime = sp.diff(f1, x)
    print(f"f(x) = {f1}")
    print(f"f'(x) = {f1_prime}")
    
    # Chain rule example
    f2 = sp.exp(x**2 + 1)
    f2_prime = sp.diff(f2, x)
    print(f"\nf(x) = {f2}")
    print(f"f'(x) = {f2_prime}")
    
    # Multivariable function
    f3 = x**2 * y + 3*x*y**2 - 2*y
    f3_dx = sp.diff(f3, x)
    f3_dy = sp.diff(f3, y)
    print(f"\nf(x,y) = {f3}")
    print(f"∂f/∂x = {f3_dx}")
    print(f"∂f/∂y = {f3_dy}")
    
    # Gradient vector
    gradient = [f3_dx, f3_dy]
    print(f"∇f = {gradient}")

# Gradient descent implementation
def gradient_descent(f, grad_f, x0, learning_rate=0.01, max_iterations=1000, tolerance=1e-6):
    """
    Gradient descent optimization
    
    Args:
        f: objective function
        grad_f: gradient function
        x0: initial point
        learning_rate: step size
        max_iterations: maximum iterations
        tolerance: convergence tolerance
    
    Returns:
        x: optimal point
        history: optimization history
    """
    x = np.array(x0, dtype=float)
    history = {'x': [x.copy()], 'f': [f(x)]}
    
    for i in range(max_iterations):
        grad = grad_f(x)
        x_new = x - learning_rate * grad
        
        # Check convergence
        if np.linalg.norm(x_new - x) < tolerance:
            break
            
        x = x_new
        history['x'].append(x.copy())
        history['f'].append(f(x))
    
    return x, history

# Example: Minimize quadratic function
def quadratic_optimization():
    # Function: f(x) = x^2 - 4x + 3
    def f(x):
        return x**2 - 4*x + 3
    
    def grad_f(x):
        return 2*x - 4
    
    # Gradient descent
    x_opt, history = gradient_descent(f, grad_f, x0=0.0, learning_rate=0.1)
    
    print("Quadratic Function Optimization:")
    print(f"Optimal x: {x_opt:.6f}")
    print(f"Optimal f(x): {f(x_opt):.6f}")
    print(f"Analytical solution: x = 2, f(x) = -1")
    
    # Plot optimization path
    x_range = np.linspace(-1, 5, 100)
    y_range = [f(x) for x in x_range]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_range, 'b-', linewidth=2, label='f(x) = x² - 4x + 3')
    plt.plot([x for x in history['x']], history['f'], 'ro-', 
             markersize=4, label='Gradient Descent Path')
    plt.plot(x_opt, f(x_opt), 'g*', markersize=15, label='Optimum')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gradient Descent Optimization')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

# Multivariable optimization
def multivariable_optimization():
    # Function: f(x,y) = x^2 + y^2 - 2x - 4y + 5
    def f(xy):
        x, y = xy
        return x**2 + y**2 - 2*x - 4*y + 5
    
    def grad_f(xy):
        x, y = xy
        return np.array([2*x - 2, 2*y - 4])
    
    # Gradient descent
    x_opt, history = gradient_descent(f, grad_f, x0=[0.0, 0.0], learning_rate=0.1)
    
    print("\nMultivariable Function Optimization:")
    print(f"Optimal (x,y): ({x_opt[0]:.6f}, {x_opt[1]:.6f})")
    print(f"Optimal f(x,y): {f(x_opt):.6f}")
    print(f"Analytical solution: (1, 2), f(1,2) = 0")
    
    # 3D visualization
    x_range = np.linspace(-2, 4, 50)
    y_range = np.linspace(-1, 5, 50)
    X, Y = np.meshgrid(x_range, y_range)
    Z = X**2 + Y**2 - 2*X - 4*Y + 5
    
    fig = plt.figure(figsize=(12, 5))
    
    # 3D surface plot
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot_surface(X, Y, Z, alpha=0.6, cmap='viridis')
    
    # Plot optimization path
    path_x = [xy[0] for xy in history['x']]
    path_y = [xy[1] for xy in history['x']]
    path_z = history['f']
    ax1.plot(path_x, path_y, path_z, 'ro-', markersize=4)
    ax1.plot([x_opt[0]], [x_opt[1]], [f(x_opt)], 'g*', markersize=15)
    
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('f(x,y)')
    ax1.set_title('3D Surface and Optimization Path')
    
    # Contour plot
    ax2 = fig.add_subplot(122)
    contour = ax2.contour(X, Y, Z, levels=20)
    ax2.clabel(contour, inline=True, fontsize=8)
    ax2.plot(path_x, path_y, 'ro-', markersize=4, label='Gradient Descent')
    ax2.plot(x_opt[0], x_opt[1], 'g*', markersize=15, label='Optimum')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_title('Contour Plot and Optimization Path')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# Neural network backpropagation example
def backpropagation_example():
    """Simple neural network with one hidden layer"""
    
    # Activation functions
    def sigmoid(x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    
    def sigmoid_derivative(x):
        s = sigmoid(x)
        return s * (1 - s)
    
    # Generate sample data
    np.random.seed(42)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # XOR problem
    y = np.array([[0], [1], [1], [0]])
    
    # Initialize weights
    input_size, hidden_size, output_size = 2, 4, 1
    W1 = np.random.randn(input_size, hidden_size) * 0.5
    b1 = np.zeros((1, hidden_size))
    W2 = np.random.randn(hidden_size, output_size) * 0.5
    b2 = np.zeros((1, output_size))
    
    learning_rate = 1.0
    epochs = 10000
    losses = []
    
    for epoch in range(epochs):
        # Forward pass
        z1 = X @ W1 + b1
        a1 = sigmoid(z1)
        z2 = a1 @ W2 + b2
        a2 = sigmoid(z2)
        
        # Compute loss
        loss = np.mean((a2 - y)**2)
        losses.append(loss)
        
        # Backward pass (chain rule)
        dL_da2 = 2 * (a2 - y) / len(X)
        dL_dz2 = dL_da2 * sigmoid_derivative(z2)
        dL_dW2 = a1.T @ dL_dz2
        dL_db2 = np.sum(dL_dz2, axis=0, keepdims=True)
        
        dL_da1 = dL_dz2 @ W2.T
        dL_dz1 = dL_da1 * sigmoid_derivative(z1)
        dL_dW1 = X.T @ dL_dz1
        dL_db1 = np.sum(dL_dz1, axis=0, keepdims=True)
        
        # Update weights
        W2 -= learning_rate * dL_dW2
        b2 -= learning_rate * dL_db2
        W1 -= learning_rate * dL_dW1
        b1 -= learning_rate * dL_db1
    
    # Final predictions
    z1 = X @ W1 + b1
    a1 = sigmoid(z1)
    z2 = a1 @ W2 + b2
    predictions = sigmoid(z2)
    
    print("Neural Network Backpropagation (XOR Problem):")
    print("Input -> Target -> Prediction")
    for i in range(len(X)):
        print(f"{X[i]} -> {y[i][0]:.0f} -> {predictions[i][0]:.3f}")
    
    # Plot loss curve
    plt.figure(figsize=(10, 6))
    plt.plot(losses)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Neural Network Training Loss')
    plt.grid(True, alpha=0.3)
    plt.yscale('log')
    plt.show()

# Lagrange multipliers example
def lagrange_multipliers_example():
    """Minimize f(x,y) = x^2 + y^2 subject to x + y = 1"""
    
    # Using scipy.optimize
    def objective(xy):
        x, y = xy
        return x**2 + y**2
    
    def constraint(xy):
        x, y = xy
        return x + y - 1
    
    # Constraint as dictionary
    cons = {'type': 'eq', 'fun': constraint}
    
    # Initial guess
    x0 = [0.0, 0.0]
    
    # Optimize
    result = minimize(objective, x0, method='SLSQP', constraints=cons)
    
    print("Lagrange Multipliers Example:")
    print(f"Minimize f(x,y) = x² + y² subject to x + y = 1")
    print(f"Optimal point: ({result.x[0]:.6f}, {result.x[1]:.6f})")
    print(f"Optimal value: {result.fun:.6f}")
    print(f"Analytical solution: (0.5, 0.5), f = 0.5")
    
    # Visualization
    x_range = np.linspace(-1, 2, 100)
    y_range = np.linspace(-1, 2, 100)
    X, Y = np.meshgrid(x_range, y_range)
    Z = X**2 + Y**2
    
    plt.figure(figsize=(8, 6))
    contour = plt.contour(X, Y, Z, levels=20)
    plt.clabel(contour, inline=True, fontsize=8)
    
    # Constraint line
    x_constraint = np.linspace(-1, 2, 100)
    y_constraint = 1 - x_constraint
    plt.plot(x_constraint, y_constraint, 'r-', linewidth=3, label='Constraint: x + y = 1')
    
    # Optimal point
    plt.plot(result.x[0], result.x[1], 'g*', markersize=15, label='Optimum')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Constrained Optimization with Lagrange Multipliers')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    print("=== Symbolic Derivatives ===")
    symbolic_derivatives()
    
    print("\n=== Quadratic Optimization ===")
    quadratic_optimization()
    
    print("\n=== Multivariable Optimization ===")
    multivariable_optimization()
    
    print("\n=== Neural Network Backpropagation ===")
    backpropagation_example()
    
    print("\n=== Lagrange Multipliers ===")
    lagrange_multipliers_example()
```

---

## 🎯 Key Takeaways

1. **Derivatives are Fundamental**: Every optimization algorithm uses derivatives
2. **Master the Chain Rule**: Critical for backpropagation in neural networks
3. **Understand Gradients**: Direction of steepest ascent/descent
4. **Learn Multivariable Calculus**: Most ML problems are multidimensional
5. **Practice Optimization**: Gradient descent is everywhere in ML
6. **Connect to ML**: See calculus in every learning algorithm

---

## 📚 Next Steps

After mastering calculus, proceed to:
1. **Optimization Theory** - Advanced optimization techniques
2. **Information Theory** - Entropy and information measures
3. **Numerical Methods** - Computational approaches
4. **Differential Equations** - Dynamic systems and continuous learning

---

## 🔗 Resources

- **Khan Academy**: Calculus fundamentals
- **3Blue1Brown**: "Essence of Calculus" series
- **MIT 18.01**: Single Variable Calculus
- **MIT 18.02**: Multivariable Calculus
- **SymPy Documentation**: Symbolic mathematics in Python

---

*Calculus is the engine of optimization in ML/AI. Master it to understand how algorithms learn and improve!*