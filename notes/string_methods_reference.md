# Python String Methods Reference

## Basic String Operations
```python
name = "Hello, World!"

# Basic info
type(name)          # <class 'str'>
len(name)           # 13
name[0]             # 'H' (first character)
```

## Search and Replace
```python
name.find("World")           # 7 (index position)
name.replace("World", "Python")  # "Hello, Python!"
name.split(", ")             # ['Hello', 'World!']
```

## Case Methods
```python
name.upper()        # "HELLO, WORLD!"
name.lower()        # "hello, world!"
```

## Cleaning Methods
```python
name.strip("!")     # "Hello, World" (removes from ends)
```

## Boolean Methods
```python
name.startswith("Hello")     # True
name.endswith("World!")      # True
name.isalpha()              # False (has punctuation)
"12345".isnumeric()         # True
```

## String Formatting
```python
"{} - {}".format("Greeting", name)  # "Greeting - Hello, World!"
f"Greeting: {name}"                 # "Greeting: Hello, World!"
```

## String Multiplication
```python
name * 3            # Repeats string 3 times
```