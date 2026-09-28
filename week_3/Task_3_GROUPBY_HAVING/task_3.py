"""
Task 3: GROUP BY & HAVING Clauses
Executes group aggregation queries and filters aggregated buckets using HAVING.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "Database" / "company_analytics.db"


def run_task_3():
    print("=" * 75)
    print("TASK 3: GROUP BY & HAVING CLAUSES")
    print("=" * 75)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. GROUP BY on Department_ID with aggregates
    print("\n--- Query 3.1: Aggregate Metrics Grouped by Department_ID ---")
    query_3_1 = """
    SELECT 
        Department_ID,
        COUNT(*) AS Headcount,
        ROUND(AVG(Salary), 2) AS Average_Salary,
        SUM(Salary) AS Total_Payroll,
        MIN(Salary) AS Min_Salary,
        MAX(Salary) AS Max_Salary
    FROM Employees
    WHERE Department_ID IS NOT NULL
    GROUP BY Department_ID
    ORDER BY Department_ID;
    """
    cursor.execute(query_3_1)
    rows = cursor.fetchall()
    print(f"{'Dept ID':<8} {'Headcount':<11} {'Average Salary':<16} {'Total Payroll':<16} {'Min Salary':<14} {'Max Salary':<14}")
    print("-" * 82)
    for r in rows:
        print(f"{r[0]:<8} {r[1]:<11} Rs. {r[2]:>10,.2f}  Rs. {r[3]:>10,.2f}  Rs. {r[4]:>8,.2f}  Rs. {r[5]:>8,.2f}")

    # 2. GROUP BY with HAVING (Average Salary > 65,000)
    print("\n--- Query 3.2: HAVING Filter (Average Salary > Rs. 65,000) ---")
    query_3_2 = """
    SELECT 
        Department_ID,
        COUNT(*) AS Headcount,
        ROUND(AVG(Salary), 2) AS Average_Salary,
        SUM(Salary) AS Total_Payroll
    FROM Employees
    WHERE Department_ID IS NOT NULL
    GROUP BY Department_ID
    HAVING AVG(Salary) > 65000
    ORDER BY Average_Salary DESC;
    """
    cursor.execute(query_3_2)
    rows = cursor.fetchall()
    print(f"{'Dept ID':<8} {'Headcount':<11} {'Average Salary':<16} {'Total Payroll':<16}")
    print("-" * 55)
    for r in rows:
        print(f"{r[0]:<8} {r[1]:<11} Rs. {r[2]:>10,.2f}  Rs. {r[3]:>10,.2f}")

    # 3. GROUP BY with HAVING (Headcount >= 5)
    print("\n--- Query 3.3: HAVING Filter (Large Departments: Headcount >= 5) ---")
    query_3_3 = """
    SELECT 
        Department_ID,
        COUNT(*) AS Headcount,
        ROUND(AVG(Salary), 2) AS Average_Salary,
        SUM(Salary) AS Total_Payroll
    FROM Employees
    WHERE Department_ID IS NOT NULL
    GROUP BY Department_ID
    HAVING COUNT(*) >= 5;
    """
    cursor.execute(query_3_3)
    rows = cursor.fetchall()
    print(f"{'Dept ID':<8} {'Headcount':<11} {'Average Salary':<16} {'Total Payroll':<16}")
    print("-" * 55)
    for r in rows:
        print(f"{r[0]:<8} {r[1]:<11} Rs. {r[2]:>10,.2f}  Rs. {r[3]:>10,.2f}")

    conn.close()
    print("\n" + "=" * 75)
    print("TASK 3 COMPLETED SUCCESSFULLY")
    print("=" * 75)


if __name__ == "__main__":
    run_task_3()
