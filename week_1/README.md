# Week 1 - Python Fundamentals for Data Analytics

**Student:** Ayush

**Assignment:** Python Fundamentals for Data Analytics

## Tasks Completed

1. **Python Basics** — Takes student details as input and displays them.
2. **Variables & Data Types** — Demonstrates integer, float, string, and boolean values.
3. **Operators** — Performs calculator operations on two numbers.
4. **Conditional Statements** — Validates marks and displays the corresponding grade.
5. **Loops** — Demonstrates `for` and `while` loops with numbers and a multiplication table.
6. **Functions** — Uses functions to calculate a square and the average of three numbers.
7. **Strings & Collections** — Demonstrates string methods and list, tuple, dictionary, and set operations.
8. **File Handling** — Writes an introduction to a text file and reads it back.
9. **Student Record Management System** — Provides menu-driven add, display, search, and delete operations.

## Technologies Used

- Python
- VS Code
- Streamlit

## Concepts Covered

- Variables
- Data Types
- Input/Output
- Operators
- if/elif/else
- for loop
- while loop
- Functions
- Strings
- Lists
- Tuples
- Dictionaries
- Sets
- File Handling
- Basic CRUD-style operations using Python lists/dictionaries

## Running the Programs

Run each program independently from its task folder, for example:

```bash
python task_1.py
```

Task 8 creates `introduction.txt` in its own folder when it runs. Place your actual program screenshots in the `Screenshots` folder after running the programs.

## Streamlit Interfaces

From the `Week_1` folder, enter the assignment folder and install the UI dependency:

```bash
cd week_1
pip install -r requirements.txt
```

Run the Task 8 file-handling interface:

```bash
streamlit run Task_8_File_Handling/app.py
```

Run the Task 9 student-record interface:

```bash
streamlit run Task_9_Student_Record_System/app.py
```

The original command-line programs remain available as `task_8.py` and `student_record_system.py`.

On Windows, you can use the project virtual environment directly:

```bash
cd week_1
.venv/Scripts/python.exe -m streamlit run Task_8_File_Handling/app.py
```

# DA_Internship
