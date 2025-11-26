#! /usr/bin/env python3
# random module provides various functions to generate random numbers and perform random operations
# functions include random(), randint(), choice(), shuffle(), sample(), uniform(), randrange(), seed(), etc.

import random


x = random.random()  # generates a random float between 0.0 and 1.0
print("Random float between 0.0 and 1.0:", x)

y = random.randint(1, 10)  # generates a random integer between 1 and 10 (inclusive)
print("Random integer between 1 and 10:", y)

colors = ['red', 'blue', 'green', 'yellow']
chosen_color = random.choice(colors)  # randomly selects an element from the list
print("Randomly chosen color:", chosen_color)

deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
random.shuffle(deck)  # shuffles the list in place
print("Shuffled deck:", deck)



