

LOAD DATA [LOCAL] INFILE 'tarinishankar@Tarinis-MacBook-Pro/desktop/courses/24f-CS3200-shankar/Career-Compass/database-files/Advisor.csv'
INTO TABLE Advisor
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, First_Name, Last_Name, Title, Students_List, College_ID);

CREATE TABLE Advisor (
    id INT PRIMARY KEY,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Title VARCHAR(100),
    Students_List TEXT,
    College_ID INT
);
-- ####################################################################
-- # Basic INSERT statement
-- # See https://www.ibm.com/docs/en/db2-for-zos/13?topic=statements-insert for complete syntax.
-- ####################################################################
INSERT INTO table-name (column-name)
    VALUES (expression)