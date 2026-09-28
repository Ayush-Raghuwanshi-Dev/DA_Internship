# Task 8: VLOOKUP & XLOOKUP Functions

**Student:** Ayush  
**Course:** B.Tech CSE (IoT)  
**College:** Prestige Institute of Engineering, Management & Research, Indore  
**Workbook:** `Excel/Week_3_Excel_Data_Analytics.xlsx`  
**Sheet:** `Task_8_VLOOKUP_XLOOKUP`  

---

## 1. Task Objective

To demonstrate relational lookups between two structured Excel tables by comparing the classic **VLOOKUP()** function with the modern, flexible **XLOOKUP()** function, illustrating syntax, exact matching, and bi-directional capability.

---

## 2. Table Layout & Relationship

- **Primary Transaction Table** (`Columns A to F`):
  - Contains: `Emp ID`, `Employee Name`, `Dept ID`, `Salary`.
  - Goal: Retrieve the official `Department Name` and corresponding `Manager Name` dynamically from the catalog.
- **Reference Catalog Table** (`Columns I to M`):
  - Contains: `Dept ID` (Col I), `Department Name` (Col J), `Manager Name` (Col K), `Location` (Col L), `Budget` (Col M).

---

## 3. Function Implementations

### A. `VLOOKUP()` Implementation
- **Formula applied in Column E**:
  ```excel
  =VLOOKUP(C5, $I$5:$M$10, 2, FALSE)
  ```
- **Syntax Breakdown**:
  - `lookup_value` (`C5`): The `Dept ID` in the active row.
  - `table_array` (`$I$5:$M$10`): The absolute range containing department reference data.
  - `col_index_num` (`2`): The 2nd column of the reference table (`Department Name`).
  - `[range_lookup]` (`FALSE`): Enforces strict exact matching.

### B. `XLOOKUP()` Implementation
- **Formula applied in Column F**:
  ```excel
  =XLOOKUP(C5, $I$5:$I$10, $K$5:$K$10, "Unassigned")
  ```
- **Syntax Breakdown**:
  - `lookup_value` (`C5`): The `Dept ID` in the active row.
  - `lookup_array` (`$I$5:$I$10`): Column I containing department IDs.
  - `return_array` (`$K$5:$K$10`): Column K containing manager names.
  - `[if_not_found]` (`"Unassigned"`): Built-in graceful fallback when a department is missing or NULL (e.g. for Emp 125 Tanvi Bansal).

---

## 4. Architectural Comparison: VLOOKUP vs. XLOOKUP

| Evaluation Criteria | Classic `VLOOKUP()` | Modern `XLOOKUP()` |
| :--- | :--- | :--- |
| **Lookup Direction** | **Left-to-Right only.** Lookup key must be in the first column of the table array. | **Bi-directional.** Can look left, right, vertically, or horizontally. |
| **Column Modification Risk** | **Fragile.** Hard-coded column index (`2`) breaks if columns are inserted or deleted. | **Robust.** Range references (`$K$5:$K$10`) automatically adjust when columns move. |
| **Default Match Mode** | **Approximate Match by default.** Forgetting `FALSE` causes subtle lookup errors. | **Exact Match by default.** Safe and predictable for enterprise identifiers. |
| **Built-in Error Handling** | **None.** Requires wrapping formula in `=IFERROR(VLOOKUP(...), "Not Found")`. | **Native.** Built-in 4th argument `[if_not_found]` handles errors directly. |
| **Computational Overhead** | Slower on large datasets because it tracks the entire matrix table array. | Highly optimized; evaluates only the specified lookup and return vectors. |

---

## 5. Screenshot Capture Guide

- Open `Excel/Week_3_Excel_Data_Analytics.xlsx`.
- Switch to sheet **`Task_8_VLOOKUP_XLOOKUP`**.
- Capture the worksheet showing both the main transaction table (with `VLOOKUP` and `XLOOKUP` output columns populated) and the side Department Reference table and comparison box.
- Save image to: **`Screenshots/task_8_excel.png`**.
