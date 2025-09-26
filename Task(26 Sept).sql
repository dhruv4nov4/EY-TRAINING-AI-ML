CREATE TABLE Employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10,2)
);

INSERT INTO Employees(name,age,department,salary)
VALUES
('DHRUV',21,'ML',90.54),
('ZOYA',22,'DL',78.12),
('Damon',23,'AI',70.54),
('Elena',24,'RL',88.12);
Select * from Employees;
SELECT name,marks FROM Employees;
SELECT * FROM Employees WHERE salary>90;

UPDATE Employees
SET salary = 95.12, department = 'devops'
WHERE id = 4;

DELETE FROM Employees WHERE id = 2;