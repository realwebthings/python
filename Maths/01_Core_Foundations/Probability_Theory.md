# 🎲 Probability Theory for ML/AI

## 📋 Table of Contents
- [Overview](#overview)
- [Basic Probability Concepts](#basic-probability-concepts)
- [Random Variables](#random-variables)
- [Probability Distributions](#probability-distributions)
- [Bayes' Theorem](#bayes-theorem)
- [Joint and Conditional Probability](#joint-and-conditional-probability)
- [Expectation and Variance](#expectation-and-variance)
- [Common Distributions](#common-distributions)
- [Applications in ML/AI](#applications-in-mlai)
- [Practice Problems](#practice-problems)
- [Python Implementation](#python-implementation)

---

## Overview

Probability theory is the **mathematical foundation** of uncertainty and randomness in ML/AI:

### 🎯 **Critical Applications:**
- **Bayesian Machine Learning**: Prior and posterior distributions
- **Classification**: Probabilistic predictions
- **Generative Models**: VAEs, GANs model data distributions
- **Reinforcement Learning**: Stochastic policies and environments
- **Natural Language Processing**: Language models are probability distributions
- **Uncertainty Quantification**: Model confidence and calibration

---

## Basic Probability Concepts

### Sample Space and Events
- **Sample Space (Ω)**: Set of all possible outcomes
- **Event (A)**: Subset of sample space
- **Elementary Event**: Single outcome

### Probability Axioms
1. **Non-negativity**: P(A) ≥ 0 for all events A
2. **Normalization**: P(Ω) = 1
3. **Additivity**: P(A ∪ B) = P(A) + P(B) if A ∩ B = ∅

### Basic Rules
- **Complement**: P(Aᶜ) = 1 - P(A)
- **Union**: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
- **Intersection**: P(A ∩ B) = P(A|B) × P(B)

### Independence
Events A and B are independent if:
P(A ∩ B) = P(A) × P(B)

---

## Random Variables

### Definition
A random variable X is a function that assigns a real number to each outcome in the sample space.

### Types
- **Discrete**: Countable outcomes (coin flips, dice)
- **Continuous**: Uncountable outcomes (height, weight)

### Probability Mass Function (PMF) - Discrete
P(X = x) = probability that X takes value x

**Properties:**
- P(X = x) ≥ 0 for all x
- Σₓ P(X = x) = 1

### Probability Density Function (PDF) - Continuous
f(x) such that P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx

**Properties:**
- f(x) ≥ 0 for all x
- ∫₋∞^∞ f(x) dx = 1

### Cumulative Distribution Function (CDF)
F(x) = P(X ≤ x)

**Properties:**
- F(x) is non-decreasing
- lim_{x→-∞} F(x) = 0, lim_{x→∞} F(x) = 1
- For continuous X: f(x) = F'(x)

---

## Probability Distributions

### Discrete Distributions

#### Bernoulli Distribution
**Use**: Single trial with success/failure
**PMF**: P(X = 1) = p, P(X = 0) = 1-p
**Parameters**: p ∈ [0,1]
**Mean**: p, **Variance**: p(1-p)

#### Binomial Distribution
**Use**: Number of successes in n trials
**PMF**: P(X = k) = C(n,k) × pᵏ × (1-p)ⁿ⁻ᵏ
**Parameters**: n (trials), p (success probability)
**Mean**: np, **Variance**: np(1-p)

#### Poisson Distribution
**Use**: Number of events in fixed interval
**PMF**: P(X = k) = (λᵏ × e⁻λ) / k!
**Parameters**: λ > 0 (rate)
**Mean**: λ, **Variance**: λ

### Continuous Distributions

#### Uniform Distribution
**Use**: Equal probability over interval
**PDF**: f(x) = 1/(b-a) for x ∈ [a,b]
**Parameters**: a, b (interval bounds)
**Mean**: (a+b)/2, **Variance**: (b-a)²/12

#### Normal (Gaussian) Distribution
**Use**: Most common continuous distribution
**PDF**: f(x) = (1/√(2πσ²)) × exp(-(x-μ)²/(2σ²))
**Parameters**: μ (mean), σ² (variance)
**Mean**: μ, **Variance**: σ²

#### Exponential Distribution
**Use**: Time between events
**PDF**: f(x) = λe⁻λˣ for x ≥ 0
**Parameters**: λ > 0 (rate)
**Mean**: 1/λ, **Variance**: 1/λ²

---

## Bayes' Theorem

### Formula
P(A|B) = P(B|A) × P(A) / P(B)

### Components
- **P(A|B)**: Posterior probability
- **P(B|A)**: Likelihood
- **P(A)**: Prior probability
- **P(B)**: Evidence (marginal probability)

### Extended Form
P(A|B) = P(B|A) × P(A) / [P(B|A) × P(A) + P(B|Aᶜ) × P(Aᶜ)]

### ML Applications
- **Naive Bayes Classifier**: Assumes feature independence
- **Bayesian Inference**: Update beliefs with new evidence
- **A/B Testing**: Compare treatment effects
- **Medical Diagnosis**: Disease probability given symptoms

---

## Joint and Conditional Probability

### Joint Probability
P(X = x, Y = y) = probability that X = x AND Y = y

### Marginal Probability
P(X = x) = Σᵧ P(X = x, Y = y) (discrete)
P(X = x) = ∫ P(X = x, Y = y) dy (continuous)

### Conditional Probability
P(X = x | Y = y) = P(X = x, Y = y) / P(Y = y)

### Independence
X and Y are independent if:
P(X = x, Y = y) = P(X = x) × P(Y = y)

### Chain Rule
P(X₁, X₂, ..., Xₙ) = P(X₁) × P(X₂|X₁) × P(X₃|X₁,X₂) × ... × P(Xₙ|X₁,...,Xₙ₋₁)

---

## Expectation and Variance

### Expectation (Mean)
**Discrete**: E[X] = Σₓ x × P(X = x)
**Continuous**: E[X] = ∫ x × f(x) dx

### Properties of Expectation
- **Linearity**: E[aX + bY] = aE[X] + bE[Y]
- **Independence**: E[XY] = E[X] × E[Y] if X, Y independent

### Variance
Var(X) = E[(X - E[X])²] = E[X²] - (E[X])²

### Properties of Variance
- **Scaling**: Var(aX) = a² × Var(X)
- **Independence**: Var(X + Y) = Var(X) + Var(Y) if X, Y independent

### Standard Deviation
σ = √Var(X)

### Covariance
Cov(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y]

### Correlation
ρ(X, Y) = Cov(X, Y) / (σₓ × σᵧ)
**Range**: [-1, 1]

---

## Common Distributions

### Central Limit Theorem
For large n, the sum of independent random variables approaches normal distribution:
(X₁ + X₂ + ... + Xₙ - nμ) / (σ√n) → N(0, 1)

### Law of Large Numbers
Sample mean converges to population mean as n → ∞:
(X₁ + X₂ + ... + Xₙ) / n → E[X]

### Maximum Likelihood Estimation (MLE)
Find parameters θ that maximize likelihood:
θ̂ = argmax_θ L(θ) = argmax_θ ∏ᵢ P(xᵢ|θ)

### Maximum A Posteriori (MAP)
Find parameters that maximize posterior:
θ̂ = argmax_θ P(θ|data) ∝ argmax_θ P(data|θ) × P(θ)

---

## Applications in ML/AI

### 1. Naive Bayes Classifier
```
P(class|features) ∝ P(class) × ∏ᵢ P(featureᵢ|class)
```

### 2. Logistic Regression
```
P(y=1|x) = 1 / (1 + exp(-(w·x + b)))
```

### 3. Gaussian Mixture Models
```
P(x) = Σₖ πₖ × N(x|μₖ, Σₖ)
```

### 4. Hidden Markov Models
```
P(observations|states) = ∏ₜ P(oₜ|sₜ)
P(states) = P(s₁) × ∏ₜ P(sₜ|sₜ₋₁)
```

### 5. Bayesian Neural Networks
```
P(weights|data) ∝ P(data|weights) × P(weights)
```

---

## Practice Problems

### Problem 1: Basic Probability
A bag contains 3 red balls and 2 blue balls. What's the probability of drawing 2 red balls without replacement?

**Solution:**
P(1st red) = 3/5
P(2nd red | 1st red) = 2/4 = 1/2
P(both red) = (3/5) × (1/2) = 3/10 = 0.3

### Problem 2: Bayes' Theorem
A medical test is 95% accurate. Disease prevalence is 1%. If you test positive, what's the probability you have the disease?

**Solution:**
- P(Disease) = 0.01
- P(Test+|Disease) = 0.95
- P(Test+|No Disease) = 0.05

P(Disease|Test+) = P(Test+|Disease) × P(Disease) / P(Test+)
P(Test+) = 0.95 × 0.01 + 0.05 × 0.99 = 0.0095 + 0.0495 = 0.059
P(Disease|Test+) = (0.95 × 0.01) / 0.059 ≈ 0.161 = 16.1%

### Problem 3: Normal Distribution
X ~ N(100, 15²). Find P(85 < X < 115).

**Solution:**
Standardize: Z = (X - 100) / 15
P(85 < X < 115) = P(-1 < Z < 1) ≈ 0.68 (68% rule)

### Problem 4: Expected Value
A lottery ticket costs $2. Win $100 with probability 0.01, $10 with probability 0.1, nothing otherwise. What's the expected profit?

**Solution:**
E[Profit] = 0.01 × (100-2) + 0.1 × (10-2) + 0.89 × (0-2)
E[Profit] = 0.98 + 0.8 - 1.78 = $0.00

---

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# Basic probability calculations
def basic_probability():
    # Simulate coin flips
    n_flips = 1000
    flips = np.random.choice(['H', 'T'], size=n_flips)
    prob_heads = np.mean(flips == 'H')
    print(f"Probability of heads (simulated): {prob_heads:.3f}")
    
    # Theoretical vs empirical probability
    n_trials = np.arange(1, n_flips + 1)
    cumulative_prob = np.cumsum(flips == 'H') / n_trials
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_trials, cumulative_prob, 'b-', alpha=0.7)
    plt.axhline(y=0.5, color='r', linestyle='--', label='Theoretical (0.5)')
    plt.xlabel('Number of Flips')
    plt.ylabel('Probability of Heads')
    plt.title('Law of Large Numbers: Coin Flips')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

# Common distributions
def plot_distributions():
    x = np.linspace(-4, 4, 1000)
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # Normal distribution
    axes[0, 0].plot(x, stats.norm.pdf(x, 0, 1), 'b-', label='μ=0, σ=1')
    axes[0, 0].plot(x, stats.norm.pdf(x, 0, 0.5), 'r-', label='μ=0, σ=0.5')
    axes[0, 0].plot(x, stats.norm.pdf(x, 1, 1), 'g-', label='μ=1, σ=1')
    axes[0, 0].set_title('Normal Distribution')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # Exponential distribution
    x_exp = np.linspace(0, 5, 1000)
    axes[0, 1].plot(x_exp, stats.expon.pdf(x_exp, scale=1), 'b-', label='λ=1')
    axes[0, 1].plot(x_exp, stats.expon.pdf(x_exp, scale=0.5), 'r-', label='λ=2')
    axes[0, 1].plot(x_exp, stats.expon.pdf(x_exp, scale=2), 'g-', label='λ=0.5')
    axes[0, 1].set_title('Exponential Distribution')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # Uniform distribution
    x_unif = np.linspace(-2, 3, 1000)
    axes[0, 2].plot(x_unif, stats.uniform.pdf(x_unif, 0, 1), 'b-', label='[0,1]')
    axes[0, 2].plot(x_unif, stats.uniform.pdf(x_unif, -1, 2), 'r-', label='[-1,1]')
    axes[0, 2].set_title('Uniform Distribution')
    axes[0, 2].legend()
    axes[0, 2].grid(True, alpha=0.3)
    
    # Binomial distribution
    x_binom = np.arange(0, 21)
    axes[1, 0].bar(x_binom, stats.binom.pmf(x_binom, 20, 0.3), alpha=0.7, label='n=20, p=0.3')
    axes[1, 0].bar(x_binom, stats.binom.pmf(x_binom, 20, 0.7), alpha=0.7, label='n=20, p=0.7')
    axes[1, 0].set_title('Binomial Distribution')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # Poisson distribution
    x_pois = np.arange(0, 15)
    axes[1, 1].bar(x_pois, stats.poisson.pmf(x_pois, 2), alpha=0.7, label='λ=2')
    axes[1, 1].bar(x_pois, stats.poisson.pmf(x_pois, 5), alpha=0.7, label='λ=5')
    axes[1, 1].set_title('Poisson Distribution')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    # Beta distribution
    x_beta = np.linspace(0, 1, 1000)
    axes[1, 2].plot(x_beta, stats.beta.pdf(x_beta, 2, 2), 'b-', label='α=2, β=2')
    axes[1, 2].plot(x_beta, stats.beta.pdf(x_beta, 1, 3), 'r-', label='α=1, β=3')
    axes[1, 2].plot(x_beta, stats.beta.pdf(x_beta, 3, 1), 'g-', label='α=3, β=1')
    axes[1, 2].set_title('Beta Distribution')
    axes[1, 2].legend()
    axes[1, 2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# Bayes' theorem example
def bayes_theorem_example():
    # Medical diagnosis example
    # P(Disease) = 0.01 (1% prevalence)
    # P(Test+|Disease) = 0.95 (95% sensitivity)
    # P(Test+|No Disease) = 0.05 (5% false positive rate)
    
    prior_disease = 0.01
    sensitivity = 0.95
    false_positive_rate = 0.05
    
    # Calculate posterior probability
    evidence = sensitivity * prior_disease + false_positive_rate * (1 - prior_disease)
    posterior_disease = (sensitivity * prior_disease) / evidence
    
    print("Medical Diagnosis Example:")
    print(f"Prior probability of disease: {prior_disease:.1%}")
    print(f"Test sensitivity: {sensitivity:.1%}")
    print(f"False positive rate: {false_positive_rate:.1%}")
    print(f"Posterior probability given positive test: {posterior_disease:.1%}")
    
    # Visualize how prior affects posterior
    priors = np.linspace(0.001, 0.1, 100)
    posteriors = []
    
    for prior in priors:
        evidence = sensitivity * prior + false_positive_rate * (1 - prior)
        posterior = (sensitivity * prior) / evidence
        posteriors.append(posterior)
    
    plt.figure(figsize=(10, 6))
    plt.plot(priors * 100, np.array(posteriors) * 100, 'b-', linewidth=2)
    plt.axvline(x=1, color='r', linestyle='--', label='Original prior (1%)')
    plt.axhline(y=posterior_disease * 100, color='r', linestyle='--', 
                label=f'Posterior ({posterior_disease:.1%})')
    plt.xlabel('Prior Probability (%)')
    plt.ylabel('Posterior Probability (%)')
    plt.title('Effect of Prior on Posterior Probability')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

# Central Limit Theorem demonstration
def central_limit_theorem():
    # Sample from non-normal distribution (exponential)
    n_samples = 1000
    sample_sizes = [1, 5, 10, 30, 100]
    
    fig, axes = plt.subplots(1, len(sample_sizes), figsize=(20, 4))
    
    for i, n in enumerate(sample_sizes):
        # Generate sample means
        sample_means = []
        for _ in range(n_samples):
            sample = np.random.exponential(scale=2, size=n)
            sample_means.append(np.mean(sample))
        
        # Plot histogram
        axes[i].hist(sample_means, bins=30, density=True, alpha=0.7, 
                    color='skyblue', edgecolor='black')
        
        # Overlay theoretical normal distribution
        mean_of_means = 2  # True mean of exponential(2)
        std_of_means = 2 / np.sqrt(n)  # Standard error
        x = np.linspace(min(sample_means), max(sample_means), 100)
        axes[i].plot(x, stats.norm.pdf(x, mean_of_means, std_of_means), 
                    'r-', linewidth=2, label='Theoretical Normal')
        
        axes[i].set_title(f'Sample Size: {n}')
        axes[i].set_xlabel('Sample Mean')
        axes[i].set_ylabel('Density')
        axes[i].legend()
        axes[i].grid(True, alpha=0.3)
    
    plt.suptitle('Central Limit Theorem: Sample Means from Exponential Distribution')
    plt.tight_layout()
    plt.show()

# Maximum Likelihood Estimation example
def mle_example():
    # Generate data from normal distribution
    true_mu, true_sigma = 5, 2
    n_samples = 100
    data = np.random.normal(true_mu, true_sigma, n_samples)
    
    # MLE for normal distribution
    mle_mu = np.mean(data)
    mle_sigma = np.sqrt(np.mean((data - mle_mu)**2))
    
    print("Maximum Likelihood Estimation:")
    print(f"True parameters: μ = {true_mu}, σ = {true_sigma}")
    print(f"MLE estimates: μ̂ = {mle_mu:.3f}, σ̂ = {mle_sigma:.3f}")
    
    # Plot data and fitted distribution
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=20, density=True, alpha=0.7, color='skyblue', 
             edgecolor='black', label='Data')
    
    x = np.linspace(data.min(), data.max(), 100)
    plt.plot(x, stats.norm.pdf(x, true_mu, true_sigma), 'r-', 
             linewidth=2, label=f'True: N({true_mu}, {true_sigma}²)')
    plt.plot(x, stats.norm.pdf(x, mle_mu, mle_sigma), 'g--', 
             linewidth=2, label=f'MLE: N({mle_mu:.2f}, {mle_sigma:.2f}²)')
    
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.title('Maximum Likelihood Estimation for Normal Distribution')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

# Naive Bayes classifier example
def naive_bayes_example():
    from sklearn.datasets import make_classification
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, classification_report
    
    # Generate sample data
    X, y = make_classification(n_samples=1000, n_features=2, n_redundant=0, 
                              n_informative=2, n_clusters_per_class=1, 
                              random_state=42)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, 
                                                        random_state=42)
    
    # Train Naive Bayes classifier
    nb = GaussianNB()
    nb.fit(X_train, y_train)
    
    # Make predictions
    y_pred = nb.predict(X_test)
    y_pred_proba = nb.predict_proba(X_test)
    
    print("Naive Bayes Classifier:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Visualize decision boundary
    plt.figure(figsize=(12, 5))
    
    # Plot 1: Data points
    plt.subplot(1, 2, 1)
    scatter = plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, 
                         cmap='viridis', alpha=0.7)
    plt.colorbar(scatter)
    plt.title('True Labels')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    
    # Plot 2: Predicted probabilities
    plt.subplot(1, 2, 2)
    scatter = plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred_proba[:, 1], 
                         cmap='viridis', alpha=0.7)
    plt.colorbar(scatter, label='P(Class=1)')
    plt.title('Predicted Probabilities')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("=== Basic Probability ===")
    basic_probability()
    
    print("\n=== Probability Distributions ===")
    plot_distributions()
    
    print("\n=== Bayes' Theorem ===")
    bayes_theorem_example()
    
    print("\n=== Central Limit Theorem ===")
    central_limit_theorem()
    
    print("\n=== Maximum Likelihood Estimation ===")
    mle_example()
    
    print("\n=== Naive Bayes Classifier ===")
    naive_bayes_example()
```

---

## 🎯 Key Takeaways

1. **Probability is Fundamental**: Every ML algorithm involves uncertainty
2. **Master Bayes' Theorem**: Critical for Bayesian methods and inference
3. **Understand Distributions**: Know when to use each distribution
4. **Learn MLE and MAP**: Core parameter estimation techniques
5. **Practice with Code**: Implement probability concepts in Python
6. **Connect to ML**: See probability in classification, regression, and generation

---

## 📚 Next Steps

After mastering probability theory, proceed to:
1. **Statistics** - Hypothesis testing and inference
2. **Calculus** - Derivatives for optimization
3. **Information Theory** - Entropy and mutual information
4. **Optimization Theory** - Advanced optimization techniques

---

## 🔗 Resources

- **Khan Academy**: Probability and statistics
- **3Blue1Brown**: Bayes' theorem visualization
- **SciPy Documentation**: Statistical functions
- **Think Stats**: Probability and statistics for programmers
- **Pattern Recognition and Machine Learning**: Bishop's book

---

*Probability theory is the language of uncertainty in ML/AI. Master it to understand how algorithms make decisions under uncertainty!*