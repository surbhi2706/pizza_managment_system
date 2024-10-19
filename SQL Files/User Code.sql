CREATE TABLE User (
  User_ID varchar(10) NOT NULL,
  First_Name varchar(20) DEFAULT NULL,
  Last_Name varchar(20) DEFAULT NULL,
  User_Name varchar(30) DEFAULT NULL,
  Password varchar(20) NOT NULL,
  PHNO bigint DEFAULT NULL,
  Gender varchar(10) DEFAULT NULL,
  DOB date NOT NULL,
  Age int DEFAULT NULL,
  Email varchar(30) DEFAULT NULL,
  Address varchar(75) DEFAULT NULL,
  PRIMARY KEY (User_ID),
  UNIQUE KEY User_Name (User_Name),
  UNIQUE KEY Email (Email),
  CONSTRAINT check_Email_validity CHECK (((Email like '%___@________%') and (Email like '%.com'))),
  CONSTRAINT check_PHNO_validity CHECK (((PHNO > 999999999) and (PHNO < 10000000000)))
);

INSERT INTO User VALUES
  ('U101','xyz','abc','xyz_abc','xyz@123',1234567890,'Female','2005-05-05',17,'xyz@example.com','xyz'),
  ('U102','abc','xyz','abc_xyz','abc@123',1234567890,'Male','2007-07-07',15,'abc@example.com','abc');

SELECT * FROM User;

CREATE VIEW User_View AS
  SELECT First_Name, Last_Name, User_Name, PHNO, Gender, DOB, Age, Email, Address FROM User;

SELECT * FROM User_View;