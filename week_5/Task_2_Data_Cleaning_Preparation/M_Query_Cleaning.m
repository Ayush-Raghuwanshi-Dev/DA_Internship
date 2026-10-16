// ==============================================================================
// Power Query M-Code: Data Cleaning, Preparation & Transformation Pipeline
// Assignment: Week 5 - Power BI & Business Intelligence (Task 2)
// Student: Ayush | Prestige Institute of Engineering, Management & Research, Indore
// Description: Automated ETL pipeline to clean, deduplicate, type-cast, impute,
//              and enrich raw transaction data into a production-ready fact table.
// ==============================================================================

let
    // 1. Data Source Ingestion
    Source = Csv.Document(
        File.Contents("D:\Internship\Week_5\week_5\Data\raw_fact_sales.csv"),
        [Delimiter=",", Columns=22, Encoding=65001, QuoteStyle=QuoteStyle.None]
    ),
    
    // 2. Promote First Row as Headers
    PromoteHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    
    // 3. Remove Obsolete Technical & Ingestion Metadata Columns
    RemoveUnnecessaryColumns = Table.RemoveColumns(
        PromoteHeaders,
        {"ETL_Batch_ID", "Sys_Load_Timestamp", "Legacy_System_Flag"}
    ),
    
    // 4. Remove Duplicate Transaction Records
    RemoveDuplicates = Table.Distinct(RemoveUnnecessaryColumns, {"Order_ID"}),
    
    // 5. Filter Corrupt Rows with Null Customer Keys
    FilterValidCustomerKeys = Table.SelectRows(RemoveDuplicates, each [Customer_Key] <> null and [Customer_Key] <> ""),
    
    // 6. Explicit Data Type Casting
    ChangeDataTypes = Table.TransformColumnTypes(
        FilterValidCustomerKeys,
        {
            {"Order_ID", type text},
            {"Order_Date", type date},
            {"Ship_Date", type date},
            {"Date_Key", Int64.Type},
            {"Customer_Key", Int64.Type},
            {"Product_Key", Int64.Type},
            {"Region_Key", Int64.Type},
            {"Ship_Mode", type text},
            {"Order_Priority", type text},
            {"Quantity", Int64.Type},
            {"Unit_Price", type number},
            {"Unit_Cost", type number},
            {"Discount_Rate", type number},
            {"Discount_Amount", type number},
            {"Sales_Amount", type number},
            {"Shipping_Cost", type number},
            {"Total_Cost", type number},
            {"Profit", type number},
            {"Profit_Margin_Pct", type number}
        }
    ),
    
    // 7. Handle Missing Values in Profit via Mathematical Recalculation
    // Formula: Net Sales - Total Cost
    ImputeMissingProfit = Table.ReplaceValue(
        ChangeDataTypes,
        each [Profit],
        each if [Profit] = null then [Sales_Amount] - [Total_Cost] else [Profit],
        Replacer.ReplaceValue,
        {"Profit"}
    ),
    
    // 8. Recompute Profit Margin Percentage if missing
    ImputeMissingMargin = Table.ReplaceValue(
        ImputeMissingProfit,
        each [Profit_Margin_Pct],
        each if [Profit_Margin_Pct] = null and [Sales_Amount] > 0 
             then Number.Round(([Profit] / [Sales_Amount]) * 100, 2) 
             else [Profit_Margin_Pct],
        Replacer.ReplaceValue,
        {"Profit_Margin_Pct"}
    ),
    
    // 9. Add Custom Conditional Column: Profitability Status
    AddProfitabilityBucket = Table.AddColumn(
        ImputeMissingMargin,
        "Profitability_Status",
        each if [Profit_Margin_Pct] >= 25.0 then "High Margin (>=25%)"
             else if [Profit_Margin_Pct] >= 10.0 then "Standard Margin (10-25%)"
             else if [Profit_Margin_Pct] >= 0.0 then "Low Margin (0-10%)"
             else "Loss-Making (<0%)",
        type text
    ),
    
    // 10. Add Custom Conditional Column: Order Size Category
    AddOrderSizeBucket = Table.AddColumn(
        AddProfitabilityBucket,
        "Order_Size_Category",
        each if [Quantity] >= 6 then "Bulk Order (6+ units)"
             else if [Quantity] >= 2 then "Multi-Item Order (2-5 units)"
             else "Single Item Order (1 unit)",
        type text
    ),
    
    // 11. Add Calculated Column: Delivery Duration in Days
    AddDeliveryDays = Table.AddColumn(
        AddOrderSizeBucket,
        "Delivery_Days",
        each Duration.Days([Ship_Date] - [Order_Date]),
        Int64.Type
    ),
    
    // 12. Rename Columns to Clean Business Presentation Standards
    RenameColumns = Table.RenameColumns(
        AddDeliveryDays,
        {
            {"Order_ID", "Order ID"},
            {"Order_Date", "Order Date"},
            {"Ship_Date", "Ship Date"},
            {"Ship_Mode", "Ship Mode"},
            {"Order_Priority", "Order Priority"},
            {"Unit_Price", "Unit Price"},
            {"Unit_Cost", "Unit Cost"},
            {"Discount_Rate", "Discount Rate"},
            {"Discount_Amount", "Discount Amount"},
            {"Sales_Amount", "Sales Amount"},
            {"Shipping_Cost", "Shipping Cost"},
            {"Total_Cost", "Total Cost"},
            {"Profit_Margin_Pct", "Profit Margin %"},
            {"Profitability_Status", "Profitability Status"},
            {"Order_Size_Category", "Order Size Category"},
            {"Delivery_Days", "Delivery Days"}
        }
    )
in
    RenameColumns
