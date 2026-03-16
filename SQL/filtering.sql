DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Marks;

CREATE TABLE IF NOT EXISTS Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    class INT,
    city VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Marks (
    mark_id INT PRIMARY KEY,
    student_id INT,
    subject VARCHAR(30),
    marks INT
);

INSERT INTO Students VALUES
(1, 'Rahim', 6, 'Dhaka'),
(2, 'Karim', 6, 'Chittagong'),
(3, 'Sumaiya', 7, 'Dhaka'),
(4, 'Nila', 6, 'Sylhet'),
(5, 'Rafi', 7, 'Dhaka');

INSERT INTO Marks VALUES
(1, 1, 'Math', 85),
(2, 1, 'English', 78),
(3, 2, 'Math', 92),
(4, 2, 'English', 88),
(5, 3, 'Math', 67),
(6, 4, 'Math', 95),
(7, 4, 'English', 90),
(8, 5, 'Math', 73);

SELECT *
FROM Students
WHERE class = 6;

SELECT *
FROM Students
WHERE name LIKE 'R%';

SELECT MAX(marks) AS highest_mark FROM Marks;

SELECT MIN(marks) AS lowest_mark FROM Marks;

SELECT AVG(marks) AS average_mark FROM Marks;

SELECT SUM(marks) AS total_marks FROM Marks;

SELECT student_id, SUM(marks) AS total_marks
FROM Marks
GROUP BY student_id;

SELECT *
FROM Marks
ORDER BY marks ASC;

SELECT *
FROM Marks
ORDER BY marks DESC;