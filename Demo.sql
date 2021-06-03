-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: onesimusdb
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'HR Manager');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(13,1,13),(14,1,14),(15,1,15),(16,1,16),(17,1,17),(18,1,18),(19,1,19),(20,1,20),(21,1,21),(22,1,22),(23,1,23),(24,1,24),(25,1,25),(26,1,26),(27,1,27),(28,1,28),(29,1,29),(30,1,30),(31,1,31),(32,1,32),(33,1,33),(34,1,34),(35,1,35),(36,1,36),(37,1,37),(38,1,38),(39,1,39),(40,1,40),(41,1,41),(42,1,42),(43,1,43),(44,1,44),(45,1,45),(46,1,46),(47,1,47),(48,1,48),(49,1,49),(50,1,50),(51,1,51),(52,1,52),(53,1,53),(54,1,54),(55,1,55),(56,1,56),(57,1,57),(58,1,58),(59,1,59),(60,1,60),(61,1,61),(62,1,62),(63,1,63),(64,1,64),(65,1,65),(66,1,66),(67,1,67),(68,1,68),(69,1,69),(70,1,70),(71,1,71),(72,1,72),(73,1,73),(74,1,74),(75,1,75),(76,1,76),(77,1,77),(78,1,78),(79,1,79),(80,1,80),(81,1,81),(82,1,82),(83,1,83),(84,1,84),(85,1,85),(86,1,86),(87,1,87),(88,1,88),(89,1,89),(90,1,90),(91,1,91),(92,1,92),(93,1,93),(94,1,94),(95,1,95),(96,1,96),(97,1,97),(98,1,98),(99,1,99),(100,1,100);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add child background',7,'add_childbackground'),(26,'Can change child background',7,'change_childbackground'),(27,'Can delete child background',7,'delete_childbackground'),(28,'Can view child background',7,'view_childbackground'),(29,'Can add educational background',8,'add_educationalbackground'),(30,'Can change educational background',8,'change_educationalbackground'),(31,'Can delete educational background',8,'delete_educationalbackground'),(32,'Can view educational background',8,'view_educationalbackground'),(33,'Can add emergency details',9,'add_emergencydetails'),(34,'Can change emergency details',9,'change_emergencydetails'),(35,'Can delete emergency details',9,'delete_emergencydetails'),(36,'Can view emergency details',9,'view_emergencydetails'),(37,'Can add employee personal info',10,'add_employeepersonalinfo'),(38,'Can change employee personal info',10,'change_employeepersonalinfo'),(39,'Can delete employee personal info',10,'delete_employeepersonalinfo'),(40,'Can view employee personal info',10,'view_employeepersonalinfo'),(41,'Can add employee position',11,'add_employeeposition'),(42,'Can change employee position',11,'change_employeeposition'),(43,'Can delete employee position',11,'delete_employeeposition'),(44,'Can view employee position',11,'view_employeeposition'),(45,'Can add employee position history',12,'add_employeepositionhistory'),(46,'Can change employee position history',12,'change_employeepositionhistory'),(47,'Can delete employee position history',12,'delete_employeepositionhistory'),(48,'Can view employee position history',12,'view_employeepositionhistory'),(49,'Can add employee work location',13,'add_employeeworklocation'),(50,'Can change employee work location',13,'change_employeeworklocation'),(51,'Can delete employee work location',13,'delete_employeeworklocation'),(52,'Can view employee work location',13,'view_employeeworklocation'),(53,'Can add employment history',14,'add_employmenthistory'),(54,'Can change employment history',14,'change_employmenthistory'),(55,'Can delete employment history',14,'delete_employmenthistory'),(56,'Can view employment history',14,'view_employmenthistory'),(57,'Can add family member background',15,'add_familymemberbackground'),(58,'Can change family member background',15,'change_familymemberbackground'),(59,'Can delete family member background',15,'delete_familymemberbackground'),(60,'Can view family member background',15,'view_familymemberbackground'),(61,'Can add spouse background',16,'add_spousebackground'),(62,'Can change spouse background',16,'change_spousebackground'),(63,'Can delete spouse background',16,'delete_spousebackground'),(64,'Can view spouse background',16,'view_spousebackground'),(65,'Can add document',17,'add_document'),(66,'Can change document',17,'change_document'),(67,'Can delete document',17,'delete_document'),(68,'Can view document',17,'view_document'),(69,'Can add employee',18,'add_employee'),(70,'Can change employee',18,'change_employee'),(71,'Can delete employee',18,'delete_employee'),(72,'Can view employee',18,'view_employee'),(73,'Can add timekeeping',19,'add_timekeeping'),(74,'Can change timekeeping',19,'change_timekeeping'),(75,'Can delete timekeeping',19,'delete_timekeeping'),(76,'Can view timekeeping',19,'view_timekeeping'),(77,'Can add noac',20,'add_noac'),(78,'Can change noac',20,'change_noac'),(79,'Can delete noac',20,'delete_noac'),(80,'Can view noac',20,'view_noac'),(81,'Can add major offense',21,'add_majoroffense'),(82,'Can change major offense',21,'change_majoroffense'),(83,'Can delete major offense',21,'delete_majoroffense'),(84,'Can view major offense',21,'view_majoroffense'),(85,'Can add awol',22,'add_awol'),(86,'Can change awol',22,'change_awol'),(87,'Can delete awol',22,'delete_awol'),(88,'Can view awol',22,'view_awol'),(89,'Can add awards',23,'add_awards'),(90,'Can change awards',23,'change_awards'),(91,'Can delete awards',23,'delete_awards'),(92,'Can view awards',23,'view_awards'),(93,'Can add record',24,'add_record'),(94,'Can change record',24,'change_record'),(95,'Can delete record',24,'delete_record'),(96,'Can view record',24,'view_record'),(97,'Can add notification',25,'add_notification'),(98,'Can change notification',25,'change_notification'),(99,'Can delete notification',25,'delete_notification'),(100,'Can view notification',25,'view_notification');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$216000$pe2ANyqBTTjz$Rb35jme6LxUbh/vfZfJOUDVHXG23fQpyYmmOCMkADNQ=','2021-06-02 09:42:35.539793',1,'onesimushelm','','','',1,1,'2021-03-06 11:00:16.000000'),(2,'pbkdf2_sha256$216000$9JcS0QoynbxT$sMYlCVp2h/YrVdoUN6K6gh0Hm9hwMcjAf++4amRVpwo=','2021-04-28 09:58:19.979728',0,'juandelacruz','','','',0,1,'2021-03-06 11:14:33.626347');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,1,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `awards`
--

DROP TABLE IF EXISTS `awards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `awards` (
  `aMemoReferenceNumber` int NOT NULL,
  `awardIssuer` varchar(100) NOT NULL,
  `awardPurpose` varchar(100) NOT NULL,
  `awardType` varchar(20) NOT NULL,
  PRIMARY KEY (`aMemoReferenceNumber`),
  CONSTRAINT `awards_fk` FOREIGN KEY (`aMemoReferenceNumber`) REFERENCES `record` (`memoReferenceNumber`),
  CONSTRAINT `awards_ibfk_1` FOREIGN KEY (`aMemoReferenceNumber`) REFERENCES `record` (`memoReferenceNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `awards`
--

LOCK TABLES `awards` WRITE;
/*!40000 ALTER TABLE `awards` DISABLE KEYS */;
/*!40000 ALTER TABLE `awards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `awol`
--

DROP TABLE IF EXISTS `awol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `awol` (
  `noOfOffense` int NOT NULL DEFAULT '0',
  `hearingDate` datetime DEFAULT NULL,
  `wNMemoReferenceNumber` int NOT NULL,
  PRIMARY KEY (`wNMemoReferenceNumber`),
  CONSTRAINT `awol_ibfk_1` FOREIGN KEY (`wNMemoReferenceNumber`) REFERENCES `record` (`memoReferenceNumber`),
  CONSTRAINT `awol_ibfk_2` FOREIGN KEY (`wNMemoReferenceNumber`) REFERENCES `noac` (`nMemoReferenceNumber`),
  CONSTRAINT `awol_chk_1` CHECK ((`noOfOffense` <= 100))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `awol`
--

LOCK TABLES `awol` WRITE;
/*!40000 ALTER TABLE `awol` DISABLE KEYS */;
/*!40000 ALTER TABLE `awol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `child_background`
--

DROP TABLE IF EXISTS `child_background`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `child_background` (
  `childName` varchar(100) NOT NULL,
  `childAge` int DEFAULT NULL,
  `childOccupation` varchar(20) DEFAULT NULL,
  `childId` int NOT NULL AUTO_INCREMENT,
  `informationId` int NOT NULL,
  PRIMARY KEY (`childId`),
  KEY `informationId` (`informationId`),
  CONSTRAINT `child_background_ibfk_1` FOREIGN KEY (`informationId`) REFERENCES `employee_personal_info` (`informationId`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `child_background`
--

LOCK TABLES `child_background` WRITE;
/*!40000 ALTER TABLE `child_background` DISABLE KEYS */;
INSERT INTO `child_background` VALUES ('Juana Dela Cruz',5,'Child',30,14),('Tori Spec',15,'Student',31,16),('Orit Spec',13,'Student',32,16);
/*!40000 ALTER TABLE `child_background` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=139 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-03-06 11:14:33.738124','2','juandelacruz',1,'[{\"added\": {}}]',4,1),(2,'2021-04-27 11:17:59.123705','1','Service , Cashier',1,'[{\"added\": {}}]',11,1),(3,'2021-04-28 13:26:14.200577','2','2',3,'',9,1),(4,'2021-04-28 13:26:16.709435','12','12',3,'',9,1),(5,'2021-04-28 13:26:19.299347','13','13',3,'',9,1),(6,'2021-04-28 13:26:21.470880','14','14',3,'',9,1),(7,'2021-04-28 13:26:24.003861','15','15',3,'',9,1),(8,'2021-04-28 13:26:26.185888','123','123',3,'',9,1),(9,'2021-04-28 13:26:28.818758','456','456',3,'',9,1),(10,'2021-04-28 13:26:56.381198','4','Juan Dela Cruz2 id = 4',3,'',10,1),(11,'2021-04-29 06:43:40.984399','1','Record object (1)',1,'[{\"added\": {}}]',24,1),(12,'2021-04-29 06:43:57.452890','1','Document object (1)',1,'[{\"added\": {}}]',17,1),(13,'2021-06-02 07:49:35.373495','1','HR Manager',1,'[{\"added\": {}}]',3,1),(14,'2021-06-02 07:49:46.651123','1','onesimushelm',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(15,'2021-06-02 08:06:02.679950','12','Awards object (12)',3,'',23,1),(16,'2021-06-02 08:06:11.698780','3','Timekeeping object (3)',3,'',19,1),(17,'2021-06-02 08:06:17.205515','3','Noac object (3)',3,'',20,1),(18,'2021-06-02 08:06:23.532594','2','Document object (2)',3,'',17,1),(19,'2021-06-02 08:06:26.405385','3','Document object (3)',3,'',17,1),(20,'2021-06-02 08:06:29.749715','4','Document object (4)',3,'',17,1),(21,'2021-06-03 06:57:26.199419','1','EmployeePositionHistory object (1)',3,'',12,1),(22,'2021-06-03 06:57:28.954096','2','EmployeePositionHistory object (2)',3,'',12,1),(23,'2021-06-03 06:59:31.842071','52423','Awol object (52423)',3,'',22,1),(24,'2021-06-03 06:59:35.610845','1234','Awards object (1234)',3,'',23,1),(25,'2021-06-03 06:59:37.836930','13125','Awards object (13125)',3,'',23,1),(26,'2021-06-03 06:59:50.971281','2323','Timekeeping object (2323)',3,'',19,1),(27,'2021-06-03 06:59:57.330410','2323','Noac object (2323)',3,'',20,1),(28,'2021-06-03 06:59:59.505177','52423','Noac object (52423)',3,'',20,1),(29,'2021-06-03 07:00:04.378426','1','Record object (1)',3,'',24,1),(30,'2021-06-03 07:00:07.172453','3','Record object (3)',3,'',24,1),(31,'2021-06-03 07:00:10.705921','12','Record object (12)',3,'',24,1),(33,'2021-06-03 07:00:23.376825','12','Document object (12)',3,'',17,1),(34,'2021-06-03 07:00:26.171551','11','Document object (11)',3,'',17,1),(35,'2021-06-03 07:00:29.345516','10','Document object (10)',3,'',17,1),(36,'2021-06-03 07:00:33.009165','9','Document object (9)',3,'',17,1),(37,'2021-06-03 07:00:36.325145','8','Document object (8)',3,'',17,1),(38,'2021-06-03 07:00:39.218497','7','Document object (7)',3,'',17,1),(39,'2021-06-03 07:00:42.185860','6','Document object (6)',3,'',17,1),(40,'2021-06-03 07:00:45.698691','5','Document object (5)',3,'',17,1),(41,'2021-06-03 07:01:13.874390','1234','Record object (1234)',3,'',24,1),(42,'2021-06-03 07:01:16.337194','13125','Record object (13125)',3,'',24,1),(43,'2021-06-03 07:01:18.844346','2323','Record object (2323)',3,'',24,1),(44,'2021-06-03 07:01:22.112170','52423','Record object (52423)',3,'',24,1),(45,'2021-06-03 07:01:51.291134','25','id= 25, John Dela Cruz Jr. child of Bob',3,'',7,1),(46,'2021-06-03 07:01:51.302118','24','id= 24, John Dela Cruz child of Bob',3,'',7,1),(47,'2021-06-03 07:01:51.309117','23','id= 23, John Dela Cruz Jr. child of Juan Dela Cruz Sas',3,'',7,1),(48,'2021-06-03 07:01:51.317065','22','id= 22, John Dela Cruz child of Juan Dela Cruz Sas',3,'',7,1),(49,'2021-06-03 07:01:51.325044','17','id= 17, John Dela Cruz Sr. child of Juan Dela Cruz Was',3,'',7,1),(50,'2021-06-03 07:01:51.332026','16','id= 16, John Dela Cruz Jr. child of Juan Dela Cruz Was',3,'',7,1),(51,'2021-06-03 07:01:51.340028','15','id= 15, John Dela Cruz child of Juan Dela Cruz Was',3,'',7,1),(52,'2021-06-03 07:01:51.347010','14','id= 14, John Dela Cruz Rr. child of Juan Dela Cruz WWE',3,'',7,1),(53,'2021-06-03 07:01:51.355092','13','id= 13, John Dela Cruz Xr. child of Juan Dela Cruz WWE',3,'',7,1),(54,'2021-06-03 07:01:51.362352','12','id= 12, John Dela Cruz Sr. child of Juan Dela Cruz WWE',3,'',7,1),(55,'2021-06-03 07:01:51.369817','11','id= 11, John Dela Cruz Jr. child of Juan Dela Cruz WWE',3,'',7,1),(56,'2021-06-03 07:01:51.377212','10','id= 10, John Dela Cruz child of Juan Dela Cruz WWE',3,'',7,1),(57,'2021-06-03 07:01:51.384328','8','id= 8, John Dela Cruz Jr child of Juan Dela Cruz3',3,'',7,1),(58,'2021-06-03 07:01:51.392418','7','id= 7, Juana Dela Cruz child of Juan Dela Cruz3',3,'',7,1),(59,'2021-06-03 07:01:51.400390','4','id= 4, John Dela Cruz child of Juan Dela Cruz',3,'',7,1),(60,'2021-06-03 07:02:01.199740','19','id= 19, Bob studied at XE with degree of Grade School',3,'',8,1),(61,'2021-06-03 07:02:01.208250','18','id= 18, Juan Dela Cruz Sas studied at XE with degree of Grade School',3,'',8,1),(62,'2021-06-03 07:02:01.215101','17','id= 17, Juan Dela Cruz Sas studied at Ateneo with degree of College',3,'',8,1),(63,'2021-06-03 07:02:01.223357','15','id= 15, Juan Dela Cruz Was studied at Ateneo HS with degree of High School',3,'',8,1),(64,'2021-06-03 07:02:01.230860','14','id= 14, Juan Dela Cruz Was studied at Ateneo with degree of College',3,'',8,1),(65,'2021-06-03 07:02:01.238521','13','id= 13, Juan Dela Cruz WWE studied at Ateneo GS with degree of Grade School',3,'',8,1),(66,'2021-06-03 07:02:01.246272','12','id= 12, Juan Dela Cruz WWE studied at Ateneo HS with degree of High School',3,'',8,1),(67,'2021-06-03 07:02:01.254028','11','id= 11, Juan Dela Cruz WWE studied at Ateneo with degree of College',3,'',8,1),(68,'2021-06-03 07:02:01.261627','10','id= 10, Juan Dela Cruz3 studied at Ateneo GS with degree of Grade School',3,'',8,1),(69,'2021-06-03 07:02:01.269354','8','id= 8, Juan Dela Cruz3 studied at Ateneo HS with degree of High School',3,'',8,1),(70,'2021-06-03 07:02:01.276558','7','id= 7, Juan Dela Cruz3 studied at Ateneo with degree of College',3,'',8,1),(71,'2021-06-03 07:02:01.284341','6','id= 6, Juan Dela Cruz studied at Ateneo GS with degree of Grade School',3,'',8,1),(72,'2021-06-03 07:02:01.292139','5','id= 5, Juan Dela Cruz studied at Ateneo HS with degree of High School',3,'',8,1),(73,'2021-06-03 07:02:01.299119','4','id= 4, Juan Dela Cruz studied at Ateneo with degree of College',3,'',8,1),(74,'2021-06-03 07:02:22.217145','12','Bob id = 12',3,'',10,1),(75,'2021-06-03 07:02:22.225774','11','Juan Dela Cruz Sas id = 11',3,'',10,1),(76,'2021-06-03 07:02:22.233500','10','Juan Dela Cruz Sas id = 10',3,'',10,1),(77,'2021-06-03 07:02:22.241690','6','Juan Dela Cruz Was id = 6',3,'',10,1),(78,'2021-06-03 07:02:22.249679','5','Juan Dela Cruz WWE id = 5',3,'',10,1),(79,'2021-06-03 07:02:22.287742','3','Juan Dela Cruz3 id = 3',3,'',10,1),(80,'2021-06-03 07:02:22.295869','2','Juan Dela Cruz id = 2',3,'',10,1),(81,'2021-06-03 07:02:41.424234','26','id= 26, as Previously worked at as',3,'',14,1),(82,'2021-06-03 07:02:41.435480','22','id= 22, Bob Previously worked at H23',3,'',14,1),(83,'2021-06-03 07:02:41.443491','21','id= 21, Bob Previously worked at Cruz4',3,'',14,1),(84,'2021-06-03 07:02:41.451231','20','id= 20, Juan Dela Cruz Sas Previously worked at Cruz4',3,'',14,1),(85,'2021-06-03 07:02:41.461304','19','id= 19, Juan Dela Cruz Sas Previously worked at Cruz4',3,'',14,1),(86,'2021-06-03 07:02:41.472137','17','id= 17, Juan Dela Cruz Was Previously worked at Ateneo HS',3,'',14,1),(87,'2021-06-03 07:02:41.483211','16','id= 16, Juan Dela Cruz Was Previously worked at Cruz4',3,'',14,1),(88,'2021-06-03 07:02:41.490507','15','id= 15, Juan Dela Cruz WWE Previously worked at Ateneo GSsa',3,'',14,1),(89,'2021-06-03 07:02:41.501234','14','id= 14, Juan Dela Cruz WWE Previously worked at Ateneo College',3,'',14,1),(90,'2021-06-03 07:02:41.510134','13','id= 13, Juan Dela Cruz WWE Previously worked at Ateneo HS',3,'',14,1),(91,'2021-06-03 07:02:41.518194','12','id= 12, Juan Dela Cruz WWE Previously worked at Cruz4',3,'',14,1),(92,'2021-06-03 07:02:41.526318','11','id= 11, Juan Dela Cruz3 Previously worked at Ateneo GS',3,'',14,1),(93,'2021-06-03 07:02:41.533565','7','id= 7, Juan Dela Cruz3 Previously worked at Ateneo GS',3,'',14,1),(94,'2021-06-03 07:02:41.541329','5','id= 5, Juan Dela Cruz Previously worked at Ateneo HS',3,'',14,1),(95,'2021-06-03 07:02:41.549343','4','id= 4, Juan Dela Cruz Previously worked at Ateneo GS',3,'',14,1),(96,'2021-06-03 07:02:47.246870','18','id= 18, Juana Dela Cruz family member of Bob',3,'',15,1),(97,'2021-06-03 07:02:47.257916','17','id= 17, Juana Dela Cruz family member of Juan Dela Cruz Sas',3,'',15,1),(98,'2021-06-03 07:02:47.266461','16','id= 16, Juana Dela Cruz family member of Juan Dela Cruz Sas',3,'',15,1),(99,'2021-06-03 07:02:47.274271','14','id= 14, John Dela Cruz family member of Juan Dela Cruz Was',3,'',15,1),(100,'2021-06-03 07:02:47.282510','13','id= 13, Juana Dela Cruz family member of Juan Dela Cruz Was',3,'',15,1),(101,'2021-06-03 07:02:47.289968','12','id= 12, John Dela Cruz family member of Juan Dela Cruz WWE',3,'',15,1),(102,'2021-06-03 07:02:47.297655','11','id= 11, Juana Dela Cruz family member of Juan Dela Cruz WWE',3,'',15,1),(103,'2021-06-03 07:02:47.305608','8','id= 8, John Dela Cruz family member of Juan Dela Cruz3',3,'',15,1),(104,'2021-06-03 07:02:47.312833','7','id= 7, Juana Dela Cruz family member of Juan Dela Cruz3',3,'',15,1),(105,'2021-06-03 07:02:47.321158','5','id= 5, John Dela Cruz family member of Juan Dela Cruz',3,'',15,1),(106,'2021-06-03 07:02:47.328356','4','id= 4, Juana Dela Cruz family member of Juan Dela Cruz',3,'',15,1),(107,'2021-06-03 07:03:02.622240','5','Juan Spouse Cruz2, id = 5',3,'',16,1),(108,'2021-06-03 07:03:02.633309','4','Juan Spouse Cruz Xxl, id = 4',3,'',16,1),(109,'2021-06-03 07:03:02.641623','3','Juan Spouse Cruz Xxl, id = 3',3,'',16,1),(110,'2021-06-03 07:03:02.649261','2','Juan Spouse Cruz, id = 2',3,'',16,1),(111,'2021-06-03 07:03:19.336119','12','Bob id = 12',3,'',10,1),(112,'2021-06-03 07:03:19.347264','11','Juan Dela Cruz Sas id = 11',3,'',10,1),(113,'2021-06-03 07:03:19.354338','10','Juan Dela Cruz Sas id = 10',3,'',10,1),(114,'2021-06-03 07:03:19.366081','6','Juan Dela Cruz Was id = 6',3,'',10,1),(115,'2021-06-03 07:03:19.373231','5','Juan Dela Cruz WWE id = 5',3,'',10,1),(116,'2021-06-03 07:03:19.382292','3','Juan Dela Cruz3 id = 3',3,'',10,1),(117,'2021-06-03 07:03:19.389544','2','Juan Dela Cruz id = 2',3,'',10,1),(118,'2021-06-03 07:03:27.821801','5','Juan Spouse Cruz2, id = 5',3,'',16,1),(119,'2021-06-03 07:03:27.832950','4','Juan Spouse Cruz Xxl, id = 4',3,'',16,1),(120,'2021-06-03 07:03:27.840771','3','Juan Spouse Cruz Xxl, id = 3',3,'',16,1),(121,'2021-06-03 07:03:27.847897','2','Juan Spouse Cruz, id = 2',3,'',16,1),(122,'2021-06-03 07:03:39.568155','2','2',3,'',9,1),(123,'2021-06-03 07:03:39.578618','19','19',3,'',9,1),(124,'2021-06-03 07:03:39.586373','1','1',3,'',9,1),(125,'2021-06-03 07:03:44.492549','3145','3145',3,'',9,1),(126,'2021-06-03 07:34:14.576287','2','HR , Manager',1,'[{\"added\": {}}]',11,1),(127,'2021-06-03 07:34:20.395962','3','Service , Manager',1,'[{\"added\": {}}]',11,1),(128,'2021-06-03 07:35:44.218889','3','Store , Manager',2,'[{\"changed\": {\"fields\": [\"Department\"]}}]',11,1),(129,'2021-06-03 07:36:19.197676','4','HR , Staff',1,'[{\"added\": {}}]',11,1),(130,'2021-06-03 07:37:18.555529','5','HR , Training Officer',1,'[{\"added\": {}}]',11,1),(131,'2021-06-03 07:37:55.068904','6','Store , Supervisor',1,'[{\"added\": {}}]',11,1),(132,'2021-06-03 07:38:17.947777','7','Sales , Associates',1,'[{\"added\": {}}]',11,1),(133,'2021-06-03 07:38:29.713939','8','Logistics , Helper',1,'[{\"added\": {}}]',11,1),(134,'2021-06-03 07:38:40.970073','9','Logistics , Assistant',1,'[{\"added\": {}}]',11,1),(135,'2021-06-03 07:39:05.738381','1','Store , Cashier',2,'[{\"changed\": {\"fields\": [\"Department\"]}}]',11,1),(136,'2021-06-03 07:39:44.238174','Onesimus Main Office','NCR , Onesimus Main Office',2,'[{\"changed\": {\"fields\": [\"Branch\"]}}]',13,1),(137,'2021-06-03 07:40:11.163160','SM Test','NCR , SM Test',3,'',13,1),(138,'2021-06-03 08:32:34.131346','8',', id = 8',3,'',16,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(23,'loginapp','awards'),(22,'loginapp','awol'),(7,'loginapp','childbackground'),(17,'loginapp','document'),(8,'loginapp','educationalbackground'),(9,'loginapp','emergencydetails'),(18,'loginapp','employee'),(10,'loginapp','employeepersonalinfo'),(11,'loginapp','employeeposition'),(12,'loginapp','employeepositionhistory'),(13,'loginapp','employeeworklocation'),(14,'loginapp','employmenthistory'),(15,'loginapp','familymemberbackground'),(21,'loginapp','majoroffense'),(20,'loginapp','noac'),(24,'loginapp','record'),(16,'loginapp','spousebackground'),(19,'loginapp','timekeeping'),(25,'notifications','notification'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-03-06 10:59:29.333925'),(2,'auth','0001_initial','2021-03-06 10:59:29.796832'),(3,'admin','0001_initial','2021-03-06 10:59:31.035477'),(4,'admin','0002_logentry_remove_auto_add','2021-03-06 10:59:31.305162'),(5,'admin','0003_logentry_add_action_flag_choices','2021-03-06 10:59:31.323741'),(6,'contenttypes','0002_remove_content_type_name','2021-03-06 10:59:31.680890'),(7,'auth','0002_alter_permission_name_max_length','2021-03-06 10:59:32.028789'),(8,'auth','0003_alter_user_email_max_length','2021-03-06 10:59:32.063527'),(9,'auth','0004_alter_user_username_opts','2021-03-06 10:59:32.076741'),(10,'auth','0005_alter_user_last_login_null','2021-03-06 10:59:32.179057'),(11,'auth','0006_require_contenttypes_0002','2021-03-06 10:59:32.187065'),(12,'auth','0007_alter_validators_add_error_messages','2021-03-06 10:59:32.199743'),(13,'auth','0008_alter_user_username_max_length','2021-03-06 10:59:32.293992'),(14,'auth','0009_alter_user_last_name_max_length','2021-03-06 10:59:32.391042'),(15,'auth','0010_alter_group_name_max_length','2021-03-06 10:59:32.431148'),(16,'auth','0011_update_proxy_permissions','2021-03-06 10:59:32.443488'),(17,'auth','0012_alter_user_first_name_max_length','2021-03-06 10:59:32.886613'),(18,'sessions','0001_initial','2021-03-06 10:59:33.070836'),(19,'loginapp','0001_initial','2021-03-06 11:11:38.773280'),(20,'notifications','0001_initial','2021-06-02 07:48:20.761919'),(21,'notifications','0002_auto_20150224_1134','2021-06-02 07:48:21.510203'),(22,'notifications','0003_notification_data','2021-06-02 07:48:21.568048'),(23,'notifications','0004_auto_20150826_1508','2021-06-02 07:48:21.583008'),(24,'notifications','0005_auto_20160504_1520','2021-06-02 07:48:21.598022'),(25,'notifications','0006_indexes','2021-06-02 07:48:21.944767'),(26,'notifications','0007_add_timestamp_index','2021-06-02 07:48:22.008596'),(27,'notifications','0008_index_together_recipient_unread','2021-06-02 07:48:22.080432');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('73k4jn7fyoqtl4ll2gjr2a6rnfzpaejk','.eJxVjDsOwjAQBe_iGln-Zh1Kes5geb1rHECxFCcV4u4QKQW0b2beS8S0rTVunZc4kTgLLU6_G6b84HkHdE_zrcnc5nWZUO6KPGiX10b8vBzu30FNvX5rF0hpYkcjOA0GudiBPJQxBzN4Z6AgKavKyAZ9tj4oYItQUiA0AEq8P9sZN7M:1lIUy8:FA7ttgv8I3R8fOnoMjqJbvaeLKKhmKrb2ebcXzurhjU','2021-03-20 11:19:36.295827'),('qugiiqkh8m930b32hvqqsqvv8yjr5j5t','.eJxVjDsOwjAQBe_iGln-Zh1Kes5geb1rHECxFCcV4u4QKQW0b2beS8S0rTVunZc4kTgLLU6_G6b84HkHdE_zrcnc5nWZUO6KPGiX10b8vBzu30FNvX5rF0hpYkcjOA0GudiBPJQxBzN4Z6AgKavKyAZ9tj4oYItQUiA0AEq8P9sZN7M:1liWEE:1et-7KLQYxH1ProZsLbJTBKIcLjT8-jQLRcKLOof9yw','2021-05-31 05:55:46.236159'),('x3twk6v01hn0hk81znh1xoekezt1cah0','.eJxVjEEOwiAQRe_C2hBmHARcuvcMhBlAqqZNSrsy3l2bdKHb_977LxXTurS49jLHIauzQnX43TjJo4wbyPc03iYt07jMA-tN0Tvt-jrl8rzs7t9BS719a2fBkaATqKZCQQ4BqHqs5I4o5QToLXEgzzaxT14YqwGDQM5mKqLeH8WANz4:1lbgxX:X98kV_QKqMoRrzcoZOF-J3y0quf1LGpl5GPqS1RCefQ','2021-05-12 09:58:19.983718');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `document`
--

DROP TABLE IF EXISTS `document`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `document` (
  `documentId` int NOT NULL AUTO_INCREMENT,
  `documentName` varchar(100) NOT NULL,
  `documentlink` varchar(255) NOT NULL,
  `dateAndTimeCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `author` varchar(50) NOT NULL,
  `dateAndTimeLastEdited` datetime DEFAULT CURRENT_TIMESTAMP,
  `recentEditor` varchar(50) DEFAULT NULL,
  `employeeId` int NOT NULL,
  `preparedBy` varchar(100) NOT NULL,
  `preparationDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `notedBy` varchar(100) NOT NULL,
  `notedDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `approvedBy` varchar(100) NOT NULL,
  `approvedDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `receivedBy` varchar(100) NOT NULL,
  `receivedDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `memoReferenceNumber` int DEFAULT NULL,
  `documenthide` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`documentId`),
  KEY `employeeId` (`employeeId`),
  KEY `memoReferenceNumber` (`memoReferenceNumber`),
  CONSTRAINT `document_ibfk_1` FOREIGN KEY (`employeeId`) REFERENCES `employee` (`employeeId`),
  CONSTRAINT `document_ibfk_2` FOREIGN KEY (`memoReferenceNumber`) REFERENCES `record` (`memoReferenceNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document`
--

LOCK TABLES `document` WRITE;
/*!40000 ALTER TABLE `document` DISABLE KEYS */;
/*!40000 ALTER TABLE `document` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `educational_background`
--

DROP TABLE IF EXISTS `educational_background`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `educational_background` (
  `highestDegree` varchar(20) DEFAULT NULL,
  `schoolName` varchar(100) NOT NULL,
  `startingYearAttended` date NOT NULL,
  `endingYearAttended` date NOT NULL,
  `schoolType` varchar(15) NOT NULL DEFAULT 'Elementary',
  `informationId` int NOT NULL,
  `degreeId` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`degreeId`),
  KEY `informationId` (`informationId`),
  CONSTRAINT `educational_background_ibfk_1` FOREIGN KEY (`informationId`) REFERENCES `employee_personal_info` (`informationId`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `educational_background`
--

LOCK TABLES `educational_background` WRITE;
/*!40000 ALTER TABLE `educational_background` DISABLE KEYS */;
INSERT INTO `educational_background` VALUES ('High School','Ateneo High School','1988-01-22','1994-01-22','High School',14,23),('High School','Ateneo Grade School','1977-01-22','1988-01-22','Grade School',14,24),('Grade School','Ateneo','1978-06-01','1987-06-01','Grade School',15,25),('College','Miriam','1985-06-01','1990-06-02','College',16,26),('College','Miriam','1981-06-01','1985-06-01','High School',16,27),('College','Miriam','1975-06-01','1981-06-01','Grade School',16,28),('College','Miriam','2006-05-29','2014-05-26','College',17,29),('College','Miriam','2000-05-29','2005-05-30','High School',17,30),('College','Miriam','1990-05-28','2000-05-29','Grade School',17,31);
/*!40000 ALTER TABLE `educational_background` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emergency_details`
--

DROP TABLE IF EXISTS `emergency_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emergency_details` (
  `emergencyContactNumber` varchar(20) NOT NULL,
  `emergencyContactName` varchar(100) NOT NULL,
  `emergencyRelationship` varchar(20) DEFAULT NULL,
  `emergencyAddress` varchar(255) NOT NULL,
  PRIMARY KEY (`emergencyContactNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emergency_details`
--

LOCK TABLES `emergency_details` WRITE;
/*!40000 ALTER TABLE `emergency_details` DISABLE KEYS */;
INSERT INTO `emergency_details` VALUES ('09175995999','Juan Emergency Cruz','Brother','592 Cordillera Street, Brgy. Malamig, Mandaluyong City'),('0917869230','Bob Rock Cruz','Father','Fairview Terraces, Ayala Malls, Brgy. Pasong Putik, Novaliches, Quezon City'),('09187231213','Ariel Emergency','Guardian','592 Cordillera Street, Brgy. Malamig, Mandaluyong City'),('09187922332','Estaban Emergency','Guardian','592 Cordillera Street, Brgy. Malamig, Mandaluyong City'),('09187923013','Emergency Contacter','Guardian','592 Cordillera Street, Brgy. Malamig, Mandaluyong City');
/*!40000 ALTER TABLE `emergency_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `employeeId` int NOT NULL,
  `branch` varchar(20) DEFAULT NULL,
  `startDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `endDate` datetime DEFAULT NULL,
  `employmentStatus` varchar(15) NOT NULL DEFAULT 'Probationary',
  `salaryType` varchar(10) NOT NULL DEFAULT 'Monthly',
  `salary` float(10,2) NOT NULL DEFAULT '0.00',
  `jobId` int DEFAULT NULL,
  `informationId` int NOT NULL,
  `deletehide` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`employeeId`),
  KEY `branch` (`branch`),
  KEY `jobId` (`jobId`),
  KEY `informationId` (`informationId`),
  CONSTRAINT `employee_ibfk_5` FOREIGN KEY (`branch`) REFERENCES `employee_work_location` (`branch`),
  CONSTRAINT `employee_ibfk_6` FOREIGN KEY (`jobId`) REFERENCES `employee_position` (`jobId`),
  CONSTRAINT `employee_ibfk_7` FOREIGN KEY (`informationId`) REFERENCES `employee_personal_info` (`informationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'Festival Mall','2000-10-01 16:00:00',NULL,'Probationary','Daily',500.00,1,14,0),(2,'Factory Outlet','2017-04-24 16:00:00',NULL,'Probationary','Monthly',500.00,7,15,0),(3,'Onesimus Main Office','1990-08-02 16:00:00',NULL,'Probationary','Monthly',30000.00,2,16,0),(4,'Factory Outlet','2019-06-02 16:00:00',NULL,'Probationary','Monthly',15000.00,3,17,0),(5,'Glorietta','2021-06-02 16:00:00',NULL,'Probationary','Monthly',500.00,7,18,0);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_personal_info`
--

DROP TABLE IF EXISTS `employee_personal_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_personal_info` (
  `employeeName` varchar(100) NOT NULL,
  `emergencyContactNumber` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `birthDate` date NOT NULL,
  `civilStatus` varchar(10) NOT NULL,
  `citizenship` varchar(20) NOT NULL,
  `religion` varchar(20) DEFAULT NULL,
  `bloodType` varchar(10) NOT NULL DEFAULT 'Unknown',
  `numberOfDependent` int NOT NULL DEFAULT '0',
  `presentAddress` varchar(255) NOT NULL,
  `permanentAddress` varchar(255) NOT NULL,
  `contactNumber` varchar(20) NOT NULL,
  `spouseId` int DEFAULT NULL,
  `informationId` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`informationId`),
  KEY `emergencyContactNumber` (`emergencyContactNumber`),
  KEY `spouseId` (`spouseId`),
  CONSTRAINT `employee_personal_info_ibfk_2` FOREIGN KEY (`emergencyContactNumber`) REFERENCES `emergency_details` (`emergencyContactNumber`),
  CONSTRAINT `employee_personal_info_ibfk_3` FOREIGN KEY (`spouseId`) REFERENCES `spouse_background` (`spouseId`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_personal_info`
--

LOCK TABLES `employee_personal_info` WRITE;
/*!40000 ALTER TABLE `employee_personal_info` DISABLE KEYS */;
INSERT INTO `employee_personal_info` VALUES ('Juan Dela Cruz','09175995999','Male','1970-05-31','Single','Filipino','Catholic','O-',4,'Katipunan Ave, Quezon City, 1108 Metro Manila','Katipunan Ave, Quezon City, 1108 Metro Manila','09179999999',7,14),('Bob Cruz','0917869230','Male','1970-06-08','Single','Filipino','Catholic','O-',2,'Fairview Terraces, Ayala Malls, Brgy. Pasong Putik, Novaliches, Quezon City','Fairview Terraces, Ayala Malls, Brgy. Pasong Putik, Novaliches, Quezon City','0918762918',NULL,15),('Manager Toriel Spec','09187923013','Female','1969-05-05','Married','Filipino','Catholic','OA-',3,'592 Cordillera Street, Brgy. Malamig, Mandaluyong City','592 Cordillera Street, Brgy. Malamig, Mandaluyong City','09189586910',9,16),('Ariel Uriel','09187231213','Female','1972-06-05','Single','Filipino','Catholic','O+',1,'592 Cordillera Street, Brgy. Malamig, Mandaluyong City','592 Cordillera Street, Brgy. Malamig, Mandaluyong City','09189582310',NULL,17),('Junior Esteban','09187922332','Male','1986-06-02','Single','Filipino','Catholic','AB+',0,'592 Cordillera Street, Brgy. Malamig, Mandaluyong City','592 Cordillera Street, Brgy. Malamig, Mandaluyong City','091895123122',NULL,18);
/*!40000 ALTER TABLE `employee_personal_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_position`
--

DROP TABLE IF EXISTS `employee_position`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_position` (
  `position` varchar(20) NOT NULL,
  `jobId` int NOT NULL AUTO_INCREMENT,
  `department` varchar(20) NOT NULL,
  PRIMARY KEY (`jobId`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_position`
--

LOCK TABLES `employee_position` WRITE;
/*!40000 ALTER TABLE `employee_position` DISABLE KEYS */;
INSERT INTO `employee_position` VALUES ('Cashier',1,'Store'),('Manager',2,'HR'),('Manager',3,'Store'),('Staff',4,'HR'),('Training Officer',5,'HR'),('Supervisor',6,'Store'),('Associates',7,'Sales'),('Helper',8,'Logistics'),('Assistant',9,'Logistics');
/*!40000 ALTER TABLE `employee_position` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_position_history`
--

DROP TABLE IF EXISTS `employee_position_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_position_history` (
  `previousDepartment` varchar(20) NOT NULL,
  `previousPosition_One` varchar(20) NOT NULL,
  `previousBranch` varchar(20) NOT NULL,
  `year` year NOT NULL,
  `employeeId` int NOT NULL,
  `pastPositionId` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`pastPositionId`),
  KEY `employeeHistory_fk` (`employeeId`),
  CONSTRAINT `employeeHistory_fk` FOREIGN KEY (`employeeId`) REFERENCES `employee` (`employeeId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_position_history`
--

LOCK TABLES `employee_position_history` WRITE;
/*!40000 ALTER TABLE `employee_position_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee_position_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_work_location`
--

DROP TABLE IF EXISTS `employee_work_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_work_location` (
  `branch` varchar(20) NOT NULL,
  `region` varchar(20) NOT NULL,
  PRIMARY KEY (`branch`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_work_location`
--

LOCK TABLES `employee_work_location` WRITE;
/*!40000 ALTER TABLE `employee_work_location` DISABLE KEYS */;
INSERT INTO `employee_work_location` VALUES ('Factory Outlet','NCR'),('Festival Mall','NCR'),('Glorietta','NCR'),('Mall of Asia','NCR'),('Market! Market!','NCR'),('Onesimus Main Office','NCR'),('Robinson Galleria','NCR'),('SM Bicutan','NCR'),('SM Marikina','NCR'),('SM Megamall','NCR'),('SM North Edsa','NCR');
/*!40000 ALTER TABLE `employee_work_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employment_history`
--

DROP TABLE IF EXISTS `employment_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employment_history` (
  `previousCompanyName` varchar(100) NOT NULL,
  `previousPosition` varchar(20) DEFAULT NULL,
  `reasonForLeaving` varchar(255) DEFAULT NULL,
  `companyContactNumber` varchar(20) DEFAULT NULL,
  `withCOEorClearance` varchar(10) NOT NULL,
  `employmentHistoryId` int NOT NULL AUTO_INCREMENT,
  `informationId` int NOT NULL,
  PRIMARY KEY (`employmentHistoryId`),
  KEY `informationId` (`informationId`),
  CONSTRAINT `employment_history_ibfk_1` FOREIGN KEY (`informationId`) REFERENCES `employee_personal_info` (`informationId`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employment_history`
--

LOCK TABLES `employment_history` WRITE;
/*!40000 ALTER TABLE `employment_history` DISABLE KEYS */;
INSERT INTO `employment_history` VALUES ('Ateneo GS','Teacher','Wanted to look for a new job.','02 8426 6001','WithCOE',27,14),('Loyola Schools','Manager','Better pay.','02 8426 6001','WithCOE',28,16),('SM','Manager','Better pay.','02 8926 4776','WithCOE',29,16),('Loyola Schools','Manager','Better pay.','02 8426 6001','WithCOE',30,17);
/*!40000 ALTER TABLE `employment_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `family_member_background`
--

DROP TABLE IF EXISTS `family_member_background`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `family_member_background` (
  `memberName` varchar(100) NOT NULL,
  `memberAge` int DEFAULT NULL,
  `memberRelationship` varchar(20) NOT NULL DEFAULT 'Mother',
  `memberOccupation` varchar(20) DEFAULT NULL,
  `familyId` int NOT NULL AUTO_INCREMENT,
  `informationId` int NOT NULL,
  PRIMARY KEY (`familyId`),
  KEY `informationId` (`informationId`),
  CONSTRAINT `family_member_background_ibfk_1` FOREIGN KEY (`informationId`) REFERENCES `employee_personal_info` (`informationId`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `family_member_background`
--

LOCK TABLES `family_member_background` WRITE;
/*!40000 ALTER TABLE `family_member_background` DISABLE KEYS */;
INSERT INTO `family_member_background` VALUES ('Juana Dela Cruz',89,'Mother','Retired',23,14),('John Dela Cruz',89,'Father','Retired',24,14),('Bob Rock Cruz',76,'Father','Retired',25,15),('Bobella Rock',73,'Mother','Retired',26,15),('Torias Spec',98,'Father','Deceased',27,16),('Torielas Spec',98,'Mother','Deceased',28,16),('Ariel Desriel',88,'Mother','Retired',29,17),('Marian Esteban',65,'Mother','Deceased',30,18),('Bob Estaban',60,'Father','Deceased',31,18);
/*!40000 ALTER TABLE `family_member_background` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `major_offense`
--

DROP TABLE IF EXISTS `major_offense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `major_offense` (
  `hearingDate` datetime DEFAULT NULL,
  `mNMemoReferenceNumber` int NOT NULL,
  PRIMARY KEY (`mNMemoReferenceNumber`),
  CONSTRAINT `major_offense_ibfk_1` FOREIGN KEY (`mNMemoReferenceNumber`) REFERENCES `record` (`memoReferenceNumber`),
  CONSTRAINT `major_offense_ibfk_2` FOREIGN KEY (`mNMemoReferenceNumber`) REFERENCES `noac` (`nMemoReferenceNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `major_offense`
--

LOCK TABLES `major_offense` WRITE;
/*!40000 ALTER TABLE `major_offense` DISABLE KEYS */;
/*!40000 ALTER TABLE `major_offense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `noac`
--

DROP TABLE IF EXISTS `noac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `noac` (
  `nMemoReferenceNumber` int NOT NULL,
  `remarks` text,
  `noacType` varchar(15) NOT NULL DEFAULT 'Timekeeping',
  `sanction` varchar(100) NOT NULL,
  PRIMARY KEY (`nMemoReferenceNumber`),
  CONSTRAINT `noac_fk` FOREIGN KEY (`nMemoReferenceNumber`) REFERENCES `record` (`memoReferenceNumber`),
  CONSTRAINT `noac_ibfk_1` FOREIGN KEY (`nMemoReferenceNumber`) REFERENCES `record` (`memoReferenceNumber`),
  CONSTRAINT `noac_chk_1` CHECK ((`noacType` in (_utf8mb4'Timekeeping',_utf8mb4'AWOL',_utf8mb4'Major')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `noac`
--

LOCK TABLES `noac` WRITE;
/*!40000 ALTER TABLE `noac` DISABLE KEYS */;
/*!40000 ALTER TABLE `noac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifications_notification`
--

DROP TABLE IF EXISTS `notifications_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notifications_notification` (
  `id` int NOT NULL AUTO_INCREMENT,
  `level` varchar(20) NOT NULL,
  `unread` tinyint(1) NOT NULL,
  `actor_object_id` varchar(255) NOT NULL,
  `verb` varchar(255) NOT NULL,
  `description` longtext,
  `target_object_id` varchar(255) DEFAULT NULL,
  `action_object_object_id` varchar(255) DEFAULT NULL,
  `timestamp` datetime(6) NOT NULL,
  `public` tinyint(1) NOT NULL,
  `action_object_content_type_id` int DEFAULT NULL,
  `actor_content_type_id` int NOT NULL,
  `recipient_id` int NOT NULL,
  `target_content_type_id` int DEFAULT NULL,
  `deleted` tinyint(1) NOT NULL,
  `emailed` tinyint(1) NOT NULL,
  `data` longtext,
  PRIMARY KEY (`id`),
  KEY `notifications_notifi_action_object_conten_7d2b8ee9_fk_django_co` (`action_object_content_type_id`),
  KEY `notifications_notifi_actor_content_type_i_0c69d7b7_fk_django_co` (`actor_content_type_id`),
  KEY `notifications_notifi_target_content_type__ccb24d88_fk_django_co` (`target_content_type_id`),
  KEY `notifications_notification_deleted_b32b69e6` (`deleted`),
  KEY `notifications_notification_emailed_23a5ad81` (`emailed`),
  KEY `notifications_notification_public_1bc30b1c` (`public`),
  KEY `notifications_notification_unread_cce4be30` (`unread`),
  KEY `notifications_notification_timestamp_6a797bad` (`timestamp`),
  KEY `notifications_notification_recipient_id_unread_253aadc9_idx` (`recipient_id`,`unread`),
  CONSTRAINT `notifications_notifi_action_object_conten_7d2b8ee9_fk_django_co` FOREIGN KEY (`action_object_content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `notifications_notifi_actor_content_type_i_0c69d7b7_fk_django_co` FOREIGN KEY (`actor_content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `notifications_notifi_target_content_type__ccb24d88_fk_django_co` FOREIGN KEY (`target_content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `notifications_notification_recipient_id_d055f3f0_fk_auth_user_id` FOREIGN KEY (`recipient_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications_notification`
--

LOCK TABLES `notifications_notification` WRITE;
/*!40000 ALTER TABLE `notifications_notification` DISABLE KEYS */;
/*!40000 ALTER TABLE `notifications_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `record`
--

DROP TABLE IF EXISTS `record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `record` (
  `memoReferenceNumber` int NOT NULL,
  `recordName` varchar(100) NOT NULL,
  `memoDate` date DEFAULT NULL,
  `issuingBranch` varchar(20) NOT NULL,
  `recordDescription` text,
  `recordType` varchar(15) NOT NULL,
  `issuingDepartment` varchar(20) NOT NULL,
  PRIMARY KEY (`memoReferenceNumber`),
  CONSTRAINT `record_chk_1` CHECK ((`recordType` in (_utf8mb4'Award',_utf8mb4'Discipline')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `record`
--

LOCK TABLES `record` WRITE;
/*!40000 ALTER TABLE `record` DISABLE KEYS */;
/*!40000 ALTER TABLE `record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `spouse_background`
--

DROP TABLE IF EXISTS `spouse_background`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `spouse_background` (
  `spouseName` varchar(100) NOT NULL,
  `spouseCompany` varchar(20) DEFAULT NULL,
  `spouseCompanyAddress` varchar(255) DEFAULT NULL,
  `numberOfChildren` int DEFAULT '0',
  `spouseId` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`spouseId`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spouse_background`
--

LOCK TABLES `spouse_background` WRITE;
/*!40000 ALTER TABLE `spouse_background` DISABLE KEYS */;
INSERT INTO `spouse_background` VALUES ('Juan Spouse Cruz','Onesimus','592 Cordillera Street, Brgy. Malamig, Mandaluyong City',1,7),('Toryspouse Spec','Ateneo','Katipunan Ave, Quezon City, 1108 Metro Manila',2,9);
/*!40000 ALTER TABLE `spouse_background` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timekeeping`
--

DROP TABLE IF EXISTS `timekeeping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `timekeeping` (
  `noOfOffense` int NOT NULL DEFAULT '0',
  `tNMemoReferenceNumber` int NOT NULL,
  PRIMARY KEY (`tNMemoReferenceNumber`),
  CONSTRAINT `timekeeping_ibfk_1` FOREIGN KEY (`tNMemoReferenceNumber`) REFERENCES `record` (`memoReferenceNumber`),
  CONSTRAINT `timekeeping_ibfk_2` FOREIGN KEY (`tNMemoReferenceNumber`) REFERENCES `noac` (`nMemoReferenceNumber`),
  CONSTRAINT `timekeeping_chk_1` CHECK ((`noOfOffense` <= 100))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timekeeping`
--

LOCK TABLES `timekeeping` WRITE;
/*!40000 ALTER TABLE `timekeeping` DISABLE KEYS */;
/*!40000 ALTER TABLE `timekeeping` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-03 16:34:34
