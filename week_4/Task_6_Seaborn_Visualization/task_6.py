"""
Task 6: Advanced Data Visualization using Seaborn
Internship: Data Analytics - Week 4
Student: Ayush | Prestige Institute of Engineering, Management & Research, Indore
Objective: Create 4 advanced Seaborn visualizations:
           1. Countplot (Customer counts by City categorized by Gender)
           2. Boxplot (Annual Income and Total Spend across Churn Risk levels)
           3. Heatmap (Correlation Matrix of numerical features with annotations)
           4. Pairplot (Multivariate pairwise relationships colored by Churn Risk)
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_task_6():
    print("=" * 75)
    print("WEEK 4 - TASK 6: ADVANCED DATA VISUALIZATION USING SEABORN")
    print("=" * 75)

    # 1. Setup paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "Data", "ecommerce_customer_data.csv")
    out_dir = os.path.join(base_dir, "Visualizations", "seaborn")
    os.makedirs(out_dir, exist_ok=True)

    df = pd.read_csv(data_path)
    print(f"Loaded {len(df)} records for Seaborn visualization.")

    # Apply global Seaborn theme
    sns.set_theme(style="whitegrid", font="sans-serif")
    palette = sns.color_palette("muted")

    # -------------------------------------------------------------
    # 1. COUNTPLOT: Customer Count Across Cities by Gender
    # -------------------------------------------------------------
    print("\n[1/4] Generating Seaborn Countplot...")
    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=300)
    sns.countplot(
        data=df,
        x="City",
        hue="Gender",
        palette=["#3B82F6", "#EC4899"], # Blue for Male, Pink for Female
        edgecolor="#1E293B",
        ax=ax
    )
    # Add count labels on top of bars
    for p in ax.patches:
        height = p.get_height()
        if not np.isnan(height) and height > 0:
            ax.annotate(
                f"{int(height)}",
                (p.get_x() + p.get_width() / 2., height),
                ha="center", va="bottom",
                fontsize=9.5, fontweight="bold",
                xytext=(0, 3), textcoords="offset points"
            )

    ax.set_title("Customer Demographic Distribution: City vs. Gender", fontsize=14, fontweight="bold", pad=14, color="#0F172A")
    ax.set_xlabel("Metropolitan City", fontsize=11, fontweight="bold", labelpad=8)
    ax.set_ylabel("Customer Count", fontsize=11, fontweight="bold", labelpad=8)
    ax.legend(title="Gender", frameon=True, facecolor="white", edgecolor="#E2E8F0")

    countplot_path = os.path.join(out_dir, "countplot_city_gender.png")
    fig.tight_layout()
    fig.savefig(countplot_path, dpi=300)
    plt.close(fig)
    print(f"  -> Saved: {countplot_path}")

    # -------------------------------------------------------------
    # 2. BOXPLOT: Total Spend Distribution by Churn Risk
    # -------------------------------------------------------------
    print("[2/4] Generating Seaborn Boxplot...")
    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=300)
    sns.boxplot(
        data=df,
        x="Churn_Risk",
        y="Total_Spend",
        order=["Low", "Medium", "High"],
        palette=["#10B981", "#F59E0B", "#EF4444"], # Emerald, Amber, Rose
        width=0.45,
        fliersize=5,
        flierprops=dict(marker="o", markerfacecolor="#EF4444", markeredgecolor="#7F1D1D"),
        ax=ax
    )
    # Overlay slight stripplot for data density
    sns.stripplot(
        data=df,
        x="Churn_Risk",
        y="Total_Spend",
        order=["Low", "Medium", "High"],
        color="#0F172A",
        alpha=0.35,
        jitter=0.2,
        size=4.5,
        ax=ax
    )

    ax.set_title("Distribution of Customer Total Spend across Churn Risk Segments", fontsize=14, fontweight="bold", pad=14, color="#0F172A")
    ax.set_xlabel("Churn Risk Category", fontsize=11, fontweight="bold", labelpad=8)
    ax.set_ylabel("Total Spend (INR)", fontsize=11, fontweight="bold", labelpad=8)

    boxplot_path = os.path.join(out_dir, "boxplot_spend_by_churn.png")
    fig.tight_layout()
    fig.savefig(boxplot_path, dpi=300)
    plt.close(fig)
    print(f"  -> Saved: {boxplot_path}")

    # -------------------------------------------------------------
    # 3. HEATMAP: Correlation Matrix
    # -------------------------------------------------------------
    print("[3/4] Generating Seaborn Heatmap...")
    numeric_df = df.select_dtypes(include=[np.number])
    corr = numeric_df.corr(method="pearson")

    fig, ax = plt.subplots(figsize=(9, 7), dpi=300)
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        center=0,
        linewidths=1,
        linecolor="#E2E8F0",
        cbar_kws={"shrink": 0.82, "label": "Pearson Correlation Coefficient (r)"},
        annot_kws={"fontsize": 9, "fontweight": "bold"},
        ax=ax
    )
    ax.set_title("Inter-Feature Correlation Matrix Heatmap", fontsize=14, fontweight="bold", pad=16, color="#0F172A")
    plt.xticks(rotation=45, ha="right", fontsize=9.5, fontweight="bold")
    plt.yticks(rotation=0, fontsize=9.5, fontweight="bold")

    heatmap_path = os.path.join(out_dir, "heatmap_correlation_matrix.png")
    fig.tight_layout()
    fig.savefig(heatmap_path, dpi=300)
    plt.close(fig)
    print(f"  -> Saved: {heatmap_path}")

    # -------------------------------------------------------------
    # 4. PAIRPLOT: Pairwise Relationships Across Key Features
    # -------------------------------------------------------------
    print("[4/4] Generating Seaborn Pairplot...")
    pairplot_cols = ["Annual_Income_k", "Spending_Score", "Total_Spend", "Website_Time_Mins", "Churn_Risk"]
    g = sns.pairplot(
        df[pairplot_cols],
        hue="Churn_Risk",
        hue_order=["Low", "Medium", "High"],
        palette=["#10B981", "#F59E0B", "#EF4444"],
        diag_kind="kde",
        plot_kws={"alpha": 0.7, "s": 35, "edgecolor": "none"},
        height=2.3,
        aspect=1.1
    )
    g.fig.subplots_adjust(top=0.93)
    g.fig.suptitle("Multivariate Pairplot: Pairwise Distributions by Churn Risk", fontsize=14, fontweight="bold", color="#0F172A")

    pairplot_path = os.path.join(out_dir, "pairplot_multivariate.png")
    g.savefig(pairplot_path, dpi=300)
    plt.close(g.fig)
    print(f"  -> Saved: {pairplot_path}")

    print("=" * 75)
    print("TASK 6 COMPLETED SUCCESSFULLY! All 4 Seaborn figures created.")
    print("=" * 75 + "\n")

if __name__ == "__main__":
    run_task_6()
