# Task 1 Guide: Power BI Introduction & Data Import

**Student:** Ayush  
**Course:** B.Tech Computer Science & Engineering (IoT)  
**Institution:** Prestige Institute of Engineering, Management & Research (PIEMR), Indore  
**Assignment:** Week 5 — Power BI & Business Intelligence (Task 1: 10 Marks)  

---

## 1. Power BI Desktop Interface Exploration

Microsoft Power BI Desktop is an enterprise-grade business intelligence and data visualization application that integrates the high-performance **VertiPaq in-memory columnar database engine**, the **Power Query ETL engine (M language)**, and the **Data Analysis Expressions (DAX)** modeling formula language into a unified canvas.

### The Three Primary Views

| View Name | Icon Location | Primary Operational Purpose |
|---|:---:|---|
| **Report View** | Top Left Icon | The interactive report canvas where visualizations (charts, maps, matrices, KPI cards, slicers) are constructed, arranged, formatted, and interconnected. |
| **Table / Data View** | Middle Left Icon | Displays the underlying relational data in tabular format post-Power Query transformations. Used to inspect rows, verify data types, inspect calculated columns, and sort columns by specific keys. |
| **Model View** | Bottom Left Icon | The visual relationship diagram where the Star Schema or Snowflake Schema is architected. Allows engineers to define relationships, cardinality (`1:*`, `1:1`, `*:*`), cross-filter direction, and organize measures into display folders. |

---

### Supporting Panes & Windows

1. **The Ribbon:**
   - **Home:** Contains data ingestion options (*Get Data*, *Excel Workbook*), *Transform Data* (launches Power Query), text boxes, shapes, and the *Publish* button.
   - **Insert:** Visual galleries, AI visuals (*Key Influencers*, *Decomposition Tree*, *Q&A*), buttons, and bookmarks.
   - **Modeling:** Create New Measure, New Calculated Column, New Table, manage relationships, format DAX code, and configure Row-Level Security (RLS).
   - **View:** Theme picker, canvas gridlines, mobile layout editor, Bookmarks pane, Selection pane, and Performance Analyzer.
   - **Optimize:** Pause visual queries, configure DirectQuery optimization, and inspect query performance.

2. **The Data / Fields Pane (Right Side):**
   - Displays all imported tables (`Fact_Sales`, `Dim_Customer`, `Dim_Product`, `Dim_Region`, `Dim_Date`).
   - Distinguishes numeric measures (calculator icon $\sum$), calculated columns, date hierarchies, and categorical text attributes.

3. **The Visualizations Pane:**
   - Visual catalog containing 30+ native visuals (Bar, Column, Line, Area, Ribbon, Waterfall, Funnel, Scatter, Pie, Donut, Tree Map, Map, Filled Map, Gauge, Card, Multi-row Card, KPI, Slicer, Table, Matrix).
   - Field wells (*X-axis*, *Y-axis*, *Legend*, *Small multiples*, *Tooltips*) for drag-and-drop visual assembly.

4. **The Format Pane:**
   - Granular styling controls: Canvas background, visual title, data labels, callout values, axis formatting, padding, borders, drop shadows, and conditional formatting rules.

5. **Power Query Editor (Separate Window):**
   - The extraction, transformation, and loading (ETL) workstation where M-code scripts execute to reshape, clean, deduplicate, and type-cast raw data before loading into the VertiPaq model.

---

## 2. Data Ingestion Architecture & Connection Modes

Power BI offers multiple data connection architectures depending on data volume, update frequency, and latency requirements:

```
                                  ┌─────────────────────────────┐
                                  │      Power BI Desktop       │
                                  └──────────────┬──────────────┘
                                                 │
                      ┌──────────────────────────┴──────────────────────────┐
                      ▼                                                     ▼
        ┌───────────────────────────┐                         ┌───────────────────────────┐
        │        Import Mode        │                         │     DirectQuery Mode      │
        │ (In-Memory VertiPaq Engine)│                         │ (Real-Time Query Pushdown)│
        ├───────────────────────────┤                         ├───────────────────────────┤
        │ • Data compressed in RAM  │                         │ • Zero data stored in PBI │
        │ • Blazing query speed     │                         │ • Queries sent to source  │
        │ • Full DAX capabilities   │                         │ • Supports multi-TB scale │
        │ • Scheduled cloud refresh │                         │ • DAX limitations apply   │
        └───────────────────────────┘                         └───────────────────────────┘
```

For our Retail E-Commerce business intelligence project, **Import Mode** is selected because it compresses multi-table relational schemas into memory, supports advanced Time Intelligence DAX functions (`TOTALYTD`, `SAMEPERIODLASTYEAR`), and delivers instantaneous visual cross-filtering.

---

## 3. Step-by-Step Data Import Procedure

### Method A: Importing from Multi-Tab Excel Workbook (`Retail_BI_Data_Model.xlsx`)
1. Launch Power BI Desktop.
2. In the **Home** ribbon, click **Get Data** $\rightarrow$ **Excel workbook**.
3. Navigate to `D:\Internship\Week_5\week_5\Data\Retail_BI_Data_Model.xlsx` and click **Open**.
4. The **Navigator** dialogue window appears, displaying all 5 structured tables:
   - `Fact_Sales`
   - `Dim_Customer`
   - `Dim_Product`
   - `Dim_Region`
   - `Dim_Date`
5. Select all five checkboxes. A live data preview is displayed for each table.
6. Click **Transform Data** to inspect and clean the schema inside Power Query Editor before committing to the data model.

### Method B: Importing from CSV Files (`Data/*.csv`)
1. Click **Get Data** $\rightarrow$ **Text/CSV**.
2. Select `Dim_Region.csv`, verify file origin (`65001: Unicode (UTF-8)`) and comma delimiter, and click **Load** (or **Transform Data**).
3. Repeat for `Dim_Product.csv`, `Dim_Customer.csv`, `Dim_Date.csv`, and `Fact_Sales.csv`.

---

## 4. Multi-Table Schema & Data Type Audit

| Table Name | Entity Role | Record Count | Primary Key | Key Business Columns & Data Types |
|---|:---:|:---:|:---:|---|
| **`Fact_Sales`** | Transaction Fact | 1,200 | `Order_ID` | `Order_ID` (Text), `Order_Date` (Date), `Ship_Date` (Date), `Customer_Key` (Whole Number), `Product_Key` (Whole Number), `Region_Key` (Whole Number), `Quantity` (Whole Number), `Unit_Price` (Decimal), `Sales_Amount` (Decimal), `Shipping_Cost` (Decimal), `Total_Cost` (Decimal), `Profit` (Decimal), `Discount_Rate` (Percentage). |
| **`Dim_Customer`** | Dimension | 120 | `Customer_Key` | `Customer_Key` (Whole Number), `Customer_ID` (Text), `Customer_Name` (Text), `Segment` (Text: Consumer/Corporate/Home Office), `City` (Text), `State` (Text), `Country` (Text), `Postal_Code` (Text). |
| **`Dim_Product`** | Dimension | 30 | `Product_Key` | `Product_Key` (Whole Number), `Product_ID` (Text), `Product_Name` (Text), `Category` (Text: Technology/Furniture/Office Supplies), `Sub_Category` (Text), `Unit_Price` (Decimal), `Cost_Price` (Decimal). |
| **`Dim_Region`** | Dimension | 5 | `Region_Key` | `Region_Key` (Whole Number), `Region_Name` (Text), `Regional_Manager` (Text), `Target_Quota` (Decimal), `Headquarters` (Text). |
| **`Dim_Date`** | Dimension | 1,096 | `Date_Key` | `Date` (Date), `Date_Key` (Whole Number), `Year` (Whole Number), `Quarter` (Text), `Month_Num` (Whole Number), `Month_Name` (Text), `Week_Num` (Whole Number), `Day_Of_Week` (Text), `Is_Weekend` (Text). |

---

## 5. Strategic Purpose of Power BI in Enterprise Analytics

Power BI serves as the enterprise bridge connecting raw transactional operational databases (OLTP) and strategic executive decision-making. Its fundamental advantages over traditional spreadsheets include:

1. **Centralized Semantic Layer (Single Source of Truth):** Rather than having disparate departments maintain inconsistent Excel formula definitions, Power BI establishes a unified, shared business model where core metrics (`[Profit Margin %]`, `[YoY Sales Growth %]`) are calculated identically across all corporate reports.
2. **High-Performance VertiPaq Columnar Engine:** Compresses large datasets by up to 10x using dictionary encoding and run-length compression, querying millions of rows in milliseconds entirely in memory.
3. **Interactive Visual Exploration:** Unlike static reporting decks, Power BI visuals dynamically cross-filter one another. Clicking "Furniture" on a bar chart instantly filters the line chart to show Furniture trends and filters the geographic map to highlight regional Furniture demand.
4. **Governed Self-Service BI:** Non-technical business users can drag and drop pre-certified measures to build ad-hoc reports without needing to write SQL queries or disturb database administrators.
5. **Automated End-to-End Governance:** Supports scheduled incremental data refresh, automated email subscriptions, Row-Level Security (RLS) restricting regional managers to their own territorial data, and seamless Microsoft Teams/Mobile embedding.
