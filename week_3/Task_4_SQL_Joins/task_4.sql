-- ============================================================================
-- TASK 4: SQL JOINS (INNER, LEFT, RIGHT JOIN)
-- Student: Ayush | College: Prestige Institute of Engg, Mgmt & Research, Indore
-- ============================================================================

-- Query 4.1: INNER JOIN
-- Returns only records with matching Department_ID in BOTH tables.
-- Excludes unassigned employees (Tanvi Bansal) and empty departments (R&D).
SELECT 
    e.Emp_ID,
    e.First_Name || ' ' || e.Last_Name AS Employee_Name,
    e.Job_Title,
    d.Department_Name,
    d.Manager_Name,
    e.Salary
FROM Employees e
INNER JOIN Departments d 
    ON e.Department_ID = d.Department_ID
ORDER BY d.Department_Name, e.Salary DESC;


-- Query 4.2: LEFT JOIN (LEFT OUTER JOIN)
-- Returns ALL records from Employees (left table), matching Department details where available.
-- Preserves unassigned employees (e.g. Tanvi Bansal, Emp 125) with NULL department info.
SELECT 
    e.Emp_ID,
    e.First_Name || ' ' || e.Last_Name AS Employee_Name,
    e.Job_Title,
    COALESCE(d.Department_Name, 'Unassigned') AS Department_Name,
    COALESCE(d.Location, 'N/A') AS Dept_Location,
    e.Salary
FROM Employees e
LEFT JOIN Departments d 
    ON e.Department_ID = d.Department_ID
ORDER BY e.Emp_ID;


-- Query 4.3: RIGHT JOIN (RIGHT OUTER JOIN)
-- Returns ALL records from Departments (right table), matching Employees where available.
-- Preserves departments with zero staff (e.g. Research & Development) with NULL employee info.
SELECT 
    d.Department_ID,
    d.Department_Name,
    d.Manager_Name,
    d.Budget,
    e.Emp_ID,
    COALESCE(e.First_Name || ' ' || e.Last_Name, 'No Staff Assigned') AS Employee_Name,
    e.Salary
FROM Employees e
RIGHT JOIN Departments d 
    ON e.Department_ID = d.Department_ID
ORDER BY d.Department_ID, e.Salary DESC;
