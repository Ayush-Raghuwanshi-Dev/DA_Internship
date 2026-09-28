-- ============================================================================
-- WEEK 3 DATA ANALYTICS INTERNSHIP: SQL & EXCEL ASSIGNMENT
-- Student: Ayush | College: Prestige Institute of Engg, Mgmt & Research, Indore
-- File: schema.sql - Relational Schema Definition
-- ============================================================================

DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Departments;

-- 1. Departments Table
CREATE TABLE Departments (
    Department_ID INTEGER PRIMARY KEY,
    Department_Name TEXT NOT NULL,
    Manager_Name TEXT NOT NULL,
    Location TEXT NOT NULL,
    Budget REAL NOT NULL
);

-- 2. Employees Table
CREATE TABLE Employees (
    Emp_ID INTEGER PRIMARY KEY,
    First_Name TEXT NOT NULL,
    Last_Name TEXT NOT NULL,
    Department_ID INTEGER,
    Job_Title TEXT NOT NULL,
    Salary REAL NOT NULL,
    Hire_Date TEXT NOT NULL,
    Performance_Rating INTEGER CHECK (Performance_Rating BETWEEN 1 AND 5),
    City TEXT NOT NULL,
    FOREIGN KEY (Department_ID) REFERENCES Departments(Department_ID)
);
