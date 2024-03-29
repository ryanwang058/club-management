-- Insert sample members
INSERT INTO Member(email, first_name, last_name)
VALUES 
('john.doe@cmail.ca', 'John', 'Doe'),
('jane.smith@cmail.ca', 'Jane', 'Smith'),
('alice.jones@cmail.ca', 'Alice', 'Jones'),
('bob.brown@cmail.ca', 'Bob', 'Brown'),
('charlie.black@cmail.ca', 'Charlie', 'Black');

-- Insert sample payments
INSERT INTO Payment(member_id, payment_type, amount, date, status)
VALUES 
(1, 'Membership Fees', 49.99, '2024-03-01', 'Completed'),
(2, 'Training Class Fees', 39.99, '2024-03-03', 'Completed'),
(3, 'Membership Fees', 59.99, '2024-03-01', 'Completed'),
(4, 'Training Class Fees', 29.99, '2024-03-04', 'Declined'),
(5, 'Membership Fees', 34.99, '2024-03-01', 'Completed');

-- Insert sample exercises
INSERT INTO Exercise(member_id, exercise_type, duration, date)
VALUES 
(1, 'Yoga', 60, '2024-03-05'),
(2, 'Strength', 45, '2024-03-07'),
(3, 'Yoga', 60, '2024-03-08'),
(4, 'Cardio', 30, '2024-03-07'),
(5, 'Strength', 45, '2024-03-08');

-- Insert sample trainers
INSERT INTO Trainer(email, first_name, last_name, exercise_type)
VALUES 
('coach.mike@scs.carleton.ca', 'Mike', 'Johnson', 'Strength'),
('coach.anna@scs.carleton.ca', 'Anna', 'Davis', 'Yoga');

-- Insert sample rooms
INSERT INTO Room(room_id, RoomType, Status)
VALUES 
(101, 'Big Room', 'Available'),
(102, 'Small Room', 'Booked'),
(103, 'Big Room', 'Available'),
(104, 'Small Room', 'Available'),
(105, 'Big Room', 'Available');

-- Insert sample classes
INSERT INTO Class(member_id, trainer_id, room_id, duration, date)
VALUES 
(1, 2, 103, 60, '2024-03-05'),
(1, 1, 101, 60, '2024-03-05'),
(2, 2, 103, 60, '2024-03-05'),
(3, 1, 101, 60, '2024-03-06'),
(4, 2, 103, 60, '2024-03-07'),
(5, 1, 101, 60, '2024-03-08');

-- 3.5
-- member 1 booked trainer 2 at 103

-- Insert sample trainer availability for March 2024 with more options
INSERT INTO Trainer_Availability(trainer_id, date, status)
VALUES 
(1, '2024-03-05', 'Available'),
(2, '2024-03-05', 'Booked'),
(1, '2024-03-06', 'Available'),
(2, '2024-03-06', 'Available'),
(1, '2024-03-07', 'Booked'),
(2, '2024-03-07', 'Available'),
(1, '2024-03-08', 'Available'),
(2, '2024-03-08', 'Booked');

-- Insert sample health metrics for each member
INSERT INTO Health_Metrics(member_id, height, weight, bfp)
VALUES 
(1, 175, 70.0, 15.0),
(2, 160, 60.0, 20.0),
(3, 170, 65.0, 18.0),
(4, 180, 80.0, 10.0),
(5, 165, 55.0, 22.0);

-- Insert sample equipment with updated status
INSERT INTO Equipment(equipment_type, status)
VALUES 
('Treadmill', 'Normal'),
('Dumbbell Set', 'Normal'),
('Yoga Mat', 'Broken');
