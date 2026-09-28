"""
Initialize SQLite database for Week 3: SQL & Excel for Data Analytics.
Creates Database/company_analytics.db from schema.sql and seed_data.sql.
"""

import sqlite3
from pathlib import Path

DB_DIR = Path(__file__).resolve().parent
DB_PATH = DB_DIR / "company_analytics.db"
SCHEMA_PATH = DB_DIR / "schema.sql"
SEED_PATH = DB_DIR / "seed_data.sql"


def initialize_database():
    print("=" * 60)
    print("INITIALIZING COMPANY ANALYTICS DATABASE")
    print("=" * 60)

    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Execute schema
    print("Applying schema.sql...")
    cursor.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))

    # Execute seed data
    print("Inserting seed records from seed_data.sql...")
    cursor.executescript(SEED_PATH.read_text(encoding="utf-8"))

    conn.commit()

    # Verification
    cursor.execute("SELECT COUNT(*) FROM Departments;")
    dept_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM Employees;")
    emp_count = cursor.fetchone()[0]

    print(f"Database successfully created at: {DB_PATH.name}")
    print(f"Total Departments: {dept_count}")
    print(f"Total Employees: {emp_count}")
    print("=" * 60)

    conn.close()


if __name__ == "__main__":
    initialize_database()
