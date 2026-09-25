import numpy as np

print("# ========================================")
print("TASK 2 - INDEXING, SLICING & RESHAPING")
print("# ========================================")

original_array = np.arange(1, 13)
print("Original one-dimensional array:")
print(original_array)
print("Element at index 2:", original_array[2])
print("Last element:", original_array[-1])
print("Slice from index 3 to 7:", original_array[3:8])

two_dimensional = original_array.reshape(3, 4)
print("\nTwo-dimensional array:")
print(two_dimensional)
print("Specific row (row 2):", two_dimensional[1])
print("Specific column (column 3):", two_dimensional[:, 2])
print("Element at row 1, column 4:", two_dimensional[0, 3])

reshaped_array = original_array.reshape(4, 3)
print("\nReshaped array (4 x 3):")
print(reshaped_array)
