# 🔗 Set Theory Basics for ML/AI

## 📋 Table of Contents
- [Overview](#overview)
- [Basic Set Concepts](#basic-set-concepts)
- [Set Operations](#set-operations)
- [Relations](#relations)
- [Functions](#functions)
- [Mappings and Transformations](#mappings-and-transformations)
- [Cardinality and Infinity](#cardinality-and-infinity)
- [Applications in ML/AI](#applications-in-mlai)
- [Practice Problems](#practice-problems)
- [Python Implementation](#python-implementation)

---

## Overview

Set theory provides the **logical foundation** for mathematics and computer science. In ML/AI, set theory is essential for:

### 🎯 **Critical Applications:**
- **Data Representation**: Datasets as sets of samples
- **Feature Spaces**: Input and output domains
- **Probability Theory**: Sample spaces and events
- **Logic and Reasoning**: Boolean operations in AI
- **Database Operations**: Joins, unions, intersections
- **Graph Theory**: Vertices and edges as sets
- **Classification**: Decision boundaries and regions

---

## Basic Set Concepts

### Definition
A **set** is a well-defined collection of distinct objects called **elements** or **members**.

**Notation**: 
- Set: A = {1, 2, 3, 4, 5}
- Element membership: 3 ∈ A (3 is in A)
- Non-membership: 6 ∉ A (6 is not in A)

### Ways to Define Sets

#### 1. **Roster Method** (List all elements)
```
A = {1, 2, 3, 4, 5}
B = {red, blue, green}
C = {apple, banana, orange}
```

#### 2. **Set-Builder Notation** (Describe properties)
```
A = {x | x is a positive integer less than 6}
B = {x | x² < 10}
C = {(x, y) | x + y = 5}
```

#### 3. **Interval Notation** (For continuous sets)
```
[a, b] = {x | a ≤ x ≤ b}    (closed interval)
(a, b) = {x | a < x < b}     (open interval)
[a, b) = {x | a ≤ x < b}     (half-open interval)
```

### Special Sets

#### **Empty Set (∅)**
The set with no elements: ∅ = { }

**Example**: Set of real numbers x where x² = -1
```python
# In Python
empty_set = set()
print(f"Empty set: {empty_set}")
print(f"Size: {len(empty_set)}")
```

#### **Universal Set (U)**
The set containing all elements under consideration.

**Example**: In studying integers, U might be all integers ℤ

#### **Subset (⊆)**
A ⊆ B means every element of A is also in B.

**Example**: 
- A = {1, 2} and B = {1, 2, 3, 4}
- Then A ⊆ B (A is a subset of B)

```python
A = {1, 2}
B = {1, 2, 3, 4}
print(f"A ⊆ B: {A.issubset(B)}")  # True
```

#### **Proper Subset (⊂)**
A ⊂ B means A ⊆ B and A ≠ B.

#### **Power Set (P(A))**
The set of all subsets of A.

**Example**: If A = {1, 2}, then P(A) = {∅, {1}, {2}, {1, 2}}

```python
def power_set(s):
    """Generate power set of a set"""
    from itertools import combinations
    result = []
    for i in range(len(s) + 1):
        for combo in combinations(s, i):
            result.append(set(combo))
    return result

A = {1, 2}
P_A = power_set(A)
print(f"Power set of {A}: {P_A}")
```

---

## Set Operations

### Union (∪)
A ∪ B = {x | x ∈ A or x ∈ B}

**Example**: 
- A = {1, 2, 3}, B = {3, 4, 5}
- A ∪ B = {1, 2, 3, 4, 5}

**Venn Diagram**: The entire shaded region covering both circles.

```python
A = {1, 2, 3}
B = {3, 4, 5}
union = A.union(B)  # or A | B
print(f"A ∪ B = {union}")
```

### Intersection (∩)
A ∩ B = {x | x ∈ A and x ∈ B}

**Example**: 
- A = {1, 2, 3}, B = {3, 4, 5}
- A ∩ B = {3}

**Venn Diagram**: The overlapping region of both circles.

```python
intersection = A.intersection(B)  # or A & B
print(f"A ∩ B = {intersection}")
```

### Difference (−)
A − B = {x | x ∈ A and x ∉ B}

**Example**: 
- A = {1, 2, 3}, B = {3, 4, 5}
- A − B = {1, 2}

```python
difference = A.difference(B)  # or A - B
print(f"A − B = {difference}")
```

### Symmetric Difference (△)
A △ B = (A − B) ∪ (B − A) = (A ∪ B) − (A ∩ B)

**Example**: 
- A = {1, 2, 3}, B = {3, 4, 5}
- A △ B = {1, 2, 4, 5}

```python
sym_diff = A.symmetric_difference(B)  # or A ^ B
print(f"A △ B = {sym_diff}")
```

### Complement (Aᶜ)
Aᶜ = U − A (elements in universal set but not in A)

**Example**: If U = {1, 2, 3, 4, 5} and A = {1, 3, 5}, then Aᶜ = {2, 4}

### Properties of Set Operations

#### **Commutative Laws**
- A ∪ B = B ∪ A
- A ∩ B = B ∩ A

#### **Associative Laws**
- (A ∪ B) ∪ C = A ∪ (B ∪ C)
- (A ∩ B) ∩ C = A ∩ (B ∩ C)

#### **Distributive Laws**
- A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
- A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)

#### **De Morgan's Laws**
- (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
- (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ

---

## Relations

### Definition
A **relation** R from set A to set B is a subset of the Cartesian product A × B.

**Notation**: If (a, b) ∈ R, we write aRb or R(a, b).

### Cartesian Product
A × B = {(a, b) | a ∈ A and b ∈ B}

**Example**: 
- A = {1, 2}, B = {x, y}
- A × B = {(1, x), (1, y), (2, x), (2, y)}

```python
import itertools

A = {1, 2}
B = {'x', 'y'}
cartesian_product = set(itertools.product(A, B))
print(f"A × B = {cartesian_product}")
```

### Types of Relations

#### **Reflexive**
For all a ∈ A, aRa.

**Example**: "≤" on real numbers (every number is ≤ itself)

#### **Symmetric**
If aRb, then bRa.

**Example**: "=" on real numbers (if a = b, then b = a)

#### **Transitive**
If aRb and bRc, then aRc.

**Example**: "<" on real numbers (if a < b and b < c, then a < c)

#### **Equivalence Relation**
A relation that is reflexive, symmetric, and transitive.

**Example**: "=" (equality) is an equivalence relation.

### Equivalence Classes
If R is an equivalence relation on A, the equivalence class of a ∈ A is:
[a] = {x ∈ A | xRa}

**Example**: Consider integers modulo 3
- [0] = {..., -6, -3, 0, 3, 6, ...}
- [1] = {..., -5, -2, 1, 4, 7, ...}
- [2] = {..., -4, -1, 2, 5, 8, ...}

---

## Functions

### Definition
A **function** f: A → B is a relation where each element in A is related to exactly one element in B.

**Notation**: f(a) = b means f maps a to b.

### Domain, Codomain, and Range
- **Domain**: Set A (input set)
- **Codomain**: Set B (target set)
- **Range**: {f(a) | a ∈ A} ⊆ B (actual outputs)

**Example**: f: ℝ → ℝ defined by f(x) = x²
- Domain: ℝ (all real numbers)
- Codomain: ℝ
- Range: [0, ∞) (non-negative real numbers)

### Types of Functions

#### **Injective (One-to-One)**
If f(a₁) = f(a₂), then a₁ = a₂.

**Example**: f(x) = 2x is injective.

```python
def is_injective(func, domain):
    """Check if function is injective on given domain"""
    outputs = [func(x) for x in domain]
    return len(outputs) == len(set(outputs))

f = lambda x: 2 * x
domain = range(-10, 11)
print(f"f(x) = 2x is injective: {is_injective(f, domain)}")
```

#### **Surjective (Onto)**
For every b ∈ B, there exists a ∈ A such that f(a) = b.

**Example**: f: ℝ → ℝ defined by f(x) = x³ is surjective.

#### **Bijective (One-to-One and Onto)**
A function that is both injective and surjective.

**Example**: f: ℝ → ℝ defined by f(x) = 2x + 1 is bijective.

### Function Composition
If f: A → B and g: B → C, then (g ∘ f): A → C is defined by:
(g ∘ f)(a) = g(f(a))

**Example**: 
- f(x) = x + 1
- g(x) = 2x
- (g ∘ f)(x) = g(f(x)) = g(x + 1) = 2(x + 1) = 2x + 2

```python
def compose(g, f):
    """Function composition: (g ∘ f)(x) = g(f(x))"""
    return lambda x: g(f(x))

f = lambda x: x + 1
g = lambda x: 2 * x
g_compose_f = compose(g, f)

x = 5
print(f"f({x}) = {f(x)}")
print(f"g({x}) = {g(x)}")
print(f"(g ∘ f)({x}) = {g_compose_f(x)}")
```

### Inverse Functions
If f: A → B is bijective, then f⁻¹: B → A exists such that:
- f⁻¹(f(a)) = a for all a ∈ A
- f(f⁻¹(b)) = b for all b ∈ B

**Example**: If f(x) = 2x + 1, then f⁻¹(x) = (x - 1)/2

---

## Mappings and Transformations

### Linear Transformations
A function T: V → W between vector spaces that preserves vector operations:
- T(u + v) = T(u) + T(v)
- T(cu) = cT(u)

**Example**: T(x, y) = (2x + y, x - y) is a linear transformation.

```python
import numpy as np

def linear_transform(matrix, vector):
    """Apply linear transformation represented by matrix"""
    return matrix @ vector

# Transformation matrix
T = np.array([[2, 1], [1, -1]])
v = np.array([3, 2])

result = linear_transform(T, v)
print(f"T({v}) = {result}")
```

### Affine Transformations
T(x) = Ax + b where A is a matrix and b is a vector.

**Example**: Translation, rotation, scaling in computer graphics.

### Homeomorphisms
Continuous bijective functions with continuous inverses.

**Example**: f: (0, 1) → ℝ defined by f(x) = tan(π(x - 1/2))

---

## Cardinality and Infinity

### Finite Sets
|A| = n for some non-negative integer n.

**Example**: A = {1, 2, 3} has |A| = 3.

### Countably Infinite Sets
Sets that can be put in one-to-one correspondence with ℕ.

**Examples**: 
- ℕ (natural numbers)
- ℤ (integers)
- ℚ (rational numbers)

### Uncountably Infinite Sets
Sets that cannot be put in one-to-one correspondence with ℕ.

**Examples**:
- ℝ (real numbers)
- Power set of ℕ

### Cantor's Theorem
For any set A, |A| < |P(A)| (the power set has strictly greater cardinality).

---

## Applications in ML/AI

### 1. **Data Representation**
```python
# Dataset as set of samples
dataset = {(x1, y1), (x2, y2), ..., (xn, yn)}

# Feature space
feature_space = {(f1, f2, ..., fd) | fi ∈ ℝ}

# Label space for classification
label_space = {0, 1}  # Binary classification
label_space = {0, 1, 2, ..., k-1}  # Multi-class classification
```

### 2. **Probability Theory**
```python
# Sample space (set of all possible outcomes)
sample_space = {H, T}  # Coin flip
sample_space = {1, 2, 3, 4, 5, 6}  # Die roll

# Events (subsets of sample space)
event_A = {H}  # Getting heads
event_B = {2, 4, 6}  # Getting even number
```

### 3. **Boolean Logic in AI**
```python
# Logical operations as set operations
def logical_and(A, B):
    return A.intersection(B)

def logical_or(A, B):
    return A.union(B)

def logical_not(A, universe):
    return universe.difference(A)
```

### 4. **Graph Theory**
```python
# Graph as sets
vertices = {1, 2, 3, 4, 5}
edges = {(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)}

# Adjacency as relation
adjacency_relation = {(u, v) | (u, v) ∈ edges or (v, u) ∈ edges}
```

### 5. **Database Operations**
```python
# SQL-like operations using sets
def inner_join(table1, table2, key):
    """Inner join based on common key"""
    result = set()
    for row1 in table1:
        for row2 in table2:
            if row1[key] == row2[key]:
                result.add(row1 + row2)
    return result

# Union of query results
query1_results = {(1, 'Alice'), (2, 'Bob')}
query2_results = {(3, 'Charlie'), (4, 'David')}
combined_results = query1_results.union(query2_results)
```

### 6. **Feature Selection**
```python
# Feature sets
all_features = {'age', 'income', 'education', 'location', 'gender'}
selected_features = {'age', 'income', 'education'}
removed_features = all_features.difference(selected_features)

print(f"Selected: {selected_features}")
print(f"Removed: {removed_features}")
```

---

## Practice Problems

### Problem 1: Set Operations
Given A = {1, 2, 3, 4} and B = {3, 4, 5, 6}, find:
a) A ∪ B
b) A ∩ B  
c) A − B
d) A △ B

**Solutions:**
a) A ∪ B = {1, 2, 3, 4, 5, 6}
b) A ∩ B = {3, 4}
c) A − B = {1, 2}
d) A △ B = {1, 2, 5, 6}

### Problem 2: Relations
Let R be the relation "divides" on {1, 2, 3, 4, 6, 12}.
Is R reflexive, symmetric, or transitive?

**Solution:**
- Reflexive: Yes (every number divides itself)
- Symmetric: No (2 divides 4, but 4 doesn't divide 2)
- Transitive: Yes (if a|b and b|c, then a|c)

### Problem 3: Functions
Determine if f: ℝ → ℝ defined by f(x) = x² is injective, surjective, or bijective.

**Solution:**
- Injective: No (f(-2) = f(2) = 4)
- Surjective: No (no real x satisfies f(x) = -1)
- Bijective: No (neither injective nor surjective)

### Problem 4: Cardinality
Find |P(A)| where A = {1, 2, 3}.

**Solution:**
P(A) = {∅, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}
|P(A)| = 8 = 2³ = 2^|A|

---

## Python Implementation

```python
import itertools
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib_venn import venn2, venn3

class SetOperations:
    """Class for set operations and visualizations"""
    
    @staticmethod
    def demonstrate_basic_operations():
        """Demonstrate basic set operations"""
        A = {1, 2, 3, 4}
        B = {3, 4, 5, 6}
        
        print("Set Operations Demonstration")
        print(f"A = {A}")
        print(f"B = {B}")
        print(f"A ∪ B = {A.union(B)}")
        print(f"A ∩ B = {A.intersection(B)}")
        print(f"A − B = {A.difference(B)}")
        print(f"B − A = {B.difference(A)}")
        print(f"A △ B = {A.symmetric_difference(B)}")
        
        # Verify De Morgan's laws
        U = {1, 2, 3, 4, 5, 6, 7, 8}
        A_complement = U.difference(A)
        B_complement = U.difference(B)
        
        # (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
        left_side = U.difference(A.union(B))
        right_side = A_complement.intersection(B_complement)
        
        print(f"\nDe Morgan's Law Verification:")
        print(f"(A ∪ B)ᶜ = {left_side}")
        print(f"Aᶜ ∩ Bᶜ = {right_side}")
        print(f"Equal? {left_side == right_side}")
    
    @staticmethod
    def visualize_venn_diagrams():
        """Create Venn diagrams for set operations"""
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # Union
        venn2(subsets=(2, 2, 1), set_labels=('A', 'B'), ax=axes[0, 0])
        axes[0, 0].set_title('A ∪ B (Union)')
        
        # Intersection
        venn2(subsets=(0, 0, 1), set_labels=('A', 'B'), ax=axes[0, 1])
        axes[0, 1].set_title('A ∩ B (Intersection)')
        
        # Difference A - B
        venn2(subsets=(1, 0, 0), set_labels=('A', 'B'), ax=axes[1, 0])
        axes[1, 0].set_title('A − B (Difference)')
        
        # Symmetric Difference
        venn2(subsets=(1, 1, 0), set_labels=('A', 'B'), ax=axes[1, 1])
        axes[1, 1].set_title('A △ B (Symmetric Difference)')
        
        plt.tight_layout()
        plt.show()

class RelationAnalyzer:
    """Class for analyzing relations"""
    
    def __init__(self, domain, relation_pairs):
        self.domain = set(domain)
        self.relation = set(relation_pairs)
    
    def is_reflexive(self):
        """Check if relation is reflexive"""
        for a in self.domain:
            if (a, a) not in self.relation:
                return False
        return True
    
    def is_symmetric(self):
        """Check if relation is symmetric"""
        for (a, b) in self.relation:
            if (b, a) not in self.relation:
                return False
        return True
    
    def is_transitive(self):
        """Check if relation is transitive"""
        for (a, b) in self.relation:
            for (c, d) in self.relation:
                if b == c and (a, d) not in self.relation:
                    return False
        return True
    
    def is_equivalence_relation(self):
        """Check if relation is an equivalence relation"""
        return (self.is_reflexive() and 
                self.is_symmetric() and 
                self.is_transitive())
    
    def get_equivalence_classes(self):
        """Get equivalence classes if relation is equivalence"""
        if not self.is_equivalence_relation():
            return None
        
        classes = []
        remaining = self.domain.copy()
        
        while remaining:
            element = remaining.pop()
            equiv_class = {element}
            
            for other in list(remaining):
                if (element, other) in self.relation:
                    equiv_class.add(other)
                    remaining.remove(other)
            
            classes.append(equiv_class)
        
        return classes

class FunctionAnalyzer:
    """Class for analyzing functions"""
    
    def __init__(self, func, domain, codomain):
        self.func = func
        self.domain = domain
        self.codomain = codomain
        self.range = {func(x) for x in domain}
    
    def is_injective(self):
        """Check if function is injective (one-to-one)"""
        outputs = [self.func(x) for x in self.domain]
        return len(outputs) == len(set(outputs))
    
    def is_surjective(self):
        """Check if function is surjective (onto)"""
        return self.range == set(self.codomain)
    
    def is_bijective(self):
        """Check if function is bijective"""
        return self.is_injective() and self.is_surjective()
    
    def visualize_function(self):
        """Visualize function mapping"""
        if len(self.domain) <= 10 and len(self.codomain) <= 10:
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Draw domain and codomain
            domain_y = [i for i in range(len(self.domain))]
            codomain_y = [i for i in range(len(self.codomain))]
            
            # Plot domain points
            ax.scatter([0] * len(self.domain), domain_y, 
                      s=100, c='blue', label='Domain')
            for i, x in enumerate(self.domain):
                ax.annotate(str(x), (0, i), xytext=(-20, 0), 
                           textcoords='offset points')
            
            # Plot codomain points
            ax.scatter([2] * len(self.codomain), codomain_y, 
                      s=100, c='red', label='Codomain')
            for i, y in enumerate(self.codomain):
                ax.annotate(str(y), (2, i), xytext=(20, 0), 
                           textcoords='offset points')
            
            # Draw function mappings
            for i, x in enumerate(self.domain):
                y = self.func(x)
                if y in self.codomain:
                    j = list(self.codomain).index(y)
                    ax.arrow(0.1, i, 1.8, j - i, 
                            head_width=0.05, head_length=0.05, 
                            fc='green', ec='green', alpha=0.7)
            
            ax.set_xlim(-0.5, 2.5)
            ax.set_ylim(-0.5, max(len(self.domain), len(self.codomain)) - 0.5)
            ax.set_title('Function Mapping Visualization')
            ax.legend()
            plt.show()

# Practical examples
def ml_applications_demo():
    """Demonstrate ML applications of set theory"""
    
    print("=== ML Applications of Set Theory ===")
    
    # 1. Dataset representation
    print("\n1. Dataset Representation:")
    training_set = {(1, 0), (2, 0), (3, 1), (4, 1), (5, 1)}
    test_set = {(1.5, 0), (2.5, 0), (3.5, 1), (4.5, 1)}
    
    print(f"Training set: {training_set}")
    print(f"Test set: {test_set}")
    print(f"All data: {training_set.union(test_set)}")
    
    # 2. Feature selection
    print("\n2. Feature Selection:")
    all_features = {'age', 'income', 'education', 'location', 'gender', 'occupation'}
    important_features = {'age', 'income', 'education'}
    demographic_features = {'age', 'gender', 'location'}
    
    print(f"All features: {all_features}")
    print(f"Important features: {important_features}")
    print(f"Demographic features: {demographic_features}")
    print(f"Important ∩ Demographic: {important_features.intersection(demographic_features)}")
    print(f"Features to remove: {all_features.difference(important_features)}")
    
    # 3. Classification regions
    print("\n3. Classification Regions:")
    feature_space = set(itertools.product(range(10), range(10)))  # 10x10 grid
    class_0_region = {(x, y) for (x, y) in feature_space if x + y < 10}
    class_1_region = feature_space.difference(class_0_region)
    
    print(f"Total feature space size: {len(feature_space)}")
    print(f"Class 0 region size: {len(class_0_region)}")
    print(f"Class 1 region size: {len(class_1_region)}")
    print(f"Regions are disjoint: {class_0_region.isdisjoint(class_1_region)}")
    print(f"Regions cover all space: {class_0_region.union(class_1_region) == feature_space}")

if __name__ == "__main__":
    # Basic set operations
    print("=== Basic Set Operations ===")
    SetOperations.demonstrate_basic_operations()
    
    # Visualize Venn diagrams
    print("\n=== Venn Diagrams ===")
    SetOperations.visualize_venn_diagrams()
    
    # Relation analysis
    print("\n=== Relation Analysis ===")
    # Example: "divides" relation on {1, 2, 3, 4, 6, 12}
    domain = [1, 2, 3, 4, 6, 12]
    divides_relation = [(a, b) for a in domain for b in domain if b % a == 0]
    
    analyzer = RelationAnalyzer(domain, divides_relation)
    print(f"Domain: {domain}")
    print(f"'Divides' relation: {divides_relation}")
    print(f"Reflexive: {analyzer.is_reflexive()}")
    print(f"Symmetric: {analyzer.is_symmetric()}")
    print(f"Transitive: {analyzer.is_transitive()}")
    print(f"Equivalence relation: {analyzer.is_equivalence_relation()}")
    
    # Function analysis
    print("\n=== Function Analysis ===")
    # Example: f(x) = x^2 on domain {-2, -1, 0, 1, 2}
    domain = [-2, -1, 0, 1, 2]
    codomain = [0, 1, 2, 3, 4]
    f = lambda x: x**2
    
    func_analyzer = FunctionAnalyzer(f, domain, codomain)
    print(f"Function: f(x) = x²")
    print(f"Domain: {domain}")
    print(f"Codomain: {codomain}")
    print(f"Range: {func_analyzer.range}")
    print(f"Injective: {func_analyzer.is_injective()}")
    print(f"Surjective: {func_analyzer.is_surjective()}")
    print(f"Bijective: {func_analyzer.is_bijective()}")
    
    # ML applications
    ml_applications_demo()
```

---

## 🎯 Key Takeaways

1. **Sets are Fundamental**: Every mathematical concept builds on set theory
2. **Master Set Operations**: Union, intersection, difference are everywhere in ML
3. **Understand Relations**: Functions are special relations crucial for ML
4. **Learn Function Properties**: Injective, surjective, bijective matter for invertibility
5. **Practice with Code**: Implement set operations in Python
6. **Connect to ML**: See sets in data representation, feature spaces, and logic

---

## 📚 Next Steps

After mastering set theory basics, proceed to:
1. **Linear Algebra** - Vector spaces built on set theory foundations
2. **Probability Theory** - Sample spaces and events as sets
3. **Graph Theory** - Vertices and edges as sets
4. **Logic and Boolean Algebra** - Set operations in reasoning systems

---

## 🔗 Resources

- **Khan Academy**: Set theory fundamentals
- **MIT OpenCourseWare**: Mathematics for Computer Science
- **Python Documentation**: Set operations and methods
- **Discrete Mathematics**: Rosen's textbook
- **Mathematical Logic**: For advanced set theory

---

*Set theory provides the logical foundation for all of mathematics and computer science. Master it to understand the structure underlying all ML/AI concepts!*