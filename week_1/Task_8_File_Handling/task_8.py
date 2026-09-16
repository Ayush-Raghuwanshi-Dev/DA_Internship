file_name = "introduction.txt"

introduction = """Name: Ayush
College: Prestige Institute of Engineering, Management & Research, Indore
Branch: B.Tech CSE (IoT)
I am learning Python fundamentals for Data Analytics.
"""

with open(file_name, "w", encoding="utf-8") as file:
    file.write(introduction)

with open(file_name, "r", encoding="utf-8") as file:
    file_contents = file.read()

print("----- File Contents -----")
print(file_contents)
