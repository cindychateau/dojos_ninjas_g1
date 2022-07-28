-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojos_ninjas_flask
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dojos_ninjas_flask
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojos_ninjas_flask` DEFAULT CHARACTER SET utf8 ;
USE `dojos_ninjas_flask` ;

-- -----------------------------------------------------
-- Table `dojos_ninjas_flask`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_ninjas_flask`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojos_ninjas_flask`.`ninjas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_ninjas_flask`.`ninjas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `age` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `dojo_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ninjas_dojos_idx` (`dojo_id` ASC),
  CONSTRAINT `fk_ninjas_dojos`
    FOREIGN KEY (`dojo_id`)
    REFERENCES `dojos_ninjas_flask`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
