DROP DATABASE IF EXISTS Career_Compass;

CREATE DATABASE IF NOT EXISTS Career_Compass;

USE Career_Compass;

CREATE TABLE System_Admin
(
    ID            INT AUTO_INCREMENT PRIMARY KEY,
    First_Name    VARCHAR(255),
    Last_Name     VARCHAR(255),
    Prefered_Name VARCHAR(255)
);

-- Create the Company table
CREATE TABLE Company
(
    ID                 INT AUTO_INCREMENT PRIMARY KEY,
    Name               VARCHAR(255) NOT NULL,
    Industry           VARCHAR(255),
    Description        TEXT
);

CREATE TABLE College
(
    Name VARCHAR(255),
    ID   INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE Major
(
    ID   INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255)
);

CREATE TABLE Minor
(
    ID   INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255)
);

-- Create the Skill table
CREATE TABLE Skill
(
    ID          INT AUTO_INCREMENT PRIMARY KEY,
    Name        VARCHAR(255) NOT NULL,
    Description TEXT,
    Industry    VARCHAR(255)
);

-- Create the Advisor table
CREATE TABLE Advisor
(
    ID            INT AUTO_INCREMENT PRIMARY KEY,
    First_Name    VARCHAR(255),
    Last_Name     VARCHAR(255),
    Prefered_Name VARCHAR(255), -- optional
    College_ID    INT NOT NULL,
    FOREIGN KEY (College_ID) REFERENCES College (ID)

);

CREATE TABLE Posting_Location
(
    ID             INT AUTO_INCREMENT PRIMARY KEY,
    Region         VARCHAR(255),
    State          VARCHAR(100),
    Zip_Code       CHAR(10),
    Address_Number INT,
    Street         VARCHAR(255),
    City           VARCHAR(255),
    Country        VARCHAR(100)
);


CREATE TABLE Posting
(
    ID          INT AUTO_INCREMENT PRIMARY KEY,
    Name        VARCHAR(255) NOT NULL,
    Company_ID  INT          NOT NULL,
    Industry    VARCHAR(255),
    Location    INT          NOT NULL,
    FOREIGN KEY (Company_ID) REFERENCES Company (ID),
    FOREIGN KEY (Location) REFERENCES Posting_Location (ID),
    Date_Start  DATE,
    Date_End    DATE,
    Filled      BOOLEAN,
    Minimum_GPA DECIMAL(3, 2) CHECK (Minimum_GPA >= 0 AND Minimum_GPA <= 4.0),
    Title       VARCHAR(255),
    Description TEXT,
    Pay         INT          NOT NULL
);

-- Create the Alumni table
CREATE TABLE Alumni
(
    ID         INT PRIMARY KEY,
    Title      VARCHAR(255),
    Grad_Year  INT NOT NULL,
    First_Name VARCHAR(255),
    Last_Name  VARCHAR(255),
    Email      VARCHAR(255),
    NUID       INT NOT NULL,
    College_ID INT NOT NULL,
    Opt_out    BOOLEAN,
    FOREIGN KEY (College_ID) REFERENCES College (ID)
);


CREATE TABLE Alumni_Position
(
    Position_ID INT NOT NULL,
    Alumni_ID   INT NOT NULL,
    PRIMARY KEY (Position_ID, Alumni_ID),
    FOREIGN KEY (Position_ID) REFERENCES Posting (ID),
    FOREIGN KEY (Alumni_ID) REFERENCES Alumni (ID)
);

CREATE TABLE Cycle
(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    cycle VARCHAR(50) NOT NULL
);

-- Create the Student table
CREATE TABLE Student
(
    ID            INT AUTO_INCREMENT PRIMARY KEY,
    First_Name    VARCHAR(255) NOT NULL,
    Last_Name     VARCHAR(255) NOT NULL,
    Prefered_Name VARCHAR(255),
    GPA           DECIMAL(3, 2) CHECK (GPA >= 0 AND GPA <= 4.0),
    College_ID    INT         NOT NULL,
    FOREIGN KEY (College_ID) REFERENCES College (ID),
    Grad_Year     INT          NOT NULL,
    Cycle         INT NOT NULL,
    Advisor_ID    INT          NOT NULL,
    Eligibility   BOOLEAN,
    Hired         BOOLEAN,
    FOREIGN KEY (Advisor_ID) REFERENCES Advisor (ID),
    FOREIGN KEY (Cycle) REFERENCES Cycle (ID),
    Resume_Link VARCHAR(255),
    Email VARCHAR(255),
    Phone_Number VARCHAR(255),
    Description TEXT,
);

CREATE TABLE Student_Majors (
    Student_ID INT NOT NULL,
    Major_ID INT NOT NULL,
    PRIMARY KEY (Student_ID, Major_ID),
    FOREIGN KEY (Student_ID) REFERENCES Student(ID),
    FOREIGN KEY (Major_ID) REFERENCES Major(ID)
);

CREATE TABLE Student_Minors (
    Student_ID INT NOT NULL,
    Minor_ID INT NOT NULL,
    PRIMARY KEY (Student_ID, Minor_ID),
    FOREIGN KEY (Student_ID) REFERENCES Student(ID),
    FOREIGN KEY (Minor_ID) REFERENCES Minor(ID)
);



-- Create the Posting_Skills table (junction table)
CREATE TABLE Posting_Skills
(
    Position_ID INT NOT NULL,
    Skill_ID    INT NOT NULL,
    PRIMARY KEY (Position_ID, Skill_ID),
    FOREIGN KEY (Position_ID) REFERENCES Posting (ID),
    FOREIGN KEY (Skill_ID) REFERENCES Skill (ID)
);

-- Create the Student_Skills table (junction table)
CREATE TABLE Student_Skills
(
    Student_ID INT NOT NULL,
    Skill_ID   INT NOT NULL,
    PRIMARY KEY (Student_ID, Skill_ID),
    FOREIGN KEY (Student_ID) REFERENCES Student (ID),
    FOREIGN KEY (Skill_ID) REFERENCES Skill (ID)
);

-- Create the Application table
CREATE TABLE Application
(
    ID          INT AUTO_INCREMENT PRIMARY KEY,
    Student_ID  INT NOT NULL,
    Position_ID INT NOT NULL,
    Accepted BOOLEAN,
    Resume_Link VARCHAR(255),
    FOREIGN KEY (Student_ID) REFERENCES Student (ID),
    FOREIGN KEY (Position_ID) REFERENCES Posting (ID)

);

CREATE TABLE Question
(
    ID             INT AUTO_INCREMENT PRIMARY KEY,
    Question       TEXT NOT NULL,
    Answer         TEXT,
    Application_ID INT  NOT NULL,
    FOREIGN KEY (Application_ID) REFERENCES Application (ID)
);


CREATE TABLE Ticket
(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Reporter_ID INT NOT NULL,
    Buggy_Entity_ID INT,
    FOREIGN KEY (Reporter_ID) REFERENCES System_Admin (ID),
    Message VARCHAR(255),
    Completed BOOLEAN
);

CREATE TABLE Message
(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    RE INT,
    FOREIGN KEY (RE) REFERENCES Message (ID),
    Student_ID INT NOT NULL,
    FOREIGN KEY (Student_ID) REFERENCES Student (ID),
    Message    TEXT,
    Alumni_ID  INT NOT NULL,
    FOREIGN KEY (Alumni_ID) REFERENCES Alumni (ID)
);



# Insert Statements 

# System_Admin Insert Statements
INSERT INTO System_Admin (First_Name, Last_Name, Prefered_Name)
VALUES
INSERT INTO System_Admin (First_Name, Last_Name, Prefered_Name)
VALUES
('John', 'Doe', 'Johnny'),
('Jane', 'Smith', 'Janie'),
('Michael', 'Johnson', 'Mike'),
('Emily', 'Brown', 'Em'),
('Chris', 'Evans', 'Chrisy'),
('Anna', 'Taylor', 'Annie'),
('David', 'Wilson', 'Dave'),
('Sarah', 'Moore', 'Sarah'),
('Daniel', 'Anderson', 'Dan'),
('Laura', 'White', 'Laurie'),
('James', 'Harris', 'Jim'),
('Olivia', 'Martin', 'Liv'),
('Robert', 'Thompson', 'Rob'),
('Sophia', 'Garcia', 'Soph'),
('William', 'Martinez', 'Will'),
('Isabella', 'Rodriguez', 'Bella'),
('Benjamin', 'Lee', 'Ben'),
('Mia', 'Perez', 'Mimi'),
('Charles', 'Clark', 'Charlie'),
('Charlotte', 'Lewis', 'Charlie'),
('Joseph', 'Walker', 'Joe'),
('Amelia', 'Young', 'Amy'),
('Thomas', 'Allen', 'Tom'),
('Harper', 'King', 'Harpy'),
('Henry', 'Wright', 'Hank'),
('Evelyn', 'Scott', 'Evy'),
('Alexander', 'Hill', 'Alex'),
('Abigail', 'Green', 'Abby'),
('Jackson', 'Adams', 'Jack'),
('Emily', 'Baker', 'Emmy'),
('Lucas', 'Nelson', 'Luke'),
('Grace', 'Carter', 'Gracie'),
('Matthew', 'Mitchell', 'Matt'),
('Chloe', 'Perez', 'Chloe'),
('Sebastian', 'Roberts', 'Seb'),
('Victoria', 'Turner', 'Vicky'),
('Owen', 'Phillips', 'Oweny'),
('Ella', 'Campbell', 'Ellie'),
('Jacob', 'Parker', 'Jake'),
('Scarlett', 'Evans', 'Scar'),
('Jack', 'Edwards', 'Jacky'),
('Madison', 'Collins', 'Maddie'),
('Liam', 'Stewart', 'Liam'),
('Zoey', 'Sanchez', 'Zoe'),
('Aiden', 'Morris', 'Aid'),
('Hannah', 'Rogers', 'Hanny'),
('Ethan', 'Reed', 'Ethan'),
('Lily', 'Cook', 'Lil'),
('Noah', 'Morgan', 'Noah'),
('Emily', 'Bailey', 'Emy');


# Company Insert Statements
INSERT INTO Company (Name, Industry, Description)
VALUES
INSERT INTO Company (Name, Industry, Description)
VALUES
('Tech Innovators', 'Software Engineer', 'A leading technology firm focused on developing innovative AI-driven solutions for businesses, governments, and educational institutions.'),
('Green Future Inc.', 'Renewable Energy Expert', 'Dedicated to creating sustainable energy solutions, including solar farms and wind energy, to help reduce carbon emissions globally.'),
('Urban Creators Co.', 'Architect', 'Specializing in modern, eco-friendly urban designs, focusing on maximizing space while maintaining environmental sustainability.'),
('Health First LLC', 'Medical Researcher', 'A cutting-edge medical research organization working on innovative treatments for chronic diseases and advancing telemedicine technologies.'),
('EduTrackers Inc.', 'Data Scientist', 'A leader in education technology, creating tools for tracking student performance and personalizing learning experiences through AI.'),
('BuildIt Ltd.', 'Construction Manager', 'An innovative construction company with a mission to design and build sustainable, resilient infrastructure for smart cities.'),
('NextGen AI', 'AI Specialist', 'A trailblazer in artificial intelligence, offering machine learning tools and services that empower industries to automate complex tasks.'),
('Marketing Masters', 'Digital Marketer', 'An agency that crafts unique digital marketing strategies using big data and analytics to drive customer engagement and growth.'),
('CodeCrafts LLC', 'Backend Developer', 'Building robust and scalable backend systems for applications in finance, healthcare, and e-commerce industries.'),
('Global Connect', 'Business Consultant', 'Connecting businesses across borders with strategic insights, market research, and operational optimization.'),
('DesignWorks Studio', 'Graphic Designer', 'Creating visually stunning brand identities, marketing materials, and web designs for companies in diverse sectors.'),
('MediCare Plus', 'Healthcare Admin', 'Providing advanced patient management systems and streamlining healthcare operations with innovative IT solutions.'),
('RenewEnergy Corp.', 'Solar Engineer', 'Pioneering solar power technology to create affordable and efficient energy solutions for residential and commercial use.'),
('AgriTech Solutions', 'Agricultural Engineer', 'Innovating the agriculture sector with smart irrigation, precision farming, and advanced crop monitoring systems.'),
('FinWise LLC', 'Financial Analyst', 'Helping businesses make informed financial decisions through comprehensive data-driven analysis and strategic planning.'),
('EcoBuilders Co.', 'Eco Consultant', 'Providing consultancy on sustainable building practices and green certifications to reduce environmental footprints.'),
('TranspoNet', 'Logistics Specialist', 'Optimizing global supply chains by integrating AI and IoT solutions for better efficiency and transparency.'),
('CleanWater Initiative', 'Environmental Specialist', 'Committed to providing clean water access to underserved communities using sustainable water purification technologies.'),
('Edutech World', 'Instructional Designer', 'Developing innovative e-learning platforms and tools to revolutionize education for all age groups.'),
('Innovatech Labs', 'Data Engineer', 'Designing large-scale data pipelines and implementing data warehouse solutions for multinational corporations.'),
('FutureFoods Inc.', 'Food Scientist', 'Advancing the food industry by creating sustainable and nutrient-rich food alternatives to address global food security.'),
('SmartHome Ltd.', 'IoT Specialist', 'Transforming homes with smart IoT devices that enhance security, energy efficiency, and everyday convenience.'),
('GreenLeaf Solutions', 'Sustainability Expert', 'Helping organizations implement eco-friendly practices to meet their sustainability goals and reduce waste.'),
('LegalTech LLC', 'Legal Consultant', 'Empowering law firms with AI tools for contract analysis, case prediction, and streamlined legal workflows.'),
('HealthTrackers Co.', 'Healthcare Analyst', 'Specializing in predictive analytics to improve patient outcomes and streamline hospital operations.'),
('FinanceWorks', 'Accountant', 'Providing financial planning, auditing, and tax advisory services tailored for small and medium enterprises.'),
('CodeBuddies', 'Frontend Developer', 'Creating responsive and visually appealing front-end designs for web and mobile applications across industries.'),
('Creative Minds', 'UX Designer', 'Delivering user-centric design solutions that enhance digital experiences and drive customer satisfaction.'),
('SecureTech', 'Cybersecurity Analyst', 'Providing state-of-the-art cybersecurity services to protect businesses from ever-evolving digital threats.'),
('MediaWorks', 'Media Consultant', 'Helping brands navigate the digital media landscape with strategic campaigns and content development.'),
('SocializeNow', 'Social Media Manager', 'Creating data-driven social media campaigns to increase brand visibility and engage target audiences.'),
('FastTrack Logistics', 'Transport Manager', 'Offering seamless shipping and transportation services by leveraging advanced route optimization technologies.'),
('SolarWise', 'Renewable Energy Consultant', 'Promoting clean energy solutions by designing and implementing large-scale solar power projects worldwide.'),
('GreenZone', 'Environmental Planner', 'Focused on developing urban green spaces and sustainable city planning for healthier communities.'),
('SmartNet', 'Network Engineer', 'Designing and maintaining reliable, high-speed network infrastructures for corporate and public sectors.'),
('BrightFuture', 'Teacher', 'Innovating classroom education with interactive and personalized teaching methods to inspire future generations.'),
('AppWorks', 'Mobile Developer', 'Developing user-friendly mobile applications that cater to a variety of needs, from fitness tracking to e-commerce.'),
('TravelSmart', 'Tourism Specialist', 'Crafting personalized travel experiences that combine adventure with sustainability for global explorers.'),
('DataDynamics', 'Data Analyst', 'Helping organizations uncover actionable insights from big data through advanced visualization and analytics tools.'),
('RetailBoost', 'Merchandiser', 'Assisting retailers in optimizing inventory and boosting sales with tailored merchandising strategies.'),
('PowerGrid Corp.', 'Electrical Engineer', 'Enhancing energy distribution systems with smart grid technologies for a more reliable power supply.'),
('NextStep', 'Career Coach', 'Providing career guidance and professional development resources to help individuals achieve their goals.'),
('HealthConnect', 'Health IT Specialist', 'Developing health IT solutions to improve communication and data management in healthcare systems.'),
('FarmTech', 'Agricultural Technician', 'Revolutionizing agriculture with drone technology and automated machinery for efficient farming.'),
('CodeSavvy', 'Software Tester', 'Ensuring software quality through rigorous testing and debugging processes to deliver reliable applications.'),
('Innovative Labs', 'Research Scientist', 'Driving groundbreaking scientific discoveries in pharmaceuticals, AI, and renewable energy sectors.'),
('BrightEnergy Co.', 'Renewable Energy Analyst', 'Leading the way in renewable energy adoption by analyzing and implementing solar and wind energy solutions.'),
('HomeCare Inc.', 'Care Specialist', 'Providing compassionate home care services for elderly and disabled individuals to improve their quality of life.'),
('NetSecure', 'Cybersecurity Consultant', 'Protecting businesses from cyber threats with cutting-edge security solutions and risk management strategies.');

# College Insert Statements
INSERT INTO College (Name)
VALUES
('Harvard University'),
('Stanford University'),
('Massachusetts Institute of Technology');


# Major Insert Statements
INSERT INTO Major (Name)
VALUES
('Computer Science'),
('Mechanical Engineering'),
('Business Administration');

# Minor Insert Statements
INSERT INTO Minor (Name)
VALUES
('Data Science'),
('Mathematics'),
('Environmental Studies');

# Skill Insert Stattements
INSERT INTO Skill (Name, Description, Industry)
VALUES
('Python', 'Programming language used for data science and software development.', 'Technology'),
('Leadership', 'Ability to lead teams and manage projects.', 'Management'),
('Machine Learning', 'Expertise in building AI-driven systems.', 'Artificial Intelligence');

# Advisor Insert Statements
INSERT INTO Advisor (First_Name, Last_Name, Prefered_Name, College_ID)
VALUES
('Emily', 'Brown', 'Em', 1),
('Chris', 'Evans', 'CE', 2),
('Anna', 'White', NULL, 3);


# Posting_Location Insert Statements
INSERT INTO Posting_Location (Region, State, Zip_Code, Address_Number, Street, City, Country)
VALUES
('Northeast', 'Massachusetts', '02139', 123, 'Main St', 'Cambridge', 'USA'),
('West Coast', 'California', '94016', 456, 'Market St', 'San Francisco', 'USA'),
('Midwest', 'Illinois', '60601', 789, 'Lake Shore Dr', 'Chicago', 'USA');


# Posting Insert Statements
INSERT INTO Posting (Name, Company_ID, Industry, Location, Date_Start, Date_End, Filled, Minimum_GPA, Title, Description, Pay)
VALUES
('Software Engineer Intern', 1, 'Technology', 1, '2024-06-01', '2024-08-31', FALSE, 3.5, 'Internship', 'Assist with developing ML models.', 6000),
('Project Manager Intern', 2, 'Management', 2, '2024-06-01', '2024-08-31', FALSE, 3.2, 'Internship', 'Support project management tasks.', 5000),
('Data Analyst Intern', 3, 'Data Science', 3, '2024-06-01', '2024-08-31', TRUE, 3.8, 'Internship', 'Analyze large datasets for insights.', 5500);


# Alumni Insert Statements
INSERT INTO Alumni (ID, Title, Grad_Year, First_Name, Last_Name, Email, NUID, College_ID, Opt_out)
VALUES
(1, 'Dr.', 2020, 'Sarah', 'Connor', 'sconnor@example.com', 123456, 1, FALSE),
(2, 'Mr.', 2018, 'James', 'Carter', 'jcarter@example.com', 234567, 2, TRUE),
(3, 'Ms.', 2021, 'Laura', 'Adams', 'ladams@example.com', 345678, 3, FALSE);


# Alumni_Position Insert Statements
INSERT INTO Alumni_Position (Position_ID, Alumni_ID)
VALUES
(1, 1),
(2, 2),
(3, 3);


# Student Insert Statements
INSERT INTO Student (First_Name, Last_Name, Prefered_Name, Major, Minor, GPA, College_ID, Grad_Year, Cycle, Advisor_ID, Eligibility, Hired, Resume_Link, Email, Phone_Number, Description, NUID)
VALUES
('Alex', 'Johnson', 'AJ', 1, 2, 3.8, 1, 2025, 'Fall', 1, TRUE, FALSE, 'link1.pdf', 'ajohnson@example.com', '123-456-7890', 'Looking for a software engineering internship.', 456789),
('Taylor', 'Smith', 'Tay', 2, 1, 3.6, 2, 2026, 'Spring', 2, TRUE, TRUE, 'link2.pdf', 'tsmith@example.com', '987-654-3210', 'Interested in data science roles.', 567890),
('Jordan', 'Lee', NULL, 3, NULL, 3.9, 3, 2027, 'Summer', 3, TRUE, FALSE, 'link3.pdf', 'jlee@example.com', '456-789-1230', 'Aspiring business analyst.', 678901);

# Posting_Skills Insert Statements
INSERT INTO Posting_Skills (Position_ID, Skill_ID)
VALUES
(1, 1),
(1, 3),
(2, 2),
(3, 1),
(3, 3);

# Student_Skills Insert Statements
INSERT INTO Student_Skills (Student_ID, Skill_ID)
VALUES
(1, 1),
(1, 3),
(2, 2),
(3, 1),
(3, 3);


# Application Insert Statements
INSERT INTO Application (Student_ID, Position_ID, Accepted, Resume_Link)
VALUES
(1, 1, TRUE, 'link1.pdf'),
(2, 2, FALSE, 'link2.pdf'),
(3, 3, TRUE, 'link3.pdf');


# Question Insert Statements
INSERT INTO Question (Question, Answer, Application_ID)
VALUES
('Why do you want this internship?', 'To gain real-world experience in software engineering.', 1),
('What is your greatest strength?', 'Problem-solving and teamwork.', 2),
('Describe a challenging project you worked on.', 'Developed a data pipeline for analyzing large datasets.', 3);


# Ticket Insert Statements
INSERT INTO Ticket (Reporter_ID, Buggy_Entity_ID, Message, Completed)
VALUES
(1, 2, 'Error in application submission.', FALSE),
(2, 1, 'Duplicate entries in the alumni table.', TRUE),
(3, 3, 'Skill data not populating correctly.', FALSE);

# Message Insert Statements
INSERT INTO Message (RE, Student_ID, Message, Alumni_ID)
VALUES
(NULL, 1, 'Congratulations on your application!', 1),
(1, 2, 'Thank you for the update!', 2),
(NULL, 3, 'Welcome to the platform!', 3);
