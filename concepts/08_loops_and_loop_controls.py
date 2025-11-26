while True:
    print("This loop will run forever unless interrupted.")
    break  # Remove this line to let the loop run indefinitely


for i in range(5):
    print(f"Iteration number: {i}")



name = None

try:
    while name == None:
        name = input("Enter your name (or press Enter to quit): ")
        if name:
            print(f"Hello, {name}!")
        else:
            print("Goodbye!")
except EOFError:
    print("\nNo input provided. Exiting the loop.")


for i in range(3):
    print("This will print three times.")

try:
    name = ""
    while name == "":
        name = input("Please enter your name: ")
    print(f"Thank you, {name}!")    
except EOFError:
    print("\nNo input provided. Exiting the input prompt.")





for i in range(1, 6):
    for j in range(1, 6): 
        print("*", end=" ") # Print stars in the same line with spaces
    print() # Move to the next line after inner loop


    

while True:
    user_input = input("Type 'exit' to quit the loop: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {user_input}") 

for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")

for i in range(1, 11):
    if i == 6:
        break  # Exit the loop when i is 6
    print(f"Number: {i}")

for i in range(1, 11):
    if i == 6:
        pass  # Do nothing for i = 6
    else:
        print(f"Number: {i}")