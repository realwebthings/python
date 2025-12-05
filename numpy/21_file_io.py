# NumPy File I/O Operations
import numpy as np
import os

print("=" * 60)
print("NUMPY FILE I/O OPERATIONS")
print("=" * 60)

# Sample data
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Sample data:\n{data}")

print("\n" + "=" * 50)
print("1. SAVE/LOAD BINARY FILES (.npy)")
print("=" * 50)

# Save to binary file
np.save('data.npy', data)
print("Saved data to 'data.npy'")

# Load from binary file
loaded_data = np.load('data.npy')
print(f"Loaded data:\n{loaded_data}")

print("\n" + "=" * 50)
print("2. SAVE/LOAD MULTIPLE ARRAYS (.npz)")
print("=" * 50)

# Multiple arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([[7, 8], [9, 10]])

# Save multiple arrays
np.savez('multiple_arrays.npz', first=arr1, second=arr2, third=arr3)
print("Saved multiple arrays to 'multiple_arrays.npz'")

# Save multiple arrays compressed
np.savez_compressed('compressed_arrays.npz', first=arr1, second=arr2, third=arr3)
print("Saved compressed arrays to 'compressed_arrays.npz'")

# Load multiple arrays
loaded = np.load('multiple_arrays.npz')
loaded_compressed = np.load('compressed_arrays.npz')
print(f"Available arrays: {list(loaded.keys())}")
print(f"First array: {loaded['first']}")
print(f"Compressed first array: {loaded_compressed['first']}")

print("\n" + "=" * 50)
print("3. TEXT FILE I/O")
print("=" * 50)

# Save to text file
np.savetxt('data.txt', data, fmt='%d', delimiter=',')
print("Saved data to 'data.txt' (CSV format)")

# Load from text file
loaded_text = np.loadtxt('data.txt', delimiter=',')
print(f"Loaded from text:\n{loaded_text}")

# Save with headers
np.savetxt('data_with_header.txt', data, 
           header='col1,col2,col3', 
           delimiter=',', 
           fmt='%d')
print("Saved with header to 'data_with_header.txt'")

print("\n" + "=" * 50)
print("4. ADVANCED TEXT I/O")
print("=" * 50)

# Mixed data types
mixed_data = np.array([('Alice', 25, 5.5), ('Bob', 30, 6.0), ('Charlie', 35, 5.8)],
                     dtype=[('name', 'U10'), ('age', 'i4'), ('height', 'f4')])
print(f"Mixed data:\n{mixed_data}")

# Save structured array
np.savetxt('mixed_data.txt', mixed_data, 
           fmt='%s,%d,%.1f', 
           header='name,age,height')
print("Saved mixed data to 'mixed_data.txt'")

print("\n" + "=" * 50)
print("5. MEMORY-MAPPED FILES")
print("=" * 50)

# Create memory-mapped array
mmap_array = np.memmap('mmap_data.dat', dtype='float32', mode='w+', shape=(1000, 1000))
mmap_array[0, :10] = np.arange(10)
print("Created memory-mapped file 'mmap_data.dat'")
print(f"First 10 elements: {mmap_array[0, :10]}")

# Cleanup files
cleanup_files = ['data.npy', 'multiple_arrays.npz', 'compressed_arrays.npz', 'data.txt', 
                'data_with_header.txt', 'mixed_data.txt', 'mmap_data.dat']
for file in cleanup_files:
    if os.path.exists(file):
        os.remove(file)
        print(f"Cleaned up {file}")

print("\n" + "=" * 50)
print("FILE I/O SUMMARY")
print("=" * 50)
print("BINARY FILES:")
print("- np.save()/np.load(): Single array (.npy)")
print("- np.savez()/np.load(): Multiple arrays (.npz)")
print("- np.savez_compressed(): Compressed multiple arrays (.npz)")
print("\nTEXT FILES:")
print("- np.savetxt()/np.loadtxt(): Human-readable format")
print("- Supports CSV, custom delimiters, headers")
print("\nMEMORY-MAPPED:")
print("- np.memmap(): Large files, partial loading")
print("- Efficient for huge datasets")