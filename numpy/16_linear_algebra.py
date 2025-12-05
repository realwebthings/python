# NumPy Linear Algebra - Matrix operations and linear algebra functions
import numpy as np

print("=" * 60)
print("NUMPY LINEAR ALGEBRA")
print("=" * 60)

# Sample matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
vector = np.array([1, 2])

print("Sample matrices:")
print(f"Matrix A:\n{A}")
print(f"Matrix B:\n{B}")
print(f"Vector: {vector}")

print("\n" + "=" * 50)
print("1. MATRIX OPERATIONS")
print("=" * 50)

# Matrix multiplication
matrix_mult = np.dot(A, B)
print(f"Matrix multiplication (A @ B):\n{matrix_mult}")

# Alternative syntax
matrix_mult_alt = A @ B
print(f"Alternative syntax (A @ B):\n{matrix_mult_alt}")

# Matrix-vector multiplication
mat_vec_mult = A @ vector
print(f"Matrix-vector multiplication:\n{mat_vec_mult}")

print("\n" + "=" * 50)
print("2. MATRIX PROPERTIES")
print("=" * 50)

# Determinant
det_A = np.linalg.det(A)
print(f"Determinant of A: {det_A:.2f}")

# Inverse
try:
    inv_A = np.linalg.inv(A)
    print(f"Inverse of A:\n{inv_A}")
    
    # Verify inverse
    identity = A @ inv_A
    print(f"A @ inv(A) (should be identity):\n{identity}")
except np.linalg.LinAlgError:
    print("Matrix A is singular (not invertible)")

# Transpose
transpose_A = A.T
print(f"Transpose of A:\n{transpose_A}")

print("\n" + "=" * 50)
print("3. EIGENVALUES AND EIGENVECTORS")
print("=" * 50)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}")

print("\n" + "=" * 50)
print("4. SOLVING LINEAR SYSTEMS")
print("=" * 50)

# Solve Ax = b
b = np.array([5, 11])  # Right-hand side
x = np.linalg.solve(A, b)
print(f"Solving Ax = b where b = {b}")
print(f"Solution x: {x}")

# Verify solution
verification = A @ x
print(f"Verification (A @ x): {verification}")
print(f"Should equal b: {b}")

print("\n" + "=" * 50)
print("5. MATRIX DECOMPOSITIONS")
print("=" * 50)

# SVD (Singular Value Decomposition)
U, s, Vt = np.linalg.svd(A)
print(f"SVD of A:")
print(f"U:\n{U}")
print(f"Singular values: {s}")
print(f"V^T:\n{Vt}")

# QR decomposition
Q, R = np.linalg.qr(A)
print(f"\nQR decomposition:")
print(f"Q:\n{Q}")
print(f"R:\n{R}")

print("\n" + "=" * 50)
print("6. NORMS AND DISTANCES")
print("=" * 50)

# Vector norms
vec = np.array([3, 4])
l2_norm = np.linalg.norm(vec)
l1_norm = np.linalg.norm(vec, ord=1)
print(f"Vector {vec}:")
print(f"L2 norm (Euclidean): {l2_norm}")
print(f"L1 norm (Manhattan): {l1_norm}")

# Matrix norms
frobenius_norm = np.linalg.norm(A, 'fro')
print(f"\nMatrix A Frobenius norm: {frobenius_norm:.2f}")