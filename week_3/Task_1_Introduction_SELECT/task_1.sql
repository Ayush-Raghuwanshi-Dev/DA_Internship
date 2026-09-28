-- ============================================================================
-- TASK 1: INTRODUCTION TO DATABASES & SELECT STATEMENT
-- Student: Ayush | College: Prestige Institute of Engg, Mgmt & Research, Indore
-- ============================================================================

-- Query 1.1: Retrieve all columns and all records from Employees table
SELECT * 
FROM Employees;

-- Query 1.2: Select specific columns (Employee ID, Name, Job Title, and Monthly Salary)
SELECT 
    Emp_ID, 
    First_Name, 
    Last_Name, 
    Job_Title, 
    Salary
FROM Employees;

-- Query 1.3: Use column aliases (AS) to format output and calculate Annual Salary
SELECT 
    Emp_ID AS Employee_ID,
    First_Name || ' ' || Last_Name AS Full_Name,
    Job_Title AS Designation,
    Salary AS Monthly_Salary,
    (Salary * 12) AS Annual_Compensation
FROM Employees;
