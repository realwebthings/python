# 📡 Information Theory for ML/AI

## 📋 Table of Contents
- [Overview](#overview)
- [Entropy](#entropy)
- [Mutual Information](#mutual-information)
- [Kullback-Leibler Divergence](#kullback-leibler-divergence)
- [Cross-Entropy](#cross-entropy)
- [Channel Capacity](#channel-capacity)
- [Data Compression](#data-compression)
- [Information-Theoretic Learning](#information-theoretic-learning)
- [Applications in ML/AI](#applications-in-mlai)
- [Practice Problems](#practice-problems)
- [Python Implementation](#python-implementation)

---

## Overview

Information theory is the **mathematical study of information** and its transmission, storage, and processing. It's fundamental to ML/AI:

### 🎯 **Critical Applications:**
- **Loss Functions**: Cross-entropy loss in neural networks
- **Feature Selection**: Mutual information for feature relevance
- **Model Selection**: Information criteria (AIC, BIC)
- **Compression**: Data encoding and representation learning
- **Natural Language Processing**: Language modeling and entropy
- **Generative Models**: Variational autoencoders and information bottleneck
- **Reinforcement Learning**: Information-theoretic exploration

---

## Entropy

### Definition
**Entropy** H(X) measures the average amount of information (uncertainty) in a random variable X.

**Formula**: H(X) = -Σ p(x) log₂ p(x)

Where the sum is over all possible values x of X.

### Properties
1. **Non-negative**: H(X) ≥ 0
2. **Maximum**: H(X) ≤ log₂|X| (achieved when uniform distribution)
3. **Minimum**: H(X) = 0 (achieved when deterministic)

### Intuitive Understanding
- **High entropy**: High uncertainty, many possible outcomes
- **Low entropy**: Low uncertainty, few likely outcomes
- **Units**: Bits (base 2), nats (base e), or dits (base 10)

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy

def calculate_entropy(probabilities, base=2):
    """Calculate entropy of a probability distribution"""
    # Remove zero probabilities to avoid log(0)
    probs = np.array(probabilities)
    probs = probs[probs > 0]
    
    if base == 2:
        return -np.sum(probs * np.log2(probs))
    elif base == np.e:
        return -np.sum(probs * np.log(probs))
    else:
        return -np.sum(probs * np.log(probs) / np.log(base))

# Example 1: Fair coin
fair_coin = [0.5, 0.5]
h_fair = calculate_entropy(fair_coin)
print(f"Entropy of fair coin: {h_fair:.3f} bits")

# Example 2: Biased coin
biased_coin = [0.9, 0.1]
h_biased = calculate_entropy(biased_coin)
print(f"Entropy of biased coin: {h_biased:.3f} bits")

# Example 3: Fair die
fair_die = [1/6] * 6
h_die = calculate_entropy(fair_die)
print(f"Entropy of fair die: {h_die:.3f} bits")
```

### Binary Entropy Function
For binary random variable with probability p:
H(p) = -p log₂(p) - (1-p) log₂(1-p)

```python
def binary_entropy(p):
    """Calculate binary entropy H(p)"""
    if p == 0 or p == 1:
        return 0
    return -p * np.log2(p) - (1-p) * np.log2(1-p)

# Plot binary entropy function
p_values = np.linspace(0.001, 0.999, 1000)
h_values = [binary_entropy(p) for p in p_values]

plt.figure(figsize=(10, 6))
plt.plot(p_values, h_values, 'b-', linewidth=2)
plt.axhline(y=1, color='r', linestyle='--', alpha=0.7, label='Maximum (1 bit)')
plt.axvline(x=0.5, color='g', linestyle='--', alpha=0.7, label='p = 0.5')
plt.xlabel('Probability p')
plt.ylabel('Entropy H(p) [bits]')
plt.title('Binary Entropy Function')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
```

### Joint and Conditional Entropy

#### **Joint Entropy**
H(X, Y) = -Σ Σ p(x, y) log₂ p(x, y)

#### **Conditional Entropy**
H(Y|X) = -Σ Σ p(x, y) log₂ p(y|x) = H(X, Y) - H(X)

**Interpretation**: Average uncertainty in Y given knowledge of X.

```python
def joint_entropy(joint_prob_matrix):
    """Calculate joint entropy H(X,Y)"""
    # Flatten and remove zeros
    probs = joint_prob_matrix.flatten()
    probs = probs[probs > 0]
    return -np.sum(probs * np.log2(probs))

def conditional_entropy(joint_prob_matrix):
    """Calculate conditional entropy H(Y|X)"""
    h_xy = joint_entropy(joint_prob_matrix)
    
    # Marginal probability of X
    p_x = np.sum(joint_prob_matrix, axis=1)
    h_x = calculate_entropy(p_x)
    
    return h_xy - h_x

# Example: Joint distribution
joint_prob = np.array([[0.25, 0.25], 
                      [0.25, 0.25]])  # Independent uniform

h_xy = joint_entropy(joint_prob)
h_y_given_x = conditional_entropy(joint_prob)

print(f"Joint entropy H(X,Y): {h_xy:.3f} bits")
print(f"Conditional entropy H(Y|X): {h_y_given_x:.3f} bits")
```

---

## Mutual Information

### Definition
**Mutual Information** I(X; Y) measures the amount of information shared between two random variables.

**Formula**: I(X; Y) = H(X) - H(X|Y) = H(Y) - H(Y|X) = H(X) + H(Y) - H(X, Y)

### Properties
1. **Symmetric**: I(X; Y) = I(Y; X)
2. **Non-negative**: I(X; Y) ≥ 0
3. **Independence**: I(X; Y) = 0 if X and Y are independent
4. **Upper bound**: I(X; Y) ≤ min(H(X), H(Y))

### Intuitive Understanding
- **High MI**: Variables are highly dependent
- **Low MI**: Variables are nearly independent
- **Zero MI**: Variables are completely independent

```python
def mutual_information(joint_prob_matrix):
    """Calculate mutual information I(X;Y)"""
    # Marginal probabilities
    p_x = np.sum(joint_prob_matrix, axis=1)
    p_y = np.sum(joint_prob_matrix, axis=0)
    
    # Calculate MI using definition: I(X;Y) = H(X) + H(Y) - H(X,Y)
    h_x = calculate_entropy(p_x)
    h_y = calculate_entropy(p_y)
    h_xy = joint_entropy(joint_prob_matrix)
    
    return h_x + h_y - h_xy

def mutual_information_direct(joint_prob_matrix):
    """Calculate MI directly using I(X;Y) = Σ p(x,y) log[p(x,y)/(p(x)p(y))]"""
    p_x = np.sum(joint_prob_matrix, axis=1)
    p_y = np.sum(joint_prob_matrix, axis=0)
    
    mi = 0
    for i in range(joint_prob_matrix.shape[0]):
        for j in range(joint_prob_matrix.shape[1]):
            if joint_prob_matrix[i, j] > 0:
                mi += joint_prob_matrix[i, j] * np.log2(
                    joint_prob_matrix[i, j] / (p_x[i] * p_y[j])
                )
    
    return mi

# Example 1: Independent variables
independent = np.array([[0.25, 0.25], 
                       [0.25, 0.25]])
mi_indep = mutual_information(independent)
print(f"MI (independent): {mi_indep:.3f} bits")

# Example 2: Perfectly dependent variables
dependent = np.array([[0.5, 0.0], 
                     [0.0, 0.5]])
mi_dep = mutual_information(dependent)
print(f"MI (perfectly dependent): {mi_dep:.3f} bits")

# Example 3: Partially dependent variables
partial = np.array([[0.4, 0.1], 
                   [0.1, 0.4]])
mi_partial = mutual_information(partial)
print(f"MI (partially dependent): {mi_partial:.3f} bits")
```

### Normalized Mutual Information
To compare MI across different scales:
NMI(X; Y) = I(X; Y) / √(H(X) × H(Y))

```python
def normalized_mutual_information(joint_prob_matrix):
    """Calculate normalized mutual information"""
    p_x = np.sum(joint_prob_matrix, axis=1)
    p_y = np.sum(joint_prob_matrix, axis=0)
    
    h_x = calculate_entropy(p_x)
    h_y = calculate_entropy(p_y)
    mi = mutual_information(joint_prob_matrix)
    
    if h_x == 0 or h_y == 0:
        return 0
    
    return mi / np.sqrt(h_x * h_y)

nmi = normalized_mutual_information(partial)
print(f"Normalized MI: {nmi:.3f}")
```

---

## Kullback-Leibler Divergence

### Definition
**KL Divergence** D_KL(P||Q) measures how different probability distribution P is from reference distribution Q.

**Formula**: D_KL(P||Q) = Σ p(x) log₂[p(x)/q(x)]

### Properties
1. **Non-negative**: D_KL(P||Q) ≥ 0
2. **Asymmetric**: D_KL(P||Q) ≠ D_KL(Q||P) in general
3. **Zero**: D_KL(P||Q) = 0 if and only if P = Q
4. **Not a metric**: Doesn't satisfy triangle inequality

### Intuitive Understanding
- **Low KL**: Distributions are similar
- **High KL**: Distributions are very different
- **Direction matters**: P→Q vs Q→P give different values

```python
def kl_divergence(p, q, base=2):
    """Calculate KL divergence D_KL(P||Q)"""
    p = np.array(p)
    q = np.array(q)
    
    # Avoid division by zero and log(0)
    mask = (p > 0) & (q > 0)
    
    if base == 2:
        return np.sum(p[mask] * np.log2(p[mask] / q[mask]))
    else:
        return np.sum(p[mask] * np.log(p[mask] / q[mask]) / np.log(base))

# Example 1: Similar distributions
p1 = [0.5, 0.3, 0.2]
q1 = [0.4, 0.4, 0.2]
kl1 = kl_divergence(p1, q1)
print(f"KL(P||Q) similar: {kl1:.3f} bits")

# Example 2: Very different distributions
p2 = [0.9, 0.05, 0.05]
q2 = [0.1, 0.45, 0.45]
kl2 = kl_divergence(p2, q2)
print(f"KL(P||Q) different: {kl2:.3f} bits")

# Example 3: Asymmetry
kl_pq = kl_divergence(p2, q2)
kl_qp = kl_divergence(q2, p2)
print(f"KL(P||Q): {kl_pq:.3f}, KL(Q||P): {kl_qp:.3f}")
```

### Jensen-Shannon Divergence
A symmetric version of KL divergence:
JS(P, Q) = ½D_KL(P||M) + ½D_KL(Q||M)
where M = ½(P + Q)

```python
def jensen_shannon_divergence(p, q):
    """Calculate Jensen-Shannon divergence"""
    p = np.array(p)
    q = np.array(q)
    m = 0.5 * (p + q)
    
    return 0.5 * kl_divergence(p, m) + 0.5 * kl_divergence(q, m)

js = jensen_shannon_divergence(p2, q2)
print(f"Jensen-Shannon divergence: {js:.3f} bits")
```

---

## Cross-Entropy

### Definition
**Cross-entropy** H(P, Q) measures the average number of bits needed to encode events from distribution P using coding scheme optimized for distribution Q.

**Formula**: H(P, Q) = -Σ p(x) log₂ q(x)

### Relationship to KL Divergence
H(P, Q) = H(P) + D_KL(P||Q)

### Applications in ML
- **Loss function**: Cross-entropy loss for classification
- **Model evaluation**: Perplexity in language models
- **Information bottleneck**: Compression and prediction trade-off

```python
def cross_entropy(p, q, base=2):
    """Calculate cross-entropy H(P, Q)"""
    p = np.array(p)
    q = np.array(q)
    
    # Avoid log(0)
    mask = (p > 0) & (q > 0)
    
    if base == 2:
        return -np.sum(p[mask] * np.log2(q[mask]))
    else:
        return -np.sum(p[mask] * np.log(q[mask]) / np.log(base))

# Example: Cross-entropy vs entropy
p_true = [0.7, 0.2, 0.1]
q_model = [0.6, 0.3, 0.1]

h_p = calculate_entropy(p_true)
h_pq = cross_entropy(p_true, q_model)
kl_pq = kl_divergence(p_true, q_model)

print(f"Entropy H(P): {h_p:.3f} bits")
print(f"Cross-entropy H(P,Q): {h_pq:.3f} bits")
print(f"KL divergence: {kl_pq:.3f} bits")
print(f"Verification: H(P,Q) = H(P) + KL(P||Q) = {h_p + kl_pq:.3f}")
```

### Perplexity
Perplexity is 2^(cross-entropy), measuring how well a model predicts a sample.

```python
def perplexity(p, q):
    """Calculate perplexity"""
    ce = cross_entropy(p, q, base=2)
    return 2 ** ce

perp = perplexity(p_true, q_model)
print(f"Perplexity: {perp:.3f}")
```

---

## Channel Capacity

### Definition
**Channel capacity** C is the maximum rate at which information can be reliably transmitted over a communication channel.

### Binary Symmetric Channel (BSC)
For a BSC with error probability p:
C = 1 - H(p) bits per transmission

```python
def bsc_capacity(error_prob):
    """Calculate capacity of Binary Symmetric Channel"""
    if error_prob == 0 or error_prob == 1:
        return 0 if error_prob == 0.5 else 1
    
    h_p = binary_entropy(error_prob)
    return 1 - h_p

# Plot BSC capacity
error_probs = np.linspace(0, 0.5, 1000)
capacities = [bsc_capacity(p) for p in error_probs]

plt.figure(figsize=(10, 6))
plt.plot(error_probs, capacities, 'b-', linewidth=2)
plt.xlabel('Error Probability p')
plt.ylabel('Channel Capacity [bits]')
plt.title('Binary Symmetric Channel Capacity')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='r', linestyle='--', alpha=0.7)
plt.axvline(x=0.5, color='r', linestyle='--', alpha=0.7, label='p = 0.5 (no capacity)')
plt.legend()
plt.show()
```

### Shannon's Channel Coding Theorem
For any rate R < C, there exists a coding scheme that achieves arbitrarily low error probability.

---

## Data Compression

### Huffman Coding
Optimal prefix-free coding that minimizes expected code length.

```python
import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(text):
    """Build Huffman tree and generate codes"""
    # Count frequencies
    freq = Counter(text)
    
    # Build priority queue
    heap = [HuffmanNode(char, f) for char, f in freq.items()]
    heapq.heapify(heap)
    
    # Build Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)
    
    # Generate codes
    root = heap[0]
    codes = {}
    
    def generate_codes(node, code=""):
        if node.char is not None:  # Leaf node
            codes[node.char] = code if code else "0"  # Handle single character
        else:
            generate_codes(node.left, code + "0")
            generate_codes(node.right, code + "1")
    
    generate_codes(root)
    return codes, freq

def analyze_compression(text):
    """Analyze compression efficiency"""
    codes, freq = huffman_coding(text)
    
    # Calculate metrics
    total_chars = len(text)
    unique_chars = len(set(text))
    
    # Original encoding (fixed-length)
    bits_per_char = np.ceil(np.log2(unique_chars))
    original_bits = total_chars * bits_per_char
    
    # Huffman encoding
    huffman_bits = sum(len(codes[char]) * count for char, count in freq.items())
    
    # Theoretical minimum (entropy)
    probs = [count/total_chars for count in freq.values()]
    entropy_bits = calculate_entropy(probs) * total_chars
    
    print(f"Text analysis: '{text}'")
    print(f"Characters: {total_chars}, Unique: {unique_chars}")
    print(f"Huffman codes: {codes}")
    print(f"Original encoding: {original_bits:.0f} bits ({bits_per_char:.0f} bits/char)")
    print(f"Huffman encoding: {huffman_bits:.0f} bits ({huffman_bits/total_chars:.2f} bits/char)")
    print(f"Theoretical minimum: {entropy_bits:.1f} bits ({entropy_bits/total_chars:.2f} bits/char)")
    print(f"Compression ratio: {original_bits/huffman_bits:.2f}:1")
    print(f"Efficiency: {entropy_bits/huffman_bits:.3f} (1.0 = optimal)")

# Example
text = "ABRACADABRA"
analyze_compression(text)
```

---

## Information-Theoretic Learning

### Information Bottleneck Principle
Find representation Z of input X that is maximally informative about target Y:
min I(X; Z) - βI(Z; Y)

### Variational Information Maximization
Maximize mutual information between input and learned representation.

```python
def information_bottleneck_objective(i_xz, i_zy, beta=1.0):
    """Information bottleneck objective"""
    return i_xz - beta * i_zy

# Example: Different β values
i_xz = 2.0  # Information between X and Z
i_zy = 1.5  # Information between Z and Y

betas = [0.1, 0.5, 1.0, 2.0, 5.0]
for beta in betas:
    obj = information_bottleneck_objective(i_xz, i_zy, beta)
    print(f"β = {beta}: Objective = {obj:.2f}")
```

---

## Applications in ML/AI

### 1. **Cross-Entropy Loss in Neural Networks**
```python
def cross_entropy_loss(y_true, y_pred, epsilon=1e-15):
    """Cross-entropy loss for classification"""
    # Clip predictions to prevent log(0)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    
    # Binary cross-entropy
    if len(y_pred.shape) == 1 or y_pred.shape[1] == 1:
        return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    
    # Categorical cross-entropy
    return -np.mean(np.sum(y_true * np.log(y_pred), axis=1))

# Example: Binary classification
y_true_binary = np.array([1, 0, 1, 1, 0])
y_pred_binary = np.array([0.9, 0.1, 0.8, 0.7, 0.2])

loss_binary = cross_entropy_loss(y_true_binary, y_pred_binary)
print(f"Binary cross-entropy loss: {loss_binary:.3f}")

# Example: Multi-class classification
y_true_multi = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
y_pred_multi = np.array([[0.8, 0.1, 0.1], [0.2, 0.7, 0.1], [0.1, 0.2, 0.7]])

loss_multi = cross_entropy_loss(y_true_multi, y_pred_multi)
print(f"Multi-class cross-entropy loss: {loss_multi:.3f}")
```

### 2. **Feature Selection using Mutual Information**
```python
def mutual_information_feature_selection(X, y, k=5):
    """Select top k features based on mutual information with target"""
    from sklearn.feature_selection import mutual_info_classif
    from sklearn.preprocessing import LabelEncoder
    
    # Calculate MI for each feature
    mi_scores = mutual_info_classif(X, y)
    
    # Get top k features
    top_k_indices = np.argsort(mi_scores)[-k:][::-1]
    
    print("Feature Selection using Mutual Information:")
    for i, idx in enumerate(top_k_indices):
        print(f"Feature {idx}: MI = {mi_scores[idx]:.3f}")
    
    return top_k_indices, mi_scores

# Example with synthetic data
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, 
                          n_redundant=2, random_state=42)

selected_features, mi_scores = mutual_information_feature_selection(X, y, k=5)
```

### 3. **Information-Theoretic Model Selection**
```python
def information_criteria(n_samples, n_params, log_likelihood):
    """Calculate information criteria for model selection"""
    # Akaike Information Criterion
    aic = 2 * n_params - 2 * log_likelihood
    
    # Bayesian Information Criterion
    bic = np.log(n_samples) * n_params - 2 * log_likelihood
    
    # Corrected AIC for small samples
    if n_samples / n_params < 40:
        aicc = aic + (2 * n_params * (n_params + 1)) / (n_samples - n_params - 1)
    else:
        aicc = aic
    
    return {'AIC': aic, 'BIC': bic, 'AICc': aicc}

# Example: Compare models
models = [
    {'params': 3, 'log_likelihood': -100},
    {'params': 5, 'log_likelihood': -95},
    {'params': 8, 'log_likelihood': -92}
]

n_samples = 1000
print("Model Selection using Information Criteria:")
for i, model in enumerate(models):
    criteria = information_criteria(n_samples, model['params'], model['log_likelihood'])
    print(f"Model {i+1} ({model['params']} params): AIC={criteria['AIC']:.1f}, BIC={criteria['BIC']:.1f}")
```

### 4. **Entropy-based Decision Trees**
```python
def information_gain(parent_entropy, children_entropies, children_weights):
    """Calculate information gain for decision tree split"""
    weighted_child_entropy = sum(w * h for w, h in zip(children_weights, children_entropies))
    return parent_entropy - weighted_child_entropy

def gini_impurity(probabilities):
    """Calculate Gini impurity"""
    return 1 - sum(p**2 for p in probabilities)

# Example: Decision tree split evaluation
parent_probs = [0.6, 0.4]  # Class distribution in parent node
parent_entropy = calculate_entropy(parent_probs)

# After split
left_probs = [0.8, 0.2]
right_probs = [0.3, 0.7]
left_entropy = calculate_entropy(left_probs)
right_entropy = calculate_entropy(right_probs)

# Weights (proportion of samples in each child)
left_weight = 0.6
right_weight = 0.4

ig = information_gain(parent_entropy, [left_entropy, right_entropy], 
                     [left_weight, right_weight])

print(f"Decision Tree Split Analysis:")
print(f"Parent entropy: {parent_entropy:.3f}")
print(f"Information gain: {ig:.3f}")

# Compare with Gini impurity
parent_gini = gini_impurity(parent_probs)
left_gini = gini_impurity(left_probs)
right_gini = gini_impurity(right_probs)
gini_gain = parent_gini - (left_weight * left_gini + right_weight * right_gini)

print(f"Gini impurity gain: {gini_gain:.3f}")
```

### 5. **Language Model Evaluation**
```python
def evaluate_language_model(true_sequence, model_probs):
    """Evaluate language model using perplexity"""
    # Calculate cross-entropy
    ce = 0
    for i, true_word in enumerate(true_sequence):
        if true_word in model_probs[i]:
            ce -= np.log2(model_probs[i][true_word])
        else:
            ce -= np.log2(1e-10)  # Small probability for unknown words
    
    ce /= len(true_sequence)
    perplexity = 2 ** ce
    
    return ce, perplexity

# Example: Simple language model evaluation
true_sequence = ['the', 'cat', 'sat', 'on', 'mat']
model_probs = [
    {'the': 0.3, 'a': 0.2, 'cat': 0.1, 'dog': 0.1, 'other': 0.3},
    {'cat': 0.4, 'dog': 0.3, 'bird': 0.1, 'other': 0.2},
    {'sat': 0.5, 'ran': 0.2, 'jumped': 0.1, 'other': 0.2},
    {'on': 0.6, 'under': 0.2, 'near': 0.1, 'other': 0.1},
    {'mat': 0.3, 'floor': 0.3, 'chair': 0.2, 'other': 0.2}
]

ce, perp = evaluate_language_model(true_sequence, model_probs)
print(f"Language Model Evaluation:")
print(f"Cross-entropy: {ce:.3f} bits/word")
print(f"Perplexity: {perp:.3f}")
```

---

## Practice Problems

### Problem 1: Entropy Calculation
Calculate the entropy of a fair 8-sided die.

**Solution:**
H(X) = -Σ (1/8) log₂(1/8) = -8 × (1/8) × (-3) = 3 bits

### Problem 2: Mutual Information
Given joint distribution:
```
P(X=0,Y=0) = 0.4, P(X=0,Y=1) = 0.1
P(X=1,Y=0) = 0.1, P(X=1,Y=1) = 0.4
```
Calculate I(X;Y).

**Solution:**
- H(X) = H(Y) = -0.5 log₂(0.5) - 0.5 log₂(0.5) = 1 bit
- H(X,Y) = -0.4 log₂(0.4) - 0.1 log₂(0.1) - 0.1 log₂(0.1) - 0.4 log₂(0.4) ≈ 1.522 bits
- I(X;Y) = 1 + 1 - 1.522 = 0.478 bits

### Problem 3: KL Divergence
Calculate D_KL(P||Q) where P = [0.5, 0.3, 0.2] and Q = [0.4, 0.4, 0.2].

**Solution:**
D_KL(P||Q) = 0.5 log₂(0.5/0.4) + 0.3 log₂(0.3/0.4) + 0.2 log₂(0.2/0.2)
           = 0.5 × 0.322 + 0.3 × (-0.415) + 0.2 × 0
           ≈ 0.037 bits

---

## 🎯 Key Takeaways

1. **Information is Quantifiable**: Entropy measures uncertainty and information content
2. **Mutual Information is Fundamental**: Measures dependence between variables
3. **KL Divergence Measures Difference**: Essential for comparing distributions
4. **Cross-Entropy is Everywhere**: Primary loss function in deep learning
5. **Compression and Learning are Connected**: Both involve finding efficient representations
6. **Information Theory Guides ML**: From feature selection to model evaluation

---

## 📚 Next Steps

After mastering information theory, proceed to:
1. **Advanced Probability Theory** - Deeper probabilistic modeling
2. **Coding Theory** - Error correction and channel coding
3. **Algorithmic Information Theory** - Kolmogorov complexity
4. **Quantum Information Theory** - Information in quantum systems

---

## 🔗 Resources

- **Elements of Information Theory**: Cover & Thomas (classic textbook)
- **Information Theory, Inference, and Learning**: MacKay
- **Pattern Recognition and Machine Learning**: Bishop (Chapter 1)
- **Deep Learning**: Goodfellow, Bengio & Courville (information theory sections)
- **SciPy**: Statistical and information-theoretic functions

---

*Information theory provides the mathematical foundation for understanding information, uncertainty, and learning. Master it to understand the theoretical principles underlying modern ML/AI!*