CREATE TABLE Teachers (
	teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    subject_id INT,
    FOREIGN KEY (subject_id) REFERENCES Subjects (subject_id)
);

CREATE TABLE Subjects (
    subject_id INT auto_increment PRIMARY KEY,
    subject_name VARCHAR(50) NOT NULL
);

ALTER TABLE Teachers DROP FOREIGN KEY Teachers_ibfk_1;
TRUNCATE TABLE Teachers;
TRUNCATE TABLE Subjects;
DROP TABLE Teachers;
DROP TABLE Subjects;

INSERT INTO Teachers (name,subject_id)
VALUES
('DHRUV', 1),
('MIKE', 2),
('DAMON', 1);

INSERT INTO Subjects (subject_name)
VALUES
('PHYSICS'),
('CHEMISTRY'),
('MATHS');

SELECT t.name, t.subject_id, s.subject_name
FROM Teachers t
INNER JOIN Subjects s
ON t.subject_id = s.subject_id;

SELECT t.name, t.subject_id, s.subject_name
FROM Teachers t
LEFT JOIN Subjects s
ON t.subject_id = s.subject_id;

SELECT t.name, t.subject_id, s.subject_name
FROM Teachers t
RIGHT JOIN Subjects s
ON t.subject_id = s.subject_id;

SELECT t.name, t.subject_id, s.subject_name
FROM Teachers t
LEFT JOIN Subjects s
ON t.subject_id = s.subject_id;
UNION
SELECT t.name, t.subject_id, s.subject_name
FROM Teachers t
RIGHT JOIN Subjects s
ON t.subject_id = s.subject_id;

