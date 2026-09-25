import pandas as pd

print("# ========================================")
print("TASK 4 - PANDAS SERIES & DATAFRAME")
print("# ========================================")

attendance = pd.Series([92, 88, 95, 90], index=["Aarav", "Diya", "Kabir", "Meera"])
print("Pandas Series:")
print(attendance)

students = pd.DataFrame({
    "Name": ["Aarav", "Diya", "Kabir", "Meera"],
    "Age": [20, 21, 20, 22],
    "Branch": ["CSE", "IoT", "CSE", "IoT"],
    "Marks": [86, 91, 78, 94]
})

print("\nStudent DataFrame:")
print(students)
print("\nColumn names:", list(students.columns))
print("Index:", students.index)

students["Result"] = students["Marks"].apply(lambda marks: "Pass" if marks >= 40 else "Fail")
print("\nUpdated DataFrame:")
print(students)
