"""
Task 5: Data Visualization using Matplotlib
Internship: Data Analytics - Week 4
Student: Ayush | Prestige Institute of Engineering, Management & Research, Indore
Objective: Create 5 publication-quality customized Matplotlib charts:
           1. Line Plot (Spend Progression by Customer Order Frequency)
           2. Bar Plot (City-wise Average Annual Income and Total Spend)
           3. Pie Chart (Customer Distribution by Churn Risk Segment)
           4. Histogram (Annual Income Distribution with Mean & Median markers)
           5. Scatter Plot (Income vs. Total Spend with OLS Trendline)
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run_task_5():
    print("=" * 75)
    print("WEEK 4 - TASK 5: DATA VISUALIZATION USING MATPLOTLIB")
    print("=" * 75)

    # 1. Setup paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "Data", "ecommerce_customer_data.csv")
    out_dir = os.path.join(base_dir, "Visualizations", "matplotlib")
    os.makedirs(out_dir, exist_ok=True)

    df = pd.read_csv(data_path)
    print(f"Loaded {len(df)} records for Matplotlib visualization.")

    # Global Matplotlib Styling Configuration
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    plt.rcParams["font.sans-serif"] = "DejaVu Sans"
    plt.rcParams["axes.edgecolor"] = "#CBD5E1"
    plt.rcParams["axes.linewidth"] = 0.8

    # -------------------------------------------------------------
    # 1. LINE PLOT: Average Spend by Purchase Frequency Tier
    # -------------------------------------------------------------
    print("\n[1/5] Generating Line Plot...")
    freq_grouped = df.groupby("Purchase_Frequency")["Total_Spend"].mean().reset_index()
    freq_grouped = freq_grouped.sort_values("Purchase_Frequency")

    fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
    ax.plot(
        freq_grouped["Purchase_Frequency"],
        freq_grouped["Total_Spend"],
        color="#1E40AF",
        marker="o",
        linewidth=2.5,
        markersize=6,
        markerfacecolor="#3B82F6",
        markeredgecolor="#1E40AF",
        label="Mean Total Spend (INR)"
    )
    # Fill under curve for modern look
    ax.fill_between(freq_grouped["Purchase_Frequency"], freq_grouped["Total_Spend"], color="#93C5FD", alpha=0.3)
    ax.set_title("Customer Spend Trend by Annual Purchase Frequency", fontsize=14, fontweight="bold", pad=14, color="#0F172A")
    ax.set_xlabel("Annual Purchase Frequency (Orders / Year)", fontsize=11, fontweight="bold", labelpad=8, color="#334155")
    ax.set_ylabel("Mean Total Spend (INR)", fontsize=11, fontweight="bold", labelpad=8, color="#334155")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(frameon=True, facecolor="white", edgecolor="#E2E8F0", loc="upper left")
    
    line_path = os.path.join(out_dir, "line_plot_spend_trend.png")
    fig.tight_layout()
    fig.savefig(line_path, dpi=300)
    plt.close(fig)
    print(f"  -> Saved: {line_path}")

    # -------------------------------------------------------------
    # 2. BAR PLOT: City-wise Average Total Spend & Income
    # -------------------------------------------------------------
    print("[2/5] Generating Bar Plot...")
    city_grouped = df.groupby("City")[["Total_Spend", "Annual_Income_k"]].mean().reset_index()
    city_grouped = city_grouped.sort_values("Total_Spend", ascending=False)

    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=300)
    colors = ["#0284C7", "#0EA5E9", "#38BDF8", "#7DD3FC", "#BAE6FD"]
    bars = ax.bar(city_grouped["City"], city_grouped["Total_Spend"], color=colors[:len(city_grouped)], edgecolor="#0369A1", width=0.55)
    
    # Value annotations on bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2.0,
            yval + 800,
            f"INR {yval:,.0f}",
            ha="center",
            va="bottom",
            fontsize=9.5,
            fontweight="bold",
            color="#0F172A"
        )

    ax.set_title("Average Customer Annual Spend Across Major Metro Hubs", fontsize=14, fontweight="bold", pad=14, color="#0F172A")
    ax.set_xlabel("Metropolitan City", fontsize=11, fontweight="bold", labelpad=8, color="#334155")
    ax.set_ylabel("Average Total Spend (INR)", fontsize=11, fontweight="bold", labelpad=8, color="#334155")
    ax.set_ylim(0, city_grouped["Total_Spend"].max() * 1.15)
    ax.grid(axis="y", linestyle="--", alpha=0.6)

    bar_path = os.path.join(out_dir, "bar_plot_city_spending.png")
    fig.tight_layout()
    fig.savefig(bar_path, dpi=300)
    plt.close(fig)
    print(f"  -> Saved: {bar_path}")

    # -------------------------------------------------------------
    # 3. PIE CHART: Customer Churn Risk Proportions
    # -------------------------------------------------------------
    print("[3/5] Generating Pie Chart...")
    churn_counts = df["Churn_Risk"].value_counts()
    churn_labels = churn_counts.index.tolist()
    churn_values = churn_counts.values.tolist()
    pie_colors = ["#EF4444", "#F59E0B", "#10B981"] # High (red), Medium (amber), Low (emerald)
    explode = (0.06, 0.02, 0.02) # Emphasize high risk

    fig, ax = plt.subplots(figsize=(7.5, 5.5), dpi=300)
    wedges, texts, autotexts = ax.pie(
        churn_values,
        labels=churn_labels,
        autopct="%1.1f%%",
        startangle=140,
        colors=pie_colors,
        explode=explode,
        shadow=True,
        wedgeprops=dict(width=0.85, edgecolor="#FFFFFF", linewidth=2)
    )
    for t in texts:
        t.set_fontsize(11)
        t.set_fontweight("bold")
        t.set_color("#0F172A")
    for at in autotexts:
        at.set_fontsize(10.5)
        at.set_fontweight("bold")
        at.set_color("white")

    ax.set_title("Customer Portfolio Segmentation by Churn Risk Level", fontsize=14, fontweight="bold", pad=16, color="#0F172A")
    
    pie_path = os.path.join(out_dir, "pie_chart_churn_risk.png")
    fig.tight_layout()
    fig.savefig(pie_path, dpi=300)
    plt.close(fig)
    print(f"  -> Saved: {pie_path}")

    # -------------------------------------------------------------
    # 4. HISTOGRAM: Annual Income Distribution with Mean/Median Lines
    # -------------------------------------------------------------
    print("[4/5] Generating Histogram...")
    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=300)
    n, bins, patches = ax.hist(
        df["Annual_Income_k"],
        bins=14,
        color="#6366F1",
        edgecolor="#4338CA",
        alpha=0.75,
        rwidth=0.9
    )
    income_mean = df["Annual_Income_k"].mean()
    income_median = df["Annual_Income_k"].median()

    ax.axvline(income_mean, color="#DC2626", linestyle="--", linewidth=2, label=f"Mean: {income_mean:.1f}k")
    ax.axvline(income_median, color="#059669", linestyle="-.", linewidth=2, label=f"Median: {income_median:.1f}k")

    ax.set_title("Customer Annual Income Distribution (with Central Tendency Markers)", fontsize=14, fontweight="bold", pad=14, color="#0F172A")
    ax.set_xlabel("Annual Income (in Thousand INR)", fontsize=11, fontweight="bold", labelpad=8, color="#334155")
    ax.set_ylabel("Customer Count (Frequency)", fontsize=11, fontweight="bold", labelpad=8, color="#334155")
    ax.legend(frameon=True, facecolor="white", edgecolor="#E2E8F0", loc="upper right")
    ax.grid(axis="y", linestyle="--", alpha=0.6)

    hist_path = os.path.join(out_dir, "histogram_income_distribution.png")
    fig.tight_layout()
    fig.savefig(hist_path, dpi=300)
    plt.close(fig)
    print(f"  -> Saved: {hist_path}")

    # -------------------------------------------------------------
    # 5. SCATTER PLOT: Annual Income vs Total Spend with Trendline
    # -------------------------------------------------------------
    print("[5/5] Generating Scatter Plot...")
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    
    # Scatter points colored by spending score
    scatter = ax.scatter(
        df["Annual_Income_k"],
        df["Total_Spend"],
        c=df["Spending_Score"],
        cmap="viridis",
        s=65,
        alpha=0.85,
        edgecolors="#334155",
        linewidths=0.6
    )
    
    # Linear Regression fit
    m, b = np.polyfit(df["Annual_Income_k"], df["Total_Spend"], 1)
    x_vals = np.linspace(df["Annual_Income_k"].min(), df["Annual_Income_k"].max(), 100)
    ax.plot(x_vals, m * x_vals + b, color="#DC2626", linewidth=2, linestyle="--", label=f"Trendline (y = {m:.1f}x + {b:,.0f})")

    cbar = fig.colorbar(scatter, ax=ax, pad=0.02)
    cbar.set_label("Spending Score (1 - 100)", fontsize=10, fontweight="bold", labelpad=8)

    ax.set_title("Correlation Analysis: Customer Annual Income vs. Total Spend", fontsize=14, fontweight="bold", pad=14, color="#0F172A")
    ax.set_xlabel("Annual Income (in Thousand INR)", fontsize=11, fontweight="bold", labelpad=8, color="#334155")
    ax.set_ylabel("Total Annual Spend (INR)", fontsize=11, fontweight="bold", labelpad=8, color="#334155")
    ax.legend(frameon=True, facecolor="white", edgecolor="#E2E8F0", loc="upper left")
    ax.grid(True, linestyle="--", alpha=0.6)

    scatter_path = os.path.join(out_dir, "scatter_plot_income_vs_spend.png")
    fig.tight_layout()
    fig.savefig(scatter_path, dpi=300)
    plt.close(fig)
    print(f"  -> Saved: {scatter_path}")

    print("=" * 75)
    print("TASK 5 COMPLETED SUCCESSFULLY! All 5 Matplotlib figures created.")
    print("=" * 75 + "\n")

if __name__ == "__main__":
    run_task_5()
