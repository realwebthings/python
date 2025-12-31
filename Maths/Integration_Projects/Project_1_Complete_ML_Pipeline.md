# 🚀 Integration Project 1: Complete ML Pipeline with Mathematical Foundations

## 📋 Project Overview

This project demonstrates how **all mathematical concepts** work together in a complete machine learning pipeline. We'll build a comprehensive system that showcases:

- **Linear Algebra**: Data representation and transformations
- **Statistics**: Data analysis and hypothesis testing
- **Probability**: Uncertainty quantification and Bayesian methods
- **Calculus**: Optimization and gradient descent
- **Information Theory**: Feature selection and model evaluation
- **Graph Theory**: Network analysis and graph-based features

---

## 🎯 Project Goals

1. **Integrate Multiple Math Topics**: Show how different areas of mathematics work together
2. **Build Complete ML Pipeline**: From data preprocessing to model deployment
3. **Mathematical Rigor**: Implement algorithms from mathematical first principles
4. **Real-world Application**: Solve a practical problem using mathematical foundations

---

## 📊 Dataset: Social Network Analysis with Fraud Detection

We'll analyze a social network to detect fraudulent users, combining graph theory with traditional ML.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from scipy import stats
from scipy.optimize import minimize
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

class MathematicalMLPipeline:
    """Complete ML pipeline with mathematical foundations"""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.model_params = None
        self.feature_importance = None
        self.graph = None
        
    def generate_synthetic_data(self, n_users=1000, fraud_rate=0.1):
        """Generate synthetic social network with fraud labels"""
        print("🔢 STEP 1: DATA GENERATION (Probability Theory)")
        print("=" * 60)
        
        # Generate user features using different probability distributions
        data = {}
        
        # Age: Normal distribution
        data['age'] = np.random.normal(35, 12, n_users)
        data['age'] = np.clip(data['age'], 18, 80)
        
        # Account balance: Log-normal distribution
        data['balance'] = np.random.lognormal(8, 1.5, n_users)
        
        # Transaction frequency: Poisson distribution
        data['transaction_freq'] = np.random.poisson(5, n_users)
        
        # Account age in days: Exponential distribution
        data['account_age'] = np.random.exponential(365, n_users)
        
        # Number of connections: Power law distribution (preferential attachment)
        data['connections'] = np.random.pareto(1.16, n_users) + 1
        data['connections'] = np.clip(data['connections'], 1, 100).astype(int)
        
        # Generate fraud labels (imbalanced)
        n_fraud = int(n_users * fraud_rate)
        fraud_labels = np.zeros(n_users)
        fraud_indices = np.random.choice(n_users, n_fraud, replace=False)
        fraud_labels[fraud_indices] = 1
        
        # Fraudulent users have different characteristics
        for idx in fraud_indices:
            data['age'][idx] *= np.random.uniform(0.8, 1.2)  # Slightly different age
            data['balance'][idx] *= np.random.uniform(0.3, 0.7)  # Lower balance
            data['transaction_freq'][idx] *= np.random.uniform(2, 5)  # Higher frequency
            data['account_age'][idx] *= np.random.uniform(0.1, 0.5)  # Newer accounts
            data['connections'][idx] = max(1, int(data['connections'][idx] * 0.3))  # Fewer connections
        
        # Create DataFrame
        df = pd.DataFrame(data)
        df['is_fraud'] = fraud_labels
        
        print(f"Generated {n_users} users with {n_fraud} fraudulent accounts ({fraud_rate:.1%})")
        print(f"Features: {list(df.columns[:-1])}")
        
        return df
    
    def exploratory_data_analysis(self, df):
        """Comprehensive EDA using statistical methods"""
        print("\n📊 STEP 2: EXPLORATORY DATA ANALYSIS (Statistics)")
        print("=" * 60)
        
        # Descriptive statistics
        print("Descriptive Statistics:")
        print(df.describe())
        
        # Statistical tests for feature significance
        print("\nStatistical Significance Tests:")
        features = ['age', 'balance', 'transaction_freq', 'account_age', 'connections']
        
        for feature in features:
            fraud_group = df[df['is_fraud'] == 1][feature]
            normal_group = df[df['is_fraud'] == 0][feature]
            
            # Two-sample t-test
            t_stat, p_value = stats.ttest_ind(fraud_group, normal_group)
            
            # Effect size (Cohen's d)
            pooled_std = np.sqrt(((len(fraud_group) - 1) * fraud_group.var() + 
                                 (len(normal_group) - 1) * normal_group.var()) / 
                                (len(fraud_group) + len(normal_group) - 2))
            cohens_d = (fraud_group.mean() - normal_group.mean()) / pooled_std
            
            print(f"{feature}: t={t_stat:.3f}, p={p_value:.4f}, Cohen's d={cohens_d:.3f}")
        
        # Correlation analysis
        print(f"\nCorrelation Matrix:")
        corr_matrix = df[features].corr()
        print(corr_matrix.round(3))
        
        # Visualizations
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        axes = axes.flatten()
        
        for i, feature in enumerate(features):
            # Distribution comparison
            df[df['is_fraud'] == 0][feature].hist(alpha=0.7, bins=30, 
                                                 label='Normal', ax=axes[i])
            df[df['is_fraud'] == 1][feature].hist(alpha=0.7, bins=30, 
                                                 label='Fraud', ax=axes[i])
            axes[i].set_title(f'{feature} Distribution')
            axes[i].legend()
            axes[i].grid(True, alpha=0.3)
        
        # Correlation heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Feature Correlation Matrix')
        plt.show()
        
        return corr_matrix
    
    def create_social_network(self, df):
        """Create social network graph using graph theory"""
        print("\n🕸️ STEP 3: SOCIAL NETWORK CREATION (Graph Theory)")
        print("=" * 60)
        
        n_users = len(df)
        G = nx.Graph()
        
        # Add nodes with attributes
        for i, row in df.iterrows():
            G.add_node(i, 
                      age=row['age'],
                      balance=row['balance'],
                      is_fraud=row['is_fraud'])
        
        # Create edges based on similarity and preferential attachment
        for i in range(n_users):
            n_connections = int(df.iloc[i]['connections'])
            
            # Calculate similarity scores with other users
            similarities = []
            for j in range(n_users):
                if i != j:
                    # Age similarity
                    age_sim = 1 / (1 + abs(df.iloc[i]['age'] - df.iloc[j]['age']) / 10)
                    # Balance similarity (log scale)
                    balance_sim = 1 / (1 + abs(np.log(df.iloc[i]['balance'] + 1) - 
                                              np.log(df.iloc[j]['balance'] + 1)))
                    # Combined similarity
                    total_sim = (age_sim + balance_sim) / 2
                    similarities.append((j, total_sim))
            
            # Sort by similarity and add edges to most similar users
            similarities.sort(key=lambda x: x[1], reverse=True)
            for j, sim in similarities[:n_connections]:
                if not G.has_edge(i, j):
                    G.add_edge(i, j, weight=sim)
        
        # Calculate graph metrics
        print(f"Network Statistics:")
        print(f"Nodes: {G.number_of_nodes()}")
        print(f"Edges: {G.number_of_edges()}")
        print(f"Density: {nx.density(G):.4f}")
        print(f"Average clustering: {nx.average_clustering(G):.4f}")
        
        if nx.is_connected(G):
            print(f"Average path length: {nx.average_shortest_path_length(G):.3f}")
        else:
            largest_cc = max(nx.connected_components(G), key=len)
            subgraph = G.subgraph(largest_cc)
            print(f"Average path length (largest component): {nx.average_shortest_path_length(subgraph):.3f}")
        
        self.graph = G
        return G
    
    def extract_graph_features(self, df, G):
        """Extract graph-based features using spectral methods"""
        print("\n🔍 STEP 4: GRAPH FEATURE EXTRACTION (Linear Algebra + Graph Theory)")
        print("=" * 60)
        
        # Calculate centrality measures
        degree_centrality = nx.degree_centrality(G)
        betweenness_centrality = nx.betweenness_centrality(G)
        closeness_centrality = nx.closeness_centrality(G)
        eigenvector_centrality = nx.eigenvector_centrality(G)
        
        # Calculate clustering coefficient
        clustering = nx.clustering(G)
        
        # PageRank (random walk centrality)
        pagerank = nx.pagerank(G)
        
        # Add graph features to dataframe
        df_enhanced = df.copy()
        df_enhanced['degree_centrality'] = [degree_centrality[i] for i in range(len(df))]
        df_enhanced['betweenness_centrality'] = [betweenness_centrality[i] for i in range(len(df))]
        df_enhanced['closeness_centrality'] = [closeness_centrality[i] for i in range(len(df))]
        df_enhanced['eigenvector_centrality'] = [eigenvector_centrality[i] for i in range(len(df))]
        df_enhanced['clustering'] = [clustering[i] for i in range(len(df))]
        df_enhanced['pagerank'] = [pagerank[i] for i in range(len(df))]
        
        # Spectral features using graph Laplacian
        A = nx.adjacency_matrix(G).toarray()
        D = np.diag(np.sum(A, axis=1))
        L = D - A  # Graph Laplacian
        
        # Compute eigenvalues and eigenvectors
        eigenvals, eigenvecs = np.linalg.eigh(L)
        
        # Use first few non-zero eigenvectors as features
        n_spectral_features = 5
        for i in range(1, min(n_spectral_features + 1, len(eigenvals))):
            df_enhanced[f'spectral_feature_{i}'] = eigenvecs[:, i]
        
        print(f"Added {6 + min(n_spectral_features, len(eigenvals)-1)} graph-based features")
        print(f"Graph Laplacian eigenvalues (first 10): {eigenvals[:10].round(4)}")
        
        return df_enhanced
    
    def feature_selection_information_theory(self, X, y):
        """Select features using mutual information"""
        print("\n📡 STEP 5: FEATURE SELECTION (Information Theory)")
        print("=" * 60)
        
        from sklearn.feature_selection import mutual_info_classif
        
        # Calculate mutual information
        mi_scores = mutual_info_classif(X, y, random_state=42)
        
        # Create feature importance ranking
        feature_names = X.columns
        feature_importance = pd.DataFrame({
            'feature': feature_names,
            'mutual_info': mi_scores
        }).sort_values('mutual_info', ascending=False)
        
        print("Feature Importance (Mutual Information):")
        print(feature_importance.head(10))
        
        # Select top features
        top_features = feature_importance.head(10)['feature'].tolist()
        X_selected = X[top_features]
        
        # Visualize feature importance
        plt.figure(figsize=(12, 8))
        plt.barh(range(len(feature_importance)), feature_importance['mutual_info'])
        plt.yticks(range(len(feature_importance)), feature_importance['feature'])
        plt.xlabel('Mutual Information Score')
        plt.title('Feature Importance using Mutual Information')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.show()
        
        self.feature_importance = feature_importance
        return X_selected, top_features
    
    def implement_logistic_regression(self, X, y):
        """Implement logistic regression from scratch using calculus"""
        print("\n🧮 STEP 6: MODEL IMPLEMENTATION (Calculus + Optimization)")
        print("=" * 60)
        
        # Add intercept term
        X_with_intercept = np.column_stack([np.ones(X.shape[0]), X])
        
        def sigmoid(z):
            """Sigmoid activation function"""
            # Clip z to prevent overflow
            z = np.clip(z, -500, 500)
            return 1 / (1 + np.exp(-z))
        
        def cost_function(theta, X, y):
            """Logistic regression cost function"""
            m = len(y)
            z = X @ theta
            h = sigmoid(z)
            
            # Add small epsilon to prevent log(0)
            epsilon = 1e-15
            h = np.clip(h, epsilon, 1 - epsilon)
            
            cost = -(1/m) * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))
            return cost
        
        def gradient(theta, X, y):
            """Gradient of cost function"""
            m = len(y)
            z = X @ theta
            h = sigmoid(z)
            grad = (1/m) * X.T @ (h - y)
            return grad
        
        def hessian(theta, X, y):
            """Hessian matrix for Newton's method"""
            m = len(y)
            z = X @ theta
            h = sigmoid(z)
            S = np.diag(h * (1 - h))
            H = (1/m) * X.T @ S @ X
            return H
        
        # Initialize parameters
        theta_init = np.random.normal(0, 0.01, X_with_intercept.shape[1])
        
        # Gradient descent implementation
        def gradient_descent(X, y, theta_init, learning_rate=0.01, max_iter=1000):
            theta = theta_init.copy()
            costs = []
            
            for i in range(max_iter):
                cost = cost_function(theta, X, y)
                grad = gradient(theta, X, y)
                
                theta = theta - learning_rate * grad
                costs.append(cost)
                
                if i % 100 == 0:
                    print(f"Iteration {i}: Cost = {cost:.6f}")
            
            return theta, costs
        
        # Newton's method implementation
        def newtons_method(X, y, theta_init, max_iter=100):
            theta = theta_init.copy()
            costs = []
            
            for i in range(max_iter):
                cost = cost_function(theta, X, y)
                grad = gradient(theta, X, y)
                H = hessian(theta, X, y)
                
                # Add regularization to Hessian for numerical stability
                H_reg = H + 1e-6 * np.eye(H.shape[0])
                
                try:
                    theta = theta - np.linalg.solve(H_reg, grad)
                except np.linalg.LinAlgError:
                    print("Hessian is singular, switching to gradient descent")
                    break
                
                costs.append(cost)
                
                if i % 10 == 0:
                    print(f"Newton iteration {i}: Cost = {cost:.6f}")
                
                # Check convergence
                if len(costs) > 1 and abs(costs[-1] - costs[-2]) < 1e-8:
                    print(f"Converged after {i+1} iterations")
                    break
            
            return theta, costs
        
        # Train using both methods
        print("Training with Gradient Descent:")
        theta_gd, costs_gd = gradient_descent(X_with_intercept, y, theta_init)
        
        print("\nTraining with Newton's Method:")
        theta_newton, costs_newton = newtons_method(X_with_intercept, y, theta_init)
        
        # Compare convergence
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        plt.plot(costs_gd)
        plt.title('Gradient Descent Convergence')
        plt.xlabel('Iteration')
        plt.ylabel('Cost')
        plt.grid(True, alpha=0.3)
        
        plt.subplot(1, 2, 2)
        plt.plot(costs_newton)
        plt.title("Newton's Method Convergence")
        plt.xlabel('Iteration')
        plt.ylabel('Cost')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
        # Use Newton's method result (typically converges faster)
        self.model_params = theta_newton
        
        def predict_proba(X_new):
            X_new_with_intercept = np.column_stack([np.ones(X_new.shape[0]), X_new])
            return sigmoid(X_new_with_intercept @ theta_newton)
        
        def predict(X_new, threshold=0.5):
            return (predict_proba(X_new) >= threshold).astype(int)
        
        return predict, predict_proba
    
    def bayesian_model_evaluation(self, y_true, y_pred, y_pred_proba):
        """Evaluate model using Bayesian statistics"""
        print("\n🎲 STEP 7: BAYESIAN MODEL EVALUATION (Probability Theory)")
        print("=" * 60)
        
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
        from sklearn.metrics import roc_auc_score, roc_curve
        
        # Basic metrics
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        auc = roc_auc_score(y_true, y_pred_proba)
        
        print(f"Model Performance:")
        print(f"Accuracy: {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        print(f"F1-Score: {f1:.4f}")
        print(f"AUC-ROC: {auc:.4f}")
        
        # Bayesian confidence intervals for accuracy
        n = len(y_true)
        successes = np.sum(y_true == y_pred)
        
        # Beta posterior (conjugate prior for binomial likelihood)
        alpha_prior, beta_prior = 1, 1  # Uniform prior
        alpha_posterior = alpha_prior + successes
        beta_posterior = beta_prior + (n - successes)
        
        # Credible interval
        credible_interval = stats.beta.interval(0.95, alpha_posterior, beta_posterior)
        posterior_mean = alpha_posterior / (alpha_posterior + beta_posterior)
        
        print(f"\nBayesian Analysis:")
        print(f"Posterior mean accuracy: {posterior_mean:.4f}")
        print(f"95% Credible interval: [{credible_interval[0]:.4f}, {credible_interval[1]:.4f}]")
        
        # Model comparison using Bayes factors (simplified)
        # Compare with random classifier
        random_accuracy = 0.5
        
        # Log Bayes factor (approximate)
        log_bf = (successes * np.log(posterior_mean / random_accuracy) + 
                 (n - successes) * np.log((1 - posterior_mean) / (1 - random_accuracy)))
        
        print(f"Log Bayes Factor vs Random: {log_bf:.3f}")
        if log_bf > 3:
            print("Strong evidence for our model")
        elif log_bf > 1:
            print("Moderate evidence for our model")
        else:
            print("Weak evidence for our model")
        
        # Visualizations
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Confusion Matrix
        cm = confusion_matrix(y_true, y_pred)
        sns.heatmap(cm, annot=True, fmt='d', ax=axes[0, 0], cmap='Blues')
        axes[0, 0].set_title('Confusion Matrix')
        axes[0, 0].set_xlabel('Predicted')
        axes[0, 0].set_ylabel('Actual')
        
        # ROC Curve
        fpr, tpr, _ = roc_curve(y_true, y_pred_proba)
        axes[0, 1].plot(fpr, tpr, linewidth=2, label=f'ROC (AUC = {auc:.3f})')
        axes[0, 1].plot([0, 1], [0, 1], 'k--', alpha=0.5)
        axes[0, 1].set_xlabel('False Positive Rate')
        axes[0, 1].set_ylabel('True Positive Rate')
        axes[0, 1].set_title('ROC Curve')
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        
        # Posterior distribution of accuracy
        x = np.linspace(0, 1, 1000)
        posterior_pdf = stats.beta.pdf(x, alpha_posterior, beta_posterior)
        axes[1, 0].plot(x, posterior_pdf, 'b-', linewidth=2)
        axes[1, 0].axvline(posterior_mean, color='r', linestyle='--', label='Posterior Mean')
        axes[1, 0].axvline(credible_interval[0], color='g', linestyle=':', label='95% CI')
        axes[1, 0].axvline(credible_interval[1], color='g', linestyle=':')
        axes[1, 0].set_xlabel('Accuracy')
        axes[1, 0].set_ylabel('Posterior Density')
        axes[1, 0].set_title('Posterior Distribution of Accuracy')
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        
        # Prediction probability distribution
        axes[1, 1].hist(y_pred_proba[y_true == 0], bins=30, alpha=0.7, 
                       label='Normal Users', density=True)
        axes[1, 1].hist(y_pred_proba[y_true == 1], bins=30, alpha=0.7, 
                       label='Fraudulent Users', density=True)
        axes[1, 1].set_xlabel('Predicted Probability')
        axes[1, 1].set_ylabel('Density')
        axes[1, 1].set_title('Prediction Probability Distribution')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
        return {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'auc': auc,
            'posterior_mean': posterior_mean,
            'credible_interval': credible_interval,
            'log_bayes_factor': log_bf
        }
    
    def network_analysis_results(self, df, G):
        """Analyze network properties of fraudulent vs normal users"""
        print("\n🕸️ STEP 8: NETWORK ANALYSIS RESULTS (Graph Theory)")
        print("=" * 60)
        
        # Separate fraud and normal users
        fraud_nodes = df[df['is_fraud'] == 1].index.tolist()
        normal_nodes = df[df['is_fraud'] == 0].index.tolist()
        
        # Calculate network metrics for each group
        def calculate_group_metrics(nodes, G):
            if not nodes:
                return {}
            
            subgraph = G.subgraph(nodes)
            
            # Basic metrics
            metrics = {
                'nodes': len(nodes),
                'edges': subgraph.number_of_edges(),
                'density': nx.density(subgraph) if len(nodes) > 1 else 0,
                'avg_clustering': nx.average_clustering(subgraph)
            }
            
            # Centrality measures
            degree_cent = nx.degree_centrality(G)
            between_cent = nx.betweenness_centrality(G)
            
            metrics['avg_degree_centrality'] = np.mean([degree_cent[n] for n in nodes])
            metrics['avg_betweenness_centrality'] = np.mean([between_cent[n] for n in nodes])
            
            return metrics
        
        fraud_metrics = calculate_group_metrics(fraud_nodes, G)
        normal_metrics = calculate_group_metrics(normal_nodes, G)
        
        print("Network Analysis by User Type:")
        print("\nFraudulent Users:")
        for key, value in fraud_metrics.items():
            print(f"  {key}: {value:.4f}")
        
        print("\nNormal Users:")
        for key, value in normal_metrics.items():
            print(f"  {key}: {value:.4f}")
        
        # Statistical comparison
        print("\nStatistical Comparison:")
        
        # Degree centrality comparison
        fraud_degree_cent = [nx.degree_centrality(G)[n] for n in fraud_nodes]
        normal_degree_cent = [nx.degree_centrality(G)[n] for n in normal_nodes]
        
        t_stat, p_value = stats.ttest_ind(fraud_degree_cent, normal_degree_cent)
        print(f"Degree Centrality: t={t_stat:.3f}, p={p_value:.4f}")
        
        # Visualize network with fraud highlighting
        plt.figure(figsize=(15, 10))
        
        pos = nx.spring_layout(G, k=0.5, iterations=50)
        
        # Draw normal users
        nx.draw_networkx_nodes(G, pos, nodelist=normal_nodes, 
                              node_color='lightblue', node_size=30, alpha=0.7)
        
        # Draw fraudulent users
        nx.draw_networkx_nodes(G, pos, nodelist=fraud_nodes, 
                              node_color='red', node_size=100, alpha=0.9)
        
        # Draw edges
        nx.draw_networkx_edges(G, pos, alpha=0.1, width=0.5)
        
        plt.title('Social Network: Red = Fraudulent Users, Blue = Normal Users')
        plt.axis('off')
        plt.show()
        
        return fraud_metrics, normal_metrics
    
    def run_complete_pipeline(self):
        """Run the complete mathematical ML pipeline"""
        print("🚀 MATHEMATICAL ML PIPELINE: FRAUD DETECTION IN SOCIAL NETWORKS")
        print("=" * 80)
        
        # Step 1: Generate data
        df = self.generate_synthetic_data(n_users=1000, fraud_rate=0.1)
        
        # Step 2: EDA
        corr_matrix = self.exploratory_data_analysis(df)
        
        # Step 3: Create social network
        G = self.create_social_network(df)
        
        # Step 4: Extract graph features
        df_enhanced = self.extract_graph_features(df, G)
        
        # Step 5: Feature selection
        X = df_enhanced.drop(['is_fraud'], axis=1)
        y = df_enhanced['is_fraud']
        
        X_selected, top_features = self.feature_selection_information_theory(X, y)
        
        # Step 6: Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X_selected, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Step 7: Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Step 8: Train model
        predict_func, predict_proba_func = self.implement_logistic_regression(
            X_train_scaled, y_train
        )
        
        # Step 9: Make predictions
        y_pred = predict_func(X_test_scaled)
        y_pred_proba = predict_proba_func(X_test_scaled)
        
        # Step 10: Evaluate model
        results = self.bayesian_model_evaluation(y_test, y_pred, y_pred_proba)
        
        # Step 11: Network analysis
        fraud_metrics, normal_metrics = self.network_analysis_results(df_enhanced, G)
        
        print("\n🎉 PIPELINE COMPLETED SUCCESSFULLY!")
        print("=" * 80)
        print("Mathematical concepts demonstrated:")
        print("✓ Probability Theory: Data generation and Bayesian evaluation")
        print("✓ Statistics: EDA, hypothesis testing, and significance tests")
        print("✓ Linear Algebra: Matrix operations and spectral features")
        print("✓ Graph Theory: Network creation and centrality measures")
        print("✓ Information Theory: Feature selection using mutual information")
        print("✓ Calculus: Gradient descent and Newton's method optimization")
        print("✓ Optimization Theory: Cost function minimization")
        
        return {
            'data': df_enhanced,
            'graph': G,
            'model_results': results,
            'network_metrics': (fraud_metrics, normal_metrics),
            'selected_features': top_features
        }

# Run the complete pipeline
if __name__ == "__main__":
    pipeline = MathematicalMLPipeline()
    results = pipeline.run_complete_pipeline()
```

---

## 🔍 Mathematical Concepts Demonstrated

### 1. **Probability Theory**
- **Data Generation**: Used different probability distributions (Normal, Log-normal, Poisson, Exponential, Pareto)
- **Bayesian Evaluation**: Beta-binomial conjugate analysis for model confidence
- **Uncertainty Quantification**: Credible intervals and Bayes factors

### 2. **Statistics**
- **Descriptive Statistics**: Mean, variance, correlation analysis
- **Hypothesis Testing**: Two-sample t-tests for feature significance
- **Effect Size**: Cohen's d for practical significance
- **Statistical Inference**: Confidence intervals and p-values

### 3. **Linear Algebra**
- **Matrix Operations**: Adjacency matrices, graph Laplacian
- **Eigendecomposition**: Spectral features from graph structure
- **Vector Operations**: Feature vectors and transformations
- **Matrix Factorization**: Implicit in network analysis

### 4. **Graph Theory**
- **Network Creation**: Similarity-based edge formation
- **Centrality Measures**: Degree, betweenness, closeness, eigenvector
- **Spectral Analysis**: Graph Laplacian eigenvalues and eigenvectors
- **Community Structure**: Clustering and network properties

### 5. **Information Theory**
- **Mutual Information**: Feature selection based on information content
- **Entropy**: Implicit in classification and uncertainty measures
- **Information Gain**: Feature importance ranking

### 6. **Calculus & Optimization**
- **Gradient Descent**: First-order optimization method
- **Newton's Method**: Second-order optimization using Hessian
- **Cost Functions**: Logistic regression loss function
- **Convergence Analysis**: Monitoring optimization progress

---

## 🎯 Key Learning Outcomes

1. **Integration**: See how different mathematical areas work together
2. **Implementation**: Build algorithms from mathematical first principles
3. **Real-world Application**: Solve practical problems using mathematical foundations
4. **Comparative Analysis**: Understand trade-offs between different approaches
5. **Evaluation**: Use rigorous mathematical methods for model assessment

---

## 📈 Extensions and Improvements

1. **Advanced Optimization**: Implement Adam, RMSprop, or other optimizers
2. **Regularization**: Add L1/L2 penalties with mathematical justification
3. **Cross-validation**: Implement k-fold CV with statistical significance testing
4. **Feature Engineering**: Create polynomial features with combinatorial analysis
5. **Ensemble Methods**: Combine multiple models using probability theory
6. **Deep Learning**: Extend to neural networks with backpropagation mathematics

---

## 🔗 Mathematical Connections

This project demonstrates the **interconnected nature** of mathematics in ML:

- **Probability → Statistics**: Random variables lead to statistical inference
- **Linear Algebra → Graph Theory**: Matrix representations of networks
- **Calculus → Optimization**: Derivatives enable gradient-based learning
- **Information Theory → Feature Selection**: Entropy guides feature importance
- **Graph Theory → Network Analysis**: Structural properties reveal patterns
- **Statistics → Model Evaluation**: Rigorous assessment of performance

---

*This integration project shows how mathematical foundations work together to solve real-world problems. Each concept builds upon others, creating a powerful framework for machine learning and AI!*