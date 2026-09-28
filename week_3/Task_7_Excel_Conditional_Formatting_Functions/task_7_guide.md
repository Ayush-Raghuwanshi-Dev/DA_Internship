# Task 7: Conditional Formatting & Excel Functions (IF, COUNTIF, SUMIF)

**Student:** Ayush  
**Course:** B.Tech CSE (IoT)  
**College:** Prestige Institute of Engineering, Management & Research, Indore  
**Workbook:** `Excel/Week_3_Excel_Data_Analytics.xlsx`  
**Sheet:** `Task_7_Conditional_Functions`  

---

## 1. Task Objective

To automate categorical data segmentation and summary metric extraction using Excel's core logical and statistical functions (`IF`, `COUNTIF`, `SUMIF`), combined with visual highlighting via Conditional Formatting.

---

## 2. Excel Functions Demonstrated

### A. The `IF()` Function
- **Purpose**: Evaluates a logical condition and returns one value if TRUE and another if FALSE.
- **Applied Syntax**:
  ```excel
  =IF(E5>=75000, "High Earner", "Standard")
  ```
- **Description**: Evaluates the monthly salary in Column E. If the salary is greater than or equal to ₹75,000, the employee is categorized as `"High Earner"`; otherwise, they are designated `"Standard"`.
- **Result**: Identifies 9 high-earning professionals across the organization.

### B. The `COUNTIF()` Function
- **Purpose**: Counts the number of cells within a specified range that meet a given criterion.
- **Applied Formulas in Dashboard**:
  1. `=COUNTIF(C5:C29, "Engineering")` → **6 employees**
  2. `=COUNTIF(C5:C29, "Data Analytics")` → **6 employees**
  3. `=COUNTIF(C5:C29, "Sales & Marketing")` → **5 employees**
  4. `=COUNTIF(C5:C29, "Finance")` → **4 employees**
  5. `=COUNTIF(C5:C29, "Human Resources")` → **3 employees**
  6. `=COUNTIF(F5:F29, 5)` → **6 employees** with top Performance Rating (5 stars).
  7. `=COUNTIF(G5:G29, "High Earner")` → **9 employees**.

### C. The `SUMIF()` Function
- **Purpose**: Adds the values in a range that meet a specific condition.
- **Applied Formulas in Dashboard**:
  1. Engineering Total Payroll:
     ```excel
     =SUMIF(C5:C29, "Engineering", E5:E29)
     ```
     → **₹474,000.00**
  2. Data Analytics Total Payroll:
     ```excel
     =SUMIF(C5:C29, "Data Analytics", E5:E29)
     ```
     → **₹432,000.00**

---

## 3. Conditional Formatting Rules

1. **Top Earner Highlight (Salary >= ₹75,000)**:
   - Target Range: `E5:E29`
   - Fill Color: Soft Mint Green (`#D1FAE5`)
   - Text Color: Dark Emerald Green (`#065F46`, Bold)
   - Visual Impact: Instantly identifies leadership and senior technical personnel without manual scanning.
2. **Top Performer Highlight (Rating = 5)**:
   - Target Range: `F5:F29`
   - Fill Color: Soft Amber / Gold (`#FEF3C7`)
   - Text Color: Dark Bronze (`#92400E`, Bold)
   - Visual Impact: Flags star contributors eligible for annual merit awards.

---

## 4. Screenshot Capture Guide

- Open `Excel/Week_3_Excel_Data_Analytics.xlsx`.
- Switch to sheet **`Task_7_Conditional_Functions`**.
- Capture the main table showing the `Salary Category (IF)` column with green/amber highlights, plus the **Excel Functions Summary Dashboard** on the right side.
- Save image to: **`Screenshots/task_7_excel.png`**.
