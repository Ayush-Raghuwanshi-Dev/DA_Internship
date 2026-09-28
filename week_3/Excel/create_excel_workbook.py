"""
Create a comprehensive, professional Microsoft Excel Workbook for Week 3:
Week_3_Excel_Data_Analytics.xlsx
Contains 4 dedicated worksheets for Tasks 6, 7, 8, and 9 with real formulas,
conditional formatting rules, cell styling, and an embedded Excel Bar Chart.
"""

from pathlib import Path
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule
from openpyxl.chart import BarChart, Reference

EXCEL_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = EXCEL_DIR / "Week_3_Excel_Data_Analytics.xlsx"

# Palette Tokens
NAVY_HEADER = "1E3A8A"
NAVY_LIGHT = "DBEAFE"
SLATE_HEADER = "1E293B"
ZEBRA_FILL = "F8FAFC"
WHITE = "FFFFFF"
BORDER_COLOR = "CBD5E1"
GREEN_BG = "D1FAE5"
GREEN_TXT = "065F46"
AMBER_BG = "FEF3C7"
AMBER_TXT = "92400E"

# Styles
font_header = Font(name="Calibri", size=11, bold=True, color=WHITE)
font_bold = Font(name="Calibri", size=10, bold=True)
font_regular = Font(name="Calibri", size=10)
font_title = Font(name="Calibri", size=14, bold=True, color="1E3A8A")
font_subtitle = Font(name="Calibri", size=10, italic=True, color="64748B")

fill_header = PatternFill(start_color=NAVY_HEADER, end_color=NAVY_HEADER, fill_type="solid")
fill_zebra = PatternFill(start_color=ZEBRA_FILL, end_color=ZEBRA_FILL, fill_type="solid")
fill_subtotal = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")

thin_border_side = Side(style='thin', color=BORDER_COLOR)
cell_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
thick_bottom = Border(bottom=Side(style='double', color='0F172A'), top=Side(style='thin', color=BORDER_COLOR))

# Raw Data
EMPLOYEES_DATA = [
    (121, "Amit", "Chouhan", 1, "Engineering", "System Architect", 115000.00, "2019-09-01", 5, "Indore"),
    (109, "Varun", "Deshmukh", 4, "Sales & Marketing", "Sales Manager", 92000.00, "2020-08-19", 5, "Bhopal"),
    (101, "Aarav", "Sharma", 1, "Engineering", "Senior Software Engineer", 88000.00, "2022-03-15", 5, "Indore"),
    (124, "Bhavna", "Rawat", 2, "Data Analytics", "Machine Learning Analyst", 88000.00, "2021-12-10", 5, "Indore"),
    (104, "Meera", "Rao", 2, "Data Analytics", "Senior Data Analyst", 85000.00, "2021-11-20", 5, "Indore"),
    (112, "Pooja", "Bhatia", 3, "Human Resources", "HR Manager", 82000.00, "2020-06-30", 5, "Indore"),
    (115, "Gaurav", "Yadav", 2, "Data Analytics", "Data Engineer", 80000.00, "2022-04-18", 4, "Indore"),
    (103, "Kabir", "Joshi", 1, "Engineering", "DevOps Engineer", 78000.00, "2022-07-01", 4, "Bhopal"),
    (111, "Manish", "Tiwari", 5, "Finance", "Senior Accountant", 75000.00, "2021-01-15", 4, "Bhopal"),
    (113, "Siddharth", "Malhotra", 1, "Engineering", "Backend Developer", 74000.00, "2022-12-01", 4, "Indore"),
    (110, "Ishita", "Chopra", 2, "Data Analytics", "BI Developer", 72000.00, "2022-10-05", 4, "Indore"),
    (107, "Aditya", "Mishra", 5, "Finance", "Financial Analyst", 66000.00, "2021-04-25", 4, "Indore"),
    (102, "Diya", "Patel", 2, "Data Analytics", "Data Analyst", 62000.00, "2023-01-10", 4, "Indore"),
    (108, "Neha", "Gupta", 1, "Engineering", "Frontend Developer", 60000.00, "2023-02-14", 3, "Indore"),
    (116, "Ananya", "Reddy", 1, "Engineering", "QA Automation Engineer", 59000.00, "2023-03-22", 4, "Bhopal"),
    (118, "Ritu", "Singhania", 4, "Sales & Marketing", "Business Development Exec", 58000.00, "2022-11-15", 4, "Indore"),
    (105, "Rohan", "Verma", 4, "Sales & Marketing", "Marketing Specialist", 54000.00, "2023-05-18", 3, "Indore"),
    (122, "Sanjana", "Bose", 4, "Sales & Marketing", "Digital Marketer", 53000.00, "2023-07-19", 4, "Bhopal"),
    (117, "Harsh", "Vardhan", 5, "Finance", "Accountant", 52000.00, "2023-08-01", 3, "Indore"),
    (114, "Kavya", "Saxena", 4, "Sales & Marketing", "Content Strategist", 51000.00, "2023-06-10", 3, "Bhopal"),
    (120, "Priyanka", "Dubey", 3, "Human Resources", "Talent Acquisition Exec", 49000.00, "2023-04-12", 3, "Indore"),
    (106, "Sneha", "Kulkarni", 3, "Human Resources", "HR Executive", 48000.00, "2022-09-12", 4, "Bhopal"),
    (123, "Nikhil", "Shukla", 5, "Finance", "Finance Executive", 48000.00, "2024-02-01", 3, "Indore"),
    (119, "Kunal", "Pandey", 2, "Data Analytics", "Junior Data Analyst", 45000.00, "2024-01-08", 3, "Bhopal"),
    (125, "Tanvi", "Bansal", None, "Unassigned", "Graduate Trainee", 32000.00, "2024-03-01", 3, "Indore"),
]

DEPARTMENTS_DATA = [
    (1, "Engineering", "Rajesh Sharma", "Indore", 1200000.00),
    (2, "Data Analytics", "Pooja Verma", "Indore", 850000.00),
    (3, "Human Resources", "Anjali Mehta", "Bhopal", 500000.00),
    (4, "Sales & Marketing", "Vikram Singh", "Indore", 950000.00),
    (5, "Finance", "Suresh Nair", "Bhopal", 750000.00),
    (6, "Research & Development", "Dr. Meena Iyer", "Indore", 1100000.00),
]


def auto_fit_columns(ws, min_width=12):
    for col in ws.columns:
        max_len = 0
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            val_str = str(cell.value or '')
            if cell.number_format and '₹' in cell.number_format:
                val_str += '   '
            max_len = max(max_len, len(val_str))
        ws.column_dimensions[col_letter].width = max(max_len + 3, min_width)


def build_task_6_sheet(wb):
    """Task 6: Data Formatting, Sorting & Filtering"""
    ws = wb.create_sheet(title="Task_6_Format_Sort_Filter")
    ws.views.sheetView[0].showGridLines = True

    # Title block
    ws["A1"] = "COMPANY EMPLOYEE DATASET — SORTED BY SALARY DESCENDING"
    ws["A1"].font = font_title
    ws["A2"] = "Task 6: Applied professional formatting, currency formatting, borders, and auto-filters."
    ws["A2"].font = font_subtitle

    headers = ["Emp ID", "First Name", "Last Name", "Dept ID", "Department", "Job Title", "Salary (INR)", "Hire Date", "Rating", "City"]
    ws.append([]) # row 3 blank
    ws.append(headers) # row 4
    
    header_row_idx = 4
    for col_idx in range(1, len(headers) + 1):
        cell = ws.cell(row=header_row_idx, column=col_idx)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = cell_border
    ws.row_dimensions[header_row_idx].height = 25

    # Add records (already sorted by salary descending)
    for i, emp in enumerate(EMPLOYEES_DATA):
        row_idx = header_row_idx + 1 + i
        ws.append(list(emp))
        for col_idx in range(1, len(headers) + 1):
            cell = ws.cell(row=row_idx, column=col_idx)
            cell.font = font_regular
            cell.border = cell_border
            if i % 2 == 1:
                cell.fill = fill_zebra
            
            # Alignments & formats
            if col_idx in (1, 4, 9):
                cell.alignment = Alignment(horizontal="center")
            elif col_idx == 7: # Salary
                cell.number_format = '₹#,##0.00'
                cell.alignment = Alignment(horizontal="right")
            elif col_idx == 8: # Hire Date
                cell.alignment = Alignment(horizontal="center")
            else:
                cell.alignment = Alignment(horizontal="left")

    # Total Row
    tot_row = header_row_idx + len(EMPLOYEES_DATA) + 1
    ws.cell(row=tot_row, column=1, value="TOTAL PAYROLL").font = font_bold
    ws.cell(row=tot_row, column=1).alignment = Alignment(horizontal="left")
    ws.cell(row=tot_row, column=7, value=f"=SUM(G5:G{tot_row-1})").font = font_bold
    ws.cell(row=tot_row, column=7).number_format = '₹#,##0.00'
    ws.cell(row=tot_row, column=7).alignment = Alignment(horizontal="right")
    
    for c in range(1, len(headers) + 1):
        cell = ws.cell(row=tot_row, column=c)
        cell.border = thick_bottom
        cell.fill = fill_subtotal

    # Enable AutoFilter
    ws.auto_filter.ref = f"A{header_row_idx}:J{tot_row-1}"
    auto_fit_columns(ws)


def build_task_7_sheet(wb):
    """Task 7: Conditional Formatting & Excel Functions (IF, COUNTIF, SUMIF)"""
    ws = wb.create_sheet(title="Task_7_Conditional_Functions")
    ws.views.sheetView[0].showGridLines = True

    ws["A1"] = "EMPLOYEE PERFORMANCE & PAYROLL FUNCTIONS"
    ws["A1"].font = font_title
    ws["A2"] = "Task 7: Demonstrating IF(), COUNTIF(), SUMIF() functions and conditional formatting rules."
    ws["A2"].font = font_subtitle

    headers = ["Emp ID", "Employee Name", "Department", "Job Title", "Salary (INR)", "Rating", "Salary Category (IF)"]
    ws.append([])
    ws.append(headers)

    header_row_idx = 4
    for col_idx in range(1, len(headers) + 1):
        cell = ws.cell(row=header_row_idx, column=col_idx)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = cell_border
    ws.row_dimensions[header_row_idx].height = 25

    for i, emp in enumerate(EMPLOYEES_DATA):
        row_idx = header_row_idx + 1 + i
        full_name = f"{emp[1]} {emp[2]}"
        # IF formula: =IF(E{row}>=75000, "High Earner", "Standard")
        if_formula = f'=IF(E{row_idx}>=75000, "High Earner", "Standard")'
        row_vals = [emp[0], full_name, emp[4], emp[5], emp[6], emp[8], if_formula]
        ws.append(row_vals)
        for col_idx in range(1, len(headers) + 1):
            cell = ws.cell(row=row_idx, column=col_idx)
            cell.font = font_regular
            cell.border = cell_border
            if i % 2 == 1:
                cell.fill = fill_zebra
            if col_idx in (1, 6):
                cell.alignment = Alignment(horizontal="center")
            elif col_idx == 5:
                cell.number_format = '₹#,##0.00'
                cell.alignment = Alignment(horizontal="right")
            elif col_idx == 7:
                cell.alignment = Alignment(horizontal="center")
            else:
                cell.alignment = Alignment(horizontal="left")

    # Add Summary Functions Table on the right side (Cols I to L)
    ws["I4"] = "EXCEL FUNCTIONS SUMMARY DASHBOARD"
    ws["I4"].font = font_header
    ws["I4"].fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
    ws.merge_cells("I4:L4")
    ws["I4"].alignment = Alignment(horizontal="center")

    func_headers = ["Metric Description", "Excel Formula Applied", "Calculated Result"]
    ws["I5"] = func_headers[0]; ws["J5"] = ""; ws.merge_cells("I5:J5")
    ws["K5"] = func_headers[1]
    ws["L5"] = func_headers[2]
    for c in ["I5", "J5", "K5", "L5"]:
        ws[c].font = font_bold
        ws[c].fill = fill_subtotal
        ws[c].border = cell_border

    function_rows = [
        ("Engineering Headcount", "=COUNTIF(C5:C29, \"Engineering\")", '0'),
        ("Data Analytics Headcount", "=COUNTIF(C5:C29, \"Data Analytics\")", '0'),
        ("Sales & Marketing Headcount", "=COUNTIF(C5:C29, \"Sales & Marketing\")", '0'),
        ("Finance Headcount", "=COUNTIF(C5:C29, \"Finance\")", '0'),
        ("HR Headcount", "=COUNTIF(C5:C29, \"Human Resources\")", '0'),
        ("High Performers (Rating = 5)", "=COUNTIF(F5:F29, 5)", '0'),
        ("Engineering Total Payroll", "=SUMIF(C5:C29, \"Engineering\", E5:E29)", '₹#,##0.00'),
        ("Data Analytics Total Payroll", "=SUMIF(C5:C29, \"Data Analytics\", E5:E29)", '₹#,##0.00'),
        ("High Earners Count", "=COUNTIF(G5:G29, \"High Earner\")", '0'),
    ]

    for idx, (label, formula, num_fmt) in enumerate(function_rows):
        r = 6 + idx
        ws[f"I{r}"] = label
        ws.merge_cells(f"I{r}:J{r}")
        ws[f"K{r}"] = f"'{formula}" # display formula as text
        ws[f"L{r}"] = formula        # execute formula
        
        ws[f"I{r}"].font = font_regular
        ws[f"K{r}"].font = Font(name="Consolas", size=9, color="1E3A8A")
        ws[f"L{r}"].font = font_bold
        ws[f"L{r}"].number_format = num_fmt
        
        for c in [f"I{r}", f"J{r}", f"K{r}", f"L{r}"]:
            ws[c].border = cell_border
            ws[c].fill = PatternFill(start_color="FAFAFA", end_color="FAFAFA", fill_type="solid")

    # Conditional Formatting: Highlight Salary >= 75000 in light green
    green_rule = CellIsRule(operator='greaterThanOrEqual', formula=['75000'],
                            fill=PatternFill(start_color=GREEN_BG, end_color=GREEN_BG, fill_type='solid'),
                            font=Font(color=GREEN_TXT, bold=True))
    ws.conditional_formatting.add("E5:E29", green_rule)

    # Highlight Rating = 5 in soft amber
    amber_rule = CellIsRule(operator='equal', formula=['5'],
                            fill=PatternFill(start_color=AMBER_BG, end_color=AMBER_BG, fill_type='solid'),
                            font=Font(color=AMBER_TXT, bold=True))
    ws.conditional_formatting.add("F5:F29", amber_rule)

    auto_fit_columns(ws)


def build_task_8_sheet(wb):
    """Task 8: VLOOKUP & XLOOKUP Functions"""
    ws = wb.create_sheet(title="Task_8_VLOOKUP_XLOOKUP")
    ws.views.sheetView[0].showGridLines = True

    ws["A1"] = "RELATIONAL LOOKUPS: VLOOKUP vs. XLOOKUP"
    ws["A1"].font = font_title
    ws["A2"] = "Task 8: Demonstrating exact-match vertical lookup (VLOOKUP) and modern bi-directional lookup (XLOOKUP)."
    ws["A2"].font = font_subtitle

    # Main Transaction Table (Left: A to F)
    headers_main = ["Emp ID", "Employee Name", "Dept ID", "Salary", "Department Name (VLOOKUP)", "Manager Name (XLOOKUP)"]
    ws.append([])
    ws.append(headers_main)

    header_row_idx = 4
    for col_idx in range(1, len(headers_main) + 1):
        cell = ws.cell(row=header_row_idx, column=col_idx)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = cell_border
    ws.row_dimensions[header_row_idx].height = 25

    # Department Reference Table (Right: I to M)
    headers_ref = ["Dept ID", "Department Name", "Manager Name", "Location", "Budget (INR)"]
    for col_idx, h in enumerate(headers_ref, start=9):
        cell = ws.cell(row=header_row_idx, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = PatternFill(start_color=SLATE_HEADER, end_color=SLATE_HEADER, fill_type="solid")
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = cell_border

    # Populate Reference Table
    for r_idx, dept in enumerate(DEPARTMENTS_DATA, start=5):
        for c_idx, val in enumerate(dept, start=9):
            cell = ws.cell(row=r_idx, column=c_idx, value=val)
            cell.font = font_regular
            cell.border = cell_border
            if c_idx == 9:
                cell.alignment = Alignment(horizontal="center")
            elif c_idx == 13:
                cell.number_format = '₹#,##0.00'
                cell.alignment = Alignment(horizontal="right")

    # Populate Main Table with VLOOKUP and XLOOKUP formulas
    for i, emp in enumerate(EMPLOYEES_DATA):
        r_idx = header_row_idx + 1 + i
        full_name = f"{emp[1]} {emp[2]}"
        dept_id = emp[3]
        
        if dept_id is not None:
            # VLOOKUP: =VLOOKUP(C{row}, $I$5:$M$10, 2, FALSE)
            vlookup_f = f'=VLOOKUP(C{r_idx}, $I$5:$M$10, 2, FALSE)'
            # XLOOKUP: =XLOOKUP(C{row}, $I$5:$I$10, $K$5:$K$10, "Unassigned")
            xlookup_f = f'=XLOOKUP(C{r_idx}, $I$5:$I$10, $K$5:$K$10, "Unassigned")'
        else:
            vlookup_f = "N/A (No Dept)"
            xlookup_f = '=XLOOKUP(C29, $I$5:$I$10, $K$5:$K$10, "Unassigned")'

        row_vals = [emp[0], full_name, dept_id if dept_id is not None else "None", emp[6], vlookup_f, xlookup_f]
        ws.append(row_vals)

        for col_idx in range(1, len(headers_main) + 1):
            cell = ws.cell(row=r_idx, column=col_idx)
            cell.font = font_regular
            cell.border = cell_border
            if i % 2 == 1:
                cell.fill = fill_zebra
            if col_idx in (1, 3):
                cell.alignment = Alignment(horizontal="center")
            elif col_idx == 4:
                cell.number_format = '₹#,##0.00'
                cell.alignment = Alignment(horizontal="right")
            else:
                cell.alignment = Alignment(horizontal="left")

    # Educational Commentary Box below Reference Table
    comp_row = 12
    ws[f"I{comp_row}"] = "VLOOKUP vs. XLOOKUP FEATURE COMPARISON"
    ws[f"I{comp_row}"].font = font_bold
    ws[f"I{comp_row}"].fill = fill_subtotal
    ws.merge_cells(f"I{comp_row}:M{comp_row}")
    
    comparisons = [
        ("Feature", "VLOOKUP", "XLOOKUP"),
        ("Lookup Direction", "Left-to-Right Only", "Any Direction (Left, Right, Up, Down)"),
        ("Column Insertion Risk", "Breaks when columns change", "Resilient; uses direct range references"),
        ("Default Match Mode", "Approximate (requires FALSE)", "Exact Match by default"),
        ("Error Handling", "Requires nesting in IFERROR()", "Built-in [if_not_found] parameter"),
        ("Performance", "Slower on large tables", "Significantly faster and lightweight"),
    ]
    for offset, (feat, v_val, x_val) in enumerate(comparisons):
        curr_r = comp_row + 1 + offset
        ws[f"I{curr_r}"] = feat
        ws[f"J{curr_r}"] = v_val; ws.merge_cells(f"J{curr_r}:K{curr_r}")
        ws[f"L{curr_r}"] = x_val; ws.merge_cells(f"L{curr_r}:M{curr_r}")
        for c in [f"I{curr_r}", f"J{curr_r}", f"K{curr_r}", f"L{curr_r}", f"M{curr_r}"]:
            ws[c].border = cell_border
            if offset == 0:
                ws[c].font = font_bold
                ws[c].fill = fill_subtotal
            else:
                ws[c].font = font_regular

    auto_fit_columns(ws)


def build_task_9_sheet(wb):
    """Task 9: Pivot Table & Excel Charts"""
    ws = wb.create_sheet(title="Task_9_Pivot_and_Charts")
    ws.views.sheetView[0].showGridLines = True

    ws["A1"] = "DEPARTMENTAL ANALYTICS SUMMARY & BUDGET CHART"
    ws["A1"].font = font_title
    ws["A2"] = "Task 9: Aggregated Pivot Table summary and budget vs. actual payroll chart."
    ws["A2"].font = font_subtitle

    # Summary Table Headers
    headers = ["Department ID", "Department Name", "Headcount", "Total Payroll (INR)", "Average Salary (INR)", "Allocated Budget (INR)", "Budget Utilization %"]
    ws.append([])
    ws.append(headers)

    header_row_idx = 4
    for col_idx in range(1, len(headers) + 1):
        cell = ws.cell(row=header_row_idx, column=col_idx)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = cell_border
    ws.row_dimensions[header_row_idx].height = 25

    summary_data = [
        (1, "Engineering", 6, 474000.00, 79000.00, 1200000.00, "=D5/F5"),
        (2, "Data Analytics", 6, 432000.00, 72000.00, 850000.00, "=D6/F6"),
        (3, "Human Resources", 3, 179000.00, 59666.67, 500000.00, "=D7/F7"),
        (4, "Sales & Marketing", 5, 308000.00, 61600.00, 950000.00, "=D8/F8"),
        (5, "Finance", 4, 241000.00, 60250.00, 750000.00, "=D9/F9"),
        (6, "Research & Development", 0, 0.00, 0.00, 1100000.00, "=D10/F10"),
    ]

    for idx, row in enumerate(summary_data):
        r_idx = header_row_idx + 1 + idx
        ws.append(list(row))
        for col_idx in range(1, len(headers) + 1):
            cell = ws.cell(row=r_idx, column=col_idx)
            cell.font = font_regular
            cell.border = cell_border
            if idx % 2 == 1:
                cell.fill = fill_zebra
            if col_idx in (1, 3):
                cell.alignment = Alignment(horizontal="center")
            elif col_idx in (4, 5, 6):
                cell.number_format = '₹#,##0.00'
                cell.alignment = Alignment(horizontal="right")
            elif col_idx == 7:
                cell.number_format = '0.0%'
                cell.alignment = Alignment(horizontal="right")
            else:
                cell.alignment = Alignment(horizontal="left")

    # Total Row
    tot_r = header_row_idx + len(summary_data) + 1
    ws.cell(row=tot_r, column=1, value="COMPANY TOTAL").font = font_bold
    ws.cell(row=tot_r, column=3, value=f"=SUM(C5:C{tot_r-1})").font = font_bold
    ws.cell(row=tot_r, column=4, value=f"=SUM(D5:D{tot_r-1})").font = font_bold
    ws.cell(row=tot_r, column=4).number_format = '₹#,##0.00'
    ws.cell(row=tot_r, column=5, value=f"=AVERAGE(E5:E{tot_r-1})").font = font_bold
    ws.cell(row=tot_r, column=5).number_format = '₹#,##0.00'
    ws.cell(row=tot_r, column=6, value=f"=SUM(F5:F{tot_r-1})").font = font_bold
    ws.cell(row=tot_r, column=6).number_format = '₹#,##0.00'
    ws.cell(row=tot_r, column=7, value=f"=D{tot_r}/F{tot_r}").font = font_bold
    ws.cell(row=tot_r, column=7).number_format = '0.0%'

    for c in range(1, len(headers) + 1):
        ws.cell(row=tot_r, column=c).border = thick_bottom
        ws.cell(row=tot_r, column=c).fill = fill_subtotal

    # Add Bar Chart
    chart = BarChart()
    chart.type = "col"
    chart.style = 10
    chart.title = "Department Payroll Expenditure vs. Total Budget"
    chart.y_axis.title = "Amount in INR (₹)"
    chart.x_axis.title = "Department"
    chart.width = 16
    chart.height = 10

    # Data: Total Payroll (Col D) and Budget (Col F)
    # Categories: Dept Names (Col B)
    data = Reference(ws, min_col=4, min_row=4, max_col=6, max_row=10)
    # We want Col D (Payroll) and Col F (Budget). Let's construct chart reference cleanly:
    categories = Reference(ws, min_col=2, min_row=5, max_row=10)
    
    # Adding series individually for clean labels
    payroll_data = Reference(ws, min_col=4, min_row=4, max_row=10)
    budget_data = Reference(ws, min_col=6, min_row=4, max_row=10)
    
    chart.add_data(payroll_data, titles_from_data=True)
    chart.add_data(budget_data, titles_from_data=True)
    chart.set_categories(categories)

    ws.add_chart(chart, "A14")

    # Analytical Commentary Box
    ws["I14"] = "CHART ANALYSIS & BUSINESS INSIGHTS"
    ws["I14"].font = font_bold
    ws["I14"].fill = fill_subtotal
    ws.merge_cells("I14:M14")

    commentary = [
        ("1. Headcount & Payroll Leader:", "Engineering incurs the highest monthly payroll (₹474,000) with 6 staff."),
        ("2. Highest Budget Allocation:", "Engineering holds the largest budget (₹1.2M), followed by R&D (₹1.1M)."),
        ("3. Budget Utilization:", "All active departments operate comfortably within allocation (utilization ranges 32% to 51%)."),
        ("4. Unstaffed Department:", "R&D has a ₹1.1M budget but currently 0 employees, representing planned future hiring."),
        ("5. Average Compensation:", "Engineering (₹79,000) and Data Analytics (₹72,000) lead in average employee remuneration.")
    ]
    for offset, (pt, desc) in enumerate(commentary):
        curr_r = 15 + offset
        ws[f"I{curr_r}"] = pt
        ws[f"I{curr_r}"].font = font_bold
        ws[f"J{curr_r}"] = desc
        ws.merge_cells(f"J{curr_r}:M{curr_r}")
        ws[f"J{curr_r}"].font = font_regular
        for col_name in ["I", "J", "K", "L", "M"]:
            ws[f"{col_name}{curr_r}"].border = cell_border

    auto_fit_columns(ws)


def main():
    print("=" * 70)
    print("GENERATING EXCEL WORKBOOK: Week_3_Excel_Data_Analytics.xlsx")
    print("=" * 70)

    wb = openpyxl.Workbook()
    # Remove default sheet
    default_sheet = wb.active
    wb.remove(default_sheet)

    print("Building Sheet 1: Task_6_Format_Sort_Filter...")
    build_task_6_sheet(wb)

    print("Building Sheet 2: Task_7_Conditional_Functions...")
    build_task_7_sheet(wb)

    print("Building Sheet 3: Task_8_VLOOKUP_XLOOKUP...")
    build_task_8_sheet(wb)

    print("Building Sheet 4: Task_9_Pivot_and_Charts...")
    build_task_9_sheet(wb)

    wb.save(OUTPUT_FILE)
    print(f"\nWorkbook saved successfully to: {OUTPUT_FILE.name}")
    print("=" * 70)


if __name__ == "__main__":
    main()
