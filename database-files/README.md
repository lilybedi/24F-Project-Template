# `database-files` Folder

TODO: Put some notes here about how this works.  include how to re-bootstrap the db. 

Tarini Shankar, Lillian Bedichek, Kalina Monova, Neel Avancha and Anya Khemlani

This document aims to outline the functionality of the Career-Compass database provides instructions for re-bootstrapping the database when necessary. This database contains critical elements of the platform, including user data for students, advisors, employers, and alumni, as well as job postings, application tracking, real-time updates, and mentorship connections. This database represents the relational model of the database through various primary and foreign keys that allow for a myriad of relationships between tables. 

To re-bootstrap the database,create the database. Then create tables that represent strong entities such as College, Company, Skill, System Admin, Student, Alumni, etc. Depict the relational nature of these tables using foreign keys such as Student_ID in order to represent the relational model. We then added a lot of data to our database so that we could accurately depict it, making sure to insert values that aligned with our specifications set in our "create table" statements.

Once ready, execute the script to create required tables, and populate them with initial data if applicable. After the script completes, verify the database setup by checking the schema and any predefined records. Finally, test the application to confirm seamless integration with the reinitialized database.