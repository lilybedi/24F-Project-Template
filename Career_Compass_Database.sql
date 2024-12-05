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

CREATE TABLE FieldOfStudy (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Description TEXT
);

CREATE TABLE Major
(
    Student_ID INT NOT NULL,
    FieldOfStudy_ID INT NOT NULL,
    PRIMARY KEY (Student_ID, FieldOfStudy_ID),
    FOREIGN KEY (Student_ID) REFERENCES Student(ID),
    FOREIGN KEY (FieldOfStudy_ID) REFERENCES FieldOfStudy(ID)
);

CREATE TABLE Minor
(
    Student_ID INT NOT NULL,
    FieldOfStudy_ID INT NOT NULL,
    PRIMARY KEY (Student_ID, FieldOfStudy_ID),
    FOREIGN KEY (Student_ID) REFERENCES Student(ID),
    FOREIGN KEY (FieldOfStudy_ID) REFERENCES FieldOfStudy(ID)
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
('Arizona State University');

# FieldOFStudy Insert Statements
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

# Major Insert Statements 
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
INSERT INTO Minor (Student_ID, FieldOfStudy_ID) VALUES
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

# Skill Insert Stattements
INSERT INTO Skill (Name, Description, Industry)
VALUES
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
