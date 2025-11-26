food = ["pizza", "hamburger", "hotdog", "spaghetti"]

print(food[0])  # Output: pizza 
print(food[1])  # Output: hamburger


food.append("sushi")  # Add sushi to the end of the list
print(food)  # Output: ['pizza', 'hamburger', 'hotdog', 'spaghetti', 'sushi'] 
food.remove("hotdog")  # Remove hotdog from the list
print(food)  # Output: ['pizza', 'hamburger', 'spaghetti', 'sushi'] 

food.reverse()  # Reverse the order of the list
print(food)  # Output: ['sushi', 'spaghetti', 'hamburger', 'pizza']
print(len(food))  # Output: 4 (number of items in the list)

food.extend(["ice cream", "salad"])  # Add multiple items to the list
print(food)  # Output: ['sushi', 'spaghetti', 'hamburger', 'pizza', 'ice cream', 'salad']
print(food.index("pizza"))  # Output: 3 (index of pizza in the list)
print(food.count("salad"))  # Output: 1 (number of times salad appears in the list)

food.insert(2, "fries")  # Insert fries at index 2
print(food)  # Output: ['sushi', 'spaghetti', 'fries', 'hamburger', 'pizza', 'ice cream', 'salad'] 
food.pop()  # Remove and return the last item in the list
print(food)  # Output: ['sushi', 'spaghetti', 'fries', 'hamburger', 'pizza', 'ice cream']
food.sort()  # Sort the list in ascending order 
sorted_food = sorted(food)  # Create a new sorted list without modifying the original
food.sort(reverse=True)  # Sort the list in descending order
print(food)  # Output: ['sushi', 'spaghetti', 'pizza', 'hamburger', 'fries', 'ice cream']

print("sort food in descending order without modifying the original list:")
sorted(food, reverse=True) # Sort the list in descending order without modifying the original
print(food)  # Output: [] (the list is now empty)
food.clear()  # Remove all items from the list



# 2D Lists (Lists of Lists)
drinks = ["coffee", "tea", "juice"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food[0][1])  # Output: tea (second item in the drinks list)
print(food[1][0])  # Output: pizza (first item in the dinner list 

for food_category in food:
    for item in food_category:
        print(item)  # Print each item in the 2D list