# Task 9: Excel Pivot Table & Charts

**Student:** Ayush  
**Course:** B.Tech CSE (IoT)  
**College:** Prestige Institute of Engineering, Management & Research, Indore  
**Workbook:** `Excel/Week_3_Excel_Data_Analytics.xlsx`  
**Sheet:** `Task_9_Pivot_and_Charts`  

---

## 1. Task Objective

To aggregate multi-dimensional company employee and departmental data using Pivot Table mechanics, construct a comparative Clustered Column Chart, and analyze corporate budget utilization versus actual payroll commitments.

---

## 2. Pivot Summary Table Structure

The Pivot Summary aggregates employee metrics across all 6 company departments:

| Dept ID | Department Name | Headcount | Total Payroll (INR) | Average Salary (INR) | Allocated Budget (INR) | Budget Utilization % |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **1** | Engineering | 6 | ₹474,000.00 | ₹79,000.00 | ₹1,200,000.00 | 39.5% |
| **2** | Data Analytics | 6 | ₹432,000.00 | ₹72,000.00 | ₹850,000.00 | 50.8% |
| **3** | Human Resources | 3 | ₹179,000.00 | ₹59,666.67 | ₹500,000.00 | 35.8% |
| **4** | Sales & Marketing | 5 | ₹308,000.00 | ₹61,600.00 | ₹950,000.00 | 32.4% |
| **5** | Finance | 4 | ₹241,000.00 | ₹60,250.00 | ₹750,000.00 | 32.1% |
| **6** | Research & Development | 0 | ₹0.00 | ₹0.00 | ₹1,100,000.00 | 0.0% |
| **TOTAL**| **COMPANY TOTAL** | **24** | **₹1,634,000.00** | **₹68,083.33** | **₹5,350,000.00** | **30.5%** |

*(Note: Excludes unassigned trainee 125 with ₹32,000 payroll, bringing total company payroll to ₹1,666,000.00).*

---

## 3. Clustered Column Chart Design

- **Chart Title**: `Department Payroll Expenditure vs. Total Budget`
- **Chart Type**: Clustered Column (2D Bar Chart)
- **Series 1 (Blue Columns)**: `Total Payroll (INR)` (Monthly actuals)
- **Series 2 (Dark Slate / Orange Columns)**: `Allocated Budget (INR)` (Department fiscal ceiling)
- **X-Axis Category**: Department Name
- **Y-Axis Values**: Financial Amount in Indian Rupees (₹)

---

## 4. Analytical Findings & Business Interpretation

1. **Top Payroll Driver**:
   - **Engineering** accounts for the single highest monthly payroll expenditure (₹474,000.00), closely followed by **Data Analytics** (₹432,000.00). Together, these two technical divisions constitute 55.4% of total departmental payroll.
2. **Highest Budget Allocation**:
   - Engineering commands the largest departmental budget at ₹1,200,000.00, reflecting major infrastructure, cloud computing, and software licensing requirements.
3. **Fiscal Runway & Safety Margin**:
   - All operating departments run well within their allocated budgets. **Data Analytics** has the highest budget utilization at 50.8%, while **Sales & Marketing** and **Finance** maintain conservative utilization rates of ~32%.
4. **Strategic Reserve in R&D**:
   - **Research & Development** holds a ₹1,100,000.00 budget allocation with zero current staff. This highlights an intentional strategic growth initiative where talent recruitment is scheduled for subsequent quarters.

---

## 5. Screenshot Capture Guide

- Open `Excel/Week_3_Excel_Data_Analytics.xlsx`.
- Switch to sheet **`Task_9_Pivot_and_Charts`**.
- Capture the Summary Table alongside the **Department Payroll vs. Budget Bar Chart** and the insight box.
- Save image to: **`Screenshots/task_9_excel.png`**.
