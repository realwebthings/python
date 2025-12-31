# 🌳 Decision Trees - Complete Guide

## 📋 Overview
Decision trees create interpretable models by learning simple decision rules inferred from data features.

## 🎯 Key Concepts

### Tree Structure
- **Root Node**: Top of tree, contains all data
- **Internal Nodes**: Decision points (feature tests)
- **Leaf Nodes**: Final predictions
- **Branches**: Outcomes of decisions

### Decision Process
1. Start at root node
2. Follow branches based on feature values
3. Continue until reaching leaf node
4. Return leaf node's prediction

## 📊 Splitting Criteria

### Entropy (Information Theory)
```
Entropy(S) = -Σ p_i × log₂(p_i)
```
- **p_i**: Proportion of class i in set S
- **Range**: [0, log₂(classes)]
- **0**: Pure set (all same class)
- **Maximum**: Equally distributed classes

### Information Gain
```
IG(S, A) = Entropy(S) - Σ (|S_v|/|S|) × Entropy(S_v)
```
- **S**: Dataset
- **A**: Attribute/feature
- **S_v**: Subset where attribute A has value v
- **Goal**: Maximize information gain

### Gini Impurity
```
Gini(S) = 1 - Σ p_i²
```
- **Alternative to entropy**
- **Range**: [0, 1-1/classes]
- **0**: Pure set
- **Faster to compute** than entropy

### Gini Gain
```
Gini_Gain(S, A) = Gini(S) - Σ (|S_v|/|S|) × Gini(S_v)
```

## ✂️ Tree Pruning

### Why Prune?
- **Prevent overfitting**
- **Improve generalization**
- **Reduce model complexity**
- **Better interpretability**

### Pre-pruning (Early Stopping)
- **Max depth**: Limit tree depth
- **Min samples split**: Minimum samples to split node
- **Min samples leaf**: Minimum samples in leaf
- **Max features**: Limit features considered per split

### Post-pruning
- **Build full tree** first
- **Remove branches** that don't improve validation performance
- **Cost complexity pruning**: Balance accuracy vs complexity

## 🐍 Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.datasets import make_classification, load_iris
from sklearn.model_selection import train_test_split

class DecisionTreeNode:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature      # Feature index for splitting
        self.threshold = threshold  # Threshold value for splitting
        self.left = left           # Left subtree
        self.right = right         # Right subtree
        self.value = value         # Prediction value (for leaf nodes)

class DecisionTreeClassifier:
    def __init__(self, max_depth=10, min_samples_split=2, min_samples_leaf=1, 
                 criterion='gini', max_features=None):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.criterion = criterion
        self.max_features = max_features
        self.root = None
        self.feature_importances_ = None
    
    def entropy(self, y):
        """Calculate entropy of labels"""
        if len(y) == 0:
            return 0
        
        proportions = np.bincount(y) / len(y)
        proportions = proportions[proportions > 0]  # Remove zeros
        return -np.sum(proportions * np.log2(proportions))
    
    def gini_impurity(self, y):
        """Calculate Gini impurity of labels"""
        if len(y) == 0:
            return 0
        
        proportions = np.bincount(y) / len(y)
        return 1 - np.sum(proportions ** 2)
    
    def information_gain(self, y, y_left, y_right):
        """Calculate information gain from split"""
        if self.criterion == 'entropy':
            parent_impurity = self.entropy(y)
            left_impurity = self.entropy(y_left)
            right_impurity = self.entropy(y_right)
        else:  # gini
            parent_impurity = self.gini_impurity(y)
            left_impurity = self.gini_impurity(y_left)
            right_impurity = self.gini_impurity(y_right)
        
        n = len(y)
        n_left, n_right = len(y_left), len(y_right)
        
        if n_left == 0 or n_right == 0:
            return 0
        
        weighted_impurity = (n_left/n) * left_impurity + (n_right/n) * right_impurity
        return parent_impurity - weighted_impurity
    
    def best_split(self, X, y):
        """Find the best feature and threshold to split on"""
        n_samples, n_features = X.shape
        
        if self.max_features:
            features = np.random.choice(n_features, self.max_features, replace=False)
        else:
            features = range(n_features)
        
        best_gain = -1
        best_feature = None
        best_threshold = None
        
        for feature in features:
            thresholds = np.unique(X[:, feature])
            
            for threshold in thresholds:
                # Split data
                left_mask = X[:, feature] <= threshold
                right_mask = ~left_mask
                
                if np.sum(left_mask) < self.min_samples_leaf or \
                   np.sum(right_mask) < self.min_samples_leaf:
                    continue
                
                # Calculate information gain
                y_left, y_right = y[left_mask], y[right_mask]
                gain = self.information_gain(y, y_left, y_right)
                
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_threshold = threshold
        
        return best_feature, best_threshold, best_gain
    
    def build_tree(self, X, y, depth=0):
        """Recursively build the decision tree"""
        n_samples, n_features = X.shape
        n_classes = len(np.unique(y))
        
        # Stopping criteria
        if (depth >= self.max_depth or 
            n_classes == 1 or 
            n_samples < self.min_samples_split):
            # Create leaf node
            most_common_class = Counter(y).most_common(1)[0][0]
            return DecisionTreeNode(value=most_common_class)
        
        # Find best split
        best_feature, best_threshold, best_gain = self.best_split(X, y)
        
        if best_feature is None or best_gain == 0:
            # No good split found, create leaf
            most_common_class = Counter(y).most_common(1)[0][0]
            return DecisionTreeNode(value=most_common_class)
        
        # Split data
        left_mask = X[:, best_feature] <= best_threshold
        right_mask = ~left_mask
        
        # Recursively build subtrees
        left_subtree = self.build_tree(X[left_mask], y[left_mask], depth + 1)
        right_subtree = self.build_tree(X[right_mask], y[right_mask], depth + 1)
        
        return DecisionTreeNode(
            feature=best_feature,
            threshold=best_threshold,
            left=left_subtree,
            right=right_subtree
        )
    
    def fit(self, X, y):
        """Train the decision tree"""
        self.root = self.build_tree(X, y)
        self._calculate_feature_importances(X, y)
    
    def _calculate_feature_importances(self, X, y):
        """Calculate feature importances based on information gain"""
        n_features = X.shape[1]
        importances = np.zeros(n_features)
        
        def traverse(node, samples_ratio=1.0):
            if node.value is not None:  # Leaf node
                return
            
            # Calculate weighted information gain for this split
            left_mask = X[:, node.feature] <= node.threshold
            right_mask = ~left_mask
            
            y_left, y_right = y[left_mask], y[right_mask]
            gain = self.information_gain(y, y_left, y_right)
            
            importances[node.feature] += gain * samples_ratio
            
            # Recursively traverse subtrees
            left_ratio = np.sum(left_mask) / len(y) * samples_ratio
            right_ratio = np.sum(right_mask) / len(y) * samples_ratio
            
            traverse(node.left, left_ratio)
            traverse(node.right, right_ratio)
        
        traverse(self.root)
        self.feature_importances_ = importances / np.sum(importances) if np.sum(importances) > 0 else importances
    
    def predict_sample(self, x, node=None):
        """Predict single sample"""
        if node is None:
            node = self.root
        
        if node.value is not None:  # Leaf node
            return node.value
        
        if x[node.feature] <= node.threshold:
            return self.predict_sample(x, node.left)
        else:
            return self.predict_sample(x, node.right)
    
    def predict(self, X):
        """Predict multiple samples"""
        return np.array([self.predict_sample(x) for x in X])
    
    def print_tree(self, node=None, depth=0):
        """Print tree structure"""
        if node is None:
            node = self.root
        
        if node.value is not None:
            print("  " * depth + f"Predict: {node.value}")
        else:
            print("  " * depth + f"Feature {node.feature} <= {node.threshold:.3f}")
            print("  " * depth + "├─ True:")
            self.print_tree(node.left, depth + 1)
            print("  " * depth + "└─ False:")
            self.print_tree(node.right, depth + 1)

# Example usage
def decision_tree_example():
    # Generate sample data
    X, y = make_classification(n_samples=1000, n_features=4, n_informative=3, 
                             n_redundant=1, n_classes=3, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train decision tree
    dt = DecisionTreeClassifier(max_depth=5, min_samples_split=10, criterion='gini')
    dt.fit(X_train, y_train)
    
    # Make predictions
    y_pred = dt.predict(X_test)
    
    # Calculate accuracy
    accuracy = np.mean(y_test == y_pred)
    print(f"Decision Tree Accuracy: {accuracy:.3f}")
    
    # Print tree structure (first few levels)
    print("\nTree Structure:")
    dt.print_tree()
    
    # Feature importances
    print(f"\nFeature Importances: {dt.feature_importances_}")
    
    return dt, X_test, y_test, y_pred

def compare_splitting_criteria():
    """Compare entropy vs Gini impurity"""
    X, y = make_classification(n_samples=1000, n_features=2, n_redundant=0, 
                             n_informative=2, n_clusters_per_class=1, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train with different criteria
    dt_gini = DecisionTreeClassifier(max_depth=5, criterion='gini')
    dt_entropy = DecisionTreeClassifier(max_depth=5, criterion='entropy')
    
    dt_gini.fit(X_train, y_train)
    dt_entropy.fit(X_train, y_train)
    
    # Compare accuracies
    acc_gini = np.mean(y_test == dt_gini.predict(X_test))
    acc_entropy = np.mean(y_test == dt_entropy.predict(X_test))
    
    print(f"\nSplitting Criteria Comparison:")
    print(f"Gini Impurity Accuracy: {acc_gini:.3f}")
    print(f"Entropy Accuracy: {acc_entropy:.3f}")

def visualize_tree_depth_effect():
    """Show effect of tree depth on performance"""
    X, y = make_classification(n_samples=1000, n_features=2, n_redundant=0, 
                             n_informative=2, n_clusters_per_class=1, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    depths = range(1, 16)
    train_accuracies = []
    test_accuracies = []
    
    for depth in depths:
        dt = DecisionTreeClassifier(max_depth=depth)
        dt.fit(X_train, y_train)
        
        train_acc = np.mean(y_train == dt.predict(X_train))
        test_acc = np.mean(y_test == dt.predict(X_test))
        
        train_accuracies.append(train_acc)
        test_accuracies.append(test_acc)
    
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(depths, train_accuracies, 'o-', label='Training Accuracy')
    plt.plot(depths, test_accuracies, 's-', label='Test Accuracy')
    plt.xlabel('Max Depth')
    plt.ylabel('Accuracy')
    plt.title('Effect of Tree Depth on Performance')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    
    print(f"Best test accuracy: {max(test_accuracies):.3f} at depth {depths[np.argmax(test_accuracies)]}")

if __name__ == "__main__":
    decision_tree_example()
    compare_splitting_criteria()
    visualize_tree_depth_effect()
```

## 🔍 Key Insights

### Advantages
- **Highly interpretable**: Easy to understand and explain
- **No assumptions** about data distribution
- **Handles both numerical and categorical** features
- **Automatic feature selection**
- **Can capture non-linear relationships**
- **Robust to outliers**

### Disadvantages
- **Prone to overfitting**: Especially with deep trees
- **Unstable**: Small data changes can create very different trees
- **Biased toward features** with more levels
- **Difficulty with linear relationships**
- **Can create overly complex trees**

### When to Use
- **Need interpretable model**
- **Mixed data types** (numerical + categorical)
- **Non-linear relationships**
- **Feature interactions** are important
- **Baseline model** for comparison

## 🎯 Practice Exercises

1. Implement regression trees for continuous targets
2. Add support for categorical features
3. Implement cost-complexity pruning
4. Compare different splitting criteria on various datasets
5. Build a tree ensemble (Random Forest preview)

## 📚 Next Steps
- **Random Forests**: Ensemble of decision trees
- **Gradient Boosting**: Sequential tree building
- **XGBoost/LightGBM**: Advanced tree-based methods
- **Feature Engineering**: Creating better tree inputs

*Decision trees are the building blocks of powerful ensemble methods - understand them deeply!*