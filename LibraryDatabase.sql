CREATE DATABASE  IF NOT EXISTS `mainlibrarydatabase` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mainlibrarydatabase`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: mainlibrarydatabase
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `book_id` int NOT NULL,
  `title` varchar(20) DEFAULT NULL,
  `author` varchar(20) DEFAULT NULL,
  `publisher` varchar(20) DEFAULT NULL,
  `year_of_publish` int DEFAULT NULL,
  PRIMARY KEY (`book_id`),
  KEY `publisher` (`publisher`),
  CONSTRAINT `book_ibfk_1` FOREIGN KEY (`publisher`) REFERENCES `publisher` (`NAME`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'java','siddharth','pearson',2019),(2,'DBMS','siddharth','MCGRAW-HILL',2017),(3,'Data structure','sid','MCGRAW-HILL',2016),(4,'Comuter Networks','rohit','PEARSON',2013),(5,'Python Programming','sid','PEARSON',2012),(6,'Data structure','sid','MCGRAW-HILL',2016),(7,'english grammer','siddharth','sid pub',2012);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_copies`
--

DROP TABLE IF EXISTS `book_copies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_copies` (
  `NoOfCopies` int DEFAULT NULL,
  `bookId` int NOT NULL,
  `branchId` int NOT NULL,
  PRIMARY KEY (`bookId`,`branchId`),
  KEY `branchId` (`branchId`),
  CONSTRAINT `book_copies_ibfk_1` FOREIGN KEY (`branchId`) REFERENCES `librarybranch` (`branchId`) ON DELETE CASCADE,
  CONSTRAINT `book_copies_ibfk_2` FOREIGN KEY (`bookId`) REFERENCES `book` (`book_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_copies`
--

LOCK TABLES `book_copies` WRITE;
/*!40000 ALTER TABLE `book_copies` DISABLE KEYS */;
INSERT INTO `book_copies` VALUES (10,1,10),(5,1,11),(12,2,10),(2,2,12),(5,2,13),(8,3,14),(4,4,11),(1,5,10),(13,6,12),(11,7,10);
/*!40000 ALTER TABLE `book_copies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_lending`
--

DROP TABLE IF EXISTS `book_lending`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_lending` (
  `DATE_OUT` date DEFAULT NULL,
  `DUE_DATE` date DEFAULT NULL,
  `BOOK_ID` int NOT NULL,
  `BRANCH_ID` int NOT NULL,
  `CARD_NO` int NOT NULL,
  PRIMARY KEY (`BOOK_ID`,`BRANCH_ID`,`CARD_NO`),
  KEY `BRANCH_ID` (`BRANCH_ID`),
  CONSTRAINT `book_lending_ibfk_1` FOREIGN KEY (`BOOK_ID`) REFERENCES `book` (`book_id`) ON DELETE CASCADE,
  CONSTRAINT `book_lending_ibfk_2` FOREIGN KEY (`BRANCH_ID`) REFERENCES `librarybranch` (`branchId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_lending`
--

LOCK TABLES `book_lending` WRITE;
/*!40000 ALTER TABLE `book_lending` DISABLE KEYS */;
INSERT INTO `book_lending` VALUES ('2020-12-08','2020-12-23',1,10,101),('2020-12-04','2020-12-19',1,11,104),('2020-12-16','2020-12-26',2,10,105),('2020-12-06','2020-12-21',2,13,101);
/*!40000 ALTER TABLE `book_lending` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `librarybranch`
--

DROP TABLE IF EXISTS `librarybranch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `librarybranch` (
  `branchId` int NOT NULL,
  `branchName` varchar(20) DEFAULT NULL,
  `branchAddress` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`branchId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `librarybranch`
--

LOCK TABLES `librarybranch` WRITE;
/*!40000 ALTER TABLE `librarybranch` DISABLE KEYS */;
INSERT INTO `librarybranch` VALUES (10,'RR-NAGAR','BANGALORE'),(11,'RNSIT','BANGALORE'),(12,'RAJAJI-NAGAR','BANGALORE'),(13,'NITTE','MANGALORE'),(14,'MANIPAL','UDUPI');
/*!40000 ALTER TABLE `librarybranch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publisher`
--

DROP TABLE IF EXISTS `publisher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `publisher` (
  `NAME` varchar(20) NOT NULL,
  `PHONE` varchar(10) DEFAULT NULL,
  `ADDRESS` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publisher`
--

LOCK TABLES `publisher` WRITE;
/*!40000 ALTER TABLE `publisher` DISABLE KEYS */;
INSERT INTO `publisher` VALUES ('GRUPOPLANETA','7756120238','BANGALORE'),('HACHETTELIVRE','8970862340','CHENAI'),('MCGRAW-HILL','9989076587','BANGALORE'),('PEARSON','9889076565','NEWDELHI'),('RANDOMHOUSE','7455679345','HYDRABAD'),('sid pub','134','asdf');
/*!40000 ALTER TABLE `publisher` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-20  2:23:52
