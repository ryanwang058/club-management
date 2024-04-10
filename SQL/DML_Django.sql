-- insert django related tables
INSERT INTO club_user(id, password, last_login, is_superuser, email, first_name, last_name, is_member, is_trainer, is_staff)
VALUES
(1, 'pbkdf2_sha256$720000$Nhi0X5H1rLeWkqP0piBOqv$CWprFH30azUO/6M9xjLNkhbmBEotd8fDBmQJQ0ytc2Q=', '2024-04-06 16:06:33.009672-04', false, 'mem1@gmail.com', 'Alex', 'Turner', true, false, false),
(2, 'pbkdf2_sha256$720000$11pa7PDu3P5Qr65az0skvP$3CF1dd5sn+V6Rr6ETqqE0FbtfI7rkFP9bcmAEnqaR70=', '2024-04-06 15:45:42.946371-04', false, 'coach1@gmail.com', 'Mike', 'Johnson', false, true, false),
(3, 'pbkdf2_sha256$720000$UZ9X6hwWckO6OnSZuVyL4U$mifjLr1aJl4nNO17zBq2wJNVgFkfsFlllNzN3EjxRmE=', '2024-04-03 14:51:48.811084-04', false, 'coach2@gmail.com', 'Anna', 'Davis', false, true, false),
(4, 'pbkdf2_sha256$720000$tbZNIkrpPmUbR09Z6r7COe$TOWwZRiAh45BNF5hKa0RhlPwM+MrUEGRChjMF5wZftM=', '2024-04-06 15:32:36.258414-04', false, 'admin1@gmail.com', 'Charlie', 'Black', false, false, true),
(5, 'pbkdf2_sha256$720000$xihbji5puThy2kADsvZWk1$N0n2RecMlOb1O80Z+LzT0CjoIat/VSrWtsZt+TLNJyA=', '2024-04-06 16:06:07.844247-04', false, 'mem2@gmail.com', 'John', 'Carlos', true, false, false); 

INSERT INTO auth_group(id, name)
VALUES
(1, 'Members'),
(2, 'Trainers'),
(3, 'AdminStaff');

-- table for user group & authentication
INSERT INTO club_user_groups(id, user_id, group_id)
VALUES
(1,1,1),
(2,2,2),
(3,3,2),
(4,4,3),
(5,5,1);

-- for django authentication, member/trainer/adminstaff are linked to user
INSERT INTO members_member(id, user_id)
VALUES
(1,1),
(2,5);

INSERT INTO trainers_trainer(id, exercise_type, user_id)
VALUES
(1, 'Strength', 2),
(2, 'Yoga', 3);

INSERT INTO adminstaff_adminstaff(id, user_id)
VALUES
(1,4);

-- Insert sample payments
INSERT INTO members_payment(member_id, payment_type, amount, date, status)
VALUES 
(1, 'Training Class Fees', 30.00, '2024-03-01', 'Completed'),
(2, 'Training Class Fees', 30.00, '2024-03-03', 'Pending');

-- Insert sample exercises
INSERT INTO members_exercise(member_id, exercise_type, duration, date)
VALUES 
(1, 'Yoga', 60, '2024-03-05'),
(1, 'Yoga', 55, '2024-03-12'),
(1, 'Strength', 45, '2024-03-30'),
(2, 'Strength', 45, '2024-03-15');

-- Insert sample rooms
INSERT INTO rooms_room(room_id, room_type, status)
VALUES 
(101, 'Big Room', 'Available'),
(102, 'Small Room', 'Available'),
(103, 'Big Room', 'Booked'),
(104, 'Small Room', 'Available'),
(105, 'Big Room', 'Available');

-- Insert sample classes
INSERT INTO classes_class(member_id, trainer_id, room_id, duration, date)
VALUES 
(2, 1, 103, 60, '2024-04-12'),
(1, 2, null, 60, '2024-04-13');

-- Insert sample trainer availability
INSERT INTO trainers_trainer_availability(trainer_id, date, status)
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
INSERT INTO members_health_metrics(member_id, height, weight, bfp, date)
VALUES 
(1, 175, 70.0, 15.1, '2024-03-07'),
(1, 169, 60.3, 20.3, '2024-03-08'),
(1, 183, 80.0, 25.3, '2024-03-10'),
(2, 170, 65.0, 18.4, '2024-03-09'),
(2, 165, 55.0, 22.7, '2024-03-11');

-- Insert sample fitness goals
INSERT INTO members_fitness_goals(member_id, exercise_type, duration)
VALUES 
(1, 'Yoga', 180),
(1, 'Strength', 200),
(1, 'Cardio', 100),
(2, 'Yoga', 150);

-- Insert sample equipment
INSERT INTO equipment_equipment(equipment_type, status)
VALUES 
('Treadmill', 'Normal'),
('Dumbbell Set', 'Broken'),
('Yoga Mat', 'Broken');