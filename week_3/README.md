# Week 3 — SQL & Excel for Data Analytics

**Student:** Ayush  
**Course:** B.Tech CSE (IoT)  
**College:** Prestige Institute of Engineering, Management & Research, Indore  
**Assignment:** Week 3 — SQL & Excel for Data Analytics (Marks: 100)  

---

## Folder Structure

```
week_3/
│
├── Task_1_Introduction_SELECT/
│   ├── task_1.sql
│   └── task_1.py
│
├── Task_2_WHERE_ORDERBY_Aggregates/
│   ├── task_2.sql
│   └── task_2.py
│
├── Task_3_GROUPBY_HAVING/
│   ├── task_3.sql
│   └── task_3.py
│
├── Task_4_SQL_Joins/
│   ├── task_4.sql
│   └── task_4.py
│
├── Task_5_SQL_Subqueries/
│   ├── task_5.sql
│   └── task_5.py
│
├── Task_6_Excel_Formatting_Sorting_Filtering/
│   └── task_6_guide.md
│
├── Task_7_Excel_Conditional_Formatting_Functions/
│   └── task_7_guide.md
│
├── Task_8_Excel_VLOOKUP_XLOOKUP/
│   └── task_8_guide.md
│
├── Task_9_Excel_Pivot_Table_Charts/
│   └── task_9_guide.md
│
├── Database/
│   ├── schema.sql
│   ├── seed_data.sql
│   ├── init_db.py
│   └── company_analytics.db
│
├── Excel/
│   ├── create_excel_workbook.py
│   └── Week_3_Excel_Data_Analytics.xlsx
│
├── Screenshots/
│   ├── task_1_output.png
│   ├── task_2_output.png
│   ├── task_3_output.png
│   ├── task_4_output.png
│   ├── task_5_output.png
│   ├── task_6_excel.png
│   ├── task_7_excel.png
│   ├── task_8_excel.png
│   └── task_9_excel.png
│
├── run_all_sql_tasks.py
├── generate_report.py
├── requirements.txt
├── README.md
└── Week_3_SQL_Excel_Report.pdf
```

---

## Tasks Overview

### SQL Tasks (Tasks 1 to 5)
1. **Task 1: Introduction to Databases & SELECT Statement (10 Marks)**
   - Database architecture, `SELECT *`, specific column projection, column aliases (`AS`), and derived calculations (`Annual_Compensation`).
2. **Task 2: WHERE, ORDER BY & Aggregate Functions (15 Marks)**
   - Conditional filtering using `WHERE` (`=`, `>=`, `BETWEEN`, `IN`), multi-column sorting (`ORDER BY Salary DESC, Hire_Date ASC`), and aggregate statistics (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`).
3. **Task 3: GROUP BY & HAVING (10 Marks)**
   - Multi-department aggregation, calculating departmental headcount, average salary, and total payroll; group-level filtering with `HAVING AVG(Salary) > 65000` and `HAVING COUNT(*) >= 5`.
4. **Task 4: SQL Joins (15 Marks)**
   - `INNER JOIN`, `LEFT JOIN`, and `RIGHT JOIN` across `Employees` and `Departments`, demonstrating preservation of unassigned staff and unstaffed departments.
5. **Task 5: SQL Subqueries (10 Marks)**
   - Single-row scalar subquery (employees earning above company average), multi-row subquery with `IN` (employees in departments with budget > ₹800,000), and correlated subqueries (top earner per department).

### Excel Tasks (Tasks 6 to 9)
Workbook: `Excel/Week_3_Excel_Data_Analytics.xlsx`
6. **Task 6: Data Formatting, Sorting & Filtering (10 Marks)**
   - Sheet: `Task_6_Format_Sort_Filter` — Professional Navy headers, currency formatting (`₹#,##0.00`), zebra striping, descending salary sort, active auto-filters.
7. **Task 7: Conditional Formatting & Functions (15 Marks)**
   - Sheet: `Task_7_Conditional_Functions` — Automated category assignment using `=IF()`, department count with `=COUNTIF()`, payroll summation with `=SUMIF()`, and soft green/amber conditional highlights.
8. **Task 8: VLOOKUP & XLOOKUP (10 Marks)**
   - Sheet: `Task_8_VLOOKUP_XLOOKUP` — Side-by-side exact match lookups against reference catalog, demonstrating left-to-right lookups and XLOOKUP's native error handling and bi-directional advantages.
9. **Task 9: Pivot Table & Charts (5 Marks)**
   - Sheet: `Task_9_Pivot_and_Charts` — Pivot aggregation table and clustered column chart comparing Departmental Budgets vs. Monthly Payroll Expenditures, with analytical commentary.

---

## Installation & Running

Install dependencies:
```bash
pip install -r requirements.txt
```

Initialize the database:
```bash
python Database/init_db.py
```

Run all SQL tasks:
```bash
python run_all_sql_tasks.py
```

Generate the Excel workbook:
```bash
python Excel/create_excel_workbook.py
```

Generate or re-compile the PDF report:
```bash
python generate_report.py
```
