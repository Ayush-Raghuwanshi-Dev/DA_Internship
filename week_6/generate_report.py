"""
Report Generation Script for Week 6: Git, GitHub & Final Data Analytics Project
Generates a clean, simple, student-friendly PDF report: Week_6_Final_Data_Analytics_Capstone_Report.pdf
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
OUTPUT_PDF = BASE_DIR / "Week_6_Final_Data_Analytics_Capstone_Report.pdf"


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
                "WEEK 6 ASSIGNMENT: GIT, GITHUB & FINAL DATA ANALYTICS PROJECT"
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
        fontSize=17,
        leading=21,
        textColor=primary_color,
        spaceAfter=2,
        alignment=0
    ))

    styles.add(ParagraphStyle(
        name="MainSubtitle",
        fontName="Helvetica",
        fontSize=9.5,
        leading=13,
        textColor=secondary_color,
        spaceAfter=7,
        alignment=0
    ))

    styles.add(ParagraphStyle(
        name="StudentLabel",
        fontName="Helvetica-Bold",
        fontSize=7.8,
        leading=10.5,
        textColor=primary_color
    ))

    styles.add(ParagraphStyle(
        name="StudentVal",
        fontName="Helvetica",
        fontSize=7.8,
        leading=10.5,
        textColor=dark_text
    ))

    styles.add(ParagraphStyle(
        name="TaskHeader",
        fontName="Helvetica-Bold",
        fontSize=11.5,
        leading=15,
        textColor=primary_color,
        spaceBefore=4,
        spaceAfter=3,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        name="QuestionBox",
        fontName="Helvetica-Oblique",
        fontSize=7.8,
        leading=11,
        textColor=colors.HexColor("#1E293B"),
        spaceAfter=2
    ))

    styles.add(ParagraphStyle(
        name="SectionSubtitle",
        fontName="Helvetica-Bold",
        fontSize=8.5,
        leading=11.5,
        textColor=secondary_color,
        spaceBefore=3,
        spaceAfter=2,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        name="StudentNote",
        fontName="Helvetica",
        fontSize=8,
        leading=11,
        textColor=body_text,
        spaceAfter=2
    ))

    styles.add(ParagraphStyle(
        name="BulletPoint",
        fontName="Helvetica",
        fontSize=7.8,
        leading=11,
        textColor=body_text,
        leftIndent=10,
        firstLineIndent=-7,
        spaceAfter=1.5
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
    print("=" * 80)
    print("BUILDING SIMPLE STUDENT-STYLE WEEK 6 FINAL CAPSTONE PDF REPORT")
    print(f"Destination: {OUTPUT_PDF}")
    print("=" * 80)

    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = get_styles()
    story = []

    # =========================================================================
    # PAGE 1: TITLE, STUDENT DETAILS & TASK 1
    # =========================================================================
    story.append(Paragraph("WEEK 6 ASSIGNMENT: GIT, GITHUB & FINAL DATA ANALYTICS PROJECT", styles["MainTitle"]))
    story.append(Paragraph("Final Capstone Project Practical Submission | 100 Marks Evaluation", styles["MainSubtitle"]))

    details_data = [
        [Paragraph("Student Name", styles["StudentLabel"]), Paragraph("Ayush", styles["StudentVal"]),
         Paragraph("Assignment Module", styles["StudentLabel"]), Paragraph("Week 6: Git, GitHub & Capstone Project", styles["StudentVal"])],
        [Paragraph("Degree & Branch", styles["StudentLabel"]), Paragraph("B.Tech in CSE (IoT)", styles["StudentVal"]),
         Paragraph("Evaluation Marks", styles["StudentLabel"]), Paragraph("100 Marks (Tasks 1 to 8 Covered)", styles["StudentVal"])],
        [Paragraph("Institution", styles["StudentLabel"]), Paragraph("Prestige Institute of Engineering, Management & Research, Indore", styles["StudentVal"]),
         Paragraph("Core Technologies", styles["StudentLabel"]), Paragraph("Python, Git, GitHub, Pandas, Seaborn, Power BI", styles["StudentVal"])],
        [Paragraph("GitHub Repository", styles["StudentLabel"]), Paragraph("https://github.com/Ayush-Raghuwanshi-Dev/DA_Internship.git", styles["StudentVal"]),
         Paragraph("Submission Date", styles["StudentLabel"]), Paragraph("October 2026", styles["StudentVal"])],
    ]

    t_details = Table(details_data, colWidths=[95, 175, 110, 160])
    t_details.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#CBD5E1")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(t_details)
    story.append(Spacer(1, 5))

    # Task 1
    story.append(Paragraph("Task 1: Git & GitHub Basics (10 Marks)", styles["TaskHeader"]))
    q1_text = (
        "<b>Question:</b> Set up Git and GitHub and perform the following: Install Git. "
        "Create a GitHub account if you do not already have one. Create a new repository. "
        "Clone the repository to your local system. Add project files to the repository. "
        "Create at least one commit. Push the changes to GitHub."
    )
    t_q1 = Table([[Paragraph(q1_text, styles["QuestionBox"])]], colWidths=[540])
    t_q1.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#BFDBFE")),
        ("PADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t_q1)
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>Student Explanation & Implementation Summary:</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("• Verified Git binary on Windows (version 2.49.0.windows.1) configured with user identity.", styles["BulletPoint"]))
    story.append(Paragraph("• Synced with GitHub remote repository: https://github.com/Ayush-Raghuwanshi-Dev/DA_Internship.git on branch main.", styles["BulletPoint"]))
    story.append(Paragraph("• Initialized project tracking and verified staging index and working tree connectivity.", styles["BulletPoint"]))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>Output Screenshot (Git & GitHub Configuration Audit):</b>", styles["SectionSubtitle"]))
    img_t1 = SCREENSHOTS_DIR / "task_1_git_basics_terminal.png"
    if img_t1.exists():
        story.append(Image(str(img_t1), width=540, height=215))
        story.append(Paragraph("Figure 1.1: Task 1 - Git Version & Remote Repository Configuration Terminal Output", styles["ImageCaption"]))

    # =========================================================================
    # PAGE 2: TASK 2: GIT WORKFLOW PRACTICE
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Task 2: Git Workflow Practice (10 Marks)", styles["TaskHeader"]))
    q2_text = (
        "<b>Question:</b> Practice the basic Git workflow: git clone, git add, git commit, git push, git pull. "
        "Create at least 3 meaningful commits while working on your final project."
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
    story.append(Paragraph("• Practiced standard Git workflow commands: git clone (downloading repository), git add (staging changes), git commit (saving snapshots), git push (uploading to remote), and git pull (updating local branch).", styles["BulletPoint"]))
    story.append(Paragraph("• Executed 4 distinct, meaningful atomic commit milestones across project development:", styles["BulletPoint"]))
    story.append(Paragraph("  - Commit 1: feat(week_6): initialize capstone project dataset selection, preparation (Tasks 1-3)", styles["BulletPoint"]))
    story.append(Paragraph("  - Commit 2: feat(week_6): implement comprehensive exploratory data analysis & visuals (Tasks 4-5)", styles["BulletPoint"]))
    story.append(Paragraph("  - Commit 3: feat(week_6): build interactive power bi dashboard & business insights (Tasks 6-7)", styles["BulletPoint"]))
    story.append(Paragraph("  - Commit 4: docs(week_6): complete capstone documentation, presentation & pdf report (Task 8)", styles["BulletPoint"]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Output Screenshot (Git Workflow Execution & Multi-Stage Commit History):</b>", styles["SectionSubtitle"]))
    img_t2 = SCREENSHOTS_DIR / "task_2_git_workflow_terminal.png"
    if img_t2.exists():
        story.append(Image(str(img_t2), width=540, height=240))
        story.append(Paragraph("Figure 2.1: Task 2 - Git Commit Milestones and Working Tree Verification Terminal Output", styles["ImageCaption"]))

    # =========================================================================
    # PAGE 3: TASK 3: DATASET SELECTION & DATA PREPARATION
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Task 3: Dataset Selection & Data Preparation (10 Marks)", styles["TaskHeader"]))
    q3_text = (
        "<b>Question:</b> Select a real-world dataset related to any suitable domain (Sales, E-commerce, Customer Analytics). "
        "Perform dataset selection, data inspection, identification of columns and data types, identification of missing values, "
        "handling of missing values, removal of duplicate or incorrect records where required, preparation of dataset for analysis."
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
    story.append(Paragraph("• <b>Selected Domain:</b> Omnichannel E-Commerce & Retail Customer Analytics (1,500 transactions, 5 regions in India).", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Defect Audit on Raw Data:</b> Detected 25 duplicate orders, 10 missing Ship_Dates, 12 missing Profit values, and 8 unlinked Customer_IDs in raw_ecommerce_sales.csv.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>ETL Data Cleaning Pipeline:</b> Purged 3 obsolete system columns; removed 25 duplicate rows; filtered 8 unlinked customer records; imputed missing profit as Sales - Total Cost; imputed missing ship dates via Order_Date + 3 days.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Feature Engineering:</b> Added Delivery_Days, Profitability_Status (High Margin, Standard Margin, Loss-Making), and Order_Size_Bucket.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Cleaned Output:</b> 1,492 validated rows x 29 columns with 0 nulls and 0 duplicates (97.8% retention rate), exported to cleaned_ecommerce_sales.csv.", styles["BulletPoint"]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Output Screenshot (ETL Cleaning Pipeline & Pre/Post Audit):</b>", styles["SectionSubtitle"]))
    img_t3 = SCREENSHOTS_DIR / "task_3_data_cleaning_terminal.png"
    if img_t3.exists():
        story.append(Image(str(img_t3), width=540, height=240))
        story.append(Paragraph("Figure 3.1: Task 3 - Data Cleaning Pipeline, Imputation, and Validation Terminal Output", styles["ImageCaption"]))

    # =========================================================================
    # PAGE 4: TASK 4: EXPLORATORY DATA ANALYSIS (EDA)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Task 4: Exploratory Data Analysis (EDA) (15 Marks)", styles["TaskHeader"]))
    q4_text = (
        "<b>Question:</b> Perform EDA on the selected dataset using concepts learned during the internship. "
        "Include descriptive statistics, data inspection, data cleaning, missing-value handling, correlation analysis, "
        "identification of important patterns and trends, identification of outliers where applicable. "
        "Write a brief explanation of your findings."
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
    story.append(Paragraph("• <b>Descriptive Statistics:</b> Evaluated mean, median, standard deviation, skewness, and kurtosis across 1,492 records. Mean Order Value = INR 47,005.19, Median = INR 25,000.00, demonstrating right skewness due to large corporate technology orders.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>IQR Outlier Detection:</b> Flagged 131 sales outliers (8.78%) and 156 profit outliers (10.46%) beyond Q3 + 1.5*IQR bounds, representing valid large enterprise purchases.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Correlation Matrix:</b> Strong positive correlation between Sales and Profit (r = +0.947); negative correlation between Discount Rate and Profit (r = -0.218), showing margin erosion.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Category Disparity:</b> Technology operates at a healthy 25.22% margin (INR 11.28M profit), while Furniture experiences margin compression down to 9.09% (INR 2.07M profit).", styles["BulletPoint"]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Output Screenshot (Descriptive Statistics, IQR Outliers & Correlation Output):</b>", styles["SectionSubtitle"]))
    img_t4 = SCREENSHOTS_DIR / "task_4_eda_statistics_terminal.png"
    if img_t4.exists():
        story.append(Image(str(img_t4), width=540, height=240))
        story.append(Paragraph("Figure 4.1: Task 4 - Descriptive Statistics, Outlier Detection, and Correlation Matrix Terminal Output", styles["ImageCaption"]))

    # =========================================================================
    # PAGE 5: TASK 5: DATA VISUALIZATION (PART 1)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Task 5: Data Visualization (15 Marks) - Part 1", styles["TaskHeader"]))
    q5_text = (
        "<b>Question:</b> Create meaningful visualizations based on your analysis. Use appropriate visualization tools "
        "and create at least 5 charts/visualizations. Represent important information, use meaningful titles and labels, "
        "and clearly communicate trends, comparisons, or relationships."
    )
    t_q5 = Table([[Paragraph(q5_text, styles["QuestionBox"])]], colWidths=[540])
    t_q5.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#BFDBFE")),
        ("PADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t_q5)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Chart 1: Sales Revenue, Net Profit & Margin % by Category (Clustered Bar + Dual-Axis Line)</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("Compares revenue and gross margin across categories, highlighting Technology's dominance (INR 44.7M sales, 25.2% margin) and Furniture's margin compression (9.1%).", styles["StudentNote"]))
    img_c1 = SCREENSHOTS_DIR / "task_5_category_chart.png"
    if img_c1.exists():
        story.append(Image(str(img_c1), width=540, height=195))
        story.append(Paragraph("Figure 5.1: Clustered Bar and Profit Margin Line Chart across Product Categories", styles["ImageCaption"]))

    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>Chart 2: Monthly Sales Trajectory & 3-Month Rolling Average Trendline (2024-2026)</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("Shows 36-month sales and profit progression with quarterly mid-year procurement spikes and +34.8% YoY growth in 2026.", styles["StudentNote"]))
    img_c2 = SCREENSHOTS_DIR / "task_5_monthly_trend.png"
    if img_c2.exists():
        story.append(Image(str(img_c2), width=540, height=140))
        story.append(Paragraph("Figure 5.2: Monthly Sales Revenue Trendline and 3-Month Rolling Average", styles["ImageCaption"]))

    # =========================================================================
    # PAGE 6: TASK 5: DATA VISUALIZATION (PART 2)
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Task 5: Data Visualization (15 Marks) - Part 2", styles["TaskHeader"]))

    story.append(Paragraph("<b>Chart 3: Customer Segment Order Value Distribution (Box Plot)</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("Demonstrates that Corporate clients have a significantly higher median order value (INR 72.7k AOV) compared to Consumer retail (INR 26.8k AOV).", styles["StudentNote"]))
    img_c3 = SCREENSHOTS_DIR / "task_5_segment_box.png"
    if img_c3.exists():
        story.append(Image(str(img_c3), width=540, height=140))
        story.append(Paragraph("Figure 5.3: Customer Segment Basket Economics and Order Value Distribution", styles["ImageCaption"]))

    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>Chart 4: Multivariate Correlation Heatmap (Seaborn)</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("Visualizes correlation coefficients across 6 metrics, highlighting positive sales-profit correlation and negative discount-margin relationship.", styles["StudentNote"]))
    img_c4 = SCREENSHOTS_DIR / "task_5_correlation_heatmap.png"
    if img_c4.exists():
        story.append(Image(str(img_c4), width=540, height=140))
        story.append(Paragraph("Figure 5.4: Seaborn Correlation Heatmap for Financial and Logistics Metrics", styles["ImageCaption"]))

    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>Chart 5: Discounting vs Profit Margin Scatter Plot (Margin Cliff Analysis)</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("Plots discount percentage against profit margin, showing that discounts exceeding 20% systematically generate loss-making transactions.", styles["StudentNote"]))
    img_c5 = SCREENSHOTS_DIR / "task_5_discount_scatter.png"
    if img_c5.exists():
        story.append(Image(str(img_c5), width=540, height=140))
        story.append(Paragraph("Figure 5.5: Discount Rate vs Profit Margin Scatter Plot with Margin Erosion Trendline", styles["ImageCaption"]))

    # =========================================================================
    # PAGE 7: TASK 6: POWER BI DASHBOARD
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Task 6: Power BI Dashboard (20 Marks)", styles["TaskHeader"]))
    q6_text = (
        "<b>Question:</b> Create an interactive Power BI Dashboard using the selected dataset. "
        "Include at least 3 KPI Cards, at least 4 different visualizations, appropriate filters/slicers, "
        "meaningful dashboard title, proper layout and organization, and important business metrics."
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
    story.append(Paragraph("• <b>Executive Layout:</b> Designed a 16:9 Full HD (1920x1080) dashboard with sleek slate dark theme, organized into header slicers, KPI ribbon, and 4 visualization panels.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>5 KPI Summary Cards:</b> Total Sales (INR 70.13M, +34.8% YoY), Net Commercial Profit (INR 14.02M, +28.4% YoY), Gross Profit Margin (19.99%), Total Orders (1,492), and Basket Units (2.50 Units/Order).", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Interactive Slicers:</b> Multi-select interactive filter controls for Year (2024, 2025, 2026), Region (5 regions), Category (3 categories), and Customer Segment.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Integrated Visuals:</b> Category Revenue vs Profit Bar Chart, Customer Segment Donut Chart (Corporate 58%, Consumer 22%, Home Office 20%), 36-Month Sales Trendline, and Regional Quota Horizontal Bar Chart.", styles["BulletPoint"]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Output Screenshot (Full HD Power BI Executive Dashboard Canvas):</b>", styles["SectionSubtitle"]))
    img_dash = SCREENSHOTS_DIR / "task_6_power_bi_dashboard.png"
    if img_dash.exists():
        story.append(Image(str(img_dash), width=540, height=270))
        story.append(Paragraph("Figure 6.1: Task 6 - Full HD Omnichannel E-Commerce Executive Analytics Dashboard Canvas", styles["ImageCaption"]))

    # =========================================================================
    # PAGE 8: TASK 7: BUSINESS INSIGHTS & RECOMMENDATIONS
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Task 7: Business Insights & Recommendations (10 Marks)", styles["TaskHeader"]))
    q7_text = (
        "<b>Question:</b> Based on your complete analysis and Power BI dashboard: Identify at least 5 meaningful "
        "business insights. Explain important trends and patterns. Identify high/low performing areas where applicable. "
        "Provide at least 2 data-driven business recommendations."
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
    story.append(Paragraph("• <b>Insight 1 (Top Category):</b> Technology produces 63.8% of sales and 80.5% of profit with an outstanding 25.2% gross margin.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Insight 2 (Underperforming Area):</b> Furniture generates high sales (INR 22.8M) but suffers from 9.09% compressed profit margin due to courier freight and aggressive discounting.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Insight 3 (Segment Leadership):</b> Corporate clients have an AOV of INR 72,718 (2.7x higher than Consumer retail) and contribute 58% of national revenue.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Recommendation 1 (Furniture Discount Cap):</b> Cap standalone furniture discounts at 10%. Require bundling with high-margin tech accessories to unlock 20% discount. Expected to lift Furniture margin from 9.1% to 16.5% (+INR 1.65M profit).", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Recommendation 2 (Corporate B2B Portal):</b> Launch a self-service corporate purchasing portal with invoice credit terms (Net 30/60) to expand Corporate revenue share to 68% (+INR 7.5M revenue).", styles["BulletPoint"]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Output Screenshot (Business Insights & Strategic Recommendations Output):</b>", styles["SectionSubtitle"]))
    img_t7 = SCREENSHOTS_DIR / "task_7_business_insights_terminal.png"
    if img_t7.exists():
        story.append(Image(str(img_t7), width=540, height=255))
        story.append(Paragraph("Figure 7.1: Task 7 - Terminal Output of 5 Empirical Insights and 2 Strategic Recommendations", styles["ImageCaption"]))

    # =========================================================================
    # PAGE 9: TASK 8: GITHUB DOCUMENTATION & PRESENTATION
    # =========================================================================
    story.append(PageBreak())
    story.append(Paragraph("Task 8: GitHub Documentation & Project Presentation (10 Marks)", styles["TaskHeader"]))
    q8_text = (
        "<b>Question:</b> Create professional documentation for your project repository. Your GitHub repository should contain: "
        "Project Title, Project Overview, Problem Statement, Dataset Description, Tools Used, Data Cleaning Process, "
        "EDA, Visualizations, Power BI Dashboard, Key Insights, Business Recommendations, Conclusion. "
        "Also prepare a short presentation explaining your project."
    )
    t_q8 = Table([[Paragraph(q8_text, styles["QuestionBox"])]], colWidths=[540])
    t_q8.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#BFDBFE")),
        ("PADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t_q8)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Student Explanation & Implementation Summary:</b>", styles["SectionSubtitle"]))
    story.append(Paragraph("• <b>GitHub Documentation (README.md):</b> Authored end-to-end repository documentation covering all 12 required sections: Title, Overview, Problem Statement, Dataset, Tools, Cleaning, EDA, Visuals, Dashboard, Insights, Recommendations, and Conclusion.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Executive Presentation Deck:</b> Prepared a 10-slide executive summary presentation (Presentation/project_presentation.md) detailing project objectives, data cleaning, statistical findings, visualizations, dashboard architecture, and financial ROI.", styles["BulletPoint"]))
    story.append(Paragraph("• <b>Repository Deliverables:</b> Includes raw and cleaned CSV datasets, data dictionary, Excel workbook model, Python analysis scripts, high-resolution charts, master dashboard canvas, and this comprehensive PDF report.", styles["BulletPoint"]))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Output Screenshot (Documentation & Presentation Audit Terminal Output):</b>", styles["SectionSubtitle"]))
    img_t8 = SCREENSHOTS_DIR / "task_8_documentation_terminal.png"
    if img_t8.exists():
        story.append(Image(str(img_t8), width=540, height=255))
        story.append(Paragraph("Figure 8.1: Task 8 - README Documentation Sections and Presentation Deck Audit Terminal Output", styles["ImageCaption"]))

    # Build Document
    doc.build(story, canvasmaker=SimpleNumberedCanvas)
    print("=" * 80)
    print(f"REPORT SUCCESSFULLY GENERATED: {OUTPUT_PDF}")
    print(f"File Size: {OUTPUT_PDF.stat().st_size:,} bytes")
    print("=" * 80)


if __name__ == "__main__":
    build_pdf()
