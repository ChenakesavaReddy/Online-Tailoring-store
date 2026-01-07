/*
SQLyog Community v13.2.0 (64 bit)
MySQL - 8.4.0 : Database - menztailor
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`menztailor` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `menztailor`;

/*Table structure for table `admin` */

DROP TABLE IF EXISTS `admin`;

CREATE TABLE `admin` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `admin` */

insert  into `admin`(`id`,`email`,`password`) values 
(1,'bckr2003@gmail.com','b');

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add contact',7,'add_contact'),
(26,'Can change contact',7,'change_contact'),
(27,'Can delete contact',7,'delete_contact'),
(28,'Can view contact',7,'view_contact'),
(29,'Can add add notification',8,'add_addnotification'),
(30,'Can change add notification',8,'change_addnotification'),
(31,'Can delete add notification',8,'delete_addnotification'),
(32,'Can view add notification',8,'view_addnotification'),
(33,'Can add admin',9,'add_admin'),
(34,'Can change admin',9,'change_admin'),
(35,'Can delete admin',9,'delete_admin'),
(36,'Can view admin',9,'view_admin'),
(37,'Can add designer',10,'add_designer'),
(38,'Can change designer',10,'change_designer'),
(39,'Can delete designer',10,'delete_designer'),
(40,'Can view designer',10,'view_designer'),
(41,'Can add registration',11,'add_registration'),
(42,'Can change registration',11,'change_registration'),
(43,'Can delete registration',11,'delete_registration'),
(44,'Can view registration',11,'view_registration'),
(45,'Can add designer gallery',12,'add_designergallery'),
(46,'Can change designer gallery',12,'change_designergallery'),
(47,'Can delete designer gallery',12,'delete_designergallery'),
(48,'Can view designer gallery',12,'view_designergallery'),
(49,'Can add designer service',13,'add_designerservice'),
(50,'Can change designer service',13,'change_designerservice'),
(51,'Can delete designer service',13,'delete_designerservice'),
(52,'Can view designer service',13,'view_designerservice'),
(53,'Can add booking',14,'add_booking'),
(54,'Can change booking',14,'change_booking'),
(55,'Can delete booking',14,'delete_booking'),
(56,'Can view booking',14,'view_booking'),
(57,'Can add review',15,'add_review'),
(58,'Can change review',15,'change_review'),
(59,'Can delete review',15,'delete_review'),
(60,'Can view review',15,'view_review');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `booking_date` datetime(6) NOT NULL,
  `scheduled_date` date NOT NULL,
  `status` varchar(20) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `notes` longtext,
  `designer_id` bigint NOT NULL,
  `service_id` bigint NOT NULL,
  `customer_id` bigint NOT NULL,
  `actual_start_date` date DEFAULT NULL,
  `expected_end_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Booking_designer_id_d31c3300_fk_Designer_id` (`designer_id`),
  KEY `Booking_service_id_d56ad6f3_fk_DesignerService_id` (`service_id`),
  KEY `Booking_customer_id_c91abfdd_fk_Register_id` (`customer_id`),
  CONSTRAINT `Booking_customer_id_c91abfdd_fk_Register_id` FOREIGN KEY (`customer_id`) REFERENCES `register` (`id`),
  CONSTRAINT `Booking_designer_id_d31c3300_fk_Designer_id` FOREIGN KEY (`designer_id`) REFERENCES `designer` (`id`),
  CONSTRAINT `Booking_service_id_d56ad6f3_fk_DesignerService_id` FOREIGN KEY (`service_id`) REFERENCES `designerservice` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `booking` */

insert  into `booking`(`id`,`booking_date`,`scheduled_date`,`status`,`total_price`,`notes`,`designer_id`,`service_id`,`customer_id`,`actual_start_date`,`expected_end_date`) values 
(4,'2025-12-16 09:39:59.547825','2025-12-19','completed',1500.00,'Size: XXL',1,1,3,'2025-12-16','2025-12-31'),
(5,'2025-12-17 06:37:24.920715','2025-12-18','pending',1000.00,'size xxl',2,2,3,NULL,NULL),
(6,'2025-12-19 06:01:34.486574','2025-12-20','in_progress',1500.00,'Size: XL',1,1,4,'2025-12-19','2025-12-29');

/*Table structure for table `contact` */

DROP TABLE IF EXISTS `contact`;

CREATE TABLE `contact` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `subject` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `contact` */

insert  into `contact`(`id`,`message`,`name`,`email`,`subject`) values 
(1,'Contact us','B Chennakesava Reddy','bckr2003@gmail.com','Meztailor'),
(2,'Contact Me','Ram','bckr2003@gmail.com','Meztailor'),
(3,'Contact Me','Ram','bckr2003@gmail.com','Meztailor');

/*Table structure for table `designer` */

DROP TABLE IF EXISTS `designer`;

CREATE TABLE `designer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `profile_image` varchar(100) DEFAULT NULL,
  `fullname` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `mobile_number` varchar(10) NOT NULL,
  `password` varchar(100) NOT NULL,
  `address` longtext NOT NULL,
  `city` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `pincode` int NOT NULL,
  `gender` varchar(20) NOT NULL,
  `experience` int NOT NULL,
  `specialization` varchar(200) NOT NULL,
  `aboutme` longtext NOT NULL,
  `status` varchar(20) NOT NULL,
  `otp` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `designer` */

insert  into `designer`(`id`,`profile_image`,`fullname`,`email`,`mobile_number`,`password`,`address`,`city`,`location`,`pincode`,`gender`,`experience`,`specialization`,`aboutme`,`status`,`otp`) values 
(1,'profiles/Gemini_Generated_Image_mc0lawmc0lawmc0l_a93rPwf.png','B Chennakesava Reddy','bckr2003@gmail.com','9666039039','pbkdf2_sha256$1000000$SgkF1A0v8dLPiYCBE5cFIz$RHEnk+Y+ujmyb+IS5HJRAzkuHbJW5JZqDCJA/bq6cpU=','KPHB Colony','Warangal','Telangana',500012,'male',4,'men','I  am experienced in stiching Shirts','accepted',NULL),
(2,'profiles/kurthi.jpeg','B sindhuja Reddy','battulachennakesavareddy2003@gmail.com','9666039039','pbkdf2_sha256$1000000$IcAJHPEQ7H9rnBKioRqUMY$gwr700eexfU+klCsdjfBm4KgMK6ONL6U2xfwDQ4Augk=','KPHB Colony','hyd','Telangana',500054,'female',3,'women','I am experienced in making kurthis','accepted',NULL),
(3,'profiles/Gemini_Generated_Image_mc0lawmc0lawmc0l_ReaTsBQ.png','Ram','bc@gmail.com','9666039039','pbkdf2_sha256$1000000$RwQBpZjgKetykhhyGnhZJm$K9NZzmyBbc28JmL7p/bw21Nf6d5t7jdiDcNs/3/CUBo=','KPHB Colony','Hyderbad','Telangana',500054,'male',3,'kids','I am experienced in making kids dress','accepted',NULL);

/*Table structure for table `designergallery` */

DROP TABLE IF EXISTS `designergallery`;

CREATE TABLE `designergallery` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `designer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `DesignerGallery_designer_id_054a4456_fk_Designer_id` (`designer_id`),
  CONSTRAINT `DesignerGallery_designer_id_054a4456_fk_Designer_id` FOREIGN KEY (`designer_id`) REFERENCES `designer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `designergallery` */

insert  into `designergallery`(`id`,`image`,`uploaded_at`,`designer_id`) values 
(1,'designer_gallery/shirt.webp','2025-12-15 13:11:04.122039',1);

/*Table structure for table `designerservice` */

DROP TABLE IF EXISTS `designerservice`;

CREATE TABLE `designerservice` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `timeperiod` int unsigned NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `designer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `DesignerService_designer_id_64e14bc8_fk_Designer_id` (`designer_id`),
  CONSTRAINT `DesignerService_designer_id_64e14bc8_fk_Designer_id` FOREIGN KEY (`designer_id`) REFERENCES `designer` (`id`),
  CONSTRAINT `designerservice_chk_1` CHECK ((`timeperiod` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `designerservice` */

insert  into `designerservice`(`id`,`title`,`category`,`timeperiod`,`price`,`image`,`designer_id`) values 
(1,'Stiching','Men',10,1500.00,'service_images/shirt.webp',1),
(2,'Altering','Women',7,1000.00,'service_images/kurthi.jpeg',2),
(3,'Stiching','Kids',7,750.00,'service_images/kids.jpg',3),
(9,'sjvlzd','men',10,1500.00,'',1);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(8,'realapp','addnotification'),
(9,'realapp','admin'),
(14,'realapp','booking'),
(7,'realapp','contact'),
(10,'realapp','designer'),
(12,'realapp','designergallery'),
(13,'realapp','designerservice'),
(11,'realapp','registration'),
(15,'realapp','review'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2025-12-15 06:59:36.558604'),
(2,'auth','0001_initial','2025-12-15 06:59:37.463615'),
(3,'admin','0001_initial','2025-12-15 06:59:37.694975'),
(4,'admin','0002_logentry_remove_auto_add','2025-12-15 06:59:37.694975'),
(5,'admin','0003_logentry_add_action_flag_choices','2025-12-15 06:59:37.710737'),
(6,'contenttypes','0002_remove_content_type_name','2025-12-15 06:59:37.821690'),
(7,'auth','0002_alter_permission_name_max_length','2025-12-15 06:59:37.916937'),
(8,'auth','0003_alter_user_email_max_length','2025-12-15 06:59:37.948463'),
(9,'auth','0004_alter_user_username_opts','2025-12-15 06:59:37.970168'),
(10,'auth','0005_alter_user_last_login_null','2025-12-15 06:59:38.059752'),
(11,'auth','0006_require_contenttypes_0002','2025-12-15 06:59:38.059752'),
(12,'auth','0007_alter_validators_add_error_messages','2025-12-15 06:59:38.075832'),
(13,'auth','0008_alter_user_username_max_length','2025-12-15 06:59:38.218403'),
(14,'auth','0009_alter_user_last_name_max_length','2025-12-15 06:59:38.320419'),
(15,'auth','0010_alter_group_name_max_length','2025-12-15 06:59:38.346180'),
(16,'auth','0011_update_proxy_permissions','2025-12-15 06:59:38.346180'),
(17,'auth','0012_alter_user_first_name_max_length','2025-12-15 06:59:38.441184'),
(18,'realapp','0001_initial','2025-12-15 06:59:38.472730'),
(19,'realapp','0002_addnotification_admin_designer_registration_and_more','2025-12-15 06:59:39.479391'),
(20,'realapp','0003_designer_status','2025-12-15 06:59:39.558600'),
(21,'realapp','0004_booking_actual_start_date_booking_expected_end_date_and_more','2025-12-15 06:59:39.637573'),
(22,'realapp','0005_registration_otp','2025-12-15 06:59:39.669242'),
(23,'realapp','0006_designer_otp','2025-12-15 06:59:39.717337'),
(24,'sessions','0001_initial','2025-12-15 06:59:39.813300');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('di0dvy5q3e4l5bpin1xktyhqr09mg6f7','eyJlbWFpbCI6ImJja3IyMDAzQGdtYWlsLmNvbSIsImNhbl9yZXNldF9kZXNpZ25lcl9wYXNzd29yZCI6dHJ1ZX0:1vXYTM:hHlZraFLCnYjH3nDcY3EYSJjbR5g0i-QSSxRNnC_BNE','2026-01-05 05:28:44.094728');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `date_posted` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `notification` */

insert  into `notification`(`id`,`title`,`description`,`date_posted`) values 
(1,'New Designer Registration','Chennakesava Reddy has registered as a designer. Please review her profile and approve/decline.','2025-12-15 07:05:14.745513');

/*Table structure for table `register` */

DROP TABLE IF EXISTS `register`;

CREATE TABLE `register` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `profile_image` varchar(100) DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `mobile_number` varchar(10) NOT NULL,
  `password` varchar(100) NOT NULL,
  `address` longtext NOT NULL,
  `city` varchar(50) NOT NULL,
  `pincode` int NOT NULL,
  `status` varchar(20) NOT NULL,
  `otp` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `register` */

insert  into `register`(`id`,`profile_image`,`name`,`email`,`mobile_number`,`password`,`address`,`city`,`pincode`,`status`,`otp`) values 
(3,'profiles/Gemini_Generated_Image_mc0lawmc0lawmc0l_w8TVztT.png','Rama','bckr2003@gmail.com','9666933312','pbkdf2_sha256$1000000$dSxfK6OiHzqjwM9iHbYMTA$YaxuwL0ilIphfwo4jw5djCLewQDLYiV0qL2FndjLrAE=','SR nagar','Hyderbad',500056,'accepted',NULL),
(4,'profiles/Gemini_Generated_Image_mc0lawmc0lawmc0l_gmBsPkc.png','Rama','radhakaitha35@gmail.com','9666933312','pbkdf2_sha256$1000000$gGD3i1lgwe1XUQD3R1mL7M$Jx0aHPYknkmKDQd1650Yon7lsuhLwLVzS+H5uFiDF+I=','kphb colony','Warangal',500054,'accepted',NULL);

/*Table structure for table `review` */

DROP TABLE IF EXISTS `review`;

CREATE TABLE `review` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` smallint unsigned NOT NULL,
  `comment` longtext,
  `created_at` datetime(6) NOT NULL,
  `booking_id` bigint NOT NULL,
  `customer_id` bigint NOT NULL,
  `designer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `booking_id` (`booking_id`),
  KEY `Review_customer_id_7171ab32_fk_Register_id` (`customer_id`),
  KEY `Review_designer_id_3239ca71_fk_Designer_id` (`designer_id`),
  CONSTRAINT `Review_booking_id_a9b0db53_fk_Booking_id` FOREIGN KEY (`booking_id`) REFERENCES `booking` (`id`),
  CONSTRAINT `Review_customer_id_7171ab32_fk_Register_id` FOREIGN KEY (`customer_id`) REFERENCES `register` (`id`),
  CONSTRAINT `Review_designer_id_3239ca71_fk_Designer_id` FOREIGN KEY (`designer_id`) REFERENCES `designer` (`id`),
  CONSTRAINT `review_chk_1` CHECK ((`rating` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `review` */

insert  into `review`(`id`,`rating`,`comment`,`created_at`,`booking_id`,`customer_id`,`designer_id`) values 
(2,5,'Fast Delivery','2025-12-16 10:54:49.115163',4,3,1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
