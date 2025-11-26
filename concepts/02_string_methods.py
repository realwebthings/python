# String Methods Examples
name = "Hello, World!"

print(name)  # Output: Hello, World!

# Basic string properties
print("type:", type(name))  # Output: <class 'str'>
print("length:", len(name))  # Output: 13
print("first character:", name[0])  # Output: H

# String searching and manipulation
print("index of 'World':", name.find("World"))  # Output: 7
print("replaced string:", name.replace("World", "Python"))  # Output: Hello, Python!
print("split string:", name.split(", "))  # Output: ['Hello', 'World!']

# Case conversion
print("upper case:", name.upper())  # Output: HELLO, WORLD!
print("lower case:", name.lower())  # Output: hello, world!

# String cleaning and validation
print("stripped string:", name.strip("!"))  # Output: Hello, World
print("starts with 'Hello':", name.startswith("Hello"))  # Output: True
print("ends with 'World!':", name.endswith("World!"))  # Output: True
# Check if string contains only alphabetic characters (improved readability)
cleaned_name = name.replace(", ","").replace("!","")
print("is alphabetic:", cleaned_name.isalpha())  # Output: True
print("is numeric:", "12345".isnumeric())  # Output: True

# String formatting
print("formatted string:", "{} - {}".format("Greeting", name))  # Output: Greeting - Hello, World!
print("f-string:", f"Greeting: {name}")  # Output: Greeting: Hello, World!
print(name * 3)  # Output: Hello, World!Hello, World!Hello, World!



print("\nString slicing examples:")
text = "PythonProgramming"
print("Original text:", text)  # Output: PythonProgramming
print("First 6 characters:", text[:6])  # Output: Python
print("Characters from index 6 to 11:", text[6:11])  # Output: Progr
print("Last 11 characters:", text[-11:])  # Output: Programming
print("Every second character:", text[::2])  # Output: Ptorgamn
print("Reversed text:", text[::-1])  # Output: gnimmargorPnohtyP


print("\nString slicing examples with slice function:")
slice1 = slice(0, 6)

print(text[slice1])

# Fixed slice - slice(6, -11) creates empty result for 17-char string
slice2 = slice(6, 11)  # Gets characters from index 6 to 10
print("slice2 result:", text[slice2])  # Output: Progr
print("slice2 object:", slice2)

# Reverse slicing using slice method
reverse_slice = slice(None, None, -1)  # Equivalent to [::-1]
print("Reversed using slice:", text[reverse_slice])  # Output: gnimmargorPnohtyP

# Reverse slice with bounds
reverse_partial = slice(10, 5, -1)  # From index 10 to 6 (reverse)
print("Partial reverse:", text[reverse_partial])  # Output: amarg

# Last 5 characters (normal order)
last5 = slice(-5, None)  # Last 5 chars
print("Last 5 chars:", text[last5])  # Output: mming

# Characters from 6th to 5th from end (slice -6 to -5)
last_6_to_5 = slice(-6, -5)  # 6th from end to 5th from end
print("6th to 5th from end:", text[last_6_to_5])  # Output: m

# Reverse last 5 characters
reverse_last5 = slice(-1, -6, -1)  # Last 5 chars reversed
print("Last 5 reversed:", text[reverse_last5])  # Output: gnimm


# Why slice(10, 0) doesn't work
print("slice(10, 0) result:", repr(text[slice(10, 0)]))  # Output: '' (empty)
print("Reason: start > end with positive step defaults to step=1")

# To go from index 10 to 0, need negative step
print("slice(10, 0, -1):", text[slice(10, 0, -1)])  # Output: margorPnoh
print("slice(10, -1, -3):", text[slice(10, -1, -3)])  # Output: oP


# slice(10, -1) gives 'rammin' (excludes last char)
print("slice(10, -1):", text[slice(10, -1)])  # Output: rammin

# To get 'ramming' (include last char), use slice(10, None)
print("slice(10, None):", text[slice(10, None)])  # Output: ramming

