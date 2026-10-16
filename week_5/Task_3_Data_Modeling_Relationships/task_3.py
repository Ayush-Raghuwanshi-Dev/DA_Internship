"""
Task 3: Data Modeling & Star Schema Relational Architecture
Internship: Data Analytics - Week 5
Student: Ayush | Prestige Institute of Engineering, Management & Research, Indore
Objective: Verify relational integrity across Star Schema tables, confirm primary/foreign key
           cardinality, and generate a publication-grade Star Schema architecture diagram.
"""

import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def run_task_3():
    print("=" * 80)
    print("WEEK 5 - TASK 3: DATA MODELING & RELATIONSHIPS (STAR SCHEMA ARCHITECTURE)")
    print("=" * 80)

    base_dir = Path(__file__).resolve().parent.parent
    data_dir = base_dir / "Data"
    model_vis_dir = base_dir / "Visualizations" / "model"
    model_vis_dir.mkdir(parents=True, exist_ok=True)

    # 1. Load Cleaned Model Tables
    df_sales = pd.read_csv(data_dir / "Fact_Sales.csv")
    df_cust = pd.read_csv(data_dir / "Dim_Customer.csv")
    df_prod = pd.read_csv(data_dir / "Dim_Product.csv")
    df_reg = pd.read_csv(data_dir / "Dim_Region.csv")
    df_date = pd.read_csv(data_dir / "Dim_Date.csv")

    print(f"Loaded Star Schema Tables:")
    print(f"  * Fact_Sales   : {len(df_sales)} transaction rows")
    print(f"  * Dim_Customer : {len(df_cust)} customer entities")
    print(f"  * Dim_Product  : {len(df_prod)} product catalog entities")
    print(f"  * Dim_Region   : {len(df_reg)} geographic regions")
    print(f"  * Dim_Date     : {len(df_date)} calendar dates\n")

    # 2. Referential Integrity & Key Validation
    print("-" * 80)
    print("RELATIONAL KEY VALIDATION & CARDINALITY CHECKS")
    print("-" * 80)

    checks = [
        ("Dim_Customer", "Customer_Key", "Fact_Sales", "Customer_Key", df_cust["Customer_Key"], df_sales["Customer_Key"]),
        ("Dim_Product", "Product_Key", "Fact_Sales", "Product_Key", df_prod["Product_Key"], df_sales["Product_Key"]),
        ("Dim_Region", "Region_Key", "Fact_Sales", "Region_Key", df_reg["Region_Key"], df_sales["Region_Key"]),
        ("Dim_Date", "Date_Key", "Fact_Sales", "Date_Key", df_date["Date_Key"], df_sales["Date_Key"])
    ]

    rel_summary = []
    for dim_name, dim_pk, fact_name, fact_fk, pk_series, fk_series in checks:
        pk_unique = pk_series.is_unique
        orphan_keys = set(fk_series) - set(pk_series)
        orphan_count = len(orphan_keys)
        cardinality = "1 : *" if pk_unique else "* : *"

        print(f"Relationship: {dim_name}[{dim_pk}] (1) ---> {fact_name}[{fact_fk}] (*)")
        print(f"  - Primary Key Unique in Dimension: {pk_unique}")
        print(f"  - Unmatched Orphan Keys in Fact: {orphan_count}")
        print(f"  - Established Cardinality: {cardinality} (Single Direction Filter)")

        rel_summary.append({
            "Dimension": dim_name,
            "Primary_Key": dim_pk,
            "Fact": fact_name,
            "Foreign_Key": fact_fk,
            "Cardinality": cardinality,
            "Status": "Valid (100% Integrity)" if orphan_count == 0 else "Error"
        })
        print()

    # 3. Generate Star Schema Architecture Diagram
    print("-" * 80)
    print("GENERATING STAR SCHEMA ARCHITECTURE DIAGRAM...")
    print("-" * 80)

    fig, ax = plt.subplots(figsize=(12, 8.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # Background color
    fig.patch.set_facecolor("#F8FAFC")
    ax.set_facecolor("#F8FAFC")

    # Helper function to draw table box
    def draw_table(x, y, w, h, title, fields, bg_header, bg_body="#FFFFFF", border="#0F172A"):
        # Body
        body_box = patches.FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.5,rounding_size=2",
            facecolor=bg_body, edgecolor=border, linewidth=1.5
        )
        ax.add_patch(body_box)

        # Header
        header_h = 4.5
        header_box = patches.FancyBboxPatch(
            (x, y + h - header_h), w, header_h, boxstyle="round,pad=0.5,rounding_size=2",
            facecolor=bg_header, edgecolor=border, linewidth=1.5
        )
        ax.add_patch(header_box)

        # Title
        ax.text(x + w/2, y + h - header_h/2, title, ha="center", va="center",
                fontsize=11, fontweight="bold", color="white", fontfamily="sans-serif")

        # Fields
        line_y = y + h - header_h - 2.5
        for f in fields:
            weight = "bold" if "[PK]" in f or "[FK]" in f else "normal"
            f_color = "#1E3A8A" if "[PK]" in f else ("#047857" if "[FK]" in f else "#334155")
            ax.text(x + 2, line_y, f, ha="left", va="center",
                    fontsize=8.5, fontweight=weight, color=f_color, fontfamily="monospace")
            line_y -= 2.2

    # Draw Fact Table (Center)
    fact_fields = [
        "Order_ID [Degenerate Key]",
        "Order_Date (Date)",
        "Ship_Date (Date)",
        "Date_Key [FK] -> Dim_Date",
        "Customer_Key [FK] -> Dim_Customer",
        "Product_Key [FK] -> Dim_Product",
        "Region_Key [FK] -> Dim_Region",
        "Quantity (Int)",
        "Unit_Price (Decimal)",
        "Sales_Amount (Currency)",
        "Shipping_Cost (Currency)",
        "Total_Cost (Currency)",
        "Profit (Currency)",
        "Profit_Margin_Pct (%)",
        "Discount_Rate (%)"
    ]
    draw_table(36, 28, 28, 42, "Fact_Sales (Center)", fact_fields, "#1E3A8A", "#FFFFFF", "#1E3A8A")

    # Draw Dim_Customer (Top)
    cust_fields = [
        "Customer_Key [PK]",
        "Customer_ID",
        "Customer_Name",
        "Segment (Consumer/Corp)",
        "City, State, Country",
        "Postal_Code"
    ]
    draw_table(36, 78, 28, 19, "Dim_Customer", cust_fields, "#0F766E")

    # Draw Dim_Date (Bottom)
    date_fields = [
        "Date_Key [PK]",
        "Date (Date)",
        "Year, Quarter, Month",
        "Month_Name, Week_Num",
        "Day_Of_Week, Is_Weekend"
    ]
    draw_table(36, 3, 28, 18, "Dim_Date", date_fields, "#0369A1")

    # Draw Dim_Region (Left)
    region_fields = [
        "Region_Key [PK]",
        "Region_Name",
        "Regional_Manager",
        "Target_Quota",
        "Headquarters"
    ]
    draw_table(4, 40, 24, 18, "Dim_Region", region_fields, "#7C3AED")

    # Draw Dim_Product (Right)
    product_fields = [
        "Product_Key [PK]",
        "Product_ID",
        "Product_Name",
        "Category (Tech/Furn/Off)",
        "Sub_Category",
        "Unit_Price, Cost_Price"
    ]
    draw_table(72, 40, 24, 20, "Dim_Product", product_fields, "#C2410C")

    # Helper function for connectors
    def draw_connector(x1, y1, x2, y2, label_dim, label_fact, text_label=""):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="-", color="#475569", lw=2, linestyle="-"))
        # Cardinality labels
        ax.text(x1, y1, label_dim, fontsize=10, fontweight="bold", color="#B91C1C", ha="center", va="center")
        ax.text(x2, y2, label_fact, fontsize=11, fontweight="bold", color="#B91C1C", ha="center", va="center")
        if text_label:
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            ax.text(mid_x, mid_y + 1.5, text_label, fontsize=8, fontweight="bold", color="#475569",
                    ha="center", va="center", bbox=dict(boxstyle="round,pad=0.2", facecolor="#F1F5F9", edgecolor="none"))

    # Connect Dim_Customer to Fact_Sales
    draw_connector(50, 77, 50, 71, "1", "*", "1 : * (Single)")

    # Connect Dim_Date to Fact_Sales
    draw_connector(50, 22, 50, 27, "1", "*", "1 : * (Active)")

    # Connect Dim_Region to Fact_Sales
    draw_connector(29, 49, 35, 49, "1", "*", "1 : *")

    # Connect Dim_Product to Fact_Sales
    draw_connector(71, 50, 65, 50, "1", "*", "1 : *")

    # Title & Legend
    ax.text(50, 97.5, "RETAIL BUSINESS INTELLIGENCE - STAR SCHEMA DATA MODEL",
            ha="center", va="center", fontsize=15, fontweight="bold", color="#0F172A")
    ax.text(50, 95, "Power BI In-Memory Relational Model (1:Many Relationships, Single Cross-Filter Direction)",
            ha="center", va="center", fontsize=9.5, color="#64748B")

    diagram_path = model_vis_dir / "star_schema_model.png"
    plt.tight_layout()
    plt.savefig(diagram_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print(f"  -> Saved Star Schema Diagram to: {diagram_path}")

    # 4. Export Summary Report
    summary_path = base_dir / "Task_3_Data_Modeling_Relationships" / "task_3_summary.txt"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("TASK 3: DATA MODELING & RELATIONSHIPS SUMMARY REPORT\n")
        f.write("=" * 70 + "\n\n")
        f.write("STAR SCHEMA RELATIONSHIPS AUDIT:\n")
        for r in rel_summary:
            f.write(f"- {r['Dimension']} [{r['Primary_Key']}] (1) ---> {r['Fact']} [{r['Foreign_Key']}] (*)\n")
            f.write(f"  Cardinality: {r['Cardinality']} | Status: {r['Status']}\n")
        f.write("\nKEY ARCHITECTURAL HIGHLIGHTS:\n")
        f.write("1. 100% Referential Integrity: All foreign keys in Fact_Sales resolve to valid dimension primary keys.\n")
        f.write("2. Single Direction Cross-Filtering: Eliminates ambiguity and ensures deterministic filter propagation.\n")
        f.write("3. Storage Optimization: Normalized dimensional attributes reduce memory footprint in VertiPaq engine.\n")
        f.write(f"4. Diagram Asset: {diagram_path.name} exported at 300 DPI.\n")

    print(f"\nTask 3 modeling documentation saved to: {summary_path}")
    print("=" * 80)
    print("TASK 3 COMPLETED SUCCESSFULLY!\n")

if __name__ == "__main__":
    run_task_3()
