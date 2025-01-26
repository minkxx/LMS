CREATE DATABASE IF NOT EXISTS LMS;
USE LMS;
CREATE TABLE IF NOT EXISTS `Role` (
	`id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`type` varchar(255) NOT NULL UNIQUE,
	PRIMARY KEY (`id`)
);
CREATE TABLE IF NOT EXISTS `Gender` (
	`id` int AUTO_INCREMENT NOT NULL,
	`type` varchar(255) NOT NULL UNIQUE,
	PRIMARY KEY (`id`)
);
CREATE TABLE IF NOT EXISTS `Genre` (
	`id` int AUTO_INCREMENT NOT NULL,
	`type` varchar(255) NOT NULL UNIQUE,
	PRIMARY KEY (`id`)
);
CREATE TABLE IF NOT EXISTS `Users` (
	`id` int AUTO_INCREMENT NOT NULL,
	`firstname` varchar(255) NOT NULL,
	`surname` varchar(255) NULL,
	`email` varchar(255) NOT NULL UNIQUE,
	`mobile_phone` varchar(255) NULL UNIQUE,
	`password_hash` varchar(255) NULL,
	`gender_id` int NOT NULL,
	`address` varchar(255) NULL,
	`role_id` int NOT NULL,
	PRIMARY KEY (`id`)
);
CREATE TABLE IF NOT EXISTS `Books` (
	`id` int AUTO_INCREMENT NOT NULL,
	`title` varchar(255) NOT NULL,
	`author` varchar(255) NOT NULL,
	`genre_id` int NOT NULL,
	`description` varchar(255) NULL,
	`total_amount` int NOT NULL,
	PRIMARY KEY (`id`)
);
CREATE TABLE IF NOT EXISTS `Events` (
	`id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`book_id` int NOT NULL,
	`user_id` int NOT NULL,
	`issue_date` date NOT NULL,
	`return_date` date NOT NULL,
	PRIMARY KEY (`id`)
);
ALTER TABLE `Users` ADD CONSTRAINT `Users_fk6` FOREIGN KEY (`gender_id`) REFERENCES `Gender`(`id`);
ALTER TABLE `Users` ADD CONSTRAINT `Users_fk8` FOREIGN KEY (`role_id`) REFERENCES `Role`(`id`);
ALTER TABLE `Books` ADD CONSTRAINT `Books_fk3` FOREIGN KEY (`genre_id`) REFERENCES `Genre`(`id`);
ALTER TABLE `Events` ADD CONSTRAINT `Events_fk1` FOREIGN KEY (`book_id`) REFERENCES `Books`(`id`);
ALTER TABLE `Events` ADD CONSTRAINT `Events_fk2` FOREIGN KEY (`user_id`) REFERENCES `Users`(`id`);
INSERT INTO `Role` (`type`) VALUES ('Admin'), ('Student');
INSERT INTO `Gender` (`type`) VALUES ('Male'), ('Female'), ('Other');
INSERT INTO `Genre` (`type`) VALUES ('Fantasy'), ('Science Fiction'), ('Mystery'), ('Horror'), ('Romance'), ('Thriller'), ('Western'),('Cookbook'), ('Biography'),('Travel'), ('Humor');
INSERT INTO users (firstname, surname, email, mobile_phone, gender_id, address, role_id) 
VALUES
('Alice', 'Smith', 'alice.smith@example.com', '1234567890', 2, 'Springfield', 2),
('Bob', 'Johnson', 'bob.johnson@example.com', '2345678901', 1, 'Greenwood', 2),
('Charlie', 'Brown', 'charlie.brown@example.com', '3456789012', 3, 'Hilltop', 2),
('Diana', 'Prince', 'diana.prince@example.com', '4567890123', 2, 'Seaside', 2),
('Evan', 'Taylor', 'evan.taylor@example.com', '5678901234', 1, 'Oakwood', 2),
('Fiona', 'Davis', 'fiona.davis@example.com', '6789012345', 2, 'Lakeview', 2),
('George', 'Clark', 'george.clark@example.com', '7890123456', 3, 'Maple Street', 2),
('Hannah', 'Morris', 'hannah.morris@example.com', '8901234567', 2, 'Riverside', 2),
('Ian', 'Wright', 'ian.wright@example.com', '9012345678', 1, 'Elm Avenue', 2);
INSERT INTO books (title, author, genre_id, description, total_amount) 
VALUES
('Name of the Wind', 'Patrick Rothfuss', 1, 'A legendary figure in a world of magic.', 5),
('Dune', 'Frank Herbert', 2, 'A desert planet and its political intrigue.', 8),
('Girl with the Dragon Tattoo', 'Stieg Larsson', 3, 'A mystery involving a missing woman.', 7),
('It', 'Stephen King', 4, 'A horror novel about an evil entity in a small town.', 6),
('Pride & Prejudice', 'Jane Austen', 5, 'A romantic story about love and class.', 10),
('Girl on the Train', 'Paula Hawkins', 6, 'A psychological thriller with twists and turns.', 9),
('Virginian', 'Owen Wister', 7, 'A western novel about a cowboy’s life.', 4),
('Joy of Cooking', 'Irma S. Rombauer', 8, 'A classic cookbook with simple recipes.', 15),
('Steve Jobs', 'Walter Isaacson', 9, 'A biography of the visionary Apple co-founder.', 12),
('Art of Travel', 'Alain de Botton', 10, 'A philosophical exploration of travel.', 3),
('Hitchhiker Guide', 'Douglas Adams', 11, 'A humorous adventure through space.', 10);
