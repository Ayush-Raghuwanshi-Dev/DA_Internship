"""
Task 2: WHERE, ORDER BY & Aggregate Functions
Executes queries demonstrating conditional filtering, multi-column sorting, and statistical aggregations.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "Database" / "company_analytics.db"


def run_task_2():
    print("=" * 75)
    print("TASK 2: WHERE, ORDER BY & AGGREGATE FUNCTIONS")
    print("=" * 75)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Filter using WHERE and comparison operators
    print("\n--- Query 2.1: WHERE Filtering (City = 'Indore', Salary >= 70,000, Rating >= 4) ---")
    query_2_1 = """
    SELECT Emp_ID, First_Name, Last_Name, Job_Title, Salary, City, Performance_Rating
    FROM Employees
    WHERE City = 'Indore' AND Salary >= 70000 AND Performance_Rating >= 4;
    """
    cursor.execute(query_2_1)
    rows = cursor.fetchall()
    print(f"{'ID':<6} {'Name':<18} {'Job Title':<26} {'Salary (Rs.)':<14} {'City':<10} {'Rating':<6}")
    print("-" * 75)
    for r in rows:
        print(f"{r[0]:<6} {r[1] + ' ' + r[2]:<18} {r[3]:<26} {r[4]:>12,.2f} {r[5]:<10} {r[6]:<6}")

    # 2. Filter using BETWEEN and IN operators
    print("\n--- Query 2.2: BETWEEN and IN Operators (Salary BETWEEN 50k-80k, Dept IN (1, 2)) ---")
    query_2_2 = """
    SELECT Emp_ID, First_Name, Last_Name, Department_ID, Salary
    FROM Employees
    WHERE Salary BETWEEN 50000 AND 80000 AND Department_ID IN (1, 2);
    """
    cursor.execute(query_2_2)
    rows = cursor.fetchall()
    print(f"{'ID':<6} {'Name':<20} {'Dept ID':<10} {'Salary (Rs.)':<14}")
    print("-" * 55)
    for r in rows:
        print(f"{r[0]:<6} {r[1] + ' ' + r[2]:<20} {r[3]:<10} {r[4]:>12,.2f}")

    # 3. Sort using ORDER BY (Multi-tier: Salary DESC, Hire_Date ASC)
    print("\n--- Query 2.3: Sorting using ORDER BY (Salary DESC, Hire_Date ASC - Top 5) ---")
    query_2_3 = """
    SELECT Emp_ID, First_Name, Last_Name, Job_Title, Salary, Hire_Date
    FROM Employees
    ORDER BY Salary DESC, Hire_Date ASC
    LIMIT 5;
    """
    cursor.execute(query_2_3)
    rows = cursor.fetchall()
    print(f"{'ID':<6} {'Name':<18} {'Job Title':<26} {'Salary (Rs.)':<14} {'Hire Date':<12}")
    print("-" * 75)
    for r in rows:
        print(f"{r[0]:<6} {r[1] + ' ' + r[2]:<18} {r[3]:<26} {r[4]:>12,.2f} {r[5]:<12}")

    # 4. Aggregate Functions (COUNT, SUM, AVG, MIN, MAX)
    print("\n--- Query 2.4: Aggregate Functions (COUNT, SUM, AVG, MIN, MAX) ---")
    query_2_4 = """
    SELECT 
        COUNT(*) AS Total_Employees,
        COUNT(Department_ID) AS Assigned_Employees,
        SUM(Salary) AS Total_Payroll,
        ROUND(AVG(Salary), 2) AS Average_Salary,
        MIN(Salary) AS Minimum_Salary,
        MAX(Salary) AS Maximum_Salary
    FROM Employees;
    """
    cursor.execute(query_2_4)
    r = cursor.fetchone()
    print(f"Total Employee Count   : {r[0]}")
    print(f"Assigned to Dept Count : {r[1]}")
    print(f"Total Monthly Payroll  : Rs. {r[2]:,.2f}")
    print(f"Average Monthly Salary : Rs. {r[3]:,.2f}")
    print(f"Minimum Salary         : Rs. {r[4]:,.2f}")
    print(f"Maximum Salary         : Rs. {r[5]:,.2f}")

    conn.close()
    print("\n" + "=" * 75)
    print("TASK 2 COMPLETED SUCCESSFULLY")
    print("=" * 75)


if __name__ == "__main__":
    run_task_2()
