# DECORATORS - Add functionality to functions without modifying them
# Think of decorators like gift wrapping - they wrap around functions to add extra features

# ============================================
# 1. BASIC FUNCTION DECORATOR
# ============================================

def my_decorator(func):
    """A simple decorator that adds behavior before and after a function"""
    def wrapper():
        print("🎁 Something before the function")
        func()  # Call the original function
        print("🎁 Something after the function")
    return wrapper

# Without decorator (manual way)
def say_hello():
    print("Hello!")

# Apply decorator manually
say_hello = my_decorator(say_hello)

print("=== Manual Decorator Application ===")
say_hello()

print("\n" + "="*50)

# ============================================
# 2. USING @ SYNTAX (Pythonic Way)
# ============================================

@my_decorator
def say_goodbye():
    print("Goodbye!")

print("=== Using @ Syntax ===")
say_goodbye()

print("\n" + "="*50)

# ============================================
# 3. DECORATOR WITH ARGUMENTS
# ============================================

def timing_decorator(func):
    """Decorator that measures how long a function takes"""
    import time
    def wrapper(*args, **kwargs):  # Accept any arguments
        start = time.time()
        result = func(*args, **kwargs)  # Call with arguments
        end = time.time()
        print(f"⏱️  {func.__name__} took {end - start:.4f} seconds")
        return result  # Return the original result
    return wrapper

@timing_decorator
def slow_function(n):
    """A function that takes some time"""
    import time
    time.sleep(0.1)  # Simulate slow work
    return f"Processed {n} items"

print("=== Timing Decorator ===")
result = slow_function(100)
print(f"Result: {result}")

print("\n" + "="*50)

# ============================================
# 4. MULTIPLE DECORATORS (STACKING)
# ============================================

def bold_decorator(func):
    """Make output bold"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"**{result}**"
    return wrapper

def italic_decorator(func):
    """Make output italic"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"*{result}*"
    return wrapper

@bold_decorator
@italic_decorator
def format_text(text):
    return text

print("=== Multiple Decorators ===")
print(format_text("Hello World"))

print("\n" + "="*50)

# ============================================
# 5. CLASS-BASED DECORATOR
# ============================================

class CountCalls:
    """Decorator class that counts function calls"""
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"📞 Call #{self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    return f"Hello, {name}!"

print("=== Class-Based Decorator ===")
print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))

print("\n" + "="*50)

# ============================================
# 6. PRACTICAL EXAMPLE - LOGIN REQUIRED
# ============================================

def login_required(func):
    """Decorator that checks if user is logged in"""
    def wrapper(user, *args, **kwargs):
        if not user.get('logged_in', False):
            return "❌ Access denied! Please log in first."
        return func(user, *args, **kwargs)
    return wrapper

@login_required
def view_profile(user):
    return f"👤 Welcome to your profile, {user['name']}!"

@login_required
def delete_account(user):
    return f"🗑️  Account deleted for {user['name']}"

print("=== Login Required Decorator ===")

# Test with logged out user
loggedout_user = {'name': 'John', 'logged_in': False}
print(view_profile(loggedout_user))

# Test with logged in user
loggedin_user = {'name': 'John', 'logged_in': True}
print(view_profile(loggedin_user))

print("\n" + "="*50)

# ============================================
# 7. DECORATOR WITH PARAMETERS
# ============================================

def repeat(times):
    """Decorator factory - creates a decorator that repeats function calls"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi there! 👋")

print("=== Decorator with Parameters ===")
say_hi()

print("\n" + "="*50)

# ============================================
# SUMMARY
# ============================================

summary = """
🎯 DECORATOR SUMMARY:

1. Basic Decorator: Wraps a function to add behavior
2. @ Syntax: Clean way to apply decorators
3. Arguments: Use *args, **kwargs to handle any function
4. Stacking: Apply multiple decorators with multiple @
5. Class-based: Use classes as decorators for state
6. Practical: Real-world examples like authentication
7. Parameters: Create configurable decorators

💡 Remember: Decorators are just functions that take functions and return functions!
"""

print(summary)  