# Week 2 - NumPy & Pandas for Data Analytics

**Student:** Ayush  
**Institution:** Prestige Institute of Engineering, Management & Research, Indore  
**Assignment:** NumPy & Pandas for Data Analytics  

---

## 📋 Overview
This directory contains all **10 practical tasks** completed for Week 2 of the Data Analytics Internship. The focus is on core NumPy and Pandas operations for data analysis, data manipulation, cleaning, aggregation, merging, pivoting, and an end-to-end Mini Data Analysis Project with a professional PDF report.

---

## 📁 Tasks Completed

| Task | Title | Description | Key Methods / Concepts |
|---|---|---|---|
| **Task 1** | **NumPy Introduction & Arrays** | Creating 1D and 2D NumPy arrays; inspecting properties. | `np.array()`, `.shape`, `.size`, `.dtype` |
| **Task 2** | **Indexing, Slicing & Reshaping** | Slicing 1D/2D arrays, indexing elements, and reshaping arrays. | Array slicing `[start:end]`, `np.reshape()`, 2D index `[r, c]` |
| **Task 3** | **Mathematical & Statistical Operations** | Element-wise arithmetic, aggregation, and statistical metrics. | `+`, `-`, `*`, `/`, `np.mean()`, `np.median()`, `np.std()`, `np.var()`, `np.min()`, `np.max()`, `np.sum()` |
| **Task 4** | **Pandas Series & DataFrames** | Constructing Series and DataFrames from Python dicts and lists. | `pd.Series()`, `pd.DataFrame()`, `.index`, `.columns`, `.dtypes` |
| **Task 5** | **Reading & Inspecting Data** | Loading CSV datasets and inspecting structure and statistics. | `pd.read_csv()`, `.head()`, `.tail()`, `.info()`, `.describe()`, `.shape` |
| **Task 6** | **Selection, Filtering & Sorting** | Column extraction, multi-condition Boolean filtering, sorting. | `df[['col']]`, `df[(cond1) & (cond2)]`, `df.sort_values()` |
| **Task 7** | **Handling Missing Values** | Detecting null values, filling with mean/defaults, dropping rows. | `df.isnull().sum()`, `df.fillna()`, `df.dropna()` |
| **Task 8** | **Merge, Concat, GroupBy & Pivot Tables** | Merging datasets on key columns, grouping, and pivoting. | `pd.merge()`, `df.groupby().agg()`, `pd.pivot_table()` |
| **Task 9** | **Exporting Data** | Saving cleaned and processed DataFrames to disk. | `df.to_csv()`, `index=False` |
| **Task 10** | **Mini Data Analysis Project** | End-to-end sales analysis: ingestion, cleaning, KPIs, product & regional breakdowns, customer spend distribution, and summary report. | Full pipeline analysis, metric calculations, summary file export |

---

## 📄 Deliverables

- **Task Scripts:** Python scripts (`task_1.py` through `task_10.py` / `mini_project.py`) organized in dedicated task folders.
- **Datasets:** Input and output CSV datasets (`sales_data.csv`, `product_data.csv`, `cleaned_sales_data.csv`, `processed_sales_data.csv`, etc.).
- **Summary Report:** `analysis_summary.txt` summarizing business insights and KPIs.
- **Report Script:** `generate_report.py` using ReportLab to dynamically generate the PDF report with verified outputs.
- **Official Report PDF:** [`Week_2_NumPy_Pandas_Report.pdf`](./Week_2_NumPy_Pandas_Report.pdf).

---

## 🛠️ Requirements & Installation

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

Dependencies:
- `numpy`
- `pandas`
- `reportlab`

---

## ▶️ Running the Tasks

Run each task script independently from its directory or the `week_2` folder:

```bash
# Example: Run Task 1
python Task_1_NumPy_Introduction/task_1.py

# Example: Run Task 10 Mini Project
python Task_10_Mini_Data_Analysis_Project/mini_project.py
```

To re-run all tasks and regenerate the comprehensive PDF report:

```bash
python generate_report.py
```
