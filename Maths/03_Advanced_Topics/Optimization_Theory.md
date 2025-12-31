# 🎯 Optimization Theory for ML/AI

## 📋 Table of Contents
- [Why Optimization Theory is Critical](#why-optimization-theory-is-critical)
- [Convex Optimization](#convex-optimization)
- [Lagrange Multipliers](#lagrange-multipliers)
- [KKT Conditions](#kkt-conditions)
- [Gradient-Based Methods](#gradient-based-methods)
- [Second-Order Methods](#second-order-methods)
- [Constrained Optimization](#constrained-optimization)
- [Stochastic Optimization](#stochastic-optimization)
- [Applications in ML/AI](#applications-in-mlai)
- [Practice Problems](#practice-problems)
- [Python Implementation](#python-implementation)

---

## Why Optimization Theory is Critical

Optimization is the **mathematical heart** of machine learning:

### 🎯 **Critical Applications:**
- **Training ML Models**: Minimizing loss functions
- **Hyperparameter Tuning**: Finding optimal model configurations
- **Neural Network Training**: Backpropagation and gradient descent
- **Support Vector Machines**: Quadratic programming
- **Principal Component Analysis**: Eigenvalue optimization
- **Reinforcement Learning**: Policy optimization
- **Generative Models**: Adversarial optimization in GANs

---

## Convex Optimization

### Convex Sets
A set C is convex if for any x, y ∈ C and λ ∈ [0,1]:
λx + (1-λ)y ∈ C

**Examples:**
- Lines, planes, hyperplanes
- Balls and ellipsoids
- Polyhedra
- Positive semidefinite cone

### Convex Functions
A function f is convex if its domain is convex and for any x, y in domain and λ ∈ [0,1]:
f(λx + (1-λ)y) ≤ λf(x) + (1-λ)f(y)

**Properties:**
- **First-order condition**: f(y) ≥ f(x) + ∇f(x)ᵀ(y - x)
- **Second-order condition**: ∇²f(x) ⪰ 0 (positive semidefinite Hessian)

### Why Convexity Matters
- **Global Optimum**: Any local minimum is global minimum
- **Efficient Algorithms**: Polynomial-time solvable
- **Convergence Guarantees**: Algorithms converge to optimal solution

### Common Convex Functions
- **Linear**: f(x) = aᵀx + b
- **Quadratic**: f(x) = ½xᵀPx + qᵀx + r (P ⪰ 0)
- **Exponential**: f(x) = eᵃˣ
- **Logarithmic**: f(x) = -log(x) (x > 0)
- **Norms**: ||x||ₚ for p ≥ 1

---

## Lagrange Multipliers

### Equality Constraints
**Problem**: minimize f(x) subject to g(x) = 0

**Lagrangian**: L(x, λ) = f(x) - λᵀg(x)

**Optimality Conditions**:
- ∇ₓL = ∇f(x) - λᵀ∇g(x) = 0
- ∇λL = -g(x) = 0

**Geometric Interpretation**: At optimum, ∇f and ∇g are parallel.

### Method of Lagrange Multipliers
1. Form the Lagrangian L(x, λ)
2. Set ∇ₓL = 0 and ∇λL = 0
3. Solve the system of equations
4. Check second-order conditions

### Example: Minimize x² + y² subject to x + y = 1
**Solution**:
- L(x, y, λ) = x² + y² - λ(x + y - 1)
- ∂L/∂x = 2x - λ = 0 → x = λ/2
- ∂L/∂y = 2y - λ = 0 → y = λ/2
- ∂L/∂λ = -(x + y - 1) = 0 → λ/2 + λ/2 = 1 → λ = 1
- Solution: x = y = 1/2, minimum value = 1/2

---

## KKT Conditions

### Inequality Constraints
**Problem**: 
```
minimize f(x)
subject to gᵢ(x) ≤ 0, i = 1,...,m
           hⱼ(x) = 0, j = 1,...,p
```

**Lagrangian**: L(x, λ, μ) = f(x) + λᵀg(x) + μᵀh(x)

### KKT Conditions
For x* to be optimal, there exist λ*, μ* such that:

1. **Stationarity**: ∇f(x*) + λ*ᵀ∇g(x*) + μ*ᵀ∇h(x*) = 0
2. **Primal feasibility**: gᵢ(x*) ≤ 0, hⱼ(x*) = 0
3. **Dual feasibility**: λᵢ* ≥ 0
4. **Complementary slackness**: λᵢ*gᵢ(x*) = 0

### Complementary Slackness Interpretation
- If constraint gᵢ(x*) < 0 (inactive), then λᵢ* = 0
- If λᵢ* > 0, then constraint gᵢ(x*) = 0 (active)

---

## Gradient-Based Methods

### Gradient Descent
**Update Rule**: x_{k+1} = x_k - α_k ∇f(x_k)

**Convergence Rate**:
- **Convex functions**: O(1/k)
- **Strongly convex**: O(ρᵏ) for some ρ < 1

### Steepest Descent
Choose direction that minimizes f locally:
d_k = -∇f(x_k) / ||∇f(x_k)||

### Line Search Methods
**Exact Line Search**: α_k = argmin_α f(x_k - α∇f(x_k))

**Backtracking Line Search** (Armijo Rule):
- Start with α = 1
- While f(x_k - α∇f(x_k)) > f(x_k) - cα||∇f(x_k)||²:
  - α ← βα (typically β = 0.5, c = 10⁻⁴)

### Momentum Methods
**Heavy Ball Method**: 
```
v_{k+1} = βv_k - α∇f(x_k)
x_{k+1} = x_k + v_{k+1}
```

**Nesterov Acceleration**:
```
y_k = x_k + β(x_k - x_{k-1})
x_{k+1} = y_k - α∇f(y_k)
```

---

## Second-Order Methods

### Newton's Method
**Update Rule**: x_{k+1} = x_k - [∇²f(x_k)]⁻¹∇f(x_k)

**Advantages**:
- Quadratic convergence near optimum
- Scale-invariant

**Disadvantages**:
- Requires Hessian computation and inversion
- May not converge if Hessian is not positive definite

### Quasi-Newton Methods
Approximate Hessian using gradient information.

**BFGS Update**:
```
B_{k+1} = B_k + (y_k y_k^T)/(y_k^T s_k) - (B_k s_k s_k^T B_k)/(s_k^T B_k s_k)
```
where s_k = x_{k+1} - x_k, y_k = ∇f(x_{k+1}) - ∇f(x_k)

**L-BFGS**: Limited-memory version for large-scale problems.

### Gauss-Newton Method
For least squares problems: f(x) = ½||r(x)||²
**Update**: x_{k+1} = x_k - [J_k^T J_k]⁻¹ J_k^T r_k
where J_k is Jacobian of residual r(x).

---

## Constrained Optimization

### Penalty Methods
Transform constrained problem to unconstrained:
**Penalty Function**: P(x, ρ) = f(x) + ρ∑max(0, gᵢ(x))² + ρ∑hⱼ(x)²

### Barrier Methods
Keep iterates in feasible region:
**Barrier Function**: B(x, μ) = f(x) - μ∑log(-gᵢ(x))

### Augmented Lagrangian
Combine Lagrangian with penalty:
L_A(x, λ, ρ) = f(x) + λᵀg(x) + (ρ/2)||g(x)||²

### Sequential Quadratic Programming (SQP)
Solve sequence of quadratic subproblems:
```
minimize ∇f(x_k)^T d + ½d^T ∇²L(x_k, λ_k) d
subject to ∇g(x_k)^T d + g(x_k) = 0
```

---

## Stochastic Optimization

### Stochastic Gradient Descent (SGD)
**Update**: x_{k+1} = x_k - α_k ∇f_i(x_k)
where f_i is randomly selected component of objective.

### Mini-batch SGD
Use subset of data:
**Update**: x_{k+1} = x_k - α_k (1/|B|) ∑_{i∈B} ∇f_i(x_k)

### Adaptive Methods

**AdaGrad**:
```
G_k = G_{k-1} + ∇f(x_k) ∇f(x_k)^T
x_{k+1} = x_k - α G_k^{-1/2} ∇f(x_k)
```

**Adam**:
```
m_k = β₁m_{k-1} + (1-β₁)∇f(x_k)
v_k = β₂v_{k-1} + (1-β₂)∇f(x_k)²
x_{k+1} = x_k - α m̂_k / (√v̂_k + ε)
```
where m̂_k, v̂_k are bias-corrected estimates.

---

## Applications in ML/AI

### 1. Linear Regression
**Objective**: min ||Xθ - y||²
**Solution**: θ* = (X^T X)⁻¹ X^T y (normal equations)
**Gradient**: ∇J(θ) = X^T(Xθ - y)

### 2. Logistic Regression
**Objective**: min ∑[y_i log(1 + e^{-θ^T x_i}) + (1-y_i) log(1 + e^{θ^T x_i})]
**Gradient**: ∇J(θ) = X^T(σ(Xθ) - y)

### 3. Support Vector Machine
**Primal Problem**:
```
minimize ½||w||² + C∑ξᵢ
subject to yᵢ(w^T xᵢ + b) ≥ 1 - ξᵢ, ξᵢ ≥ 0
```

**Dual Problem**:
```
maximize ∑αᵢ - ½∑∑αᵢαⱼyᵢyⱼxᵢ^T xⱼ
subject to ∑αᵢyᵢ = 0, 0 ≤ αᵢ ≤ C
```

### 4. Neural Network Training
**Objective**: min (1/n)∑L(f(xᵢ; θ), yᵢ) + λR(θ)
**Method**: Backpropagation + SGD/Adam

### 5. Principal Component Analysis
**Objective**: max w^T Σ w subject to ||w|| = 1
**Solution**: w* = eigenvector of Σ with largest eigenvalue

---

## Practice Problems

### Problem 1: Convex Function
Prove that f(x) = x² + 2x + 1 is convex.

**Solution**:
f''(x) = 2 > 0 for all x, so f is convex.

### Problem 2: Lagrange Multipliers
Minimize f(x,y) = x² + 4y² subject to x + 2y = 3.

**Solution**:
- L(x,y,λ) = x² + 4y² - λ(x + 2y - 3)
- ∂L/∂x = 2x - λ = 0 → x = λ/2
- ∂L/∂y = 8y - 2λ = 0 → y = λ/4
- ∂L/∂λ = -(x + 2y - 3) = 0 → λ/2 + λ/2 = 3 → λ = 3
- Solution: x = 3/2, y = 3/4, minimum = 18/4 = 4.5

### Problem 3: KKT Conditions
Minimize f(x) = x² subject to x ≥ 1.

**Solution**:
- Constraint: g(x) = 1 - x ≤ 0
- KKT conditions: 2x - λ = 0, λ ≥ 0, λ(1-x) = 0, x ≥ 1
- If x > 1: λ = 0, so 2x = 0 (impossible)
- If x = 1: λ = 2 ≥ 0 ✓
- Solution: x* = 1, λ* = 2

---

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, minimize_scalar
from sklearn.datasets import make_regression
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings('ignore')

# Gradient descent implementation
class GradientDescent:
    def __init__(self, learning_rate=0.01, max_iterations=1000, tolerance=1e-6):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.history = {'x': [], 'f': [], 'grad_norm': []}
    
    def optimize(self, f, grad_f, x0):
        x = np.array(x0, dtype=float)
        
        for i in range(self.max_iterations):
            grad = grad_f(x)
            grad_norm = np.linalg.norm(grad)
            
            # Store history
            self.history['x'].append(x.copy())
            self.history['f'].append(f(x))
            self.history['grad_norm'].append(grad_norm)
            
            # Check convergence
            if grad_norm < self.tolerance:
                print(f"Converged after {i} iterations")
                break
            
            # Update
            x = x - self.learning_rate * grad
        
        return x

# Newton's method implementation
class NewtonMethod:
    def __init__(self, max_iterations=100, tolerance=1e-6):
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.history = {'x': [], 'f': [], 'grad_norm': []}
    
    def optimize(self, f, grad_f, hess_f, x0):
        x = np.array(x0, dtype=float)
        
        for i in range(self.max_iterations):
            grad = grad_f(x)
            hess = hess_f(x)
            grad_norm = np.linalg.norm(grad)
            
            # Store history
            self.history['x'].append(x.copy())
            self.history['f'].append(f(x))
            self.history['grad_norm'].append(grad_norm)
            
            # Check convergence
            if grad_norm < self.tolerance:
                print(f"Converged after {i} iterations")
                break
            
            # Newton step
            try:
                step = np.linalg.solve(hess, grad)
                x = x - step
            except np.linalg.LinAlgError:
                print("Hessian is singular, switching to gradient descent")
                x = x - 0.01 * grad
        
        return x

# Compare optimization methods
def compare_optimization_methods():
    # Quadratic function: f(x) = x^T A x + b^T x + c
    A = np.array([[2, 1], [1, 3]])
    b = np.array([1, 2])
    c = 1
    
    def f(x):
        return 0.5 * x.T @ A @ x + b.T @ x + c
    
    def grad_f(x):
        return A @ x + b
    
    def hess_f(x):
        return A
    
    # Analytical solution
    x_analytical = -np.linalg.solve(A, b)
    f_analytical = f(x_analytical)
    
    print("Optimization Methods Comparison")
    print(f"Analytical solution: x* = {x_analytical}, f* = {f_analytical:.6f}")
    
    # Initial point
    x0 = [2.0, 2.0]
    
    # Gradient descent
    gd = GradientDescent(learning_rate=0.1, max_iterations=1000)
    x_gd = gd.optimize(f, grad_f, x0)
    print(f"Gradient Descent: x* = {x_gd}, f* = {f(x_gd):.6f}")
    
    # Newton's method
    newton = NewtonMethod(max_iterations=100)
    x_newton = newton.optimize(f, grad_f, hess_f, x0)
    print(f"Newton's Method: x* = {x_newton}, f* = {f(x_newton):.6f}")
    
    # Visualization
    x_range = np.linspace(-2, 3, 100)
    y_range = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x_range, y_range)
    Z = np.zeros_like(X)
    
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = f(np.array([X[i, j], Y[i, j]]))
    
    plt.figure(figsize=(12, 5))
    
    # Gradient descent path
    plt.subplot(1, 2, 1)
    plt.contour(X, Y, Z, levels=20)
    gd_path = np.array(gd.history['x'])
    plt.plot(gd_path[:, 0], gd_path[:, 1], 'ro-', markersize=4, label='Gradient Descent')
    plt.plot(x_analytical[0], x_analytical[1], 'g*', markersize=15, label='Optimum')
    plt.xlabel('x₁')
    plt.ylabel('x₂')
    plt.title('Gradient Descent Path')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Newton's method path
    plt.subplot(1, 2, 2)
    plt.contour(X, Y, Z, levels=20)
    newton_path = np.array(newton.history['x'])
    plt.plot(newton_path[:, 0], newton_path[:, 1], 'bo-', markersize=4, label="Newton's Method")
    plt.plot(x_analytical[0], x_analytical[1], 'g*', markersize=15, label='Optimum')
    plt.xlabel('x₁')
    plt.ylabel('x₂')
    plt.title("Newton's Method Path")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Convergence comparison
    plt.figure(figsize=(10, 6))
    plt.semilogy(gd.history['grad_norm'], 'r-', label='Gradient Descent')
    plt.semilogy(newton.history['grad_norm'], 'b-', label="Newton's Method")
    plt.xlabel('Iteration')
    plt.ylabel('Gradient Norm')
    plt.title('Convergence Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

# Constrained optimization example
def constrained_optimization_example():
    """Minimize f(x,y) = x² + y² subject to x + y = 1"""
    
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
    
    # Optimize using different methods
    methods = ['SLSQP', 'trust-constr']
    
    print("Constrained Optimization: min x² + y² subject to x + y = 1")
    print("Analytical solution: x = y = 0.5, f = 0.5")
    
    for method in methods:
        result = minimize(objective, x0, method=method, constraints=cons)
        print(f"{method}: x* = ({result.x[0]:.6f}, {result.x[1]:.6f}), f* = {result.fun:.6f}")

# Stochastic gradient descent for linear regression
def sgd_linear_regression():
    # Generate data
    np.random.seed(42)
    X, y = make_regression(n_samples=1000, n_features=2, noise=10, random_state=42)
    
    # Add bias term
    X = np.column_stack([np.ones(X.shape[0]), X])
    n_samples, n_features = X.shape
    
    # Initialize parameters
    theta = np.random.randn(n_features) * 0.01
    
    # SGD parameters
    learning_rate = 0.01
    epochs = 100
    batch_size = 32
    
    # Track loss
    losses = []
    
    for epoch in range(epochs):
        # Shuffle data
        indices = np.random.permutation(n_samples)
        X_shuffled = X[indices]
        y_shuffled = y[indices]
        
        epoch_loss = 0
        n_batches = 0
        
        # Mini-batch SGD
        for i in range(0, n_samples, batch_size):
            batch_X = X_shuffled[i:i+batch_size]
            batch_y = y_shuffled[i:i+batch_size]
            
            # Forward pass
            predictions = batch_X @ theta
            loss = np.mean((predictions - batch_y)**2)
            epoch_loss += loss
            n_batches += 1
            
            # Backward pass
            gradient = (2/len(batch_X)) * batch_X.T @ (predictions - batch_y)
            
            # Update parameters
            theta = theta - learning_rate * gradient
        
        losses.append(epoch_loss / n_batches)
    
    # Compare with analytical solution
    theta_analytical = np.linalg.solve(X.T @ X, X.T @ y)
    
    print("Stochastic Gradient Descent for Linear Regression")
    print(f"SGD solution: {theta}")
    print(f"Analytical solution: {theta_analytical}")
    print(f"Difference: {np.linalg.norm(theta - theta_analytical):.6f}")
    
    # Plot loss curve
    plt.figure(figsize=(10, 6))
    plt.plot(losses)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('SGD Training Loss')
    plt.grid(True, alpha=0.3)
    plt.show()

# Adam optimizer implementation
class AdamOptimizer:
    def __init__(self, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.learning_rate = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.m = None
        self.v = None
        self.t = 0
    
    def update(self, params, gradients):
        if self.m is None:
            self.m = np.zeros_like(params)
            self.v = np.zeros_like(params)
        
        self.t += 1
        
        # Update biased first moment estimate
        self.m = self.beta1 * self.m + (1 - self.beta1) * gradients
        
        # Update biased second raw moment estimate
        self.v = self.beta2 * self.v + (1 - self.beta2) * gradients**2
        
        # Compute bias-corrected first moment estimate
        m_hat = self.m / (1 - self.beta1**self.t)
        
        # Compute bias-corrected second raw moment estimate
        v_hat = self.v / (1 - self.beta2**self.t)
        
        # Update parameters
        params = params - self.learning_rate * m_hat / (np.sqrt(v_hat) + self.epsilon)
        
        return params

def adam_vs_sgd():
    """Compare Adam and SGD on a simple optimization problem"""
    
    # Rosenbrock function: f(x,y) = (a-x)² + b(y-x²)²
    a, b = 1, 100
    
    def f(xy):
        x, y = xy
        return (a - x)**2 + b * (y - x**2)**2
    
    def grad_f(xy):
        x, y = xy
        df_dx = -2*(a - x) - 4*b*x*(y - x**2)
        df_dy = 2*b*(y - x**2)
        return np.array([df_dx, df_dy])
    
    # Initial point
    x0 = np.array([-1.0, 1.0])
    
    # SGD
    x_sgd = x0.copy()
    sgd_path = [x_sgd.copy()]
    learning_rate_sgd = 0.001
    
    # Adam
    x_adam = x0.copy()
    adam_path = [x_adam.copy()]
    adam = AdamOptimizer(learning_rate=0.01)
    
    # Optimization
    for i in range(1000):
        # SGD update
        grad_sgd = grad_f(x_sgd)
        x_sgd = x_sgd - learning_rate_sgd * grad_sgd
        sgd_path.append(x_sgd.copy())
        
        # Adam update
        grad_adam = grad_f(x_adam)
        x_adam = adam.update(x_adam, grad_adam)
        adam_path.append(x_adam.copy())
    
    print("Adam vs SGD on Rosenbrock Function")
    print(f"True minimum: (1, 1), f = 0")
    print(f"SGD final: ({x_sgd[0]:.6f}, {x_sgd[1]:.6f}), f = {f(x_sgd):.6f}")
    print(f"Adam final: ({x_adam[0]:.6f}, {x_adam[1]:.6f}), f = {f(x_adam):.6f}")
    
    # Visualization
    x_range = np.linspace(-2, 2, 100)
    y_range = np.linspace(-1, 3, 100)
    X, Y = np.meshgrid(x_range, y_range)
    Z = (a - X)**2 + b * (Y - X**2)**2
    
    plt.figure(figsize=(12, 5))
    
    # SGD path
    plt.subplot(1, 2, 1)
    plt.contour(X, Y, Z, levels=np.logspace(0, 3, 20))
    sgd_path = np.array(sgd_path)
    plt.plot(sgd_path[:, 0], sgd_path[:, 1], 'r-', alpha=0.7, label='SGD')
    plt.plot(1, 1, 'g*', markersize=15, label='True minimum')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('SGD on Rosenbrock Function')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Adam path
    plt.subplot(1, 2, 2)
    plt.contour(X, Y, Z, levels=np.logspace(0, 3, 20))
    adam_path = np.array(adam_path)
    plt.plot(adam_path[:, 0], adam_path[:, 1], 'b-', alpha=0.7, label='Adam')
    plt.plot(1, 1, 'g*', markersize=15, label='True minimum')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Adam on Rosenbrock Function')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("=== Optimization Methods Comparison ===")
    compare_optimization_methods()
    
    print("\n=== Constrained Optimization ===")
    constrained_optimization_example()
    
    print("\n=== Stochastic Gradient Descent ===")
    sgd_linear_regression()
    
    print("\n=== Adam vs SGD ===")
    adam_vs_sgd()
```

---

## 🎯 Key Takeaways

1. **Convexity is Crucial**: Convex problems have global optima and efficient algorithms
2. **Understand KKT Conditions**: Essential for constrained optimization
3. **Master Gradient Methods**: Foundation of all ML training algorithms
4. **Learn Second-Order Methods**: Faster convergence but higher computational cost
5. **Practice Stochastic Methods**: Critical for large-scale ML problems
6. **Connect to ML**: Every ML algorithm is an optimization problem

---

## 📚 Next Steps

After mastering optimization theory, proceed to:
1. **Information Theory** - Entropy and information measures
2. **Game Theory** - Multi-agent optimization
3. **Variational Methods** - Calculus of variations
4. **Numerical Optimization** - Computational aspects

---

## 🔗 Resources

- **Boyd & Vandenberghe**: "Convex Optimization" (free online)
- **Nocedal & Wright**: "Numerical Optimization"
- **Bertsekas**: "Nonlinear Programming"
- **SciPy Documentation**: Optimization functions
- **CVX**: Convex optimization modeling

---

*Optimization theory is the mathematical foundation that makes machine learning possible. Master it to understand how algorithms find the best solutions!*