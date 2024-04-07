DROP TABLE IF EXISTS Member CASCADE;
DROP TABLE IF EXISTS Trainer CASCADE;
DROP TABLE IF EXISTS AdminStaff CASCADE;
DROP TABLE IF EXISTS Payment CASCADE;
DROP TABLE IF EXISTS Exercise CASCADE;
DROP TABLE IF EXISTS Room CASCADE;
DROP TABLE IF EXISTS Class CASCADE;
DROP TABLE IF EXISTS Health_Metrics CASCADE;
DROP TABLE IF EXISTS Fitness_Goals CASCADE;
DROP TABLE IF EXISTS Equipment CASCADE;
DROP TABLE IF EXISTS Trainer_Availability CASCADE;

CREATE TABLE Member (
  member_id SERIAL PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL
);

CREATE TABLE Trainer (
  trainer_id SERIAL PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  exercise_type VARCHAR(50) NOT NULL
);

CREATE TABLE AdminStaff (
  admin_id SERIAL PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL
);

CREATE TABLE Payment (
  payment_id SERIAL PRIMARY KEY,
  member_id INT NOT NULL,
  payment_type VARCHAR(50) NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  date Date NOT NULL,
  status VARCHAR(50) NOT NULL,
  FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

CREATE TABLE Exercise (
  exercise_id SERIAL PRIMARY KEY,
  member_id INT NOT NULL,
  exercise_type VARCHAR(50) NOT NULL,
  duration INT NOT NULL,
  date Date NOT NULL,
  FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

CREATE TABLE Room (
  room_id INT PRIMARY KEY,
  RoomType VARCHAR(50) NOT NULL,
  Status VARCHAR(50) NOT NULL
);

CREATE TABLE Class (
  class_id SERIAL PRIMARY KEY,
  member_id INT NOT NULL,
  trainer_id INT NOT NULL,
  room_id INT,
  duration INT NOT NULL,
  date Date NOT NULL,
  FOREIGN KEY (member_id) REFERENCES Member(member_id),
  FOREIGN KEY (trainer_id) REFERENCES Trainer(trainer_id),
  FOREIGN KEY (room_id) REFERENCES Room(room_id)
);

CREATE TABLE Trainer_Availability (
  trainer_id INT,
  date Date,
  status VARCHAR(50) NOT NULL,
  PRIMARY KEY (trainer_id, date),
  FOREIGN KEY (trainer_id) REFERENCES Trainer(trainer_id)
);

CREATE TABLE Health_Metrics (
  member_id INT PRIMARY KEY,
  height INT NOT NULL,
  weight DECIMAL(5,2) NOT NULL,
  bfp DECIMAL(5,2) NOT NULL,
  FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

CREATE TABLE Fitness_Goals (
  member_id INT PRIMARY KEY,
  exercise_type VARCHAR(50) NOT NULL,
  duration int NOT NULL,
  FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

CREATE TABLE Equipment (
  equipment_id SERIAL PRIMARY KEY,
  equipment_type VARCHAR(50) NOT NULL,
  status VARCHAR(50) NOT NULL
);