CREATE DATABASE CompanyDB;
USE CompanyDB;

CREATE TABLE Departments (
	dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);

CREATE TABLE Employees (
    emp_id INT auto_increment PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    salary DECIMAL(10,2),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

INSERT INTO Departments(dept_name)
VALUES
('BANK'),
('FINANCE'),
('IT');

INSERT INTO Employees(name,age,salary,dept_id)
VALUES
('DHRUV',21,90.12,1),
('FZOYA',22,80.12,2),
('MIKE',23,70.34,3),
('Oggy',24,60.45,1);

# Removing data from table and we cant directly remove foreign key so use this command
ALTER TABLE Employees DROP FOREIGN KEY employees_ibfk_1;
TRUNCATE TABLE Employees;
TRUNCATE TABLE Departments;

SELECT e.name, e.salary, d.dept_name
FROM Employees e
INNER JOIN Departments d
ON e.dept_id = d.dept_id;

SELECT e.name, e.salary, d.dept_name
FROM Employees e
LEFT JOIN Departments d
ON e.dept_id = d.dept_id;

SELECT e.name, e.salary, d.dept_name
FROM Employees e
RIGHT JOIN Departments d
ON e.dept_id = d.dept_id;

#FULL JOIN
SELECT e.name, e.salary, d.dept_name
FROM Employees e
LEFT JOIN Departments d
ON e.dept_id = d.dept_id;
UNION
SELECT e.name, e.salary, d.dept_name
FROM Employees e
RIGHT JOIN Departments d
ON e.dept_id = d.dept_id;





