# Career Compass 
Tarini Shankar, Lillian Bedichek, Kalina Monova, Neel Avancha and Anya Khemlani

## Final Presentation Video Link 


## Env file setup
SECRET_KEY=someCrazyS3cR3T!Key.!
DB_USER=root
DB_HOST=db
DB_PORT=3306
DB_NAME=Career_Compass
MYSQL_ROOT_PASSWORD=MYSQLpassword

## Controlling the Containers

- `docker compose up -d` to start all the containers in the background
- `docker compose down` to shutdown and delete the containers
- `docker compose up db -d` only start the database container (replace db with the other services as needed)
- `docker compose stop` to "turn off" the containers but not delete them. 

## Project Overview 

Career Compass is a data-driven application designed to enhance NUWorks by revolutionizing how Northeastern students, advisors, alumni, and employers/companies connect in the search and application process. By centralizing and streamlining profile management, job applications, and advisor progress tracking, this app empowers a variety of end-users to ensure a curated, efficient, and effective co-op search process. For students seeking highly specific roles, our app offers advanced filtering and tailored recommendations to ensure each co-op position aligns with their skillset, location preferences, and pay requirements. Meanwhile, advisors can monitor their set of assigned students at a glance, and easily identify those needing extra support through our advanced dashboard. They will no longer have to send and wait for email responses on co-op status, our dashboard will update in real-time once a student accepts an offer!	 

Our app directly addresses critical pain points in the system by allowing companies to set minimum qualifications and job requirements, reducing time spent sifting through unqualified applications. It also allows for alumni to directly connect and mentor students without giving away sensitive information (phone number, etc). Key features include the ability for students to track their application history, advisors to view cohort-wide metrics, and employers to update job postings in real time. With this platform, each end-user has the tools to manage their co-op experience with confidence and transparency, fostering a stronger, more engaged Northeastern co-op program for all!

## Current Project Components

Currently, there are three major components which will each run in their own Docker Containers:

- Streamlit App in the `./app` directory
- Flask REST api in the `./api` directory
- SQL files for your data model and data base in the `./database-files` directory


## Users 

### Student 
A student currently taking classes at Northeastern needs to be able to apply to co-ops and use special filters, connect with alumni and their advisor. 
### Company Employee 
A company employee that needs to be able to post/edit a job with minimum requirements, view student applications and mark a posting as filled or delete it. 
### Student Advisor
An advisor needs to be able to interact with their students by viewing their applications. Should also be able to filter students that have and have not recieved co-ops and view their profiles. 
### Alumni 
An alumni who has graduated from Northeastern having done a co-op should be able to connect with students to give them advice. They should also be able to display thier previous co-op experiences. 
### System Administrator 
A system administrator should be able view tickets of errors that need fixing, resolve or delete these errors and they should have full control over all users including, deleting accounts. 

## Handling User Role Access and Control

Each persona is accessed by click on one of the Act as blank Buttons which brings the user to exclusive 

## Accessing Career Compass
http://localhost:8503/


 
