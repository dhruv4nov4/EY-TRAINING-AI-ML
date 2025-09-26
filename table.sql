INSERT INTO Students(name,age,course,marks)
VALUES
('DHRUV',21,'ML',90),
('ZOYA',22,'DL',78);
Select * from Students;
SELECT name,marks FROM Students;
SELECT * FROM Students WHERE marks>80;

UPDATE Students
SET marks = 95, course = 'ai'
WHERE id = 4;

Select * from Students;

