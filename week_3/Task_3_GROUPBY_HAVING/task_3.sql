-- ============================================================================
-- TASK 3: GROUP BY & HAVING CLAUSES
-- Student: Ayush | College: Prestige Institute of Engg, Mgmt & Research, Indore
-- ============================================================================

-- Query 3.1: Basic GROUP BY on Department_ID with multiple aggregates
SELECT 
    Department_ID,
    COUNT(*) AS Headcount,
    ROUND(AVG(Salary), 2) AS Average_Salary,
    SUM(Salary) AS Total_Payroll,
    MIN(Salary) AS Min_Salary,
    MAX(Salary) AS Max_Salary
FROM Employees
WHERE Department_ID IS NOT NULL
GROUP BY Department_ID;

-- Query 3.2: GROUP BY with HAVING clause (Filter departments with Average Salary > 65,000)
SELECT 
    Department_ID,
    COUNT(*) AS Headcount,
    ROUND(AVG(Salary), 2) AS Average_Salary,
    SUM(Salary) AS Total_Payroll
FROM Employees
WHERE Department_ID IS NOT NULL
GROUP BY Department_ID
HAVING AVG(Salary) > 65000
ORDER BY Average_Salary DESC;

-- Query 3.3: GROUP BY with HAVING clause (Filter departments with Headcount >= 5)
SELECT 
    Department_ID,
    COUNT(*) AS Headcount,
    ROUND(AVG(Salary), 2) AS Average_Salary,
    SUM(Salary) AS Total_Payroll
FROM Employees
WHERE Department_ID IS NOT NULL
GROUP BY Department_ID
HAVING COUNT(*) >= 5;

-- Query 3.4: Grouping by City and Performance Rating
SELECT 
    City,
    Performance_Rating,
    COUNT(*) AS Employee_Count,
    ROUND(AVG(Salary), 2) AS Avg_Salary
FROM Employees
GROUP BY City, Performance_Rating
HAVING COUNT(*) > 1
ORDER BY City, Performance_Rating DESC;
