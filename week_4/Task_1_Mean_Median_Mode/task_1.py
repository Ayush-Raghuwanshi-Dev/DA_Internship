"""
Task 1: Statistical Analysis - Mean, Median & Mode
Internship: Data Analytics - Week 4
Student: Ayush | Prestige Institute of Engineering, Management & Research, Indore
Objective: Calculate and interpret central tendency measures (Mean, Median, Mode)
           across key customer numerical attributes.
"""

import os
import numpy as np
import pandas as pd
from scipy import stats

def run_task_1():
    print("=" * 70)
    print("WEEK 4 - TASK 1: STATISTICAL ANALYSIS (MEAN, MEDIAN & MODE)")
    print("=" * 70)

    # 1. Load the dataset
    data_path = os.path.join(os.path.dirname(__file__), "..", "Data", "ecommerce_customer_data.csv")
    df = pd.read_csv(data_path)
    print(f"Dataset successfully loaded from: {data_path}")
    print(f"Total Records: {len(df)}, Total Features: {df.shape[1]}\n")

    # 2. Select numerical columns for central tendency analysis
    numerical_cols = [
        "Annual_Income_k",
        "Spending_Score",
        "Total_Spend",
        "Website_Time_Mins",
        "Age"
    ]

    results = []

    print("-" * 70)
    print(f"{'Feature':<20} | {'Mean':>10} | {'Median':>10} | {'Mode':>10} | {'Skewness':>12}")
    print("-" * 70)

    for col in numerical_cols:
        series = df[col].dropna()
        
        # Calculate Mean
        col_mean = float(series.mean())
        
        # Calculate Median
        col_median = float(series.median())
        
        # Calculate Mode using scipy.stats or pandas
        mode_res = series.mode()
        col_mode = float(mode_res.iloc[0]) if not mode_res.empty else np.nan
        
        # Skewness to understand shape
        col_skew = float(series.skew())
        skew_type = "Symmetric" if abs(col_skew) < 0.2 else ("Right-Skewed" if col_skew > 0 else "Left-Skewed")

        results.append({
            "Feature": col,
            "Mean": round(col_mean, 2),
            "Median": round(col_median, 2),
            "Mode": round(col_mode, 2),
            "Skewness": round(col_skew, 2),
            "Shape": skew_type
        })

        print(f"{col:<20} | {col_mean:>10.2f} | {col_median:>10.2f} | {col_mode:>10.2f} | {col_skew:>8.2f} ({skew_type[:5]})")

    print("-" * 70)
    print("\nDetailed Interpretations:")
    for r in results:
        feat = r['Feature']
        mean = r['Mean']
        median = r['Median']
        mode = r['Mode']
        shape = r['Shape']
        print(f"\n* Feature: {feat}")
        print(f"  - Mean = {mean}: Represents the arithmetic average. It incorporates every observation but is sensitive to extreme values.")
        print(f"  - Median = {median}: Represents the true 50th percentile (middle customer). 50% of customers fall below this and 50% above.")
        print(f"  - Mode = {mode}: Represents the most frequently observed value in the sample.")
        if shape == "Right-Skewed":
            print(f"  - Distribution Shape: Right-skewed (Mean {mean} > Median {median}). Indicates a cluster of typical values with high-value positive outliers pulling the mean upwards.")
        elif shape == "Left-Skewed":
            print(f"  - Distribution Shape: Left-skewed (Mean {mean} < Median {median}). Indicates a long tail of lower values.")
        else:
            print(f"  - Distribution Shape: Approximately symmetric (Mean {mean} ~= Median {median}). Indicates a balanced, bell-shaped distribution.")

    # Save summary report for report generator
    summary_path = os.path.join(os.path.dirname(__file__), "task_1_summary.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("TASK 1: CENTRAL TENDENCY MEASURES SUMMARY\n")
        f.write("=" * 60 + "\n\n")
        for r in results:
            f.write(f"Feature: {r['Feature']}\n")
            f.write(f"  Mean: {r['Mean']}\n")
            f.write(f"  Median: {r['Median']}\n")
            f.write(f"  Mode: {r['Mode']}\n")
            f.write(f"  Skewness: {r['Skewness']} ({r['Shape']})\n\n")
    print(f"\nTask 1 summary saved to: {summary_path}")
    print("=" * 70)
    print("TASK 1 COMPLETED SUCCESSFULLY!\n")

if __name__ == "__main__":
    run_task_1()
