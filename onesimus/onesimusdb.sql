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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add child background',7,'add_childbackground'),(26,'Can change child background',7,'change_childbackground'),(27,'Can delete child background',7,'delete_childbackground'),(28,'Can view child background',7,'view_childbackground'),(29,'Can add educational background',8,'add_educationalbackground'),(30,'Can change educational background',8,'change_educationalbackground'),(31,'Can delete educational background',8,'delete_educationalbackground'),(32,'Can view educational background',8,'view_educationalbackground'),(33,'Can add emergency details',9,'add_emergencydetails'),(34,'Can change emergency details',9,'change_emergencydetails'),(35,'Can delete emergency details',9,'delete_emergencydetails'),(36,'Can view emergency details',9,'view_emergencydetails'),(37,'Can add employee personal info',10,'add_employeepersonalinfo'),(38,'Can change employee personal info',10,'change_employeepersonalinfo'),(39,'Can delete employee personal info',10,'delete_employeepersonalinfo'),(40,'Can view employee personal info',10,'view_employeepersonalinfo'),(41,'Can add employee position',11,'add_employeeposition'),(42,'Can change employee position',11,'change_employeeposition'),(43,'Can delete employee position',11,'delete_employeeposition'),(44,'Can view employee position',11,'view_employeeposition'),(45,'Can add employee position history',12,'add_employeepositionhistory'),(46,'Can change employee position history',12,'change_employeepositionhistory'),(47,'Can delete employee position history',12,'delete_employeepositionhistory'),(48,'Can view employee position history',12,'view_employeepositionhistory'),(49,'Can add employee work location',13,'add_employeeworklocation'),(50,'Can change employee work location',13,'change_employeeworklocation'),(51,'Can delete employee work location',13,'delete_employeeworklocation'),(52,'Can view employee work location',13,'view_employeeworklocation'),(53,'Can add employment history',14,'add_employmenthistory'),(54,'Can change employment history',14,'change_employmenthistory'),(55,'Can delete employment history',14,'delete_employmenthistory'),(56,'Can view employment history',14,'view_employmenthistory'),(57,'Can add family member background',15,'add_familymemberbackground'),(58,'Can change family member background',15,'change_familymemberbackground'),(59,'Can delete family member background',15,'delete_familymemberbackground'),(60,'Can view family member background',15,'view_familymemberbackground'),(61,'Can add spouse background',16,'add_spousebackground'),(62,'Can change spouse background',16,'change_spousebackground'),(63,'Can delete spouse background',16,'delete_spousebackground'),(64,'Can view spouse background',16,'view_spousebackground'),(65,'Can add document',17,'add_document'),(66,'Can change document',17,'change_document'),(67,'Can delete document',17,'delete_document'),(68,'Can view document',17,'view_document'),(69,'Can add employee',18,'add_employee'),(70,'Can change employee',18,'change_employee'),(71,'Can delete employee',18,'delete_employee'),(72,'Can view employee',18,'view_employee'),(73,'Can add timekeeping',19,'add_timekeeping'),(74,'Can change timekeeping',19,'change_timekeeping'),(75,'Can delete timekeeping',19,'delete_timekeeping'),(76,'Can view timekeeping',19,'view_timekeeping'),(77,'Can add noac',20,'add_noac'),(78,'Can change noac',20,'change_noac'),(79,'Can delete noac',20,'delete_noac'),(80,'Can view noac',20,'view_noac'),(81,'Can add major offense',21,'add_majoroffense'),(82,'Can change major offense',21,'change_majoroffense'),(83,'Can delete major offense',21,'delete_majoroffense'),(84,'Can view major offense',21,'view_majoroffense'),(85,'Can add awol',22,'add_awol'),(86,'Can change awol',22,'change_awol'),(87,'Can delete awol',22,'delete_awol'),(88,'Can view awol',22,'view_awol'),(89,'Can add awards',23,'add_awards'),(90,'Can change awards',23,'change_awards'),(91,'Can delete awards',23,'delete_awards'),(92,'Can view awards',23,'view_awards'),(93,'Can add record',24,'add_record'),(94,'Can change record',24,'change_record'),(95,'Can delete record',24,'delete_record'),(96,'Can view record',24,'view_record');
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$216000$pe2ANyqBTTjz$Rb35jme6LxUbh/vfZfJOUDVHXG23fQpyYmmOCMkADNQ=','2021-03-06 11:19:36.286603',1,'onesimushelm','','','',1,1,'2021-03-06 11:00:16.569890'),(2,'pbkdf2_sha256$216000$9JcS0QoynbxT$sMYlCVp2h/YrVdoUN6K6gh0Hm9hwMcjAf++4amRVpwo=','2021-03-06 11:14:54.984633',0,'juandelacruz','','','',0,1,'2021-03-06 11:14:33.626347');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
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
  `awardIssuer` varchar(20) NOT NULL,
  `awardPurpose` varchar(20) NOT NULL,
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
  `childName` varchar(20) NOT NULL,
  `childAge` int DEFAULT NULL,
  `childOccupation` varchar(20) DEFAULT NULL,
  `childId` int NOT NULL AUTO_INCREMENT,
  `informationId` int NOT NULL,
  PRIMARY KEY (`childId`),
  KEY `informationId` (`informationId`),
  CONSTRAINT `child_background_ibfk_1` FOREIGN KEY (`informationId`) REFERENCES `employee_personal_info` (`informationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `child_background`
--

LOCK TABLES `child_background` WRITE;
/*!40000 ALTER TABLE `child_background` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-03-06 11:14:33.738124','2','juandelacruz',1,'[{\"added\": {}}]',4,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(23,'loginapp','awards'),(22,'loginapp','awol'),(7,'loginapp','childbackground'),(17,'loginapp','document'),(8,'loginapp','educationalbackground'),(9,'loginapp','emergencydetails'),(18,'loginapp','employee'),(10,'loginapp','employeepersonalinfo'),(11,'loginapp','employeeposition'),(12,'loginapp','employeepositionhistory'),(13,'loginapp','employeeworklocation'),(14,'loginapp','employmenthistory'),(15,'loginapp','familymemberbackground'),(21,'loginapp','majoroffense'),(20,'loginapp','noac'),(24,'loginapp','record'),(16,'loginapp','spousebackground'),(19,'loginapp','timekeeping'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-03-06 10:59:29.333925'),(2,'auth','0001_initial','2021-03-06 10:59:29.796832'),(3,'admin','0001_initial','2021-03-06 10:59:31.035477'),(4,'admin','0002_logentry_remove_auto_add','2021-03-06 10:59:31.305162'),(5,'admin','0003_logentry_add_action_flag_choices','2021-03-06 10:59:31.323741'),(6,'contenttypes','0002_remove_content_type_name','2021-03-06 10:59:31.680890'),(7,'auth','0002_alter_permission_name_max_length','2021-03-06 10:59:32.028789'),(8,'auth','0003_alter_user_email_max_length','2021-03-06 10:59:32.063527'),(9,'auth','0004_alter_user_username_opts','2021-03-06 10:59:32.076741'),(10,'auth','0005_alter_user_last_login_null','2021-03-06 10:59:32.179057'),(11,'auth','0006_require_contenttypes_0002','2021-03-06 10:59:32.187065'),(12,'auth','0007_alter_validators_add_error_messages','2021-03-06 10:59:32.199743'),(13,'auth','0008_alter_user_username_max_length','2021-03-06 10:59:32.293992'),(14,'auth','0009_alter_user_last_name_max_length','2021-03-06 10:59:32.391042'),(15,'auth','0010_alter_group_name_max_length','2021-03-06 10:59:32.431148'),(16,'auth','0011_update_proxy_permissions','2021-03-06 10:59:32.443488'),(17,'auth','0012_alter_user_first_name_max_length','2021-03-06 10:59:32.886613'),(18,'sessions','0001_initial','2021-03-06 10:59:33.070836'),(19,'loginapp','0001_initial','2021-03-06 11:11:38.773280');
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
INSERT INTO `django_session` VALUES ('73k4jn7fyoqtl4ll2gjr2a6rnfzpaejk','.eJxVjDsOwjAQBe_iGln-Zh1Kes5geb1rHECxFCcV4u4QKQW0b2beS8S0rTVunZc4kTgLLU6_G6b84HkHdE_zrcnc5nWZUO6KPGiX10b8vBzu30FNvX5rF0hpYkcjOA0GudiBPJQxBzN4Z6AgKavKyAZ9tj4oYItQUiA0AEq8P9sZN7M:1lIUy8:FA7ttgv8I3R8fOnoMjqJbvaeLKKhmKrb2ebcXzurhjU','2021-03-20 11:19:36.295827');
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
  `documentName` varchar(50) NOT NULL,
  `dateAndTimeCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `author` varchar(50) NOT NULL,
  `dateAndTimeLastEdited` datetime DEFAULT CURRENT_TIMESTAMP,
  `recentEditor` varchar(50) DEFAULT NULL,
  `employeeId` int NOT NULL,
  `preparedBy` varchar(20) NOT NULL,
  `preparationDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `notedBy` varchar(20) NOT NULL,
  `notedDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `approvedBy` varchar(20) NOT NULL,
  `approvedDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `receivedBy` varchar(20) NOT NULL,
  `receivedDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `memoReferenceNumber` int NOT NULL,
  PRIMARY KEY (`documentId`),
  KEY `employeeId` (`employeeId`),
  KEY `memoReferenceNumber` (`memoReferenceNumber`),
  CONSTRAINT `document_ibfk_1` FOREIGN KEY (`employeeId`) REFERENCES `employee` (`employeeId`),
  CONSTRAINT `document_ibfk_2` FOREIGN KEY (`memoReferenceNumber`) REFERENCES `record` (`memoReferenceNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
  `schoolName` varchar(20) NOT NULL,
  `startingYearAttended` date NOT NULL,
  `endingYearAttended` date NOT NULL,
  `schoolType` varchar(15) NOT NULL DEFAULT 'Elementary',
  `informationId` int NOT NULL,
  `degreeId` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`degreeId`),
  KEY `informationId` (`informationId`),
  CONSTRAINT `educational_background_ibfk_1` FOREIGN KEY (`informationId`) REFERENCES `employee_personal_info` (`informationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `educational_background`
--

LOCK TABLES `educational_background` WRITE;
/*!40000 ALTER TABLE `educational_background` DISABLE KEYS */;
/*!40000 ALTER TABLE `educational_background` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emergency_details`
--

DROP TABLE IF EXISTS `emergency_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emergency_details` (
  `emergencyContactNumber` int NOT NULL,
  `emergencyContactName` varchar(20) NOT NULL,
  `emergencyRelationship` varchar(20) DEFAULT NULL,
  `emergencyAddress` varchar(50) NOT NULL,
  PRIMARY KEY (`emergencyContactNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emergency_details`
--

LOCK TABLES `emergency_details` WRITE;
/*!40000 ALTER TABLE `emergency_details` DISABLE KEYS */;
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
  PRIMARY KEY (`employeeId`),
  KEY `branch` (`branch`),
  KEY `jobId` (`jobId`),
  KEY `informationId` (`informationId`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`employeeId`) REFERENCES `document` (`employeeId`),
  CONSTRAINT `employee_ibfk_5` FOREIGN KEY (`branch`) REFERENCES `employee_work_location` (`branch`),
  CONSTRAINT `employee_ibfk_6` FOREIGN KEY (`jobId`) REFERENCES `employee_position` (`jobId`),
  CONSTRAINT `employee_ibfk_7` FOREIGN KEY (`informationId`) REFERENCES `employee_personal_info` (`informationId`),
  CONSTRAINT `employee_chk_3` CHECK ((`employmentStatus` in (_utf8mb4'Probationary',_utf8mb4'Seasonal',_utf8mb4'Project-Based',_utf8mb4'Reliever')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_personal_info`
--

DROP TABLE IF EXISTS `employee_personal_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_personal_info` (
  `employeeName` varchar(20) NOT NULL,
  `emergencyContactNumber` int NOT NULL,
  `gender` varchar(10) NOT NULL,
  `birthDate` date NOT NULL,
  `civilStatus` varchar(10) NOT NULL,
  `citizenship` varchar(20) NOT NULL,
  `religion` varchar(20) DEFAULT NULL,
  `bloodType` varchar(10) NOT NULL DEFAULT 'Unknown',
  `numberOfDependent` int NOT NULL DEFAULT '0',
  `presentAddress` varchar(100) NOT NULL,
  `permanentAddress` varchar(100) NOT NULL,
  `contactNumber` int NOT NULL,
  `spouseId` int DEFAULT NULL,
  `informationId` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`informationId`),
  KEY `emergencyContactNumber` (`emergencyContactNumber`),
  KEY `spouseId` (`spouseId`),
  CONSTRAINT `employee_personal_info_ibfk_2` FOREIGN KEY (`emergencyContactNumber`) REFERENCES `emergency_details` (`emergencyContactNumber`),
  CONSTRAINT `employee_personal_info_ibfk_3` FOREIGN KEY (`spouseId`) REFERENCES `spouse_background` (`spouseId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_personal_info`
--

LOCK TABLES `employee_personal_info` WRITE;
/*!40000 ALTER TABLE `employee_personal_info` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_position`
--

LOCK TABLES `employee_position` WRITE;
/*!40000 ALTER TABLE `employee_position` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!40000 ALTER TABLE `employee_work_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employment_history`
--

DROP TABLE IF EXISTS `employment_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employment_history` (
  `previousCompanyName` varchar(20) NOT NULL,
  `previousPosition` varchar(20) DEFAULT NULL,
  `reasonForLeaving` varchar(20) DEFAULT NULL,
  `companyContactNumber` varchar(20) DEFAULT NULL,
  `withCOEorClearance` varchar(10) NOT NULL,
  `employmentHistoryId` int NOT NULL AUTO_INCREMENT,
  `informationId` int NOT NULL,
  PRIMARY KEY (`employmentHistoryId`),
  KEY `informationId` (`informationId`),
  CONSTRAINT `employment_history_ibfk_1` FOREIGN KEY (`informationId`) REFERENCES `employee_personal_info` (`informationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employment_history`
--

LOCK TABLES `employment_history` WRITE;
/*!40000 ALTER TABLE `employment_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `employment_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `family_member_background`
--

DROP TABLE IF EXISTS `family_member_background`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `family_member_background` (
  `memberName` varchar(20) NOT NULL,
  `memberAge` int DEFAULT NULL,
  `memberRelationship` varchar(20) NOT NULL DEFAULT 'Mother',
  `memberOccupation` varchar(20) DEFAULT NULL,
  `familyId` int NOT NULL AUTO_INCREMENT,
  `informationId` int NOT NULL,
  PRIMARY KEY (`familyId`),
  KEY `informationId` (`informationId`),
  CONSTRAINT `family_member_background_ibfk_1` FOREIGN KEY (`informationId`) REFERENCES `employee_personal_info` (`informationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `family_member_background`
--

LOCK TABLES `family_member_background` WRITE;
/*!40000 ALTER TABLE `family_member_background` DISABLE KEYS */;
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
  `remarks` varchar(50) DEFAULT NULL,
  `noacType` varchar(15) NOT NULL DEFAULT 'Timekeeping',
  `sanction` varchar(20) NOT NULL,
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
-- Table structure for table `record`
--

DROP TABLE IF EXISTS `record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `record` (
  `memoReferenceNumber` int NOT NULL,
  `recordName` varchar(20) NOT NULL,
  `memoDate` date DEFAULT NULL,
  `issuingBranch` varchar(20) NOT NULL,
  `recordDescription` varchar(20) DEFAULT NULL,
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
  `spouseName` varchar(20) NOT NULL,
  `spouseCompany` varchar(20) DEFAULT NULL,
  `spouseCompanyAddress` varchar(20) DEFAULT NULL,
  `numberOfChildren` int DEFAULT '0',
  `spouseId` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`spouseId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spouse_background`
--

LOCK TABLES `spouse_background` WRITE;
/*!40000 ALTER TABLE `spouse_background` DISABLE KEYS */;
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

-- Dump completed on 2021-03-06 20:07:18
