"""
Master Execution Pipeline: Week 5 - Power BI & Business Intelligence
Internship: Data Analytics
Student: Ayush | Prestige Institute of Engineering, Management & Research, Indore
Description: Runs all 7 task modules sequentially, verifies Star Schema integrity,
             checks visual dashboard assets, and compiles the PDF submission report.
"""

import os
import sys
import time
import subprocess
from pathlib import Path

def run_script(script_path, desc):
    print("\n" + "=" * 85)
    print(f"RUNNING: {desc}")
    print(f"Target Script: {script_path}")
    print("=" * 85)
    t0 = time.time()
    result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
    t1 = time.time()
    
    if result.returncode == 0:
        print(result.stdout)
        print(f"[SUCCESS] {desc} finished in {t1 - t0:.2f} seconds.")
        return True
    else:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        print(f"[ERROR] {desc} failed with exit code {result.returncode}!")
        return False

def main():
    start_time = time.time()
    print("*" * 85)
    print("      DATA ANALYTICS INTERNSHIP - WEEK 5 MASTER AUTOMATION PIPELINE      ")
    print("      POWER BI & BUSINESS INTELLIGENCE (100 MARKS EVALUATION)            ")
    print("      STUDENT: AYUSH | CSE (IoT) | PIEMR, INDORE                         ")
    print("*" * 85)

    base_dir = Path(__file__).resolve().parent

    pipeline = [
        (base_dir / "Data" / "generate_datasets.py", "Step 0: Multi-Table Star Schema Generation"),
        (base_dir / "Task_1_PowerBI_Intro_Data_Import" / "task_1.py", "Task 1: Power BI Interface & Ingestion Audit"),
        (base_dir / "Task_2_Data_Cleaning_Preparation" / "task_2.py", "Task 2: Power Query ETL Data Cleaning"),
        (base_dir / "Task_3_Data_Modeling_Relationships" / "task_3.py", "Task 3: Star Schema Data Modeling & Diagram"),
        (base_dir / "Task_4_DAX_Calculated_Columns_Measures" / "task_4.py", "Task 4: DAX Measures & Calculated Columns"),
        (base_dir / "Task_5_PowerBI_Visualizations" / "task_5.py", "Task 5: Power BI Visualization Components"),
        (base_dir / "Task_6_Interactive_Dashboard_Filters" / "task_6.py", "Task 6: Master Interactive Dashboard Canvas"),
        (base_dir / "Task_7_Business_Insights_Recommendations" / "task_7.py", "Task 7: Business Insights & Strategic Recommendations")
    ]

    success_count = 0
    for script, desc in pipeline:
        ok = run_script(script, desc)
        if ok:
            success_count += 1
        else:
            print(f"\nPipeline halted due to error in: {desc}")
            sys.exit(1)

    # Check if report generator exists
    report_script = base_dir / "generate_report.py"
    if report_script.exists():
        ok = run_script(report_script, "Master Step: PDF Report Compilation")
        if ok:
            success_count += 1

    total_time = time.time() - start_time
    total_steps = len(pipeline) + (1 if report_script.exists() else 0)
    print("\n" + "*" * 85)
    print(f"PIPELINE COMPLETED! {success_count}/{total_steps} steps executed successfully.")
    print(f"Total Pipeline Runtime: {total_time:.2f} seconds.")
    print("*" * 85 + "\n")

if __name__ == "__main__":
    main()
