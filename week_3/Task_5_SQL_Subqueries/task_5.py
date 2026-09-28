"""
Task 5: SQL Subqueries
Executes single-row, multi-row, and correlated subqueries.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "Database" / "company_analytics.db"


def run_task_5():
    print("=" * 80)
    print("TASK 5: SQL SUBQUERIES")
    print("=" * 80)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Problem 1: Scalar Subquery (Salary > Company Average)
    cursor.execute("SELECT ROUND(AVG(Salary), 2) FROM Employees;")
    company_avg = cursor.fetchone()[0]
    print(f"\n--- Problem 1: Employees Earning Above Company Average (Avg = Rs. {company_avg:,.2f}) ---")
    query_sub_1 = """
    SELECT 
        Emp_ID,
        First_Name || ' ' || Last_Name AS Employee_Name,
        Job_Title,
        Salary
    FROM Employees
    WHERE Salary > (SELECT AVG(Salary) FROM Employees)
    ORDER BY Salary DESC;
    """
    cursor.execute(query_sub_1)
    rows = cursor.fetchall()
    print(f"{'ID':<6} {'Employee Name':<20} {'Job Title':<26} {'Salary (Rs.)':<14}")
    print("-" * 70)
    for r in rows:
        print(f"{r[0]:<6} {r[1]:<20} {r[2]:<26} {r[3]:>12,.2f}")
    print(f"Total employees earning above average: {len(rows)}")

    # Problem 2: Multi-row Subquery with IN (Budget > 800,000)
    print("\n--- Problem 2: Employees in High-Budget Departments (Budget > Rs. 800,000) ---")
    query_sub_2 = """
    SELECT 
        Emp_ID,
        First_Name || ' ' || Last_Name AS Employee_Name,
        Department_ID,
        Job_Title,
        Salary
    FROM Employees
    WHERE Department_ID IN (
        SELECT Department_ID FROM Departments WHERE Budget > 800000
    )
    ORDER BY Department_ID, Salary DESC
    LIMIT 6;
    """
    cursor.execute(query_sub_2)
    rows = cursor.fetchall()
    print(f"{'ID':<6} {'Employee Name':<20} {'Dept ID':<10} {'Job Title':<26} {'Salary (Rs.)':<14}")
    print("-" * 80)
    for r in rows:
        print(f"{r[0]:<6} {r[1]:<20} {r[2]:<10} {r[3]:<26} {r[4]:>12,.2f}")

    # Problem 3: Correlated Subquery (Highest Earner in Each Department)
    print("\n--- Problem 3: Correlated Subquery (Top Earner Per Department) ---")
    query_sub_3 = """
    SELECT 
        e.Emp_ID,
        e.First_Name || ' ' || e.Last_Name AS Employee_Name,
        e.Department_ID,
        e.Job_Title,
        e.Salary
    FROM Employees e
    WHERE e.Salary = (
        SELECT MAX(sub.Salary) 
        FROM Employees sub 
        WHERE sub.Department_ID = e.Department_ID
    )
    ORDER BY e.Department_ID;
    """
    cursor.execute(query_sub_3)
    rows = cursor.fetchall()
    print(f"{'ID':<6} {'Employee Name':<20} {'Dept ID':<10} {'Job Title':<26} {'Top Salary (Rs.)':<16}")
    print("-" * 82)
    for r in rows:
        print(f"{r[0]:<6} {r[1]:<20} {r[2]:<10} {r[3]:<26} {r[4]:>14,.2f}")

    conn.close()
    print("\n" + "=" * 80)
    print("TASK 5 COMPLETED SUCCESSFULLY")
    print("=" * 80)


if __name__ == "__main__":
    run_task_5()
