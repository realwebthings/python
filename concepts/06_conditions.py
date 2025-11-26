try:
    
    age = int(input("Please enter your age: "))
except EOFError:
    print(f"Invalid input: {EOFError}")
    print("No input provided.")
    age = -1


if age < 0:
    print("Age cannot be negative.")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")