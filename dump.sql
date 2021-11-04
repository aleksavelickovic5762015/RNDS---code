SET default_storage_engine=InnoDB;

CREATE DATABASE IF NOT EXISTS rnds;

USE rnds;

-- MySQL dump 10.16  Distrib 10.2.13-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: rnds
-- ------------------------------------------------------
-- Server version       10.2.13-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `defaultstatuses`
--

DROP TABLE IF EXISTS `defaultstatuses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `defaultstatuses` (
  `name` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(50) NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `defaultStatuses_name_uindex` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `defaultstatuses`
--

LOCK TABLES `defaultstatuses` WRITE;
/*!40000 ALTER TABLE `defaultstatuses` DISABLE KEYS */;
INSERT INTO `defaultstatuses` VALUES (1,'Not at home'),(2,'Sleeping'),(3,'Studying'),(4,'Chilling Out');
/*!40000 ALTER TABLE `defaultstatuses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `houses`
--

DROP TABLE IF EXISTS `houses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `houses` (
  `name` int(11) NOT NULL AUTO_INCREMENT,
  `roomsNumber` int(11) NOT NULL DEFAULT 2,
  `shared spaces` int(11) NOT NULL DEFAULT 1,
  `description` varchar(50) NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `HOUSES_name_uindex` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `houses`
--

LOCK TABLES `houses` WRITE;
/*!40000 ALTER TABLE `houses` DISABLE KEYS */;
INSERT INTO `houses` VALUES (1,2,1,'Our Home');
/*!40000 ALTER TABLE `houses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lu_noise`
--

DROP TABLE IF EXISTS `lu_noise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lu_noise` (
  `name` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(50) NOT NULL,
  `dbmin` int(11) NOT NULL,
  `dbmax` int(11) DEFAULT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `lu_noise_name_uindex` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lu_noise`
--

LOCK TABLES `lu_noise` WRITE;
/*!40000 ALTER TABLE `lu_noise` DISABLE KEYS */;
INSERT INTO `lu_noise` VALUES (1,'low',0,30),(2,'medium',31,50),(3,'hight',51,70),(4,'Any noise',71,9000);
/*!40000 ALTER TABLE `lu_noise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `name` int(11) NOT NULL,
  `completeName` varchar(50) NOT NULL,
  `house` int(11) NOT NULL,
  `roomNumber` int(11) NOT NULL,
  `windowId` int(11) DEFAULT NULL,
  `doorId` int(11) DEFAULT NULL,
  `windowStatus` int(11) DEFAULT NULL,
  `doorStatus` int(11) DEFAULT 0,
  `lightId` int(11) DEFAULT NULL,
  `lightStatus` int(11) DEFAULT 0,
  `phoneNumber` int(11) DEFAULT NULL,
  `vlcId` int(11) DEFAULT NULL,
  `actualUserStatus` varchar(5) NOT NULL,
  `isDisturbing` tinyint(1) NOT NULL DEFAULT 0,
  `actualNoiseLevel` int(11) DEFAULT 1,
  PRIMARY KEY (`name`),
  UNIQUE KEY `Users_name_uindex` (`name`),
  UNIQUE KEY `users_completeName_uindex` (`completeName`),
  KEY `Users_houses_name_fk` (`house`),
  KEY `users_lu_noise_name_fk` (`actualNoiseLevel`),
  CONSTRAINT `Users_houses_name_fk` FOREIGN KEY (`house`) REFERENCES `houses` (`name`),
  CONSTRAINT `users_lu_noise_name_fk` FOREIGN KEY (`actualNoiseLevel`) REFERENCES `lu_noise` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Andrea',1,1,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,'1_1',0,1),(2,'Aleksa',1,1,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,'2_2',0,1),(3,'Selena',1,2,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,'3_3',0,1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usersettings`
--

DROP TABLE IF EXISTS `usersettings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usersettings` (
  `name` varchar(10),
  `isWindowsOpen` int(11) NOT NULL DEFAULT 0,
  `isDoorOpen` int(11) NOT NULL DEFAULT 0,
  `isLightsOn` int(11) NOT NULL DEFAULT 0,
  `noiseLevel` int(11) NOT NULL DEFAULT 2,
  KEY `usersettings_userstatuses_name_fk` (`name`),
  KEY `usersettings_lu_noise_name_fk` (`noiseLevel`),
  CONSTRAINT `usersettings_lu_noise_name_fk` FOREIGN KEY (`noiseLevel`) REFERENCES `lu_noise` (`name`),
  CONSTRAINT `usersettings_userstatuses_name_fk` FOREIGN KEY (`name`) REFERENCES `userstatuses` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usersettings`
--

LOCK TABLES `usersettings` WRITE;
/*!40000 ALTER TABLE `usersettings` DISABLE KEYS */;
INSERT INTO `usersettings` VALUES ('1_1',1,0,0,4),('1_2',0,0,0,2),('1_3',0,0,0,2),('1_4',0,0,0,2),('2_1',0,0,0,2),('2_2',0,0,0,2),('2_3',0,0,0,2),('2_4',0,0,0,2),('3_1',0,0,0,2),('3_2',0,0,0,2),('3_3',0,0,0,2),('3_4',0,0,0,2);
/*!40000 ALTER TABLE `usersettings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userstatuses`
--

DROP TABLE IF EXISTS `userstatuses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userstatuses` (
  `name` varchar(5) NOT NULL,
  `user` int(11) NOT NULL,
  `DefaultStatus` int(11) NOT NULL,
  `customisedDescription` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `userStatuses_name_uindex` (`name`),
  KEY `userstatuses_defaultstatuses_name_fk` (`DefaultStatus`),
  KEY `userstatuses_users_name_fk` (`user`),
  CONSTRAINT `userstatuses_defaultstatuses_name_fk` FOREIGN KEY (`DefaultStatus`) REFERENCES `defaultstatuses` (`name`),
  CONSTRAINT `userstatuses_users_name_fk` FOREIGN KEY (`user`) REFERENCES `users` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userstatuses`
--

LOCK TABLES `userstatuses` WRITE;
/*!40000 ALTER TABLE `userstatuses` DISABLE KEYS */;
INSERT INTO `userstatuses` VALUES ('1_1',1,1,''),('1_2',1,2,''),('1_3',1,3,''),('1_4',1,4,''),('2_1',2,1,''),('2_2',2,2,''),('2_3',2,3,''),('2_4',2,4,''),('3_1',3,1,''),('3_2',3,2,''),('3_3',3,3,''),('3_4',3,4,'');
/*!40000 ALTER TABLE `userstatuses` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
