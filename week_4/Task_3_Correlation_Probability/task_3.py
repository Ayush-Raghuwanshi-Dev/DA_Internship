"""
Task 3: Correlation & Probability Analysis
Internship: Data Analytics - Week 4
Student: Ayush | Prestige Institute of Engineering, Management & Research, Indore
Objective: Calculate Pearson & Spearman correlation coefficients, interpret linear relationships,
           and compute marginal, joint, and conditional probabilities for business decision-making.
"""

import os
import numpy as np
import pandas as pd
from scipy import stats

def run_task_3():
    print("=" * 75)
    print("WEEK 4 - TASK 3: CORRELATION & PROBABILITY ANALYSIS")
    print("=" * 75)

    # 1. Load dataset
    data_path = os.path.join(os.path.dirname(__file__), "..", "Data", "ecommerce_customer_data.csv")
    df = pd.read_csv(data_path)
    print(f"Loaded {len(df)} records from {data_path}\n")

    # 2. Correlation Analysis
    pairs = [
        ("Annual_Income_k", "Total_Spend", "Customer Income vs Overall Spending"),
        ("Website_Time_Mins", "Spending_Score", "Website Browsing Time vs Spending Score"),
        ("Age", "Total_Spend", "Customer Age vs Total Spending")
    ]

    print("PART A: CORRELATION COEFFICIENT ANALYSIS")
    print("-" * 75)
    print(f"{'Variable Pair':<35} | {'Pearson r':>10} | {'p-value':>10} | {'Spearman rho':>12}")
    print("-" * 75)

    corr_results = []
    for var1, var2, desc in pairs:
        s1 = df[var1].dropna()
        s2 = df[var2].dropna()
        
        # Pearson correlation
        r_pearson, p_pearson = stats.pearsonr(s1, s2)
        
        # Spearman correlation
        rho_spearman, p_spearman = stats.spearmanr(s1, s2)

        # Interpret direction and strength
        direction = "Positive" if r_pearson > 0 else ("Negative" if r_pearson < 0 else "Zero")
        abs_r = abs(r_pearson)
        if abs_r >= 0.7:
            strength = "Strong"
        elif abs_r >= 0.4:
            strength = "Moderate"
        elif abs_r >= 0.2:
            strength = "Weak"
        else:
            strength = "Negligible / Very Weak"

        corr_results.append({
            "Pair": f"{var1} & {var2}",
            "Description": desc,
            "Pearson_r": round(r_pearson, 4),
            "p_value": round(p_pearson, 6),
            "Spearman_rho": round(rho_spearman, 4),
            "Direction": direction,
            "Strength": strength
        })

        print(f"{var1[:15]} & {var2[:15]:<16} | {r_pearson:>10.4f} | {p_pearson:>10.4e} | {rho_spearman:>12.4f}")

    print("-" * 75)
    print("\nCorrelation Interpretations:")
    for cr in corr_results:
        print(f"* {cr['Pair']} ({cr['Description']}):")
        print(f"  - Pearson r = {cr['Pearson_r']} (p = {cr['p_value']:.4e})")
        print(f"  - Relationship: {cr['Strength']} {cr['Direction']} correlation.")
        if cr['Pearson_r'] > 0.4:
            print(f"  - Business Insight: Proportional increase confirmed. Higher {cr['Pair'].split(' & ')[0]} directly translates to higher {cr['Pair'].split(' & ')[1]}.")
        elif cr['Pearson_r'] < -0.2:
            print(f"  - Business Insight: Inverse trend observed.")
        else:
            print(f"  - Business Insight: Near zero correlation indicates independent or non-linear behavior.")

    # 3. Probability Calculations
    print("\n" + "=" * 75)
    print("PART B: PROBABILITY CALCULATIONS")
    print("=" * 75)

    n_total = len(df)

    # Event A: High Value Customer (Total_Spend > 40,000)
    high_spenders = df[df["Total_Spend"] > 40000]
    p_high_spend = len(high_spenders) / n_total

    # Event B: At-Risk of Churn (Churn_Risk == "High")
    churn_customers = df[df["Churn_Risk"] == "High"]
    p_churn = len(churn_customers) / n_total

    # Event C: Low Engagement / Low Spending Score (Spending_Score < 40)
    low_score_customers = df[df["Spending_Score"] < 40]
    p_low_score = len(low_score_customers) / n_total

    # Conditional Probability: P(Churn_Risk == "High" | Spending_Score < 40)
    churn_given_low_score = df[(df["Spending_Score"] < 40) & (df["Churn_Risk"] == "High")]
    p_churn_given_low_score = len(churn_given_low_score) / len(low_score_customers) if len(low_score_customers) > 0 else 0

    # Conditional Probability: P(Churn_Risk == "High" | Spending_Score >= 40)
    high_score_customers = df[df["Spending_Score"] >= 40]
    churn_given_high_score = df[(df["Spending_Score"] >= 40) & (df["Churn_Risk"] == "High")]
    p_churn_given_high_score = len(churn_given_high_score) / len(high_score_customers) if len(high_score_customers) > 0 else 0

    print(f"Total Sample Size (N): {n_total} customers")
    print(f"1. Marginal Probability P(Total_Spend > $40,000): {len(high_spenders)}/{n_total} = {p_high_spend:.4f} ({p_high_spend*100:.2f}%)")
    print(f"2. Marginal Probability P(Churn_Risk = 'High'): {len(churn_customers)}/{n_total} = {p_churn:.4f} ({p_churn*100:.2f}%)")
    print(f"3. Marginal Probability P(Spending_Score < 40): {len(low_score_customers)}/{n_total} = {p_low_score:.4f} ({p_low_score*100:.2f}%)")
    print(f"4. Conditional Probability P(Churn='High' | Spending_Score < 40): {len(churn_given_low_score)}/{len(low_score_customers)} = {p_churn_given_low_score:.4f} ({p_churn_given_low_score*100:.2f}%)")
    print(f"5. Conditional Probability P(Churn='High' | Spending_Score >= 40): {len(churn_given_high_score)}/{len(high_score_customers)} = {p_churn_given_high_score:.4f} ({p_churn_given_high_score*100:.2f}%)")
    
    risk_multiplier = (p_churn_given_low_score / p_churn_given_high_score) if p_churn_given_high_score > 0 else 0
    print(f"   => Key Probability Finding: Customers with low spending scores (<40) are {risk_multiplier:.2f}x more likely to churn into high risk!")

    # 4. Usefulness of Probability in Data Analytics
    print("\n" + "-" * 75)
    print("Why Probability is Essential in Data Analytics:")
    print("---------------------------------------------------------------------------")
    print("1. Decision Making Under Uncertainty: Business environments are inherently uncertain. Probability quantifies risk and likelihood rather than relying on guesswork.")
    print("2. Predictive Modeling & Machine Learning: Classification algorithms (Logistic Regression, Naive Bayes, Random Forests) output class probabilities (e.g., probability of churn or fraud).")
    print("3. A/B Testing & Hypothesis Testing: P-values and confidence intervals determine whether an observed uplift in conversion rate is statistically significant or merely random chance.")
    print("4. Customer Lifetime Value (CLV) & Risk Scoring: Conditional probabilities allow businesses to segment customers dynamically and trigger automated retention campaigns for high-risk cohorts.")

    # Save summary
    summary_path = os.path.join(os.path.dirname(__file__), "task_3_summary.txt")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("TASK 3: CORRELATION & PROBABILITY SUMMARY\n")
        f.write("=" * 60 + "\n\n")
        f.write("A. CORRELATIONS:\n")
        for cr in corr_results:
            f.write(f"- {cr['Pair']} ({cr['Description']}):\n")
            f.write(f"  Pearson r = {cr['Pearson_r']} (p = {cr['p_value']:.4e})\n")
            f.write(f"  Spearman rho = {cr['Spearman_rho']}\n")
            f.write(f"  Interpretation: {cr['Strength']} {cr['Direction']}\n\n")
        f.write("B. PROBABILITY CALCULATIONS:\n")
        f.write(f"- P(Total_Spend > $40k): {p_high_spend*100:.2f}%\n")
        f.write(f"- P(Churn_Risk = 1): {p_churn*100:.2f}%\n")
        f.write(f"- P(Churn | Spending_Score < 40): {p_churn_given_low_score*100:.2f}%\n")
        f.write(f"- P(Churn | Spending_Score >= 40): {p_churn_given_high_score*100:.2f}%\n")
        f.write(f"- Risk Multiplier: {risk_multiplier:.2f}x\n")
    print(f"\nTask 3 summary saved to: {summary_path}")
    print("=" * 75)
    print("TASK 3 COMPLETED SUCCESSFULLY!\n")

if __name__ == "__main__":
    run_task_3()
