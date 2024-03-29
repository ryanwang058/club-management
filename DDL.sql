CREATE TABLE Member (
  member_id SERIAL PRIMARY KEY,
  email VARCHAR(255),
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

CREATE TABLE Payment (
  payment_id SERIAL PRIMARY KEY,
  member_id INT,
  payment_type VARCHAR(50),
  amount DECIMAL(10,2),
  date Date,
  status VARCHAR(50),
  FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

CREATE TABLE Exercise (
  exercise_id SERIAL PRIMARY KEY,
  member_id INT,
  exercise_type VARCHAR(50),
  duration INT,
  date Date,
  FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

CREATE TABLE Trainer (
  trainer_id SERIAL PRIMARY KEY,
  email VARCHAR(255),
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  exercise_type VARCHAR(50)
);

CREATE TABLE Room (
  room_id INT PRIMARY KEY,
  RoomType VARCHAR(50),
  Status VARCHAR(50)
);

CREATE TABLE Class (
  class_id SERIAL PRIMARY KEY,
  member_id INT,
  trainer_id INT,
  room_id INT,
  duration INT,
  date Date,
  FOREIGN KEY (member_id) REFERENCES Member(member_id),
  FOREIGN KEY (trainer_id) REFERENCES Trainer(trainer_id),
  FOREIGN KEY (room_id) REFERENCES Room(room_id)
);

CREATE TABLE Trainer_Availability (
  trainer_id INT,
  date Date,
  status VARCHAR(50),
  PRIMARY KEY (trainer_id, date),
  FOREIGN KEY (trainer_id) REFERENCES Trainer(trainer_id)
);

CREATE TABLE Health_Metrics (
  member_id INT PRIMARY KEY,
  height INT,
  weight DECIMAL(5,2),
  bfp DECIMAL(5,2),
  FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

CREATE TABLE Equipment (
  equipment_id SERIAL PRIMARY KEY,
  equipment_type VARCHAR(50),
  status VARCHAR(50)
);

-- Foreign Keys
-- ALTER TABLE Payment ADD CONSTRAINT fk_payment_member_id FOREIGN KEY (member_id) REFERENCES Member(member_id);
-- ALTER TABLE Exercise ADD CONSTRAINT fk_exercise_member_id FOREIGN KEY (member_id) REFERENCES Member(member_id);
-- ALTER TABLE Class ADD CONSTRAINT fk_class_member_id FOREIGN KEY (member_id) REFERENCES Member(member_id);
-- ALTER TABLE Class ADD CONSTRAINT fk_class_trainer_id FOREIGN KEY (trainer_id) REFERENCES Trainer(trainer_id);
-- ALTER TABLE Class ADD CONSTRAINT fk_class_room_id FOREIGN KEY (room_id) REFERENCES Room(room_id);
-- ALTER TABLE TrainerAvailability ADD CONSTRAINT fk_traineravailability_trainer_id FOREIGN KEY (trainer_id) REFERENCES Trainer(trainer_id);
-- ALTER TABLE HealthMetrics ADD CONSTRAINT fk_healthmetrics_member_id FOREIGN KEY (member_id) REFERENCES Member(member_id);
