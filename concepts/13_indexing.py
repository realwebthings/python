# index operator = [] = allows you to access individual characters in a string or elements in a list/tuple by their position (index)
# indexing starts at 0 for the first element, 1 for the second, and so on. Negative indexing starts at -1 for the last element, -2 for the second last, etc.



name = "Hello, World!"
print(name[0])  # Output: H (first character)
print(name[7])  # Output: W (eighth character)
print(name[-1]) # Output: ! (last character)
print(name[-5]) # Output: o (fifth character from the end)
print(name[0:5])  # Output: Hello (characters from index 0 to 4)
print(name[7:12]) # Output: World (characters from index 7 to 11)
print(name[:5])   # Output: Hello (first five characters)
print(name[7:])   # Output: World! (characters from index 7 to the end)
print(name[-6:])  # Output: World! (last six characters)
print(name[:-7])  # Output: Hello, (all characters except the last seven)
print(name[::2])  # Output: Hlo ol! (every second character)
print(name[::-1]) # Output: !dlroW ,olleH (reversed string)


# Strings are immutable, so the following operations will raise errors
# name[0] = "h"  # This will raise a TypeError
# name.append("!!!")  # This will raise an AttributeError
# name.remove("H")  # This will raise an AttributeError


