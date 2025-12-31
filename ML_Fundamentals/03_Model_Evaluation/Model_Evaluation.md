# 📊 Model Evaluation & Metrics - Complete Guide

## 📋 Overview
Proper model evaluation is crucial for building reliable ML systems. This guide covers all essential evaluation techniques and metrics.

## 🔄 Data Splitting Strategies

### Train/Test Split
```python
# Basic split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
- **Training Set**: 60-80% of data
- **Test Set**: 20-40% of data
- **Use**: Final model evaluation

### Train/Validation/Test Split
```python
# Three-way split
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
```
- **Training**: 60% (model training)
- **Validation**: 20% (hyperparameter tuning)
- **Test**: 20% (final evaluation)

## 🔄 Cross-Validation

### K-Fold Cross-Validation
```python
from sklearn.model_selection import KFold, cross_val_score

kfold = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')
```

### Stratified K-Fold
```python
from sklearn.model_selection import StratifiedKFold

skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skfold, scoring='accuracy')
```
- **Maintains class distribution** in each fold
- **Better for imbalanced datasets**

### Leave-One-Out (LOO)
```python
from sklearn.model_selection import LeaveOneOut

loo = LeaveOneOut()
scores = cross_val_score(model, X, y, cv=loo, scoring='accuracy')
```
- **Uses n-1 samples for training, 1 for testing**
- **Computationally expensive**
- **Good for small datasets**

## 📈 Classification Metrics

### Confusion Matrix
```
                Predicted
                0    1
Actual    0    TN   FP
          1    FN   TP
```
- **TP**: True Positives
- **TN**: True Negatives  
- **FP**: False Positives (Type I Error)
- **FN**: False Negatives (Type II Error)

### Accuracy
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```
- **Range**: [0, 1]
- **Good for balanced datasets**
- **Misleading for imbalanced data**

### Precision
```
Precision = TP / (TP + FP)
```
- **"Of all positive predictions, how many were correct?"**
- **Important when FP is costly**
- **Example**: Medical diagnosis

### Recall (Sensitivity)
```
Recall = TP / (TP + FN)
```
- **"Of all actual positives, how many were found?"**
- **Important when FN is costly**
- **Example**: Fraud detection

### F1-Score
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```
- **Harmonic mean of precision and recall**
- **Good for imbalanced datasets**
- **Single metric combining both concerns**

### Specificity
```
Specificity = TN / (TN + FP)
```
- **True negative rate**
- **"Of all actual negatives, how many were correctly identified?"**

### ROC Curve & AUC
- **ROC**: Receiver Operating Characteristic
- **Plots**: True Positive Rate vs False Positive Rate
- **AUC**: Area Under Curve
- **Range**: [0, 1], 0.5 = random, 1.0 = perfect

## 📉 Regression Metrics

### Mean Squared Error (MSE)
```
MSE = (1/n) × Σ(y_true - y_pred)²
```
- **Penalizes large errors heavily**
- **Same units as target squared**
- **Sensitive to outliers**

### Root Mean Squared Error (RMSE)
```
RMSE = √MSE
```
- **Same units as target**
- **Interpretable scale**
- **Still sensitive to outliers**

### Mean Absolute Error (MAE)
```
MAE = (1/n) × Σ|y_true - y_pred|
```
- **Robust to outliers**
- **Same units as target**
- **Linear penalty for errors**

### R² Score (Coefficient of Determination)
```
R² = 1 - (SS_res / SS_tot)
SS_res = Σ(y_true - y_pred)²
SS_tot = Σ(y_true - y_mean)²
```
- **Range**: (-∞, 1]
- **1.0**: Perfect predictions
- **0.0**: As good as predicting mean
- **Negative**: Worse than predicting mean

## 🐍 Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, make_regression
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import (confusion_matrix, classification_report, roc_curve, 
                           auc, precision_recall_curve, mean_squared_error, 
                           mean_absolute_error, r2_score)
import seaborn as sns

class ModelEvaluator:
    def __init__(self):
        self.classification_metrics = {}
        self.regression_metrics = {}
    
    def evaluate_classification(self, y_true, y_pred, y_pred_proba=None):
        """Comprehensive classification evaluation"""
        # Confusion matrix
        cm = confusion_matrix(y_true, y_pred)
        
        # Basic metrics from confusion matrix
        if len(np.unique(y_true)) == 2:  # Binary classification
            tn, fp, fn, tp = cm.ravel()
            
            accuracy = (tp + tn) / (tp + tn + fp + fn)
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0
            specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
            f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
            
            self.classification_metrics = {
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall,
                'specificity': specificity,
                'f1_score': f1,
                'confusion_matrix': cm
            }
            
            # ROC curve and AUC
            if y_pred_proba is not None:
                fpr, tpr, _ = roc_curve(y_true, y_pred_proba)
                roc_auc = auc(fpr, tpr)
                self.classification_metrics['roc_auc'] = roc_auc
                self.classification_metrics['fpr'] = fpr
                self.classification_metrics['tpr'] = tpr
        
        else:  # Multiclass
            from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
            
            accuracy = accuracy_score(y_true, y_pred)
            precision = precision_score(y_true, y_pred, average='weighted')
            recall = recall_score(y_true, y_pred, average='weighted')
            f1 = f1_score(y_true, y_pred, average='weighted')
            
            self.classification_metrics = {
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall,
                'f1_score': f1,
                'confusion_matrix': cm
            }
        
        return self.classification_metrics
    
    def evaluate_regression(self, y_true, y_pred):
        """Comprehensive regression evaluation"""
        mse = mean_squared_error(y_true, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)
        
        # Additional metrics
        mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100  # Mean Absolute Percentage Error
        residuals = y_true - y_pred
        
        self.regression_metrics = {
            'mse': mse,
            'rmse': rmse,
            'mae': mae,
            'r2_score': r2,
            'mape': mape,
            'residuals': residuals
        }
        
        return self.regression_metrics
    
    def plot_classification_results(self, y_true, y_pred, y_pred_proba=None):
        """Plot classification evaluation results"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Confusion Matrix
        cm = self.classification_metrics['confusion_matrix']
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0,0])
        axes[0,0].set_title('Confusion Matrix')
        axes[0,0].set_xlabel('Predicted')
        axes[0,0].set_ylabel('Actual')
        
        # Metrics bar plot
        metrics = ['accuracy', 'precision', 'recall', 'f1_score']
        values = [self.classification_metrics[m] for m in metrics]
        axes[0,1].bar(metrics, values)
        axes[0,1].set_title('Classification Metrics')
        axes[0,1].set_ylim(0, 1)
        axes[0,1].tick_params(axis='x', rotation=45)
        
        # ROC Curve (if probabilities available)
        if 'roc_auc' in self.classification_metrics:
            fpr = self.classification_metrics['fpr']
            tpr = self.classification_metrics['tpr']
            roc_auc = self.classification_metrics['roc_auc']
            
            axes[1,0].plot(fpr, tpr, color='darkorange', lw=2, 
                          label=f'ROC curve (AUC = {roc_auc:.2f})')
            axes[1,0].plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
            axes[1,0].set_xlim([0.0, 1.0])
            axes[1,0].set_ylim([0.0, 1.05])
            axes[1,0].set_xlabel('False Positive Rate')
            axes[1,0].set_ylabel('True Positive Rate')
            axes[1,0].set_title('ROC Curve')
            axes[1,0].legend(loc="lower right")
        
        # Prediction distribution
        axes[1,1].hist(y_pred[y_true == 0], alpha=0.7, label='Class 0', bins=20)
        axes[1,1].hist(y_pred[y_true == 1], alpha=0.7, label='Class 1', bins=20)
        axes[1,1].set_title('Prediction Distribution by Class')
        axes[1,1].set_xlabel('Predicted Probability')
        axes[1,1].set_ylabel('Frequency')
        axes[1,1].legend()
        
        plt.tight_layout()
        plt.show()
    
    def plot_regression_results(self, y_true, y_pred):
        """Plot regression evaluation results"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Actual vs Predicted
        axes[0,0].scatter(y_true, y_pred, alpha=0.6)
        axes[0,0].plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', lw=2)
        axes[0,0].set_xlabel('Actual Values')
        axes[0,0].set_ylabel('Predicted Values')
        axes[0,0].set_title('Actual vs Predicted')
        
        # Residuals plot
        residuals = self.regression_metrics['residuals']
        axes[0,1].scatter(y_pred, residuals, alpha=0.6)
        axes[0,1].axhline(y=0, color='r', linestyle='--')
        axes[0,1].set_xlabel('Predicted Values')
        axes[0,1].set_ylabel('Residuals')
        axes[0,1].set_title('Residuals Plot')
        
        # Residuals histogram
        axes[1,0].hist(residuals, bins=30, alpha=0.7)
        axes[1,0].set_xlabel('Residuals')
        axes[1,0].set_ylabel('Frequency')
        axes[1,0].set_title('Residuals Distribution')
        
        # Metrics text
        metrics_text = f"""
        MSE: {self.regression_metrics['mse']:.4f}
        RMSE: {self.regression_metrics['rmse']:.4f}
        MAE: {self.regression_metrics['mae']:.4f}
        R²: {self.regression_metrics['r2_score']:.4f}
        MAPE: {self.regression_metrics['mape']:.2f}%
        """
        axes[1,1].text(0.1, 0.5, metrics_text, fontsize=12, verticalalignment='center')
        axes[1,1].set_xlim(0, 1)
        axes[1,1].set_ylim(0, 1)
        axes[1,1].axis('off')
        axes[1,1].set_title('Regression Metrics')
        
        plt.tight_layout()
        plt.show()

def cross_validation_example():
    """Demonstrate cross-validation techniques"""
    # Generate sample data
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, 
                             n_redundant=10, n_classes=2, random_state=42)
    
    # Create model
    model = LogisticRegression(random_state=42)
    
    # Different CV strategies
    cv_strategies = {
        'K-Fold (5)': StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
        'K-Fold (10)': StratifiedKFold(n_splits=10, shuffle=True, random_state=42),
    }
    
    print("Cross-Validation Results:")
    print("-" * 40)
    
    for name, cv in cv_strategies.items():
        scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')
        print(f"{name}:")
        print(f"  Mean Accuracy: {scores.mean():.4f} (+/- {scores.std() * 2:.4f})")
        print(f"  Individual Scores: {scores}")
        print()

def classification_example():
    """Complete classification evaluation example"""
    # Generate sample data
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=15, 
                             n_redundant=5, n_classes=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    # Evaluate
    evaluator = ModelEvaluator()
    metrics = evaluator.evaluate_classification(y_test, y_pred, y_pred_proba)
    
    print("Classification Results:")
    print("-" * 30)
    for metric, value in metrics.items():
        if metric not in ['confusion_matrix', 'fpr', 'tpr']:
            print(f"{metric.capitalize()}: {value:.4f}")
    
    # Plot results
    evaluator.plot_classification_results(y_test, y_pred, y_pred_proba)

def regression_example():
    """Complete regression evaluation example"""
    # Generate sample data
    X, y = make_regression(n_samples=1000, n_features=10, noise=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate
    evaluator = ModelEvaluator()
    metrics = evaluator.evaluate_regression(y_test, y_pred)
    
    print("Regression Results:")
    print("-" * 25)
    for metric, value in metrics.items():
        if metric != 'residuals':
            print(f"{metric.upper()}: {value:.4f}")
    
    # Plot results
    evaluator.plot_regression_results(y_test, y_pred)

if __name__ == "__main__":
    print("=== Cross-Validation Example ===")
    cross_validation_example()
    
    print("\n=== Classification Example ===")
    classification_example()
    
    print("\n=== Regression Example ===")
    regression_example()
```

## 🎯 Key Insights

### Choosing the Right Metric

**Classification:**
- **Balanced data**: Accuracy
- **Imbalanced data**: F1-score, Precision/Recall
- **Cost-sensitive**: Custom metrics based on business impact
- **Ranking problems**: AUC-ROC

**Regression:**
- **General purpose**: RMSE
- **Outlier robust**: MAE
- **Relative performance**: R²
- **Percentage errors**: MAPE

### Common Pitfalls
- **Data leakage**: Information from future/test set in training
- **Overfitting to validation set**: Too much hyperparameter tuning
- **Wrong metric choice**: Not aligned with business objectives
- **Insufficient test data**: Unreliable performance estimates

## 🎯 Practice Exercises

1. Implement custom evaluation metrics for specific business cases
2. Compare different cross-validation strategies on various datasets
3. Build a model selection pipeline using multiple metrics
4. Handle evaluation for imbalanced datasets
5. Create automated model evaluation reports

## 📚 Next Steps
- **Feature Engineering**: Improving model inputs
- **Hyperparameter Tuning**: Optimizing model performance
- **Model Selection**: Choosing the best algorithm
- **Ensemble Methods**: Combining multiple models

*Proper evaluation is the foundation of reliable ML - measure what matters!*