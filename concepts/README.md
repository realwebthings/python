# Python Concepts - Complete Learning Guide

Master Python from basics to advanced concepts with 55+ well-organized tutorials.

## 📁 Folder Structure

```
concepts/
├── 00_python_concepts_index.py        # Learning roadmap
│
├── WEEK 1: PYTHON BASICS (01-10)
├── 01_variables.py                    # Variables and data types
├── 02_string_methods.py               # String manipulation
├── 03_type_cast.py                    # Type conversion
├── 04_user_input.py                   # Getting user input
├── 05_maths.py                        # Math operations
├── 06_conditions.py                   # If/elif/else statements
├── 07_logical_operators.py            # and, or, not operators
├── 08_loops_and_loop_controls.py      # for, while, break, continue
├── 09_list.py                         # Lists and list operations
├── 10_tuples.py                       # Tuples (immutable sequences)
│
├── WEEK 2: DATA STRUCTURES & FUNCTIONS (11-20)
├── 11_sets.py                         # Sets and set operations
├── 12_dictionary.py                   # Dictionaries (key-value pairs)
├── 13_indexing.py                     # Indexing and slicing
├── 14_functions.py                    # Function basics and first-class functions
├── 15_function_arguments.py           # Args, kwargs, default parameters
├── 16_variable_scope.py               # Local, global, nonlocal scope
├── 17_string_format.py                # String formatting (f-strings, format())
├── 18_number_format.py                # Number formatting
├── 19_random.py                       # Random module
├── 20_Exceptions.py                   # Error handling (try/except/finally)
│
├── WEEK 3: FILE I/O & MODULES (21-23)
├── 21_file_detection_using_os_module.py  # OS module for file detection
├── 22_file_system.py                  # File operations (read/write)
├── 23_modules.py                      # Import and creating modules
│
├── WEEK 4: OBJECT-ORIENTED PROGRAMMING (24-34)
├── 24_class_and_methods.py            # Classes, methods, __init__
├── 25_class_vs_instance_variable.py   # Class vs instance variables
├── 26_inheritance.py                  # Basic inheritance
├── 27_multi_level_inheritance.py      # Multi-level inheritance
├── 28_multi_inheritance.py            # Multiple inheritance
├── 29_inheritance_method_overriding.py # Method overriding
├── 30_method_chaining.py              # Method chaining pattern
├── 31_super_keyword.py                # super() function
├── 32_abstract_class.py               # Abstract classes (ABC)
├── 33_pass_class_as_parameter.py      # Classes as function parameters
├── 34_duck_typing.py                  # Duck typing concept
│
├── WEEK 5: ADVANCED FEATURES (35-46)
├── 35_static_methods.py               # @staticmethod decorator
├── 35_1_class_methods.py              # @classmethod decorator
├── 35_2_magic_methods.py              # Dunder methods (__str__, __repr__)
├── 35_3_@property_decorator.py        # @property decorator
├── 35_4_decorators.py                 # Function decorators
├── 35_walrus_operator.py              # := operator (Python 3.8+)
├── 36_assign_function_to_variable.py  # Functions as first-class objects
├── 37_higher_order_function.py        # Higher-order functions
├── 38_lambda_function.py              # Lambda expressions
├── 39_sort_function.py                # Sorting with key functions
├── 40_map.py                          # map() function
├── 41_filter.py                       # filter() function
├── 42_reduce.py                       # reduce() function
├── 43_list_comprehension.py           # List comprehensions
├── 44_dictionary_comprehension.py     # Dictionary comprehensions
├── 45_zip_function.py                 # zip() function
├── 46_main_function.py                # if __name__ == "__main__"
│
├── WEEK 6: CONCURRENCY & ADVANCED (47-55)
├── 47_time_module.py                  # Time module
├── 47_1_datetime_module.py            # Datetime module
├── 48_multiprocessing_calculations.py # Multiprocessing (CPU-bound)
├── 49_multithreading_io_bound.py      # Multithreading (I/O-bound)
├── 50_daemon_thread.py                # Daemon threads
├── 51_generators.py                   # Generator functions (yield)
├── 52_context_managers.py             # Context managers (with statement)
├── 53_iterators.py                    # Iterator protocol
├── 54_regular_expressions.py          # Regex pattern matching
└── 55_collections_module.py           # Collections (Counter, deque, etc.)
```

## 🎯 Learning Path

### Week 1: Python Basics (01-10)
**Foundation concepts for Python programming**

- Variables and data types (int, float, str, bool)
- String manipulation and methods
- Type conversion and casting
- User input handling
- Mathematical operations
- Conditional statements (if/elif/else)
- Logical operators (and, or, not)
- Loops (for, while) and loop controls
- Lists and list operations
- Tuples (immutable sequences)

### Week 2: Data Structures & Functions (11-20)
**Core data structures and function concepts**

- Sets and set operations
- Dictionaries (key-value pairs)
- Indexing and slicing
- Function definition and usage
- Function arguments (positional, keyword, default, *args, **kwargs)
- Variable scope (local, global, nonlocal)
- String and number formatting
- Random number generation
- Exception handling (try/except/finally/else)

### Week 3: File I/O & Modules (21-23)
**Working with files and organizing code**

- OS module for file system operations
- Reading and writing files
- Creating and importing modules
- Package management

### Week 4: Object-Oriented Programming (24-34)
**Master OOP concepts**

- Classes and methods
- Instance vs class variables
- Inheritance (single, multi-level, multiple)
- Method overriding
- Method chaining
- super() keyword
- Abstract classes
- Duck typing
- Passing classes as parameters

### Week 5: Advanced Features (35-46)
**Advanced Python features and functional programming**

- Static methods and class methods
- Magic/dunder methods
- Property decorators
- Function decorators
- Walrus operator (:=)
- Functions as first-class objects
- Higher-order functions
- Lambda expressions
- Sorting with custom keys
- map(), filter(), reduce()
- List and dictionary comprehensions
- zip() function
- Main guard pattern

### Week 6: Concurrency & Advanced Topics (47-55)
**Advanced topics and performance**

- Time and datetime modules
- Multiprocessing (CPU-bound tasks)
- Multithreading (I/O-bound tasks)
- Daemon threads
- Generators (memory-efficient iteration)
- Context managers (resource management)
- Iterators (custom iteration)
- Regular expressions (pattern matching)
- Collections module (specialized containers)

## 📚 Quick Reference

### Basic Syntax
```python
# Variables
name = "Python"
age = 30
is_active = True

# Conditions
if age > 18:
    print("Adult")
elif age > 12:
    print("Teen")
else:
    print("Child")

# Loops
for i in range(5):
    print(i)

while condition:
    # code
    break
```

### Data Structures
```python
# List (mutable, ordered)
my_list = [1, 2, 3]
my_list.append(4)

# Tuple (immutable, ordered)
my_tuple = (1, 2, 3)

# Set (unique, unordered)
my_set = {1, 2, 3}

# Dictionary (key-value)
my_dict = {"name": "Alice", "age": 30}
```

### Functions
```python
# Basic function
def greet(name):
    return f"Hello, {name}"

# Lambda
square = lambda x: x ** 2

# Decorator
@decorator
def function():
    pass
```

### OOP
```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, I'm {self.name}"

# Inheritance
class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
```

### Comprehensions
```python
# List comprehension
squares = [x**2 for x in range(10)]

# Dict comprehension
square_dict = {x: x**2 for x in range(5)}

# Generator expression
gen = (x**2 for x in range(10))
```

### Advanced
```python
# Context manager
with open('file.txt', 'r') as f:
    content = f.read()

# Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Decorator
def timer(func):
    def wrapper(*args, **kwargs):
        # timing code
        return func(*args, **kwargs)
    return wrapper
```

## 💡 Learning Tips

1. **Follow the sequence**: Files are numbered for progressive learning
2. **Run every file**: Execute and observe the output
3. **Modify examples**: Change values and see what happens
4. **Practice daily**: Consistency is key
5. **Build projects**: Apply concepts in real projects
6. **Read documentation**: Python docs are excellent
7. **Debug actively**: Use print() and debuggers

## 🎯 Key Files to Master

| Priority | Files | Concepts |
|----------|-------|----------|
| ⭐⭐⭐ | 01, 06, 08, 09 | Basics: variables, conditions, loops, lists |
| ⭐⭐⭐ | 14, 15, 16 | Functions and scope |
| ⭐⭐⭐ | 20 | Exception handling |
| ⭐⭐⭐ | 24, 26, 32 | OOP fundamentals |
| ⭐⭐ | 35_4, 37, 38 | Decorators, HOF, lambda |
| ⭐⭐ | 43, 44 | Comprehensions |
| ⭐⭐ | 51, 52, 53 | Generators, context managers, iterators |
| ⭐ | 48, 49 | Concurrency |

## 📈 Progress Tracker

- [ ] Week 1: Python Basics (01-10)
- [ ] Week 2: Data Structures & Functions (11-20)
- [ ] Week 3: File I/O & Modules (21-23)
- [ ] Week 4: Object-Oriented Programming (24-34)
- [ ] Week 5: Advanced Features (35-46)
- [ ] Week 6: Concurrency & Advanced (47-55)

## 🚀 Getting Started

```bash
# Navigate to concepts folder
cd /Users/mukeshkumar/MyRepo/python/concepts

# Start with the index
python 00_python_concepts_index.py

# Follow the learning path
python 01_variables.py
python 02_string_methods.py
# ... and so on
```

## 🎓 Practice Projects

### Beginner (Week 1-2)
- Calculator
- Todo list
- Number guessing game
- Temperature converter

### Intermediate (Week 3-4)
- Contact manager with file storage
- Simple banking system
- Student grade tracker
- Text-based adventure game

### Advanced (Week 5-6)
- Web scraper with threading
- Custom decorator library
- Data processing pipeline with generators
- Multi-threaded download manager

## 📖 Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Real Python Tutorials](https://realpython.com/)

## 🔑 Python Principles

1. **Readability counts** - Write clear, understandable code
2. **Simple is better than complex** - Avoid over-engineering
3. **Explicit is better than implicit** - Be clear about intentions
4. **DRY** - Don't Repeat Yourself
5. **KISS** - Keep It Simple, Stupid

---

**Happy Learning! 🐍**
