"""
Dataset generator for Week 4: Statistics, Data Visualization & EDA.
Generates:
1. Data/ecommerce_customer_data.csv (Clean master dataset of 120 records)
2. Data/raw_customer_data.csv and Task_7_EDA_Inspection_Cleaning/raw_customer_data.csv (Dirty dataset for Task 7)
"""

import numpy as np
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data"
TASK_7_DIR = BASE_DIR / "Task_7_EDA_Inspection_Cleaning"

DATA_DIR.mkdir(parents=True, exist_ok=True)
TASK_7_DIR.mkdir(parents=True, exist_ok=True)

# Set random seed for authentic reproducible results
np.random.seed(42)

n_samples = 120

customer_ids = [f"CUST_{1001 + i}" for i in range(n_samples)]
cities = np.random.choice(["Indore", "Bhopal", "Mumbai", "Delhi", "Bengaluru"], size=n_samples, p=[0.28, 0.22, 0.20, 0.15, 0.15])
genders = np.random.choice(["Female", "Male"], size=n_samples, p=[0.52, 0.48])
ages = np.random.randint(19, 65, size=n_samples)

# Annual Income in thousands (₹) roughly normally distributed around 65k with spread
income_k = np.random.normal(loc=65, scale=22, size=n_samples).round(1)
income_k = np.clip(income_k, 25.0, 130.0)

# Add intentional high-income outliers at indices 10 and 25
income_k[10] = 185.0
income_k[25] = 195.0

# Spending Score (1 to 100)
spending_scores = np.random.randint(8, 98, size=n_samples)

# Website time in minutes (positively correlated with spending score)
website_time = (15 + spending_scores * 0.45 + np.random.normal(0, 5, size=n_samples)).round(1)
website_time = np.clip(website_time, 8.0, 65.0)

# Purchase frequency (orders per year)
purchase_freq = np.random.poisson(lam=14, size=n_samples)
purchase_freq = np.clip(purchase_freq, 3, 36)

# Average Order Value (in ₹)
avg_order_value = (800 + income_k * 25 + np.random.normal(0, 150, size=n_samples)).round(2)

# Total Spend (in ₹)
total_spend = (purchase_freq * avg_order_value).round(2)
# Add an extreme purchase outlier at index 15
total_spend[15] = 145000.00

# Satisfaction score (1 to 5)
satisfaction = np.random.choice([1, 2, 3, 4, 5], size=n_samples, p=[0.08, 0.14, 0.28, 0.32, 0.18])

# Churn risk (derived logic: low satisfaction or low spending -> higher churn)
churn_risk = []
for sat, spend_sc in zip(satisfaction, spending_scores):
    if sat <= 2 or spend_sc < 30:
        churn_risk.append("High")
    elif sat == 3 or spend_sc < 60:
        churn_risk.append("Medium")
    else:
        churn_risk.append("Low")

clean_df = pd.DataFrame({
    "Customer_ID": customer_ids,
    "Age": ages,
    "Gender": genders,
    "City": cities,
    "Annual_Income_k": income_k,
    "Spending_Score": spending_scores,
    "Purchase_Frequency": purchase_freq,
    "Avg_Order_Value": avg_order_value,
    "Total_Spend": total_spend,
    "Website_Time_Mins": website_time,
    "Satisfaction_Score": satisfaction,
    "Churn_Risk": churn_risk
})

clean_path = DATA_DIR / "ecommerce_customer_data.csv"
clean_df.to_csv(clean_path, index=False)
print(f"Clean master dataset created: {clean_path} ({len(clean_df)} records)")

# -------------------------------------------------------------------------
# Build Raw / Dirty Dataset for Task 7 Data Inspection & Cleaning
# -------------------------------------------------------------------------
raw_df = clean_df.copy()

# 1. Introduce missing values (NaN)
np.random.seed(99)
missing_age_idx = np.random.choice(raw_df.index, size=5, replace=False)
raw_df.loc[missing_age_idx, "Age"] = np.nan

missing_inc_idx = np.random.choice(raw_df.index, size=4, replace=False)
raw_df.loc[missing_inc_idx, "Annual_Income_k"] = np.nan

missing_score_idx = np.random.choice(raw_df.index, size=3, replace=False)
raw_df.loc[missing_score_idx, "Spending_Score"] = np.nan

missing_sat_idx = np.random.choice(raw_df.index, size=4, replace=False)
raw_df.loc[missing_sat_idx, "Satisfaction_Score"] = np.nan

# 2. Inconsistent casing / labels in Gender
raw_df.loc[2, "Gender"] = "female"
raw_df.loc[7, "Gender"] = "F"
raw_df.loc[14, "Gender"] = "M"
raw_df.loc[22, "Gender"] = "male"

# 3. Invalid out-of-range values
raw_df.loc[18, "Age"] = -4
raw_df.loc[45, "Spending_Score"] = 150

# 4. Duplicate rows (append 5 duplicates)
duplicates = raw_df.iloc[[3, 11, 24, 38, 52]].copy()
raw_df = pd.concat([raw_df, duplicates], ignore_index=True)

raw_data_path1 = DATA_DIR / "raw_customer_data.csv"
raw_data_path2 = TASK_7_DIR / "raw_customer_data.csv"
raw_df.to_csv(raw_data_path1, index=False)
raw_df.to_csv(raw_data_path2, index=False)

print(f"Raw dirty dataset created: {raw_data_path1} and {raw_data_path2} ({len(raw_df)} records with intentional defects)")
