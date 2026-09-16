print("===== A. STRING OPERATIONS =====")
sample_string = "Python for Data Analytics"
print("Original:", sample_string)
print("Uppercase:", sample_string.upper())
print("Lowercase:", sample_string.lower())
print("Replace:", sample_string.replace("Python", "Learning Python"))
print("Position of 'Data':", sample_string.find("Data"))

print("\n===== B. LIST OPERATIONS =====")
marks = [75, 62, 89]
print("Original list:", marks)
marks.append(94)
print("After append:", marks)
marks.remove(62)
print("After remove:", marks)
marks.sort()
print("After sort:", marks)

print("\n===== C. TUPLE =====")
students = ("Ayush", "Rahul", "Aman")
print("Tuple:", students)
print("First student:", students[0])

print("\n===== D. DICTIONARY =====")
student = {
    "name": "Ayush",
    "age": 21,
    "branch": "B.Tech CSE (IoT)"
}
print("Student dictionary:", student)
print("Name:", student["name"])
print("Age:", student["age"])
print("Branch:", student["branch"])

print("\n===== E. SET =====")
subjects = {"Python", "Statistics", "Excel"}
print("Original set:", subjects)
subjects.add("SQL")
print("After add:", subjects)
subjects.remove("Excel")
print("After remove:", subjects)
