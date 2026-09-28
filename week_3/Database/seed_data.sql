-- ============================================================================
-- WEEK 3 DATA ANALYTICS INTERNSHIP: SQL & EXCEL ASSIGNMENT
-- Student: Ayush | College: Prestige Institute of Engg, Mgmt & Research, Indore
-- File: seed_data.sql - Seed Records for Database
-- ============================================================================

-- 1. Insert Departments (6 records)
INSERT INTO Departments (Department_ID, Department_Name, Manager_Name, Location, Budget) VALUES
(1, 'Engineering', 'Rajesh Sharma', 'Indore', 1200000.00),
(2, 'Data Analytics', 'Pooja Verma', 'Indore', 850000.00),
(3, 'Human Resources', 'Anjali Mehta', 'Bhopal', 500000.00),
(4, 'Sales & Marketing', 'Vikram Singh', 'Indore', 950000.00),
(5, 'Finance', 'Suresh Nair', 'Bhopal', 750000.00),
(6, 'Research & Development', 'Dr. Meena Iyer', 'Indore', 1100000.00);

-- 2. Insert Employees (25 records)
INSERT INTO Employees (Emp_ID, First_Name, Last_Name, Department_ID, Job_Title, Salary, Hire_Date, Performance_Rating, City) VALUES
(101, 'Aarav', 'Sharma', 1, 'Senior Software Engineer', 88000.00, '2022-03-15', 5, 'Indore'),
(102, 'Diya', 'Patel', 2, 'Data Analyst', 62000.00, '2023-01-10', 4, 'Indore'),
(103, 'Kabir', 'Joshi', 1, 'DevOps Engineer', 78000.00, '2022-07-01', 4, 'Bhopal'),
(104, 'Meera', 'Rao', 2, 'Senior Data Analyst', 85000.00, '2021-11-20', 5, 'Indore'),
(105, 'Rohan', 'Verma', 4, 'Marketing Specialist', 54000.00, '2023-05-18', 3, 'Indore'),
(106, 'Sneha', 'Kulkarni', 3, 'HR Executive', 48000.00, '2022-09-12', 4, 'Bhopal'),
(107, 'Aditya', 'Mishra', 5, 'Financial Analyst', 66000.00, '2021-04-25', 4, 'Indore'),
(108, 'Neha', 'Gupta', 1, 'Frontend Developer', 60000.00, '2023-02-14', 3, 'Indore'),
(109, 'Varun', 'Deshmukh', 4, 'Sales Manager', 92000.00, '2020-08-19', 5, 'Bhopal'),
(110, 'Ishita', 'Chopra', 2, 'BI Developer', 72000.00, '2022-10-05', 4, 'Indore'),
(111, 'Manish', 'Tiwari', 5, 'Senior Accountant', 75000.00, '2021-01-15', 4, 'Bhopal'),
(112, 'Pooja', 'Bhatia', 3, 'HR Manager', 82000.00, '2020-06-30', 5, 'Indore'),
(113, 'Siddharth', 'Malhotra', 1, 'Backend Developer', 74000.00, '2022-12-01', 4, 'Indore'),
(114, 'Kavya', 'Saxena', 4, 'Content Strategist', 51000.00, '2023-06-10', 3, 'Bhopal'),
(115, 'Gaurav', 'Yadav', 2, 'Data Engineer', 80000.00, '2022-04-18', 4, 'Indore'),
(116, 'Ananya', 'Reddy', 1, 'QA Automation Engineer', 59000.00, '2023-03-22', 4, 'Bhopal'),
(117, 'Harsh', 'Vardhan', 5, 'Accountant', 52000.00, '2023-08-01', 3, 'Indore'),
(118, 'Ritu', 'Singhania', 4, 'Business Development Exec', 58000.00, '2022-11-15', 4, 'Indore'),
(119, 'Kunal', 'Pandey', 2, 'Junior Data Analyst', 45000.00, '2024-01-08', 3, 'Bhopal'),
(120, 'Priyanka', 'Dubey', 3, 'Talent Acquisition Exec', 49000.00, '2023-04-12', 3, 'Indore'),
(121, 'Amit', 'Chouhan', 1, 'System Architect', 115000.00, '2019-09-01', 5, 'Indore'),
(122, 'Sanjana', 'Bose', 4, 'Digital Marketer', 53000.00, '2023-07-19', 4, 'Bhopal'),
(123, 'Nikhil', 'Shukla', 5, 'Finance Executive', 48000.00, '2024-02-01', 3, 'Indore'),
(124, 'Bhavna', 'Rawat', 2, 'Machine Learning Analyst', 88000.00, '2021-12-10', 5, 'Indore'),
(125, 'Tanvi', 'Bansal', NULL, 'Graduate Trainee', 32000.00, '2024-03-01', 3, 'Indore');
