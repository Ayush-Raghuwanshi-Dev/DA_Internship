-- ============================================================================
-- TASK 2: WHERE, ORDER BY & AGGREGATE FUNCTIONS
-- Student: Ayush | College: Prestige Institute of Engg, Mgmt & Research, Indore
-- ============================================================================

-- Query 2.1: Filter records using WHERE and comparison operators
-- Find all employees in Indore with Salary >= 70,000 and Performance Rating >= 4
SELECT 
    Emp_ID,
    First_Name,
    Last_Name,
    Job_Title,
    Salary,
    City,
    Performance_Rating
FROM Employees
WHERE City = 'Indore' 
  AND Salary >= 70000 
  AND Performance_Rating >= 4;

-- Query 2.2: Filter using BETWEEN and IN operators
-- Find employees with salary between 50,000 and 80,000 working in Department 1 or 2
SELECT 
    Emp_ID,
    First_Name,
    Last_Name,
    Department_ID,
    Salary
FROM Employees
WHERE Salary BETWEEN 50000 AND 80000
  AND Department_ID IN (1, 2);

-- Query 2.3: Sort records using ORDER BY (Multi-tier: Salary DESC, Hire_Date ASC)
SELECT 
    Emp_ID,
    First_Name,
    Last_Name,
    Job_Title,
    Salary,
    Hire_Date
FROM Employees
ORDER BY Salary DESC, Hire_Date ASC
LIMIT 10;

-- Query 2.4: Aggregate Functions: COUNT, SUM, AVG, MIN, MAX across entire company
SELECT 
    COUNT(*) AS Total_Employees,
    COUNT(Department_ID) AS Assigned_Employees,
    SUM(Salary) AS Total_Payroll,
    ROUND(AVG(Salary), 2) AS Average_Salary,
    MIN(Salary) AS Minimum_Salary,
    MAX(Salary) AS Maximum_Salary
FROM Employees;
