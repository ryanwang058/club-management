-- Insert sample data for django settings



-- Insert sample members
-- INSERT INTO members_member(email, first_name, last_name)
-- VALUES 
-- ('john.doe@cmail.ca', 'John', 'Doe'),
-- ('jane.smith@cmail.ca', 'Jane', 'Smith'),
-- ('alice.jones@cmail.ca', 'Alice', 'Jones'),
-- ('bob.brown@cmail.ca', 'Bob', 'Brown'),

-- Insert sample adminstaff
-- INSERT INTO adminstaff_adminstaff(email, first_name, last_name)
-- VALUES
-- ('admin1@gmail.com', 'Charlie', 'Black');

-- Insert sample payments
INSERT INTO members_payment(member_id, payment_type, amount, date, status)
VALUES 
(1, 'Membership Fees', 49.99, '2024-03-01', 'Completed'),
(2, 'Training Class Fees', 39.99, '2024-03-03', 'Completed'),
(3, 'Membership Fees', 59.99, '2024-03-01', 'Completed'),
(4, 'Training Class Fees', 29.99, '2024-03-04', 'Declined'),
(5, 'Membership Fees', 34.99, '2024-03-01', 'Completed');

-- Insert sample exercises
INSERT INTO members_exercise(member_id, exercise_type, duration, date)
VALUES 
(1, 'Yoga', 60, '2024-03-05'),
(2, 'Strength', 45, '2024-03-07'),
(3, 'Yoga', 60, '2024-03-08'),
(4, 'Cardio', 30, '2024-03-07'),
(5, 'Strength', 45, '2024-03-08');

-- Insert sample trainers
-- INSERT INTO trainers_trainer(email, first_name, last_name, exercise_type)
-- VALUES 
-- ('coach1@gmail.com', 'Mike', 'Johnson', 'Strength'),
-- ('coach2@gmail.com', 'Anna', 'Davis', 'Yoga');

-- Insert sample rooms
INSERT INTO rooms_room(room_id, room_type, status)  -- Assuming 'room_id' is renamed to 'id' by Django
VALUES 
(101, 'Big Room', 'Available'),
(102, 'Small Room', 'Booked'),
(103, 'Big Room', 'Available'),
(104, 'Small Room', 'Available'),
(105, 'Big Room', 'Available');

-- Since classes_class might conflict with a reserved keyword 'class', it's renamed to 'classes_class' by Django
-- Insert sample classes
INSERT INTO classes_class(member_id, trainer_id, room_id, duration, date)
VALUES 
(1, 2, 103, 60, '2024-03-05'),
(1, 1, 101, 60, '2024-03-05'),
(2, 2, 103, 60, '2024-03-05'),
(3, 1, 101, 60, '2024-03-06'),
(4, 2, 103, 60, '2024-03-07'),
(5, 1, 101, 60, '2024-03-08');

-- Insert sample trainer availability
INSERT INTO trainers_trainer_availability(trainer_id, date, status)
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
INSERT INTO members_health_metrics(member_id, height, weight, bfp)
VALUES 
(1, 175, 70.0, 15.0),
(2, 160, 60.0, 20.0),
(3, 170, 65.0, 18.0),
(4, 180, 80.0, 10.0),
(5, 165, 55.0, 22.0);

-- Insert sample equipment
INSERT INTO equipment_equipment(equipment_type, status)
VALUES 
('Treadmill', 'Normal'),
('Dumbbell Set', 'Normal'),
('Yoga Mat', 'Broken');
