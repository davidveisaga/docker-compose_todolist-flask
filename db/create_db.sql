CREATE DATABASE IF NOT EXISTS `db_flask`;

USE `db_flask`;

CREATE TABLE `db_flask`.`mytable` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `text_value` VARCHAR(500) NULL,
  PRIMARY KEY (`ID`));