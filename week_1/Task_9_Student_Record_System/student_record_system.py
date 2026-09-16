students = []


def add_student():
    """Collect student details and add a record to the list."""
    print("\n----- Add Student -----")
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    branch = input("Enter student branch: ")
    college = input("Enter student college: ")
    marks = float(input("Enter student marks: "))

    student = {
        "name": name,
        "age": age,
        "branch": branch,
        "college": college,
        "marks": marks
    }
    students.append(student)
    print("Student added successfully.")


def display_students():
    """Display every student currently stored."""
    if not students:
        print("No student records found.")
        return

    print("\n----- Student Records -----")
    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Branch:", student["branch"])
        print("College:", student["college"])
        print("Marks:", student["marks"])
        print("--------------------------")


def search_student():
    """Find and display records matching a student's name."""
    search_name = input("Enter student name to search: ").strip().lower()

    for student in students:
        if student["name"].lower() == search_name:
            print("\nStudent found:")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Branch:", student["branch"])
            print("College:", student["college"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


def delete_student():
    """Delete the first record matching a student's name."""
    delete_name = input("Enter student name to delete: ").strip().lower()

    for student in students:
        if student["name"].lower() == delete_name:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def main():
    while True:
        print("\n========================================")
        print("STUDENT RECORD MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 5.")


if __name__ == "__main__":
    main()
