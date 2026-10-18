"""
Dataset Generation Script for Week 6 Capstone Project
Domain: Omnichannel E-Commerce & Retail Customer Analytics
Generates:
  1. raw_ecommerce_sales.csv (1525 rows with intentional defects for cleaning audit)
  2. cleaned_ecommerce_sales.csv (1500 valid records for analytical modeling)
  3. ecommerce_data_dictionary.csv (column metadata and specifications)
"""

import os
import random
from datetime import datetime, timedelta
from pathlib import Path
import numpy as np
import pandas as pd

# Set reproducible seed
np.random.seed(42)
random.seed(42)

BASE_DIR = Path(__file__).resolve().parent
BASE_DIR.mkdir(parents=True, exist_ok=True)

# Domain Entities
REGIONS = {
    "North": [("Delhi", "Delhi"), ("Jaipur", "Rajasthan"), ("Chandigarh", "Punjab"), ("Lucknow", "Uttar Pradesh")],
    "South": [("Bengaluru", "Karnataka"), ("Hyderabad", "Telangana"), ("Chennai", "Tamil Nadu"), ("Kochi", "Kerala")],
    "West": [("Mumbai", "Maharashtra"), ("Pune", "Maharashtra"), ("Ahmedabad", "Gujarat"), ("Surat", "Gujarat")],
    "East": [("Kolkata", "West Bengal"), ("Bhubaneswar", "Odisha"), ("Patna", "Bihar"), ("Guwahati", "Assam")],
    "Central": [("Indore", "Madhya Pradesh"), ("Bhopal", "Madhya Pradesh"), ("Nagpur", "Maharashtra"), ("Raipur", "Chhattisgarh")]
}

PRODUCTS = [
    # Technology (High margin, high price)
    ("PROD-TECH-01", "Smartphone Ultra 5G", "Technology", "Phones", 45000.0, 31500.0),
    ("PROD-TECH-02", "Pro Laptop 16-inch", "Technology", "Laptops", 85000.0, 61000.0),
    ("PROD-TECH-03", "Wireless Noise-Canceling Headphones", "Technology", "Accessories", 12500.0, 8000.0),
    ("PROD-TECH-04", "4K Ultra-Wide Monitor", "Technology", "Accessories", 28000.0, 19500.0),
    ("PROD-TECH-05", "Smart Fitness Watch", "Technology", "Accessories", 9500.0, 6200.0),
    ("PROD-TECH-06", "Enterprise Tablet 11-inch", "Technology", "Phones", 38000.0, 27000.0),
    # Furniture (High freight, moderate/compressed margin)
    ("PROD-FURN-01", "Ergonomic Mesh Office Chair", "Furniture", "Chairs", 14500.0, 12000.0),
    ("PROD-FURN-02", "Motorized Standing Desk", "Furniture", "Tables", 26500.0, 22500.0),
    ("PROD-FURN-03", "Solid Teak Executive Desk", "Furniture", "Tables", 34000.0, 29000.0),
    ("PROD-FURN-04", "Modular 4-Shelf Bookcase", "Furniture", "Bookcases", 11500.0, 9800.0),
    ("PROD-FURN-05", "Steel Lateral Filing Cabinet", "Furniture", "Storage", 16000.0, 13800.0),
    ("PROD-FURN-06", "Conference Room Swivel Chair", "Furniture", "Chairs", 18500.0, 15500.0),
    # Office Supplies (Lower price, high transaction velocity)
    ("PROD-OFF-01", "Heavy-Duty Cross-Cut Shredder", "Office Supplies", "Appliances", 6800.0, 4800.0),
    ("PROD-OFF-02", "Ergonomic Gel Mouse Pad & Wrist Rest", "Office Supplies", "Accessories", 850.0, 520.0),
    ("PROD-OFF-03", "Multipurpose Premium Paper Reams (5x)", "Office Supplies", "Paper", 1450.0, 950.0),
    ("PROD-OFF-04", "Lockable Metal Storage Bin", "Office Supplies", "Storage", 3200.0, 2100.0),
    ("PROD-OFF-05", "Professional Marker & Whiteboard Kit", "Office Supplies", "Art", 950.0, 600.0),
    ("PROD-OFF-06", "Secure Document Envelopes (Pack of 50)", "Office Supplies", "Envelopes", 650.0, 380.0)
]

CUSTOMERS = [
    (f"CUST-{1000 + i}", name, seg)
    for i, (name, seg) in enumerate([
        ("Aarav Sharma", "Consumer"), ("Isha Iyer", "Corporate"), ("Rohan Mehta", "Corporate"),
        ("Priya Patel", "Consumer"), ("Vikram Malhotra", "Corporate"), ("Ananya Verma", "Home Office"),
        ("Kabir Joshi", "Consumer"), ("Neha Gupta", "Corporate"), ("Siddharth Rao", "Consumer"),
        ("Pooja Nair", "Home Office"), ("Aditya Kapoor", "Corporate"), ("Divya Reddy", "Consumer"),
        ("Arjun Das", "Home Office"), ("Sneha Kulkarni", "Corporate"), ("Karan Singhania", "Consumer"),
        ("Tanvi Deshmukh", "Home Office"), ("Rajeshwari Pillai", "Corporate"), ("Manish Sen", "Consumer"),
        ("Ritu Chawla", "Consumer"), ("Harsh Vardhan", "Corporate"), ("Shreya Bansal", "Home Office"),
        ("Gaurav Pandey", "Consumer"), ("Meera Nambiar", "Corporate"), ("Deepak Choudhary", "Consumer"),
        ("Kavita Sundaram", "Home Office"), ("Alok Mukherjee", "Corporate"), ("Simran Kaur", "Consumer"),
        ("Naveen Bhatia", "Corporate"), ("Sunita Agarwal", "Home Office"), ("Varun Tiwari", "Consumer")
    ])
]

SHIP_MODES = ["Standard Class", "Second Class", "First Class", "Same Day"]
PAYMENT_MODES = ["Credit Card", "Debit Card", "UPI", "Net Banking", "Cash on Delivery"]
DELIVERY_STATUSES = ["Delivered", "Delivered", "Delivered", "Delivered", "Shipped", "In Transit", "Returned"]


def generate_clean_records(n=1500):
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2026, 9, 30)
    total_days = (end_date - start_date).days

    rows = []
    for i in range(1, n + 1):
        order_id = f"ORD-{2024 + (i % 3)}-{10000 + i}"
        
        # Bias dates towards mid-year and Q4 (cyclical retail peaks)
        day_offset = random.randint(0, total_days)
        order_dt = start_date + timedelta(days=day_offset)
        
        # Delivery SLA: 1 to 5 days
        delivery_days = random.choices([1, 2, 3, 4, 5], weights=[0.1, 0.25, 0.40, 0.15, 0.10])[0]
        ship_dt = order_dt + timedelta(days=delivery_days)
        
        # Customer & Region
        cust_id, cust_name, cust_seg = random.choice(CUSTOMERS)
        region = random.choices(list(REGIONS.keys()), weights=[0.25, 0.28, 0.24, 0.12, 0.11])[0]
        city, state = random.choice(REGIONS[region])
        
        # Product & Category
        prod = random.choice(PRODUCTS)
        prod_id, prod_name, cat, sub_cat, base_price, base_cost = prod
        
        # Quantity & Pricing
        if cust_seg == "Corporate":
            qty = random.choices([2, 3, 4, 5, 6, 8], weights=[0.2, 0.3, 0.2, 0.15, 0.1, 0.05])[0]
            disc_rate = random.choices([0.0, 0.05, 0.10, 0.15], weights=[0.4, 0.35, 0.20, 0.05])[0]
        elif cust_seg == "Home Office":
            qty = random.choices([1, 2, 3, 4], weights=[0.4, 0.35, 0.15, 0.1])[0]
            disc_rate = random.choices([0.0, 0.05, 0.10, 0.15, 0.20], weights=[0.3, 0.3, 0.25, 0.1, 0.05])[0]
        else:
            qty = random.choices([1, 2, 3], weights=[0.6, 0.3, 0.1])[0]
            disc_rate = random.choices([0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30], weights=[0.25, 0.25, 0.2, 0.15, 0.08, 0.04, 0.03])[0]

        # Financial Calculations
        gross_sales = qty * base_price
        disc_amount = round(gross_sales * disc_rate, 2)
        sales_amount = round(gross_sales - disc_amount, 2)
        
        # Shipping logistics
        shipping_cost = 150.0 if cat != "Furniture" else random.choice([450.0, 650.0, 850.0])
        total_cost = round((qty * base_cost) + shipping_cost, 2)
        profit = round(sales_amount - total_cost, 2)
        margin_pct = round((profit / sales_amount) * 100, 2) if sales_amount > 0 else 0.0

        ship_mode = random.choices(SHIP_MODES, weights=[0.55, 0.25, 0.15, 0.05])[0]
        payment_mode = random.choices(PAYMENT_MODES, weights=[0.35, 0.20, 0.25, 0.12, 0.08])[0]
        del_status = random.choice(DELIVERY_STATUSES)

        rows.append({
            "Order_ID": order_id,
            "Order_Date": order_dt.strftime("%Y-%m-%d"),
            "Ship_Date": ship_dt.strftime("%Y-%m-%d"),
            "Ship_Mode": ship_mode,
            "Customer_ID": cust_id,
            "Customer_Name": cust_name,
            "Customer_Segment": cust_seg,
            "City": city,
            "State": state,
            "Region": region,
            "Product_ID": prod_id,
            "Product_Name": prod_name,
            "Category": cat,
            "Sub_Category": sub_cat,
            "Quantity": qty,
            "Unit_Price": base_price,
            "Unit_Cost": base_cost,
            "Discount_Rate": disc_rate,
            "Discount_Amount": disc_amount,
            "Sales_Amount": sales_amount,
            "Shipping_Cost": shipping_cost,
            "Total_Cost": total_cost,
            "Profit": profit,
            "Profit_Margin_Pct": margin_pct,
            "Payment_Mode": payment_mode,
            "Delivery_Status": del_status
        })

    return pd.DataFrame(rows)


def inject_defects(df_clean):
    """Create raw contaminated dataset with intentional defects for Task 3 ETL audit."""
    df_raw = df_clean.copy()

    # 1. Add obsolete technical system columns
    df_raw["ETL_Batch_ID"] = [f"BATCH-2026-Q{random.randint(1,4)}" for _ in range(len(df_raw))]
    df_raw["Sys_Load_Timestamp"] = [datetime.now().strftime("%Y-%m-%d %H:%M:%S") for _ in range(len(df_raw))]
    df_raw["Legacy_System_Flag"] = ["LEGACY_V1" if random.random() < 0.2 else "V2_CLOUD" for _ in range(len(df_raw))]

    # 2. Inject 25 duplicate rows
    dup_indices = random.sample(range(len(df_raw)), 25)
    dups = df_raw.iloc[dup_indices].copy()
    df_raw = pd.concat([df_raw, dups], ignore_index=True)

    # 3. Inject 10 missing Ship_Dates
    null_ship_indices = random.sample(range(len(df_raw)), 10)
    df_raw.loc[null_ship_indices, "Ship_Date"] = np.nan

    # 4. Inject 12 missing Profits
    null_profit_indices = random.sample(range(len(df_raw)), 12)
    df_raw.loc[null_profit_indices, "Profit"] = np.nan

    # 5. Inject 8 unlinked missing Customer_IDs
    null_cust_indices = random.sample(range(len(df_raw)), 8)
    df_raw.loc[null_cust_indices, "Customer_ID"] = np.nan

    return df_raw


def create_data_dictionary():
    dict_data = [
        {"Column_Name": "Order_ID", "Data_Type": "String", "Description": "Unique identifier for each retail transaction", "Example": "ORD-2025-10142"},
        {"Column_Name": "Order_Date", "Data_Type": "Date (YYYY-MM-DD)", "Description": "Calendar timestamp of transaction creation", "Example": "2025-06-14"},
        {"Column_Name": "Ship_Date", "Data_Type": "Date (YYYY-MM-DD)", "Description": "Date of carrier handover and order fulfillment", "Example": "2025-06-17"},
        {"Column_Name": "Ship_Mode", "Data_Type": "String", "Description": "Shipping fulfillment tier (Standard, Second, First, Same Day)", "Example": "Standard Class"},
        {"Column_Name": "Customer_ID", "Data_Type": "String", "Description": "Unique client primary identifier", "Example": "CUST-1004"},
        {"Column_Name": "Customer_Name", "Data_Type": "String", "Description": "Full registered name of purchasing client", "Example": "Isha Iyer"},
        {"Column_Name": "Customer_Segment", "Data_Type": "String", "Description": "Commercial customer tier (Consumer, Corporate, Home Office)", "Example": "Corporate"},
        {"Column_Name": "City", "Data_Type": "String", "Description": "Metropolitan delivery destination", "Example": "Bengaluru"},
        {"Column_Name": "State", "Data_Type": "String", "Description": "State or territorial jurisdiction", "Example": "Karnataka"},
        {"Column_Name": "Region", "Data_Type": "String", "Description": "Macro sales territory (North, South, East, West, Central)", "Example": "South"},
        {"Column_Name": "Product_ID", "Data_Type": "String", "Description": "Catalog Stock Keeping Unit (SKU)", "Example": "PROD-TECH-01"},
        {"Column_Name": "Product_Name", "Data_Type": "String", "Description": "Descriptive nomenclature of purchased inventory item", "Example": "Smartphone Ultra 5G"},
        {"Column_Name": "Category", "Data_Type": "String", "Description": "Primary merchandise department (Technology, Furniture, Office Supplies)", "Example": "Technology"},
        {"Column_Name": "Sub_Category", "Data_Type": "String", "Description": "Secondary product classification tier", "Example": "Phones"},
        {"Column_Name": "Quantity", "Data_Type": "Integer", "Description": "Number of units purchased in single basket", "Example": "2"},
        {"Column_Name": "Unit_Price", "Data_Type": "Float (INR)", "Description": "Catalog list price per unit in Indian Rupees", "Example": "45000.0"},
        {"Column_Name": "Unit_Cost", "Data_Type": "Float (INR)", "Description": "Cost of goods sold (COGS) per inventory unit", "Example": "31500.0"},
        {"Column_Name": "Discount_Rate", "Data_Type": "Float (0.0-0.3)", "Description": "Applied discount percentage off list price", "Example": "0.10"},
        {"Column_Name": "Discount_Amount", "Data_Type": "Float (INR)", "Description": "Total currency deduction applied", "Example": "9000.0"},
        {"Column_Name": "Sales_Amount", "Data_Type": "Float (INR)", "Description": "Net top-line transaction value realized", "Example": "81000.0"},
        {"Column_Name": "Shipping_Cost", "Data_Type": "Float (INR)", "Description": "Logistics courier handling cost incurred", "Example": "150.0"},
        {"Column_Name": "Total_Cost", "Data_Type": "Float (INR)", "Description": "Total expense (COGS + Shipping Overhead)", "Example": "63150.0"},
        {"Column_Name": "Profit", "Data_Type": "Float (INR)", "Description": "Net bottom-line commercial gross profit realized", "Example": "17850.0"},
        {"Column_Name": "Profit_Margin_Pct", "Data_Type": "Float (%)", "Description": "Gross profit margin percentage (Profit / Sales)", "Example": "22.04%"},
        {"Column_Name": "Payment_Mode", "Data_Type": "String", "Description": "Settlement tender instrument utilized", "Example": "Credit Card"},
        {"Column_Name": "Delivery_Status", "Data_Type": "String", "Description": "Final order operational lifecycle status", "Example": "Delivered"}
    ]
    return pd.DataFrame(dict_data)


def main():
    print("=" * 80)
    print("GENERATING REAL-WORLD E-COMMERCE CAPSTONE DATASET (WEEK 6)")
    print("=" * 80)

    # 1. Generate clean dataset (1,500 rows)
    df_clean = generate_clean_records(n=1500)
    clean_csv_path = BASE_DIR / "cleaned_ecommerce_sales.csv"
    df_clean.to_csv(clean_csv_path, index=False)
    print(f"Generated Pristine Dataset: {clean_csv_path} ({len(df_clean)} rows x {len(df_clean.columns)} cols)")

    # 2. Generate raw contaminated dataset (1,525+ rows with defects)
    df_raw = inject_defects(df_clean)
    raw_csv_path = BASE_DIR / "raw_ecommerce_sales.csv"
    df_raw.to_csv(raw_csv_path, index=False)
    print(f"Generated Contaminated Raw Dataset: {raw_csv_path} ({len(df_raw)} rows x {len(df_raw.columns)} cols)")

    # 3. Generate data dictionary
    df_dict = create_data_dictionary()
    dict_csv_path = BASE_DIR / "ecommerce_data_dictionary.csv"
    df_dict.to_csv(dict_csv_path, index=False)
    print(f"Generated Data Dictionary: {dict_csv_path} ({len(df_dict)} attributes defined)")

    # 4. Generate structured Excel workbook for Power BI data source
    excel_path = BASE_DIR / "Ecommerce_Capstone_Data_Model.xlsx"
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        df_clean.to_excel(writer, sheet_name="Cleaned_Sales_Facts", index=False)
        df_dict.to_excel(writer, sheet_name="Data_Dictionary", index=False)
    print(f"Generated Excel Data Model Workbook: {excel_path}")

    # Summary Statistics
    total_sales = df_clean["Sales_Amount"].sum()
    total_profit = df_clean["Profit"].sum()
    overall_margin = (total_profit / total_sales) * 100
    print("\nCAPSTONE DATASET SUMMARY METRICS:")
    print(f"  * Total Revenue     : INR {total_sales:,.2f}")
    print(f"  * Total Profit      : INR {total_profit:,.2f}")
    print(f"  * Gross Margin %    : {overall_margin:.2f}%")
    print(f"  * Total Orders      : {len(df_clean):,}")
    print(f"  * Date Range        : {df_clean['Order_Date'].min()} to {df_clean['Order_Date'].max()}")
    print("=" * 80)


if __name__ == "__main__":
    main()
