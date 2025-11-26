#Exceptions in Python are used to handle errors and other exceptional events that occur during program execution. 
# They allow you to manage errors gracefully without crashing the program.


numerator =  int(input("Enter numerator: "), 10)
denominator = int(input("Enter denominator: "), 10)

result = numerator/denominator
print(f"Result: {result}")


# The above code will raise a ZeroDivisionError if the denominator is zero.
# To handle this, we can use try-except blocks. 

try:
    numerator =  int(input("Enter numerator: "), 10)
    denominator = int(input("Enter denominator: "), 10)

    result = numerator/denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("No exceptions occurred.")
    print(f"Result: {result}")
finally:
    print("Execution completed.")