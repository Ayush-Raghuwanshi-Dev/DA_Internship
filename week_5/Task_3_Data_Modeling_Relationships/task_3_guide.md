# Task 3 Guide: Data Modeling & Relationships (Star Schema)

**Student:** Ayush  
**Course:** B.Tech Computer Science & Engineering (IoT)  
**Institution:** Prestige Institute of Engineering, Management & Research (PIEMR), Indore  
**Assignment:** Week 5 — Power BI & Business Intelligence (Task 3: 15 Marks)  

---

## 1. Architectural Foundations of Data Modeling in Power BI

A robust data model is the core backbone of any Business Intelligence solution. In Power BI, data modeling involves structuring disparate raw tables into a cohesive relational architecture optimized for the **VertiPaq columnar in-memory database engine**.

### Fact Tables vs. Dimension Tables

```
                    ┌────────────────────────────────────────────────────────┐
                    │                      STAR SCHEMA                       │
                    └────────────────────────────────────────────────────────┘

                                    ┌───────────────────────┐
                                    │     Dim_Customer      │
                                    │ (Customer_Key [PK])   │
                                    └───────────┬───────────┘
                                                │ 1
                                                │
                                                │ *
┌───────────────────────┐           ┌───────────┴───────────┐           ┌───────────────────────┐
│      Dim_Region       │           │      Fact_Sales       │           │      Dim_Product      │
│  (Region_Key [PK])    ├───────────┤   (Order_ID [Deg])    ├───────────┤  (Product_Key [PK])   │
└───────────────────────┘ 1       * │ (Customer_Key [FK])   │ *       1 └───────────────────────┘
                                    │  (Product_Key [FK])   │
                                    │   (Region_Key [FK])   │
                                    │    (Date_Key [FK])    │
                                    └───────────┬───────────┘
                                                │ *
                                                │
                                                │ 1
                                    ┌───────────┴───────────┐
                                    │       Dim_Date        │
                                    │   (Date_Key [PK])     │
                                    └───────────────────────┘
```

1. **Fact Tables (`Fact_Sales`):**
   - Contains numerical, additive, or semi-additive metrics (e.g., `Sales_Amount`, `Quantity`, `Profit`, `Shipping_Cost`, `Discount_Amount`).
   - High row volume, updated continuously.
   - Contains foreign keys (`Customer_Key`, `Product_Key`, `Region_Key`, `Date_Key`) referencing dimensions.

2. **Dimension Tables (`Dim_Customer`, `Dim_Product`, `Dim_Region`, `Dim_Date`):**
   - Contains descriptive, qualitative attributes used for filtering, slicing, grouping, and drilling down (e.g., Customer Name, Segment, City, Product Category, Sub-Category, Year, Month).
   - Low to medium row volume, high attribute width.
   - Contains unique primary keys.

---

## 2. Why Star Schema is Superior to a Single Flat Table

| Evaluation Criterion | Flat Un-Normalized Table | Star Schema Architecture (Our Model) |
|---|---|---|
| **Memory Compression** | Low compression. Product names, categories, and customer addresses duplicate millions of times. | **Exceptional compression.** Text strings stored once in dictionary tables; fact table contains small integer surrogate keys. |
| **VertiPaq Column Scan** | Slow query scans across wide tables with 40+ columns. | **Blazing speed.** Scans narrow fact columns; filter propagation handled via lightweight relationship pointers. |
| **DAX Complexity** | Complex DAX expressions requiring manual deduplication filters. | **Clean, elegant DAX.** Simple aggregations (`SUM`, `AVERAGE`) filter naturally through relationship propagation. |
| **Maintenance & Integrity** | High risk of update anomalies. Changing a product category requires updating thousands of rows. | **Zero anomalies.** Update product attributes once in `Dim_Product`; automatically reflected across all transactions. |

---

## 3. Relational Key Mapping & Cardinality Specifications

Our production model establishes four primary active relationships and one inactive role-playing relationship:

| Source (Dimension) | Target (Fact Table) | Primary Key (1) | Foreign Key (*) | Cardinality | Filter Direction | Relationship State |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **`Dim_Customer`** | `Fact_Sales` | `Customer_Key` | `Customer_Key` | One-to-Many (`1:*`) | Single (`Dim` $\rightarrow$ `Fact`) | **Active** |
| **`Dim_Product`** | `Fact_Sales` | `Product_Key` | `Product_Key` | One-to-Many (`1:*`) | Single (`Dim` $\rightarrow$ `Fact`) | **Active** |
| **`Dim_Region`** | `Fact_Sales` | `Region_Key` | `Region_Key` | One-to-Many (`1:*`) | Single (`Dim` $\rightarrow$ `Fact`) | **Active** |
| **`Dim_Date`** | `Fact_Sales` | `Date_Key` | `Date_Key` | One-to-Many (`1:*`) | Single (`Dim` $\rightarrow$ `Fact`) | **Active (Order Date)** |
| **`Dim_Date`** | `Fact_Sales` | `Date_Key` | `Ship_Date_Key` | One-to-Many (`1:*`) | Single (`Dim` $\rightarrow$ `Fact`) | **Inactive (Ship Date)** |

---

## 4. Key Modeling Concepts & Best Practices

### A. Cardinality Choices:
- **One-to-Many (`1:*`):** The gold standard of relational modeling. Each customer or product appears exactly once in the dimension, but can participate in multiple purchase orders in the fact table.
- **Many-to-Many (`*:*`):** Strongly avoided unless strictly necessary, as it introduces ambiguity, non-deterministic performance penalties, and complex bridge table overhead.

### B. Cross-Filter Direction (Single vs. Both):
- **Single Direction (Selected):** Filters flow downstream from the dimension table to the fact table. Slicing by "Technology" filters `Fact_Sales` to only Technology records.
- **Bi-Directional Filtering (`Both`):** Allows fact table selections to filter dimension tables. Avoided as a global default because it creates circular reference loops, ambiguous filter paths, and significant performance degradation.

### C. Role-Playing Dimensions & `USERELATIONSHIP`:
- A transaction possesses multiple temporal milestones (Order Date vs. Ship Date).
- Power BI permits only **one active relationship** between any two tables at a given moment to maintain deterministic query execution.
- The Order Date relationship is marked **Active**. To analyze sales based on delivery dates, DAX dynamically invokes the inactive relationship:
  ```dax
  Sales by Delivery Date = 
  CALCULATE(
      [Total Sales],
      USERELATIONSHIP(Fact_Sales[Ship_Date_Key], Dim_Date[Date_Key])
  )
  ```
