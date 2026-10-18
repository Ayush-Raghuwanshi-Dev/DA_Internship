# Week 6: Git, GitHub & Final Data Analytics Project

**Student:** Ayush  
**Academic Degree & Branch:** B.Tech in Computer Science & Engineering (IoT)  
**Institution:** Prestige Institute of Engineering, Management & Research (PIEMR), Indore  
**Subject:** Data Analytics Internship — Final Capstone Project (100 Marks)  
**Repository:** [https://github.com/Ayush-Raghuwanshi-Dev/DA_Internship.git](https://github.com/Ayush-Raghuwanshi-Dev/DA_Internship.git)  

---

## 1. Project Title
**Omnichannel E-Commerce Customer Analytics & Executive Business Intelligence**

---

## 2. Project Overview
This final capstone project represents the culmination of the Data Analytics Internship, synthesizing skills acquired across the 6-week curriculum:
- **Weeks 1 & 2 (NumPy & Pandas):** Vectorized calculations, dataframe manipulation, missing-value imputation.
- **Week 3 (SQL & Excel):** Relational data architectures, aggregation, business reporting models.
- **Week 4 (Statistics & EDA):** Parametric/non-parametric distributions, variance, Tukey's IQR outlier detection, correlation analysis.
- **Week 5 (Power BI & Business Intelligence):** Star Schema dimensional modeling, DAX measures, interactive dashboard design.
- **Week 6 (Git & GitHub):** Version control, multi-stage branching/commits, repository documentation, project presentation.

---

## 3. Problem Statement
Omnichannel retail enterprises face margin compression caused by uncontrolled price discounting, bulky furniture shipping overhead, and unsegmented customer engagement. This project addresses:
1. Identifying high-margin vs loss-leading merchandise lines.
2. Quantifying the basket economics of distinct customer tiers (Corporate vs Consumer).
3. Defining the empirical discount threshold beyond which transactions destroy profitability.
4. Structuring an interactive executive BI dashboard for data-driven C-suite decision-making.

---

## 4. Dataset Description
The analysis leverages a transactional dataset of 1,500 retail records spanning 2024 to 2026 across 5 macro-territories in India:
- **Volume:** 1,492 validated commercial orders across 29 analytical attributes.
- **Entities:** Customers (Consumer, Corporate, Home Office), Geography (North, South, East, West, Central), Products (Technology, Furniture, Office Supplies).
- **Files:**
  - `Data/raw_ecommerce_sales.csv`: Uncleaned ingestion feed with defects.
  - `Data/cleaned_ecommerce_sales.csv`: Pristine analytical dataset.
  - `Data/ecommerce_data_dictionary.csv`: Full attribute metadata.
  - `Data/Ecommerce_Capstone_Data_Model.xlsx`: Multi-tab Excel data model.

---

## 5. Tools Used
- **Programming & Analysis:** Python 3.10, NumPy, Pandas, SciPy
- **Data Visualization:** Matplotlib, Seaborn
- **Business Intelligence:** Power BI Desktop, Power Query, DAX
- **Version Control:** Git, GitHub
- **Report & Documentation:** ReportLab, Markdown

---

## 6. Data Cleaning Process (ETL Pipeline)
Inspected raw ingestion data (1,525 rows) and executed a systematic ETL pipeline (`Task_3_Dataset_Preparation/task_3.py`):
1. **Purged Obsolete Columns:** Dropped `ETL_Batch_ID`, `Sys_Load_Timestamp`, and `Legacy_System_Flag`.
2. **Deduplicated Records:** Removed 25 duplicate orders sharing identical `Order_ID`s.
3. **Filtered Null Foreign Keys:** Filtered 8 unlinked records missing `Customer_ID`.
4. **Imputed Missing Profit:** Computed 12 missing values via `Sales_Amount - Total_Cost`.
5. **Imputed Missing Ship Dates:** Filled 10 missing dates via `Order_Date + 3 days` standard SLA.
6. **Feature Engineering:** Added `Delivery_Days`, `Profitability_Status`, and `Order_Size_Bucket`.
- **Validation:** 1,492 final validated rows, 0 nulls, 0 duplicates (97.8% retention rate).

---

## 7. Exploratory Data Analysis (EDA)
- **Descriptive Statistics:**
  - Mean Order Value: INR 47,005.19 | Median: INR 25,000.00 | Std Dev: INR 69,152.84
  - Right-skewed distribution driven by large corporate tech purchases.
- **Outlier Detection (IQR Method):**
  - Identified 131 sales outliers (8.78%) and 156 profit outliers (10.46%) reflecting legitimate high-value enterprise orders.
- **Multivariate Correlation:**
  - `Sales_Amount` & `Profit`: $r = +0.947$ (Strong positive correlation).
  - `Discount_Rate` & `Profit`: $r = -0.218$ (Demonstrated margin erosion).

---

## 8. Data Visualizations
Five publication-grade 300 DPI charts generated in `Visualizations/charts/`:
1. `chart_1_sales_profit_by_category.png`: Clustered Bar & Margin Curve by Category.
2. `chart_2_monthly_sales_trend.png`: 36-Month Sales Trajectory with 3-Month Rolling Average.
3. `chart_3_segment_order_value_violin.png`: Customer Segment Order Value Distribution.
4. `chart_4_correlation_heatmap.png`: Seaborn Multivariate Correlation Heatmap.
5. `chart_5_discount_vs_profit_margin_scatter.png`: Discount vs Profit Margin Cliff Scatter Plot.

---

## 9. Power BI Dashboard
Master Full HD (1920x1080) interactive dashboard canvas generated in `Visualizations/dashboard/final_power_bi_capstone_dashboard.png`:
- **5 KPI Summary Cards:**
  - Total Revenue: INR 70.13M (+34.8% YoY)
  - Net Commercial Profit: INR 14.02M (+28.4% YoY)
  - Gross Profit Margin: 19.99% (Benchmark Target: 20.0%)
  - Total Orders: 1,492 Orders (AOV: INR 47,005)
  - Basket Velocity: 2.50 Units per Order (Total Volume: 3,730 Units)
- **Interactive Controls:** Top Slicers Bar for Year, Region, Category, and Segment.
- **4 Grid Panels:** Category Performance, Customer Segment Donut, Monthly Trajectory, Regional GMV.

---

## 10. Key Insights
1. **Technology Profit Engine:** Technology accounts for 63.8% of GMV and 80.5% of company profit (25.2% margin).
2. **Furniture Margin Compression:** Furniture captures INR 22.80M in sales but yields only 9.09% profit margin due to courier freight and uncalibrated discounting.
3. **Corporate B2B Basket Economics:** Corporate clients generate an AOV of INR 72,718.73 (2.7x higher than Consumers) and contribute 58% of total revenue.
4. **Territory Polarization:** South (INR 21.1M) and North (INR 16.7M) drive 54% of sales; Central maintains an exceptional 21.49% profit margin.
5. **Discount Erosion Cliff:** Discounts exceeding 20% systematically wipe out gross margin, dropping average order profit to -INR 683.

---

## 11. Strategic Business Recommendations
1. **Dynamic Discount Governance for Furniture:**
   - Cap discretionary furniture discounts at 10%.
   - Require discounts up to 20% to be conditionally unlocked ONLY when bundled with high-margin technology peripherals.
   - **Projected Impact:** Lifts Furniture margin from 9.1% to 16.5% (+INR 1.65M profit).
2. **Corporate B2B Account Acceleration & Portal:**
   - Launch a self-service corporate purchasing portal with invoice credit terms (Net 30/60).
   - Target enterprise tech clusters across Pune, Bengaluru, and Indore.
   - **Projected Impact:** Increases Corporate revenue contribution from 58% to 68% (+INR 7.5M high-margin revenue).

---

## 12. Conclusion & Deliverables
- **GitHub Repository:** [https://github.com/Ayush-Raghuwanshi-Dev/DA_Internship.git](https://github.com/Ayush-Raghuwanshi-Dev/DA_Internship.git)
- **PDF Report:** `Week_6_Final_Data_Analytics_Capstone_Report.pdf` (Clean beginner-friendly student submission report with student details, questions, notes, and screenshots of all outputs).
- **Presentation Deck:** `Presentation/project_presentation.md` (10-slide executive summary).
