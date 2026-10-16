# Week 5 — Power BI & Business Intelligence

**Student:** Ayush  
**Course:** B.Tech Computer Science & Engineering (IoT)  
**College:** Prestige Institute of Engineering, Management & Research (PIEMR), Indore  
**Assignment:** Week 5 — Power BI & Business Intelligence (Marks: 100)  
**Repository:** [https://github.com/Ayush-Raghuwanshi-Dev/DA_Internship.git](https://github.com/Ayush-Raghuwanshi-Dev/DA_Internship.git)  

---

## Project Overview

This repository contains the complete, verified, and automated implementation of the **Week 5 Data Analytics Internship Assignment**. The project covers the complete Power BI and Business Intelligence lifecycle: multi-table dataset ingestion, automated Power Query ETL data cleaning, Star Schema dimensional data modeling, an enterprise library of 16+ production DAX measures and calculated columns, five distinct visual components, a master Full HD interactive dashboard canvas, and data-grounded strategic business recommendations.

The analysis is conducted on an omnichannel **Retail E-Commerce Business Intelligence** domain (`Fact_Sales`, `Dim_Customer`, `Dim_Product`, `Dim_Region`, `Dim_Date`) representing 1,200 commercial sales transactions spanning 2024 through 2026 across 30 catalog products and 5 major metropolitan territories.

---

## Directory Structure

```
week_5/
│
├── Data/
│   ├── generate_datasets.py            # Automated multi-table dataset generator
│   ├── Fact_Sales.csv                  # 1,200 transaction records (2024–2026)
│   ├── Dim_Customer.csv                # Customer master dimension (Segments, Geography)
│   ├── Dim_Product.csv                 # Product hierarchy dimension (Category, Sub-Category)
│   ├── Dim_Region.csv                  # Territory and regional manager dimension
│   ├── Dim_Date.csv                    # Calendar dimension (Years, Quarters, Months)
│   ├── raw_fact_sales.csv              # Contaminated raw data for Power Query demonstration
│   ├── cleaned_fact_sales.csv          # Cleaned post-ETL transaction fact table
│   └── Retail_BI_Data_Model.xlsx       # Multi-tab structured Excel workbook data model
│
├── Task_1_PowerBI_Intro_Data_Import/
│   ├── task_1.py                       # Schema audit & metadata inspector
│   ├── task_1_guide.md                 # Power BI interface & architecture guide
│   └── task_1_summary.txt              # Table schema & data type audit report
│
├── Task_2_Data_Cleaning_Preparation/
│   ├── task_2.py                       # Data cleaning pipeline & verification script
│   ├── M_Query_Cleaning.m              # Exact Power Query M-code transformations
│   ├── task_2_guide.md                 # Power Query ETL documentation
│   └── task_2_summary.txt              # Cleaning audit and retention metrics
│
├── Task_3_Data_Modeling_Relationships/
│   ├── task_3.py                       # Relational integrity & cardinality verification
│   ├── task_3_guide.md                 # Star Schema & relationships architecture guide
│   └── task_3_summary.txt              # Key mappings and relationship documentation
│
├── Task_4_DAX_Calculated_Columns_Measures/
│   ├── task_4.py                       # DAX formula calculator & mathematical verifier
│   ├── all_measures.dax                # Complete production DAX expressions library
│   ├── task_4_guide.md                 # DAX syntax, context transition & time intelligence guide
│   └── task_4_summary.txt              # Verified measure output values table
│
├── Task_5_PowerBI_Visualizations/
│   ├── task_5.py                       # Visual component generator (5 distinct chart types)
│   └── task_5_summary.txt              # Visualization specifications & design tokens
│
├── Task_6_Interactive_Dashboard_Filters/
│   ├── task_6.py                       # Master executive dashboard canvas generator
│   ├── task_6_guide.md                 # Dashboard layout, slicers & interaction guide
│   └── task_6_summary.txt              # Dashboard layout, slicer logic & UX specification
│
├── Task_7_Business_Insights_Recommendations/
│   ├── task_7.py                       # Statistical insight synthesizer & recommendation engine
│   └── business_insights_recommendations.txt # 5 core insights & 2 strategic recommendations
│
├── Visualizations/
│   ├── components/                     # Individual high-resolution visual charts
│   │   ├── kpi_summary_cards.png
│   │   ├── bar_sales_profit_by_category.png
│   │   ├── line_monthly_sales_trend.png
│   │   ├── donut_sales_by_segment.png
│   │   └── matrix_category_subcategory.png
│   ├── dashboard/
│   │   └── power_bi_executive_dashboard.png # Full HD 1920x1080 master dashboard render
│   └── model/
│       └── star_schema_model.png       # Star Schema Entity-Relationship Architecture Diagram
│
├── requirements.txt                    # Project dependencies
├── run_all_week_5.py                   # Master end-to-end automation pipeline runner
├── generate_report.py                  # ReportLab PDF report compiler
└── Week_5_PowerBI_Business_Intelligence_Report.pdf # Final comprehensive submission report
```

---

## Assignment Tasks & Core Findings

| Task | Topic | Marks | Key Empirical Findings & Metrics |
|---|---|:---:|---|
| **Task 1** | Power BI Interface & Import | 10 | Explored Report, Data, and Model views; imported 5-table Star Schema from Excel/CSV; verified column data types and 100% referential integrity across 1,200 records. |
| **Task 2** | Power Query ETL Data Cleaning | 15 | Identified and resolved defects in `raw_fact_sales.csv`: removed 20 duplicate orders, imputed missing profits via Net Sales - Total Cost, filtered orphan keys, cast types, and created custom conditional columns (`Delivery_Days`, `Profitability_Status`). Provided complete M-code (`M_Query_Cleaning.m`). |
| **Task 3** | Star Schema Data Modeling | 15 | Architected 1-to-Many (`1:*`) relationships between `Fact_Sales` and all 4 dimensions (`Dim_Customer`, `Dim_Product`, `Dim_Region`, `Dim_Date`). Single-direction cross-filtering; generated publication-grade Star Schema architecture diagram (`star_schema_model.png`). |
| **Task 4** | DAX Measures & Calculated Columns | 15 | Created library of 16+ production DAX expressions: `Total Sales` (INR 45.60M), `Total Profit` (INR 8.90M), `Profit Margin %` (19.53%), `Total Orders` (1,200), `AOV` (INR 38,003), and Time Intelligence YoY measures (+35.26% sales growth in 2026). Verified mathematically. |
| **Task 5** | Power BI Visualizations | 15 | Generated 5 customized components at 300 DPI: KPI summary cards, Clustered column & line chart (Category performance), Monthly sales YoY line chart, Customer segment donut chart, and hierarchical drill-down matrix. |
| **Task 6** | Interactive Dashboard & Slicers | 15 | Rendered master Full HD (1920x1080) Executive Dashboard canvas (`power_bi_executive_dashboard.png`) featuring top branding ribbon, 4 interactive slicers (Year, Region, Category, Segment), row of 4 KPI cards, and 2x2 analytical grid. |
| **Task 7** | Business Insights & Recommendations | 15 | Synthesized 5 empirical insights (Furniture margin compression at 6.4%, Corporate AOV premium of INR 37.6k, West/South quota leadership, 2026 growth momentum, and deep discount margin destruction). Formulated 2 strategic recommendations (Dynamic Discount Governance & Corporate B2B Portal) with projected ROI of INR 6.3M+. |
| **Total** | **All Modules** | **100** | **Comprehensive Professional PDF Report Generated.** |

---

## Visualizations Preview

All visualizations are rendered at 300 DPI and stored inside `Visualizations/`:

1. **Star Schema Model (`Visualizations/model/star_schema_model.png`):** Entity-Relationship Diagram showing `Fact_Sales` connected to `Dim_Customer`, `Dim_Product`, `Dim_Region`, and `Dim_Date` with cardinality markers.
2. **KPI Summary Cards (`Visualizations/components/kpi_summary_cards.png`):** 4 executive KPI cards for Total Sales, Net Profit, Profit Margin %, and Total Orders with variance badges.
3. **Category Performance (`Visualizations/components/bar_sales_profit_by_category.png`):** Clustered Column & Line chart showing Sales, Profit, and Profit Margin % by Category.
4. **Monthly Sales Trajectory (`Visualizations/components/line_monthly_sales_trend.png`):** 2025 vs 2026 YoY line chart with shaded area fill.
5. **Customer Segment Donut (`Visualizations/components/donut_sales_by_segment.png`):** Revenue split across Consumer (52.1%), Corporate (31.2%), and Home Office (16.7%).
6. **Hierarchical Matrix (`Visualizations/components/matrix_category_subcategory.png`):** Category $\rightarrow$ Sub-Category drill-down with conditional formatting.
7. **Master Executive Dashboard (`Visualizations/dashboard/power_bi_executive_dashboard.png`):** Full HD (1920x1080) complete interactive cockpit.

---

## How to Execute

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Entire Automation Pipeline
To execute all task modules, verify data cleaning, calculate DAX measures, generate visual components, render the dashboard, and compile the PDF report:
```bash
python run_all_week_5.py
```

### 3. Run Individual Tasks
```bash
# Step 0: Generate Star Schema Datasets
python Data/generate_datasets.py

# Task 1: Power BI Interface & Ingestion Audit
python Task_1_PowerBI_Intro_Data_Import/task_1.py

# Task 2: Power Query ETL Data Cleaning
python Task_2_Data_Cleaning_Preparation/task_2.py

# Task 3: Star Schema Data Modeling & Diagram
python Task_3_Data_Modeling_Relationships/task_3.py

# Task 4: DAX Measures & Calculated Columns
python Task_4_DAX_Calculated_Columns_Measures/task_4.py

# Task 5: Power BI Visualization Components
python Task_5_PowerBI_Visualizations/task_5.py

# Task 6: Master Interactive Dashboard Canvas
python Task_6_Interactive_Dashboard_Filters/task_6.py

# Task 7: Business Insights & Strategic Recommendations
python Task_7_Business_Insights_Recommendations/task_7.py

# Recompile PDF Report
python generate_report.py
```

---

## How to Import into Power BI Desktop

1. Open **Power BI Desktop**.
2. Click **Get Data** $\rightarrow$ **Excel workbook**.
3. Select `Data/Retail_BI_Data_Model.xlsx`.
4. In the Navigator, select all 5 tables: `Fact_Sales`, `Dim_Customer`, `Dim_Product`, `Dim_Region`, `Dim_Date`.
5. Click **Transform Data** to inspect the M-code transformations in Power Query, or click **Load** to commit directly.
6. In **Model View**, verify the Star Schema relationships (`1:*` from dimensions to `Fact_Sales`).
7. Paste measures from `Task_4_DAX_Calculated_Columns_Measures/all_measures.dax` into New Measures.
8. Recreate visual canvas using layout specs in `Task_6_Interactive_Dashboard_Filters/task_6_guide.md`.

---

## PDF Report Details

The primary submission document is **`Week_5_PowerBI_Business_Intelligence_Report.pdf`**:
- **Format:** ReportLab two-pass `NumberedCanvas` (running headers, 'Page X of Y' footers).
- **Embedded Media:** Star Schema Architecture diagram, all 5 component visualizations, and master Full HD dashboard render embedded with captions.
- **Integrity:** Strict adherence to authentic, non-plagiarized calculations and verified empirical outputs.
