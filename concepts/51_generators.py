# Generators - Functions that yield values one at a time (memory efficient)

print("=" * 60)
print("GENERATORS")
print("=" * 60)

# Regular function returns all at once
def regular_function(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Generator yields one at a time
def generator_function(n):
    for i in range(n):
        yield i ** 2

print("\n1. BASIC GENERATOR")
gen = generator_function(5)
print(f"Generator object: {gen}")
print(f"First value: {next(gen)}")
print(f"Second value: {next(gen)}")

print("\n2. ITERATE THROUGH GENERATOR")
for value in generator_function(5):
    print(value, end=" ")

print("\n\n3. GENERATOR EXPRESSION")
gen_exp = (x ** 2 for x in range(5))
print(f"Generator expression: {gen_exp}")
print(f"Values: {list(gen_exp)}")

print("\n4. MEMORY COMPARISON")
import sys
regular = regular_function(1000)
gen = generator_function(1000)
print(f"List size: {sys.getsizeof(regular)} bytes")
print(f"Generator size: {sys.getsizeof(gen)} bytes")

print("\n5. INFINITE GENERATOR")
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
print(f"First 5 values: {[next(gen) for _ in range(5)]}")

print("\n6. FIBONACCI GENERATOR")
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(f"Fibonacci: {list(fibonacci(10))}")
