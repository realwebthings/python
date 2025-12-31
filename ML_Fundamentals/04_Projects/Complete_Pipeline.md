# 🚀 Complete ML Pipeline - End-to-End Project

## 📋 Project Overview
Build a complete machine learning pipeline from raw data to production-ready model, incorporating all concepts from Weeks 3-6.

## 🎯 Project Goals
- **Data preprocessing** and cleaning
- **Feature engineering** and selection
- **Multiple algorithm comparison**
- **Proper model evaluation**
- **Hyperparameter tuning**
- **Model interpretation**
- **Production considerations**

## 📊 Dataset: Customer Churn Prediction
Predict whether customers will churn (leave) based on their behavior and demographics.

## 🐍 Complete Implementation

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import (train_test_split, cross_val_score, 
                                   GridSearchCV, StratifiedKFold)
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.feature_selection import SelectKBest, f_classif, RFE
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (classification_report, confusion_matrix, 
                           roc_auc_score, roc_curve, precision_recall_curve)
import warnings
warnings.filterwarnings('ignore')

class MLPipeline:
    def __init__(self):
        self.data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.scaler = None
        self.models = {}
        self.best_model = None
        self.feature_names = None
        
    def load_data(self, create_synthetic=True):
        """Load or create dataset"""
        if create_synthetic:
            # Create synthetic customer churn dataset
            np.random.seed(42)
            n_samples = 5000
            
            # Generate features
            age = np.random.normal(40, 15, n_samples)
            tenure = np.random.exponential(2, n_samples)
            monthly_charges = np.random.normal(65, 20, n_samples)
            total_charges = monthly_charges * tenure + np.random.normal(0, 100, n_samples)
            
            # Categorical features
            contract_type = np.random.choice(['Month-to-month', 'One year', 'Two year'], 
                                           n_samples, p=[0.5, 0.3, 0.2])
            payment_method = np.random.choice(['Electronic check', 'Mailed check', 
                                             'Bank transfer', 'Credit card'], n_samples)
            internet_service = np.random.choice(['DSL', 'Fiber optic', 'No'], 
                                              n_samples, p=[0.4, 0.4, 0.2])
            
            # Create target with realistic relationships
            churn_prob = (
                0.1 +  # Base probability
                0.3 * (contract_type == 'Month-to-month') +  # Contract effect
                0.2 * (monthly_charges > 80) +  # High charges effect
                0.15 * (tenure < 1) +  # New customer effect
                0.1 * (age < 30) +  # Young customer effect
                0.1 * np.random.random(n_samples)  # Random noise
            )
            churn = (churn_prob > 0.5).astype(int)
            
            # Create DataFrame
            self.data = pd.DataFrame({
                'age': age,
                'tenure': tenure,
                'monthly_charges': monthly_charges,
                'total_charges': total_charges,
                'contract_type': contract_type,
                'payment_method': payment_method,
                'internet_service': internet_service,
                'churn': churn
            })
            
            print(f"Dataset created: {self.data.shape}")
            print(f"Churn rate: {self.data['churn'].mean():.2%}")
            
        return self.data
    
    def explore_data(self):
        """Exploratory Data Analysis"""
        print("=== DATA EXPLORATION ===")
        print(f"Dataset shape: {self.data.shape}")
        print(f"\nMissing values:\n{self.data.isnull().sum()}")
        print(f"\nData types:\n{self.data.dtypes}")
        print(f"\nTarget distribution:\n{self.data['churn'].value_counts(normalize=True)}")
        
        # Visualizations
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        
        # Numerical features distribution
        numerical_cols = ['age', 'tenure', 'monthly_charges', 'total_charges']
        for i, col in enumerate(numerical_cols):
            row, col_idx = i // 2, i % 2
            axes[row, col_idx].hist(self.data[col], bins=30, alpha=0.7)
            axes[row, col_idx].set_title(f'{col} Distribution')
            axes[row, col_idx].set_xlabel(col)
            axes[row, col_idx].set_ylabel('Frequency')
        
        # Churn by contract type
        churn_by_contract = self.data.groupby('contract_type')['churn'].mean()
        axes[1, 2].bar(churn_by_contract.index, churn_by_contract.values)
        axes[1, 2].set_title('Churn Rate by Contract Type')
        axes[1, 2].set_ylabel('Churn Rate')
        axes[1, 2].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.show()
        
        # Correlation matrix
        plt.figure(figsize=(10, 8))
        correlation_matrix = self.data.select_dtypes(include=[np.number]).corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Feature Correlation Matrix')
        plt.tight_layout()
        plt.show()
    
    def preprocess_data(self):
        """Data preprocessing and feature engineering"""
        print("\n=== DATA PREPROCESSING ===")
        
        # Handle missing values (if any)
        self.data = self.data.dropna()
        
        # Feature engineering
        # Create new features
        self.data['charges_per_tenure'] = self.data['total_charges'] / (self.data['tenure'] + 1)
        self.data['is_senior'] = (self.data['age'] >= 65).astype(int)
        self.data['high_charges'] = (self.data['monthly_charges'] > self.data['monthly_charges'].median()).astype(int)
        self.data['new_customer'] = (self.data['tenure'] < 1).astype(int)
        
        # Encode categorical variables
        categorical_cols = ['contract_type', 'payment_method', 'internet_service']
        
        # One-hot encoding
        encoded_features = pd.get_dummies(self.data[categorical_cols], prefix=categorical_cols)
        
        # Combine all features
        numerical_cols = ['age', 'tenure', 'monthly_charges', 'total_charges', 
                         'charges_per_tenure', 'is_senior', 'high_charges', 'new_customer']
        
        X = pd.concat([self.data[numerical_cols], encoded_features], axis=1)
        y = self.data['churn']
        
        self.feature_names = X.columns.tolist()
        
        # Split data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Scale features
        self.scaler = StandardScaler()
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.scaler.transform(self.X_test)
        
        print(f"Training set: {self.X_train.shape}")
        print(f"Test set: {self.X_test.shape}")
        print(f"Features created: {len(self.feature_names)}")
    
    def feature_selection(self):
        """Feature selection using multiple methods"""
        print("\n=== FEATURE SELECTION ===")
        
        # Method 1: Univariate selection
        selector_univariate = SelectKBest(score_func=f_classif, k=15)
        X_train_univariate = selector_univariate.fit_transform(self.X_train_scaled, self.y_train)
        selected_features_univariate = selector_univariate.get_support(indices=True)
        
        # Method 2: RFE with Logistic Regression
        estimator = LogisticRegression(random_state=42)
        selector_rfe = RFE(estimator, n_features_to_select=15)
        X_train_rfe = selector_rfe.fit_transform(self.X_train_scaled, self.y_train)
        selected_features_rfe = selector_rfe.get_support(indices=True)
        
        # Method 3: Feature importance from Random Forest
        rf = RandomForestClassifier(n_estimators=100, random_state=42)
        rf.fit(self.X_train_scaled, self.y_train)
        feature_importance = pd.DataFrame({
            'feature': self.feature_names,
            'importance': rf.feature_importances_
        }).sort_values('importance', ascending=False)
        
        top_15_features = feature_importance.head(15)['feature'].tolist()
        selected_features_rf = [self.feature_names.index(f) for f in top_15_features]
        
        print("Top 15 features by Random Forest importance:")
        print(feature_importance.head(15))
        
        # Use Random Forest selection for final model
        self.selected_features = selected_features_rf
        self.X_train_selected = self.X_train_scaled[:, self.selected_features]
        self.X_test_selected = self.X_test_scaled[:, self.selected_features]
        
        # Plot feature importance
        plt.figure(figsize=(10, 8))
        plt.barh(range(15), top_15_features[::-1])
        plt.yticks(range(15), [self.feature_names[i] for i in selected_features_rf[::-1]])
        plt.xlabel('Feature Importance')
        plt.title('Top 15 Feature Importances')
        plt.tight_layout()
        plt.show()
    
    def train_models(self):
        """Train multiple models and compare performance"""
        print("\n=== MODEL TRAINING ===")
        
        # Define models
        models = {
            'Logistic Regression': LogisticRegression(random_state=42),
            'Decision Tree': DecisionTreeClassifier(random_state=42),
            'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
            'SVM': SVC(probability=True, random_state=42),
            'KNN': KNeighborsClassifier()
        }
        
        # Cross-validation
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        results = {}
        
        for name, model in models.items():
            # Cross-validation scores
            cv_scores = cross_val_score(model, self.X_train_selected, self.y_train, 
                                      cv=cv, scoring='roc_auc')
            
            # Train on full training set
            model.fit(self.X_train_selected, self.y_train)
            
            # Test set predictions
            y_pred = model.predict(self.X_test_selected)
            y_pred_proba = model.predict_proba(self.X_test_selected)[:, 1]
            
            # Calculate metrics
            test_auc = roc_auc_score(self.y_test, y_pred_proba)
            
            results[name] = {
                'model': model,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std(),
                'test_auc': test_auc,
                'y_pred': y_pred,
                'y_pred_proba': y_pred_proba
            }
            
            print(f"{name}:")
            print(f"  CV AUC: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
            print(f"  Test AUC: {test_auc:.4f}")
            print()
        
        self.models = results
        
        # Find best model
        best_model_name = max(results.keys(), key=lambda x: results[x]['test_auc'])
        self.best_model = results[best_model_name]
        print(f"Best model: {best_model_name} (Test AUC: {self.best_model['test_auc']:.4f})")
        
        return results
    
    def hyperparameter_tuning(self):
        """Hyperparameter tuning for best model"""
        print("\n=== HYPERPARAMETER TUNING ===")
        
        # Tune Random Forest (assuming it's often the best)
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [5, 10, 15, None],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }
        
        rf = RandomForestClassifier(random_state=42)
        grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='roc_auc', 
                                 n_jobs=-1, verbose=1)
        
        grid_search.fit(self.X_train_selected, self.y_train)
        
        print(f"Best parameters: {grid_search.best_params_}")
        print(f"Best CV score: {grid_search.best_score_:.4f}")
        
        # Update best model
        self.best_model['model'] = grid_search.best_estimator_
        
        # Re-evaluate on test set
        y_pred = grid_search.best_estimator_.predict(self.X_test_selected)
        y_pred_proba = grid_search.best_estimator_.predict_proba(self.X_test_selected)[:, 1]
        test_auc = roc_auc_score(self.y_test, y_pred_proba)
        
        self.best_model['y_pred'] = y_pred
        self.best_model['y_pred_proba'] = y_pred_proba
        self.best_model['test_auc'] = test_auc
        
        print(f"Tuned model Test AUC: {test_auc:.4f}")
    
    def evaluate_model(self):
        """Comprehensive model evaluation"""
        print("\n=== MODEL EVALUATION ===")
        
        y_pred = self.best_model['y_pred']
        y_pred_proba = self.best_model['y_pred_proba']
        
        # Classification report
        print("Classification Report:")
        print(classification_report(self.y_test, y_pred))
        
        # Confusion matrix
        cm = confusion_matrix(self.y_test, y_pred)
        
        # Visualizations
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Confusion Matrix
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0,0])
        axes[0,0].set_title('Confusion Matrix')
        axes[0,0].set_xlabel('Predicted')
        axes[0,0].set_ylabel('Actual')
        
        # ROC Curve
        fpr, tpr, _ = roc_curve(self.y_test, y_pred_proba)
        axes[0,1].plot(fpr, tpr, color='darkorange', lw=2, 
                      label=f'ROC curve (AUC = {self.best_model["test_auc"]:.3f})')
        axes[0,1].plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        axes[0,1].set_xlim([0.0, 1.0])
        axes[0,1].set_ylim([0.0, 1.05])
        axes[0,1].set_xlabel('False Positive Rate')
        axes[0,1].set_ylabel('True Positive Rate')
        axes[0,1].set_title('ROC Curve')
        axes[0,1].legend(loc="lower right")
        
        # Precision-Recall Curve
        precision, recall, _ = precision_recall_curve(self.y_test, y_pred_proba)
        axes[1,0].plot(recall, precision, color='blue', lw=2)
        axes[1,0].set_xlabel('Recall')
        axes[1,0].set_ylabel('Precision')
        axes[1,0].set_title('Precision-Recall Curve')
        
        # Feature Importance (if available)
        if hasattr(self.best_model['model'], 'feature_importances_'):
            selected_feature_names = [self.feature_names[i] for i in self.selected_features]
            importance_df = pd.DataFrame({
                'feature': selected_feature_names,
                'importance': self.best_model['model'].feature_importances_
            }).sort_values('importance', ascending=True)
            
            axes[1,1].barh(range(len(importance_df)), importance_df['importance'])
            axes[1,1].set_yticks(range(len(importance_df)))
            axes[1,1].set_yticklabels(importance_df['feature'])
            axes[1,1].set_xlabel('Feature Importance')
            axes[1,1].set_title('Feature Importance (Tuned Model)')
        
        plt.tight_layout()
        plt.show()
    
    def model_interpretation(self):
        """Interpret model predictions"""
        print("\n=== MODEL INTERPRETATION ===")
        
        # Feature importance analysis
        if hasattr(self.best_model['model'], 'feature_importances_'):
            selected_feature_names = [self.feature_names[i] for i in self.selected_features]
            importance_df = pd.DataFrame({
                'feature': selected_feature_names,
                'importance': self.best_model['model'].feature_importances_
            }).sort_values('importance', ascending=False)
            
            print("Top 10 Most Important Features:")
            print(importance_df.head(10))
            
            # Business insights
            print("\nBusiness Insights:")
            top_features = importance_df.head(5)['feature'].tolist()
            for feature in top_features:
                if 'contract_type' in feature:
                    print(f"- {feature}: Contract type significantly affects churn")
                elif 'tenure' in feature:
                    print(f"- {feature}: Customer tenure is crucial for retention")
                elif 'charges' in feature:
                    print(f"- {feature}: Pricing strategy impacts churn")
                elif 'age' in feature:
                    print(f"- {feature}: Customer demographics matter")
    
    def run_complete_pipeline(self):
        """Run the complete ML pipeline"""
        print("🚀 STARTING COMPLETE ML PIPELINE")
        print("=" * 50)
        
        # Step 1: Load data
        self.load_data()
        
        # Step 2: Explore data
        self.explore_data()
        
        # Step 3: Preprocess data
        self.preprocess_data()
        
        # Step 4: Feature selection
        self.feature_selection()
        
        # Step 5: Train models
        self.train_models()
        
        # Step 6: Hyperparameter tuning
        self.hyperparameter_tuning()
        
        # Step 7: Evaluate model
        self.evaluate_model()
        
        # Step 8: Model interpretation
        self.model_interpretation()
        
        print("\n🎉 PIPELINE COMPLETED SUCCESSFULLY!")
        print("=" * 50)

# Run the complete pipeline
if __name__ == "__main__":
    pipeline = MLPipeline()
    pipeline.run_complete_pipeline()
```

## 🎯 Key Learning Outcomes

### Technical Skills Demonstrated
1. **Data Preprocessing**: Handling missing values, feature engineering
2. **Feature Selection**: Multiple methods comparison
3. **Model Comparison**: Systematic evaluation of algorithms
4. **Hyperparameter Tuning**: Grid search optimization
5. **Model Evaluation**: Comprehensive metrics and visualizations
6. **Model Interpretation**: Understanding feature importance

### Best Practices Applied
- **Proper data splitting** (train/validation/test)
- **Cross-validation** for robust evaluation
- **Feature scaling** before model training
- **Stratified sampling** for imbalanced data
- **Multiple metrics** for comprehensive evaluation
- **Visualization** for better understanding

### Business Value
- **Actionable insights** from feature importance
- **Model interpretability** for stakeholder buy-in
- **Performance metrics** aligned with business goals
- **Scalable pipeline** for production deployment

## 🔄 Extensions and Improvements

### Advanced Techniques
1. **Ensemble Methods**: Combine multiple models
2. **Advanced Feature Engineering**: Automated feature generation
3. **Imbalanced Data Handling**: SMOTE, class weights
4. **Model Explainability**: SHAP, LIME
5. **Pipeline Automation**: MLflow, Kubeflow

### Production Considerations
1. **Model Versioning**: Track model changes
2. **Data Drift Detection**: Monitor input distribution
3. **A/B Testing**: Compare model versions
4. **Real-time Inference**: API deployment
5. **Monitoring**: Performance tracking

## 🎯 Practice Exercises

1. **Extend the pipeline** with additional algorithms
2. **Handle imbalanced datasets** with advanced techniques
3. **Add model explainability** with SHAP values
4. **Create automated reporting** for stakeholders
5. **Deploy the model** as a web API

## 📚 Next Steps
- **Deep Learning**: Neural networks for complex patterns
- **Time Series**: Temporal data analysis
- **NLP**: Text data processing
- **Computer Vision**: Image data analysis
- **MLOps**: Production ML systems

*This complete pipeline demonstrates professional ML development - use it as a template for real projects!*