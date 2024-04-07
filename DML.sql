-- Insert sample members
INSERT INTO Member(email, first_name, last_name)
VALUES 
('mem1@gmail.com', 'Alex', 'Turner'),
('mem2@gmail.com', 'John', 'Carlos');

-- Insert sample payments
INSERT INTO Payment(member_id, payment_type, amount, date, status)
VALUES 
(1, 'Training Class Fees', 30.00, '2024-03-01', 'Completed'),
(2, 'Training Class Fees', 30.00, '2024-03-03', 'Pending');

-- Insert sample exercises
INSERT INTO Exercise(member_id, exercise_type, duration, date)
VALUES 
(1, 'Yoga', 60, '2024-03-05'),
(1, 'Yoga', 55, '2024-03-12'),
(1, 'Strength', 45, '2024-03-30'),
(2, 'Strength', 45, '2024-03-15');

-- Insert sample trainers
INSERT INTO Trainer(email, first_name, last_name, exercise_type)
VALUES 
('coach1@gmail.com', 'Mike', 'Johnson', 'Strength'),
('coach2@gmail.com', 'Anna', 'Davis', 'Yoga');

-- Insert sample rooms
INSERT INTO Room(room_id, RoomType, Status)
VALUES 
(101, 'Big Room', 'Available'),
(102, 'Small Room', 'Available'),
(103, 'Big Room', 'Booked'),
(104, 'Small Room', 'Available'),
(105, 'Big Room', 'Available');

-- Insert sample classes
INSERT INTO Class(member_id, trainer_id, room_id, duration, date)
VALUES 
(2, 1, 103, 60, '2024-04-12'),
(1, 2, null, 60, '2024-04-13');


-- Insert sample trainer availability
INSERT INTO Trainer_Availability(trainer_id, date, status)
VALUES 
(1, '2024-03-11', 'Available'),
(1, '2024-04-11', 'Available'),
(1, '2024-04-12', 'Booked'),
(1, '2024-04-13', 'Available'),
(1, '2024-04-14', 'Available'),
(2, '2024-04-11', 'Available'),
(2, '2024-04-12', 'Available'),
(2, '2024-04-13', 'Pending'),
(2, '2024-04-14', 'Available'),
(2, '2024-04-15', 'Available');

-- Insert sample health metrics
INSERT INTO Health_Metrics(member_id, height, weight, bfp)
VALUES 
(1, 175, 70.0, 15.1, '2024-03-07'),
(1, 169, 60.3, 20.3, '2024-03-08'),
(1, 183, 80.0, 25.3, '2024-03-10'),
(2, 170, 65.0, 18.4, '2024-03-09'),
(2, 165, 55.0, 22.7, '2024-03-11');

-- Insert sample health metrics
INSERT INTO Health_Metrics(member_id, height, weight, bfp)
VALUES 
(1, 175, 70.0, 15.1, '2024-03-07'),
(1, 169, 60.3, 20.3, '2024-03-08'),
(1, 183, 80.0, 25.3, '2024-03-10'),
(2, 170, 65.0, 18.4, '2024-03-09'),
(2, 165, 55.0, 22.7, '2024-03-11');

-- Insert sample fitness goals
INSERT INTO Fitness_Goals(member_id, exercise_type, duration)
VALUES 
(1, 'Yoga', 180),
(1, 'Strength', 200),
(1, 'Cardio', 100),
(2, 'Yoga', 150);

-- Insert sample equipment 
INSERT INTO Equipment(equipment_type, status)
VALUES 
('Treadmill', 'Normal'),
('Dumbbell Set', 'Broken'),
('Yoga Mat', 'Broken');
