# Final Data Analytics Capstone Project Presentation

**Project Title:** Omnichannel E-Commerce & Retail Customer Analytics  
**Student:** Ayush | B.Tech CSE (IoT) | Prestige Institute of Engineering, Management & Research, Indore  
**Course:** Data Analytics Internship — Week 6 Final Capstone  
**Repository:** https://github.com/Ayush-Raghuwanshi-Dev/DA_Internship.git  

---

## Slide 1: Title & Executive Summary
- **Title:** Omnichannel E-Commerce Customer Analytics & Executive Business Intelligence
- **Presenter:** Ayush (CSE - IoT, PIEMR Indore)
- **Objective:** Build an end-to-end data pipeline from raw transactional ingestion to statistical EDA, high-definition visualizations, interactive Power BI dashboard, and strategic ROI recommendations.
- **Key Headline:** Analyzed 1,492 retail transactions generating INR 70.13M GMV and INR 14.02M profit at a healthy 19.99% overall margin.

---

## Slide 2: Problem Statement & Commercial Objectives
- **Context:** Rapid omnichannel retail growth has exposed hidden margin leaks, unpredictable delivery turnaround, and destructive discount discounting.
- **Key Questions Addressed:**
  1. Which merchandise categories generate sustainable commercial profit vs revenue illusion?
  2. How do customer purchasing tiers (Corporate vs Consumer) differ in order basket size and price sensitivity?
  3. At what threshold does promotional discounting transition from profit-stimulator to margin destroyer?

---

## Slide 3: Dataset Architecture & Data Cleaning Pipeline
- **Dataset Scope:** 1,500 transactions spanning 2024–2026 across 5 Indian macro-regions (North, South, East, West, Central).
- **Pre-Cleaning Defects Audit:**
  - 25 duplicate orders detected and purged.
  - 10 missing carrier delivery dates (`Ship_Date`) imputed via 3-day turnaround SLA.
  - 12 missing profit figures mathematically computed (`Sales_Amount - Total_Cost`).
  - 3 obsolete technical columns purged.
- **Final Validated Data:** 1,492 pristine records with 0 missing values and 0 duplicates (97.8% retention rate).

---

## Slide 4: Exploratory Data Analysis & Statistical Discoveries
- **Descriptive Statistics:**
  - Mean Order Value: INR 47,005.19 | Median: INR 25,000.00 | Std Dev: INR 69,152.84
  - Right-skewed distribution driven by high-value enterprise technology bundles.
- **Tukey's IQR Outlier Detection:**
  - 131 sales transactions flagged as statistical outliers (8.78%), representing bulk corporate procurement rather than bad records.
- **Correlation Findings:**
  - Sales & Profit correlation: $r = +0.947$ (Strong alignment).
  - Discount Rate & Profit: $r = -0.218$ (Demonstrable negative impact).

---

## Slide 5: Core Data Visualizations
- **Chart 1:** Category Dual-Axis Clustered Bar & Margin Curve.
- **Chart 2:** Continuous 36-Month Sales Progression with 3-Month Rolling Average.
- **Chart 3:** Customer Segment Order Value Distribution (Violin & Box Plot).
- **Chart 4:** 6x6 Multivariate Correlation Heatmap.
- **Chart 5:** Empirical Discount vs Profit Margin Scatter Plot with Margin Cliff.

---

## Slide 6: Power BI Executive Dashboard Architecture
- **Canvas:** Full HD 1920x1080 (16:9 widescreen canvas, high-contrast dark theme).
- **5 KPI Summary Cards:**
  - Total Revenue: INR 70.13M (+34.8% YoY)
  - Net Commercial Profit: INR 14.02M (+28.4% YoY)
  - Gross Margin: 19.99% (Target: 20.0%)
  - Total Orders: 1,492 Distinct Orders (AOV: INR 47,005)
  - Basket Velocity: 2.50 Units per Order
- **Interactive Controls:** Top Slicer Bar (Year, Region, Category, Segment) with bidirectional cross-filtering.

---

## Slide 7: Five Key Business Insights
1. **Profit Engine Disparity:** Technology represents 63.8% of sales and generates 80.5% of total company profit (25.2% margin). Furniture suffers margin compression at 9.09%.
2. **Corporate B2B Advantage:** Corporate clients generate an AOV of INR 72,718.73 (2.7x higher than retail consumers) and contribute 58% of national revenue.
3. **Territory Distribution:** South and North drive 54% of national sales, while Central maintains an exceptional 21.49% profit margin.
4. **Temporal Cyclicality:** Predictable surges in June and September aligning with corporate budget cycles; +34.8% YoY growth in 2026.
5. **Discount Erosion Cliff:** Discounts exceeding 20% destroy gross margin, turning transactions into loss-leaders.

---

## Slide 8: Strategic Business Recommendations
- **Recommendation 1: Dynamic Discount Governance for Furniture:**
  - Cap standalone furniture discounts at 10%.
  - Conditional bundling: allow discounts up to 20% on Furniture ONLY when paired with high-margin technology accessories.
  - Expected Impact: Expands Furniture margin from 9.1% to 16.5% (+INR 1.65M profit).
- **Recommendation 2: Dedicated Corporate B2B Procurement Portal:**
  - Launch a self-service corporate purchasing portal with invoice credit terms (Net 30/60).
  - Target enterprise tech clusters across Pune, Bengaluru, and Indore.
  - Expected Impact: Increases Corporate revenue share to 68% (+INR 7.5M revenue).

---

## Slide 9: Git & GitHub Workflow Execution
- **Version Control Rigor:** Verified Git installation (`git version 2.49.0.windows.1`), branch tracking (`main`), and remote upstream synchronization.
- **Multi-Stage Commit History:**
  1. Milestone 1: Setup, Data Sourcing, and ETL Cleaning Pipeline.
  2. Milestone 2: Statistical EDA and Matplotlib/Seaborn Visualizations.
  3. Milestone 3: Power BI Dashboard & Business Recommendations.
  4. Milestone 4: Repository Documentation, Presentation, and PDF Report.

---

## Slide 10: Conclusion & Internship Learnings
- **Comprehensive Skill Integration:** Combined Python, NumPy, Pandas, SQL, Excel, Statistics, Matplotlib, Seaborn, Power BI, DAX, and Git into an end-to-end commercial analytics portfolio project.
- **Repository Link:** https://github.com/Ayush-Raghuwanshi-Dev/DA_Internship.git
