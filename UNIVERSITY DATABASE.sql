CREATE DATABASE UniversityDB;
USE UniversityDB;
-- Students Table
CREATE TABLE Students (
student_id INT PRIMARY KEY,
name VARCHAR(50),
city VARCHAR(50)
);
-- Courses Table
CREATE TABLE Courses (
course_id INT PRIMARY KEY,
course_name VARCHAR(50),
credits INT
);
-- Enrollments Table
CREATE TABLE Enrollments (
enroll_id INT PRIMARY KEY,
student_id INT,
course_id INT,
grade CHAR(2),
FOREIGN KEY (student_id) REFERENCES Students(student_id),
FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
-- Insert Students
INSERT INTO Students VALUES
(1, 'Rahul', 'Mumbai'),
(2, 'Priya', 'Delhi'),
(3, 'Arjun', 'Bengaluru'),
(4, 'Neha', 'Hyderabad'),
(5, 'Vikram', 'Chennai');
-- Insert Courses
INSERT INTO Courses VALUES
(101, 'Mathematics', 4),
(102, 'Computer Science', 3),
(103, 'Economics', 2),
(104, 'History', 3);
-- Insert Enrollments
INSERT INTO Enrollments VALUES
(1, 1, 101, 'A'),
(2, 1, 102, 'B'),
(3, 2, 103, 'A'),
(4, 3, 101, 'C'),
(5, 4, 102, 'B'),
(6, 5, 104, 'A');

DELIMITER $$
CREATE PROCEDURE ListAllStudents()
BEGIN
	SELECT * FROM Students;
END$$

DELIMITER ;
CALL ListAllStudents;

DELIMITER $$
CREATE PROCEDURE ListAllCourses()
BEGIN
	SELECT * FROM Courses;
END$$

DELIMITER ;
CALL ListAllCourses;

DELIMITER $$
CREATE PROCEDURE StudentsFromCity(IN city_name VARCHAR(50)) 
BEGIN  
	SELECT * FROM Students WHERE city=city_name; 
    END$$
DELIMITER ;
CALL StudentsFromCity('Delhi');

DELIMITER $$
CREATE PROCEDURE StudentswithCourses()
BEGIN
	SELECT s.student_id, s.name, c.course_name
    FROM Students s
    JOIN enrollments e ON s.student_id=e.student_id
    JOIN courses c ON e.course_id=c.course_id;
    
END$$
DELIMITER ;
CALL StudentswithCourses;

DELIMITER $$
CREATE PROCEDURE StudentsinCourses(IN course INT)
BEGIN
	SELECT s.student_id, s.name 
    FROM Students s
    JOIN enrollments e ON s.student_id=e.student_id
    WHERE e.course_id=course;
END$$
DELIMITER ;
CALL StudentsinCourses(102);

DELIMITER $$
CREATE PROCEDURE CountStudentsPerCourse()
BEGIN
	SELECT c.course_name, COUNT(e.student_id) AS student_count
    FROM Courses c
    LEFT JOIN enrollments e ON c.course_id=E.course_id
    GROUP BY c.course_name;
END$$
DELIMITER ;
CALL CountStudentsPerCourse;

DELIMITER $$
CREATE PROCEDURE StudentsCoursesGrades()
BEGIN
	SELECT s.student_id, s.name, c.course_name, e.grade
    FROM Students s
    JOIN enrollments e ON s.student_id=e.student_id
    JOIN courses c ON e.course_id=c.course_id;
    
END$$
DELIMITER ;
CALL StudentsCoursesGrades;

DELIMITER $$
CREATE PROCEDURE CoursesByStudents(IN student INT)
BEGIN
	SELECT c.course_name, e.grade
    FROM courses c
    JOIN enrollments e ON c.course_id=e.course_id
    WHERE e.student_id = student;
    
END$$
DELIMITER ;
CALL CoursesByStudents(3);

DELIMITER $$
CREATE PROCEDURE AvgGradePerCourse()
BEGIN
	SELECT c.course_name
		AVG( 
			CASE 
				when e.grade = 'A' then 4
                when e.grade ='B' then 3
                when e.grade ='C' then 2
                when e.grade ='D' then 1
                else 0
			END) as avggrade
    FROM courses c
    JOIN enrollments e ON c.course_id=e.course_id
    GROUP BY c.course_name;
END$$
DELIMITER ;
CALL AvgGradePerCourse();