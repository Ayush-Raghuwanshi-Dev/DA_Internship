# Week 4 — Statistics, Data Visualization & Exploratory Data Analysis (EDA)

**Student:** Ayush  
**Course:** B.Tech Computer Science & Engineering (IoT)  
**College:** Prestige Institute of Engineering, Management & Research (PIEMR), Indore  
**Assignment:** Week 4 — Statistics, Data Visualization & Exploratory Data Analysis (Marks: 100)  
**Repository:** [https://github.com/Ayush-Raghuwanshi-Dev/DA_Internship.git](https://github.com/Ayush-Raghuwanshi-Dev/DA_Internship.git)  

---

## Project Overview

This repository contains the complete, verified, and automated implementation of the **Week 4 Data Analytics Internship Assignment**. The project covers foundational and advanced statistical modeling, univariate and multivariate data visualization using Matplotlib and Seaborn, systematic data inspection and cleaning pipelines, bivariate/multivariate correlation analysis, and data-grounded strategic business recommendations.

The analysis is conducted on an omnichannel **Retail E-Commerce Customer Analytics** dataset (`ecommerce_customer_data.csv`, 120 records, 12 attributes) covering demographics, financial capacity, engagement metrics, and retention status.

---

## Directory Structure

```
week_4/
│
├── Data/
│   ├── generate_datasets.py            # Automated dataset generator with intentional defects
│   ├── ecommerce_customer_data.csv     # Master clean customer dataset (120 records)
│   ├── raw_customer_data.csv           # Raw dataset with missing values, dupes & anomalies (125 records)
│   └── cleaned_customer_data.csv       # Cleaned and imputed customer dataset (119 records)
│
├── Task_1_Mean_Median_Mode/
│   ├── task_1.py                       # Central tendency calculations & skewness shape analysis
│   └── task_1_summary.txt              # Formatted statistical summary
│
├── Task_2_Variance_Standard_Deviation/
│   ├── task_2.py                       # Sample/Pop variance, standard deviation & CV%
│   └── task_2_summary.txt              # Dispersion summary & volatility interpretation
│
├── Task_3_Correlation_Probability/
│   ├── task_3.py                       # Pearson r, Spearman rho, p-values & conditional probability
│   └── task_3_summary.txt              # Correlation & churn risk probability findings
│
├── Task_4_Outlier_Detection/
│   ├── task_4.py                       # Interquartile Range (IQR) & Z-score outlier detection
│   └── task_4_summary.txt              # Outlier detection tables & treatment rationale
│
├── Task_5_Matplotlib_Visualization/
│   └── task_5.py                       # Line, Bar, Pie, Histogram & Scatter plot generation
│
├── Task_6_Seaborn_Visualization/
│   └── task_6.py                       # Countplot, Boxplot, Heatmap & Pairplot generation
│
├── Task_7_EDA_Inspection_Cleaning/
│   ├── raw_customer_data.csv           # Input contaminated raw dataset
│   ├── task_7.py                       # Systematic inspection, deduplication & imputation script
│   ├── cleaned_customer_data.csv       # Exported post-cleaning dataset
│   └── task_7_summary.txt              # Cleaning audit and retention metrics
│
├── Task_8_EDA_Correlation_Insights/
│   ├── task_8.py                       # Full correlation matrix & 3 core data-driven insights
│   └── eda_insights.txt                # Exported analytical insights
│
├── Task_9_Business_Recommendations/
│   ├── task_9.py                       # 3 actionable business strategies with ROI & implementation
│   └── business_recommendations.txt    # Executive recommendations report
│
├── Visualizations/
│   ├── matplotlib/
│   │   ├── line_plot_spend_trend.png
│   │   ├── bar_plot_city_spending.png
│   │   ├── pie_chart_churn_risk.png
│   │   ├── histogram_income_distribution.png
│   │   └── scatter_plot_income_vs_spend.png
│   └── seaborn/
│       ├── countplot_city_gender.png
│       ├── boxplot_spend_by_churn.png
│       ├── heatmap_correlation_matrix.png
│       └── pairplot_multivariate.png
│
├── requirements.txt                    # Project dependencies (NumPy, Pandas, SciPy, Matplotlib, Seaborn, ReportLab)
├── run_all_week_4.py                   # Master sequential pipeline runner
├── generate_report.py                  # ReportLab PDF report compiler
└── Week_4_Statistics_Visualization_EDA_Report.pdf # Final 19-page comprehensive submission report
```

---

## Assignment Tasks & Core Findings

| Task | Topic | Marks | Key Empirical Findings & Metrics |
|---|---|:---:|---|
| **Task 1** | Mean, Median & Mode | 10 | Total Spend Mean = INR 37,839.40 vs Median = INR 36,072.57 (+3.27 Skewness); Website Time is symmetric (Mean 38.8m ≈ Median 39.4m). |
| **Task 2** | Variance & Std Deviation | 10 | Total Spend std = INR 15,792.82 (CV = 41.74%, high spend heterogeneity); Website Time std = 12.67m (CV = 32.63%, predictable traffic). |
| **Task 3** | Correlation & Probability | 10 | Income vs Spend (r = +0.5042); Website Time vs Spend Score (r = +0.9086); P(Churn \| Spend Score < 40) = 69.23% (2.55x risk multiplier). |
| **Task 4** | Outlier Detection | 10 | IQR Upper Fence for Spend = INR 68,006.16; identified 3 upper outliers (e.g. CUST_1016 spending INR 145,000, Z = +6.79). |
| **Task 5** | Matplotlib Visualization | 15 | Generated 5 customized figures (Line, Bar, Pie, Histogram, Scatter) with custom styling and 300 DPI resolution. |
| **Task 6** | Seaborn Visualization | 15 | Generated 4 advanced figures (Countplot, Boxplot, Heatmap, Pairplot) with color palettes and density overlays. |
| **Task 7** | EDA Data Cleaning | 10 | Removed 5 duplicate rows, filtered 1 invalid age, imputed missing values (Median/Mean/Mode) with 95.2% retention. |
| **Task 8** | EDA Correlation Insights | 10 | Strongest correlation: Income vs AOV (r = +0.9698); established 3 deep data-grounded insights on digital immersion & churn. |
| **Task 9** | Business Recommendations | 10 | Formulated 3 strategic initiatives: Platinum Concierge tier, session gamification, and automated churn prevention (ROI: INR 7M+). |
| **Total** | **All Modules** | **100** | **Comprehensive 19-Page Professional PDF Report Generated.** |

---

## Visualizations Preview

All visualizations are rendered at 300 DPI and stored inside `Visualizations/`:

1. **Line Plot (`Visualizations/matplotlib/line_plot_spend_trend.png`):** Annual purchase frequency vs mean total spend.
2. **Bar Plot (`Visualizations/matplotlib/bar_plot_city_spending.png`):** Regional customer spending across Indore, Mumbai, Delhi, Bengaluru, and Pune.
3. **Pie Chart (`Visualizations/matplotlib/pie_chart_churn_risk.png`):** Customer churn risk segmentation (High: 40.8%, Medium: 36.7%, Low: 22.5%).
4. **Histogram (`Visualizations/matplotlib/histogram_income_distribution.png`):** Annual income distribution with Mean and Median markers.
5. **Scatter Plot (`Visualizations/matplotlib/scatter_plot_income_vs_spend.png`):** Income vs Total Spend colored by spending score with OLS regression line.
6. **Countplot (`Visualizations/seaborn/countplot_city_gender.png`):** Demographic count by City categorized by Gender.
7. **Boxplot (`Visualizations/seaborn/boxplot_spend_by_churn.png`):** Spend quartile distributions and fliers across Churn Risk levels.
8. **Heatmap (`Visualizations/seaborn/heatmap_correlation_matrix.png`):** Pearson correlation matrix across all numerical variables.
9. **Pairplot (`Visualizations/seaborn/pairplot_multivariate.png`):** Multivariate pairwise scatter & KDE distributions by Churn Risk.

---

## How to Execute

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Entire Automation Pipeline
To run all task modules, generate all visualizations, perform data cleaning, and build the PDF report:
```bash
python run_all_week_4.py
```

### 3. Run Individual Tasks
```bash
# Task 1: Mean, Median, Mode
python Task_1_Mean_Median_Mode/task_1.py

# Task 2: Variance & Standard Deviation
python Task_2_Variance_Standard_Deviation/task_2.py

# Task 3: Correlation & Probability
python Task_3_Correlation_Probability/task_3.py

# Task 4: Outlier Detection
python Task_4_Outlier_Detection/task_4.py

# Task 5: Matplotlib Charts
python Task_5_Matplotlib_Visualization/task_5.py

# Task 6: Seaborn Charts
python Task_6_Seaborn_Visualization/task_6.py

# Task 7: EDA Inspection & Cleaning
python Task_7_EDA_Inspection_Cleaning/task_7.py

# Task 8: EDA Correlation & Insights
python Task_8_EDA_Correlation_Insights/task_8.py

# Task 9: Business Recommendations
python Task_9_Business_Recommendations/task_9.py

# Recompile PDF Report
python generate_report.py
```

---

## PDF Report Details

The primary submission artifact is **`Week_4_Statistics_Visualization_EDA_Report.pdf`**:
- **Format:** ReportLab two-pass `NumberedCanvas` (running headers, 'Page X of Y' footers).
- **Length:** 19 Pages.
- **Embedded Media:** All 9 Matplotlib and Seaborn charts embedded with captions and analytical commentary.
- **Integrity:** Strict adherence to non-plagiarized, programmatically generated calculations.
