import matplotlib
import matplotlib.pyplot as plt

print(f"Matplotlib version: {matplotlib.__version__}")

# Basic plot example
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Simple Line Plot')
plt.show()