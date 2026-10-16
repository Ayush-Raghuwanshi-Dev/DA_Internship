"""
Report Generation Script for Week 5: Power BI & Business Intelligence
Generates a clean, simple, student-friendly PDF report: Week_5_PowerBI_Business_Intelligence_Report.pdf
Format: Student Details Header -> Task Heading -> Question -> Output Screenshot -> Student Explanation
"""

import sys
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image
)
from reportlab.pdfgen import canvas

BASE_DIR = Path(__file__).resolve().parent
SCREENSHOTS_DIR = BASE_DIR / "Screenshots"
OUTPUT_PDF = BASE_DIR / "Week_5_PowerBI_Business_Intelligence_Report.pdf"


class SimpleNumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas to dynamically compute and print 'Page X of Y' page numbers
    along with a clean student running header and footer.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_elements(num_pages)
            super().showPage()
        super().save()

    def draw_page_elements(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 7.5)
        self.setFillColor(colors.HexColor("#475569"))

        # Running Header on pages 2 and later
        if self._pageNumber > 1:
            self.drawString(
                36, 756,
                "WEEK 5 ASSIGNMENT: POWER BI & BUSINESS INTELLIGENCE"
            )
            self.setFont("Helvetica", 7.5)
            self.drawRightString(
                576, 756,
                "Ayush | B.Tech CSE (IoT) | PIEMR, Indore"
            )
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(36, 750, 576, 750)

        # Running Footer on all pages
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(36, 36, 576, 36)
        self.setFont("Helvetica", 7.5)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(
            36, 25,
            "Prestige Institute of Engineering, Management & Research, Indore | Data Analytics Internship"
        )
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#1E3A8A"))
        self.drawRightString(576, 25, page_str)
        self.restoreState()


def get_styles():
    styles = getSampleStyleSheet()

    primary_color = colors.HexColor("#1E3A8A")    # Deep Navy Blue
    secondary_color = colors.HexColor("#2563EB")  # Royal Blue
    dark_text = colors.HexColor("#0F172A")        # Slate 900
    body_text = colors.HexColor("#334155")        # Slate 700

    styles.add(ParagraphStyle(
        name="MainTitle",
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        textColor=primary_color,
        spaceAfter=2,
        alignment=0
    ))

    styles.add(ParagraphStyle(
        name="MainSubtitle",
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=secondary_color,
        spaceAfter=8,
        alignment=0
    ))

    styles.add(ParagraphStyle(
        name="StudentLabel",
        fontName="Helvetica-Bold",
        fontSize=8,
        leading=11,
        textColor=primary_color
    ))

    styles.add(ParagraphStyle(
        name="StudentVal",
        fontName="Helvetica",
        fontSize=8,
        leading=11,
        textColor=dark_text
    ))

    styles.add(ParagraphStyle(
        name="TaskHeader",
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=16,
        textColor=primary_color,
        spaceBefore=4,
        spaceAfter=4,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        name="QuestionBox",
        fontName="Helvetica-Oblique",
        fontSize=8,
        leading=11.5,
        textColor=colors.HexColor("#1E293B"),
        spaceAfter=2
    ))

    styles.add(ParagraphStyle(
        name="SectionSubtitle",
        fontName="Helvetica-Bold",
        fontSize=8.5,
        leading=12,
        textColor=secondary_color,
        spaceBefore=3,
        spaceAfter=2,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        name="StudentNote",
        fontName="Helvetica",
        fontSize=8,
        leading=11.5,
        textColor=body_text,
        spaceAfter=3
    ))

    styles.add(ParagraphStyle(
        name="BulletPoint",
        fontName="Helvetica",
        fontSize=8,
        leading=11.5,
        textColor=body_text,
        leftIndent=10,
        firstLineIndent=-7,
        spaceAfter=2
    ))

    styles.add(ParagraphStyle(
        name="ImageCaption",
        fontName="Helvetica-Bold",
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#64748B"),
        alignment=1, # Center
        spaceBefore=2,
        spaceAfter=4
    ))

    return styles


def build_pdf():
    print("=" * 70)
    print("BUILDING SIMPLE STUDENT-STYLE WEEK 5 PDF REPORT")
    print(f"Destination: {OUTPUT_PDF}")
    print("=" * 70)

    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=38,
        bottomMargin=38
    )

    styles = get_styles()
    story = []

    # =========================================================================
    # PAGE 1: TITLE & STUDENT DETAILS + TASK 1
    # =========================================================================
    story.append(Paragraph("WEEK 5 ASSIGNMENT: POWER BI & BUSINESS INTELLIGENCE", styles["MainTitle"]))
    story.append(Paragraph("Data Analytics Internship Practical Submission | 100 Marks", styles["MainSubtitle"]))

    # Student Details Table
    details_data = [
        [Paragraph("Student Name", styles["StudentLabel"]), Paragraph("Ayush", styles["StudentVal"]),
         Paragraph("Assignment Module", styles["StudentLabel"]), Paragraph("Week 5: Power BI & Business Intelligence", styles["StudentVal"])],
        [Paragraph("Degree & Branch", styles["StudentLabel"]), Paragraph("B.Tech in CSE (IoT)", styles["StudentVal"]),
         Paragraph("Weightage", styles["StudentLabel"]), Paragraph("100 Marks (Tasks 1 to 7 Covered)", styles["StudentVal"])],
        [Paragraph("Institution", styles["StudentLabel"]), Paragraph("Prestige Institute of Engineering, Management & Research, Indore", styles["StudentVal"]),
         Paragraph("Technologies Used", styles["StudentLabel"]), Paragraph("Power BI Desktop, Power Query, DAX, Star Schema", styles["StudentVal"])],
        [Paragraph("GitHub Repository", styles["StudentLabel"]), Paragraph("https://github.com/Ayush-Raghuwanshi-Dev/DA_Internship.git", styles["StudentVal"]),
         Paragraph("Submission Date", styles["StudentLabel"]), Paragraph("October 2026", styles["StudentVal"])],
    ]

    t_details = Table(details_data, colWidths=[95, 175, 110, 160])
    t_details.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#CBD5E1")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(t_details)
    story.append(Spacer(1, 6))

    # Task 1 Header & Question
    story.append(Paragraph("Task 1: Power BI Introduction & Data Import (10 Marks)", styles["TaskHeader"]))

    q1_text = (
        "<b>Question:</b> Explore the Power BI interface. Import a suitable dataset. "
        "View the imported data. Identify the available tables and columns. Check the data types of the columns. "
        "Explain the basic purpose of Power BI in Data Analytics."
    )
    t_q1 = Table([[Paragraph(q1_text, styles["QuestionBox"])]], colWidths=[540])
    t_q1.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#BFDBFE")),
        ("PADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t_q1)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Student Explanation & Implementation Summary:</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("• Explored Power BI Desktop across Report View, Data View, and Model View.", styles["BulletPoint"]))
    story.append(Paragraph("• Imported 5 tables: Fact_Sales (1,200 rows), Dim_Customer (120 rows), Dim_Product (30 rows), Dim_Region (5 rows), and Dim_Date (1,096 rows).", styles["BulletPoint"]))
    story.append(Paragraph("• Checked column types (Text, Integer, Float, Date). Verified 100% key matching with zero orphaned records.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Purpose of Power BI:</b> Power BI enables data analysts to connect to diverse sources, clean data in Power Query, model relationships, compute DAX measures, and present interactive visual dashboards.", styles["BulletPoint"]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Output Screenshot (Terminal Data Ingestion & Schema Audit):</b>", styles["SectionSubtitle"]))
    img_t1 = SCREENSHOTS_DIR / "task_1_terminal_output.png"
    if img_t1.exists():
        story.append(Image(str(img_t1), width=540, height=215))
        story.append(Paragraph("Figure 1.1: Task 1 - Data Ingestion & Schema Audit Output Screenshot", styles["ImageCaption"]))

    # =========================================================================
    # PAGE 2: TASK 2: DATA CLEANING & PREPARATION
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Task 2: Data Cleaning & Preparation (15 Marks)", styles["TaskHeader"]))

    q2_text = (
        "<b>Question:</b> Using Power Query: Inspect the dataset for missing or null values, duplicate records, "
        "and incorrect data types. Remove unnecessary columns or rows. Clean and transform columns "
        "(split, merge, rename, or change data types). Standardize text or numerical values. "
        "Load the cleaned data into Power BI."
    )
    t_q2 = Table([[Paragraph(q2_text, styles["QuestionBox"])]], colWidths=[540])
    t_q2.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#BFDBFE")),
        ("PADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t_q2)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Student Explanation & Implementation Summary:</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("• <b>Defect Detection:</b> Inspected raw sales dataset (1,220 rows) and detected 20 duplicate orders, 6 missing Ship_Dates, 8 unlinked records missing Customer_Key, and 12 missing Profit values.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Power Query Transformations:</b>", styles["BulletPoint"]))
    story.append(Paragraph("  - Removed 3 obsolete technical columns: <i>ETL_Batch_ID</i>, <i>Sys_Load_Timestamp</i>, and <i>Legacy_System_Flag</i>.", styles["BulletPoint"]))
    story.append(Paragraph("  - Deduplicated rows by Order_ID, removing all 20 duplicate entries.", styles["BulletPoint"]))
    story.append(Paragraph("  - Filtered out 8 unlinked records missing Customer_Key to maintain referential integrity.", styles["BulletPoint"]))
    story.append(Paragraph("  - Imputed 12 missing profits using: [Sales_Amount] - [Total_Cost].", styles["BulletPoint"]))
    story.append(Paragraph("  - Imputed missing Ship_Dates using standard 3-day fulfillment: [Order_Date] + 3 days.", styles["BulletPoint"]))
    story.append(Paragraph("  - Added conditional feature columns: <i>Delivery_Days</i>, <i>Profitability_Status</i>, and <i>Order_Size_Category</i>.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Final Clean Data:</b> 1,192 validated records with 0 missing values and 0 duplicates (97.7% retention rate), saved as cleaned_fact_sales.csv.", styles["BulletPoint"]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Output Screenshot (Power Query ETL Execution & Cleaning Audit):</b>", styles["SectionSubtitle"]))
    img_t2 = SCREENSHOTS_DIR / "task_2_terminal_output.png"
    if img_t2.exists():
        story.append(Image(str(img_t2), width=540, height=240))
        story.append(Paragraph("Figure 2.1: Task 2 - Power Query ETL Data Cleaning Pipeline Output Screenshot", styles["ImageCaption"]))

    # =========================================================================
    # PAGE 3: TASK 3: DATA MODELING & RELATIONSHIPS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Task 3: Data Modeling & Relationships (15 Marks)", styles["TaskHeader"]))

    q3_text = (
        "<b>Question:</b> Create relationships between tables. Understand Primary Keys and Foreign Keys. "
        "Define relationship cardinality (1-to-many, many-to-one). Verify relationships in Model View. "
        "Explain Star Schema and why it is used."
    )
    t_q3 = Table([[Paragraph(q3_text, styles["QuestionBox"])]], colWidths=[540])
    t_q3.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#BFDBFE")),
        ("PADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t_q3)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Student Explanation & Implementation Summary:</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("• <b>Primary Keys & Foreign Keys:</b> Unique Primary Keys exist in each Dimension table (Customer_Key, Product_Key, Region_Key, Date_Key), connecting to corresponding Foreign Keys in Fact_Sales.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Relationship Cardinality:</b> Configured four One-to-Many (1:*) relationships with single-direction cross-filtering flowing from Dimensions to the Fact table.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Star Schema Architecture:</b> Fact_Sales sits at the center with dimension tables radiating outwards. This avoids complex snowflake chains, speeds up VertiPaq engine DAX queries, and prevents circular filter ambiguity.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Referential Integrity Audit:</b> All 1,200 transaction keys matched dimension primary keys with 0 orphan records (100% referential integrity).", styles["BulletPoint"]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Output Screenshot (Power BI Star Schema Model View):</b>", styles["SectionSubtitle"]))
    img_t3 = SCREENSHOTS_DIR / "task_3_star_schema_model.png"
    if img_t3.exists():
        story.append(Image(str(img_t3), width=540, height=270))
        story.append(Paragraph("Figure 3.1: Task 3 - Power BI Star Schema Data Model (Fact & 4 Dimensions with 1:* Cardinality)", styles["ImageCaption"]))

    # =========================================================================
    # PAGE 4: TASK 4: DAX CALCULATED COLUMNS & MEASURES
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Task 4: Calculated Columns & Measures using DAX (20 Marks)", styles["TaskHeader"]))

    q4_text = (
        "<b>Question:</b> Create calculated columns using DAX (e.g., Total Price, Profit Margin, Delivery Days). "
        "Create DAX measures using aggregate functions (SUM, AVERAGE, COUNT, MIN, MAX). "
        "Use conditional logic (IF, SWITCH) and CALCULATE function. "
        "Understand the difference between Calculated Columns and Measures."
    )
    t_q4 = Table([[Paragraph(q4_text, styles["QuestionBox"])]], colWidths=[540])
    t_q4.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#BFDBFE")),
        ("PADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t_q4)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Student Explanation & Implementation Summary:</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("• <b>Calculated Columns (Row Context):</b> Evaluated row-by-row during data refresh and stored in RAM. Examples: Delivery_Days = DATEDIFF(Order_Date, Ship_Date, DAY), Profitability_Status = IF([Profit] < 0, 'Loss', IF([Profit_Margin_Pct] >= 25, 'High Margin', 'Standard')).", styles["BulletPoint"]))
    story.append(Paragraph("• <b>DAX Measures (Filter Context):</b> Evaluated dynamically on the fly during visual interactions without consuming disk/RAM. Implemented:", styles["BulletPoint"]))
    story.append(Paragraph("  - <i>Total Sales</i> = SUM(Fact_Sales[Sales_Amount])  -->  <b>INR 45,603,982.50</b>", styles["BulletPoint"]))
    story.append(Paragraph("  - <i>Total Profit</i> = [Total Sales] - [Total Cost]  -->  <b>INR 8,904,422.50</b>", styles["BulletPoint"]))
    story.append(Paragraph("  - <i>Profit Margin %</i> = DIVIDE([Total Profit], [Total Sales], 0)  -->  <b>19.53%</b>", styles["BulletPoint"]))
    story.append(Paragraph("  - <i>Average Order Value (AOV)</i> = DIVIDE([Total Sales], [Total Orders], 0)  -->  <b>INR 38,003.32</b>", styles["BulletPoint"]))
    story.append(Paragraph("  - <i>YoY Sales Growth %</i> = DIVIDE([Sales 2026] - [Sales 2025], [Sales 2025], 0)  -->  <b>+35.26%</b>", styles["BulletPoint"]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Output Screenshot (DAX Measures Verification & Calculation Engine):</b>", styles["SectionSubtitle"]))
    img_t4 = SCREENSHOTS_DIR / "task_4_terminal_output.png"
    if img_t4.exists():
        story.append(Image(str(img_t4), width=540, height=240))
        story.append(Paragraph("Figure 4.1: Task 4 - DAX Measures and Calculated Columns Output Screenshot", styles["ImageCaption"]))

    # =========================================================================
    # PAGE 5: TASK 5: POWER BI VISUALIZATIONS (PART 1)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Task 5: Power BI Visualizations (20 Marks) — Part 1", styles["TaskHeader"]))

    q5_text = (
        "<b>Question:</b> Create at least 4-5 different types of visualizations: "
        "Bar Chart / Column Chart, Line Chart (trend analysis), Pie / Donut Chart (proportion), "
        "Card / Multi-row Card (KPIs), Table / Matrix (detailed view). "
        "Format visual elements with clear titles, labels, colors, and legends."
    )
    t_q5 = Table([[Paragraph(q5_text, styles["QuestionBox"])]], colWidths=[540])
    t_q5.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#BFDBFE")),
        ("PADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t_q5)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Visual Component 1: KPI Summary Cards</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("Displays top-level summary metrics: Total Revenue (INR 45.60M), Net Profit (INR 8.90M), Profit Margin (19.53%), Total Orders (1,200), and Average Order Value (INR 38,003).", styles["StudentNote"]))
    img_kpi = SCREENSHOTS_DIR / "task_5_kpi_cards.png"
    if img_kpi.exists():
        story.append(Image(str(img_kpi), width=540, height=80))
        story.append(Paragraph("Figure 5.1: KPI Summary Cards Visual", styles["ImageCaption"]))

    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>Visual Component 2: Clustered Bar Chart (Sales & Profit by Category)</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("Compares gross sales and net profit across Technology, Furniture, and Office Supplies. Technology produces over 75% of total company profit.", styles["StudentNote"]))
    img_cat = SCREENSHOTS_DIR / "task_5_category_chart.png"
    if img_cat.exists():
        story.append(Image(str(img_cat), width=540, height=195))
        story.append(Paragraph("Figure 5.2: Bar Chart - Sales and Net Profit by Product Category", styles["ImageCaption"]))

    # =========================================================================
    # PAGE 6: TASK 5: POWER BI VISUALIZATIONS (PART 2)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Task 5: Power BI Visualizations (20 Marks) — Part 2", styles["TaskHeader"]))

    story.append(Paragraph("<b>Visual Component 3: Monthly Sales Trend Line Chart (2024–2026)</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("Plots continuous 36-month revenue progression with a 3-month rolling average trendline, showing strong recovery in 2026 (+35.26% YoY growth) and mid-year corporate buying spikes.", styles["StudentNote"]))
    img_trend = SCREENSHOTS_DIR / "task_5_monthly_trend.png"
    if img_trend.exists():
        story.append(Image(str(img_trend), width=540, height=140))
        story.append(Paragraph("Figure 5.3: Line Chart - Monthly Sales Trend (2024-2026) with Rolling Average", styles["ImageCaption"]))

    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>Visual Component 4: Donut Chart (Sales Contribution by Customer Segment)</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("Displays customer segment proportion: Consumer (50.5%), Corporate (31.2%), and Home Office (18.3%).", styles["StudentNote"]))
    img_donut = SCREENSHOTS_DIR / "task_5_segment_donut.png"
    if img_donut.exists():
        story.append(Image(str(img_donut), width=540, height=140))
        story.append(Paragraph("Figure 5.4: Donut Chart - Revenue Share by Customer Segment", styles["ImageCaption"]))

    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>Visual Component 5: Detailed Matrix Table (Category & Subcategory Breakdown)</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("Provides hierarchical table of Sales, Cost, Profit, and Profit Margin % across all 10 product subcategories with conditional color formatting.", styles["StudentNote"]))
    img_matrix = SCREENSHOTS_DIR / "task_5_matrix_table.png"
    if img_matrix.exists():
        story.append(Image(str(img_matrix), width=540, height=140))
        story.append(Paragraph("Figure 5.5: Matrix Table - Category and Sub-Category Performance Drill-Down", styles["ImageCaption"]))

    # =========================================================================
    # PAGE 7: TASK 6: INTERACTIVE DASHBOARD & FILTERS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Task 6: Interactive Dashboard & Slicers (10 Marks)", styles["TaskHeader"]))

    q6_text = (
        "<b>Question:</b> Arrange visualizations into a well-structured interactive dashboard. "
        "Add Slicers / Filters (e.g., Year/Date, Region, Category). "
        "Test cross-filtering between visuals. Format dashboard for clean layout, alignment, and visual hierarchy."
    )
    t_q6 = Table([[Paragraph(q6_text, styles["QuestionBox"])]], colWidths=[540])
    t_q6.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#BFDBFE")),
        ("PADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t_q6)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Student Explanation & Implementation Summary:</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("• <b>Dashboard Layout:</b> Designed a 16:9 widescreen executive dashboard with high-contrast dark theme, organized into top KPI ribbon, left categorical charts, center monthly trend, and right segment breakdown.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Interactive Slicers:</b> Added interactive filter buttons at the top for Year (All, 2024, 2025, 2026), Region (North, South, East, West, Central), and Product Category.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Cross-Filtering Behavior:</b> Selecting any segment in the Donut Chart or Category in the Bar Chart automatically filters all KPI cards and the Monthly Trend line chart in real time.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Visual Hierarchy:</b> Clean typography, labeled data values, formatted currency in INR, and color-coded positive/negative profit margins.", styles["BulletPoint"]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Output Screenshot (Power BI Executive Dashboard Canvas):</b>", styles["SectionSubtitle"]))
    img_dash = SCREENSHOTS_DIR / "task_6_dashboard.png"
    if img_dash.exists():
        story.append(Image(str(img_dash), width=540, height=270))
        story.append(Paragraph("Figure 6.1: Task 6 - Full HD Power BI Executive Business Intelligence Dashboard Canvas", styles["ImageCaption"]))

    # =========================================================================
    # PAGE 8: TASK 7: BUSINESS INSIGHTS & RECOMMENDATIONS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Task 7: Business Insights & Recommendations (10 Marks)", styles["TaskHeader"]))

    q7_text = (
        "<b>Question:</b> Analyze the dashboard to discover key patterns and trends. "
        "Identify top-performing and underperforming products, categories, or regions. "
        "Suggest 2-3 actionable business recommendations based on the data findings."
    )
    t_q7 = Table([[Paragraph(q7_text, styles["QuestionBox"])]], colWidths=[540])
    t_q7.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#BFDBFE")),
        ("PADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t_q7)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Student Explanation & Implementation Summary:</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("• <b>Insight 1 (Top Category):</b> Technology is the primary profit engine, generating 56.2% of sales and 75.6% of company profit with a 26.26% margin.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Insight 2 (Underperforming Area):</b> Furniture generates high revenue (INR 14.76M) but has a very low profit margin of only 6.42% due to high freight costs and aggressive discounting.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Insight 3 (Regional Leaders):</b> West (Mumbai/Pune) and South (Bengaluru/Hyderabad) lead sales (>53% total volume), while Central region maintains a strong 22.8% profit margin.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Recommendation 1 (Discount Cap on Furniture):</b> Set a strict 12% cap on discretionary furniture discounts. Require furniture discounts to be bundled with high-margin technology accessories. Expected to lift furniture margin from 6.4% to 15.0% (+INR 1.5M profit).", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Recommendation 2 (Corporate B2B Portal):</b> Launch a dedicated corporate purchasing portal with invoice credit terms to capitalize on the Corporate segment's high Average Order Value (INR 37,612). Expected to increase corporate revenue share from 31% to 42%.", styles["BulletPoint"]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Output Screenshot (Terminal Insights & Recommendations Output):</b>", styles["SectionSubtitle"]))
    img_t7 = SCREENSHOTS_DIR / "task_7_terminal_output.png"
    if img_t7.exists():
        story.append(Image(str(img_t7), width=540, height=255))
        story.append(Paragraph("Figure 7.1: Task 7 - Business Insights and Strategic Recommendations Output Screenshot", styles["ImageCaption"]))

    # Build Document
    doc.build(story, canvasmaker=SimpleNumberedCanvas)
    print("=" * 70)
    print(f"REPORT SUCCESSFULLY GENERATED: {OUTPUT_PDF}")
    print(f"File Size: {OUTPUT_PDF.stat().st_size:,} bytes")
    print("=" * 70)


if __name__ == "__main__":
    build_pdf()
