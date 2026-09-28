"""
Task 4: SQL Joins (INNER JOIN, LEFT JOIN, RIGHT JOIN)
Executes relational join queries combining Employees and Departments tables.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "Database" / "company_analytics.db"


def run_task_4():
    print("=" * 85)
    print("TASK 4: SQL JOINS (INNER, LEFT, RIGHT JOIN)")
    print("=" * 85)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. INNER JOIN
    print("\n--- Query 4.1: INNER JOIN (Only Matching Records in Both Tables) ---")
    query_inner = """
    SELECT 
        e.Emp_ID,
        e.First_Name || ' ' || e.Last_Name AS Employee_Name,
        e.Job_Title,
        d.Department_Name,
        e.Salary
    FROM Employees e
    INNER JOIN Departments d ON e.Department_ID = d.Department_ID
    LIMIT 6;
    """
    cursor.execute(query_inner)
    rows = cursor.fetchall()
    print(f"{'ID':<6} {'Employee Name':<20} {'Job Title':<26} {'Department':<20} {'Salary (Rs.)':<14}")
    print("-" * 88)
    for r in rows:
        print(f"{r[0]:<6} {r[1]:<20} {r[2]:<26} {r[3]:<20} {r[4]:>12,.2f}")
    cursor.execute("SELECT COUNT(*) FROM Employees e INNER JOIN Departments d ON e.Department_ID = d.Department_ID;")
    print(f"(Showing 6 of {cursor.fetchone()[0]} matching inner join records. Unassigned employee 125 is excluded.)")

    # 2. LEFT JOIN
    print("\n--- Query 4.2: LEFT JOIN (All Employees Preserved, Even If Unassigned) ---")
    query_left = """
    SELECT 
        e.Emp_ID,
        e.First_Name || ' ' || e.Last_Name AS Employee_Name,
        e.Job_Title,
        COALESCE(d.Department_Name, '[Unassigned]') AS Department_Name,
        e.Salary
    FROM Employees e
    LEFT JOIN Departments d ON e.Department_ID = d.Department_ID
    WHERE e.Department_ID IS NULL OR e.Emp_ID IN (101, 102);
    """
    cursor.execute(query_left)
    rows = cursor.fetchall()
    print(f"{'ID':<6} {'Employee Name':<20} {'Job Title':<26} {'Department':<20} {'Salary (Rs.)':<14}")
    print("-" * 88)
    for r in rows:
        print(f"{r[0]:<6} {r[1]:<20} {r[2]:<26} {r[3]:<20} {r[4]:>12,.2f}")
    print("(Notice: Emp 125 Tanvi Bansal is preserved with '[Unassigned]' department.)")

    # 3. RIGHT JOIN
    print("\n--- Query 4.3: RIGHT JOIN (All Departments Preserved, Even With 0 Staff) ---")
    supports_right = sqlite3.sqlite_version_info >= (3, 39)
    if supports_right:
        query_right = """
        SELECT 
            d.Department_ID,
            d.Department_Name,
            d.Manager_Name,
            d.Budget,
            COALESCE(e.First_Name || ' ' || e.Last_Name, '[No Staff Assigned]') AS Employee_Name
        FROM Employees e
        RIGHT JOIN Departments d ON e.Department_ID = d.Department_ID
        ORDER BY d.Department_ID DESC
        LIMIT 5;
        """
    else:
        query_right = """
        SELECT 
            d.Department_ID,
            d.Department_Name,
            d.Manager_Name,
            d.Budget,
            COALESCE(e.First_Name || ' ' || e.Last_Name, '[No Staff Assigned]') AS Employee_Name
        FROM Departments d
        LEFT JOIN Employees e ON d.Department_ID = e.Department_ID
        ORDER BY d.Department_ID DESC
        LIMIT 5;
        """
    cursor.execute(query_right)
    rows = cursor.fetchall()
    print(f"{'Dept ID':<8} {'Department Name':<26} {'Manager Name':<18} {'Budget (Rs.)':<16} {'Staff Assigned':<22}")
    print("-" * 94)
    for r in rows:
        print(f"{r[0]:<8} {r[1]:<26} {r[2]:<18} Rs. {r[3]:>10,.2f}  {r[4]:<22}")
    print("(Notice: Dept 6 'Research & Development' is preserved with '[No Staff Assigned]'.)")

    conn.close()
    print("\n" + "=" * 85)
    print("TASK 4 COMPLETED SUCCESSFULLY")
    print("=" * 85)


if __name__ == "__main__":
    run_task_4()
