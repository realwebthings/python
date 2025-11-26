#string formatting using format() method = optional but powerful way to format strings
# format specifiers can be used to control alignment, width, precision, and type of data

pi = 3.14159

text = "The value of pi is approximately {:.2f}.".format(pi)
print(text)  # Output: The value of pi is approximately 3.14.


# f-strings with formatting

print(f"The value of pi is approximately {pi:.3f}.")  # Output: The value of pi is approximately 3.142.


print(f"Integer: {42:d}, Hex: {42:x}, Octal: {42:o}, Binary: {42:b}, Exponential: {10000:e}, Scientific: {pi:.2e}")  
# Output: Integer: 42, Hex: 2a, Octal: 52, Binary: 101010, Scientific: 3.14e+00
print(f"Integer: {42:d}, Hex: {42:X}, Octal: {42:o}, Binary: {42:b}, , Exponential: {10000:E}, Scientific: {pi:.2E}")  
# Output: Integer: 42, Hex: 2A, Octal: 52, Binary: 101010, Scientific: 3.14E+00




