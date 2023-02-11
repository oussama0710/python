SELECT * FROM mydb.users;
SELECT * FROM mydb.users
WHERE email='mohsen@gmail.com';
SELECT * FROM mydb.users
WHERE id=3;

UPDATE `mydb`.`users` SET `first_name` = 'pnacakes' WHERE (`id` = '3');
INSERT INTO `mydb`.`users`(`first_name`,last_name,email)
VALUES
	('Mohsen','khnessi','mohsen@gmail.com'),
	('Ali','nakbi','ali.nakbi@gmail.com'),
	('Mohamed','lahmer','medlhr@gmail.com');
DELETE FROM `mydb`.`users` WHERE (`id` = '2');
SELECT first_name FROM mydb.users;
SELECT * FROM users
ORDER BY first_name DESC;