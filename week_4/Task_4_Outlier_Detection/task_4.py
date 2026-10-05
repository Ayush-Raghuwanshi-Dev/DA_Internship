"""
Task 4: Outlier Detection (IQR and Z-Score Methods)
Internship: Data Analytics - Week 4
Student: Ayush | Prestige Institute of Engineering, Management & Research, Indore
Objective: Detect, display, and interpret outliers using Interquartile Range (IQR)
           and Z-score statistical methods; evaluate business impact and handling strategies.
"""

import os
import numpy as np
import pandas as pd
from scipy import stats

def run_task_4():
    print("=" * 80)
    print("WEEK 4 - TASK 4: OUTLIER DETECTION (IQR & Z-SCORE METHODS)")
    print("=" * 80)

    # 1. Load dataset
    data_path = os.path.join(os.path.dirname(__file__), "..", "Data", "ecommerce_customer_data.csv")
    df = pd.read_csv(data_path)
    print(f"Loaded {len(df)} records from {data_path}\n")

    features_to_check = ["Annual_Income_k", "Total_Spend"]

    outlier_records = {}

    for feat in features_to_check:
        series = df[feat]
        
        # --- METHOD 1: IQR METHOD ---
        q1 = float(series.quantile(0.25))
        q3 = float(series.quantile(0.75))
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        iqr_outliers = df[(series < lower_bound) | (series > upper_bound)]

        # --- METHOD 2: Z-SCORE METHOD ---
        mean_val = float(series.mean())
        std_val = float(series.std(ddof=1))
        z_scores = (series - mean_val) / std_val
        z_outliers = df[abs(z_scores) > 2.5]

        print("-" * 80)
        print(f"OUTLIER ANALYSIS FOR FEATURE: {feat.upper()}")
        print("-" * 80)
        print(f"Statistical Summary: Mean={mean_val:.2f}, Std={std_val:.2f}")
        print(f"IQR Parameters: Q1 (25%) = {q1:.2f} | Q3 (75%) = {q3:.2f} | IQR = {iqr:.2f}")
        print(f"IQR Fences: Lower Fence = {lower_bound:.2f} | Upper Fence = {upper_bound:.2f}")
        print(f"Total Outliers Identified via IQR (factor=1.5): {len(iqr_outliers)}")
        print(f"Total Outliers Identified via Z-Score (|Z| > 2.5): {len(z_outliers)}")
        print("\nIdentified Outlier Records (IQR Method):")
        
        if not iqr_outliers.empty:
            display_cols = ["Customer_ID", "City", "Age", feat]
            for idx, row in iqr_outliers.iterrows():
                val = row[feat]
                z = (val - mean_val) / std_val
                status = "Upper Outlier" if val > upper_bound else "Lower Outlier"
                print(f"  * ID: {row['Customer_ID']} | City: {row['City']:<10} | Age: {row['Age']} | {feat}: {val:.2f} | Z-Score: {z:+.2f} ({status})")
        else:
            print("  None detected.")

        outlier_records[feat] = {
            "Q1": round(q1, 2),
            "Q3": round(q3, 2),
            "IQR": round(iqr, 2),
            "Lower_Fence": round(lower_bound, 2),
            "Upper_Fence": round(upper_bound, 2),
            "IQR_Count": len(iqr_outliers),
            "Z_Count": len(z_outliers),
            "Outlier_IDs": iqr_outliers["Customer_ID"].tolist()
        }
        print()

    # Discussion & Analytical Explanations
    print("=" * 80)
    print("CRITICAL ANALYTICAL DISCUSSION: OUTLIER MANAGEMENT IN DATA SCIENCE")
    print("=" * 80)
    print("1. Why is Outlier Detection Essential in Data Analytics?")
    print("   - Distorts Central Tendency: The arithmetic mean is heavily pulled toward extreme values, misrepresenting the 'typical' customer.")
    print("   - Inflates Variance: Standard deviation and sum of squared errors explode, causing false alarms in risk models.")
    print("   - Violates Model Assumptions: Linear regression and Ordinary Least Squares (OLS) assume normality of residuals; outliers create massive leverage points that tilt the regression line.")
    print("\n2. Should Outliers Always Be Removed or Kept?")
    print("   - NEVER automatically delete outliers without contextual investigation!")
    print("   - Scenario A: REMOVE if they represent data corruption, recording errors, or system malfunctions (e.g. Age = 999 or Total Spend = -500).")
    print("   - Scenario B: KEEP if they represent authentic, legitimate business reality (e.g. VIP customers spending INR 145,000 or ultra-high-net-worth buyers).")
    print("     Deleting legitimate high-spenders biases commercial models, understates revenue potential, and blinds businesses to high-value opportunities.")
    print("\n3. Recommended Best Practices for Outlier Handling:")
    print("   - Robust Metrics: Use Median and IQR instead of Mean and Standard Deviation.")
    print("   - Winsorization (Capping): Clip extreme values at the 1st and 99th percentiles rather than dropping data rows.")
    print("   - Data Transformation: Apply Logarithmic or Box-Cox transformations to compress heavy right tails.")
    print("   - Segmented Modeling: Isolate extreme VIP customers into a dedicated high-touch tier for specialized premium marketing.")

    # Save summary
    summary_path = os.path.join(os.path.dirname(__file__), "task_4_summary.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("TASK 4: OUTLIER DETECTION SUMMARY\n")
        f.write("=" * 60 + "\n\n")
        for feat, data in outlier_records.items():
            f.write(f"Feature: {feat}\n")
            f.write(f"  Q1: {data['Q1']}, Q3: {data['Q3']}, IQR: {data['IQR']}\n")
            f.write(f"  Fences: [{data['Lower_Fence']} to {data['Upper_Fence']}]\n")
            f.write(f"  IQR Outliers Detected: {data['IQR_Count']} customers\n")
            f.write(f"  Z-Score Outliers Detected: {data['Z_Count']} customers\n")
            f.write(f"  Customer IDs: {', '.join(data['Outlier_IDs'])}\n\n")
    print(f"\nTask 4 summary saved to: {summary_path}")
    print("=" * 80)
    print("TASK 4 COMPLETED SUCCESSFULLY!\n")

if __name__ == "__main__":
    run_task_4()
