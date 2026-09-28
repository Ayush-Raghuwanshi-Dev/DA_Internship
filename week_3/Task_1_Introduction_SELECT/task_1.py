"""
Task 1: Introduction to Databases & SELECT Statement
Executes SQL queries to display all records, select specific columns, and apply column aliases.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "Database" / "company_analytics.db"


def run_task_1():
    print("=" * 70)
    print("TASK 1: INTRODUCTION TO DATABASES & SELECT STATEMENT")
    print("=" * 70)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Display All Records (First 5 records displayed for clean output)
    print("\n--- Query 1.1: Display All Records (SELECT * FROM Employees) ---")
    cursor.execute("SELECT * FROM Employees LIMIT 5;")
    rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print(f"{' | '.join(headers)}")
    print("-" * 70)
    for row in rows:
        print(" | ".join(str(val) for val in row))
    cursor.execute("SELECT COUNT(*) FROM Employees;")
    total_records = cursor.fetchone()[0]
    print(f"(Displaying top 5 of {total_records} total employee records in table)")

    # 2. Select Specific Columns
    print("\n--- Query 1.2: Select Specific Columns ---")
    print("Columns: Emp_ID, First_Name, Last_Name, Job_Title, Salary")
    cursor.execute("SELECT Emp_ID, First_Name, Last_Name, Job_Title, Salary FROM Employees LIMIT 5;")
    rows = cursor.fetchall()
    print(f"{'ID':<6} {'First Name':<12} {'Last Name':<12} {'Job Title':<26} {'Salary (Rs.)':<12}")
    print("-" * 70)
    for r in rows:
        print(f"{r[0]:<6} {r[1]:<12} {r[2]:<12} {r[3]:<26} {r[4]:>10,.2f}")

    # 3. Column Aliases and Calculations
    print("\n--- Query 1.3: Column Aliases & Calculated Columns ---")
    query = """
    SELECT 
        Emp_ID AS Employee_ID,
        First_Name || ' ' || Last_Name AS Full_Name,
        Job_Title AS Designation,
        Salary AS Monthly_Salary,
        (Salary * 12) AS Annual_Compensation
    FROM Employees
    LIMIT 5;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    print(f"{'Emp ID':<8} {'Full Name':<20} {'Designation':<26} {'Monthly (Rs.)':<14} {'Annual Comp (Rs.)':<18}")
    print("-" * 90)
    for r in rows:
        print(f"{r[0]:<8} {r[1]:<20} {r[2]:<26} {r[3]:>12,.2f} {r[4]:>16,.2f}")

    conn.close()
    print("\n" + "=" * 70)
    print("TASK 1 COMPLETED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    run_task_1()
