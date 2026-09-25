import numpy as np

print("# ========================================")
print("TASK 1 - NUMPY INTRODUCTION & ARRAYS")
print("# ========================================")

numbers = np.array([12, 7, 25, 18, 30, 5, 42, 16, 9, 21])
one_dimensional = np.array([1, 2, 3, 4, 5])
two_dimensional = np.array([[1, 2, 3], [4, 5, 6]])

print("Array:", numbers)
print("Shape:", numbers.shape)
print("Size:", numbers.size)
print("Data type:", numbers.dtype)

print("\nOne-dimensional array:")
print(one_dimensional)

print("\nTwo-dimensional array:")
print(two_dimensional)
