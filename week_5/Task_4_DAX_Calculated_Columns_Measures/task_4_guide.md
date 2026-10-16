# Task 4 Guide: DAX Calculated Columns & Measures Architecture

**Student:** Ayush  
**Course:** B.Tech Computer Science & Engineering (IoT)  
**Institution:** Prestige Institute of Engineering, Management & Research (PIEMR), Indore  
**Assignment:** Week 5 — Power BI & Business Intelligence (Task 4: 15 Marks)  

---

## 1. Fundamentals of Data Analysis Expressions (DAX)

**Data Analysis Expressions (DAX)** is a formula expression language designed specifically for relational data models, semantic tabular models, and Power BI. Unlike spreadsheet formulas that reference cell coordinates (e.g. `A1 + B1`), DAX operates natively on **Tables**, **Columns**, and **Filter Contexts**.

### Calculated Columns vs. DAX Measures

```
┌────────────────────────────────────────────────────────┐
│            CALCULATED COLUMN (ROW CONTEXT)             │
├────────────────────────────────────────────────────────┤
│ • Evaluated row-by-row during data refresh.           │
│ • Consumes permanent RAM in VertiPaq columnar model.   │
│ • Does NOT respond to visual slicers or user clicks.   │
│ • Best for: Slicers, categorizations, grouping buckets.│
└────────────────────────────────────────────────────────┘

                           vs

┌────────────────────────────────────────────────────────┐
│              DAX MEASURE (FILTER CONTEXT)              │
├────────────────────────────────────────────────────────┤
│ • Evaluated dynamically on-the-fly at query time.      │
│ • Consumes ZERO storage RAM.                           │
│ • Dynamically re-evaluates based on active filters!    │
│ • Best for: Numerical totals, ratios, KPIs, charts.    │
└────────────────────────────────────────────────────────┘
```

---

## 2. Core Evaluation Contexts in DAX

1. **Filter Context:**
   - The set of active filters applied to the data model at the moment a measure is evaluated.
   - Sourced from visual rows, columns, slicer selections, filter pane rules, and cross-highlighting from other charts.
   - Example: In a matrix with "Technology" on rows and "2025" on columns, `[Total Sales]` is evaluated under the filter context: `Category = "Technology"` AND `Year = 2025`.

2. **Row Context:**
   - Exists when a formula iterates through a table row-by-row (e.g. calculated columns, `SUMX`, `FILTER`, `MAXX`).
   - "Knows" the value of the current row, but has zero awareness of other rows or visual filters.

3. **Context Transition (`CALCULATE`):**
   - The supreme superpower of DAX. The `CALCULATE()` function transforms an existing **Row Context** into an equivalent **Filter Context**, enabling complex calculations such as percentage of total, time intelligence, and dynamic ranking.

---

## 3. Best Practices in Enterprise DAX Formulation

1. **Explicit Measures over Implicit Measures:**
   - Always write explicit DAX measures (e.g. `[Total Sales] = SUM(Fact_Sales[Sales_Amount])`) rather than dragging raw numerical columns into visual wells as implicit sums. Explicit measures are reusable, support measure branching, and can be referenced in composite calculations.
2. **Safe Division (`DIVIDE`):**
   - Never use the arithmetic forward slash `/` for business ratios (e.g., `Profit / Sales`), because a zero in the denominator returns `#ERROR` or `Infinity`. Always use `DIVIDE([Total Profit], [Total Sales], 0)`.
3. **Measure Branching:**
   - Build complex metrics from simpler baseline measures:
     ```dax
     [Total Sales]  = SUM(Fact_Sales[Sales_Amount])
     [Total Profit] = [Total Sales] - [Total Cost]
     [Profit Margin %] = DIVIDE([Total Profit], [Total Sales], 0)
     ```
     If the sales calculation logic ever changes (e.g., tax deductions), updating `[Total Sales]` automatically updates `[Total Profit]` and `[Profit Margin %]` across the entire dashboard!
4. **Dedicated Measures Table:**
   - Organize all business measures inside a dedicated disconnected table (`_Measures` or `Key_Metrics`) to provide a clean, centralized workspace for report consumers.

---

## 4. Time Intelligence & Calendar Functions

Time Intelligence functions allow analysts to navigate temporal dimensions effortlessly:
- `TOTALYTD(Expression, CalendarDateColumn)`: Computes year-to-date accumulation.
- `SAMEPERIODLASTYEAR(CalendarDateColumn)`: Shifts the current temporal filter context back exactly 12 months, enabling rigorous Year-over-Year (YoY) variance analysis.
- `DATEADD(CalendarDateColumn, NumberOfIntervals, Interval)`: Highly flexible temporal shifting across days, months, quarters, or years.
