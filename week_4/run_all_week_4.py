"""
Master Execution Pipeline: Week 4 - Statistics, Data Visualization & EDA
Internship: Data Analytics
Student: Ayush | Prestige Institute of Engineering, Management & Research, Indore
Description: Runs all 9 task modules sequentially, checks visual asset generation,
             and verifies pipeline integrity.
"""

import os
import sys
import time
import subprocess

def run_script(script_path, desc):
    print("\n" + "=" * 80)
    print(f"RUNNING: {desc}")
    print(f"Target Script: {script_path}")
    print("=" * 80)
    t0 = time.time()
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
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
    print("*" * 80)
    print("      DATA ANALYTICS INTERNSHIP - WEEK 4 MASTER AUTOMATION PIPELINE      ")
    print("      STUDENT: AYUSH | CSE (IoT) | PIEMR, INDORE                        ")
    print("*" * 80)

    base_dir = os.path.dirname(os.path.abspath(__file__))

    pipeline = [
        (os.path.join(base_dir, "Data", "generate_datasets.py"), "Step 0: Dataset Generation"),
        (os.path.join(base_dir, "Task_1_Mean_Median_Mode", "task_1.py"), "Task 1: Mean, Median & Mode Analysis"),
        (os.path.join(base_dir, "Task_2_Variance_Standard_Deviation", "task_2.py"), "Task 2: Variance & Standard Deviation"),
        (os.path.join(base_dir, "Task_3_Correlation_Probability", "task_3.py"), "Task 3: Correlation & Probability Analysis"),
        (os.path.join(base_dir, "Task_4_Outlier_Detection", "task_4.py"), "Task 4: Outlier Detection (IQR & Z-Score)"),
        (os.path.join(base_dir, "Task_5_Matplotlib_Visualization", "task_5.py"), "Task 5: Matplotlib Data Visualizations"),
        (os.path.join(base_dir, "Task_6_Seaborn_Visualization", "task_6.py"), "Task 6: Seaborn Advanced Visualizations"),
        (os.path.join(base_dir, "Task_7_EDA_Inspection_Cleaning", "task_7.py"), "Task 7: EDA Data Inspection & Cleaning"),
        (os.path.join(base_dir, "Task_8_EDA_Correlation_Insights", "task_8.py"), "Task 8: EDA Correlation & Data Insights"),
        (os.path.join(base_dir, "Task_9_Business_Recommendations", "task_9.py"), "Task 9: Strategic Business Recommendations")
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
    report_script = os.path.join(base_dir, "generate_report.py")
    if os.path.exists(report_script):
        ok = run_script(report_script, "Master Step: PDF Report Generation")
        if ok:
            success_count += 1

    total_time = time.time() - start_time
    print("\n" + "*" * 80)
    print(f"PIPELINE COMPLETED! {success_count}/{len(pipeline) + (1 if os.path.exists(report_script) else 0)} steps executed successfully.")
    print(f"Total Pipeline Runtime: {total_time:.2f} seconds.")
    print("*" * 80 + "\n")

if __name__ == "__main__":
    main()
