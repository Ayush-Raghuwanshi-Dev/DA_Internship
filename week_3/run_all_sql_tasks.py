"""
Master execution runner for all SQL tasks (Tasks 1 to 5).
"""

import sys
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

TASKS = [
    ("Task 1: Introduction to Databases & SELECT", BASE_DIR / "Task_1_Introduction_SELECT" / "task_1.py"),
    ("Task 2: WHERE, ORDER BY & Aggregate Functions", BASE_DIR / "Task_2_WHERE_ORDERBY_Aggregates" / "task_2.py"),
    ("Task 3: GROUP BY & HAVING", BASE_DIR / "Task_3_GROUPBY_HAVING" / "task_3.py"),
    ("Task 4: SQL Joins", BASE_DIR / "Task_4_SQL_Joins" / "task_4.py"),
    ("Task 5: SQL Subqueries", BASE_DIR / "Task_5_SQL_Subqueries" / "task_5.py"),
]


def run_all():
    print("=" * 80)
    print("RUNNING ALL SQL TASKS (TASKS 1 TO 5)")
    print("=" * 80)

    for name, script_path in TASKS:
        print(f"\n>>> Executing {name}...")
        res = subprocess.run([sys.executable, str(script_path.name)], cwd=str(script_path.parent))
        if res.returncode != 0:
            print(f"Error executing {name}")
            sys.exit(res.returncode)

    print("\n" + "=" * 80)
    print("ALL SQL TASKS EXECUTED SUCCESSFULLY")
    print("=" * 80)


if __name__ == "__main__":
    run_all()
