# 🎯 Logistic Regression - Complete Guide

## 📋 Overview
Logistic regression is the go-to algorithm for classification problems, using the sigmoid function to model probabilities.

## 🎯 Key Concepts

### Binary Classification
**Goal**: Predict probability that instance belongs to positive class
**Output**: P(y=1|x) ∈ [0,1]

### Sigmoid Function
```
σ(z) = 1 / (1 + e^(-z))
where z = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ
```

**Properties**:
- Maps any real number to (0,1)
- S-shaped curve
- σ(0) = 0.5 (decision boundary)

### Decision Rule
```
ŷ = 1 if P(y=1|x) ≥ 0.5
ŷ = 0 if P(y=1|x) < 0.5
```

## 📊 Cross-Entropy Loss

### Binary Cross-Entropy
```
J(β) = -(1/n) × Σ[yᵢlog(ŷᵢ) + (1-yᵢ)log(1-ŷᵢ)]
```

**Why Cross-Entropy?**
- Penalizes wrong predictions heavily
- Convex function (guaranteed global minimum)
- Probabilistic interpretation

### Gradient Calculation
```
∇J = (1/n) × Xᵀ(σ(Xβ) - y)
```

## 🔄 Multiclass Classification

### One-vs-Rest (OvR)
- Train K binary classifiers
- Each classifier: class i vs all others
- Prediction: class with highest probability

### Softmax Function
```
P(y=k|x) = e^(z_k) / Σe^(z_j)
```
- Generalizes sigmoid to multiple classes
- Outputs sum to 1 (probability distribution)

## 🐍 Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class LogisticRegression:
    def __init__(self, learning_rate=0.01, max_iterations=1000):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.weights = None
        self.bias = None
        self.cost_history = []
    
    def sigmoid(self, z):
        # Clip z to prevent overflow
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))
    
    def fit(self, X, y):
        # Initialize parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Gradient descent
        for i in range(self.max_iterations):
            # Forward pass
            z = np.dot(X, self.weights) + self.bias
            y_pred = self.sigmoid(z)
            
            # Calculate cost (cross-entropy)
            cost = self.cross_entropy_loss(y, y_pred)
            self.cost_history.append(cost)
            
            # Calculate gradients
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)
            
            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
    
    def predict_proba(self, X):
        z = np.dot(X, self.weights) + self.bias
        return self.sigmoid(z)
    
    def predict(self, X):
        return (self.predict_proba(X) >= 0.5).astype(int)
    
    def cross_entropy_loss(self, y_true, y_pred):
        # Clip predictions to prevent log(0)
        y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)
        return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    
    def accuracy(self, y_true, y_pred):
        return np.mean(y_true == y_pred)

class MulticlassLogisticRegression:
    def __init__(self, learning_rate=0.01, max_iterations=1000):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.weights = None
        self.bias = None
        self.classes = None
    
    def softmax(self, z):
        # Subtract max for numerical stability
        z_stable = z - np.max(z, axis=1, keepdims=True)
        exp_z = np.exp(z_stable)
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)
    
    def one_hot_encode(self, y):
        n_classes = len(self.classes)
        n_samples = len(y)
        one_hot = np.zeros((n_samples, n_classes))
        for i, class_label in enumerate(y):
            class_idx = np.where(self.classes == class_label)[0][0]
            one_hot[i, class_idx] = 1
        return one_hot
    
    def fit(self, X, y):
        # Get unique classes
        self.classes = np.unique(y)
        n_classes = len(self.classes)
        n_samples, n_features = X.shape
        
        # Initialize parameters
        self.weights = np.random.normal(0, 0.01, (n_features, n_classes))
        self.bias = np.zeros(n_classes)
        
        # One-hot encode labels
        y_one_hot = self.one_hot_encode(y)
        
        # Gradient descent
        for i in range(self.max_iterations):
            # Forward pass
            z = np.dot(X, self.weights) + self.bias
            y_pred = self.softmax(z)
            
            # Calculate gradients
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y_one_hot))
            db = (1/n_samples) * np.sum(y_pred - y_one_hot, axis=0)
            
            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
    
    def predict_proba(self, X):
        z = np.dot(X, self.weights) + self.bias
        return self.softmax(z)
    
    def predict(self, X):
        probabilities = self.predict_proba(X)
        class_indices = np.argmax(probabilities, axis=1)
        return self.classes[class_indices]

# Binary classification example
def binary_classification_example():
    # Generate sample data
    X, y = make_classification(n_samples=1000, n_features=2, n_redundant=0, 
                             n_informative=2, n_clusters_per_class=1, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    model = LogisticRegression(learning_rate=0.1, max_iterations=1000)
    model.fit(X_train_scaled, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test_scaled)
    y_pred_proba = model.predict_proba(X_test_scaled)
    
    # Calculate metrics
    accuracy = model.accuracy(y_test, y_pred)
    loss = model.cross_entropy_loss(y_test, y_pred_proba)
    
    print(f"Binary Classification Results:")
    print(f"Accuracy: {accuracy:.3f}")
    print(f"Cross-entropy Loss: {loss:.3f}")
    
    # Plot results
    plt.figure(figsize=(15, 5))
    
    # Cost function
    plt.subplot(1, 3, 1)
    plt.plot(model.cost_history)
    plt.title('Cost Function Over Iterations')
    plt.xlabel('Iterations')
    plt.ylabel('Cross-entropy Loss')
    
    # Decision boundary
    plt.subplot(1, 3, 2)
    plot_decision_boundary(model, X_test_scaled, y_test, scaler)
    
    # Sigmoid function
    plt.subplot(1, 3, 3)
    z = np.linspace(-10, 10, 100)
    sigmoid_values = model.sigmoid(z)
    plt.plot(z, sigmoid_values)
    plt.title('Sigmoid Function')
    plt.xlabel('z')
    plt.ylabel('σ(z)')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def plot_decision_boundary(model, X, y, scaler):
    h = 0.02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    
    mesh_points = np.c_[xx.ravel(), yy.ravel()]
    Z = model.predict_proba(mesh_points)
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, levels=50, alpha=0.8, cmap=plt.cm.RdYlBu)
    scatter = plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdYlBu, edgecolors='black')
    plt.colorbar(scatter)
    plt.title('Decision Boundary')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')

# Multiclass classification example
def multiclass_classification_example():
    # Load iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    model = MulticlassLogisticRegression(learning_rate=0.1, max_iterations=1000)
    model.fit(X_train_scaled, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test_scaled)
    y_pred_proba = model.predict_proba(X_test_scaled)
    
    # Calculate accuracy
    accuracy = np.mean(y_test == y_pred)
    
    print(f"\nMulticlass Classification Results:")
    print(f"Accuracy: {accuracy:.3f}")
    print(f"Classes: {model.classes}")
    print(f"Sample predictions: {y_pred[:10]}")
    print(f"Sample probabilities:\n{y_pred_proba[:5]}")

if __name__ == "__main__":
    binary_classification_example()
    multiclass_classification_example()
```

## 🔍 Key Insights

### Advantages
- **Probabilistic output**: Provides confidence scores
- **No assumptions** about feature distributions
- **Less prone to outliers** than linear regression
- **Fast training** and prediction
- **Interpretable coefficients**

### Disadvantages
- **Assumes linear decision boundary**
- **Sensitive to feature scaling**
- **Requires large sample sizes** for stable results
- **Can struggle with complex relationships**

### When to Use
- **Binary or multiclass classification**
- **Need probability estimates**
- **Linear separable data**
- **Baseline model** for comparison
- **Interpretability** is important

## 🎯 Practice Exercises

1. Implement regularized logistic regression (L1/L2)
2. Compare sigmoid vs tanh activation functions
3. Handle imbalanced datasets with class weights
4. Implement feature selection using coefficient magnitudes
5. Build a spam email classifier

## 📚 Next Steps
- **Decision Trees**: Handle non-linear relationships
- **SVM**: Alternative classification approach
- **Neural Networks**: More complex decision boundaries
- **Ensemble Methods**: Combine multiple models

*Logistic regression is the foundation of classification - master it to understand all other classifiers!*