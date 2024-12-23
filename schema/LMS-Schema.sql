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
	`surname` varchar(255) NOT NULL,
	`email` varchar(255) NOT NULL UNIQUE,
	`mobile_phone` varchar(255) NOT NULL UNIQUE,
	`password_hash` varchar(255) NOT NULL,
	`gender_id` int NOT NULL,
	`address` varchar(255) NOT NULL,
	`role_id` int NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Books` (
	`id` int AUTO_INCREMENT NOT NULL,
	`title` varchar(255) NOT NULL,
	`author` varchar(255) NOT NULL,
	`genre_id` int NOT NULL,
	`description` varchar(255) NOT NULL,
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