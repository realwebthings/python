# 📊 Statistics Fundamentals for ML/AI

## 📋 Table of Contents
- [Overview](#overview)
- [Descriptive Statistics](#descriptive-statistics)
- [Probability Distributions](#probability-distributions)
- [Sampling and Estimation](#sampling-and-estimation)
- [Hypothesis Testing](#hypothesis-testing)
- [Regression Analysis](#regression-analysis)
- [Correlation and Dependence](#correlation-and-dependence)
- [Bayesian Statistics](#bayesian-statistics)
- [Applications in ML/AI](#applications-in-mlai)
- [Practice Problems](#practice-problems)
- [Python Implementation](#python-implementation)

---

## Overview

Statistics is the **science of learning from data** and the foundation of data-driven decision making in ML/AI:

### 🎯 **Critical Applications:**
- **Data Analysis**: Understanding patterns and trends in datasets
- **Model Evaluation**: Assessing performance and significance
- **Hypothesis Testing**: Validating assumptions and theories
- **Uncertainty Quantification**: Measuring confidence in predictions
- **A/B Testing**: Comparing different models or strategies
- **Feature Selection**: Identifying important variables
- **Anomaly Detection**: Finding outliers and unusual patterns

---

## Descriptive Statistics

### Measures of Central Tendency

#### **Mean (Average)**
**Population Mean**: μ = (Σxᵢ) / N
**Sample Mean**: x̄ = (Σxᵢ) / n

**Example**: Test scores [85, 90, 78, 92, 88]
Mean = (85 + 90 + 78 + 92 + 88) / 5 = 86.6

**Properties**:
- Sensitive to outliers
- Minimizes sum of squared deviations
- Used in linear regression

```python
import numpy as np

scores = [85, 90, 78, 92, 88]
mean_score = np.mean(scores)
print(f"Mean score: {mean_score}")
```

#### **Median**
The middle value when data is ordered.

**Example**: [78, 85, 88, 90, 92] → Median = 88

**Properties**:
- Robust to outliers
- 50th percentile
- Used in robust statistics

```python
median_score = np.median(scores)
print(f"Median score: {median_score}")
```

#### **Mode**
The most frequently occurring value.

**Example**: [1, 2, 2, 3, 4, 2, 5] → Mode = 2

**Properties**:
- Can have multiple modes
- Used for categorical data
- Relevant for discrete distributions

```python
from scipy import stats

data = [1, 2, 2, 3, 4, 2, 5]
mode_result = stats.mode(data)
print(f"Mode: {mode_result.mode[0]}")
```

### Measures of Variability

#### **Variance**
**Population Variance**: σ² = Σ(xᵢ - μ)² / N
**Sample Variance**: s² = Σ(xᵢ - x̄)² / (n-1)

**Example**: For scores [85, 90, 78, 92, 88] with mean 86.6:
s² = [(85-86.6)² + (90-86.6)² + (78-86.6)² + (92-86.6)² + (88-86.6)²] / 4
s² = [2.56 + 11.56 + 73.96 + 29.16 + 1.96] / 4 = 29.8

```python
variance = np.var(scores, ddof=1)  # ddof=1 for sample variance
print(f"Sample variance: {variance}")
```

#### **Standard Deviation**
σ = √σ² (population) or s = √s² (sample)

**Example**: s = √29.8 ≈ 5.46

**Interpretation**: About 68% of data falls within 1 standard deviation of the mean.

```python
std_dev = np.std(scores, ddof=1)
print(f"Standard deviation: {std_dev}")
```

#### **Range**
Range = Maximum - Minimum

**Example**: Range = 92 - 78 = 14

#### **Interquartile Range (IQR)**
IQR = Q₃ - Q₁ (75th percentile - 25th percentile)

**Properties**:
- Robust to outliers
- Used in box plots
- Identifies outliers: values outside [Q₁ - 1.5×IQR, Q₃ + 1.5×IQR]

```python
q1 = np.percentile(scores, 25)
q3 = np.percentile(scores, 75)
iqr = q3 - q1
print(f"Q1: {q1}, Q3: {q3}, IQR: {iqr}")
```

### Shape of Distribution

#### **Skewness**
Measures asymmetry of distribution.

**Formula**: Skewness = E[(X - μ)³] / σ³

**Interpretation**:
- Skewness = 0: Symmetric (normal distribution)
- Skewness > 0: Right-skewed (tail extends right)
- Skewness < 0: Left-skewed (tail extends left)

```python
skewness = stats.skew(scores)
print(f"Skewness: {skewness}")
```

#### **Kurtosis**
Measures tail heaviness of distribution.

**Formula**: Kurtosis = E[(X - μ)⁴] / σ⁴

**Interpretation**:
- Kurtosis = 3: Normal distribution (mesokurtic)
- Kurtosis > 3: Heavy tails (leptokurtic)
- Kurtosis < 3: Light tails (platykurtic)

```python
kurt = stats.kurtosis(scores)
print(f"Kurtosis: {kurt}")
```

---

## Probability Distributions

### Normal Distribution
**PDF**: f(x) = (1/√(2πσ²)) × exp(-(x-μ)²/(2σ²))

**Properties**:
- Bell-shaped, symmetric
- Mean = Median = Mode = μ
- 68-95-99.7 rule (empirical rule)

**Example**: IQ scores ~ N(100, 15²)
- 68% of people have IQ between 85-115
- 95% have IQ between 70-130
- 99.7% have IQ between 55-145

```python
import matplotlib.pyplot as plt

# Generate normal distribution
mu, sigma = 100, 15
x = np.linspace(50, 150, 1000)
y = stats.norm.pdf(x, mu, sigma)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label=f'N({mu}, {sigma}²)')
plt.axvline(mu, color='r', linestyle='--', label='Mean')
plt.axvline(mu - sigma, color='g', linestyle=':', alpha=0.7, label='±1σ')
plt.axvline(mu + sigma, color='g', linestyle=':', alpha=0.7)
plt.fill_between(x, y, alpha=0.3)
plt.xlabel('IQ Score')
plt.ylabel('Probability Density')
plt.title('Normal Distribution of IQ Scores')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### Standard Normal Distribution
Z ~ N(0, 1) where Z = (X - μ) / σ

**Uses**:
- Standardizing any normal distribution
- Computing probabilities and percentiles
- Hypothesis testing

```python
# Standardize IQ score of 115
iq_score = 115
z_score = (iq_score - mu) / sigma
print(f"IQ {iq_score} corresponds to z-score: {z_score}")

# Probability of IQ ≤ 115
prob = stats.norm.cdf(z_score)
print(f"P(IQ ≤ 115) = {prob:.3f}")
```

### t-Distribution
Used when sample size is small and population standard deviation is unknown.

**Properties**:
- Similar to normal but heavier tails
- Approaches normal as degrees of freedom increase
- Used in t-tests and confidence intervals

```python
# Compare t-distribution with normal
df_values = [1, 5, 30]
x = np.linspace(-4, 4, 1000)

plt.figure(figsize=(10, 6))
plt.plot(x, stats.norm.pdf(x), 'k-', linewidth=2, label='Normal')

for df in df_values:
    plt.plot(x, stats.t.pdf(x, df), '--', linewidth=2, label=f't(df={df})')

plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Comparison of t-distributions with Normal')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### Chi-Square Distribution
Used in goodness-of-fit tests and variance testing.

**Properties**:
- Always positive
- Right-skewed
- Shape depends on degrees of freedom

### F-Distribution
Used in ANOVA and regression analysis.

**Properties**:
- Always positive
- Used to compare variances
- F = (variance₁) / (variance₂)

---

## Sampling and Estimation

### Sampling Methods

#### **Simple Random Sampling**
Every element has equal probability of selection.

```python
# Simple random sampling
population = list(range(1, 1001))  # Population of 1000
sample_size = 100
sample = np.random.choice(population, size=sample_size, replace=False)
print(f"Sample mean: {np.mean(sample)}")
print(f"Population mean: {np.mean(population)}")
```

#### **Stratified Sampling**
Population divided into strata, sample from each stratum.

```python
# Stratified sampling example
def stratified_sample(data, strata_column, sample_size):
    """Perform stratified sampling"""
    import pandas as pd
    
    df = pd.DataFrame(data)
    samples = []
    
    for stratum in df[strata_column].unique():
        stratum_data = df[df[strata_column] == stratum]
        stratum_sample_size = int(sample_size * len(stratum_data) / len(df))
        stratum_sample = stratum_data.sample(n=stratum_sample_size)
        samples.append(stratum_sample)
    
    return pd.concat(samples)
```

#### **Systematic Sampling**
Select every kth element after random start.

### Central Limit Theorem
For large sample sizes, the sampling distribution of the mean approaches normal distribution.

**Mathematical Statement**: If X₁, X₂, ..., Xₙ are independent with mean μ and variance σ², then:
(X̄ - μ) / (σ/√n) → N(0, 1) as n → ∞

```python
# Demonstrate Central Limit Theorem
def demonstrate_clt():
    # Population: exponential distribution (highly skewed)
    population_size = 10000
    population = np.random.exponential(scale=2, size=population_size)
    
    # Sample means for different sample sizes
    sample_sizes = [5, 10, 30, 100]
    n_samples = 1000
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.ravel()
    
    for i, n in enumerate(sample_sizes):
        sample_means = []
        for _ in range(n_samples):
            sample = np.random.choice(population, size=n)
            sample_means.append(np.mean(sample))
        
        axes[i].hist(sample_means, bins=50, density=True, alpha=0.7, 
                    color='skyblue', edgecolor='black')
        
        # Overlay theoretical normal distribution
        mean_of_means = np.mean(population)
        std_of_means = np.std(population) / np.sqrt(n)
        x = np.linspace(min(sample_means), max(sample_means), 100)
        axes[i].plot(x, stats.norm.pdf(x, mean_of_means, std_of_means), 
                    'r-', linewidth=2, label='Theoretical Normal')
        
        axes[i].set_title(f'Sample Size: {n}')
        axes[i].set_xlabel('Sample Mean')
        axes[i].set_ylabel('Density')
        axes[i].legend()
        axes[i].grid(True, alpha=0.3)
    
    plt.suptitle('Central Limit Theorem Demonstration')
    plt.tight_layout()
    plt.show()

demonstrate_clt()
```

### Confidence Intervals

#### **Confidence Interval for Mean (σ known)**
CI = x̄ ± z_{α/2} × (σ/√n)

#### **Confidence Interval for Mean (σ unknown)**
CI = x̄ ± t_{α/2,n-1} × (s/√n)

```python
def confidence_interval_mean(data, confidence_level=0.95):
    """Calculate confidence interval for mean"""
    n = len(data)
    mean = np.mean(data)
    std_err = stats.sem(data)  # Standard error of mean
    
    # t-critical value
    alpha = 1 - confidence_level
    t_critical = stats.t.ppf(1 - alpha/2, df=n-1)
    
    # Confidence interval
    margin_error = t_critical * std_err
    ci_lower = mean - margin_error
    ci_upper = mean + margin_error
    
    return ci_lower, ci_upper, mean

# Example
sample_data = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
ci_lower, ci_upper, sample_mean = confidence_interval_mean(sample_data)

print(f"Sample mean: {sample_mean:.2f}")
print(f"95% Confidence Interval: [{ci_lower:.2f}, {ci_upper:.2f}]")
print(f"Interpretation: We are 95% confident the true mean is between {ci_lower:.2f} and {ci_upper:.2f}")
```

---

## Hypothesis Testing

### Steps in Hypothesis Testing
1. **State hypotheses**: H₀ (null) and H₁ (alternative)
2. **Choose significance level**: α (typically 0.05)
3. **Calculate test statistic**
4. **Find p-value**
5. **Make decision**: Reject H₀ if p-value < α

### One-Sample t-Test
Tests if sample mean differs from hypothesized population mean.

**Example**: Test if average student height is 170 cm.
- H₀: μ = 170
- H₁: μ ≠ 170

```python
def one_sample_t_test(data, hypothesized_mean, alpha=0.05):
    """Perform one-sample t-test"""
    n = len(data)
    sample_mean = np.mean(data)
    sample_std = np.std(data, ddof=1)
    
    # Calculate t-statistic
    t_stat = (sample_mean - hypothesized_mean) / (sample_std / np.sqrt(n))
    
    # Calculate p-value (two-tailed)
    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=n-1))
    
    # Decision
    reject_null = p_value < alpha
    
    print(f"One-Sample t-Test Results:")
    print(f"Sample mean: {sample_mean:.2f}")
    print(f"Hypothesized mean: {hypothesized_mean}")
    print(f"t-statistic: {t_stat:.3f}")
    print(f"p-value: {p_value:.4f}")
    print(f"Significance level: {alpha}")
    print(f"Decision: {'Reject' if reject_null else 'Fail to reject'} H₀")
    
    return t_stat, p_value, reject_null

# Example: Test if average height is 170 cm
heights = [168, 172, 165, 175, 170, 169, 173, 167, 171, 174]
one_sample_t_test(heights, hypothesized_mean=170)
```

### Two-Sample t-Test
Tests if means of two groups are different.

**Example**: Compare test scores between two teaching methods.

```python
def two_sample_t_test(group1, group2, alpha=0.05):
    """Perform independent two-sample t-test"""
    # Calculate statistics
    n1, n2 = len(group1), len(group2)
    mean1, mean2 = np.mean(group1), np.mean(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    
    # Pooled standard error
    pooled_se = np.sqrt(var1/n1 + var2/n2)
    
    # t-statistic
    t_stat = (mean1 - mean2) / pooled_se
    
    # Degrees of freedom (Welch's formula)
    df = (var1/n1 + var2/n2)**2 / ((var1/n1)**2/(n1-1) + (var2/n2)**2/(n2-1))
    
    # p-value (two-tailed)
    p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=df))
    
    # Decision
    reject_null = p_value < alpha
    
    print(f"Two-Sample t-Test Results:")
    print(f"Group 1 mean: {mean1:.2f} (n={n1})")
    print(f"Group 2 mean: {mean2:.2f} (n={n2})")
    print(f"Difference: {mean1 - mean2:.2f}")
    print(f"t-statistic: {t_stat:.3f}")
    print(f"p-value: {p_value:.4f}")
    print(f"Decision: {'Reject' if reject_null else 'Fail to reject'} H₀")
    
    return t_stat, p_value, reject_null

# Example: Compare two teaching methods
method_a_scores = [85, 88, 92, 78, 90, 87, 89, 91, 86, 84]
method_b_scores = [79, 82, 85, 88, 81, 83, 86, 80, 84, 87]

two_sample_t_test(method_a_scores, method_b_scores)
```

### Chi-Square Test of Independence
Tests if two categorical variables are independent.

```python
def chi_square_test(observed_freq):
    """Perform chi-square test of independence"""
    from scipy.stats import chi2_contingency
    
    chi2_stat, p_value, dof, expected_freq = chi2_contingency(observed_freq)
    
    print(f"Chi-Square Test of Independence:")
    print(f"Chi-square statistic: {chi2_stat:.3f}")
    print(f"p-value: {p_value:.4f}")
    print(f"Degrees of freedom: {dof}")
    print(f"Expected frequencies:")
    print(expected_freq)
    
    return chi2_stat, p_value

# Example: Test if gender and preference are independent
# Rows: Gender (Male, Female), Columns: Preference (A, B, C)
observed = [[20, 15, 10],   # Male
           [25, 20, 15]]   # Female

chi_square_test(observed)
```

---

## Regression Analysis

### Simple Linear Regression
Model: Y = β₀ + β₁X + ε

**Least Squares Estimates**:
- β₁ = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)²
- β₀ = ȳ - β₁x̄

```python
def simple_linear_regression(x, y):
    """Perform simple linear regression"""
    n = len(x)
    x_mean, y_mean = np.mean(x), np.mean(y)
    
    # Calculate slope and intercept
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean)**2)
    slope = numerator / denominator
    intercept = y_mean - slope * x_mean
    
    # Predictions
    y_pred = intercept + slope * x
    
    # R-squared
    ss_res = np.sum((y - y_pred)**2)
    ss_tot = np.sum((y - y_mean)**2)
    r_squared = 1 - (ss_res / ss_tot)
    
    # Standard error of slope
    mse = ss_res / (n - 2)
    se_slope = np.sqrt(mse / np.sum((x - x_mean)**2))
    
    print(f"Simple Linear Regression Results:")
    print(f"Intercept (β₀): {intercept:.3f}")
    print(f"Slope (β₁): {slope:.3f}")
    print(f"R-squared: {r_squared:.3f}")
    print(f"Standard error of slope: {se_slope:.3f}")
    
    return intercept, slope, r_squared, y_pred

# Example: Predict house price from size
house_size = np.array([1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400])
house_price = np.array([200, 230, 260, 290, 320, 350, 380, 410])

intercept, slope, r_squared, predictions = simple_linear_regression(house_size, house_price)

# Visualization
plt.figure(figsize=(10, 6))
plt.scatter(house_size, house_price, color='blue', alpha=0.7, label='Data')
plt.plot(house_size, predictions, color='red', linewidth=2, label='Regression Line')
plt.xlabel('House Size (sq ft)')
plt.ylabel('House Price ($1000s)')
plt.title(f'Simple Linear Regression (R² = {r_squared:.3f})')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### Multiple Linear Regression
Model: Y = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ + ε

**Matrix Form**: Y = Xβ + ε
**Solution**: β̂ = (X'X)⁻¹X'Y

```python
def multiple_linear_regression(X, y):
    """Perform multiple linear regression"""
    # Add intercept column
    X_with_intercept = np.column_stack([np.ones(len(X)), X])
    
    # Calculate coefficients using normal equation
    XtX = X_with_intercept.T @ X_with_intercept
    Xty = X_with_intercept.T @ y
    coefficients = np.linalg.solve(XtX, Xty)
    
    # Predictions
    y_pred = X_with_intercept @ coefficients
    
    # R-squared
    ss_res = np.sum((y - y_pred)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r_squared = 1 - (ss_res / ss_tot)
    
    # Adjusted R-squared
    n, p = X_with_intercept.shape
    adj_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - p)
    
    print(f"Multiple Linear Regression Results:")
    print(f"Coefficients: {coefficients}")
    print(f"R-squared: {r_squared:.3f}")
    print(f"Adjusted R-squared: {adj_r_squared:.3f}")
    
    return coefficients, r_squared, y_pred

# Example: Predict house price from size and age
house_data = np.array([[1000, 5], [1200, 3], [1400, 8], [1600, 2], 
                      [1800, 10], [2000, 1], [2200, 6], [2400, 4]])
house_prices = np.array([200, 230, 250, 290, 300, 350, 370, 410])

coeffs, r_sq, preds = multiple_linear_regression(house_data, house_prices)
```

---

## Correlation and Dependence

### Pearson Correlation Coefficient
Measures linear relationship between two variables.

**Formula**: r = Σ(xᵢ - x̄)(yᵢ - ȳ) / √[Σ(xᵢ - x̄)²Σ(yᵢ - ȳ)²]

**Interpretation**:
- r = 1: Perfect positive correlation
- r = 0: No linear correlation
- r = -1: Perfect negative correlation

```python
def correlation_analysis(x, y):
    """Analyze correlation between two variables"""
    # Pearson correlation
    pearson_r, pearson_p = stats.pearsonr(x, y)
    
    # Spearman correlation (rank-based)
    spearman_r, spearman_p = stats.spearmanr(x, y)
    
    print(f"Correlation Analysis:")
    print(f"Pearson correlation: r = {pearson_r:.3f}, p = {pearson_p:.4f}")
    print(f"Spearman correlation: ρ = {spearman_r:.3f}, p = {spearman_p:.4f}")
    
    # Visualization
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.7)
    
    # Add regression line
    slope, intercept = np.polyfit(x, y, 1)
    line_x = np.linspace(min(x), max(x), 100)
    line_y = slope * line_x + intercept
    plt.plot(line_x, line_y, 'r-', linewidth=2)
    
    plt.xlabel('X Variable')
    plt.ylabel('Y Variable')
    plt.title(f'Correlation Analysis (r = {pearson_r:.3f})')
    plt.grid(True, alpha=0.3)
    plt.show()
    
    return pearson_r, spearman_r

# Example: Correlation between study hours and test scores
study_hours = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
test_scores = [65, 70, 75, 80, 85, 88, 90, 92, 95, 98]

correlation_analysis(study_hours, test_scores)
```

---

## Bayesian Statistics

### Bayes' Theorem in Statistics
P(θ|data) = P(data|θ) × P(θ) / P(data)

Where:
- P(θ|data): Posterior distribution
- P(data|θ): Likelihood
- P(θ): Prior distribution
- P(data): Marginal likelihood (evidence)

### Bayesian vs Frequentist Approaches

**Frequentist**:
- Parameters are fixed but unknown
- Probability refers to long-run frequency
- Confidence intervals

**Bayesian**:
- Parameters are random variables
- Probability represents degree of belief
- Credible intervals

```python
def bayesian_coin_flip_analysis(flips, prior_alpha=1, prior_beta=1):
    """Bayesian analysis of coin flip data"""
    # Count heads and tails
    heads = sum(flips)
    tails = len(flips) - heads
    
    # Update Beta prior with binomial likelihood
    posterior_alpha = prior_alpha + heads
    posterior_beta = prior_beta + tails
    
    # Posterior statistics
    posterior_mean = posterior_alpha / (posterior_alpha + posterior_beta)
    posterior_var = (posterior_alpha * posterior_beta) / \
                   ((posterior_alpha + posterior_beta)**2 * (posterior_alpha + posterior_beta + 1))
    
    print(f"Bayesian Coin Flip Analysis:")
    print(f"Data: {heads} heads out of {len(flips)} flips")
    print(f"Prior: Beta({prior_alpha}, {prior_beta})")
    print(f"Posterior: Beta({posterior_alpha}, {posterior_beta})")
    print(f"Posterior mean: {posterior_mean:.3f}")
    print(f"Posterior std: {np.sqrt(posterior_var):.3f}")
    
    # Credible interval
    credible_interval = stats.beta.interval(0.95, posterior_alpha, posterior_beta)
    print(f"95% Credible interval: [{credible_interval[0]:.3f}, {credible_interval[1]:.3f}]")
    
    # Visualization
    x = np.linspace(0, 1, 1000)
    prior_pdf = stats.beta.pdf(x, prior_alpha, prior_beta)
    posterior_pdf = stats.beta.pdf(x, posterior_alpha, posterior_beta)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, prior_pdf, 'b--', linewidth=2, label='Prior')
    plt.plot(x, posterior_pdf, 'r-', linewidth=2, label='Posterior')
    plt.axvline(posterior_mean, color='r', linestyle=':', label='Posterior Mean')
    plt.fill_between(x, posterior_pdf, alpha=0.3, color='red')
    plt.xlabel('Probability of Heads')
    plt.ylabel('Density')
    plt.title('Bayesian Update: Prior to Posterior')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    
    return posterior_alpha, posterior_beta

# Example: Analyze coin flip data
coin_flips = [1, 0, 1, 1, 0, 1, 1, 1, 0, 1]  # 1 = heads, 0 = tails
bayesian_coin_flip_analysis(coin_flips)
```

---

## Applications in ML/AI

### 1. **Model Evaluation and Validation**
```python
def model_evaluation_statistics(y_true, y_pred):
    """Statistical evaluation of model performance"""
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    
    # Classification metrics
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')
    f1 = f1_score(y_true, y_pred, average='weighted')
    
    print(f"Model Performance Statistics:")
    print(f"Accuracy: {accuracy:.3f}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall: {recall:.3f}")
    print(f"F1-Score: {f1:.3f}")
    
    # Confidence interval for accuracy
    n = len(y_true)
    se_accuracy = np.sqrt(accuracy * (1 - accuracy) / n)
    ci_lower = accuracy - 1.96 * se_accuracy
    ci_upper = accuracy + 1.96 * se_accuracy
    
    print(f"95% CI for Accuracy: [{ci_lower:.3f}, {ci_upper:.3f}]")
```

### 2. **A/B Testing for Model Comparison**
```python
def ab_test_models(model_a_results, model_b_results, alpha=0.05):
    """Statistical comparison of two models using A/B testing"""
    # Convert to success rates
    success_a = np.mean(model_a_results)
    success_b = np.mean(model_b_results)
    n_a, n_b = len(model_a_results), len(model_b_results)
    
    # Pooled proportion
    pooled_p = (sum(model_a_results) + sum(model_b_results)) / (n_a + n_b)
    
    # Standard error
    se = np.sqrt(pooled_p * (1 - pooled_p) * (1/n_a + 1/n_b))
    
    # Z-test statistic
    z_stat = (success_a - success_b) / se
    
    # Two-tailed p-value
    p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    
    print(f"A/B Test Results:")
    print(f"Model A success rate: {success_a:.3f} (n={n_a})")
    print(f"Model B success rate: {success_b:.3f} (n={n_b})")
    print(f"Difference: {success_a - success_b:.3f}")
    print(f"Z-statistic: {z_stat:.3f}")
    print(f"p-value: {p_value:.4f}")
    print(f"Significant at α={alpha}: {p_value < alpha}")
    
    return z_stat, p_value

# Example: Compare two models
model_a_predictions = [1, 1, 0, 1, 1, 0, 1, 1, 1, 0] * 10  # 70% accuracy
model_b_predictions = [1, 1, 1, 1, 0, 1, 1, 1, 1, 1] * 10  # 90% accuracy

ab_test_models(model_a_predictions, model_b_predictions)
```

### 3. **Feature Importance using Statistical Tests**
```python
def feature_importance_statistical(X, y, feature_names):
    """Assess feature importance using statistical tests"""
    from sklearn.feature_selection import f_classif, chi2
    
    # ANOVA F-test for classification
    f_scores, f_pvalues = f_classif(X, y)
    
    # Create results dataframe
    import pandas as pd
    results = pd.DataFrame({
        'Feature': feature_names,
        'F_Score': f_scores,
        'P_Value': f_pvalues,
        'Significant': f_pvalues < 0.05
    })
    
    results = results.sort_values('F_Score', ascending=False)
    
    print("Feature Importance (Statistical Tests):")
    print(results)
    
    return results
```

### 4. **Outlier Detection using Statistical Methods**
```python
def statistical_outlier_detection(data, method='iqr'):
    """Detect outliers using statistical methods"""
    if method == 'iqr':
        Q1 = np.percentile(data, 25)
        Q3 = np.percentile(data, 75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = (data < lower_bound) | (data > upper_bound)
        
    elif method == 'zscore':
        z_scores = np.abs(stats.zscore(data))
        outliers = z_scores > 3
        
    elif method == 'modified_zscore':
        median = np.median(data)
        mad = np.median(np.abs(data - median))
        modified_z_scores = 0.6745 * (data - median) / mad
        outliers = np.abs(modified_z_scores) > 3.5
    
    print(f"Outlier Detection ({method.upper()}):")
    print(f"Number of outliers: {np.sum(outliers)}")
    print(f"Outlier indices: {np.where(outliers)[0]}")
    print(f"Outlier values: {data[outliers]}")
    
    return outliers

# Example: Detect outliers in dataset
sample_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100])  # 100 is outlier
outliers = statistical_outlier_detection(sample_data, method='iqr')
```

---

## Practice Problems

### Problem 1: Descriptive Statistics
Calculate mean, median, mode, variance, and standard deviation for: [2, 4, 4, 4, 5, 5, 7, 9]

**Solutions:**
- Mean: (2+4+4+4+5+5+7+9)/8 = 5
- Median: (4+5)/2 = 4.5
- Mode: 4 (appears 3 times)
- Variance: 4.57
- Standard deviation: 2.14

### Problem 2: Hypothesis Testing
Test if a coin is fair given 60 heads in 100 flips (α = 0.05).

**Solution:**
- H₀: p = 0.5, H₁: p ≠ 0.5
- Test statistic: z = (0.6 - 0.5) / √(0.5×0.5/100) = 2.0
- p-value = 2 × P(Z > 2.0) = 0.046
- Since p < 0.05, reject H₀. Coin is not fair.

### Problem 3: Confidence Interval
Find 95% CI for mean height given sample: [170, 175, 168, 172, 169] cm.

**Solution:**
- Sample mean: 170.8 cm
- Sample std: 2.86 cm
- t₀.₀₂₅,₄ = 2.776
- CI: 170.8 ± 2.776 × (2.86/√5) = [167.25, 174.35]

---

## 🎯 Key Takeaways

1. **Statistics is Data Science**: Essential for understanding and interpreting data
2. **Master Hypothesis Testing**: Critical for validating ML models and experiments
3. **Understand Distributions**: Normal, t, chi-square are everywhere in ML
4. **Learn Confidence Intervals**: Quantify uncertainty in estimates
5. **Practice with Real Data**: Apply statistical methods to actual datasets
6. **Connect to ML**: Every ML algorithm has statistical foundations

---

## 📚 Next Steps

After mastering statistics fundamentals, proceed to:
1. **Bayesian Statistics** - Advanced probabilistic modeling
2. **Experimental Design** - A/B testing and causal inference
3. **Time Series Analysis** - Sequential data analysis
4. **Multivariate Statistics** - High-dimensional data analysis

---

## 🔗 Resources

- **Khan Academy**: Statistics and probability
- **Think Stats**: Statistics for programmers
- **SciPy Documentation**: Statistical functions
- **R Documentation**: Comprehensive statistical methods
- **Coursera**: Statistical inference courses

---

*Statistics provides the tools to extract insights from data and validate our findings. Master it to become a data-driven ML practitioner!*