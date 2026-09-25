import numpy as np

print("# ========================================")
print("TASK 3 - MATHEMATICAL & STATISTICAL OPERATIONS")
print("# ========================================")

values = np.array([120, 150, 90, 200, 175, 130, 160])
print("Dataset:", values)
print("\nMathematical operations:")
print("Addition (+ 10):", values + 10)
print("Subtraction (- 10):", values - 10)
print("Multiplication (* 2):", values * 2)
print("Division (/ 2):", values / 2)

print("\nStatistical operations:")
print("Mean:", np.mean(values))
print("Median:", np.median(values))
print("Minimum:", np.min(values))
print("Maximum:", np.max(values))
print("Standard deviation:", np.std(values))
print("Sum:", np.sum(values))
