-- ============================================================================
-- TASK 5: SQL SUBQUERIES
-- Student: Ayush | College: Prestige Institute of Engg, Mgmt & Research, Indore
-- ============================================================================

-- Problem 1 (Scalar Subquery):
-- Find all employees earning more than the company-wide average salary
SELECT 
    Emp_ID,
    First_Name || ' ' || Last_Name AS Employee_Name,
    Job_Title,
    Salary,
    ROUND((SELECT AVG(Salary) FROM Employees), 2) AS Company_Avg_Salary
FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees)
ORDER BY Salary DESC;


-- Problem 2 (Multi-row Subquery with IN):
-- Find employees working in high-budget departments (Budget > Rs. 800,000)
SELECT 
    Emp_ID,
    First_Name || ' ' || Last_Name AS Employee_Name,
    Department_ID,
    Job_Title,
    Salary
FROM Employees
WHERE Department_ID IN (
    SELECT Department_ID 
    FROM Departments 
    WHERE Budget > 800000
)
ORDER BY Department_ID, Salary DESC;


-- Problem 3 (Correlated Subquery):
-- Find the top earner in each department
SELECT 
    e.Emp_ID,
    e.First_Name || ' ' || e.Last_Name AS Employee_Name,
    e.Department_ID,
    e.Job_Title,
    e.Salary
FROM Employees e
WHERE e.Salary = (
    SELECT MAX(sub.Salary) 
    FROM Employees sub 
    WHERE sub.Department_ID = e.Department_ID
)
ORDER BY e.Department_ID;
