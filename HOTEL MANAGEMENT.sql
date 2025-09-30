#STEP 1
CREATE DATABASE HospitalMgmt;
USE HospitalMgmt;
--  Patients Table
CREATE TABLE Patients (
patient_id INT PRIMARY KEY,
name VARCHAR(50),
age INT,
gender CHAR(1),
city VARCHAR(50)
);
-- Doctors Table
CREATE TABLE Doctors (
doctor_id INT PRIMARY KEY,
name VARCHAR(50),
specialization VARCHAR(50),
experience INT
);
-- Appointments Table
CREATE TABLE Appointments (
appointment_id INT PRIMARY KEY,
patient_id INT,
doctor_id INT,
appointment_date DATE,
status_s VARCHAR(20),
FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);
-- MedicalRecords Table
CREATE TABLE MedicalRecords (
record_id INT PRIMARY KEY,
patient_id INT,
doctor_id INT,
FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
diagnosis VARCHAR(100),
treatment VARCHAR(100),
date DATE
);
-- Billing Table
CREATE TABLE Billing (
bill_id INT PRIMARY KEY,
patient_id INT,
FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
amount DECIMAL(10,2),
bill_date DATE,
status VARCHAR(20)
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

#STEP 2
-- PATIENTS
INSERT INTO Patients (patient_id, name, age, gender, city) VALUES
(1, 'Ritika Mehra', 33, 'F', 'Mumbai'),
(2, 'Siddharth Malhotra', 38, 'M', 'Delhi'),
(3, 'Anjali Nair', 31, 'F', 'Bangalore'),
(4, 'Manish Sharma', 37, 'M', 'Kolkata'),
(5, 'Neha Patil', 29, 'F', 'Pune'),
(6, 'Rajiv Reddy', 42, 'M', 'Hyderabad'),
(7, 'Tanya Menon', 32, 'F', 'Chennai'),
(8, 'Karan Desai', 36, 'M', 'Ahmedabad'),
(9, 'Priya Joshi', 30, 'F', 'Lucknow'),
(10, 'Vikas Kumar', 39, 'M', 'Jaipur');

-- DOCTORS
INSERT INTO Doctors (doctor_id, name, specialization, experience) VALUES
(1, 'Dr. Varun Mehta', 'Cardiology', 15),
(2, 'Dr. Asha Kapoor', 'Orthopedics', 12),
(3, 'Dr. Sunil Iyer', 'Pediatrics', 10),
(4, 'Dr. Kavita Rao', 'Dermatology', 8),
(5, 'Dr. Pradeep Singh', 'Neurology', 20);

-- APPOINTMENTS
INSERT INTO Appointments (appointment_id, patient_id, doctor_id, appointment_date, status_s) VALUES
(1, 1, 1, '2025-09-01', 'Completed'),
(2, 2, 1, '2025-09-03', 'Pending'),
(3, 3, 2, '2025-09-05', 'Completed'),
(4, 4, 3, '2025-09-06', 'Completed'),
(5, 5, 4, '2025-09-07', 'Cancelled'),
(6, 6, 5, '2025-09-08', 'Pending'),
(7, 7, 1, '2025-09-10', 'Completed'),
(8, 8, 2, '2025-09-11', 'Completed'),
(9, 9, 3, '2025-09-12', 'Pending'),
(10, 10, 4, '2025-09-15', 'Completed');

-- MEDICALRECORDS
INSERT INTO MedicalRecords (record_id, patient_id, doctor_id, diagnosis, treatment, date) VALUES
(1, 1, 1, 'Hypertension', 'Medication A', '2025-09-01'),
(2, 2, 1, 'Arrhythmia', 'Medication B', '2025-09-03'),
(3, 3, 2, 'Fracture', 'Cast', '2025-09-05'),
(4, 4, 3, 'Flu', 'Rest & Medication', '2025-09-06'),
(5, 5, 4, 'Acne', 'Topical Cream', '2025-09-07'),
(6, 6, 5, 'Migraine', 'Medication C', '2025-09-08'),
(7, 7, 1, 'High Cholesterol', 'Diet & Medication', '2025-09-10'),
(8, 8, 2, 'Sprain', 'Physiotherapy', '2025-09-11'),
(9, 9, 3, 'Chickenpox', 'Medication D', '2025-09-12'),
(10, 10, 4, 'Eczema', 'Ointment', '2025-09-15');

-- BILLING
INSERT INTO Billing (bill_id, patient_id, amount, bill_date, status) VALUES
(1, 1, 5000.00, '2025-09-01', 'Paid'),
(2, 2, 7000.00, '2025-09-03', 'Unpaid'),
(3, 3, 3000.00, '2025-09-05', 'Paid'),
(4, 4, 1500.00, '2025-09-06', 'Unpaid'),
(5, 5, 2000.00, '2025-09-07', 'Paid'),
(6, 6, 4000.00, '2025-09-08', 'Unpaid'),
(7, 7, 6000.00, '2025-09-10', 'Paid'),
(8, 8, 3500.00, '2025-09-11', 'Unpaid'),
(9, 9, 4500.00, '2025-09-12', 'Paid'),
(10, 10, 2500.00, '2025-09-15', 'Unpaid');

#STEP 3
-- Step 3 : TASKS/EXERCISES
-- BASIC QUERIES
-- 1. List all patients assigned to a cardiologist.
SELECT p.patient_id, p.name, p.city
FROM Patients p
JOIN Appointments a ON p.patient_id = a.patient_id
JOIN Doctors d ON a.doctor_id = d.doctor_id
WHERE d.specialization = 'Cardiology';

-- 2. Find all appointments for a given doctor.
SELECT a.appointment_id, p.name AS patient_name, a.appointment_date, a.status_s
FROM Appointments a
JOIN Patients p ON a.patient_id = p.patient_id
WHERE a.doctor_id = 4; 

-- 3. Show unpaid bills of patients.
SELECT b.bill_id, p.name AS patient_name, b.amount, b.bill_date
FROM Billing b
JOIN Patients p ON b.patient_id = p.patient_id
WHERE b.status = 'Unpaid';

-- Stored Procedures
-- 4.Procedure: GetPatientHistory(patient_id) → returns all visits, diagnoses, and treatments for a patient.
DELIMITER $$
CREATE PROCEDURE GetPatientHistory(IN p_id INT)
BEGIN
    SELECT m.record_id, m.date, d.name AS doctor_name, m.diagnosis, m.treatment
    FROM MedicalRecords m
    JOIN Doctors d ON m.doctor_id = d.doctor_id
    WHERE m.patient_id = p_id
    ORDER BY m.date;
END$$
DELIMITER ;
CALL GetPatientHistory(5);

-- 5. Procedure: GetDoctorAppointments(doctor_id) → returns all appointments for a doctor.
DELIMITER $$
CREATE PROCEDURE GetDoctorAppointments(IN d_id INT)
BEGIN
    SELECT a.appointment_id, p.name AS patient_name, a.appointment_date, a.status_s
    FROM Appointments a
    JOIN Patients p ON a.patient_id = p.patient_id
    WHERE a.doctor_id = d_id
    ORDER BY a.appointment_date;
END$$
DELIMITER ;
CALL GetDoctorAppointments(2);

