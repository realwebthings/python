"""
DECORATOR vs HIGHER-ORDER FUNCTION
Key Point: Decorators ARE Higher-Order Functions with @ syntax sugar!
"""

import time

# ============================================
# HIGHER-ORDER FUNCTION (Manual Application)
# ============================================

def timing_hof(func):
    """Higher-Order Function - takes function, returns function"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

def logging_hof(func):
    """Higher-Order Function - adds logging"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

# Manual application (HOF style)
def add_numbers(a, b):
    time.sleep(0.1)  # Simulate work
    return a + b

# Apply HOFs manually
add_with_timing = timing_hof(add_numbers)
add_with_logging = logging_hof(add_numbers)
add_with_both = timing_hof(logging_hof(add_numbers))

# ============================================
# DECORATOR (Syntactic Sugar for HOF)
# ============================================

# Same functions, but applied with @ syntax
@timing_hof
@logging_hof
def multiply_numbers(a, b):
    time.sleep(0.1)  # Simulate work
    return a * b

# ============================================
# COMPARISON DEMONSTRATION
# ============================================

print("="*60)
print("DECORATOR vs HIGHER-ORDER FUNCTION")
print("="*60)

print("\n1. HIGHER-ORDER FUNCTION (Manual):")
print("   add_with_both = timing_hof(logging_hof(add_numbers))")
result1 = add_with_both(5, 3)
print(f"   Result: {result1}")

print("\n2. DECORATOR (Syntactic Sugar):")
print("   @timing_hof")
print("   @logging_hof")
print("   def multiply_numbers(a, b): ...")
result2 = multiply_numbers(5, 3)
print(f"   Result: {result2}")

# ============================================
# THEY ARE THE SAME THING!
# ============================================

print("\n" + "="*60)
print("PROOF THEY ARE THE SAME")
print("="*60)

# These are equivalent:
def original_func():
    return "Hello World"

# Method 1: HOF style
hof_version = timing_hof(original_func)

# Method 2: Decorator style  
@timing_hof
def decorator_version():
    return "Hello World"

print("\nBoth produce the same result:")
print("HOF version:", hof_version())
print("Decorator version:", decorator_version())

# ============================================
# KEY DIFFERENCES IN USAGE
# ============================================

print("\n" + "="*60)
print("KEY DIFFERENCES")
print("="*60)

differences = """
HIGHER-ORDER FUNCTION (Manual):
✅ Explicit function composition
✅ Can be applied conditionally
✅ More verbose but clearer flow
✅ Can be stored in variables
✅ Runtime application

Example:
    enhanced_func = hof1(hof2(original_func))
    if condition:
        enhanced_func = hof3(enhanced_func)

DECORATOR (@ Syntax):
✅ Clean, readable syntax
✅ Applied at definition time
✅ Pythonic way to enhance functions
✅ Cannot be applied conditionally at definition
✅ Compile-time application

Example:
    @hof1
    @hof2
    def original_func():
        pass
"""

print(differences)

# ============================================
# PRACTICAL EXAMPLES
# ============================================

print("\n" + "="*60)
print("PRACTICAL EXAMPLES")
print("="*60)

# HOF: Conditional application
def create_api_endpoint(func, auth_required=True, rate_limit=True):
    """HOF: Conditionally apply enhancements"""
    enhanced = func
    
    if auth_required:
        enhanced = require_auth(enhanced)
    
    if rate_limit:
        enhanced = apply_rate_limit(enhanced)
    
    return enhanced

def require_auth(func):
    def wrapper(*args, **kwargs):
        print("🔐 Checking authentication...")
        return func(*args, **kwargs)
    return wrapper

def apply_rate_limit(func):
    def wrapper(*args, **kwargs):
        print("⏱️  Checking rate limit...")
        return func(*args, **kwargs)
    return wrapper

# HOF usage - conditional
def get_user_data():
    return "User data"

# Apply conditionally
public_endpoint = create_api_endpoint(get_user_data, auth_required=False, rate_limit=True)
private_endpoint = create_api_endpoint(get_user_data, auth_required=True, rate_limit=True)

print("\nHOF - Conditional application:")
print("Public endpoint:")
public_endpoint()

print("\nPrivate endpoint:")
private_endpoint()

# Decorator usage - fixed at definition
@require_auth
@apply_rate_limit
def get_admin_data():
    return "Admin data"

print("\nDecorator - Fixed at definition:")
get_admin_data()

# ============================================
# WHEN TO USE WHICH
# ============================================

print("\n" + "="*60)
print("WHEN TO USE WHICH")
print("="*60)

usage_guide = """
USE HIGHER-ORDER FUNCTIONS WHEN:
🎯 You need conditional application
🎯 Runtime composition is required
🎯 Building function pipelines dynamically
🎯 Creating configurable enhancements
🎯 Functional programming style

USE DECORATORS WHEN:
🎯 Enhancement is always needed
🎯 Clean, readable code is priority
🎯 Following Python conventions
🎯 Fixed enhancement at definition time
🎯 Framework/library patterns (Flask, Django)

REMEMBER:
💡 Decorators ARE Higher-Order Functions
💡 @ is just syntactic sugar
💡 Both achieve the same goal
💡 Choose based on your use case
"""

print(usage_guide)