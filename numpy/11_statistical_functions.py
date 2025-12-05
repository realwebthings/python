import numpy as np

# Aggregate functions : summarize data and typically return only single value
array = np.array([1,2,3,4,5])

print("sum: ", np.sum(array))

array2 = np.array([[1, 2, 3], [4, 5, 6]])

print("sum: ", np.sum(array2))

print("Mean: ", np.mean(array))
print("Median: ", np.median(array))
print("Standard Deviation: ", np.std(array))
print("Variance: ", np.var(array))
print("Minimum: ", np.min(array))
print("Maximum: ", np.max(array))
print("Sum: ", np.sum(array))
print("Product: ", np.prod(array))
print("Cumulative Sum: ", np.cumsum(array))
print("Cumulative Product: ", np.cumprod(array))
print("Percentile: ", np.percentile(array, 50))
print("Correlation Coefficient: ", np.corrcoef(array, array)) # 1.0
print("Covariance: ", np.cov(array, array))
print("Unique: ", np.unique(array))
print("Arg max : ", np.argmax(array)) # index of max value
print("Arg min : ", np.argmin(array)) # index of min value


print(np.sum(array2, axis=0)) # sum of each column
print(np.sum(array2, axis=1)) # sum of each row
