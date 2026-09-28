# Task 6: Excel Data Formatting, Sorting & Filtering

**Student:** Ayush  
**Course:** B.Tech CSE (IoT)  
**College:** Prestige Institute of Engineering, Management & Research, Indore  
**Workbook:** `Excel/Week_3_Excel_Data_Analytics.xlsx`  
**Sheet:** `Task_6_Format_Sort_Filter`  

---

## 1. Task Objective

To transform raw tabular transactional/HR data into a structured, professional, and visually accessible Excel spreadsheet using standard data formatting rules, sorting logic, and active auto-filters.

---

## 2. Technical Operations Applied

### A. Data Formatting
1. **Header Row Styling**:
   - Background fill: Dark Navy (`#1E3A8A`).
   - Font: Calibri, 11 pt, Bold, White text.
   - Row height: 25 pt, vertically and horizontally centered.
2. **Column Type Formatting**:
   - **`Emp ID` & `Dept ID`**: Centered integer numbers.
   - **`Salary`**: Currency formatting (`₹#,##0.00`) aligned to the right.
   - **`Hire Date`**: Standard ISO date format (`YYYY-MM-DD`).
   - **`Rating`**: Centered numerical score (1 to 5).
   - **Text Columns** (`Name`, `Department`, `Job Title`, `City`): Left-aligned for optimal readability.
3. **Zebra Striping (Alternating Row Shading)**:
   - Even rows: Clean white fill (`#FFFFFF`).
   - Odd rows: Soft slate tint (`#F8FAFC`).
   - Gridlines explicitly enabled and framed with thin slate borders (`#CBD5E1`).
4. **Summary Total Row**:
   - Label: `TOTAL PAYROLL` in Column A.
   - Formula in Column G: `=SUM(G5:G29)`.
   - Top border: Thin line; Bottom border: Accounting double underline.

### B. Data Sorting
- **Sort Key**: `Salary (INR)` column.
- **Order**: **Descending (Highest to Lowest)**.
- **Top Earner**: Amit Chouhan (System Architect, Engineering) — ₹115,000.00.
- **Lowest Earner**: Tanvi Bansal (Graduate Trainee, Unassigned) — ₹32,000.00.

### C. Filtering
- **AutoFilter**: Enabled across the range `A4:J29`.
- **Sample Analytical Filters**:
  1. *Filter by Department*: Select `Data Analytics` to view all 6 analytics team members.
  2. *Number Filter (Salary)*: `Salary >= ₹75,000` isolates senior staff and team leads.
  3. *City Filter*: Filter by `Indore` vs. `Bhopal` to analyze regional distribution.

---

## 3. Screenshot Capture Guide

- Open `Excel/Week_3_Excel_Data_Analytics.xlsx` in Microsoft Excel.
- Switch to sheet **`Task_6_Format_Sort_Filter`**.
- Take a clear screenshot of the table with the header row, currency formatting, and total row visible.
- Save image to: **`Screenshots/task_6_excel.png`**.
