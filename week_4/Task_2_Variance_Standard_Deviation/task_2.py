"""
Task 2: Variance & Standard Deviation Analysis
Internship: Data Analytics - Week 4
Student: Ayush | Prestige Institute of Engineering, Management & Research, Indore
Objective: Calculate and interpret Variance, Standard Deviation (Sample vs Population),
           and Coefficient of Variation (CV) to understand data spread and dispersion.
"""

import os
import numpy as np
import pandas as pd

def run_task_2():
    print("=" * 75)
    print("WEEK 4 - TASK 2: VARIANCE & STANDARD DEVIATION (MEASURES OF DISPERSION)")
    print("=" * 75)

    # 1. Load dataset
    data_path = os.path.join(os.path.dirname(__file__), "..", "Data", "ecommerce_customer_data.csv")
    df = pd.read_csv(data_path)
    print(f"Loaded {len(df)} records from {data_path}\n")

    # 2. Select numerical columns
    cols = [
        "Annual_Income_k",
        "Spending_Score",
        "Total_Spend",
        "Website_Time_Mins",
        "Age"
    ]

    results = []

    print("-" * 75)
    print(f"{'Feature':<18} | {'Mean':>9} | {'Sample Var':>12} | {'Sample Std':>10} | {'CV (%)':>8}")
    print("-" * 75)

    for c in cols:
        s = df[c].dropna()
        mean_val = float(s.mean())
        
        # Sample variance (ddof=1) vs Population variance (ddof=0)
        sample_var = float(s.var(ddof=1))
        pop_var = float(s.var(ddof=0))
        
        # Sample std (ddof=1) vs Population std (ddof=0)
        sample_std = float(s.std(ddof=1))
        pop_std = float(s.std(ddof=0))
        
        # Coefficient of Variation (Relative standard deviation)
        cv = (sample_std / mean_val) * 100 if mean_val != 0 else 0.0

        results.append({
            "Feature": c,
            "Mean": round(mean_val, 2),
            "Sample_Var": round(sample_var, 2),
            "Pop_Var": round(pop_var, 2),
            "Sample_Std": round(sample_std, 2),
            "Pop_Std": round(pop_std, 2),
            "CV_Percent": round(cv, 2)
        })

        print(f"{c:<18} | {mean_val:>9.2f} | {sample_var:>12.2f} | {sample_std:>10.2f} | {cv:>7.2f}%")

    print("-" * 75)
    print("\nDetailed Dispersion Interpretations:")
    print("---------------------------------------------------------------------------")
    print("1. What does High Standard Deviation Mean?")
    print("   - High standard deviation (e.g., Total_Spend std = ~17,600 or CV = 46.5%) indicates that customer values are spread out over a very wide range.")
    print("   - In business terms: Customers exhibit vastly heterogeneous spending behaviors; there are budget buyers and high-rolling VIP spenders.")
    print("\n2. What does Low Standard Deviation Mean?")
    print("   - Low standard deviation / lower relative dispersion (e.g., Website_Time_Mins std = ~14.1 mins) indicates that observations cluster closely around the average.")
    print("   - In business terms: Customer session lengths are relatively consistent, predictable, and uniform across user cohorts.")
    print("\n3. Why Understanding Data Spread is Vital for Analytics:")
    print("   - The Mean alone can be misleading: Two customer segments could both have an average spend of $1,000, yet one segment spends between $950-$1,050 (low risk, predictable) while the other spends between $50-$3,000 (high variance, volatile inventory demand).")
    print("   - Variance and Standard Deviation quantify the uncertainty, volatility, and dispersion essential for risk management and customer segmentation.")

    # Save summary report for report generator
    summary_path = os.path.join(os.path.dirname(__file__), "task_2_summary.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("TASK 2: VARIANCE AND STANDARD DEVIATION SUMMARY\n")
        f.write("=" * 60 + "\n\n")
        for r in results:
            f.write(f"Feature: {r['Feature']}\n")
            f.write(f"  Mean: {r['Mean']}\n")
            f.write(f"  Sample Variance (s^2, ddof=1): {r['Sample_Var']}\n")
            f.write(f"  Population Variance (sigma^2, ddof=0): {r['Pop_Var']}\n")
            f.write(f"  Sample Standard Deviation (s, ddof=1): {r['Sample_Std']}\n")
            f.write(f"  Population Standard Deviation (sigma, ddof=0): {r['Pop_Std']}\n")
            f.write(f"  Coefficient of Variation: {r['CV_Percent']}%\n\n")
    print(f"\nTask 2 summary saved to: {summary_path}")
    print("=" * 75)
    print("TASK 2 COMPLETED SUCCESSFULLY!\n")

if __name__ == "__main__":
    run_task_2()
