# reshape() = Changes the shape of an array 
#             w/o alterning it's underlying data
#             .reshape(rows, columns)



import numpy as np
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

shaped_array = array.reshape(3, 4)

print(shaped_array)
print("\n" + "=" * 60)
shaped_array2 = array.reshape(2, 3, 2)

print(shaped_array2)
print("\n" + "=" * 60)


shaped_array3 = array.reshape(-1, 3)

print(shaped_array3)
print("\n" + "=" * 60)

shaped_array4 = array.reshape(2, -1)
print(shaped_array4)


print("\n" + "=" * 60)
shaped_array5 = array.reshape(-1, -1)
print(shaped_array5)

