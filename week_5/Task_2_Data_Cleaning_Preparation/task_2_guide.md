# Task 2 Guide: Power Query Data Cleaning & Preparation

**Student:** Ayush  
**Course:** B.Tech Computer Science & Engineering (IoT)  
**Institution:** Prestige Institute of Engineering, Management & Research (PIEMR), Indore  
**Assignment:** Week 5 — Power BI & Business Intelligence (Task 2: 15 Marks)  

---

## 1. Overview of the Power Query ETL Process

Data preparation constitutes up to 70% of the total analytical effort in enterprise Business Intelligence. The **Power Query Engine** executes declarative transformation pipelines formulated in the functional **M language**, ensuring reproducible data transformations every time the dataset refreshes.

```
┌──────────────────┐      ┌─────────────────────────┐      ┌──────────────────────────┐      ┌─────────────────────┐
│ 1. Raw Ingestion │ ───► │ 2. Defect Remediation   │ ───► │ 3. Feature Enrichment    │ ───► │ 4. VertiPaq Load    │
│ • raw_fact_sales │      │ • Remove 20 Duplicates  │      │ • Delivery_Days          │      │ • Clean Star Schema │
│ • 1,220 Records  │      │ • Impute 12 Null Profits│      │ • Profitability_Status   │      │ • 1,192 Clean Rows  │
│ • Corrupted Cols │      │ • Cast Data Types       │      │ • Order_Size_Category    │      │ • Zero Missing/Dupes│
└──────────────────┘      └─────────────────────────┘      └──────────────────────────┘      └─────────────────────┘
```

---

## 2. Step-by-Step Data Cleaning Workflow

### Step 1: Column Profiling & Defect Detection
- In Power Query Editor, navigate to the **View** ribbon and enable:
  - **Column quality:** Shows Valid, Error, and Empty percentages.
  - **Column distribution:** Visualizes distinct and unique values.
  - **Column profile:** Displays min, max, average, and frequency charts.
- **Identified Defects in `raw_fact_sales.csv`:**
  - 20 duplicate orders artificially inflating GMV.
  - 12 rows with null `Profit` and `Profit_Margin_Pct`.
  - 8 rows with missing `Customer_Key` (orphan foreign keys).
  - 3 unnecessary ingestion tracking columns (`ETL_Batch_ID`, `Sys_Load_Timestamp`, `Legacy_System_Flag`).
  - Text-based date fields lacking native temporal hierarchies.

### Step 2: Removing Obsolete Columns
- Select `ETL_Batch_ID`, `Sys_Load_Timestamp`, and `Legacy_System_Flag`.
- Right-click $\rightarrow$ **Remove Columns** (or press `Delete`).
- *Rationale:* Eliminating high-cardinality metadata fields dramatically shrinks RAM footprint in Power BI's in-memory columnar database.

### Step 3: Deduplication (Removing Duplicate Records)
- Select the `Order_ID` primary key column.
- Right-click $\rightarrow$ **Remove Duplicates** (`Table.Distinct(..., {"Order_ID"})`).
- *Outcome:* 20 redundant rows removed, restoring transaction integrity.

### Step 4: Remedying Orphan Keys & Nulls
- Filter `Customer_Key` $\rightarrow$ uncheck `(null)` to eliminate unlinked transactions.
- *Imputing Null Profits:* Rather than discarding transactions with missing profit, we apply domain logic:
  $$\text{Profit} = \text{Sales Amount} - \text{Total Cost}$$
  $$\text{Profit Margin \%} = \left(\frac{\text{Profit}}{\text{Sales Amount}}\right) \times 100$$

### Step 5: Explicit Data Type Casting
- Apply the appropriate types:
  - `Order_Date`, `Ship_Date` $\rightarrow$ **Date**
  - `Date_Key`, `Customer_Key`, `Product_Key`, `Region_Key`, `Quantity` $\rightarrow$ **Whole Number (`Int64.Type`)**
  - `Unit_Price`, `Unit_Cost`, `Discount_Rate`, `Sales_Amount`, `Shipping_Cost`, `Total_Cost`, `Profit` $\rightarrow$ **Fixed Decimal Number / Currency (`type number`)**
  - `Order_ID`, `Ship_Mode`, `Order_Priority` $\rightarrow$ **Text**

### Step 6: Custom Column Transformations & Feature Enrichment
- **Delivery Days:** `Duration.Days([Ship_Date] - [Order_Date])`
- **Profitability Bucket (Conditional Column):**
  - If `Profit_Margin_Pct` $\ge 25\% \rightarrow$ *"High Margin"*
  - Else If `Profit_Margin_Pct` $\ge 10\% \rightarrow$ *"Standard Margin"*
  - Else If `Profit_Margin_Pct` $\ge 0\% \rightarrow$ *"Low Margin"*
  - Else $\rightarrow$ *"Loss-Making"*
- **Order Size Category:**
  - If `Quantity` $\ge 6 \rightarrow$ *"Bulk Order"*
  - Else If `Quantity` $\ge 2 \rightarrow$ *"Multi-Item Order"*
  - Else $\rightarrow$ *"Single Item Order"*

### Step 7: Renaming Columns for Executive Reporting
- Rename snake_case technical identifiers to intuitive title-case names:
  `Sales_Amount` $\rightarrow$ `Sales Amount`, `Profit_Margin_Pct` $\rightarrow$ `Profit Margin %`, `Order_Priority` $\rightarrow$ `Order Priority`.

---

## 3. Pre- vs. Post-Cleaning Audit Comparison

| Metric | Raw Ingestion State (`raw_fact_sales.csv`) | Post-ETL Cleaned State (`cleaned_fact_sales.csv`) | Business Impact |
|---|:---:|:---:|---|
| **Total Rows** | 1,220 records | 1,192 validated records | Removed 20 duplicates + 8 unlinked orphan rows. |
| **Missing Values** | 26 missing fields | 0 missing fields (100% complete) | Mathematical recalculation of profit & margins. |
| **Duplicate Orders** | 20 duplicate orders | 0 duplicates | Restores authentic GMV and prevents revenue overstatement. |
| **Column Count** | 22 columns (with audit junk) | 22 clean, business-ready columns | Purged 3 system columns; added 3 analytical features. |
| **Referential Integrity** | Violated (8 missing customer keys) | 100% valid foreign keys | Ensures error-free relationship creation in Data Model. |
