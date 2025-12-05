import numpy as np

scores = np.array([85, 90, 88, 92, 87, 95, 89, 91, 93, 90])

print("Scores: ", scores)
print("Scores == 90:", scores == 90)
print("Scores > 90:", scores > 90)
print("Scores < 90:", scores[scores < 90])
scores[scores < 90] = 0
print("Scores < 90: ", scores)
print("\n"+"="*20)
