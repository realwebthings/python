# 🔧 Feature Engineering - Complete Guide

## 📋 Overview
Feature engineering is the art of creating better input features for ML models. Often the difference between good and great models.

## 🎯 Core Concepts

### What is Feature Engineering?
- **Transform raw data** into meaningful features
- **Create new features** from existing ones
- **Select relevant features** for the model
- **Scale and normalize** features appropriately

### Why It Matters
- **Better features = Better models**
- **Can make simple models outperform complex ones**
- **Domain knowledge becomes competitive advantage**
- **Often more impactful than algorithm choice**

## 📏 Feature Scaling

### Min-Max Normalization
```
X_scaled = (X - X_min) / (X_max - X_min)
```
- **Range**: [0, 1]
- **Preserves relationships**
- **Sensitive to outliers**

### Standardization (Z-score)
```
X_scaled = (X - μ) / σ
```
- **Mean**: 0, **Std**: 1
- **Less sensitive to outliers**
- **Assumes normal distribution**

### Robust Scaling
```
X_scaled = (X - median) / IQR
```
- **Uses median and IQR**
- **Very robust to outliers**
- **Good for skewed data**

### Unit Vector Scaling
```
X_scaled = X / ||X||
```
- **Scales to unit norm**
- **Good for text/sparse data**
- **Preserves direction**

## 🎯 Feature Selection

### Filter Methods
**Statistical tests to rank features**

#### Correlation-based
```python
# Remove highly correlated features
correlation_matrix = df.corr().abs()
upper_triangle = correlation_matrix.where(
    np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool)
)
high_corr_features = [column for column in upper_triangle.columns 
                     if any(upper_triangle[column] > 0.95)]
```

#### Univariate Selection
```python
from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(score_func=f_classif, k=10)
X_selected = selector.fit_transform(X, y)
```

### Wrapper Methods
**Use model performance to select features**

#### Recursive Feature Elimination (RFE)
```python
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

estimator = LogisticRegression()
rfe = RFE(estimator, n_features_to_select=10)
X_selected = rfe.fit_transform(X, y)
```

### Embedded Methods
**Feature selection during model training**

#### L1 Regularization (Lasso)
```python
from sklearn.linear_model import LassoCV
lasso = LassoCV(cv=5)
lasso.fit(X, y)
selected_features = X.columns[lasso.coef_ != 0]
```

## 🔄 Feature Creation

### Polynomial Features
```python
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)
```

### Interaction Features
```python
# Manual interaction
df['feature1_x_feature2'] = df['feature1'] * df['feature2']

# Automatic interactions
from itertools import combinations
for feat1, feat2 in combinations(numeric_features, 2):
    df[f'{feat1}_x_{feat2}'] = df[feat1] * df[feat2]
```

### Binning/Discretization
```python
# Equal-width binning
pd.cut(df['age'], bins=5, labels=['Young', 'Adult', 'Middle', 'Senior', 'Elder'])

# Equal-frequency binning
pd.qcut(df['income'], q=4, labels=['Low', 'Medium', 'High', 'Very High'])
```

### Date/Time Features
```python
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.dayofweek
df['is_weekend'] = df['day_of_week'].isin([5, 6])
df['quarter'] = df['date'].dt.quarter
```

## 🐍 Python Implementation

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification, load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (StandardScaler, MinMaxScaler, RobustScaler, 
                                 PolynomialFeatures, LabelEncoder, OneHotEncoder)
from sklearn.feature_selection import (SelectKBest, f_classif, RFE, 
                                     mutual_info_classif)
from sklearn.linear_model import LogisticRegression, LassoCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class FeatureEngineer:
    def __init__(self):
        self.scalers = {}
        self.encoders = {}
        self.selected_features = None
        self.feature_importance = None
    
    def scale_features(self, X_train, X_test, method='standard'):
        """Scale features using different methods"""
        if method == 'standard':
            scaler = StandardScaler()
        elif method == 'minmax':
            scaler = MinMaxScaler()
        elif method == 'robust':
            scaler = RobustScaler()
        else:
            raise ValueError("Method must be 'standard', 'minmax', or 'robust'")
        
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        self.scalers[method] = scaler
        return X_train_scaled, X_test_scaled
    
    def create_polynomial_features(self, X_train, X_test, degree=2):
        """Create polynomial features"""
        poly = PolynomialFeatures(degree=degree, include_bias=False)
        X_train_poly = poly.fit_transform(X_train)
        X_test_poly = poly.transform(X_test)
        
        return X_train_poly, X_test_poly, poly.get_feature_names_out()
    
    def create_interaction_features(self, df, features):
        """Create interaction features between specified features"""
        from itertools import combinations
        
        new_features = df.copy()
        
        for feat1, feat2 in combinations(features, 2):
            # Multiplication
            new_features[f'{feat1}_x_{feat2}'] = df[feat1] * df[feat2]
            
            # Division (avoid division by zero)
            new_features[f'{feat1}_div_{feat2}'] = df[feat1] / (df[feat2] + 1e-8)
            
            # Addition
            new_features[f'{feat1}_plus_{feat2}'] = df[feat1] + df[feat2]
            
            # Difference
            new_features[f'{feat1}_minus_{feat2}'] = df[feat1] - df[feat2]
        
        return new_features
    
    def select_features_univariate(self, X_train, y_train, X_test, k=10):
        """Select features using univariate statistical tests"""
        selector = SelectKBest(score_func=f_classif, k=k)
        X_train_selected = selector.fit_transform(X_train, y_train)
        X_test_selected = selector.transform(X_test)
        
        self.selected_features = selector.get_support(indices=True)
        return X_train_selected, X_test_selected
    
    def select_features_rfe(self, X_train, y_train, X_test, n_features=10):
        """Select features using Recursive Feature Elimination"""
        estimator = LogisticRegression(random_state=42)
        rfe = RFE(estimator, n_features_to_select=n_features)
        
        X_train_selected = rfe.fit_transform(X_train, y_train)
        X_test_selected = rfe.transform(X_test)
        
        self.selected_features = rfe.get_support(indices=True)
        return X_train_selected, X_test_selected
    
    def select_features_lasso(self, X_train, y_train, X_test, alpha=None):
        """Select features using Lasso regularization"""
        if alpha is None:
            lasso = LassoCV(cv=5, random_state=42)
        else:
            from sklearn.linear_model import Lasso
            lasso = Lasso(alpha=alpha, random_state=42)
        
        lasso.fit(X_train, y_train)
        
        # Select features with non-zero coefficients
        selected_mask = lasso.coef_ != 0
        X_train_selected = X_train[:, selected_mask]
        X_test_selected = X_test[:, selected_mask]
        
        self.selected_features = np.where(selected_mask)[0]
        return X_train_selected, X_test_selected
    
    def get_feature_importance(self, X_train, y_train, feature_names=None):
        """Get feature importance using Random Forest"""
        rf = RandomForestClassifier(n_estimators=100, random_state=42)
        rf.fit(X_train, y_train)
        
        importance_df = pd.DataFrame({
            'feature': feature_names if feature_names is not None else range(X_train.shape[1]),
            'importance': rf.feature_importances_
        }).sort_values('importance', ascending=False)
        
        self.feature_importance = importance_df
        return importance_df
    
    def plot_feature_importance(self, top_n=20):
        """Plot feature importance"""
        if self.feature_importance is None:
            print("No feature importance calculated. Run get_feature_importance first.")
            return
        
        plt.figure(figsize=(10, 8))
        top_features = self.feature_importance.head(top_n)
        
        plt.barh(range(len(top_features)), top_features['importance'])
        plt.yticks(range(len(top_features)), top_features['feature'])
        plt.xlabel('Feature Importance')
        plt.title(f'Top {top_n} Feature Importances')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.show()

def compare_scaling_methods():
    """Compare different scaling methods"""
    # Generate sample data with different scales
    np.random.seed(42)
    feature1 = np.random.normal(0, 1, 1000)      # Standard normal
    feature2 = np.random.normal(100, 15, 1000)   # Different scale
    feature3 = np.random.exponential(2, 1000)    # Skewed distribution
    
    X = np.column_stack([feature1, feature2, feature3])
    feature_names = ['Feature 1', 'Feature 2', 'Feature 3']
    
    # Apply different scaling methods
    scalers = {
        'Original': None,
        'StandardScaler': StandardScaler(),
        'MinMaxScaler': MinMaxScaler(),
        'RobustScaler': RobustScaler()
    }
    
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    
    for i, (name, scaler) in enumerate(scalers.items()):
        if scaler is None:
            X_scaled = X
        else:
            X_scaled = scaler.fit_transform(X)
        
        # Box plots
        axes[0, i].boxplot(X_scaled, labels=feature_names)
        axes[0, i].set_title(f'{name} - Box Plot')
        axes[0, i].tick_params(axis='x', rotation=45)
        
        # Histograms for first feature
        axes[1, i].hist(X_scaled[:, 0], bins=30, alpha=0.7)
        axes[1, i].set_title(f'{name} - Feature 1 Distribution')
        axes[1, i].set_xlabel('Value')
        axes[1, i].set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()

def feature_selection_comparison():
    """Compare different feature selection methods"""
    # Generate sample data
    X, y = make_classification(n_samples=1000, n_features=50, n_informative=10, 
                             n_redundant=10, n_clusters_per_class=1, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Initialize feature engineer
    fe = FeatureEngineer()
    
    # Different selection methods
    methods = {
        'All Features': (X_train_scaled, X_test_scaled),
        'Univariate (k=20)': fe.select_features_univariate(X_train_scaled, y_train, X_test_scaled, k=20),
        'RFE (n=20)': fe.select_features_rfe(X_train_scaled, y_train, X_test_scaled, n_features=20),
        'Lasso': fe.select_features_lasso(X_train_scaled, y_train, X_test_scaled)
    }
    
    # Compare performance
    results = {}
    
    for name, (X_tr, X_te) in methods.items():
        # Train model
        model = LogisticRegression(random_state=42)
        model.fit(X_tr, y_train)
        
        # Evaluate
        y_pred = model.predict(X_te)
        accuracy = accuracy_score(y_test, y_pred)
        
        results[name] = {
            'accuracy': accuracy,
            'n_features': X_tr.shape[1]
        }
        
        print(f"{name}:")
        print(f"  Features: {X_tr.shape[1]}")
        print(f"  Accuracy: {accuracy:.4f}")
        print()
    
    # Plot results
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    methods_list = list(results.keys())
    accuracies = [results[m]['accuracy'] for m in methods_list]
    n_features = [results[m]['n_features'] for m in methods_list]
    
    # Accuracy comparison
    ax1.bar(methods_list, accuracies)
    ax1.set_title('Accuracy by Feature Selection Method')
    ax1.set_ylabel('Accuracy')
    ax1.tick_params(axis='x', rotation=45)
    
    # Number of features
    ax2.bar(methods_list, n_features)
    ax2.set_title('Number of Features Selected')
    ax2.set_ylabel('Number of Features')
    ax2.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.show()

def polynomial_features_example():
    """Demonstrate polynomial feature creation"""
    # Generate non-linear data
    np.random.seed(42)
    X = np.random.uniform(-2, 2, (200, 2))
    y = (X[:, 0]**2 + X[:, 1]**2 + X[:, 0]*X[:, 1] + 
         0.1*np.random.randn(200) > 1).astype(int)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Compare linear vs polynomial features
    models = {}
    
    # Linear features
    model_linear = LogisticRegression(random_state=42)
    model_linear.fit(X_train, y_train)
    acc_linear = accuracy_score(y_test, model_linear.predict(X_test))
    models['Linear'] = acc_linear
    
    # Polynomial features
    for degree in [2, 3]:
        poly = PolynomialFeatures(degree=degree, include_bias=False)
        X_train_poly = poly.fit_transform(X_train)
        X_test_poly = poly.transform(X_test)
        
        model_poly = LogisticRegression(random_state=42)
        model_poly.fit(X_train_poly, y_train)
        acc_poly = accuracy_score(y_test, model_poly.predict(X_test_poly))
        models[f'Polynomial (degree={degree})'] = acc_poly
    
    # Results
    print("Polynomial Features Comparison:")
    print("-" * 35)
    for name, acc in models.items():
        print(f"{name}: {acc:.4f}")
    
    # Plot results
    plt.figure(figsize=(8, 6))
    plt.bar(models.keys(), models.values())
    plt.title('Accuracy: Linear vs Polynomial Features')
    plt.ylabel('Accuracy')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("=== Scaling Methods Comparison ===")
    compare_scaling_methods()
    
    print("\n=== Feature Selection Comparison ===")
    feature_selection_comparison()
    
    print("\n=== Polynomial Features Example ===")
    polynomial_features_example()
```

## 🎯 Key Insights

### Feature Engineering Pipeline
1. **Understand the data** - EDA first
2. **Handle missing values** - Imputation strategies
3. **Scale features** - Choose appropriate method
4. **Create new features** - Domain knowledge + creativity
5. **Select relevant features** - Remove noise
6. **Validate improvements** - Always measure impact

### Best Practices
- **Start simple** - Basic features first
- **Domain knowledge** - Most important ingredient
- **Iterative process** - Build, test, refine
- **Avoid data leakage** - No future information
- **Cross-validate** - Ensure robust improvements

### Common Mistakes
- **Scaling before splitting** - Data leakage
- **Over-engineering** - Too many features
- **Ignoring business context** - Features must make sense
- **Not validating** - Improvements might be noise

## 🎯 Practice Exercises

1. Build a complete feature engineering pipeline
2. Create domain-specific features for different datasets
3. Implement automated feature selection
4. Handle categorical variables with different encoding methods
5. Build features for time series data

## 📚 Next Steps
- **Advanced Feature Engineering**: Text, images, time series
- **Automated Feature Engineering**: Tools like Featuretools
- **Feature Stores**: Managing features in production
- **Deep Feature Learning**: Neural networks for feature extraction

*Great features make great models - invest time in understanding your data!*