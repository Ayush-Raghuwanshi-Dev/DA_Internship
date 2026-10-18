"""
Master Automation Pipeline: Week 6 - Git, GitHub & Final Data Analytics Project
Student: Ayush | B.Tech CSE (IoT) | PIEMR, Indore
Executes all 8 tasks sequentially, generates visual and terminal screenshots,
and compiles the final beginner student-style PDF capstone submission report.
"""

import sys
import time
import subprocess
from pathlib import Path


def run_script(script_path, desc):
    print("\n" + "=" * 85)
    print(f"RUNNING: {desc}")
    print(f"Target Script: {script_path.name}")
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
    print("      DATA ANALYTICS INTERNSHIP - WEEK 6 CAPSTONE MASTER PIPELINE        ")
    print("      GIT, GITHUB & FINAL DATA ANALYTICS PROJECT (100 MARKS)             ")
    print("      STUDENT: AYUSH | CSE (IoT) | PIEMR, INDORE                         ")
    print("*" * 85)

    base_dir = Path(__file__).resolve().parent

    pipeline = [
        (base_dir / "Data" / "generate_dataset.py", "Step 0: E-Commerce Dataset Generation"),
        (base_dir / "Task_1_Git_GitHub_Basics" / "task_1_git_verification.py", "Task 1: Git & GitHub Basics Audit"),
        (base_dir / "Task_2_Git_Workflow" / "task_2_workflow_logger.py", "Task 2: Git Workflow Practice & Commits"),
        (base_dir / "Task_3_Dataset_Preparation" / "task_3.py", "Task 3: Dataset Selection & ETL Data Cleaning"),
        (base_dir / "Task_4_Exploratory_Data_Analysis" / "task_4.py", "Task 4: Exploratory Data Analysis (EDA)"),
        (base_dir / "Task_5_Data_Visualization" / "task_5.py", "Task 5: Publication-Grade Visualizations"),
        (base_dir / "Task_6_PowerBI_Dashboard" / "task_6.py", "Task 6: Power BI Executive Dashboard Canvas"),
        (base_dir / "Task_7_Business_Insights_Recommendations" / "task_7.py", "Task 7: Business Insights & Strategic Recommendations"),
        (base_dir / "Task_8_Documentation_Presentation" / "task_8.py", "Task 8: GitHub Documentation & Presentation Audit"),
        (base_dir / "generate_screenshots.py", "Step 9: Output Screenshots Generation"),
        (base_dir / "generate_report.py", "Step 10: Final PDF Capstone Report Compilation")
    ]

    success_count = 0
    for script, desc in pipeline:
        if script.exists():
            ok = run_script(script, desc)
            if ok:
                success_count += 1
            else:
                print(f"\nPipeline halted due to error in: {desc}")
                sys.exit(1)
        else:
            print(f"[!] Warning: {script.name} not found!")

    total_time = time.time() - start_time
    print("\n" + "*" * 85)
    print(f"PIPELINE COMPLETED! {success_count}/{len(pipeline)} steps executed successfully.")
    print(f"Total Pipeline Runtime: {total_time:.2f} seconds.")
    print("*" * 85 + "\n")


if __name__ == "__main__":
    main()
