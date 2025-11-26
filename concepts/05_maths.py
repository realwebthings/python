# Math Module Examples
import math

# Mathematical constants
print("Constants:")
print("Pi(π):", math.pi)  # Output: 3.141592653589793
print("Euler's number(e):", math.e)  # Output: 2.718281828459045
print("Tau (2π):", math.tau)  # Output: 6.283185307179586
print("Golden ratio:", (1 + math.sqrt(5)) / 2)  # Output: 1.618033988749895

# Basic operations
print("\nBasic Functions:")
print("Ceiling of 4.2:", math.ceil(4.2))  # Output: 5
print("Floor of 4.7:", math.floor(4.7))  # Output: 4
print("Square root of 16:", math.sqrt(16))  # Output: 4.0
print("Power 2^3:", math.pow(2, 3))  # Output: 8.0
print("Factorial of 5:", math.factorial(5))  # Output: 120
print("GCD of 48 and 18:", math.gcd(48, 18))  # Output: 6

# Logarithms and exponentials
print("\nLogs and Exponentials:")
print("Log base 10 of 1000:", math.log10(1000))  # Output: 3.0
print("Natural log of e:", math.log(math.e))  # Output: 1.0
print("Exponential of 1:", math.exp(1))  # Output: 2.718281828459045

# Trigonometry
print("\nTrigonometry:")
print("Sin 90°:", math.sin(math.radians(90)))  # Output: 1.0
print("Cos 0°:", math.cos(math.radians(0)))  # Output: 1.0
print("Tan 45°:", math.tan(math.radians(45)))  # Output: 1.0
print("Hypotenuse (3,4):", math.hypot(3, 4))  # Output: 5.0
print("90° to radians:", math.radians(90))  # Output: 1.5707963267948966
print("π/2 to degrees:", math.degrees(math.pi / 2))  # Output: 90.0

print("\nAngular conversions:")
angle_degrees = 45
angle_radians = math.radians(angle_degrees)  # Output: 0.7853981633974483
print(f"{angle_degrees} degrees in radians is {angle_radians}")
angle_radians = math.pi / 4
angle_degrees = math.degrees(angle_radians)  # Output: 45.0
print(f"{angle_radians} radians in degrees is {angle_degrees}")

print("\nHyperbolic functions:")
print("sinh(1):", math.sinh(1))  # Output: 1.1752011936438014
print("cosh(1):", math.cosh(1))  # Output: 1.5430806348152437
print("tanh(1):", math.tanh(1))  # Output: 0.7615941559557649

print("\nSpecial functions:")
print("Gamma(5):", math.gamma(5))  # Output: 24.0
print("Log Gamma(5):", math.lgamma(5))  # Output: 3.1780538303479458

print("\nCombinatorial functions:")
print("Combinations C(5, 2):", math.comb(5, 2))  # Output: 10
print("Permutations P(5, 2):", math.perm(5, 2))  # Output: 20

print("\nIs close examples:")
print("Is 0.1 + 0.2 close to 0.3?:", math.isclose(0.1 + 0.2, 0.3))  # Output: True
print("Is 1.0000001 close to 1.0 with rel_tol=1e-7?:", math.isclose(1.0000001, 1.0, rel_tol=1e-7))  # Output: False

print("\nRounding examples:")
print("Round 3.14159 to 2 decimal places:", round(3.14159, 2))  # Output: 3.14
print("Round 2.5 to nearest integer:", round(2.5))  # Output: 2
print("Round 3.5 to nearest integer:", round(3.5))  # Output: 4
print("Round 2.675 to 2 decimal places:", round(2.675, 2))  # Output: 2.67

print("\nModf examples:")
print("Modf of 3.14:", math.modf(3.14))  # Output: (0.14000000000000012, 3.0)
print("Modf of 0.0:", math.modf(0.0))  # Output: (0.0, 0.0)
print("Modf of -2.71:", math.modf(-2.71))  # Output: (-0.7100000000000002, -2.0)

print("\nCopysign examples:")
print("Copysign of (3, -4):", math.copysign(3, -4))  # Output: -3.0
print("Copysign of (-3, 4):", math.copysign(-3, 4))  # Output: 3.0
print("Copysign of (0, -1):", math.copysign(0, -1))  # Output: -0.0



