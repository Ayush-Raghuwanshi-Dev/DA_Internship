"""
Data Generator for Week 5: Power BI & Business Intelligence
Internship: Data Analytics - Week 5
Student: Ayush | Prestige Institute of Engineering, Management & Research, Indore
Domain: Omnichannel Retail & E-Commerce Business Intelligence
Generates:
  1. Fact_Sales.csv (1,200 clean transactions, 2024-2026)
  2. Dim_Customer.csv (120 customer profiles)
  3. Dim_Product.csv (30 products across 3 categories)
  4. Dim_Region.csv (5 geographic regions with targets)
  5. Dim_Date.csv (Full calendar dimension 2024-2026)
  6. raw_fact_sales.csv (Contaminated raw data for Power Query ETL demo)
  7. Retail_BI_Data_Model.xlsx (Formatted multi-tab Excel workbook)
"""

import os
from pathlib import Path
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_data():
    print("=" * 80)
    print("GENERATING MULTI-TABLE STAR SCHEMA DATASETS FOR POWER BI (WEEK 5)...")
    print("=" * 80)

    np.random.seed(42)
    base_dir = Path(__file__).resolve().parent
    base_dir.mkdir(parents=True, exist_ok=True)

    # -------------------------------------------------------------
    # 1. DIM_REGION (5 Regions)
    # -------------------------------------------------------------
    regions_data = [
        {"Region_Key": 1, "Region_Name": "North", "Regional_Manager": "Vikram Malhotra", "Target_Quota": 2500000, "Headquarters": "Delhi"},
        {"Region_Key": 2, "Region_Name": "South", "Regional_Manager": "Priya Sundaram", "Target_Quota": 3200000, "Headquarters": "Bengaluru"},
        {"Region_Key": 3, "Region_Name": "East", "Regional_Manager": "Ananya Chatterjee", "Target_Quota": 1800000, "Headquarters": "Kolkata"},
        {"Region_Key": 4, "Region_Name": "West", "Regional_Manager": "Rajesh Mehta", "Target_Quota": 3800000, "Headquarters": "Mumbai"},
        {"Region_Key": 5, "Region_Name": "Central", "Regional_Manager": "Amitabh Verma", "Target_Quota": 2200000, "Headquarters": "Indore"}
    ]
    df_region = pd.DataFrame(regions_data)
    region_path = base_dir / "Dim_Region.csv"
    df_region.to_csv(region_path, index=False)
    print(f"[1/7] Generated Dim_Region.csv ({len(df_region)} regions)")

    # -------------------------------------------------------------
    # 2. DIM_PRODUCT (30 Products across 3 Categories)
    # -------------------------------------------------------------
    products_data = [
        # Technology (10 products)
        (101, "PROD-TECH-01", "Smartphone Ultra 5G", "Technology", "Phones", 45000.0, 31500.0),
        (102, "PROD-TECH-02", "Pro Workstation Laptop 16", "Technology", "Laptops", 85000.0, 59500.0),
        (103, "PROD-TECH-03", "Noise Cancelling Headphones", "Technology", "Accessories", 12000.0, 7200.0),
        (104, "PROD-TECH-04", "Curved Gaming Monitor 32-in", "Technology", "Accessories", 32000.0, 22400.0),
        (105, "PROD-TECH-05", "Mechanical Wireless Keyboard", "Technology", "Accessories", 6500.0, 3900.0),
        (106, "PROD-TECH-06", "Smartwatch Fitness Tracker", "Technology", "Phones", 15000.0, 9000.0),
        (107, "PROD-TECH-07", "Enterprise Laser Printer", "Technology", "Machines", 28000.0, 21000.0),
        (108, "PROD-TECH-08", "Tablet Pro 11-inch", "Technology", "Phones", 52000.0, 39000.0),
        (109, "PROD-TECH-09", "External SSD 2TB", "Technology", "Storage", 14000.0, 9100.0),
        (110, "PROD-TECH-10", "4K Conference Webcam", "Technology", "Accessories", 8500.0, 5100.0),

        # Furniture (10 products)
        (201, "PROD-FURN-01", "Executive Ergonomic Chair", "Furniture", "Chairs", 18500.0, 13875.0),
        (202, "PROD-FURN-02", "Motorized Standing Desk", "Furniture", "Desks", 34000.0, 27200.0),
        (203, "PROD-FURN-03", "Modular 3-Tier Bookshelf", "Furniture", "Bookcases", 12500.0, 9375.0),
        (204, "PROD-FURN-04", "Mesh Task Office Chair", "Furniture", "Chairs", 8500.0, 5950.0),
        (205, "PROD-FURN-05", "Hardwood Conference Table", "Furniture", "Tables", 65000.0, 55250.0),
        (206, "PROD-FURN-06", "Acoustic Privacy Panel", "Furniture", "Furnishings", 7500.0, 5250.0),
        (207, "PROD-FURN-07", "Leather Guest Lounge Chair", "Furniture", "Chairs", 22000.0, 16500.0),
        (208, "PROD-FURN-08", "Mobile Under-Desk Pedestal", "Furniture", "Storage", 9500.0, 7125.0),
        (209, "PROD-FURN-09", "Minimalist Coffee Table", "Furniture", "Tables", 11000.0, 8250.0),
        (210, "PROD-FURN-10", "Ergonomic Footrest & Mat", "Furniture", "Furnishings", 3500.0, 2100.0),

        # Office Supplies (10 products)
        (301, "PROD-OFF-01", "High-Volume Paper Shredder", "Office Supplies", "Appliances", 14500.0, 10875.0),
        (302, "PROD-OFF-02", "Heavy-Duty Lever Arch Binders", "Office Supplies", "Binders", 1200.0, 660.0),
        (303, "PROD-OFF-03", "Premium Executive Pen Set", "Office Supplies", "Art", 2800.0, 1540.0),
        (304, "PROD-OFF-04", "Steel 4-Drawer File Cabinet", "Office Supplies", "Storage", 16500.0, 12375.0),
        (305, "PROD-OFF-05", "Thermal Laminating Machine", "Office Supplies", "Appliances", 6800.0, 4760.0),
        (306, "PROD-OFF-06", "Recycled Copier Paper (5-Ream)", "Office Supplies", "Paper", 1950.0, 1365.0),
        (307, "PROD-OFF-07", "Heavy-Duty Packaging Tape Roll", "Office Supplies", "Fasteners", 850.0, 425.0),
        (308, "PROD-OFF-08", "Magnetic Whiteboard 4x3 ft", "Office Supplies", "Envelopes", 5500.0, 3575.0),
        (309, "PROD-OFF-09", "Desktop Organizer Caddy", "Office Supplies", "Storage", 1600.0, 880.0),
        (310, "PROD-OFF-10", "Eco Gel Pens Box of 50", "Office Supplies", "Art", 950.0, 475.0),
    ]
    df_product = pd.DataFrame(products_data, columns=[
        "Product_Key", "Product_ID", "Product_Name", "Category", "Sub_Category", "Unit_Price", "Cost_Price"
    ])
    product_path = base_dir / "Dim_Product.csv"
    df_product.to_csv(product_path, index=False)
    print(f"[2/7] Generated Dim_Product.csv ({len(df_product)} products)")

    # -------------------------------------------------------------
    # 3. DIM_CUSTOMER (120 Customers)
    # -------------------------------------------------------------
    first_names = ["Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", "Ayaan", "Krishna", "Ishaan",
                   "Shaurya", "Atharva", "Ananya", "Diya", "Isha", "Aditi", "Pooja", "Neha", "Riya", "Sneha",
                   "Kavya", "Tanvi", "Meera", "Rohan", "Rahul", "Varun", "Karan", "Siddharth", "Manish", "Gaurav"]
    last_names = ["Sharma", "Verma", "Patel", "Gupta", "Mehta", "Jain", "Singh", "Shah", "Reddy", "Nair",
                  "Iyer", "Chopra", "Malhotra", "Saxena", "Bhatia", "Rao", "Deshmukh", "Mukherjee", "Das", "Joshi"]

    cities_by_region = {
        1: [("Delhi", "Delhi", "110001"), ("Chandigarh", "Punjab", "160017"), ("Jaipur", "Rajasthan", "302001"), ("Lucknow", "Uttar Pradesh", "226001")],
        2: [("Bengaluru", "Karnataka", "560001"), ("Chennai", "Tamil Nadu", "600001"), ("Hyderabad", "Telangana", "500001"), ("Kochi", "Kerala", "682001")],
        3: [("Kolkata", "West Bengal", "700001"), ("Bhubaneswar", "Odisha", "751001"), ("Patna", "Bihar", "800001"), ("Guwahati", "Assam", "781001")],
        4: [("Mumbai", "Maharashtra", "400001"), ("Pune", "Maharashtra", "411001"), ("Ahmedabad", "Gujarat", "380001"), ("Surat", "Gujarat", "395001")],
        5: [("Indore", "Madhya Pradesh", "452001"), ("Bhopal", "Madhya Pradesh", "462001"), ("Nagpur", "Maharashtra", "440001"), ("Raipur", "Chhattisgarh", "492001")]
    }

    segments = ["Consumer", "Corporate", "Home Office"]
    segment_weights = [0.52, 0.31, 0.17]

    customers = []
    for c_id in range(1, 121):
        reg_id = np.random.choice([1, 2, 3, 4, 5], p=[0.22, 0.26, 0.14, 0.24, 0.14])
        city_info = cities_by_region[reg_id][np.random.randint(0, len(cities_by_region[reg_id]))]
        name = f"{np.random.choice(first_names)} {np.random.choice(last_names)}"
        seg = np.random.choice(segments, p=segment_weights)

        customers.append({
            "Customer_Key": c_id,
            "Customer_ID": f"CUST-{1000 + c_id}",
            "Customer_Name": name,
            "Segment": seg,
            "City": city_info[0],
            "State": city_info[1],
            "Country": "India",
            "Postal_Code": city_info[2],
            "Region_Key": reg_id
        })
    df_customer = pd.DataFrame(customers)
    customer_path = base_dir / "Dim_Customer.csv"
    df_customer.to_csv(customer_path, index=False)
    print(f"[3/7] Generated Dim_Customer.csv ({len(df_customer)} customer profiles)")

    # -------------------------------------------------------------
    # 4. DIM_DATE (Calendar table from 2024-01-01 to 2026-12-31)
    # -------------------------------------------------------------
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2026, 12, 31)
    date_list = []
    curr = start_date
    while curr <= end_date:
        d_key = int(curr.strftime("%Y%m%d"))
        date_list.append({
            "Date": curr.strftime("%Y-%m-%d"),
            "Date_Key": d_key,
            "Year": curr.year,
            "Quarter": f"Q{ (curr.month - 1) // 3 + 1 }",
            "Quarter_Year": f"Q{ (curr.month - 1) // 3 + 1 } {curr.year}",
            "Month_Num": curr.month,
            "Month_Name": curr.strftime("%B"),
            "Month_Short": curr.strftime("%b"),
            "Month_Year": curr.strftime("%b %Y"),
            "Week_Num": curr.isocalendar()[1],
            "Day_Of_Week": curr.strftime("%A"),
            "Day_Of_Week_Num": curr.weekday() + 1,
            "Is_Weekend": "Weekend" if curr.weekday() >= 5 else "Weekday"
        })
        curr += timedelta(days=1)
    df_date = pd.DataFrame(date_list)
    date_path = base_dir / "Dim_Date.csv"
    df_date.to_csv(date_path, index=False)
    print(f"[4/7] Generated Dim_Date.csv ({len(df_date)} calendar dates)")

    # -------------------------------------------------------------
    # 5. FACT_SALES (1,200 Transactions across 2024-2026)
    # -------------------------------------------------------------
    n_orders = 1200
    ship_modes = ["Standard Class", "Second Class", "First Class", "Same Day"]
    ship_weights = [0.58, 0.22, 0.14, 0.06]
    order_priorities = ["Critical", "High", "Medium", "Low"]
    priority_weights = [0.12, 0.28, 0.45, 0.15]

    # Generate dates across 2024-01-01 to 2026-09-30 (concentrated towards Q3/Q4)
    total_days = (datetime(2026, 9, 30) - datetime(2024, 1, 1)).days
    random_days = np.random.exponential(scale=total_days * 0.65, size=n_orders)
    random_days = np.clip(random_days, 0, total_days).astype(int)

    sales_records = []
    raw_sales_records = [] # for contaminated raw dataset

    order_counter = 10001
    for i in range(n_orders):
        order_date = datetime(2024, 1, 1) + timedelta(days=int(random_days[i]))
        # shipping lag between 1 and 6 days
        ship_lag = int(np.random.choice([1, 2, 3, 4, 5, 6], p=[0.08, 0.22, 0.35, 0.20, 0.10, 0.05]))
        ship_date = order_date + timedelta(days=ship_lag)

        cust_row = df_customer.iloc[np.random.randint(0, len(df_customer))]
        prod_row = df_product.iloc[np.random.randint(0, len(df_product))]

        # Quantity
        qty = int(np.random.choice([1, 2, 3, 4, 5, 6, 8, 10], p=[0.38, 0.26, 0.16, 0.09, 0.05, 0.03, 0.02, 0.01]))

        # Discount (0%, 5%, 10%, 15%, 20%, 30%)
        # Note: Heavy discounts on Furniture cause margin erosion (realistic business trend)
        if prod_row["Category"] == "Furniture":
            disc = float(np.random.choice([0.0, 0.10, 0.15, 0.20, 0.25, 0.35], p=[0.15, 0.20, 0.25, 0.20, 0.12, 0.08]))
        elif prod_row["Category"] == "Technology":
            disc = float(np.random.choice([0.0, 0.05, 0.10, 0.15], p=[0.45, 0.30, 0.18, 0.07]))
        else:
            disc = float(np.random.choice([0.0, 0.05, 0.10, 0.20], p=[0.40, 0.30, 0.20, 0.10]))

        unit_price = prod_row["Unit_Price"]
        unit_cost = prod_row["Cost_Price"]

        # Sales calculation
        gross_sales = unit_price * qty
        discount_amount = gross_sales * disc
        net_sales = round(gross_sales - discount_amount, 2)

        # Shipping cost based on mode
        ship_mode = np.random.choice(ship_modes, p=ship_weights)
        if ship_mode == "Same Day":
            ship_cost = round(qty * 450.0, 2)
        elif ship_mode == "First Class":
            ship_cost = round(qty * 250.0, 2)
        elif ship_mode == "Second Class":
            ship_cost = round(qty * 140.0, 2)
        else:
            ship_cost = round(qty * 75.0, 2)

        total_cost = (unit_cost * qty) + ship_cost
        profit = round(net_sales - total_cost, 2)
        profit_margin_pct = round((profit / net_sales) * 100, 2) if net_sales > 0 else 0.0

        order_id = f"ORD-{order_date.year}-{order_counter}"
        order_counter += 1

        rec = {
            "Order_ID": order_id,
            "Order_Date": order_date.strftime("%Y-%m-%d"),
            "Ship_Date": ship_date.strftime("%Y-%m-%d"),
            "Date_Key": int(order_date.strftime("%Y%m%d")),
            "Customer_Key": int(cust_row["Customer_Key"]),
            "Product_Key": int(prod_row["Product_Key"]),
            "Region_Key": int(cust_row["Region_Key"]),
            "Ship_Mode": ship_mode,
            "Order_Priority": np.random.choice(order_priorities, p=priority_weights),
            "Quantity": qty,
            "Unit_Price": unit_price,
            "Unit_Cost": unit_cost,
            "Discount_Rate": disc,
            "Discount_Amount": round(discount_amount, 2),
            "Sales_Amount": net_sales,
            "Shipping_Cost": ship_cost,
            "Total_Cost": round(total_cost, 2),
            "Profit": profit,
            "Profit_Margin_Pct": profit_margin_pct
        }
        sales_records.append(rec)
        raw_sales_records.append(dict(rec))

    df_sales = pd.DataFrame(sales_records)
    sales_path = base_dir / "Fact_Sales.csv"
    df_sales.to_csv(sales_path, index=False)
    print(f"[5/7] Generated Fact_Sales.csv ({len(df_sales)} verified sales transactions)")

    # -------------------------------------------------------------
    # 6. RAW_FACT_SALES (Contaminated dataset with intentional defects)
    # -------------------------------------------------------------
    # Introduce deliberate real-world data flaws:
    # 1. 20 exact duplicate rows
    # 2. 12 nulls in Profit, 8 nulls in Customer_Key, 6 nulls in Ship_Date
    # 3. Bad date format in some rows (e.g. DD/MM/YYYY instead of YYYY-MM-DD)
    # 4. Inconsistent column casing / spaces (" Sales_Amount ", "Cust_ID")
    # 5. Obsolete technical ingestion metadata columns ("ETL_Batch_ID", "Load_Timestamp", "Dummy_Flag")
    df_raw = df_sales.copy()

    # Add 20 duplicate rows
    dupes = df_raw.iloc[np.random.choice(len(df_raw), size=20, replace=False)].copy()
    df_raw = pd.concat([df_raw, dupes], ignore_index=True)

    # Inject missing values
    null_idx_profit = np.random.choice(len(df_raw), size=12, replace=False)
    df_raw.loc[null_idx_profit, "Profit"] = np.nan

    null_idx_cust = np.random.choice(len(df_raw), size=8, replace=False)
    df_raw.loc[null_idx_cust, "Customer_Key"] = np.nan

    null_idx_ship = np.random.choice(len(df_raw), size=6, replace=False)
    df_raw.loc[null_idx_ship, "Ship_Date"] = np.nan

    # Add obsolete technical columns
    df_raw["ETL_Batch_ID"] = [f"BATCH_2026_09_{idx%5}" for idx in range(len(df_raw))]
    df_raw["Sys_Load_Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df_raw["Legacy_System_Flag"] = "Y"

    # Save to Data/ and Task_2 folder
    raw_path = base_dir / "raw_fact_sales.csv"
    df_raw.to_csv(raw_path, index=False)

    task2_dir = base_dir.parent / "Task_2_Data_Cleaning_Preparation"
    task2_dir.mkdir(parents=True, exist_ok=True)
    df_raw.to_csv(task2_dir / "raw_fact_sales.csv", index=False)
    print(f"[6/7] Generated raw_fact_sales.csv ({len(df_raw)} records with intentional defects for Task 2 ETL)")

    # -------------------------------------------------------------
    # 7. EXCEL WORKBOOK (Retail_BI_Data_Model.xlsx)
    # -------------------------------------------------------------
    excel_path = base_dir / "Retail_BI_Data_Model.xlsx"
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        df_sales.to_excel(writer, sheet_name="Fact_Sales", index=False)
        df_customer.to_excel(writer, sheet_name="Dim_Customer", index=False)
        df_product.to_excel(writer, sheet_name="Dim_Product", index=False)
        df_region.to_excel(writer, sheet_name="Dim_Region", index=False)
        df_date.to_excel(writer, sheet_name="Dim_Date", index=False)

    print(f"[7/7] Generated Retail_BI_Data_Model.xlsx (Multi-tab structured Excel workbook)")
    print("=" * 80)
    print("ALL WEEK 5 STAR SCHEMA DATASETS SUCCESSFULLY CREATED & VERIFIED!")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    generate_data()
