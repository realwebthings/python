# 📈 Linear Regression - Complete Guide

## 📋 Overview
Linear regression is the foundation of supervised learning, modeling relationships between features and continuous targets.

## 🎯 Key Concepts

### Simple Linear Regression
**Formula**: y = mx + b
- **m**: slope (coefficient)
- **b**: y-intercept (bias)
- **Goal**: Find best line through data points

### Multiple Linear Regression
**Formula**: y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ
- **Matrix Form**: y = Xβ + ε
- **Normal Equation**: β = (XᵀX)⁻¹Xᵀy

## 📊 Cost Functions

### Mean Squared Error (MSE)
```
MSE = (1/n) × Σ(yᵢ - ŷᵢ)²
```
- **Pros**: Differentiable, penalizes large errors
- **Cons**: Sensitive to outliers

### Mean Absolute Error (MAE)
```
MAE = (1/n) × Σ|yᵢ - ŷᵢ|
```
- **Pros**: Robust to outliers
- **Cons**: Not differentiable at zero

## ⚡ Gradient Descent

### Algorithm Steps
1. Initialize parameters randomly
2. Calculate predictions: ŷ = Xβ
3. Compute cost: J(β) = MSE
4. Calculate gradients: ∇J = (2/n)Xᵀ(Xβ - y)
5. Update parameters: β = β - α∇J
6. Repeat until convergence

### Learning Rate (α)
- **Too small**: Slow convergence
- **Too large**: Overshooting, divergence
- **Typical values**: 0.001, 0.01, 0.1

## 🐍 Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class LinearRegression:
    def __init__(self, learning_rate=0.01, max_iterations=1000):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.weights = None
        self.bias = None
        self.cost_history = []
    
    def fit(self, X, y):
        # Initialize parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Gradient descent
        for i in range(self.max_iterations):
            # Forward pass
            y_pred = self.predict(X)
            
            # Calculate cost
            cost = np.mean((y - y_pred) ** 2)
            self.cost_history.append(cost)
            
            # Calculate gradients
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)
            
            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
    
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
    
    def mse(self, y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)
    
    def mae(self, y_true, y_pred):
        return np.mean(np.abs(y_true - y_pred))
    
    def r2_score(self, y_true, y_pred):
        ss_res = np.sum((y_true - y_pred) ** 2)
        ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
        return 1 - (ss_res / ss_tot)

# Example usage
def linear_regression_example():
    # Generate sample data
    X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LinearRegression(learning_rate=0.01, max_iterations=1000)
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    mse = model.mse(y_test, y_pred)
    mae = model.mae(y_test, y_pred)
    r2 = model.r2_score(y_test, y_pred)
    
    print(f"MSE: {mse:.2f}")
    print(f"MAE: {mae:.2f}")
    print(f"R²: {r2:.2f}")
    
    # Plot results
    plt.figure(figsize=(12, 4))
    
    # Cost function
    plt.subplot(1, 2, 1)
    plt.plot(model.cost_history)
    plt.title('Cost Function Over Iterations')
    plt.xlabel('Iterations')
    plt.ylabel('MSE')
    
    # Predictions vs actual
    plt.subplot(1, 2, 2)
    plt.scatter(X_test, y_test, alpha=0.7, label='Actual')
    plt.scatter(X_test, y_pred, alpha=0.7, label='Predicted')
    plt.plot(X_test, y_pred, 'r-', alpha=0.8)
    plt.xlabel('Feature')
    plt.ylabel('Target')
    plt.title('Predictions vs Actual')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# Multiple regression example
def multiple_regression_example():
    # Generate data with multiple features
    X, y = make_regression(n_samples=1000, n_features=3, noise=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    model = LinearRegression(learning_rate=0.1, max_iterations=1000)
    model.fit(X_train_scaled, y_train)
    
    # Predictions
    y_pred = model.predict(X_test_scaled)
    
    # Metrics
    print(f"Multiple Regression Results:")
    print(f"MSE: {model.mse(y_test, y_pred):.2f}")
    print(f"R²: {model.r2_score(y_test, y_pred):.2f}")
    print(f"Weights: {model.weights}")
    print(f"Bias: {model.bias:.2f}")

if __name__ == "__main__":
    linear_regression_example()
    multiple_regression_example()
```

## 🔍 Key Insights

### When to Use Linear Regression
- **Linear relationships** between features and target
- **Continuous target** variables
- **Interpretable models** needed
- **Baseline model** for comparison

### Assumptions
1. **Linearity**: Relationship is linear
2. **Independence**: Observations are independent
3. **Homoscedasticity**: Constant variance of residuals
4. **Normality**: Residuals are normally distributed

### Common Issues
- **Overfitting**: Too many features relative to samples
- **Multicollinearity**: Highly correlated features
- **Outliers**: Can significantly affect the model
- **Non-linear relationships**: Linear model won't capture them

## 🎯 Practice Exercises

1. Implement gradient descent with different learning rates
2. Compare analytical solution (normal equation) vs gradient descent
3. Add regularization (Ridge/Lasso) to prevent overfitting
4. Handle categorical features with one-hot encoding
5. Implement polynomial regression for non-linear relationships

## 📚 Next Steps
- **Logistic Regression**: For classification problems
- **Regularization**: Ridge and Lasso regression
- **Polynomial Features**: Handling non-linear relationships
- **Feature Engineering**: Creating better input features

*Linear regression is your gateway to machine learning - master it well!*