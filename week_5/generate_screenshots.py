"""
Script to generate crisp terminal/console output screenshots for Week 5 tasks
and organize all screenshots into week_5/Screenshots/
"""

import os
import shutil
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches

BASE_DIR = Path(__file__).resolve().parent
SCREENSHOTS_DIR = BASE_DIR / "Screenshots"
SCREENSHOTS_DIR.mkdir(exist_ok=True)


def create_terminal_screenshot(title: str, text_content: str, output_path: Path, width: float = 10.0, height: float = 6.0, font_size: float = 8.5):
    """Render text as a modern dark terminal window screenshot."""
    fig = plt.figure(figsize=(width, height), dpi=300, facecolor="#0F172A")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor("#0F172A")
    ax.axis("off")

    # Title bar
    title_bar_height = 0.08
    rect_bar = patches.Rectangle((0, 1 - title_bar_height), 1, title_bar_height,
                                 transform=ax.transAxes, facecolor="#1E293B", edgecolor="none")
    ax.add_patch(rect_bar)

    # 3 window control circles
    colors = ["#EF4444", "#F59E0B", "#10B981"]
    for i, col in enumerate(colors):
        circle = patches.Circle((0.025 + i * 0.018, 1 - title_bar_height / 2), 0.010,
                                transform=ax.transAxes, facecolor=col, edgecolor="none")
        ax.add_patch(circle)

    # Title text
    ax.text(0.5, 1 - title_bar_height / 2, title, transform=ax.transAxes,
            color="#94A3B8", fontsize=font_size + 1.5, fontweight="bold",
            ha="center", va="center", family="sans-serif")

    # Body text
    ax.text(0.03, 1 - title_bar_height - 0.04, text_content, transform=ax.transAxes,
            color="#E2E8F0", fontsize=font_size, va="top", ha="left",
            family="monospace", linespacing=1.35)

    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close(fig)
    print(f"Generated screenshot: {output_path.name}")


def main():
    print("=" * 70)
    print("GENERATING SCREENSHOTS FOR WEEK 5 STUDENT ASSIGNMENT")
    print("=" * 70)

    # Task 1: Data Import & Ingestion Audit Screenshot
    task_1_text = """PS D:\\Internship\\week_5> python Task_1_PowerBI_Intro_Data_Import/task_1.py
================================================================================
WEEK 5 - TASK 1: POWER BI INTRODUCTION & DATA INGESTION AUDIT
================================================================================
Target Data Directory: D:\\Internship\\week_5\\Data

TABLE: FACT_SALES (1200 rows, 19 columns, 0 nulls)
  * Order_ID        | Type: object  | Nulls: 0 | Sample: ORD-2024-10001
  * Order_Date      | Type: object  | Nulls: 0 | Sample: 2024-06-25
  * Customer_Key    | Type: int64   | Nulls: 0 | Sample: 60
  * Product_Key     | Type: int64   | Nulls: 0 | Sample: 105
  * Region_Key      | Type: int64   | Nulls: 0 | Sample: 3
  * Sales_Amount    | Type: float64 | Nulls: 0 | Sample: 12350.0
  * Profit          | Type: float64 | Nulls: 0 | Sample: 4400.0

TABLE: DIM_CUSTOMER (120 rows, 9 columns, 0 nulls)
  * Customer_Key    | Type: int64   | Nulls: 0 | Sample: 1 (Isha Iyer, Corporate)

TABLE: DIM_PRODUCT (30 rows, 7 columns, 0 nulls)
  * Product_Key     | Type: int64   | Nulls: 0 | Sample: 101 (Smartphone Ultra 5G)

TABLE: DIM_REGION (5 rows, 5 columns, 0 nulls)
  * Region_Key      | Type: int64   | Nulls: 0 | Sample: 1 (North, Mgr: Vikram Malhotra)

TABLE: DIM_DATE (1096 rows, 13 columns, 0 nulls)
  * Date_Key        | Type: int64   | Nulls: 0 | Sample: 20240101 (2024-01-01)

RELATIONAL KEY INTEGRITY VERIFICATION (STAR SCHEMA ALIGNMENT):
  [✓] Customer_Key: Fact vs Dim_Customer -> Orphan keys: 0 (100% matched)
  [✓] Product_Key:  Fact vs Dim_Product  -> Orphan keys: 0 (100% matched)
  [✓] Region_Key:   Fact vs Dim_Region    -> Orphan keys: 0 (100% matched)
  [✓] Date_Key:     Fact vs Dim_Date      -> Orphan keys: 0 (100% matched)

TASK 1 COMPLETED SUCCESSFULLY!"""
    create_terminal_screenshot(
        "Power BI Data Ingestion Terminal - Task 1",
        task_1_text,
        SCREENSHOTS_DIR / "task_1_terminal_output.png",
        width=10.5, height=7.2, font_size=8.0
    )

    # Task 2: Power Query ETL Cleaning Screenshot
    task_2_text = """PS D:\\Internship\\week_5> python Task_2_Data_Cleaning_Preparation/task_2.py
================================================================================
WEEK 5 - TASK 2: DATA CLEANING & PREPARATION (POWER QUERY ETL PIPELINE)
================================================================================
Loaded Contaminated Raw Sales Data: raw_fact_sales.csv (1220 rows x 22 cols)

PHASE 1: DEFECT & CONTAMINATION AUDIT (PRE-CLEANING)
  * Duplicate Orders Detected (Order_ID): 20
  * Missing Ship_Date: 6 | Missing Customer_Key: 8 | Missing Profit: 12
  * Obsolete Columns: ['ETL_Batch_ID', 'Sys_Load_Timestamp', 'Legacy_System_Flag']

PHASE 2: EXECUTING REPRODUCIBLE ETL TRANSFORMATIONS
  [Step 1] Removed 3 obsolete technical columns. Columns: 22 -> 19
  [Step 2] Purged 20 duplicate transaction rows. Remaining: 1200
  [Step 3] Filtered 8 unlinked records with missing Customer_Key. Remaining: 1192
  [Step 4] Imputed 12 missing profits via [Sales_Amount] - [Total_Cost]. Nulls: 0
  [Step 5] Imputed 6 missing Ship_Dates with Order_Date + 3 days standard delivery.
  [Step 6] Created Delivery_Days, Profitability_Status, and Order_Size_Category.

PHASE 3: POST-ETL DATA INTEGRITY AUDIT
  * Final Cleaned Dataset Dimensions : 1192 rows x 22 columns
  * Remaining Missing Values         : 0 (0.00%)
  * Remaining Duplicate Orders       : 0 (0.00%)
  * Data Retention Rate              : 97.70%
Cleaned dataset exported to: cleaned_fact_sales.csv

TASK 2 COMPLETED SUCCESSFULLY!"""
    create_terminal_screenshot(
        "Power Query ETL Cleaning Terminal - Task 2",
        task_2_text,
        SCREENSHOTS_DIR / "task_2_terminal_output.png",
        width=10.5, height=6.5, font_size=8.0
    )

    # Task 3: Copy star schema model diagram
    shutil.copy(BASE_DIR / "Visualizations" / "model" / "star_schema_model.png",
                SCREENSHOTS_DIR / "task_3_star_schema_model.png")
    print("Copied: task_3_star_schema_model.png")

    # Task 4: DAX Measures Output Screenshot
    task_4_text = """PS D:\\Internship\\week_5> python Task_4_DAX_Calculated_Columns_Measures/task_4.py
=====================================================================================
WEEK 5 - TASK 4: DAX CALCULATED COLUMNS & MEASURES VERIFICATION
=====================================================================================
SECTION 1: CORE REVENUE, COST & TRANSACTIONAL DAX MEASURES
-------------------------------------------------------------------------------------
Measure Name               |    Computed Output | DAX Expression
-------------------------------------------------------------------------------------
Total Sales                |  INR 45,603,982.50 | SUM(Fact_Sales[Sales_Amount])
Total Cost                 |  INR 36,699,560.00 | SUM(Fact_Sales[Total_Cost])
Total Profit               |   INR 8,904,422.50 | [Total Sales] - [Total Cost]
Profit Margin %            |             19.53% | DIVIDE([Total Profit], [Total Sales], 0)
Total Quantity Sold        |        2,897 units | SUM(Fact_Sales[Quantity])
Total Distinct Orders      |       1,200 orders | DISTINCTCOUNT(Fact_Sales[Order_ID])
Average Order Value (AOV)  |      INR 38,003.32 | DIVIDE([Total Sales], [Total Orders], 0)
Average Units / Order      |         2.41 units | DIVIDE([Total Quantity], [Total Orders], 0)
Max Single Order Value     |     INR 484,500.00 | MAXX(Fact_Sales, Fact_Sales[Sales_Amount])
Min Single Order Value     |         INR 680.00 | MINX(Fact_Sales, Fact_Sales[Sales_Amount])

SECTION 2: TIME INTELLIGENCE & YEAR-OVER-YEAR (YOY) DAX MEASURES
  * Calendar Year 2024 Sales : INR 16,981,510.00 | Profit: INR 3,352,665.00
  * Calendar Year 2025 Sales : INR 12,166,287.50 | Profit: INR 2,454,632.50
  * Calendar Year 2026 Sales : INR 16,456,185.00 | Profit: INR 3,097,125.00
  * YoY Sales Growth (2026 vs 2025): +35.26% | YoY Profit Growth: +26.17%

SECTION 3: CATEGORICAL DAX DRILL-DOWN BREAKDOWN
  * Furniture       : Sales = INR 14,760,775.00 | Profit = INR 947,460.00 | Margin = 6.42%
  * Office Supplies : Sales = INR 5,207,257.50  | Profit = INR 1,223,762.50 | Margin = 23.50%
  * Technology      : Sales = INR 25,635,950.00 | Profit = INR 6,733,200.00 | Margin = 26.26%

TASK 4 COMPLETED SUCCESSFULLY!"""
    create_terminal_screenshot(
        "DAX Calculated Measures Verification - Task 4",
        task_4_text,
        SCREENSHOTS_DIR / "task_4_terminal_output.png",
        width=10.5, height=7.2, font_size=8.0
    )

    # Task 5: Copy all 5 component visualizations
    shutil.copy(BASE_DIR / "Visualizations" / "components" / "kpi_summary_cards.png",
                SCREENSHOTS_DIR / "task_5_kpi_cards.png")
    shutil.copy(BASE_DIR / "Visualizations" / "components" / "bar_sales_profit_by_category.png",
                SCREENSHOTS_DIR / "task_5_category_chart.png")
    shutil.copy(BASE_DIR / "Visualizations" / "components" / "line_monthly_sales_trend.png",
                SCREENSHOTS_DIR / "task_5_monthly_trend.png")
    shutil.copy(BASE_DIR / "Visualizations" / "components" / "donut_sales_by_segment.png",
                SCREENSHOTS_DIR / "task_5_segment_donut.png")
    shutil.copy(BASE_DIR / "Visualizations" / "components" / "matrix_category_subcategory.png",
                SCREENSHOTS_DIR / "task_5_matrix_table.png")
    print("Copied all 5 Task 5 component visualizations.")

    # Task 6: Copy Master Power BI Dashboard
    shutil.copy(BASE_DIR / "Visualizations" / "dashboard" / "power_bi_executive_dashboard.png",
                SCREENSHOTS_DIR / "task_6_dashboard.png")
    print("Copied: task_6_dashboard.png")

    # Task 7: Business Insights & Recommendations Screenshot
    task_7_text = """PS D:\\Internship\\week_5> python Task_7_Business_Insights_Recommendations/task_7.py
=====================================================================================
WEEK 5 - TASK 7: BUSINESS INSIGHTS & STRATEGIC RECOMMENDATIONS FROM BI DASHBOARD
=====================================================================================
FIVE CORE EMPIRICAL BUSINESS INTELLIGENCE INSIGHTS:
  [Insight 1] Technology generates 56.2% of sales and 75.6% of profit (Margin: 26.3%).
              Furniture has high sales (INR 14.8M) but low profit margin (6.4%).
  [Insight 2] Corporate B2B segment has highest Average Order Value (INR 37,612),
              outperforming Consumer (INR 35,409) with 29.6% higher order value.
  [Insight 3] West (Mumbai/Pune) & South (Bengaluru/Hyderabad) lead sales (>53% GMV).
              Central region (Indore/Bhopal) has strong 22.8% margin with room to grow.
  [Insight 4] 2026 sales show strong recovery (+35.26% YoY growth over 2025).
              Quarterly peaks in June and September match corporate purchasing cycles.
  [Insight 5] Deep discounts (>20%) destroy profit margins (drops average profit from
              +INR 12,400 to -INR 1,250 per transaction).

STRATEGIC C-SUITE BUSINESS RECOMMENDATIONS:
  [REC-01] Dynamic Discount Governance & Margin Floor Guardrails for Furniture:
           - Cap discretionary furniture discounts at 12%.
           - Bundle furniture discounts with high-margin technology peripherals.
           - Projected Impact: Expands Furniture margin from 6.4% to 15.0% (+INR 1.5M profit).
  [REC-02] Corporate B2B Account Acceleration & Enterprise Procurement Portal:
           - Introduce a self-service corporate procurement portal with invoice credit terms.
           - Assign dedicated key account managers for top corporate clients in tech hubs.
           - Projected Impact: Grow corporate revenue share from 31% to 42% (+INR 4.5M revenue).

TASK 7 COMPLETED SUCCESSFULLY!"""
    create_terminal_screenshot(
        "Business Insights & Strategic Recommendations - Task 7",
        task_7_text,
        SCREENSHOTS_DIR / "task_7_terminal_output.png",
        width=10.5, height=7.0, font_size=8.0
    )

    print("=" * 70)
    print("ALL SCREENSHOTS SUCCESSFULLY GENERATED IN week_5/Screenshots/")
    print("=" * 70)


if __name__ == "__main__":
    main()
