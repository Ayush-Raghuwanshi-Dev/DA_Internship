# Task 6: Power BI Dashboard Architecture Guide

**Student:** Ayush | B.Tech CSE (IoT) | PIEMR, Indore  
**Assignment:** Week 6: Git, GitHub & Final Data Analytics Project  
**Weightage:** 20 Marks  

---

## 1. Executive Dashboard Architecture & Layout
The Capstone Power BI Dashboard is designed on a 16:9 widescreen canvas (1920x1080) adhering to international Business Intelligence best practices:

```
+---------------------------------------------------------------------------------------------------+
|  OMNICHANNEL E-COMMERCE EXECUTIVE ANALYTICS DASHBOARD       Student: Ayush | PIEMR, Indore        |
|  Filters: [Year: All | 2024 | 2025 | 2026]  [Region: North | South | East | West | Central]       |
+---------------------------------------------------------------------------------------------------+
|  [TOTAL SALES]       [NET PROFIT]        [PROFIT MARGIN]     [TOTAL ORDERS]      [AVG BASKET AOV] |
|   INR 70.13M          INR 14.02M              19.99%              1,492              INR 47,005   |
+---------------------------------------------------+-----------------------------------------------+
|  VISUAL 1: Category Sales, Profit & Margin %      |  VISUAL 2: Revenue Share by Customer Segment  |
|  (Dual-Axis Clustered Bar + Margin Curve)         |  (Donut Chart: Corporate vs Consumer vs Home) |
+---------------------------------------------------+-----------------------------------------------+
|  VISUAL 3: 36-Month Sales Trajectory & Trendline  |  VISUAL 4: Regional GMV vs Annual Quota Targets|
|  (Multi-Line Progression: 2024 to 2026)           |  (Horizontal Performance Bar Chart)           |
+---------------------------------------------------------------------------------------------------+
```

---

## 2. Core Interactive Features
- **Slicers & Filter Controls:** Multi-select interactive filter controls for Year, Region, Category, and Segment.
- **Cross-Filtering & Drill-Through:** Selecting any slice in the Donut Chart or Category in the Bar Chart filters all KPI cards and the Monthly Trend line chart in real time.
- **High-Contrast Dark Aesthetic:** Reduced visual fatigue, sleek slate surface (`#0F172A`), card elevation (`#1E293B`), and vibrant data indicators (Emerald, Royal Blue, Amber, Crimson).
