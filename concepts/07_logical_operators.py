try:
    temp = int(input("Please enter the temperature: "))
except EOFError:
    print(f"Invalid input: {EOFError}")
    print("No input provided.")
    temp = -273  # Assigning an impossible temperature to indicate error


if temp < -273:
    print("Temperature cannot be below absolute zero.")
elif temp < 0:
    print("It's freezing cold!")
elif temp < 20:
    print("It's quite chilly.")
elif temp < 30:
    print("The weather is warm.")
elif temp > 30 and temp < 40:
    print("It's normally hot.")
elif temp < 40:
    print("It's hot outside!")
else:
    print("Extreme heat warning!")