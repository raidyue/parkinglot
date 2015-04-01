CREATE DATABASE  IF NOT EXISTS `parkinglot_db` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `parkinglot_db`;
-- MySQL dump 10.13  Distrib 5.5.41, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: parkinglot_db
-- ------------------------------------------------------
-- Server version	5.5.41-0ubuntu0.14.10.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add user',7,'add_user'),(20,'Can change user',7,'change_user'),(21,'Can delete user',7,'delete_user'),(22,'Can add parkinglot',8,'add_parkinglot'),(23,'Can change parkinglot',8,'change_parkinglot'),(24,'Can delete parkinglot',8,'delete_parkinglot'),(25,'Can add lot',9,'add_lot'),(26,'Can change lot',9,'change_lot'),(27,'Can delete lot',9,'delete_lot'),(34,'Can add consumption',12,'add_consumption'),(35,'Can change consumption',12,'change_consumption'),(36,'Can delete consumption',12,'delete_consumption'),(37,'Can add manager',13,'add_manager'),(38,'Can change manager',13,'change_manager'),(39,'Can delete manager',13,'delete_manager'),(40,'Can add order',14,'add_order'),(41,'Can change order',14,'change_order'),(42,'Can delete order',14,'delete_order');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$15000$S5APHURxUHNz$z/EkTMidhPTFtnoRM1gmdCLAL2gCrF2AY//ATgQ9R/E=','2015-03-23 03:32:01',1,'admin','','','',1,1,'2015-03-10 13:39:31');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-03-10 13:45:07','2','ddd',3,'',7,1),(2,'2015-03-10 13:46:36','1','parkinglot1',1,'',8,1),(3,'2015-03-10 13:46:58','2','parkinglot1',1,'',8,1),(4,'2015-03-10 13:47:07','2','parkinglot1',3,'',8,1),(5,'2015-03-10 13:47:34','3','parkinglot2',1,'',8,1),(6,'2015-03-10 13:47:52','1','parkinglot1-1',1,'',9,1),(7,'2015-03-10 13:48:02','2','parkinglot1-2',1,'',9,1),(8,'2015-03-10 13:48:16','3','parkinglot1-3',1,'',9,1),(9,'2015-03-10 13:48:27','4','parkinglot2-1',1,'',9,1),(10,'2015-03-10 13:48:32','5','parkinglot2-2',1,'',9,1),(11,'2015-03-12 08:45:24','1','raidyue',2,'Changed over.',7,1),(12,'2015-03-22 13:46:55','1','Manager object',1,'',13,1),(13,'2015-03-22 13:48:08','1','Manager object',2,'No fields changed.',13,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'user','parkinglot','user'),(8,'parkinglot','parkinglot','parkinglot'),(9,'lot','parkinglot','lot'),(12,'consumption','parkinglot','consumption'),(13,'manager','parkinglot','manager'),(14,'order','parkinglot','order');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-03-09 03:45:21'),(2,'auth','0001_initial','2015-03-09 03:45:22'),(3,'admin','0001_initial','2015-03-09 03:45:22'),(4,'sessions','0001_initial','2015-03-09 03:45:22'),(5,'parkinglot','0001_initial','2015-03-09 03:48:05'),(6,'parkinglot','0002_auto_20150309_0556','2015-03-09 05:57:07'),(7,'parkinglot','0003_auto_20150309_0611','2015-03-09 06:11:15'),(8,'parkinglot','0004_auto_20150309_0614','2015-03-09 06:14:17'),(9,'parkinglot','0005_auto_20150310_1342','2015-03-10 13:43:05'),(10,'parkinglot','0006_auto_20150310_1534','2015-03-10 15:34:27'),(11,'parkinglot','0007_auto_20150312_0913','2015-03-12 09:13:56'),(12,'parkinglot','0008_auto_20150317_1523','2015-03-17 15:23:55'),(13,'parkinglot','0009_auto_20150321_1513','2015-03-21 15:17:50'),(14,'parkinglot','0010_auto_20150322_1336','2015-03-22 13:36:52'),(15,'parkinglot','0011_auto_20150328_0504','2015-03-28 05:05:06');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0xdqgdxwwart8zp2hrqsimi01a3zgle1','NzlkNTRkZTU0M2I0Y2JiODkwYzQzNzNmOTM5OTM3ZTc3YWUxOTFjMDp7fQ==','2015-03-23 13:33:11'),('38v32pwny9ysfe5hrt225v9152hdwsq2','NGMxMzMyN2FlZDNhOWUxNzJmZjc3YTM2MTVjMDg5Zjk5MDlkOWMwZDp7InVzZXJuYW1lIjoicmFpZHl1ZSIsIl9hdXRoX3VzZXJfaWQiOjEsImxvZ2luX3VzZXIiOiJyYWlkeXVlIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfc2Vzc2lvbl9leHBpcnkiOjAsIl9hdXRoX3VzZXJfaGFzaCI6IjAxOTVmYzhlNzZhNWNkZTFlNWFjODM5OWUyOGJiNTE5YWRmN2NhMWMiLCJtYW5hZ2VyX3VzZXIiOiJyYWlkeXVlIn0=','2015-04-05 15:07:56'),('e7n37gejjj5feb9auat6mwwe61mxt5id','NzlkNTRkZTU0M2I0Y2JiODkwYzQzNzNmOTM5OTM3ZTc3YWUxOTFjMDp7fQ==','2015-03-23 13:50:14'),('e80u2d3roprv3veybizoh36teed0mzdq','NzlkNTRkZTU0M2I0Y2JiODkwYzQzNzNmOTM5OTM3ZTc3YWUxOTFjMDp7fQ==','2015-03-23 13:50:37'),('ilwucklblr9skvkksi6ikz7hunyknkrl','NzlkNTRkZTU0M2I0Y2JiODkwYzQzNzNmOTM5OTM3ZTc3YWUxOTFjMDp7fQ==','2015-03-23 13:20:57'),('kw2t16hcu8718p0c0lxvaqsfs745ch98','Nzk2NTU3MzE1YTBiMDIyYzk1NWYxYmJiMzg3NmExMTgyYTg3ZDYyMTp7ImxvZ2luX3VzZXIiOiJyYWlkeXVlIiwibG9naW5fbWFuYWdlciI6InJhaWR5dWUiLCJfYXV0aF91c2VyX2hhc2giOiIwMTk1ZmM4ZTc2YTVjZGUxZTVhYzgzOTllMjhiYjUxOWFkZjdjYTFjIiwiX2F1dGhfdXNlcl9pZCI6MSwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==','2015-04-11 06:04:34'),('l4wefiye9gyvcq4p9kutqvqsnzytq7t7','NzlkNTRkZTU0M2I0Y2JiODkwYzQzNzNmOTM5OTM3ZTc3YWUxOTFjMDp7fQ==','2015-03-23 13:27:44'),('pc0763tnjhw1mncje7a9yzu4netm5zoo','NzlkNTRkZTU0M2I0Y2JiODkwYzQzNzNmOTM5OTM3ZTc3YWUxOTFjMDp7fQ==','2015-03-23 13:32:17'),('pyqedb9yrfi1id0v46t4c885zpmghcg0','NzlkNTRkZTU0M2I0Y2JiODkwYzQzNzNmOTM5OTM3ZTc3YWUxOTFjMDp7fQ==','2015-03-23 13:20:23'),('s1i7fm4ssuicijo0qci1nlsfrv2uar7m','NzlkNTRkZTU0M2I0Y2JiODkwYzQzNzNmOTM5OTM3ZTc3YWUxOTFjMDp7fQ==','2015-03-23 13:30:11'),('ubdjpx94iob8qoyg6s8s39elsyvmhmi9','NzlkNTRkZTU0M2I0Y2JiODkwYzQzNzNmOTM5OTM3ZTc3YWUxOTFjMDp7fQ==','2015-03-23 13:17:19'),('zpk4pm2m0jloofnsnh252fqep73sue1d','NzlkNTRkZTU0M2I0Y2JiODkwYzQzNzNmOTM5OTM3ZTc3YWUxOTFjMDp7fQ==','2015-03-24 06:13:32');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parkinglot_lot`
--

DROP TABLE IF EXISTS `parkinglot_lot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parkinglot_lot` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num` varchar(10) NOT NULL,
  `status` int(11) NOT NULL,
  `parkinglot_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `parkinglot_lot_252a6649` (`parkinglot_id`),
  CONSTRAINT `parki_parkinglot_id_252adaebc25b9aea_fk_parkinglot_parkinglot_id` FOREIGN KEY (`parkinglot_id`) REFERENCES `parkinglot_parkinglot` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parkinglot_lot`
--

LOCK TABLES `parkinglot_lot` WRITE;
/*!40000 ALTER TABLE `parkinglot_lot` DISABLE KEYS */;
INSERT INTO `parkinglot_lot` VALUES (1,'1',1,1),(2,'2',0,1),(3,'3',0,1),(4,'1',0,3),(5,'2',0,3),(6,'4',0,1),(7,'5',0,1),(13,'6',0,1),(14,'7',0,1),(15,'8',0,1),(16,'9',0,1),(17,'10',0,1),(18,'11',0,1),(19,'12',0,1),(20,'13',0,1),(21,'14',0,1),(22,'15',0,1);
/*!40000 ALTER TABLE `parkinglot_lot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parkinglot_manager`
--

DROP TABLE IF EXISTS `parkinglot_manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parkinglot_manager` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `password` varchar(20) NOT NULL,
  `parkinglot_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `manager_name` (`name`),
  KEY `parkinglot_manager_4f6bef78` (`parkinglot_id`),
  CONSTRAINT `parki_parkinglot_id_436ad315a77b726e_fk_parkinglot_parkinglot_id` FOREIGN KEY (`parkinglot_id`) REFERENCES `parkinglot_parkinglot` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parkinglot_manager`
--

LOCK TABLES `parkinglot_manager` WRITE;
/*!40000 ALTER TABLE `parkinglot_manager` DISABLE KEYS */;
INSERT INTO `parkinglot_manager` VALUES (1,'raidyue','123',1);
/*!40000 ALTER TABLE `parkinglot_manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parkinglot_order`
--

DROP TABLE IF EXISTS `parkinglot_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parkinglot_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `order_time` datetime DEFAULT NULL,
  `status` int(11) NOT NULL,
  `lot_id` int(11) NOT NULL,
  `parkinglot_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `parkinglot_order_cc853a8c` (`lot_id`),
  KEY `parkinglot_order_4f6bef78` (`parkinglot_id`),
  KEY `parkinglot_order_e8701ad4` (`user_id`),
  CONSTRAINT `parkinglot_order_lot_id_4dadb9e0f995fe10_fk_parkinglot_lot_id` FOREIGN KEY (`lot_id`) REFERENCES `parkinglot_lot` (`id`),
  CONSTRAINT `parkinglot_order_user_id_69a91d98195efdb1_fk_parkinglot_user_id` FOREIGN KEY (`user_id`) REFERENCES `parkinglot_user` (`id`),
  CONSTRAINT `parki_parkinglot_id_18fb9af209a40955_fk_parkinglot_parkinglot_id` FOREIGN KEY (`parkinglot_id`) REFERENCES `parkinglot_parkinglot` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parkinglot_order`
--

LOCK TABLES `parkinglot_order` WRITE;
/*!40000 ALTER TABLE `parkinglot_order` DISABLE KEYS */;
INSERT INTO `parkinglot_order` VALUES (12,'2015-03-28 10:53:58','2015-03-28 10:54:01','2015-03-28 10:53:51',2,1,1,1),(13,NULL,NULL,'2015-03-28 10:54:21',0,1,1,1),(14,'2015-03-28 11:15:29','2015-03-28 11:15:29','2015-03-28 11:14:16',2,2,1,1),(15,'2015-03-28 11:15:32','2015-03-28 11:15:32','2015-03-28 11:14:22',2,3,1,1),(16,NULL,NULL,'2015-03-28 11:15:36',0,2,1,1),(17,NULL,NULL,'2015-03-28 15:14:52',0,1,1,1),(18,NULL,NULL,'2015-03-28 15:14:55',0,1,1,1),(19,NULL,NULL,'2015-03-28 15:14:57',0,1,1,1),(20,NULL,NULL,'2015-03-28 15:20:32',0,1,1,1),(21,'2015-03-28 15:42:11','2015-03-28 15:42:25','2015-03-28 15:42:02',2,1,1,1),(22,NULL,NULL,'2015-03-29 06:57:56',0,1,1,1),(23,NULL,NULL,'2015-03-29 08:25:53',0,1,1,1),(24,NULL,NULL,'2015-03-29 14:30:57',0,1,1,1),(25,'2015-03-31 08:19:16','2015-03-31 08:21:28','2015-03-31 08:18:08',2,1,1,1),(26,'2015-03-31 08:21:46','2015-03-31 08:22:38','2015-03-31 08:21:42',2,1,1,1),(27,NULL,NULL,'2015-03-31 08:25:17',0,1,1,1),(28,NULL,NULL,'2015-04-01 10:00:50',0,1,1,1);
/*!40000 ALTER TABLE `parkinglot_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parkinglot_parkinglot`
--

DROP TABLE IF EXISTS `parkinglot_parkinglot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parkinglot_parkinglot` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `address` varchar(80) NOT NULL,
  `charge` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `parkinglot_parkinglot_name_7261ba59ca62d3ec_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parkinglot_parkinglot`
--

LOCK TABLES `parkinglot_parkinglot` WRITE;
/*!40000 ALTER TABLE `parkinglot_parkinglot` DISABLE KEYS */;
INSERT INTO `parkinglot_parkinglot` VALUES (1,'parkinglot1','hn','cd',2),(3,'parkinglot2','beijing','beijing',1);
/*!40000 ALTER TABLE `parkinglot_parkinglot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parkinglot_user`
--

DROP TABLE IF EXISTS `parkinglot_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parkinglot_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(20) DEFAULT NULL,
  `over` double NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parkinglot_user`
--

LOCK TABLES `parkinglot_user` WRITE;
/*!40000 ALTER TABLE `parkinglot_user` DISABLE KEYS */;
INSERT INTO `parkinglot_user` VALUES (1,'123',51,'raidyue','a@a'),(2,'123',0,'raidyue1','a@a'),(3,'123',0,'raidyue2','a@a'),(4,'123',0,'raidyue3','a@a'),(5,'123',0,'raidyue4','a@a');
/*!40000 ALTER TABLE `parkinglot_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-04-01 22:10:27
