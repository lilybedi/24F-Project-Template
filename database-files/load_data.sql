LOAD DATA INFILE '/path/to/Advisor.csv'
INTO TABLE Advisor
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, First_Name, Last_Name, Title, Students_List, College_ID);