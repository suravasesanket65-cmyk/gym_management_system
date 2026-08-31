-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: gyms
-- ------------------------------------------------------
-- Server version	8.0.45

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `attendance_id` int NOT NULL AUTO_INCREMENT,
  `member_id` int NOT NULL,
  `check_in_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `check_out_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`attendance_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `members` (`member_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance`
--

LOCK TABLES `attendance` WRITE;
/*!40000 ALTER TABLE `attendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `attendance` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$wpGEItq8C4obsWfGwxnLV2$DJ1W1umx030gEypGxmUbBys3e1kjYGlQjd0ptgBg358=','2026-08-25 08:58:59.815059',1,'admin','','','admin@gmail.com',1,1,'2026-08-24 20:28:09.954015'),(2,'pbkdf2_sha256$870000$drH4nK7d0eq7ywYdNNCfWG$tJUk7DLBQGIdDTqtlnN+eNg4NQcRBvNxJ4R2K0N1hbI=','2026-08-31 11:11:02.032591',1,'gym_admin','','','gymadmin@example.com',1,1,'2026-08-25 09:06:25.708428'),(3,'',NULL,0,'teststaff','','','staff@test.com',0,1,'2026-08-30 18:23:45.597245'),(9,'',NULL,0,'staff1','','','',0,1,'2026-08-31 18:14:58.919914');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class_schedules`
--

DROP TABLE IF EXISTS `class_schedules`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class_schedules` (
  `class_id` int NOT NULL AUTO_INCREMENT,
  `program_id` int NOT NULL,
  `trainer_id` int NOT NULL,
  `class_name` varchar(100) NOT NULL,
  `day_of_week` enum('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday') NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  `max_capacity` int DEFAULT '20',
  PRIMARY KEY (`class_id`),
  KEY `program_id` (`program_id`),
  KEY `trainer_id` (`trainer_id`),
  CONSTRAINT `class_schedules_ibfk_1` FOREIGN KEY (`program_id`) REFERENCES `programs` (`program_id`) ON DELETE CASCADE,
  CONSTRAINT `class_schedules_ibfk_2` FOREIGN KEY (`trainer_id`) REFERENCES `trainers` (`trainer_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class_schedules`
--

LOCK TABLES `class_schedules` WRITE;
/*!40000 ALTER TABLE `class_schedules` DISABLE KEYS */;
/*!40000 ALTER TABLE `class_schedules` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_appointment`
--

DROP TABLE IF EXISTS `core_appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_appointment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `appointment_date` date NOT NULL,
  `start_time` time(6) NOT NULL,
  `end_time` time(6) NOT NULL,
  `appointment_type` varchar(100) NOT NULL,
  `status` varchar(20) NOT NULL,
  `notes` longtext,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `member_id` bigint NOT NULL,
  `trainer_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_appointment_member_id_2022c0e7_fk_core_member_id` (`member_id`),
  KEY `core_appointment_appointment_date_8fba9d95` (`appointment_date`),
  KEY `core_appoin_trainer_eea254_idx` (`trainer_id`,`appointment_date`),
  CONSTRAINT `core_appointment_member_id_2022c0e7_fk_core_member_id` FOREIGN KEY (`member_id`) REFERENCES `core_member` (`id`),
  CONSTRAINT `core_appointment_trainer_id_31c263aa_fk_core_trainer_id` FOREIGN KEY (`trainer_id`) REFERENCES `core_trainer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_appointment`
--

LOCK TABLES `core_appointment` WRITE;
/*!40000 ALTER TABLE `core_appointment` DISABLE KEYS */;
INSERT INTO `core_appointment` VALUES (2,'2026-08-31','21:14:58.840802','22:14:58.840802','Consultation','Scheduled','Initial consultation','2026-08-31 18:14:58.916698','2026-08-31 18:14:58.916709',9,4);
/*!40000 ALTER TABLE `core_appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_attendance`
--

DROP TABLE IF EXISTS `core_attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_attendance` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `check_in_time` datetime(6) NOT NULL,
  `check_out_time` datetime(6) DEFAULT NULL,
  `member_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_attendance_member_id_da2e18bc_fk_core_member_id` (`member_id`),
  CONSTRAINT `core_attendance_member_id_da2e18bc_fk_core_member_id` FOREIGN KEY (`member_id`) REFERENCES `core_member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_attendance`
--

LOCK TABLES `core_attendance` WRITE;
/*!40000 ALTER TABLE `core_attendance` DISABLE KEYS */;
INSERT INTO `core_attendance` VALUES (2,'2026-08-31 18:14:58.840802',NULL,9);
/*!40000 ALTER TABLE `core_attendance` ENABLE KEYS */;
UNLOCK TABLES;



--
-- Dumping data for table `core_expense`
--

LOCK TABLES `core_expense` WRITE;
/*!40000 ALTER TABLE `core_expense` DISABLE KEYS */;
INSERT INTO `core_expense` VALUES (2,'Utilities',150.00,'2026-08-31','Monthly Electricity Bill',NULL,NULL,'2026-08-31 18:14:58.909615','2026-08-31 18:14:58.909648',NULL);
/*!40000 ALTER TABLE `core_expense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_inventoryitem`
--

DROP TABLE IF EXISTS `core_inventoryitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_inventoryitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `item_name` varchar(150) NOT NULL,
  `category` varchar(100) NOT NULL,
  `sku` varchar(100) NOT NULL,
  `quantity` int unsigned NOT NULL,
  `min_stock_level` int unsigned NOT NULL,
  `unit` varchar(50) NOT NULL,
  `purchase_price` decimal(10,2) DEFAULT NULL,
  `supplier` varchar(150) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `status` varchar(50) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sku` (`sku`),
  KEY `core_inventoryitem_category_21d977f8` (`category`),
  KEY `core_inventoryitem_status_8e3ae678` (`status`),
  CONSTRAINT `core_inventoryitem_chk_1` CHECK ((`quantity` >= 0)),
  CONSTRAINT `core_inventoryitem_chk_2` CHECK ((`min_stock_level` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_inventoryitem`
--

LOCK TABLES `core_inventoryitem` WRITE;
/*!40000 ALTER TABLE `core_inventoryitem` DISABLE KEYS */;
INSERT INTO `core_inventoryitem` VALUES (2,'Protein Powder','Supplements','dd5705c6',50,10,'kg',NULL,NULL,NULL,'Available','2026-08-31 18:14:58.905022','2026-08-31 18:14:58.905038');
/*!40000 ALTER TABLE `core_inventoryitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_member`
--

DROP TABLE IF EXISTS `core_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_member` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `date_of_birth` date NOT NULL,
  `address` longtext,
  `emergency_contact` varchar(100) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `joined_date` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_member`
--

LOCK TABLES `core_member` WRITE;
/*!40000 ALTER TABLE `core_member` DISABLE KEYS */;
INSERT INTO `core_member` VALUES (2,'TEST','MEMB','t@t.com','','','2000-01-01',NULL,NULL,'Active','2026-08-30'),(3,'testm','last','test@test.com','','','2000-01-01',NULL,NULL,'Active','2026-08-30'),(4,'rajesh','Shrama','raj@gmail.com','4578784545','M','2000-04-04','',NULL,'Active','2026-08-31'),(9,'Alice','Smith','member@example.com','1234567890','','2001-09-06','123 Gym Street',NULL,'Active','2026-08-31');
/*!40000 ALTER TABLE `core_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_membershipplan`
--

DROP TABLE IF EXISTS `core_membershipplan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_membershipplan` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `plan_name` varchar(100) NOT NULL,
  `duration_months` int NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `description` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_membershipplan`
--

LOCK TABLES `core_membershipplan` WRITE;
/*!40000 ALTER TABLE `core_membershipplan` DISABLE KEYS */;
INSERT INTO `core_membershipplan` VALUES (2,'Pro Plan',1,2999.00,'Access to all equipment and classes');
/*!40000 ALTER TABLE `core_membershipplan` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `core_trainer`
--

DROP TABLE IF EXISTS `core_trainer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_trainer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `full_name` varchar(100) NOT NULL,
  `role_specialty` varchar(100) NOT NULL,
  `image_url` varchar(500) DEFAULT NULL,
  `instagram_url` varchar(500) DEFAULT NULL,
  `linkedin_url` varchar(500) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_trainer`
--

LOCK TABLES `core_trainer` WRITE;
/*!40000 ALTER TABLE `core_trainer` DISABLE KEYS */;
INSERT INTO `core_trainer` VALUES (2,'TEST TRAIN','',NULL,NULL,NULL,'2026-08-30 17:52:12.132627'),(3,'testt','',NULL,NULL,NULL,'2026-08-30 18:06:41.518613'),(4,'John Doe','Strength Training',NULL,NULL,NULL,'2026-08-31 18:14:36.732735');
/*!40000 ALTER TABLE `core_trainer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_trialbooking`
--

DROP TABLE IF EXISTS `core_trialbooking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_trialbooking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `message` longtext,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `program_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_trialbooking_program_id_5dacdaca_fk_core_program_id` (`program_id`),
  CONSTRAINT `core_trialbooking_program_id_5dacdaca_fk_core_program_id` FOREIGN KEY (`program_id`) REFERENCES `core_program` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_trialbooking`
--

LOCK TABLES `core_trialbooking` WRITE;
/*!40000 ALTER TABLE `core_trialbooking` DISABLE KEYS */;
INSERT INTO `core_trialbooking` VALUES (2,'ram','df','rm@gmail.com','7474859641','no','Pending','2026-08-31 10:04:06.281492',1),(5,'ram','dfr','se@gmail.com','7485748574','no','Pending','2026-08-31 10:20:20.510944',1),(7,'sanket','sa','sank@gmail.com','7485748574','no','New','2026-08-31 11:10:35.553655',1),(8,'Test','User','trial@example.com','1122334455','Interested in trying out the gym.','New','2026-08-31 18:14:58.913474',6);
/*!40000 ALTER TABLE `core_trialbooking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `members` (
  `member_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `gender` enum('Male','Female','Other') DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `address` text,
  `emergency_contact` varchar(20) DEFAULT NULL,
  `status` enum('Active','Inactive','Suspended') DEFAULT 'Active',
  `joined_date` date DEFAULT (curdate()),
  PRIMARY KEY (`member_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `membership_plans`
--

DROP TABLE IF EXISTS `membership_plans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `membership_plans` (
  `plan_id` int NOT NULL AUTO_INCREMENT,
  `plan_name` varchar(50) NOT NULL,
  `duration_months` int NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `description` text,
  PRIMARY KEY (`plan_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `membership_plans`
--

LOCK TABLES `membership_plans` WRITE;
/*!40000 ALTER TABLE `membership_plans` DISABLE KEYS */;
/*!40000 ALTER TABLE `membership_plans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `payment_id` int NOT NULL AUTO_INCREMENT,
  `subscription_id` int DEFAULT NULL,
  `member_id` int NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `payment_method` enum('Cash','UPI','Credit Card','Debit Card','Net Banking') NOT NULL,
  `payment_status` enum('Completed','Pending','Failed') DEFAULT 'Completed',
  `transaction_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`payment_id`),
  KEY `subscription_id` (`subscription_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`subscription_id`) REFERENCES `subscriptions` (`subscription_id`) ON DELETE SET NULL,
  CONSTRAINT `payments_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `members` (`member_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trial_bookings`
--

DROP TABLE IF EXISTS `trial_bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trial_bookings` (
  `booking_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `program_id` int DEFAULT NULL,
  `message` text,
  `status` enum('New','Contacted','Converted','Cancelled') DEFAULT 'New',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`booking_id`),
  KEY `program_id` (`program_id`),
  CONSTRAINT `trial_bookings_ibfk_1` FOREIGN KEY (`program_id`) REFERENCES `programs` (`program_id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trial_bookings`
--

LOCK TABLES `trial_bookings` WRITE;
/*!40000 ALTER TABLE `trial_bookings` DISABLE KEYS */;
/*!40000 ALTER TABLE `trial_bookings` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-08-31 23:47:28
