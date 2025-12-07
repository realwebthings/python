# Regular Expressions - Pattern matching in strings

import re

print("=" * 60)
print("REGULAR EXPRESSIONS (regex)")
print("=" * 60)

text = "Contact: john@email.com or call 123-456-7890"

print("\n1. SEARCH - Find first match")
match = re.search(r'\d{3}-\d{3}-\d{4}', text)
if match:
    print(f"Phone found: {match.group()}")

print("\n2. FINDALL - Find all matches")
emails = re.findall(r'\w+@\w+\.\w+', text)
print(f"Emails: {emails}")

print("\n3. MATCH - Match from start")
text2 = "Python is awesome"
match = re.match(r'Python', text2)
print(f"Starts with Python: {match is not None}")

print("\n4. SUB - Replace pattern")
text3 = "Price: $100, $200, $300"
result = re.sub(r'\$\d+', 'REDACTED', text3)
print(f"Replaced: {result}")

print("\n5. SPLIT - Split by pattern")
text4 = "apple,banana;orange:grape"
fruits = re.split(r'[,;:]', text4)
print(f"Fruits: {fruits}")

print("\n6. COMMON PATTERNS")
patterns = {
    r'\d+': 'Digits',
    r'\w+': 'Word characters',
    r'\s+': 'Whitespace',
    r'[a-z]+': 'Lowercase letters',
    r'[A-Z]+': 'Uppercase letters',
    r'\d{3}-\d{3}-\d{4}': 'Phone number',
    r'\w+@\w+\.\w+': 'Email'
}
for pattern, desc in patterns.items():
    print(f"{pattern:20} - {desc}")

print("\n7. GROUPS - Extract parts")
text5 = "Name: John Doe, Age: 30"
match = re.search(r'Name: (\w+ \w+), Age: (\d+)', text5)
if match:
    print(f"Name: {match.group(1)}")
    print(f"Age: {match.group(2)}")

print("\n8. VALIDATION")
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

print(f"Valid: {validate_email('test@example.com')}")
print(f"Invalid: {validate_email('invalid.email')}")
