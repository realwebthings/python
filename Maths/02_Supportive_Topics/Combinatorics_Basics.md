# 🎲 Combinatorics Basics for ML/AI

## 📋 Table of Contents
- [Overview](#overview)
- [Fundamental Counting Principle](#fundamental-counting-principle)
- [Permutations](#permutations)
- [Combinations](#combinations)
- [Binomial Theorem](#binomial-theorem)
- [Inclusion-Exclusion Principle](#inclusion-exclusion-principle)
- [Generating Functions](#generating-functions)
- [Pigeonhole Principle](#pigeonhole-principle)
- [Applications in ML/AI](#applications-in-mlai)
- [Practice Problems](#practice-problems)
- [Python Implementation](#python-implementation)

---

## Overview

Combinatorics is the **mathematics of counting** and arrangement, fundamental to probability and discrete mathematics in ML/AI:

### 🎯 **Critical Applications:**
- **Probability Calculations**: Computing probabilities of complex events
- **Feature Selection**: Choosing subsets of features from large sets
- **Hyperparameter Tuning**: Counting possible configurations
- **Graph Theory**: Counting paths, cycles, and structures
- **Cryptography**: Key space analysis and security
- **Algorithm Analysis**: Counting operations and complexity
- **Sampling Methods**: Understanding sample spaces

---

## Fundamental Counting Principle

### Multiplication Principle
If there are m ways to do one thing and n ways to do another, then there are m × n ways to do both.

**Example**: Password Creation
- 26 letters for first character
- 10 digits for second character
- 26 letters for third character
- Total passwords: 26 × 10 × 26 = 6,760

```python
def counting_principle_example():
    """Demonstrate fundamental counting principle"""
    # Password with: 1 letter, 1 digit, 1 letter
    letters = 26
    digits = 10
    
    total_passwords = letters * digits * letters
    print(f"Password combinations (Letter-Digit-Letter): {total_passwords:,}")
    
    # More complex example: License plates (3 letters, 3 digits)
    license_plates = (26**3) * (10**3)
    print(f"License plate combinations (LLL-DDD): {license_plates:,}")
    
    return total_passwords, license_plates

counting_principle_example()
```

### Addition Principle
If there are m ways to do one thing OR n ways to do another (mutually exclusive), then there are m + n ways total.

**Example**: Transportation Options
- 5 bus routes OR 3 train routes = 5 + 3 = 8 total options

```python
def addition_principle_example():
    """Demonstrate addition principle"""
    # Transportation: bus OR train OR car
    bus_routes = 5
    train_routes = 3
    car_options = 2
    
    total_options = bus_routes + train_routes + car_options
    print(f"Transportation options: {total_options}")
    
    return total_options

addition_principle_example()
```

---

## Permutations

### Definition
A **permutation** is an arrangement of objects where **order matters**.

### Permutations of n Distinct Objects
P(n) = n! = n × (n-1) × (n-2) × ... × 2 × 1

**Example**: Arranging 5 books on a shelf
P(5) = 5! = 5 × 4 × 3 × 2 × 1 = 120 ways

```python
import math

def factorial(n):
    """Calculate factorial"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def permutations_n_objects(n):
    """Calculate permutations of n distinct objects"""
    result = math.factorial(n)
    print(f"Permutations of {n} objects: {result:,}")
    return result

# Example: Arranging 5 books
permutations_n_objects(5)
```

### Permutations of n Objects Taken r at a Time
P(n, r) = n! / (n-r)! = n × (n-1) × ... × (n-r+1)

**Example**: Selecting and arranging 3 people from 10 for president, vice-president, secretary
P(10, 3) = 10! / 7! = 10 × 9 × 8 = 720

```python
def permutations_n_r(n, r):
    """Calculate permutations of n objects taken r at a time"""
    if r > n:
        return 0
    
    result = math.factorial(n) // math.factorial(n - r)
    print(f"P({n}, {r}) = {result:,}")
    return result

# Example: Selecting 3 officers from 10 people
permutations_n_r(10, 3)
```

### Permutations with Repetition
When some objects are identical: n! / (n₁! × n₂! × ... × nₖ!)

**Example**: Arranging letters in "MISSISSIPPI"
- Total letters: 11
- M: 1, I: 4, S: 4, P: 2
- Arrangements: 11! / (1! × 4! × 4! × 2!) = 34,650

```python
def permutations_with_repetition(total, repetitions):
    """Calculate permutations with repeated objects"""
    numerator = math.factorial(total)
    denominator = 1
    
    for count in repetitions:
        denominator *= math.factorial(count)
    
    result = numerator // denominator
    print(f"Permutations with repetition: {result:,}")
    return result

# Example: MISSISSIPPI
# M:1, I:4, S:4, P:2
permutations_with_repetition(11, [1, 4, 4, 2])
```

### Circular Permutations
Arranging n objects in a circle: (n-1)!

**Example**: Seating 6 people around a circular table
Circular arrangements: (6-1)! = 5! = 120

```python
def circular_permutations(n):
    """Calculate circular permutations"""
    result = math.factorial(n - 1)
    print(f"Circular permutations of {n} objects: {result:,}")
    return result

# Example: 6 people around table
circular_permutations(6)
```

---

## Combinations

### Definition
A **combination** is a selection of objects where **order doesn't matter**.

### Combinations of n Objects Taken r at a Time
C(n, r) = n! / (r! × (n-r)!) = "n choose r"

**Example**: Selecting 3 people from 10 for a committee
C(10, 3) = 10! / (3! × 7!) = (10 × 9 × 8) / (3 × 2 × 1) = 120

```python
def combinations_n_r(n, r):
    """Calculate combinations of n objects taken r at a time"""
    if r > n or r < 0:
        return 0
    
    # Use the more efficient formula
    result = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    print(f"C({n}, {r}) = {result:,}")
    return result

# Alternative efficient implementation
def combinations_efficient(n, r):
    """More efficient combination calculation"""
    if r > n - r:  # Take advantage of symmetry
        r = n - r
    
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    
    return result

# Example: Committee selection
combinations_n_r(10, 3)
```

### Properties of Combinations
1. **Symmetry**: C(n, r) = C(n, n-r)
2. **Pascal's Identity**: C(n, r) = C(n-1, r-1) + C(n-1, r)
3. **Sum Property**: Σ C(n, r) for r=0 to n = 2ⁿ

```python
def demonstrate_combination_properties():
    """Demonstrate properties of combinations"""
    n, r = 10, 3
    
    # Symmetry property
    c1 = combinations_n_r(n, r)
    c2 = combinations_n_r(n, n - r)
    print(f"Symmetry: C({n}, {r}) = C({n}, {n-r}) = {c1} = {c2}")
    
    # Pascal's identity
    left = combinations_n_r(n, r)
    right = combinations_n_r(n-1, r-1) + combinations_n_r(n-1, r)
    print(f"Pascal's Identity: C({n}, {r}) = C({n-1}, {r-1}) + C({n-1}, {r})")
    print(f"{left} = {combinations_n_r(n-1, r-1)} + {combinations_n_r(n-1, r)} = {right}")
    
    # Sum property
    total_sum = sum(combinations_n_r(5, r) for r in range(6))
    expected = 2**5
    print(f"Sum property: Σ C(5, r) = {total_sum} = 2^5 = {expected}")

demonstrate_combination_properties()
```

### Combinations with Repetition
Selecting r objects from n types with repetition allowed: C(n+r-1, r)

**Example**: Selecting 4 fruits from {apple, banana, orange} with repetition
C(3+4-1, 4) = C(6, 4) = 15

```python
def combinations_with_repetition(n, r):
    """Calculate combinations with repetition allowed"""
    result = combinations_n_r(n + r - 1, r)
    print(f"Combinations with repetition C({n}+{r}-1, {r}) = {result}")
    return result

# Example: 4 fruits from 3 types
combinations_with_repetition(3, 4)
```

---

## Binomial Theorem

### Statement
(x + y)ⁿ = Σ C(n, k) × xⁿ⁻ᵏ × yᵏ for k=0 to n

### Binomial Coefficients
The coefficients C(n, k) form Pascal's Triangle:
```
Row 0:           1
Row 1:         1   1
Row 2:       1   2   1
Row 3:     1   3   3   1
Row 4:   1   4   6   4   1
```

```python
def generate_pascals_triangle(n_rows):
    """Generate Pascal's triangle"""
    triangle = []
    
    for n in range(n_rows):
        row = []
        for k in range(n + 1):
            row.append(combinations_n_r(n, k))
        triangle.append(row)
    
    return triangle

def print_pascals_triangle(triangle):
    """Print Pascal's triangle in formatted way"""
    max_width = len(str(max(triangle[-1])))
    
    for i, row in enumerate(triangle):
        # Center the row
        spaces = " " * (max_width * (len(triangle) - i - 1) // 2)
        row_str = spaces + " ".join(f"{num:>{max_width}}" for num in row)
        print(row_str)

# Generate and print Pascal's triangle
triangle = generate_pascals_triangle(6)
print("Pascal's Triangle:")
print_pascals_triangle(triangle)
```

### Applications of Binomial Theorem

#### **Probability Distributions**
Binomial probability: P(X = k) = C(n, k) × pᵏ × (1-p)ⁿ⁻ᵏ

```python
def binomial_probability(n, k, p):
    """Calculate binomial probability"""
    coeff = combinations_n_r(n, k)
    prob = coeff * (p**k) * ((1-p)**(n-k))
    print(f"P(X = {k}) = C({n}, {k}) × {p}^{k} × {1-p}^{n-k} = {prob:.4f}")
    return prob

# Example: Probability of exactly 3 heads in 5 coin flips
binomial_probability(5, 3, 0.5)
```

#### **Expansion Calculations**
```python
def binomial_expansion(x, y, n):
    """Calculate binomial expansion (x + y)^n"""
    terms = []
    
    for k in range(n + 1):
        coeff = combinations_n_r(n, k)
        x_power = n - k
        y_power = k
        
        term_value = coeff * (x**x_power) * (y**y_power)
        terms.append(term_value)
        
        print(f"Term {k}: C({n}, {k}) × {x}^{x_power} × {y}^{y_power} = {term_value}")
    
    total = sum(terms)
    print(f"Total: ({x} + {y})^{n} = {total}")
    return terms, total

# Example: (2 + 3)^4
binomial_expansion(2, 3, 4)
```

---

## Inclusion-Exclusion Principle

### Two Sets
|A ∪ B| = |A| + |B| - |A ∩ B|

### Three Sets
|A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C|

### General Form
For sets A₁, A₂, ..., Aₙ:
|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| - Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| - ... + (-1)ⁿ⁺¹|A₁ ∩ A₂ ∩ ... ∩ Aₙ|

```python
def inclusion_exclusion_example():
    """Demonstrate inclusion-exclusion principle"""
    # Example: Students taking Math, Physics, Chemistry
    # Math: 60, Physics: 50, Chemistry: 40
    # Math ∩ Physics: 30, Math ∩ Chemistry: 25, Physics ∩ Chemistry: 20
    # All three: 15
    
    math = 60
    physics = 50
    chemistry = 40
    
    math_physics = 30
    math_chemistry = 25
    physics_chemistry = 20
    
    all_three = 15
    
    # Apply inclusion-exclusion
    total_students = (math + physics + chemistry 
                     - math_physics - math_chemistry - physics_chemistry 
                     + all_three)
    
    print("Inclusion-Exclusion Example:")
    print(f"Students taking at least one subject: {total_students}")
    
    # Verify with individual calculations
    only_math = math - math_physics - math_chemistry + all_three
    only_physics = physics - math_physics - physics_chemistry + all_three
    only_chemistry = chemistry - math_chemistry - physics_chemistry + all_three
    only_math_physics = math_physics - all_three
    only_math_chemistry = math_chemistry - all_three
    only_physics_chemistry = physics_chemistry - all_three
    
    verification = (only_math + only_physics + only_chemistry + 
                   only_math_physics + only_math_chemistry + only_physics_chemistry + 
                   all_three)
    
    print(f"Verification: {verification}")
    
    return total_students

inclusion_exclusion_example()
```

---

## Generating Functions

### Definition
A generating function for sequence a₀, a₁, a₂, ... is:
G(x) = a₀ + a₁x + a₂x² + a₃x³ + ...

### Applications
- Solving recurrence relations
- Counting problems
- Probability generating functions

```python
def fibonacci_generating_function(n_terms):
    """Demonstrate Fibonacci generating function"""
    # Fibonacci: F(x) = x / (1 - x - x²)
    # Coefficients give Fibonacci numbers
    
    fib = [0, 1]
    for i in range(2, n_terms):
        fib.append(fib[i-1] + fib[i-2])
    
    print("Fibonacci sequence:", fib[:10])
    
    # Generate using generating function approach
    # (This is a simplified demonstration)
    return fib

fibonacci_generating_function(15)
```

---

## Pigeonhole Principle

### Statement
If n pigeons are placed in m pigeonholes and n > m, then at least one pigeonhole contains more than one pigeon.

### Generalized Form
If n objects are placed in m boxes, then at least one box contains ⌈n/m⌉ objects.

```python
def pigeonhole_examples():
    """Demonstrate pigeonhole principle applications"""
    
    print("Pigeonhole Principle Examples:")
    
    # Example 1: Birthday paradox
    print("\n1. Birthday Paradox:")
    people = 23
    days = 365
    print(f"With {people} people and {days} possible birthdays,")
    print(f"probability of shared birthday > 50%")
    
    # Example 2: Sock drawer
    print("\n2. Sock Drawer:")
    sock_colors = 4  # black, white, brown, blue
    socks_drawn = 5
    print(f"Drawing {socks_drawn} socks from {sock_colors} colors")
    print(f"Guaranteed to have at least {math.ceil(socks_drawn/sock_colors)} matching socks")
    
    # Example 3: Hash collisions
    print("\n3. Hash Collisions:")
    hash_buckets = 1000
    items = 1001
    print(f"Hashing {items} items into {hash_buckets} buckets")
    print(f"At least one bucket will have ≥{math.ceil(items/hash_buckets)} items")

pigeonhole_examples()
```

---

## Applications in ML/AI

### 1. **Feature Selection Combinations**
```python
def feature_selection_combinations(n_features, max_features):
    """Calculate number of possible feature combinations"""
    total_combinations = 0
    
    print(f"Feature Selection from {n_features} features:")
    for r in range(1, min(max_features + 1, n_features + 1)):
        combinations = combinations_n_r(n_features, r)
        total_combinations += combinations
        print(f"Selecting {r} features: {combinations:,} combinations")
    
    print(f"Total combinations (1 to {max_features}): {total_combinations:,}")
    return total_combinations

# Example: Selecting up to 5 features from 20
feature_selection_combinations(20, 5)
```

### 2. **Hyperparameter Grid Search**
```python
def hyperparameter_combinations():
    """Calculate hyperparameter search space"""
    # Example: Neural network hyperparameters
    learning_rates = [0.001, 0.01, 0.1]  # 3 options
    batch_sizes = [16, 32, 64, 128]      # 4 options
    hidden_layers = [1, 2, 3]            # 3 options
    neurons_per_layer = [50, 100, 200]   # 3 options
    
    total_combinations = len(learning_rates) * len(batch_sizes) * len(hidden_layers) * len(neurons_per_layer)
    
    print("Hyperparameter Search Space:")
    print(f"Learning rates: {len(learning_rates)} options")
    print(f"Batch sizes: {len(batch_sizes)} options")
    print(f"Hidden layers: {len(hidden_layers)} options")
    print(f"Neurons per layer: {len(neurons_per_layer)} options")
    print(f"Total combinations: {total_combinations:,}")
    
    return total_combinations

hyperparameter_combinations()
```

### 3. **Sampling Without Replacement**
```python
def sampling_combinations(population_size, sample_size):
    """Calculate number of possible samples"""
    possible_samples = combinations_n_r(population_size, sample_size)
    
    print(f"Sampling {sample_size} items from population of {population_size}:")
    print(f"Possible unique samples: {possible_samples:,}")
    
    # If we want to ensure we see each possible sample at least once
    min_experiments = possible_samples
    print(f"Minimum experiments to guarantee seeing each sample: {min_experiments:,}")
    
    return possible_samples

# Example: Cross-validation splits
sampling_combinations(1000, 100)  # 100 samples from 1000 data points
```

### 4. **Probability Calculations in ML**
```python
def ml_probability_examples():
    """Combinatorics in ML probability calculations"""
    
    # Example 1: Bagging - probability of sample inclusion
    n_samples = 1000
    bootstrap_size = 1000
    
    # Probability that a specific sample is NOT selected in one draw
    prob_not_selected_once = (n_samples - 1) / n_samples
    
    # Probability that it's never selected in bootstrap_size draws
    prob_never_selected = prob_not_selected_once ** bootstrap_size
    
    # Probability that it's selected at least once
    prob_selected = 1 - prob_never_selected
    
    print("Bagging/Bootstrap Sampling:")
    print(f"Probability sample is included: {prob_selected:.3f}")
    print(f"Expected samples in bootstrap: {n_samples * prob_selected:.0f}")
    
    # Example 2: Random Forest - feature selection
    total_features = 100
    features_per_tree = int(np.sqrt(total_features))  # Common heuristic
    
    possible_feature_combinations = combinations_n_r(total_features, features_per_tree)
    print(f"\nRandom Forest Feature Selection:")
    print(f"Possible feature combinations per tree: {possible_feature_combinations:,}")

ml_probability_examples()
```

### 5. **Combinatorial Optimization**
```python
def combinatorial_optimization_example():
    """Example of combinatorial optimization in ML"""
    
    # Traveling Salesman Problem (TSP) - related to neural network optimization
    n_cities = 10
    
    # Number of possible tours (circular permutations)
    possible_tours = math.factorial(n_cities - 1) // 2  # Divide by 2 for symmetry
    
    print("Combinatorial Optimization Example:")
    print(f"TSP with {n_cities} cities:")
    print(f"Possible tours: {possible_tours:,}")
    
    # This grows very quickly - demonstrates need for heuristics
    for cities in range(5, 16):
        tours = math.factorial(cities - 1) // 2
        print(f"{cities} cities: {tours:,} tours")
    
    return possible_tours

combinatorial_optimization_example()
```

---

## Practice Problems

### Problem 1: Committee Selection
From 12 people, how many ways can we select a committee of 5?

**Solution:**
C(12, 5) = 12! / (5! × 7!) = 792

### Problem 2: Password Strength
How many 8-character passwords are possible using:
a) Only lowercase letters
b) Lowercase + uppercase + digits

**Solutions:**
a) 26⁸ = 208,827,064,576
b) (26 + 26 + 10)⁸ = 62⁸ = 218,340,105,584,896

### Problem 3: Probability with Combinations
In a deck of 52 cards, what's the probability of getting exactly 2 aces in a 5-card hand?

**Solution:**
- Ways to choose 2 aces from 4: C(4, 2) = 6
- Ways to choose 3 non-aces from 48: C(48, 3) = 17,296
- Total favorable outcomes: 6 × 17,296 = 103,776
- Total possible hands: C(52, 5) = 2,598,960
- Probability: 103,776 / 2,598,960 ≈ 0.0399

### Problem 4: Inclusion-Exclusion
In a class of 100 students: 60 like math, 50 like science, 40 like both. How many like at least one subject?

**Solution:**
|M ∪ S| = |M| + |S| - |M ∩ S| = 60 + 50 - 40 = 70 students

---

## Python Implementation

```python
import math
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations, permutations, combinations_with_replacement

class CombinatoricsCalculator:
    """Comprehensive combinatorics calculator"""
    
    @staticmethod
    def factorial(n):
        """Calculate factorial with memoization"""
        if not hasattr(CombinatoricsCalculator, '_factorial_cache'):
            CombinatoricsCalculator._factorial_cache = {0: 1, 1: 1}
        
        if n in CombinatoricsCalculator._factorial_cache:
            return CombinatoricsCalculator._factorial_cache[n]
        
        result = n * CombinatoricsCalculator.factorial(n - 1)
        CombinatoricsCalculator._factorial_cache[n] = result
        return result
    
    @staticmethod
    def permutations(n, r=None):
        """Calculate P(n, r) = n! / (n-r)!"""
        if r is None:
            r = n
        if r > n or r < 0:
            return 0
        return CombinatoricsCalculator.factorial(n) // CombinatoricsCalculator.factorial(n - r)
    
    @staticmethod
    def combinations(n, r):
        """Calculate C(n, r) = n! / (r! * (n-r)!)"""
        if r > n or r < 0:
            return 0
        if r > n - r:  # Take advantage of symmetry
            r = n - r
        
        result = 1
        for i in range(r):
            result = result * (n - i) // (i + 1)
        return result
    
    @staticmethod
    def combinations_with_repetition(n, r):
        """Calculate combinations with repetition: C(n+r-1, r)"""
        return CombinatoricsCalculator.combinations(n + r - 1, r)
    
    @staticmethod
    def derangements(n):
        """Calculate number of derangements (permutations with no fixed points)"""
        if n == 0:
            return 1
        if n == 1:
            return 0
        
        result = 0
        for i in range(n + 1):
            result += ((-1) ** i) * CombinatoricsCalculator.factorial(n) // CombinatoricsCalculator.factorial(i)
        
        return result

def demonstrate_all_concepts():
    """Comprehensive demonstration of combinatorics concepts"""
    calc = CombinatoricsCalculator()
    
    print("=== COMBINATORICS COMPREHENSIVE DEMO ===\n")
    
    # 1. Basic counting
    print("1. BASIC COUNTING:")
    print(f"5! = {calc.factorial(5)}")
    print(f"P(10, 3) = {calc.permutations(10, 3)}")
    print(f"C(10, 3) = {calc.combinations(10, 3)}")
    
    # 2. Real-world examples
    print("\n2. REAL-WORLD EXAMPLES:")
    
    # Lottery
    lottery_combinations = calc.combinations(49, 6)
    print(f"Lottery (6 from 49): {lottery_combinations:,} combinations")
    print(f"Probability of winning: 1 in {lottery_combinations:,}")
    
    # DNA sequences
    dna_length = 10
    dna_sequences = 4 ** dna_length  # 4 bases: A, T, G, C
    print(f"DNA sequences of length {dna_length}: {dna_sequences:,}")
    
    # 3. Pascal's triangle
    print("\n3. PASCAL'S TRIANGLE:")
    for n in range(6):
        row = [calc.combinations(n, k) for k in range(n + 1)]
        spaces = " " * (5 - n)
        print(f"{spaces}{' '.join(f'{x:2d}' for x in row)}")
    
    # 4. Binomial probabilities
    print("\n4. BINOMIAL PROBABILITIES:")
    n_trials = 10
    p_success = 0.3
    
    print(f"Binomial distribution: n={n_trials}, p={p_success}")
    for k in range(n_trials + 1):
        prob = calc.combinations(n_trials, k) * (p_success ** k) * ((1 - p_success) ** (n_trials - k))
        print(f"P(X = {k:2d}) = {prob:.4f}")
    
    # 5. Derangements
    print("\n5. DERANGEMENTS:")
    for n in range(1, 8):
        derang = calc.derangements(n)
        total_perm = calc.factorial(n)
        prob = derang / total_perm if total_perm > 0 else 0
        print(f"D({n}) = {derang:4d}, P(derangement) = {prob:.4f}")

def visualize_combinatorics():
    """Create visualizations for combinatorics concepts"""
    
    # 1. Growth comparison
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    n_values = range(1, 11)
    
    # Factorial growth
    factorials = [math.factorial(n) for n in n_values]
    axes[0, 0].plot(n_values, factorials, 'bo-', linewidth=2)
    axes[0, 0].set_yscale('log')
    axes[0, 0].set_title('Factorial Growth: n!')
    axes[0, 0].set_xlabel('n')
    axes[0, 0].set_ylabel('n! (log scale)')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Combinations C(n, k) for fixed k
    k_fixed = 3
    combinations_fixed_k = [CombinatoricsCalculator.combinations(n, k_fixed) for n in range(k_fixed, 15)]
    axes[0, 1].plot(range(k_fixed, 15), combinations_fixed_k, 'ro-', linewidth=2)
    axes[0, 1].set_title(f'Combinations: C(n, {k_fixed})')
    axes[0, 1].set_xlabel('n')
    axes[0, 1].set_ylabel(f'C(n, {k_fixed})')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Pascal's triangle heatmap
    size = 10
    pascal_matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(i + 1):
            pascal_matrix[i, j] = CombinatoricsCalculator.combinations(i, j)
    
    im = axes[1, 0].imshow(pascal_matrix, cmap='Blues', aspect='equal')
    axes[1, 0].set_title("Pascal's Triangle (Heatmap)")
    axes[1, 0].set_xlabel('k')
    axes[1, 0].set_ylabel('n')
    plt.colorbar(im, ax=axes[1, 0])
    
    # Binomial distribution
    n_trials = 20
    p_success = 0.3
    k_values = range(n_trials + 1)
    probabilities = [CombinatoricsCalculator.combinations(n_trials, k) * 
                    (p_success ** k) * ((1 - p_success) ** (n_trials - k))
                    for k in k_values]
    
    axes[1, 1].bar(k_values, probabilities, alpha=0.7, color='green')
    axes[1, 1].set_title(f'Binomial Distribution: n={n_trials}, p={p_success}')
    axes[1, 1].set_xlabel('k (number of successes)')
    axes[1, 1].set_ylabel('P(X = k)')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def ml_applications_comprehensive():
    """Comprehensive ML applications of combinatorics"""
    
    print("=== ML/AI APPLICATIONS OF COMBINATORICS ===\n")
    
    # 1. Feature selection complexity
    print("1. FEATURE SELECTION COMPLEXITY:")
    features = [10, 20, 50, 100]
    for n_feat in features:
        total_subsets = 2**n_feat - 1  # Exclude empty set
        print(f"{n_feat} features: {total_subsets:,} possible subsets")
        
        # Practical limit (e.g., up to 5 features)
        practical_limit = min(5, n_feat)
        practical_combinations = sum(CombinatoricsCalculator.combinations(n_feat, r) 
                                   for r in range(1, practical_limit + 1))
        print(f"  Practical (≤{practical_limit}): {practical_combinations:,} combinations")
    
    # 2. Cross-validation combinations
    print("\n2. CROSS-VALIDATION:")
    n_samples = 1000
    k_folds = [5, 10, 20]
    
    for k in k_folds:
        fold_size = n_samples // k
        ways_to_choose_test = CombinatoricsCalculator.combinations(n_samples, fold_size)
        print(f"{k}-fold CV: {ways_to_choose_test:,} ways to choose test set")
    
    # 3. Ensemble methods
    print("\n3. ENSEMBLE METHODS:")
    n_models = 100
    ensemble_sizes = [3, 5, 10, 20]
    
    for size in ensemble_sizes:
        combinations = CombinatoricsCalculator.combinations(n_models, size)
        print(f"Ensemble of {size} from {n_models} models: {combinations:,} combinations")
    
    # 4. Hyperparameter optimization
    print("\n4. HYPERPARAMETER OPTIMIZATION:")
    
    # Grid search
    param_options = [3, 4, 5, 2, 6]  # Options for each parameter
    grid_size = np.prod(param_options)
    print(f"Grid search space: {grid_size:,} combinations")
    
    # Random search efficiency
    total_combinations = grid_size
    random_samples = 100
    coverage_prob = 1 - ((total_combinations - 1) / total_combinations) ** random_samples
    print(f"Random search ({random_samples} samples): {coverage_prob:.1%} coverage probability")

if __name__ == "__main__":
    # Run comprehensive demonstration
    demonstrate_all_concepts()
    
    # Create visualizations
    print("\n" + "="*50)
    print("Creating visualizations...")
    visualize_combinatorics()
    
    # ML applications
    print("\n" + "="*50)
    ml_applications_comprehensive()
```

---

## 🎯 Key Takeaways

1. **Counting is Fundamental**: Every probability calculation involves combinatorics
2. **Order Matters**: Distinguish between permutations (order matters) and combinations (order doesn't)
3. **Efficiency is Key**: Use symmetry and efficient algorithms for large calculations
4. **Real-World Applications**: Combinatorics appears everywhere in ML/AI
5. **Exponential Growth**: Many combinatorial problems grow exponentially
6. **Approximations Help**: For large problems, use approximations and heuristics

---

## 📚 Next Steps

After mastering combinatorics basics, proceed to:
1. **Advanced Probability** - Using combinatorics for complex probability calculations
2. **Graph Theory** - Counting paths, cycles, and graph structures
3. **Algorithm Analysis** - Complexity analysis using combinatorial methods
4. **Discrete Optimization** - Combinatorial optimization problems

---

## 🔗 Resources

- **Concrete Mathematics**: Graham, Knuth, and Patashnik
- **Introduction to Algorithms**: CLRS (combinatorial algorithms)
- **A Walk Through Combinatorics**: Bona
- **Python itertools**: Built-in combinatorial functions
- **SciPy special functions**: Advanced combinatorial calculations

---

*Combinatorics provides the counting tools essential for probability, algorithm analysis, and optimization in ML/AI. Master it to understand the mathematical foundations of computational complexity!*