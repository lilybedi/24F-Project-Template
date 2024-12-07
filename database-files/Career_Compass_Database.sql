DROP DATABASE IF EXISTS Career_Compass;

CREATE DATABASE IF NOT EXISTS Career_Compass;

USE Career_Compass;


-- Create the Skill table
CREATE TABLE Skill
(
    ID          INT AUTO_INCREMENT PRIMARY KEY,
    Name        VARCHAR(255) NOT NULL,
    Description TEXT,
    Industry    VARCHAR(255)
);


CREATE TABLE System_Admin
(
    ID            INT AUTO_INCREMENT PRIMARY KEY,
    First_Name    VARCHAR(255),
    Last_Name     VARCHAR(255),
    Preferred_Name VARCHAR(255)
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

CREATE TABLE FieldOfStudy (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Description TEXT
);

-- Create the Advisor table
CREATE TABLE Advisor
(
    ID            INT AUTO_INCREMENT PRIMARY KEY,
    First_Name    VARCHAR(255),
    Last_Name     VARCHAR(255),
    Preferred_Name VARCHAR(255), -- optional
    College_ID    INT NOT NULL,
    FOREIGN KEY (College_ID) REFERENCES College (ID)
);


CREATE TABLE Alumni
(
    ID         INT AUTO_INCREMENT PRIMARY KEY,
    Grad_Year  INT NOT NULL,
    First_Name VARCHAR(255),
    Last_Name  VARCHAR(255),
    Email      VARCHAR(255),
    College_ID INT NOT NULL,
    FOREIGN KEY (College_ID) REFERENCES College (ID)
);

CREATE TABLE Alumni_Majors
(
    Alumni_ID INT NOT NULL,
    FieldOfStudy_ID INT NOT NULL,
    PRIMARY KEY (Alumni_ID, FieldOfStudy_ID),
    FOREIGN KEY (Alumni_ID) REFERENCES Alumni(ID),
    FOREIGN KEY (FieldOfStudy_ID) REFERENCES FieldOfStudy(ID)
);

CREATE TABLE Alumni_Minors
(
    Alumni_ID INT NOT NULL,
    FieldOfStudy_ID INT NOT NULL,
    PRIMARY KEY (Alumni_ID, FieldOfStudy_ID),
    FOREIGN KEY (Alumni_ID) REFERENCES Alumni(ID),
    FOREIGN KEY (FieldOfStudy_ID) REFERENCES FieldOfStudy(ID)
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
    Preferred_Name VARCHAR(255),
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
    Description TEXT
);

CREATE TABLE Student_Majors
(
    Student_ID INT NOT NULL,
    FieldOfStudy_ID INT NOT NULL,
    PRIMARY KEY (Student_ID, FieldOfStudy_ID),
    FOREIGN KEY (Student_ID) REFERENCES Student(ID),
    FOREIGN KEY (FieldOfStudy_ID) REFERENCES FieldOfStudy(ID)
);

CREATE TABLE Student_Minors
(
    Student_ID INT NOT NULL,
    FieldOfStudy_ID INT NOT NULL,
    PRIMARY KEY (Student_ID, FieldOfStudy_ID),
    FOREIGN KEY (Student_ID) REFERENCES Student(ID),
    FOREIGN KEY (FieldOfStudy_ID) REFERENCES FieldOfStudy(ID)
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

-- Create the Status table
CREATE TABLE Status
(
    ID          INT AUTO_INCREMENT PRIMARY KEY,
    Status_Description VARCHAR(50) NOT NULL
);


-- Create the Application table
CREATE TABLE Application
(
    ID          INT AUTO_INCREMENT PRIMARY KEY,
    Student_ID  INT NOT NULL,
    Position_ID INT NOT NULL,
    submittedDate DATETIME NOT NULL,
    Status_ID INT NOT NULL,
    FOREIGN KEY (Student_ID) REFERENCES Student (ID),
    FOREIGN KEY (Position_ID) REFERENCES Posting (ID),
    FOREIGN KEY (Status_ID) REFERENCES Status (ID)
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

ALTER TABLE Student_Skills DROP FOREIGN KEY Student_Skills_ibfk_1;
ALTER TABLE Student_Skills ADD FOREIGN KEY (Student_ID) REFERENCES Student(ID) ON DELETE CASCADE;

ALTER TABLE Student_Majors DROP FOREIGN KEY Student_Majors_ibfk_1;
ALTER TABLE Student_Majors ADD FOREIGN KEY (Student_ID) REFERENCES Student(ID) ON DELETE CASCADE;

ALTER TABLE Student_Minors DROP FOREIGN KEY Student_Minors_ibfk_1;
ALTER TABLE Student_Minors ADD FOREIGN KEY (Student_ID) REFERENCES Student(ID) ON DELETE CASCADE;

ALTER TABLE Application DROP FOREIGN KEY Application_ibfk_1;
ALTER TABLE Application ADD FOREIGN KEY (Student_ID) REFERENCES Student(ID) ON DELETE CASCADE;

ALTER TABLE Message DROP FOREIGN KEY Message_ibfk_2;
ALTER TABLE Message ADD FOREIGN KEY (Student_ID) REFERENCES Student(ID) ON DELETE CASCADE;

-- Modify Alumni-related foreign keys
ALTER TABLE Alumni_Position DROP FOREIGN KEY Alumni_Position_ibfk_2;
ALTER TABLE Alumni_Position ADD FOREIGN KEY (Alumni_ID) REFERENCES Alumni(ID) ON DELETE CASCADE;

ALTER TABLE Alumni_Majors DROP FOREIGN KEY Alumni_Majors_ibfk_1;
ALTER TABLE Alumni_Majors ADD FOREIGN KEY (Alumni_ID) REFERENCES Alumni(ID) ON DELETE CASCADE;

ALTER TABLE Alumni_Minors DROP FOREIGN KEY Alumni_Minors_ibfk_1;
ALTER TABLE Alumni_Minors ADD FOREIGN KEY (Alumni_ID) REFERENCES Alumni(ID) ON DELETE CASCADE;

ALTER TABLE Message DROP FOREIGN KEY Message_ibfk_4;
ALTER TABLE Message ADD FOREIGN KEY (Alumni_ID) REFERENCES Alumni(ID) ON DELETE CASCADE;

-- Note: For Advisor, we need to handle the Student table since it references Advisor
ALTER TABLE Student DROP FOREIGN KEY Student_ibfk_2;
ALTER TABLE Student ADD FOREIGN KEY (Advisor_ID) REFERENCES Advisor(ID) ON DELETE CASCADE;


ALTER TABLE Question DROP FOREIGN KEY Question_ibfk_1;
ALTER TABLE Question 
ADD CONSTRAINT Question_ibfk_1
FOREIGN KEY (Application_ID) REFERENCES Application(ID) ON DELETE CASCADE;


 -- Insert Statements

 -- Skill Insert
INSERT INTO Skill (Name, Description, Industry)
VALUES
('Python', 'Programming language used for data science, web development, and AI.', 'Technology'),
('Leadership', 'Ability to guide, influence, and inspire teams to achieve goals.', 'Management'),
('Data Analysis', 'Process of inspecting, cleaning, and interpreting data.', 'Data Science'),
('Machine Learning', 'Application of algorithms to create systems that learn and adapt.', 'Artificial Intelligence'),
('Marketing Strategy', 'Planning and executing marketing campaigns to achieve business objectives.', 'Marketing'),
('Project Management', 'Planning, organizing, and managing resources to complete specific goals.', 'Management'),
('SEO', 'Optimizing websites to rank higher in search engine results.', 'Digital Marketing'),
('Digital Marketing', 'Promoting products or services through online channels.', 'Marketing'),
('Web Development', 'Building and maintaining websites.', 'Software Development'),
('Public Speaking', 'Delivering speeches and presentations effectively.', 'Communication'),
('Negotiation', 'Reaching mutually beneficial agreements in professional settings.', 'Business'),
('Graphic Design', 'Creating visual content using tools like Photoshop and Illustrator.', 'Design'),
('UX Design', 'Designing user-friendly interfaces and experiences.', 'Design'),
('Content Writing', 'Creating written content for websites, blogs, and other mediums.', 'Media'),
('Customer Service', 'Providing support and resolving issues for customers.', 'Retail'),
('Social Media Marketing', 'Promoting brands using social media platforms.', 'Marketing'),
('Financial Analysis', 'Analyzing financial data to support business decisions.', 'Finance'),
('Time Management', 'Organizing time effectively to meet deadlines.', 'Productivity'),
('Team Management', 'Coordinating and leading teams to achieve objectives.', 'Management'),
('Entrepreneurship', 'Developing and managing business ventures.', 'Business'),
('Event Planning', 'Organizing and coordinating events.', 'Hospitality'),
('Programming', 'Writing code in various languages like Java, C++, and Python.', 'Technology'),
('Data Visualization', 'Representing data in graphical formats for analysis.', 'Data Science'),
('Cloud Computing', 'Using cloud-based services for data storage and processing.', 'Technology'),
('Cybersecurity', 'Protecting systems and networks from cyber threats.', 'Technology'),
('Research', 'Investigating and analyzing to discover new information.', 'Academia'),
('Presentation Skills', 'Delivering engaging and effective presentations.', 'Communication'),
('Operations Management', 'Overseeing and improving business operations.', 'Management'),
('Artificial Intelligence', 'Creating systems that mimic human intelligence.', 'Technology'),
('Salesforce', 'Using CRM tools for managing customer relationships.', 'Business'),
('Public Relations', 'Managing the public image of organizations.', 'Media'),
('Supply Chain Management', 'Overseeing the flow of goods and services.', 'Logistics'),
('Branding', 'Developing a strong and consistent brand identity.', 'Marketing'),
('Mobile Development', 'Creating applications for mobile devices.', 'Technology'),
('Financial Reporting', 'Preparing and analyzing financial statements.', 'Finance'),
('SQL', 'Using structured query language for database management.', 'Technology'),
('Python for Data Science', 'Specialized Python skills for analyzing large datasets.', 'Data Science'),
('Email Marketing', 'Engaging customers through targeted email campaigns.', 'Marketing'),
('Human Resources', 'Managing employee relations and organizational development.', 'HR'),
('Statistics', 'Analyzing data and trends using mathematical principles.', 'Data Science'),
('Strategic Planning', 'Developing strategies to achieve long-term goals.', 'Business'),
('Biotechnology', 'Using biological processes for industrial purposes.', 'Healthcare'),
('Game Development', 'Designing and creating video games.', 'Entertainment'),
('Physics Simulations', 'Creating simulations to study physical systems.', 'Academia'),
('Engineering Design', 'Designing systems and processes in engineering.', 'Engineering'),
('Mathematics', 'Applying mathematical theories to solve problems.', 'Academia'),
('Customer Relationship Management', 'Building strong relationships with customers.', 'Sales'),
('Business Development', 'Identifying opportunities to grow businesses.', 'Business'),
('Digital Transformation', 'Adopting digital technology to improve business processes.', 'Technology'),
('JavaScript', 'Programming language for interactive web applications.', 'Technology'),
('Linux Administration', 'Managing Linux-based operating systems.', 'IT'),
('Cloud Architecture', 'Designing cloud solutions and infrastructures.', 'Technology'),
('Blockchain', 'Using distributed ledger technologies for secure transactions.', 'Finance'),
('Machine Learning Operations', 'Operationalizing machine learning models in production.', 'Technology'),
('Video Editing', 'Creating and editing video content.', 'Media'),
('Product Management', 'Managing the development and lifecycle of products.', 'Business'),
('Embedded Systems', 'Programming hardware-level applications.', 'Engineering'),
('Renewable Energy', 'Developing sustainable energy solutions.', 'Energy');


-- System_Admin Insert Statements
INSERT INTO System_Admin (First_Name, Last_Name, Preferred_Name)
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


 -- Company Insert Statements
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

 -- College Insert Statements
INSERT INTO College (Name)
VALUES
('Harvard University'),
('Stanford University'),
('Massachusetts Institute of Technology'),
('University of California, Berkeley'),
('California Institute of Technology'),
('University of Chicago'),
('Columbia University'),
('Princeton University'),
('Yale University'),
('Cornell University'),
('University of Pennsylvania'),
('Duke University'),
('Johns Hopkins University'),
('University of Michigan, Ann Arbor'),
('Northwestern University'),
('University of California, Los Angeles (UCLA)'),
('University of Virginia'),
('New York University (NYU)'),
('University of Texas at Austin'),
('University of Washington'),
('Carnegie Mellon University'),
('University of Southern California'),
('University of North Carolina, Chapel Hill'),
('Georgia Institute of Technology'),
('Brown University'),
('Vanderbilt University'),
('Rice University'),
('University of Florida'),
('University of Wisconsin, Madison'),
('University of Illinois at Urbana-Champaign'),
('University of Minnesota, Twin Cities'),
('Pennsylvania State University'),
('University of Maryland, College Park'),
('University of California, San Diego'),
('Boston University'),
('University of Rochester'),
('Purdue University'),
('Michigan State University'),
('Indiana University, Bloomington'),
('University of Arizona'),
('University of Colorado, Boulder'),
('University of California, Irvine'),
('University of California, Davis'),
('University of Massachusetts, Amherst'),
('University of Georgia'),
('Florida State University'),
('University of Miami'),
('Ohio State University'),
('Arizona State University'),
('Alabama');


 -- FieldOFStudy Insert Statements
INSERT INTO FieldOfStudy (Name, Description)
VALUES
('Computer Science', 'Study of computation, algorithms, and systems.'),
('Mathematics', 'Study of numbers, quantities, and shapes.'),
('Business Administration', 'Management of businesses and organizations.'),
('Economics', 'Study of production, distribution, and consumption of goods.'),
('Psychology', 'Study of the human mind and behavior.'),
('Biology', 'Study of living organisms.'),
('Chemistry', 'Study of matter and its interactions.'),
('Physics', 'Study of matter, energy, and forces.'),
('Political Science', 'Study of political systems and behavior.'),
('Sociology', 'Study of social behavior and societies.'),
('Philosophy', 'Study of knowledge, reality, and existence.'),
('English Literature', 'Study of written works in the English language.'),
('History', 'Study of past events and their impact.'),
('Art History', 'Study of art and its historical development.'),
('Anthropology', 'Study of human societies and cultures.'),
('Linguistics', 'Study of language and its structure.'),
('Environmental Science', 'Study of the environment and its protection.'),
('Data Science', 'Study of extracting knowledge from data.'),
('Cybersecurity', 'Study of protecting computer systems and networks.'),
('Marketing', 'Study of promoting and selling products or services.'),
('Accounting', 'Study of financial transactions and reporting.'),
('Finance', 'Study of managing money and investments.'),
('Public Relations', 'Study of managing public image and communication.'),
('Graphic Design', 'Study of creating visual content.'),
('International Relations', 'Study of political and economic relations between countries.'),
('Journalism', 'Study of collecting, writing, and reporting news.'),
('Health Sciences', 'Study of health and healthcare systems.'),
('Education', 'Study of teaching and learning processes.'),
('Pre-Medicine', 'Preparation for medical school.'),
('Pre-Law', 'Preparation for law school.'),
('Theater Arts', 'Study of acting, directing, and theater production.'),
('Music', 'Study of musical theory and practice.'),
('Neuroscience', 'Study of the nervous system.'),
('Film Studies', 'Study of cinema and its production.'),
('Sports Management', 'Study of managing sports organizations.'),
('Criminal Justice', 'Study of law enforcement and criminal behavior.'),
('Urban Planning', 'Study of designing and managing urban areas.'),
('Public Policy', 'Study of creating and evaluating government policies.'),
('Sustainability Studies', 'Study of sustainable practices and development.'),
('Environmental Engineering', 'Engineering solutions to environmental challenges.'),
('Agricultural Science', 'Study of farming and food production.'),
('Biomedical Engineering', 'Application of engineering principles to healthcare.'),
('Mechanical Engineering', 'Study of machines and mechanical systems.'),
('Civil Engineering', 'Study of infrastructure and construction.'),
('Electrical Engineering', 'Study of electrical systems and circuits.'),
('Chemical Engineering', 'Study of chemical processes in manufacturing.'),
('Hospitality Management', 'Study of managing hotels and tourism.'),
('Supply Chain Management', 'Study of managing supply chains.'),
('Game Design', 'Study of creating video games.'),
('Artificial Intelligence', 'Study of intelligent systems and algorithms.');

INSERT INTO Advisor (First_Name, Last_Name, Preferred_Name, College_ID)
VALUES
('Emily', 'Brown', 'Em', 1),
('Chris', 'Evans', 'CE', 2),
('Anna', 'White', NULL, 3),
('David', 'Wilson', 'Dave', 4),
('Sarah', 'Moore', 'Sarah', 5),
('Michael', 'Johnson', 'Mike', 6),
('Laura', 'Taylor', 'Laurie', 7),
('James', 'Harris', 'Jim', 8),
('Sophia', 'Martinez', 'Soph', 9),
('William', 'Garcia', 'Will', 10),
('Isabella', 'Rodriguez', 'Bella', 11),
('Benjamin', 'Lee', 'Ben', 12),
('Charlotte', 'Clark', 'Charlie', 13),
('Joseph', 'Walker', 'Joe', 14),
('Amelia', 'Young', 'Amy', 15),
('Henry', 'Allen', 'Hank', 16),
('Evelyn', 'King', 'Evy', 17),
('Alexander', 'Wright', 'Alex', 18),
('Abigail', 'Scott', 'Abby', 19),
('Jackson', 'Hill', 'Jack', 20),
('Emily', 'Green', 'Emmy', 21),
('Lucas', 'Adams', 'Luke', 22),
('Grace', 'Baker', 'Gracie', 23),
('Matthew', 'Nelson', 'Matt', 24),
('Chloe', 'Carter', 'Chloe', 25),
('Sebastian', 'Mitchell', 'Seb', 26),
('Victoria', 'Perez', 'Vicky', 27),
('Owen', 'Roberts', 'Oweny', 28),
('Ella', 'Turner', 'Ellie', 29),
('Jacob', 'Phillips', 'Jake', 30),
('Scarlett', 'Campbell', 'Scar', 31),
('Jack', 'Parker', 'Jacky', 32),
('Madison', 'Collins', 'Maddie', 33),
('Liam', 'Stewart', 'Liam', 34),
('Zoey', 'Sanchez', 'Zoe', 35),
('Aiden', 'Morris', 'Aid', 36),
('Hannah', 'Rogers', 'Hanny', 37),
('Ethan', 'Reed', 'Ethan', 38),
('Lily', 'Cook', 'Lil', 39),
('Noah', 'Morgan', 'Noah', 40),
('Emily', 'Bailey', 'Emy', 41),
('Olivia', 'Cruz', 'Liv', 42),
('Daniel', 'Rivera', 'Dan', 43),
('Zoe', 'Torres', 'Zozo', 44),
('Mason', 'Gomez', 'Mace', 45),
('Sophia', 'Diaz', 'Sophy', 46),
('James', 'Ramirez', 'Jimbo', 47),
('Mia', 'Hernandez', 'Mimi', 48),
('Alexander', 'Flores', 'Alex', 49),
('Emma', 'Nguyen', 'Em', 50);


-- Alumni Insert Statements
INSERT INTO Alumni (Grad_Year, First_Name, Last_Name, Email, College_ID)
VALUES
(2001, 'Emma', 'Walsh', 'emma.walsh@gmail.com', 16),
(2014, 'Kimberly', 'Chung', 'kimberly.chung@data.com', 43),
(2020, 'Michelle', 'Johnson', 'michelle.johnson@pm.com', 21),
(2014, 'Debra', 'Wilson', 'debra.wilson@pm.com', 14),
(2000, 'Jennifer', 'Farrell', 'jennifer.farrell@marketing.com', 30),
(2013, 'William', 'Freeman', 'william.freeman@finance.com', 20),
(2010, 'Gary', 'Bryant', 'gary.bryant@hr.com', 36),
(2020, 'Terri', 'Coleman', 'terri.coleman@design.com', 37),
(1993, 'Melissa', 'Lee', 'melissa.lee@web.com', 16),
(2013, 'Jennifer', 'Hernandez', 'jennifer.hernandez@ai.com', 40),
(2004, 'Seth', 'Stout', 'seth.stout@it.com', 13),
(1992, 'Patrick', 'Johns', 'patrick.johns@edu.com', 50),
(2023, 'Gail', 'Murphy', 'gail.murphy@tech.com', 3),
(1993, 'Cynthia', 'Fritz', 'cynthia.fritz@bio.com', 2),
(1998, 'Nancy', 'Lane', 'nancy.lane@finance.com', 35),
(1999, 'Lisa', 'Williams', 'lisa.williams@edu.com', 3),
(2008, 'Jason', 'Smith', 'jason.smith@cs.com', 36),
(2016, 'Shawn', 'Garcia', 'shawn.garcia@marketing.com', 43),
(2018, 'Angela', 'Nichols', 'angela.nichols@design.com', 40),
(2012, 'William', 'Ochoa', 'william.ochoa@edu.com', 19),
(2010, 'Scott', 'Turner', 'scott.turner@tech.com', 10),
(2010, 'Jennifer', 'Quinn', 'jennifer.quinn@bio.com', 48),
(2012, 'Timothy', 'Huffman', 'timothy.huffman@cs.com', 32),
(1998, 'Melinda', 'Payne', 'melinda.payne@edu.com', 39),
(1997, 'John', 'Barnett', 'john.barnett@tech.com', 3),
(2023, 'Daniel', 'Velez', 'daniel.velez@marketing.com', 25),
(2003, 'Danielle', 'Reid', 'danielle.reid@design.com', 46),
(1994, 'Lynn', 'Hoffman', 'lynn.hoffman@bio.com', 17),
(2010, 'Marie', 'Foster', 'marie.foster@cs.com', 42),
(2006, 'Johnathan', 'Lam', 'johnathan.lam@web.com', 33),
(2001, 'Damon', 'Hines', 'damon.hines@tech.com', 37),
(1999, 'Katherine', 'Bell', 'katherine.bell@design.com', 31),
(2016, 'Mary', 'Keller', 'mary.keller@finance.com', 23),
(1998, 'Denise', 'Smith', 'denise.smith@edu.com', 28),
(2009, 'Andrew', 'Ferrell', 'andrew.ferrell@bio.com', 31),
(1993, 'Christie', 'Hernandez', 'christie.hernandez@tech.com', 48),
(2021, 'Christopher', 'Hunter', 'christopher.hunter@cs.com', 39),
(2012, 'Sara', 'Hall', 'sara.hall@edu.com', 7),
(2007, 'Stephanie', 'Daniels', 'stephanie.daniels@ai.com', 38),
(1999, 'Matthew', 'Bullock', 'matthew.bullock@marketing.com', 10),
(1993, 'Bailey', 'Scott', 'bailey.scott@design.com', 31),
(2021, 'Megan', 'Chang', 'megan.chang@bio.com', 8),
(1998, 'Danny', 'Hernandez', 'danny.hernandez@cs.com', 5),
(2017, 'Samantha', 'Meza', 'samantha.meza@web.com', 34),
(2017, 'Penny', 'Martinez', 'penny.martinez@finance.com', 15),
(2023, 'Ann', 'Beck', 'ann.beck@edu.com', 8),
(1993, 'Christopher', 'Kennedy', 'christopher.kennedy@tech.com', 15),
(2001, 'Lauren', 'Rodgers', 'lauren.rodgers@design.com', 8),
(1996, 'Angela', 'Ross', 'angela.ross@bio.com', 12),
(1996, 'Alex', 'Price', 'alex.price@cs.com', 8),
(2003, 'Crystal', 'Vargas', 'crystal.vargas@ai.com', 43),
(2020, 'Adam', 'Yang', 'adam.yang@finance.com', 23),
(2013, 'William', 'Hanson', 'william.hanson@edu.com', 23),
(2024, 'Emily', 'Williams', 'emily.williams@tech.com', 3),
(2000, 'Sara', 'Sutton', 'sara.sutton@design.com', 6),
(1990, 'Brandi', 'Williams', 'brandi.williams@bio.com', 47),
(1992, 'Joshua', 'Lewis', 'joshua.lewis@cs.com', 31),
(1996, 'Rebecca', 'Drake', 'rebecca.drake@web.com', 8),
(1992, 'Valerie', 'Dunn', 'valerie.dunn@edu.com', 34),
(2017, 'Lori', 'Moran', 'lori.moran@ai.com', 26);

-- Alumni Major Entries
INSERT INTO Alumni_Majors (Alumni_ID, FieldOfStudy_ID) VALUES
(1, 1), (1, 15),
(2, 3),
(3, 7), (3, 12),
(4, 2),
(5, 8), (5, 22),
(6, 4),
(7, 9),
(8, 5), (8, 18),
(9, 10),
(10, 6),
(11, 11), (11, 25),
(12, 13),
(13, 14), (13, 28),
(14, 16),
(15, 17), (15, 30),
(16, 19),
(17, 20),
(18, 21), (18, 35),
(19, 23),
(20, 24),
(21, 26),
(22, 27), (22, 38),
(23, 29),
(24, 31),
(25, 32), (25, 40),
(26, 33),
(27, 34),
(28, 36),
(29, 37), (29, 42),
(30, 39),
(31, 1),
(32, 3), (32, 15),
(33, 5),
(34, 7),
(35, 9), (35, 22),
(36, 11),
(37, 13), (37, 25),
(38, 2),
(39, 4),
(40, 6), (40, 28),
(41, 8),
(42, 10),
(43, 12), (43, 30),
(44, 14),
(45, 16),
(46, 18), (46, 33),
(47, 20),
(48, 24), (48, 35),
(49, 26),
(50, 28);

-- Alumni Minor Entries
INSERT INTO Alumni_Minors (Alumni_ID, FieldOfStudy_ID) VALUES
(1, 2),
(2, 4), (2, 16),
(3, 6),
(4, 8), (4, 20),
(5, 10),
(6, 12), (6, 24),
(7, 14),
(8, 1),
(9, 3), (9, 27),
(10, 5),
(11, 7),
(12, 9), (12, 30),
(13, 11),
(14, 13),
(15, 15), (15, 33),
(16, 17),
(17, 19), (17, 36),
(18, 21),
(19, 23), (19, 39),
(20, 25),
(21, 28),
(22, 31),
(23, 34), (23, 43),
(24, 37),
(25, 40),
(26, 44), (26, 45),
(27, 46),
(28, 47), (28, 48),
(29, 49),
(30, 50),
(31, 2),
(32, 4),
(33, 6), (33, 17),
(34, 8),
(35, 10), (35, 19),
(36, 12),
(37, 14),
(38, 16), (38, 21),
(39, 18),
(40, 20),
(41, 22), (41, 23),
(42, 24),
(43, 26),
(44, 28), (44, 25),
(45, 30),
(46, 32),
(47, 34), (47, 27),
(48, 36),
(49, 38), (49, 29),
(50, 40);


 -- Posting_Location Insert Statements
INSERT INTO Posting_Location (Region, State, Zip_Code, Address_Number, Street, City, Country)
VALUES
('Northeast', 'Massachusetts', '02139', 123, 'Main St', 'Cambridge', 'USA'),
('West Coast', 'California', '94016', 456, 'Market St', 'San Francisco', 'USA'),
('Midwest', 'Illinois', '60601', 789, 'Lake Shore Dr', 'Chicago', 'USA'),
('South', 'Texas', '75201', 234, 'Elm St', 'Dallas', 'USA'),
('Mountain', 'Colorado', '80202', 890, 'Pine St', 'Denver', 'USA'),
('Northeast', 'New York', '10001', 678, 'Broadway', 'New York City', 'USA'),
('West Coast', 'Washington', '98101', 345, '1st Ave', 'Seattle', 'USA'),
('Southeast', 'Florida', '33101', 910, 'Ocean Dr', 'Miami', 'USA'),
('South', 'Georgia', '30301', 567, 'Peachtree St', 'Atlanta', 'USA'),
('Southwest', 'Arizona', '85001', 432, 'Grand Ave', 'Phoenix', 'USA'),
('Midwest', 'Michigan', '48201', 876, 'Woodward Ave', 'Detroit', 'USA'),
('West Coast', 'Oregon', '97201', 321, 'Burnside St', 'Portland', 'USA'),
('Northeast', 'Pennsylvania', '19101', 654, 'Market St', 'Philadelphia', 'USA'),
('West Coast', 'California', '94101', 987, 'Van Ness Ave', 'San Francisco', 'USA'),
('Southeast', 'North Carolina', '27601', 135, 'Fayetteville St', 'Raleigh', 'USA'),
('Mountain', 'Utah', '84101', 246, 'State St', 'Salt Lake City', 'USA'),
('South', 'Alabama', '35201', 369, '20th St', 'Birmingham', 'USA'),
('Southwest', 'New Mexico', '87101', 579, 'Central Ave', 'Albuquerque', 'USA'),
('Northeast', 'Rhode Island', '02901', 258, 'Westminster St', 'Providence', 'USA'),
('West Coast', 'Nevada', '89101', 147, 'Las Vegas Blvd', 'Las Vegas', 'USA'),
('Midwest', 'Minnesota', '55401', 369, 'Hennepin Ave', 'Minneapolis', 'USA'),
('Southwest', 'Texas', '77001', 159, 'Houston St', 'Houston', 'USA'),
('South', 'Kentucky', '40501', 753, 'Main St', 'Lexington', 'USA'),
('West Coast', 'California', '95814', 486, 'Capitol Mall', 'Sacramento', 'USA'),
('Midwest', 'Ohio', '43215', 268, 'High St', 'Columbus', 'USA'),
('Southeast', 'Virginia', '23219', 197, 'Broad St', 'Richmond', 'USA'),
('Northeast', 'Maine', '04101', 874, 'Congress St', 'Portland', 'USA'),
('Midwest', 'Indiana', '46201', 659, 'Meridian St', 'Indianapolis', 'USA'),
('West Coast', 'California', '92037', 432, 'La Jolla Shores Dr', 'La Jolla', 'USA'),
('Mountain', 'Idaho', '83701', 789, 'Idaho St', 'Boise', 'USA'),
('Southwest', 'Oklahoma', '73101', 235, 'Robinson Ave', 'Oklahoma City', 'USA'),
('West Coast', 'California', '90001', 569, 'Sunset Blvd', 'Los Angeles', 'USA'),
('Midwest', 'Wisconsin', '53202', 147, 'Wisconsin Ave', 'Milwaukee', 'USA'),
('Southeast', 'Tennessee', '37201', 385, 'Broadway', 'Nashville', 'USA'),
('South', 'Arkansas', '72201', 476, 'Main St', 'Little Rock', 'USA'),
('Mountain', 'Montana', '59601', 651, 'Last Chance Gulch', 'Helena', 'USA'),
('Southwest', 'Texas', '78201', 248, 'Commerce St', 'San Antonio', 'USA'),
('Midwest', 'Kansas', '66101', 365, 'Minnesota Ave', 'Kansas City', 'USA'),
('West Coast', 'California', '92101', 843, 'Harbor Dr', 'San Diego', 'USA'),
('South', 'Louisiana', '70112', 132, 'Canal St', 'New Orleans', 'USA'),
('West Coast', 'Hawaii', '96801', 476, 'King St', 'Honolulu', 'USA'),
('Southwest', 'Nevada', '89501', 214, 'Virginia St', 'Reno', 'USA'),
('Mountain', 'Wyoming', '82001', 567, 'Capitol Ave', 'Cheyenne', 'USA'),
('Midwest', 'Nebraska', '68501', 158, 'O St', 'Lincoln', 'USA'),
('Southeast', 'South Carolina', '29201', 376, 'Gervais St', 'Columbia', 'USA'),
('Southwest', 'Texas', '76101', 142, 'Main St', 'Fort Worth', 'USA'),
('Mountain', 'Colorado', '80301', 197, 'Pearl St', 'Boulder', 'USA'),
('Southwest', 'Utah', '84701', 243, 'Cedar City Blvd', 'Cedar City', 'USA'),
('Midwest', 'North Dakota', '58102', 184, 'Broadway', 'Fargo', 'USA'),
('Southeast', 'Alabama', '36601', 349, 'Government St', 'Mobile', 'USA');


-- Posting Insert Statements
INSERT INTO Posting (Name, Company_ID, Industry, Location, Date_Start, Date_End, Filled, Minimum_GPA, Title, Description, Pay)
VALUES
('Backend Developer Intern', 1, 'Technology', 3, '2024-05-15', '2024-08-15', FALSE, 3.3, 'Internship', 'Develop and maintain backend services using Java and Spring Boot.', 65),
('Frontend Developer', 1, 'Technology', 3, '2024-06-01', '2024-08-31', FALSE, 3.0, 'Full-Time', 'Build responsive web applications using React.', 70),
('ML Engineer Intern', 2, 'AI', 5, '2024-05-20', '2024-08-20', TRUE, 3.6, 'Internship', 'Work on cutting-edge ML models and implementations.', 60),
('Data Scientist', 2, 'AI', 5, '2024-06-15', '2024-09-15', FALSE, 3.5, 'Full-Time', 'Analyze complex datasets and build predictive models.', 72),
('Software QA Intern', 3, 'Technology', 8, '2024-06-01', '2024-08-31', FALSE, 3.0, 'Internship', 'Develop and execute test plans for web applications.', 45),
('DevOps Engineer', 3, 'Technology', 8, '2024-07-01', '2024-09-30', FALSE, 3.2, 'Contract', 'Maintain CI/CD pipelines and cloud infrastructure.', 68),
('Product Manager', 4, 'Management', 12, '2024-06-01', '2024-08-31', TRUE, 3.4, 'Full-Time', 'Lead product development and strategy initiatives.', 71),
('Business Analyst Intern', 4, 'Business', 12, '2024-05-15', '2024-08-15', FALSE, 3.2, 'Internship', 'Support business analysis and reporting tasks.', 40),
('Marketing Intern', 5, 'Marketing', 15, '2024-06-01', '2024-08-31', FALSE, 3.0, 'Internship', 'Assist with digital marketing campaigns.', 35),
('Content Strategist', 5, 'Marketing', 15, '2024-06-15', '2024-09-15', FALSE, 3.1, 'Full-Time', 'Develop content strategy and manage social media presence.', 55),
('Data Engineer', 6, 'Technology', 18, '2024-05-20', '2024-08-20', FALSE, 3.4, 'Full-Time', 'Build and maintain data pipelines and warehouses.', 69),
('Cloud Engineer Intern', 6, 'Technology', 18, '2024-06-01', '2024-08-31', TRUE, 3.3, 'Internship', 'Work with AWS services and cloud architecture.', 55),
('UX Designer', 7, 'Design', 20, '2024-06-15', '2024-09-15', FALSE, 3.0, 'Full-Time', 'Create user-centered designs and prototypes.', 60),
('UI Developer Intern', 7, 'Design', 20, '2024-07-01', '2024-09-30', FALSE, 3.1, 'Internship', 'Implement responsive UI designs using modern frameworks.', 45),
('Full Stack Developer', 8, 'Technology', 22, '2024-05-15', '2024-08-15', FALSE, 3.4, 'Full-Time', 'Develop full-stack applications using MEAN stack.', 73),
('Systems Engineer Intern', 8, 'Technology', 22, '2024-06-01', '2024-08-31', TRUE, 3.2, 'Internship', 'Support system architecture and infrastructure projects.', 50),
('Finance Analyst', 9, 'Finance', 25, '2024-06-15', '2024-09-15', FALSE, 3.5, 'Full-Time', 'Perform financial analysis and reporting.', 65),
('Accounting Intern', 9, 'Finance', 25, '2024-05-20', '2024-08-20', FALSE, 3.3, 'Internship', 'Support accounting operations and reconciliations.', 40),
('HR Coordinator', 10, 'HR', 28, '2024-06-01', '2024-08-31', FALSE, 3.0, 'Full-Time', 'Manage HR operations and employee relations.', 50),
('Recruitment Intern', 10, 'HR', 28, '2024-07-01', '2024-09-30', TRUE, 3.1, 'Internship', 'Assist with recruitment and onboarding processes.', 35),
('Android Developer', 11, 'Mobile', 30, '2024-05-15', '2024-08-15', FALSE, 3.3, 'Full-Time', 'Develop Android applications using Kotlin.', 70),
('iOS Developer Intern', 11, 'Mobile', 30, '2024-06-01', '2024-08-31', FALSE, 3.2, 'Internship', 'Build iOS applications using Swift.', 55),
('Research Scientist', 12, 'Research', 32, '2024-06-15', '2024-09-15', TRUE, 3.7, 'Full-Time', 'Conduct research in computer vision and deep learning.', 75),
('Research Assistant', 12, 'Research', 32, '2024-05-20', '2024-08-20', FALSE, 3.5, 'Internship', 'Support research projects and experiments.', 45),
('Security Engineer', 13, 'Security', 35, '2024-06-01', '2024-08-31', FALSE, 3.4, 'Full-Time', 'Implement security measures and conduct audits.', 72),
('Security Analyst Intern', 13, 'Security', 35, '2024-07-01', '2024-09-30', FALSE, 3.3, 'Internship', 'Assist with security monitoring and analysis.', 50),
('Operations Manager', 14, 'Operations', 38, '2024-05-15', '2024-08-15', TRUE, 3.2, 'Full-Time', 'Manage daily operations and process improvements.', 65),
('Operations Intern', 14, 'Operations', 38, '2024-06-01', '2024-08-31', FALSE, 3.0, 'Internship', 'Support operations and logistics processes.', 40),
('Sales Representative', 15, 'Sales', 40, '2024-06-15', '2024-09-15', FALSE, 3.0, 'Full-Time', 'Drive sales growth and client relationships.', 60),
('Sales Intern', 15, 'Sales', 40, '2024-05-20', '2024-08-20', FALSE, 3.1, 'Internship', 'Support sales operations and client outreach.', 35),
('Backend Developer', 16, 'Technology', 42, '2024-06-01', '2024-08-31', TRUE, 3.4, 'Full-Time', 'Develop scalable backend services using Python.', 71),
('Frontend Developer Intern', 16, 'Technology', 42, '2024-07-01', '2024-09-30', FALSE, 3.2, 'Internship', 'Build web interfaces using Vue.js.', 50),
('Data Analyst', 17, 'Data Science', 44, '2024-05-15', '2024-08-15', FALSE, 3.3, 'Full-Time', 'Analyze business data and create reports.', 63),
('Analytics Intern', 17, 'Data Science', 44, '2024-06-01', '2024-08-31', FALSE, 3.2, 'Internship', 'Support data analysis and visualization projects.', 45),
('Product Designer', 18, 'Design', 46, '2024-06-15', '2024-09-15', TRUE, 3.1, 'Full-Time', 'Design product interfaces and user experiences.', 65),
('Design Intern', 18, 'Design', 46, '2024-05-20', '2024-08-20', FALSE, 3.0, 'Internship', 'Support product design and prototyping.', 40),
('Project Coordinator', 19, 'Management', 48, '2024-06-01', '2024-08-31', FALSE, 3.2, 'Full-Time', 'Coordinate project activities and timelines.', 55),
('Project Management Intern', 19, 'Management', 48, '2024-07-01', '2024-09-30', FALSE, 3.1, 'Internship', 'Support project planning and execution.', 40),
('Marketing Manager', 20, 'Marketing', 50, '2024-05-15', '2024-08-15', TRUE, 3.3, 'Full-Time', 'Lead marketing strategies and campaigns.', 68),
('Digital Marketing Intern', 20, 'Marketing', 50, '2024-06-01', '2024-08-31', FALSE, 3.0, 'Internship', 'Support digital marketing initiatives.', 35),
('Software Architect', 21, 'Technology', 2, '2024-06-15', '2024-09-15', FALSE, 3.6, 'Full-Time', 'Design and implement system architecture.', 74),
('Architecture Intern', 21, 'Technology', 2, '2024-05-20', '2024-08-20', FALSE, 3.4, 'Internship', 'Support architecture design and documentation.', 50),
('Business Intelligence Analyst', 22, 'Business', 4, '2024-06-01', '2024-08-31', TRUE, 3.3, 'Full-Time', 'Develop BI solutions and reports.', 65),
('BI Intern', 22, 'Business', 4, '2024-07-01', '2024-09-30', FALSE, 3.2, 'Internship', 'Support BI reporting and analysis.', 45),
('Cloud Solutions Architect', 23, 'Technology', 6, '2024-05-15', '2024-08-15', FALSE, 3.5, 'Full-Time', 'Design cloud infrastructure solutions.', 73),
('Cloud Infrastructure Intern', 23, 'Technology', 6, '2024-06-01', '2024-08-31', FALSE, 3.3, 'Internship', 'Support cloud infrastructure projects.', 55),
('Financial Analyst', 24, 'Finance', 8, '2024-06-15', '2024-09-15', TRUE, 3.4, 'Full-Time', 'Perform financial modeling and analysis.', 67),
('Finance Intern', 24, 'Finance', 8, '2024-05-20', '2024-08-20', FALSE, 3.2, 'Internship', 'Support financial analysis and reporting.', 40),
('Software Development Manager', 25, 'Technology', 10, '2024-06-01', '2024-08-31', FALSE, 3.5, 'Full-Time', 'Lead software development teams.', 75),
('Development Team Intern', 25, 'Technology', 10, '2024-07-01', '2024-09-30', FALSE, 3.3, 'Internship', 'Support development team projects.', 50),
('AI Research Scientist', 26, 'AI', 12, '2024-05-15', '2024-08-15', TRUE, 3.8, 'Full-Time', 'Conduct AI research and development.', 74),
('AI Research Intern', 26, 'AI', 12, '2024-06-01', '2024-08-31', FALSE, 3.6, 'Internship', 'Support AI research projects.', 55),
('DevOps Manager', 27, 'Technology', 14, '2024-06-15', '2024-09-15', FALSE, 3.4, 'Full-Time', 'Lead DevOps practices and teams.', 72),
('DevOps Intern', 27, 'Technology', 14, '2024-05-20', '2024-08-20', FALSE, 3.2, 'Internship', 'Support DevOps operations and automation.', 50),
('UX Research Lead', 28, 'Design', 16, '2024-06-01', '2024-08-31', TRUE, 3.3, 'Full-Time', 'Lead user research initiatives.', 68),
('UX Research Intern', 28, 'Design', 16, '2024-07-01', '2024-09-30', FALSE, 3.1, 'Internship', 'Support user research studies.', 45),
('Database Administrator', 29, 'Technology', 18, '2024-05-15', '2024-08-15', FALSE, 3.4, 'Full-Time', 'Manage database systems and performance.', 69),
('Database Intern', 29, 'Technology', 18, '2024-06-01', '2024-08-31', FALSE, 3.2, 'Internship', 'Support database administration tasks.', 45),
('Quality Assurance Lead', 30, 'Technology', 20, '2024-06-15', '2024-09-15', TRUE, 3.3, 'Full-Time', 'Lead QA processes and testing teams.', 67),
('QA Intern', 30, 'Technology', 20, '2024-05-20', '2024-08-20', FALSE, 3.1, 'Internship', 'Support QA testing and documentation.', 40),
('Cybersecurity Analyst', 13, 'Security', 35, '2024-06-01', '2024-08-31', FALSE, 3.4, 'Full-Time', 'Analyze and mitigate security threats.', 68),
('Junior Mobile Developer', 11, 'Mobile', 30, '2024-06-15', '2024-09-15', FALSE, 3.2, 'Full-Time', 'Develop and debug mobile apps for Android and iOS.', 65),
('Data Architect', 6, 'Technology', 18, '2024-05-15', '2024-08-15', TRUE, 3.5, 'Full-Time', 'Design and manage enterprise-level data models.', 73),
('Marketing Coordinator', 5, 'Marketing', 15, '2024-06-01', '2024-08-31', FALSE, 3.1, 'Full-Time', 'Coordinate marketing campaigns and events.', 60),
('SEO Specialist Intern', 5, 'Marketing', 15, '2024-05-20', '2024-08-20', FALSE, 3.2, 'Internship', 'Optimize web content for search engines.', 45),
('Software Test Engineer', 3, 'Technology', 8, '2024-06-15', '2024-09-15', TRUE, 3.4, 'Full-Time', 'Develop automated tests for software applications.', 72),
('Data Visualization Specialist', 17, 'Data Science', 44, '2024-06-01', '2024-08-31', FALSE, 3.3, 'Full-Time', 'Create interactive dashboards and data visualizations.', 65),
('Technical Writer', 4, 'Management', 12, '2024-05-15', '2024-08-15', FALSE, 3.0, 'Full-Time', 'Write technical documentation and user manuals.', 55),
('Customer Success Manager', 10, 'HR', 28, '2024-06-01', '2024-08-31', TRUE, 3.2, 'Full-Time', 'Manage client relationships and customer success strategies.', 70),
('Technical Support Specialist', 10, 'HR', 28, '2024-05-15', '2024-08-15', FALSE, 3.1, 'Internship', 'Assist with resolving technical support tickets.', 45),
('Environmental Engineer', 14, 'Environmental', 38, '2024-06-01', '2024-08-31', FALSE, 3.4, 'Full-Time', 'Design sustainable engineering solutions.', 68),
('Energy Efficiency Intern', 14, 'Environmental', 38, '2024-05-20', '2024-08-20', TRUE, 3.2, 'Internship', 'Assist in evaluating energy efficiency initiatives.', 40),
('Social Media Manager', 5, 'Marketing', 15, '2024-06-15', '2024-09-15', FALSE, 3.0, 'Full-Time', 'Plan and manage social media campaigns.', 55),
('Brand Strategist', 5, 'Marketing', 15, '2024-05-20', '2024-08-20', TRUE, 3.1, 'Full-Time', 'Develop and implement branding strategies.', 60),
('AI Ethics Researcher', 2, 'AI', 5, '2024-06-01', '2024-08-31', FALSE, 3.7, 'Full-Time', 'Research ethical implications of AI technologies.', 74),
('Cloud Migration Specialist', 6, 'Technology', 18, '2024-06-15', '2024-09-15', FALSE, 3.4, 'Full-Time', 'Assist in migrating systems to the cloud.', 72),
('Machine Learning Intern', 2, 'AI', 5, '2024-05-15', '2024-08-15', FALSE, 3.6, 'Internship', 'Develop and optimize machine learning algorithms.', 55),
('Front-End Engineer', 16, 'Technology', 42, '2024-06-01', '2024-08-31', TRUE, 3.2, 'Full-Time', 'Develop dynamic and user-friendly interfaces.', 65),
('DevOps Intern', 27, 'Technology', 14, '2024-07-01', '2024-09-30', FALSE, 3.3, 'Internship', 'Support automation and deployment pipelines.', 45),
('UX Researcher', 28, 'Design', 16, '2024-06-15', '2024-09-15', FALSE, 3.1, 'Full-Time', 'Conduct research to improve user experience.', 67),
('Game Developer Intern', 11, 'Mobile', 30, '2024-05-20', '2024-08-20', FALSE, 3.4, 'Internship', 'Develop game features for mobile platforms.', 55),
('Data Governance Analyst', 6, 'Technology', 18, '2024-05-15', '2024-08-15', FALSE, 3.5, 'Full-Time', 'Implement data governance policies.', 72),
('Financial Planner', 9, 'Finance', 25, '2024-06-15', '2024-09-15', TRUE, 3.4, 'Full-Time', 'Provide financial planning services to clients.', 68),
('Digital Advertising Intern', 5, 'Marketing', 15, '2024-05-20', '2024-08-20', FALSE, 3.2, 'Internship', 'Assist with pay-per-click advertising campaigns.', 40),
('IT Support Specialist', 10, 'HR', 28, '2024-06-01', '2024-08-31', FALSE, 3.0, 'Full-Time', 'Provide IT support to staff and clients.', 60),
('Operations Coordinator', 14, 'Operations', 38, '2024-06-15', '2024-09-15', FALSE, 3.3, 'Full-Time', 'Coordinate operational projects and logistics.', 70),
('Sustainability Intern', 14, 'Environmental', 38, '2024-05-15', '2024-08-15', TRUE, 3.1, 'Internship', 'Work on sustainability assessments and reports.', 40),
('Mobile App Designer', 11, 'Mobile', 30, '2024-06-01', '2024-08-31', FALSE, 3.3, 'Full-Time', 'Design user interfaces for mobile applications.', 68),
('Data Security Analyst', 13, 'Security', 35, '2024-05-15', '2024-08-15', TRUE, 3.5, 'Full-Time', 'Monitor and secure organizational data.', 72);



-- Alumni_Position Insert Statements
INSERT INTO Alumni_Position (Position_ID, Alumni_ID)
VALUES
(50, 20),
(46, 59),
(24, 25),
(56, 31),
(31, 59),
(36, 3),
(5, 17),
(33, 19),
(46, 18),
(51, 42),
(17, 7),
(20, 24),
(21, 22),
(4, 46),
(22, 44),
(19, 27),
(33, 13),
(41, 46),
(11, 1),
(53, 14),
(17, 45),
(32, 47),
(21, 38),
(54, 17),
(47, 3),
(9, 23),
(51, 19),
(58, 2),
(34, 31),
(34, 24),
(51, 52),
(28, 60),
(39, 42),
(12, 50),
(35, 27),
(37, 8),
(19, 3),
(37, 12),
(56, 51),
(4, 37),
(4, 18),
(1, 39),
(14, 19),
(38, 52),
(54, 2),
(22, 45),
(28, 18),
(36, 28),
(48, 58),
(30, 39),
(48, 55),
(30, 51),
(32, 9),
(37, 16),
(55, 44),
(41, 3),
(20, 13),
(40, 34),
(41, 4),
(4, 40),
(10, 38),
(32, 28),
(44, 46),
(1, 28),
(13, 37),
(4, 49),
(44, 7),
(7, 44),
(52, 10),
(29, 34),
(21, 4),
(55, 39),
(39, 9),
(12, 60),
(24, 36),
(59, 34),
(6, 2),
(54, 36),
(6, 48),
(33, 55),
(10, 4),
(34, 11),
(22, 35),
(53, 3),
(33, 43),
(6, 15),
(31, 20),
(48, 10),
(44, 29),
(38, 6),
(20, 14),
(24, 49),
(25, 49),
(53, 45),
(29, 39),
(1, 58),
(27, 35);

-- Cycle insert statements
INSERT INTO Cycle (cycle)
VALUES
('Spring'),
('Fall');

 -- Student Insert Statements
INSERT INTO Student (First_Name, Last_Name, Preferred_Name, GPA, College_ID, Grad_Year, Cycle, Advisor_ID, Eligibility, Hired, Resume_Link, Email, Phone_Number, Description)
VALUES
('Emma', 'Johnson', 'Em', 3.85, 12, 2025, 1, 25, TRUE, FALSE, 'link_to_resume_1', 'emma.johnson@gmail.com', '555-123-4567', 'Passionate about AI research.'),
('Liam', 'Smith', NULL, 3.75, 15, 2024, 2, 12, TRUE, FALSE, 'link_to_resume_2', 'liam.smith@gmail.com', '555-234-5678', 'Focused on cloud computing and cybersecurity.'),
('Sophia', 'Brown', 'Sophie', 3.90, 8, 2026, 1, 22, TRUE, FALSE, 'link_to_resume_3', 'sophia.brown@gmail.com', '555-345-6789', 'Aspiring data scientist.'),
('Noah', 'Taylor', 'Noah', 3.65, 10, 2023, 2, 18, TRUE, FALSE, 'link_to_resume_4', 'noah.taylor@gmail.com', '555-456-7890', 'Experienced in web development.'),
('Isabella', 'Davis', 'Bella', 3.80, 7, 2024, 1, 30, TRUE, FALSE, 'link_to_resume_5', 'isabella.davis@gmail.com', '555-567-8901', 'Graphic design and marketing enthusiast.'),
('Oliver', 'Jones', 'Ollie', 3.70, 5, 2025, 2, 20, TRUE, FALSE, 'link_to_resume_6', 'oliver.jones@gmail.com', '555-678-9012', 'Interest in financial modeling and analytics.'),
('Mia', 'Wilson', 'Mimi', 3.95, 13, 2026, 1, 35, TRUE, FALSE, 'link_to_resume_7', 'mia.wilson@gmail.com', '555-789-0123', 'Excited to work in renewable energy projects.'),
('Lucas', 'Garcia', NULL, 3.60, 18, 2025, 2, 17, TRUE, FALSE, 'link_to_resume_8', 'lucas.garcia@gmail.com', '555-890-1234', 'Software engineering focus with cloud expertise.'),
('Ava', 'Martinez', 'Avy', 3.85, 14, 2024, 1, 40, TRUE, FALSE, 'link_to_resume_9', 'ava.martinez@gmail.com', '555-901-2345', 'Marketing and customer engagement specialist.'),
('Ethan', 'Rodriguez', 'Ethan', 3.75, 9, 2026, 2, 19, TRUE, FALSE, 'link_to_resume_10', 'ethan.rodriguez@gmail.com', '555-012-3456', 'AI and robotics enthusiast.'),
('Emily', 'Lopez', 'Emmy', 3.80, 21, 2025, 1, 29, TRUE, FALSE, 'link_to_resume_11', 'emily.lopez@gmail.com', '555-123-4567', 'Graphic designer and creative thinker.'),
('Benjamin', 'Thomas', NULL, 3.95, 19, 2024, 2, 28, TRUE, FALSE, 'link_to_resume_12', 'benjamin.thomas@gmail.com', '555-234-5678', 'Financial analyst with passion for data.'),
('Ella', 'Anderson', 'Ellie', 3.85, 22, 2025, 1, 36, TRUE, FALSE, 'link_to_resume_13', 'ella.anderson@gmail.com', '555-345-6789', 'Experienced in project management and operations.'),
('James', 'Hernandez', 'Jimmy', 3.65, 4, 2024, 2, 27, TRUE, FALSE, 'link_to_resume_14', 'james.hernandez@gmail.com', '555-456-7890', 'Blockchain and fintech enthusiast.'),
('Lily', 'Moore', 'Lil', 3.90, 6, 2026, 1, 24, TRUE, FALSE, 'link_to_resume_15', 'lily.moore@gmail.com', '555-567-8901', 'Passionate about healthcare technology.'),
('Matthew', 'Martinez', 'Matt', 3.70, 11, 2023, 2, 23, TRUE, FALSE, 'link_to_resume_16', 'matthew.martinez@gmail.com', '555-678-9012', 'Focus on AI in education and training systems.'),
('Grace', 'Young', 'Gracie', 3.75, 16, 2024, 1, 15, TRUE, FALSE, 'link_to_resume_17', 'grace.young@gmail.com', '555-789-0123', 'Experienced in event planning and management.'),
('Jack', 'White', 'Jacky', 3.80, 17, 2026, 2, 45, TRUE, FALSE, 'link_to_resume_18', 'jack.white@gmail.com', '555-890-1234', 'Sales and CRM expert.'),
('Harper', 'Lee', 'Harp', 3.65, 20, 2025, 1, 44, TRUE, FALSE, 'link_to_resume_19', 'harper.lee@gmail.com', '555-901-2345', 'Excited to work in environmental engineering.'),
('Alexander', 'Harris', 'Alex', 3.85, 3, 2024, 2, 11, TRUE, FALSE, 'link_to_resume_20', 'alexander.harris@gmail.com', '555-012-3456', 'Business operations and strategic planning.'),
('Zoey', 'Clark', 'Zoe', 3.90, 2, 2026, 1, 33, TRUE, FALSE, 'link_to_resume_21', 'zoey.clark@gmail.com', '555-234-5678', 'Expert in social media marketing and branding.'),
('Daniel', 'Hall', 'Dan', 3.75, 5, 2025, 2, 38, TRUE, FALSE, 'link_to_resume_22', 'daniel.hall@gmail.com', '555-345-6789', 'Focused on renewable energy solutions.'),
('Scarlett', 'Brown', 'Scar', 3.80, 8, 2024, 1, 12, TRUE, FALSE, 'link_to_resume_23', 'scarlett.brown@gmail.com', '555-456-7890', 'Graphic design and creative storytelling.'),
('Henry', 'Adams', NULL, 3.95, 10, 2023, 2, 31, TRUE, FALSE, 'link_to_resume_24', 'henry.adams@gmail.com', '555-567-8901', 'Data visualization and analytics enthusiast.'),
('Victoria', 'Sanchez', 'Vicky', 3.65, 14, 2026, 1, 21, TRUE, FALSE, 'link_to_resume_25', 'victoria.sanchez@gmail.com', '555-678-9012', 'Excited to contribute to AI research.'),
('Owen', 'Roberts', NULL, 3.70, 6, 2024, 2, 25, TRUE, FALSE, 'link_to_resume_26', 'owen.roberts@gmail.com', '555-789-0123', 'Focused on machine learning applications in robotics.'),
('Ella', 'Turner', 'Ellie', 3.85, 11, 2025, 1, 14, TRUE, TRUE, 'link_to_resume_27', 'ella.turner@gmail.com', '555-890-1234', 'Marketing and customer engagement specialist.'),
('Jackson', 'Phillips', 'Jack', 3.80, 13, 2026, 2, 9, TRUE, FALSE, 'link_to_resume_28', 'jackson.phillips@gmail.com', '555-901-2345', 'Interested in cloud computing and DevOps.'),
('Zoe', 'Campbell', 'Zoe', 3.75, 4, 2024, 1, 42, TRUE, FALSE, 'link_to_resume_29', 'zoe.campbell@gmail.com', '555-012-3456', 'Experienced in video editing and content creation.'),
('Logan', 'Evans', 'Log', 3.70, 7, 2025, 2, 28, TRUE, FALSE, 'link_to_resume_30', 'logan.evans@gmail.com', '555-123-4567', 'Software engineer with a focus on AI systems.'),
('Leah', 'Murphy', 'Lea', 3.85, 9, 2026, 1, 40, TRUE, FALSE, 'link_to_resume_31', 'leah.murphy@gmail.com', '555-234-5678', 'Event planner with an eye for detail.'),
('Liam', 'Stewart', 'Liam', 3.65, 20, 2023, 2, 13, TRUE, FALSE, 'link_to_resume_32', 'liam.stewart@gmail.com', '555-345-6789', 'Excited to work in environmental engineering.'),
('Samantha', 'Morris', 'Sam', 3.90, 22, 2024, 1, 34, TRUE, FALSE, 'link_to_resume_33', 'samantha.morris@gmail.com', '555-456-7890', 'Marketing and content strategy specialist.'),
('Ethan', 'Wright', 'Ethan', 3.75, 6, 2026, 2, 29, TRUE, FALSE, 'link_to_resume_34', 'ethan.wright@gmail.com', '555-567-8901', 'Interested in cybersecurity and data privacy.'),
('Olivia', 'King', 'Liv', 3.85, 15, 2025, 1, 16, TRUE, FALSE, 'link_to_resume_35', 'olivia.king@gmail.com', '555-678-9012', 'Healthcare and biotech enthusiast.'),
('Andrew', 'Parker', 'Andy', 3.80, 11, 2024, 2, 7, TRUE, FALSE, 'link_to_resume_36', 'andrew.parker@gmail.com', '555-789-0123', 'Software engineering with a focus on SaaS.'),
('Avery', 'Collins', 'Av', 3.95, 3, 2023, 1, 5, TRUE, FALSE, 'link_to_resume_37', 'avery.collins@gmail.com', '555-890-1234', 'Passionate about education technology.'),
('Chloe', 'Morgan', 'Chlo', 3.85, 16, 2025, 2, 18, TRUE, FALSE, 'link_to_resume_38', 'chloe.morgan@gmail.com', '555-901-2345', 'Financial analyst with passion for data insights.'),
('Nathan', 'Green', 'Nate', 3.70, 10, 2026, 1, 26, TRUE, FALSE, 'link_to_resume_39', 'nathan.green@gmail.com', '555-012-3456', 'Data scientist focused on AI applications.'),
('Lila', 'Perez', NULL, 3.65, 8, 2024, 2, 43, TRUE, FALSE, 'link_to_resume_40', 'lila.perez@gmail.com', '555-123-4567', 'Content marketing and storytelling specialist.'),
('Gabriel', 'Diaz', 'Gabe', 3.90, 5, 2023, 1, 37, TRUE, FALSE, 'link_to_resume_41', 'gabriel.diaz@gmail.com', '555-234-5678', 'AI and machine learning researcher.'),
('Ella', 'Ramirez', 'Ellie', 3.85, 9, 2025, 2, 6, TRUE, FALSE, 'link_to_resume_42', 'ella.ramirez@gmail.com', '555-345-6789', 'Web development and front-end design expert.'),
('Zoe', 'Martinez', 'Zoe', 3.80, 12, 2024, 1, 15, TRUE, FALSE, 'link_to_resume_43', 'zoe.martinez@gmail.com', '555-456-7890', 'Graphic design and digital media enthusiast.'),
('Aiden', 'Lee', 'Aid', 3.65, 18, 2026, 2, 48, TRUE, FALSE, 'link_to_resume_44', 'aiden.lee@gmail.com', '555-567-8901', 'Focused on DevOps and cloud infrastructure.'),
('Madison', 'Harris', 'Maddie', 3.70, 7, 2023, 1, 39, TRUE, FALSE, 'link_to_resume_45', 'madison.harris@gmail.com', '555-678-9012', 'Software engineering for healthcare systems.'),
('Logan', 'Clark', 'Logan', 3.85, 4, 2024, 2, 25, TRUE, FALSE, 'link_to_resume_46', 'logan.clark@gmail.com', '555-789-0123', 'Blockchain technology and security specialist.'),
('Nora', 'Thompson', 'Nor', 3.90, 2, 2025, 1, 20, TRUE, FALSE, 'link_to_resume_47', 'nora.thompson@gmail.com', '555-890-1234', 'Environmental engineering and green solutions.'),
('Sophia', 'Walker', 'Sophie', 3.65, 14, 2026, 2, 11, TRUE, FALSE, 'link_to_resume_48', 'sophia.walker@gmail.com', '555-901-2345', 'Project management and operations specialist.'),
('Elliot', 'Moore', NULL, 3.70, 20, 2024, 1, 9, TRUE, FALSE, 'link_to_resume_49', 'elliot.moore@gmail.com', '555-012-3456', 'AI and robotics enthusiast.'),
('Violet', 'Brooks', 'Vi', 3.85, 19, 2025, 2, 13, TRUE, FALSE, 'link_to_resume_50', 'violet.brooks@gmail.com', '555-123-4567', 'Marketing analytics and strategy expert.');


 -- Major Insert Statements
INSERT INTO Student_Majors (Student_ID, FieldOfStudy_ID) VALUES
(1, 1), (1, 15),
(2, 3),
(3, 7), (3, 12),
(4, 2),
(5, 8), (5, 22),
(6, 4),
(7, 9),
(8, 5), (8, 18),
(9, 10),
(10, 6),
(11, 11), (11, 25),
(12, 13),
(13, 14), (13, 28),
(14, 16),
(15, 17), (15, 30),
(16, 19),
(17, 20),
(18, 21), (18, 35),
(19, 23),
(20, 24),
(21, 26),
(22, 27), (22, 38),
(23, 29),
(24, 31),
(25, 32), (25, 40),
(26, 33),
(27, 34),
(28, 36),
(29, 37), (29, 42),
(30, 39),
(31, 1),
(32, 3), (32, 15),
(33, 5),
(34, 7),
(35, 9), (35, 22),
(36, 11),
(37, 13), (37, 25),
(38, 2),
(39, 4),
(40, 6), (40, 28),
(41, 8),
(42, 10),
(43, 12), (43, 30),
(44, 14),
(45, 16),
(46, 18), (46, 33),
(47, 20),
(48, 24), (48, 35),
(49, 26),
(50, 28);

-- Minor Table Entries
INSERT INTO Student_Minors (Student_ID, FieldOfStudy_ID) VALUES
(1, 2),
(2, 4), (2, 16),
(3, 6),
(4, 8), (4, 20),
(5, 10),
(6, 12), (6, 24),
(7, 14),
(8, 1),
(9, 3), (9, 27),
(10, 5),
(11, 7),
(12, 9), (12, 30),
(13, 11),
(14, 13),
(15, 15), (15, 33),
(16, 17),
(17, 19), (17, 36),
(18, 21),
(19, 23), (19, 39),
(20, 25),
(21, 28),
(22, 31),
(23, 34), (23, 43),
(24, 37),
(25, 40),
(26, 44), (26, 45),
(27, 46),
(28, 47), (28, 48),
(29, 49),
(30, 50),
(31, 2),
(32, 4),
(33, 6), (33, 17),
(34, 8),
(35, 10), (35, 19),
(36, 12),
(37, 14),
(38, 16), (38, 21),
(39, 18),
(40, 20),
(41, 22), (41, 23),
(42, 24),
(43, 26),
(44, 28), (44, 25),
(45, 30),
(46, 32),
(47, 34), (47, 27),
(48, 36),
(49, 38), (49, 29),
(50, 40);


-- Posting_Skills Insert Statements
INSERT INTO Posting_Skills (Position_ID, Skill_ID)
VALUES
-- Backend Developer Intern (Python, Cloud Computing, Programming)
(1, 1), (1, 24), (1, 22),

-- Frontend Developer (JavaScript, Web Development, UX Design)
(2, 50), (2, 9), (2, 13),

-- ML Engineer Intern (Python, Machine Learning, AI)
(3, 1), (3, 4), (3, 29),

-- Data Scientist (Data Analysis, Python for Data Science, Statistics)
(4, 3), (4, 37), (4, 40),

-- Software QA Intern (Programming, Testing skills)
(5, 22), (5, 9), (5, 24),

-- DevOps Engineer (Cloud Computing, Linux Administration, Programming)
(6, 24), (6, 51), (6, 22),

-- Product Manager (Product Management, Leadership, Strategic Planning)
(7, 56), (7, 2), (7, 41),

-- Business Analyst Intern (Data Analysis, Financial Analysis, Business Development)
(8, 3), (8, 17), (8, 48),

-- Marketing Intern (Digital Marketing, Social Media Marketing, Content Writing)
(9, 8), (9, 16), (9, 14),

-- Content Strategist (Content Writing, SEO, Digital Marketing)
(10, 14), (10, 7), (10, 8),

-- Data Engineer (Python, SQL, Cloud Computing)
(11, 1), (11, 36), (11, 24),

-- Cloud Engineer Intern (Cloud Computing, Cloud Architecture, Linux Administration)
(12, 24), (12, 52), (12, 51),

-- UX Designer (UX Design, Graphic Design, Research)
(13, 13), (13, 12), (13, 26),

-- UI Developer Intern (Web Development, JavaScript, UX Design)
(14, 9), (14, 50), (14, 13),

-- Full Stack Developer (Programming, Web Development, JavaScript)
(15, 22), (15, 9), (15, 50),

-- Systems Engineer Intern (Cloud Computing, Linux Administration, Programming)
(16, 24), (16, 51), (16, 22),

-- Finance Analyst (Financial Analysis, Data Analysis, Financial Reporting)
(17, 17), (17, 3), (17, 35),

-- Accounting Intern (Financial Analysis, Financial Reporting)
(18, 17), (18, 35), (18, 3),

-- HR Coordinator (Human Resources, Leadership, Team Management)
(19, 39), (19, 2), (19, 19),

-- Recruitment Intern (Human Resources, Communication skills)
(20, 39), (20, 27), (20, 19),

-- Android Developer (Mobile Development, Programming, UI/UX)
(21, 34), (21, 22), (21, 13),

-- iOS Developer Intern (Mobile Development, Programming)
(22, 34), (22, 22), (22, 13),

-- Research Scientist (AI, Machine Learning, Research)
(23, 29), (23, 4), (23, 26),

-- Research Assistant (Research, Data Analysis, Statistics)
(24, 26), (24, 3), (24, 40),

-- Security Engineer (Cybersecurity, Cloud Computing, Programming)
(25, 25), (25, 24), (25, 22),

-- Security Analyst Intern (Cybersecurity, Data Analysis)
(26, 25), (26, 3), (26, 24),

-- Operations Manager (Operations Management, Leadership, Strategic Planning)
(27, 28), (27, 2), (27, 41),

-- Operations Intern (Operations Management, Time Management)
(28, 28), (28, 18), (28, 19),

-- Sales Representative (Customer Service, Negotiation, Sales)
(29, 15), (29, 11), (29, 47),

-- Sales Intern (Customer Service, Communication, Sales)
(30, 15), (30, 27), (30, 47),

-- Backend Developer (Programming, Cloud Computing, Python)
(31, 22), (31, 24), (31, 1),

-- Frontend Developer Intern (JavaScript, Web Development, UX Design)
(32, 50), (32, 9), (32, 13),

-- Data Analyst (Data Analysis, Python for Data Science, Statistics)
(33, 3), (33, 37), (33, 40),

-- Analytics Intern (Data Analysis, Python, Statistics)
(34, 3), (34, 1), (34, 40),

-- Product Designer (UX Design, Graphic Design, Research)
(35, 13), (35, 12), (35, 26),

-- Design Intern (UX Design, Graphic Design)
(36, 13), (36, 12), (36, 27),

-- Project Coordinator (Project Management, Time Management, Team Management)
(37, 6), (37, 18), (37, 19),

-- Project Management Intern (Project Management, Time Management)
(38, 6), (38, 18), (38, 27),

-- Marketing Manager (Marketing Strategy, Digital Marketing, Leadership)
(39, 5), (39, 8), (39, 2),

-- Digital Marketing Intern (Digital Marketing, Social Media Marketing)
(40, 8), (40, 16), (40, 14),

-- Software Architect (Cloud Architecture, Programming, Strategic Planning)
(41, 52), (41, 22), (41, 41),

-- Architecture Intern (Cloud Architecture, Programming)
(42, 52), (42, 22), (42, 24),

-- Business Intelligence Analyst (Data Analysis, SQL, Business Development)
(43, 3), (43, 36), (43, 48),

-- BI Intern (Data Analysis, SQL)
(44, 3), (44, 36), (44, 40),

-- Cloud Solutions Architect (Cloud Architecture, Cloud Computing, Linux Administration)
(45, 52), (45, 24), (45, 51),

-- Cloud Infrastructure Intern (Cloud Computing, Linux Administration)
(46, 24), (46, 51), (46, 22),

-- Financial Analyst (Financial Analysis, Data Analysis, Financial Reporting)
(47, 17), (47, 3), (47, 35),

-- Finance Intern (Financial Analysis, Data Analysis)
(48, 17), (48, 3), (48, 35),

-- Software Development Manager (Programming, Leadership, Team Management)
(49, 22), (49, 2), (49, 19),

-- Development Team Intern (Programming, Team Management)
(50, 22), (50, 19), (50, 18);

-- Student_Skills Insert Statements
-- Student Skills Insert Statements based on descriptions
INSERT INTO Student_Skills (Student_ID, Skill_ID) VALUES
-- Emma Johnson - AI research
(1, 1),  -- Computer Science
(1, 50), -- Artificial Intelligence
(1, 18), -- Data Science

-- Liam Smith - cloud computing and cybersecurity
(2, 1),  -- Computer Science
(2, 19), -- Cybersecurity
(2, 18), -- Data Science

-- Sophia Brown - data scientist
(3, 18), -- Data Science
(3, 1),  -- Computer Science
(3, 2),  -- Mathematics

-- Noah Taylor - web development
(4, 1),  -- Computer Science
(4, 24), -- Graphic Design

-- Isabella Davis - graphic design and marketing
(5, 24), -- Graphic Design
(5, 20), -- Marketing
(5, 23), -- Public Relations

-- Oliver Jones - financial modeling and analytics
(6, 22), -- Finance
(6, 18), -- Data Science
(6, 2),  -- Mathematics

-- Mia Wilson - renewable energy
(7, 17), -- Environmental Science
(7, 40), -- Environmental Engineering
(7, 39), -- Sustainability Studies

-- Lucas Garcia - software engineering with cloud
(8, 1),  -- Computer Science
(8, 19), -- Cybersecurity

-- Ava Martinez - marketing and customer engagement
(9, 20), -- Marketing
(9, 23), -- Public Relations

-- Ethan Rodriguez - AI and robotics
(10, 50), -- Artificial Intelligence
(10, 1),  -- Computer Science
(10, 43), -- Mechanical Engineering

-- Continue for remaining students...
(11, 24), -- Emily Lopez - Graphic Design
(11, 20), -- Marketing

(12, 22), -- Benjamin Thomas - Finance
(12, 18), -- Data Science

(13, 48), -- Ella Anderson - Supply Chain Management
(13, 3),  -- Business Administration

(14, 22), -- James Hernandez - Fintech
(14, 1),  -- Computer Science

(15, 27), -- Lily Moore - Healthcare Technology
(15, 42), -- Biomedical Engineering

-- And so on for all 50 students...
(16, 50), -- Matthew Martinez - AI in education
(16, 28), -- Education

(17, 47), -- Grace Young - Event Planning
(17, 3),  -- Business Administration

(18, 20), -- Jack White - Sales and CRM
(18, 3),  -- Business Administration

(19, 40), -- Harper Lee - Environmental Engineering
(19, 17), -- Environmental Science

(20, 3),  -- Alexander Harris - Business Operations
(20, 38), -- Public Policy

-- Continue with remaining students...
(21, 20), -- Zoey Clark - Social Media Marketing
(21, 23), -- Public Relations

(22, 40), -- Daniel Hall - Renewable Energy
(22, 39), -- Sustainability Studies

(23, 24), -- Scarlett Brown - Graphic Design
(23, 20), -- Marketing

(24, 18), -- Henry Adams - Data Analytics
(24, 2),  -- Mathematics

(25, 50), -- Victoria Sanchez - AI Research
(25, 1),  -- Computer Science

-- And the rest of the students...
(26, 50), -- Owen Roberts - Machine Learning
(26, 43), -- Mechanical Engineering

(27, 20), -- Ella Turner - Marketing
(27, 23), -- Public Relations

(28, 1),  -- Jackson Phillips - Cloud Computing
(28, 19), -- Cybersecurity

(29, 24), -- Zoe Campbell - Video Editing
(29, 34), -- Film Studies

(30, 1),  -- Logan Evans - Software Engineering
(30, 50), -- AI Systems

(31, 47), -- Leah Murphy - Event Planning
(31, 3),  -- Business Administration

(32, 40), -- Liam Stewart - Environmental Engineering
(32, 17), -- Environmental Science

(33, 20), -- Samantha Morris - Marketing
(33, 23), -- Public Relations

(34, 19), -- Ethan Wright - Cybersecurity
(34, 1),  -- Computer Science

(35, 27), -- Olivia King - Healthcare
(35, 42), -- Biomedical Engineering

(36, 1),  -- Andrew Parker - Software Engineering
(36, 18), -- Data Science

(37, 28), -- Avery Collins - Education Technology
(37, 1),  -- Computer Science

(38, 22), -- Chloe Morgan - Financial Analysis
(38, 18), -- Data Science

(39, 18), -- Nathan Green - Data Science
(39, 50), -- AI Applications

(40, 20), -- Lila Perez - Content Marketing
(40, 23), -- Public Relations

(41, 50), -- Gabriel Diaz - AI Research
(41, 1),  -- Computer Science

(42, 1),  -- Ella Ramirez - Web Development
(42, 24), -- Graphic Design

(43, 24), -- Zoe Martinez - Graphic Design
(43, 20), -- Marketing

(44, 1),  -- Aiden Lee - DevOps
(44, 19), -- Cybersecurity

(45, 1),  -- Madison Harris - Software Engineering
(45, 27), -- Health Sciences

(46, 1),  -- Logan Clark - Blockchain
(46, 19), -- Cybersecurity

(47, 40), -- Nora Thompson - Environmental Engineering
(47, 39), -- Sustainability Studies

(48, 48), -- Sophia Walker - Project Management
(48, 3),  -- Business Administration

(49, 50), -- Elliot Moore - AI and Robotics
(49, 43), -- Mechanical Engineering

(50, 20), -- Violet Brooks - Marketing Analytics
(50, 18)  -- Data Science
;

-- Status INSERT statements
INSERT INTO Status (Status_Description)
VALUES
('Under Review'),
('Rejected'),
('Accepted');

INSERT INTO Application (Student_ID, Position_ID, submittedDate, Status_ID)
VALUES
-- AI/ML focused students
(1, 3, '2024-02-15', 1),    -- Emma Johnson -> ML Engineer Intern
(41, 52, '2024-02-16', 1),  -- Gabriel Diaz -> AI Research Scientist
(49, 51, '2024-02-15', 1),  -- Elliot Moore -> AI Research Intern
(25, 3, '2024-02-17', 2),   -- Victoria Sanchez -> ML Engineer Intern
(10, 52, '2024-02-18', 1),  -- Ethan Rodriguez -> AI Research Scientist

-- Software Development focused
(8, 1, '2024-02-15', 1),    -- Lucas Garcia -> Backend Developer Intern
(30, 31, '2024-02-16', 1),  -- Logan Evans -> Backend Developer
(4, 2, '2024-02-17', 1),    -- Noah Taylor -> Frontend Developer
(42, 14, '2024-02-18', 1),  -- Ella Ramirez -> UI Developer Intern
(36, 15, '2024-02-19', 1),  -- Andrew Parker -> Full Stack Developer

-- Data Science/Analytics
(3, 4, '2024-02-15', 1),    -- Sophia Brown -> Data Scientist
(39, 33, '2024-02-16', 1),  -- Nathan Green -> Data Analyst
(24, 34, '2024-02-17', 1),  -- Henry Adams -> Analytics Intern
(12, 4, '2024-02-18', 2),   -- Benjamin Thomas -> Data Scientist
(38, 33, '2024-02-19', 1),  -- Chloe Morgan -> Data Analyst

-- Cybersecurity/DevOps
(2, 6, '2024-02-15', 1),    -- Liam Smith -> DevOps Engineer
(34, 25, '2024-02-16', 1),  -- Ethan Wright -> Security Engineer
(44, 54, '2024-02-17', 1),  -- Aiden Lee -> DevOps Manager
(46, 26, '2024-02-18', 1),  -- Logan Clark -> Security Analyst Intern
(28, 12, '2024-02-19', 1),  -- Jackson Phillips -> Cloud Engineer Intern

-- Marketing/Content
(5, 9, '2024-02-15', 1),    -- Isabella Davis -> Marketing Intern
(21, 10, '2024-02-16', 1),  -- Zoey Clark -> Content Strategist
(40, 40, '2024-02-17', 1),  -- Lila Perez -> Digital Marketing Intern
(27, 39, '2024-02-18', 1),  -- Ella Turner -> Marketing Manager
(33, 9, '2024-02-19', 1),   -- Samantha Morris -> Marketing Intern

-- Design/UX
(11, 13, '2024-02-15', 1),  -- Emily Lopez -> UX Designer
(23, 36, '2024-02-16', 1),  -- Scarlett Brown -> Product Designer
(43, 14, '2024-02-17', 1),  -- Zoe Martinez -> UI Developer Intern
(29, 56, '2024-02-18', 1),  -- Zoe Campbell -> UX Research Intern
(35, 13, '2024-02-19', 1),  -- Olivia King -> UX Designer

-- Business/Finance
(6, 17, '2024-02-15', 1),   -- Oliver Jones -> Finance Analyst
(17, 8, '2024-02-16', 1),   -- Grace Young -> Business Analyst Intern
(18, 29, '2024-02-17', 1),  -- Jack White -> Sales Representative
(31, 28, '2024-02-18', 2),  -- Leah Murphy -> Operations Intern
(48, 37, '2024-02-19', 1),  -- Sophia Walker -> Project Coordinator

-- Environmental/Sustainability
(7, 11, '2024-02-15', 1),   -- Mia Wilson -> Data Engineer
(19, 28, '2024-02-16', 1),  -- Harper Lee -> Operations Intern
(22, 11, '2024-02-17', 1),  -- Daniel Hall -> Data Engineer
(32, 28, '2024-02-18', 1),  -- Liam Stewart -> Operations Intern
(47, 37, '2024-02-19', 1),  -- Nora Thompson -> Project Coordinator

-- Technology/Engineering
(45, 1, '2024-02-15', 1),   -- Madison Harris -> Backend Developer Intern
(26, 16, '2024-02-16', 1),  -- Owen Roberts -> Systems Engineer Intern
(37, 5, '2024-02-17', 1),   -- Avery Collins -> Software QA Intern
(14, 31, '2024-02-18', 1),  -- James Hernandez -> Backend Developer
(16, 3, '2024-02-19', 1),   -- Matthew Martinez -> ML Engineer Intern

-- Research/Academic
(15, 24, '2024-02-15', 1),  -- Lily Moore -> Research Assistant
(20, 43, '2024-02-16', 1),  -- Alexander Harris -> BI Intern
(13, 37, '2024-02-17', 1),  -- Ella Anderson -> Project Coordinator
(9, 10, '2024-02-18', 1),   -- Ava Martinez -> Content Strategist
(50, 33, '2024-02-19', 1);  -- Violet Brooks -> Data Analyst


-- Question Insert Statements
INSERT INTO Question (Question, Answer, Application_ID)
VALUES
-- AI/ML focused students
('Why do you want this internship?', 'To gain real-world experience in machine learning.', 1),
('What is your greatest strength?', 'Critical thinking and perseverance.', 1),
('How do you stay updated with AI advancements?', 'I follow AI research journals and attend webinars.', 2),
('What excites you about AI research?', 'The potential to solve complex real-world problems.', 2),
('What was your favorite ML project?', 'Building a recommendation system using collaborative filtering.', 3),

-- Software Development focused
('Why do you want this position?', 'To deepen my backend development skills.', 6),
('What is your favorite programming language and why?', 'Java, because of its versatility and robust libraries.', 6),
('Describe a time you optimized a system.', 'Improved API response times by implementing caching.', 7),
('What motivates you about frontend development?', 'Creating user-friendly interfaces that improve accessibility.', 8),
('Describe a UI/UX improvement you made.', 'Redesigned a dashboard for better usability.', 9),

-- Data Science/Analytics
('How do you approach data cleaning?', 'By systematically identifying outliers and missing values.', 11),
('What is your experience with predictive modeling?', 'Developed predictive models for sales forecasting.', 12),
('How do you ensure the accuracy of your analysis?', 'By cross-validating results and using multiple datasets.', 13),
('What excites you about analytics?', 'Uncovering actionable insights from data.', 14),
('Describe a challenging dataset you worked with.', 'Cleaned and analyzed unstructured text data for sentiment analysis.', 15),

-- Cybersecurity/DevOps
('What interests you about DevOps?', 'Streamlining software development and deployment.', 16),
('Describe a security issue you solved.', 'Identified and patched a vulnerability in a web application.', 17),
('What is your experience with CI/CD?', 'Built and maintained CI/CD pipelines using Jenkins.', 18),
('Why is cybersecurity important to you?', 'To protect sensitive data and prevent breaches.', 19),
('What is your experience with cloud security?', 'Implemented security protocols for AWS deployments.', 20),

-- Marketing/Content
('Why are you passionate about marketing?', 'Connecting with audiences and creating impactful campaigns.', 21),
('What is your favorite digital marketing tool?', 'Google Analytics for its insightful data visualizations.', 22),
('How do you create effective social media campaigns?', 'By analyzing audience engagement and trends.', 23),
('Describe a successful content strategy you implemented.', 'Developed a blog series that increased traffic by 30%.', 24),
('What interests you about digital marketing?', 'The combination of creativity and analytics.', 25),

-- Design/UX
('What excites you about UX design?', 'Improving the user experience through thoughtful design.', 26),
('Describe your design process.', 'Empathize, define, ideate, prototype, and test.', 27),
('How do you handle feedback on your designs?', 'By embracing it as an opportunity for improvement.', 28),
('What is your favorite design project?', 'Creating a mobile app for budget tracking.', 29),
('How do you ensure accessibility in design?', 'Following WCAG guidelines and conducting user testing.', 30),

-- Business/Finance
('What interests you about finance?', 'Helping organizations make informed financial decisions.', 31),
('How do you manage competing priorities?', 'By prioritizing tasks based on impact and deadlines.', 32),
('Describe a financial analysis you performed.', 'Evaluated profitability and cost structure for a project.', 33),
('Why do you want this position?', 'To gain hands-on experience in financial modeling.', 34),
('What motivates you about business analysis?', 'Uncovering insights to drive strategic decisions.', 35),

-- Environmental/Sustainability
('Why do you care about sustainability?', 'To create a better future for the planet.', 36),
('Describe a sustainability project you worked on.', 'Designed a system for reducing water usage in agriculture.', 37),
('What is your experience with environmental engineering?', 'Developed renewable energy solutions for small businesses.', 38),
('How do you measure the success of sustainability initiatives?', 'Using KPIs like energy savings and waste reduction.', 39),
('What motivates you about sustainability?', 'Making a tangible impact on environmental health.', 40),

-- Technology/Engineering
('Why do you enjoy backend development?', 'The challenge of building scalable systems.', 41),
('What is your experience with API development?', 'Built RESTful APIs for a financial application.', 42),
('Describe a technical challenge you overcame.', 'Optimized database queries to reduce load times.', 43),
('What excites you about engineering?', 'Solving complex problems through innovative solutions.', 44),
('How do you stay updated with technology trends?', 'Following tech blogs and participating in hackathons.', 45),

-- Research/Academic
('Why do you enjoy research?', 'The opportunity to explore and discover new knowledge.', 46),
('What is your favorite area of study?', 'Machine learning and its applications.', 47),
('Describe a research project you led.', 'Developed a novel algorithm for image recognition.', 48),
('What motivates you about academic research?', 'Contributing to the advancement of knowledge.', 49),
('What do you enjoy about being a research assistant?', 'Learning from experts and contributing to meaningful projects.', 50);


-- Ticket Insert Statements
INSERT INTO Ticket (Reporter_ID, Message, Completed)
VALUES
(1, 'Error in application submission.', FALSE),
(2, 'Duplicate entries in the alumni table.', TRUE),
(3, 'Skill data not populating correctly.', FALSE),
(4, 'Incorrect data in student GPA field.', TRUE),
(5, 'Resume link is broken for some students.', FALSE),
(6, 'Advisor information not linked properly.', TRUE),
(7, 'Missing values in posting location.', FALSE),
(8, 'Application status ID mismatch.', TRUE),
(9, 'Issue with the frontend rendering of postings.', FALSE),
(10, 'Database connection timeout on login.', TRUE),
(11, 'Bug in the search functionality for postings.', FALSE),
(12, 'Duplicate values in major and minor tables.', TRUE),
(13, 'Error during status update for applications.', FALSE),
(14, 'Advisor cannot assign students.', TRUE),
(15, 'Internship pay field accepts negative values.', FALSE),
(16, 'Pagination not working in student list view.', TRUE),
(17, 'Broken links in the alumni section.', FALSE),
(18, 'Incorrect data formatting in posting descriptions.', TRUE),
(19, 'Error during file upload for student resumes.', FALSE),
(20, 'Bug in the reporting system for tickets.', TRUE),
(21, 'Incomplete data migration for skills.', FALSE),
(22, 'Search filters in postings not functioning.', TRUE),
(23, 'Advisor IDs not being assigned correctly.', FALSE),
(24, 'Major table schema mismatch.', TRUE),
(25, 'Notification system not sending updates.', FALSE),
(26, 'Incorrect SQL constraints on applications.', TRUE),
(27, 'Field validation missing for GPA inputs.', FALSE),
(28, 'Missing dropdown options for application statuses.', TRUE),
(29, 'Broken layout on mobile devices.', FALSE),
(30, 'Advisor college IDs not displaying.', TRUE),
(31, 'Frontend crashes during student application.', FALSE),
(32, 'Skill description field accepts invalid characters.', TRUE),
(33, 'Duplicate entries allowed in alumni positions.', FALSE),
(34, 'Error in the calculation of internship durations.', TRUE),
(35, 'Auto-complete in posting search is too slow.', FALSE),
(36, 'Application status updates are not saving.', TRUE),
(37, 'Broken links in the advisor profiles.', FALSE),
(38, 'Error in displaying applicant details.', TRUE),
(39, 'Bug in the password reset functionality.', FALSE),
(40, 'Posting pay field not validating inputs.', TRUE),
(41, 'UI issue with the dashboard view.', FALSE),
(42, 'Broken images in alumni section.', TRUE),
(43, 'Advisor dropdown list not populating.', FALSE),
(44, 'Timeout during data sync for applications.', TRUE),
(45, 'Student table missing graduation year.', FALSE),
(46, 'Search results displaying incorrect order.', TRUE),
(47, 'Error during database backup.', FALSE),
(48, 'Date validation missing for internship postings.', TRUE),
(49, 'Incorrect query result for student applications.', FALSE),
(50, 'Bug in sorting alumni by graduation year.', TRUE);

INSERT INTO Message (RE, Student_ID, Message, Alumni_ID)
VALUES
-- Conversation 1
(NULL, 1, 'Congratulations on your application!', 1),
(1, 1, 'Thank you! I am excited about this opportunity.', 1),
(2, 1, 'Do you have any tips for the interview process?', 1),
(3, 1, 'Be confident and prepare examples from past experiences.', 1),
(4, 1, 'Thank you for the advice!', 1),

-- Conversation 2
(NULL, 2, 'Welcome to the platform!', 2),
(6, 2, 'Thank you! Can you tell me more about the internship program?', 2),
(7, 2, 'Sure! The program focuses on hands-on projects and mentorship.', 2),
(8, 2, 'That sounds amazing! I look forward to applying.', 2),
(9, 2, 'Feel free to reach out if you have questions.', 2),

-- Conversation 3
(NULL, 3, 'We noticed your interest in data analytics.', 3),
(11, 3, 'Yes, I am passionate about exploring insights from data.', 3),
(12, 3, 'Great! I recommend practicing SQL and Python.', 3),
(13, 3, 'Thank you! Do you have any resources to share?', 3),
(14, 3, 'Yes, I will send you some links shortly.', 3),

-- Conversation 4
(NULL, 4, 'How can I assist you with your application?', 4),
(16, 4, 'I need help refining my resume.', 4),
(17, 4, 'Focus on highlighting your technical skills and achievements.', 4),
(18, 4, 'Thank you! Can I send you a draft for review?', 4),
(19, 4, 'Of course, feel free to send it anytime.', 4),

-- Conversation 5
(NULL, 5, 'Have you completed your profile on the platform?', 5),
(21, 5, 'Not yet, but I plan to finish it this weekend.', 5),
(22, 5, 'Let me know if you need any guidance.', 5),
(23, 5, 'Thank you! Is there anything specific I should include?', 5),
(24, 5, 'Include any relevant projects and certifications.', 5),

-- Conversation 6
(NULL, 6, 'What do you enjoy most about software development?', 6),
(26, 6, 'I enjoy solving challenging problems and building useful tools.', 6),
(27, 6, 'That’s great! Have you tried working on open-source projects?', 6),
(28, 6, 'Not yet, but I’d like to explore that soon.', 6),
(29, 6, 'It’s a good way to learn and collaborate with others.', 6),

-- Conversation 7
(NULL, 7, 'Have you started applying for internships?', 7),
(31, 7, 'Yes, I have applied to three positions so far.', 7),
(32, 7, 'Good luck! Keep track of application deadlines.', 7),
(33, 7, 'Thank you! Do you know how long it takes to hear back?', 7),
(34, 7, 'Usually a few weeks, but it varies by company.', 7),

-- Conversation 8
(NULL, 8, 'What are your career goals in AI?', 8),
(36, 8, 'I want to specialize in natural language processing.', 8),
(37, 8, 'That’s a fascinating field! Have you started any projects?', 8),
(38, 8, 'Yes, I built a chatbot as a personal project.', 8),
(39, 8, 'Impressive! Keep working on those skills.', 8),

-- Conversation 9
(NULL, 9, 'Did you find the resources I sent helpful?', 9),
(41, 9, 'Yes, they were very informative. Thank you!', 9),
(42, 9, 'Glad to hear that! Let me know if you need more.', 9),
(43, 9, 'I will! Are there any other tools I should learn?', 9),
(44, 9, 'Consider exploring Tableau for data visualization.', 9),

-- Conversation 10
(NULL, 10, 'How are your preparations going for the interview?', 10),
(46, 10, 'I’m reviewing common questions and practicing my answers.', 10),
(47, 10, 'Good! Don’t forget to research the company.', 10),
(48, 10, 'I’ve noted that. Thank you for the reminder!', 10),
(49, 10, 'You’re welcome. Best of luck!', 10);


Show TABLES;