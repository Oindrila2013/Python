DROP TABLE IF EXISTS Employees;
CREATE TABLE IF NOT EXISTS Employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary INTEGER NOT NULL
);

INSERT INTO Employees (emp_id, emp_name, department, salary) VALUES
(1, 'Amit', 'HR', 30000),
(2, 'Riya', 'IT', 50000),
(3, 'Karan', 'IT', 45000),
(4, 'Sneha', 'Finance', 60000),
(5, 'Rahul', 'HR', 35000),
(6, 'Priya', 'Finance', 70000);

SELECT * FROM Employees;

SELECT COUNT(*) AS Total_Employees FROM Employees;

SELECT SUM(salary) AS Total_Salary FROM Employees;

SELECT AVG(salary) AS Average_Salary FROM Employees;

SELECT MIN(salary) AS Minimum_Salary FROM Employees;

SELECT MAX(salary) AS Maximum_Salary FROM Employees;

SELECT * FROM Employees
WHERE department = 'IT';

SELECT * FROM Employees
WHERE salary > 50000;

SELECT SUM(salary) AS Total_IT_Salary
FROM Employees
WHERE department = 'IT';

SELECT department, SUM(salary) AS Total_Department_Salary
FROM Employees
GROUP BY department;

SELECT department, AVG(salary) AS Avg_Department_Salary
FROM Employees
GROUP BY department;

SELECT department, COUNT(*) AS Employee_Count
FROM Employees
GROUP BY department;

SELECT * FROM Employees
ORDER BY salary DESC;