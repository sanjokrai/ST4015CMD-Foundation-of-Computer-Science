-- ================================================
-- TASK 4: Basic SQL Operations
-- College Club Membership Management
-- ================================================

USE CollegeClub;

-- ================================================
-- 1. Insert a new student into the Student table
-- ================================================

INSERT INTO Student_3NF (StudentID, Name, Email)
VALUES (8, 'Priya', 'priya@email.com');

-- Verify the insert
SELECT * FROM Student_3NF;

-- ================================================
-- 2. Insert a new club into the Club table
-- ================================================

INSERT INTO Club_3NF (ClubName, ClubRoom, ClubMentor)
VALUES ('Art Club', 'R404', 'Ms. Puja');

-- Verify the insert
SELECT * FROM Club_3NF;

-- ================================================
-- 3. Display all students
-- ================================================

SELECT 
    StudentID,
    Name,
    Email
FROM Student_3NF
ORDER BY StudentID;

-- ================================================
-- 4. Display all clubs
-- ================================================

SELECT 
    ClubID,
    ClubName,
    ClubRoom,
    ClubMentor
FROM Club_3NF
ORDER BY ClubID;