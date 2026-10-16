# Task 6 Guide: Interactive Power BI Dashboard & Slicers Architecture

**Student:** Ayush  
**Course:** B.Tech Computer Science & Engineering (IoT)  
**Institution:** Prestige Institute of Engineering, Management & Research (PIEMR), Indore  
**Assignment:** Week 5 — Power BI & Business Intelligence (Task 6: 15 Marks)  

---

## 1. Executive Dashboard Design Philosophy

An executive dashboard is not merely a collection of charts; it is a **visual decision-support system**. The layout adheres to human-computer interaction (HCI) best practices and the **Z-pattern scanning principle**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. TOP HEADER & BRANDING: Executive Title, Refresh Timestamp, Academic Metadata        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. INTERACTIVE SLICERS: Year Filter | Region Filter | Category Slicer | Segment Slicer │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. EXECUTIVE KPI CARDS: Total Sales (GMV) | Net Profit | Profit Margin % | AOV / Orders│
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│ 4. VISUAL 1: Monthly Sales YoY Trend      │ 5. VISUAL 2: Customer Segment Share (Donut)│
├───────────────────────────────────────────┼────────────────────────────────────────────┤
│ 6. VISUAL 3: Category Sales vs Margin %   │ 7. VISUAL 4: Regional Sales vs Target Quota│
└───────────────────────────────────────────┴────────────────────────────────────────────┘
```

---

## 2. Interactive Slicer Architecture & Filtering Mechanics

### Slicer Configuration & Controls

| Slicer Name | Field Bound | Slicer Visual Type | Operational Selection Mode | Analytical Functionality |
|---|---|:---:|:---:|---|
| **Calendar Year** | `Dim_Date[Year]` | Horizontal Buttons / Tiles | Single Select with "All" | Evaluates Year-over-Year (YoY) metrics and isolates fiscal performance. |
| **Territory / Region** | `Dim_Region[Region_Name]` | Dropdown Menu | Multi-select with Search | Filters all fact rows to regional jurisdictions (North, South, East, West, Central). |
| **Product Category** | `Dim_Product[Category]` | Chiclet / Pill Buttons | Multi-select | Isolates Technology, Furniture, or Office Supplies performance. |
| **Customer Segment** | `Dim_Customer[Segment]` | Radio Buttons | Multi-select | Slices B2B Corporate buyers vs. B2C Consumers vs. Home Office. |

---

## 3. Power BI Interactivity Engine: How Visuals Connect

### A. Cross-Filtering vs. Cross-Highlighting
- **Cross-Filtering:** When a user clicks "Technology" in the Category bar chart, all other visuals on the canvas recalculate their axes and queries to display **only** Technology data.
- **Cross-Highlighting:** Default behavior for column charts. The visual retains full context while "ghosting" unselected portions, displaying the selected segment as an opaque sub-bar.
- *Best Practice Applied:* In the **Format** ribbon $\rightarrow$ **Edit Interactions**, cross-filtering is explicitly enabled across all visuals to maintain clean, non-cluttered visual displays.

### B. Sync Slicers Across Pages
- In multi-page enterprise reports, slicer states are synchronized using the **Sync Slicers Pane** (`View` $\rightarrow$ `Sync Slicers`). Selecting "West" on the Executive Overview page automatically persists across the Category Drill-down and Customer Retention pages.

### C. Bookmarks & Interactive Storytelling
- The **Bookmarks Pane** captures visual states, slicer filters, and visual visibility toggles.
- Bookmarks in our model:
  - *Bookmark 1 (Default Overview):* Clears all filters and presents the macro portfolio view.
  - *Bookmark 2 (High-Margin Focus):* Filters the canvas to products with Margin $\ge 25\%$.
  - *Bookmark 3 (Underperforming Regional Watch):* Focuses on regions trailing their annual quota.

### D. Drill-Through Pages
- Configured by dragging `Product_Key` or `Customer_Key` into the **Drill-through** field well on a target detail page.
- Right-clicking any product bar on the main canvas enables **Drill-through $\rightarrow$ Product Deep Dive**, passing the exact filter context to a granular transaction ledger.
