-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 05, 2024 at 06:51 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `digital_form_b`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('c5d00298c45d');

-- --------------------------------------------------------

--
-- Table structure for table `child_data`
--

CREATE TABLE `child_data` (
  `chi_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `par_id` int(11) NOT NULL,
  `child_name` varchar(30) DEFAULT NULL,
  `child_birth_date` date NOT NULL,
  `child_gender` varchar(20) DEFAULT NULL,
  `new_cnic` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `disability` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `child_data`
--

INSERT INTO `child_data` (`chi_id`, `user_id`, `par_id`, `child_name`, `child_birth_date`, `child_gender`, `new_cnic`, `created_at`, `updated_at`, `disability`) VALUES
(1, 5, 2, 'asad Khan', '2001-01-03', 'Male', '11101-3232743-3', '2024-03-26 02:11:12', '2024-03-26 02:21:39', 'No'),
(4, 5, 2, 'Asia', '1997-03-15', 'Female', '11101-3233543-4', '2024-03-26 21:33:34', '2024-03-26 21:33:34', 'No'),
(7, 7, 4, 'Waseem', '2024-03-07', 'Male', '11101-3232843-4', '2024-03-27 06:48:54', '2024-03-27 06:48:54', 'No'),
(8, 7, 4, 'bahmal', '2024-03-13', 'Male', '11101-3232742-1', '2024-03-27 06:49:09', '2024-03-27 06:49:09', 'No'),
(9, 7, 4, 'sana sadiq', '2024-03-16', 'Female', '11101-3232743-2', '2024-03-27 06:49:24', '2024-03-27 06:49:24', 'No'),
(10, 8, 5, 'rahman', '2024-03-14', 'Male', '11101-3232743-7', '2024-03-27 10:32:39', '2024-03-27 10:32:39', 'No'),
(11, 10, 6, 'Sennan Khan', '2024-04-01', 'Male', '11101-3232743-9', '2024-04-06 11:56:46', '2024-04-06 11:57:48', 'No'),
(12, 8, 5, 'Waseem', '2024-04-19', 'Male', '11101-3232743-5', '2024-04-06 13:22:46', '2024-04-06 13:22:46', 'No'),
(13, 8, 5, 'fatma', '2024-04-17', 'Female', NULL, '2024-04-21 15:12:51', '2024-04-21 15:12:51', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `complaints`
--

CREATE TABLE `complaints` (
  `comp_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `send_details` varchar(255) NOT NULL,
  `received_details` varchar(255) DEFAULT NULL,
  `status` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `complaints`
--

INSERT INTO `complaints` (`comp_id`, `user_id`, `title`, `send_details`, `received_details`, `status`, `created_at`, `updated_at`) VALUES
(1, 5, 'Unable to access', 'Unable to access the Form-B application.', 'i dont want', 'Rejected', '2024-03-24 20:24:59', '2024-03-25 20:20:49'),
(3, 5, 'uploading documents.', 'Facing issues with uploading supporting documents.1', 'yes i can do this', 'Pending', '2024-03-25 06:47:20', '2024-03-25 20:36:11');

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `cont_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `contact_type` varchar(30) DEFAULT NULL,
  `contact_number` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `delivery_boy_handover`
--

CREATE TABLE `delivery_boy_handover` (
  `ho_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `par_id` int(11) NOT NULL,
  `drop_address` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `delivery_boy_handover`
--

INSERT INTO `delivery_boy_handover` (`ho_id`, `user_id`, `par_id`, `drop_address`, `status`, `created_at`, `updated_at`) VALUES
(4, 11, 2, 'Village 3 Waligai Post Office Wanara Dali Khel Kar', 'Deliver', '2024-04-11 12:06:43', '2024-04-11 12:12:22'),
(5, 9, 4, 'Village Darga Post Office Darga Tehsel Darga Distr', 'Deliver', '2024-04-21 15:18:06', '2024-04-21 15:20:09');

-- --------------------------------------------------------

--
-- Table structure for table `district`
--

CREATE TABLE `district` (
  `district_sno` int(11) NOT NULL,
  `district_province_sno` int(11) NOT NULL,
  `district_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `district`
--

INSERT INTO `district` (`district_sno`, `district_province_sno`, `district_name`) VALUES
(2, 6, 'Bannu'),
(3, 7, 'Wazir-N'),
(4, 6, 'Peshawar'),
(5, 6, 'Kohat'),
(6, 7, 'Sargodha'),
(7, 6, 'Karak'),
(8, 6, 'Tank'),
(9, 6, 'Lakki Marwat'),
(10, 6, 'D I Khan'),
(11, 6, 'Charsada'),
(12, 6, 'Nowshehra'),
(13, 6, 'Abbotabad'),
(14, 6, 'Haripur'),
(15, 6, 'Mansehra'),
(16, 6, 'Battagram'),
(17, 6, 'Kohistan (Upper)'),
(18, 6, 'Chitral (Upper)'),
(19, 6, 'Torghar'),
(20, 6, 'Shangla'),
(21, 6, 'Swat'),
(22, 6, 'Dir Upper'),
(23, 6, 'Dir Lower'),
(24, 6, 'Mardan'),
(25, 6, 'Malakand'),
(26, 6, 'Allai'),
(27, 6, 'Buner'),
(28, 6, 'Swabi'),
(29, 6, 'Hangu'),
(30, 6, 'Kolai Palas'),
(31, 6, 'Chitral (Lower)'),
(32, 6, 'Kohistan (Lower)'),
(33, 3, 'North Waziristan'),
(34, 3, 'South Waziristan '),
(36, 3, 'Kurram'),
(37, 3, 'Orakzai'),
(38, 3, 'Mohmand'),
(39, 3, 'Bajaur'),
(40, 3, 'Khyber'),
(41, 7, 'Rawalpindi'),
(42, 7, 'Bahawalpur'),
(43, 7, 'Rahim Yar Khan'),
(44, 7, 'DG Khan'),
(45, 7, 'Jampur'),
(46, 7, 'Kot Addu'),
(47, 7, 'Layya'),
(48, 7, 'Muzaffar Garh'),
(49, 7, 'Rajanpur'),
(50, 7, 'Tunsa'),
(51, 7, 'Chinnot'),
(52, 7, 'Faisalabad'),
(53, 7, 'Jhang'),
(54, 7, 'Toba Tek Singh'),
(55, 7, 'Gujranwala'),
(56, 7, 'Narowal'),
(57, 7, 'Sialkot'),
(58, 7, 'Gujrat'),
(59, 7, 'Hafizabad'),
(60, 7, 'Mandi Bahauddin'),
(61, 7, 'Wazirabad'),
(62, 7, 'Lahore'),
(63, 7, 'Nankana'),
(64, 7, 'Qasur'),
(65, 7, 'Shekhupura'),
(66, 7, 'Mianwali'),
(67, 7, 'Bakkar'),
(68, 7, 'Talagang'),
(69, 7, 'Khaniwal'),
(70, 7, 'Lodhran'),
(71, 7, 'Multan'),
(72, 7, 'Vehari'),
(73, 7, 'Attock'),
(74, 7, 'Chakwal'),
(75, 7, 'Jhelum'),
(76, 7, 'Murree'),
(77, 7, 'Okara'),
(78, 7, 'Pakpattan'),
(79, 7, 'Sahiwal'),
(80, 7, 'Khushab'),
(82, 8, 'Hyderabad'),
(83, 8, 'Dadu'),
(84, 8, 'Thatta'),
(85, 8, 'Badin'),
(86, 8, 'Khairpur'),
(87, 8, 'Sukkur'),
(88, 8, 'Nawabshah/ Shaheed Benazirabad'),
(89, 8, 'Ghotki'),
(90, 8, 'Naushahro Feroze'),
(91, 8, 'Karachi'),
(92, 8, 'Larkana'),
(93, 8, 'Jacobabad'),
(94, 8, 'Shikarpur'),
(95, 8, 'Mirpur Khas'),
(96, 8, 'Tharparkar'),
(97, 8, 'Sanghar'),
(98, 7, 'Umerkot'),
(99, 8, 'Qambar Shahdadkot'),
(100, 8, 'Jamshoro'),
(101, 8, 'Kashmore'),
(102, 8, 'Tando Muhammad Khan'),
(103, 8, 'Matiari'),
(104, 8, 'Sujawal'),
(105, 8, 'Tando Allahyar'),
(106, 2, 'Awaran'),
(107, 2, 'Barkhan'),
(108, 2, 'Kachhi'),
(109, 2, 'Chagai'),
(110, 2, 'Chaman'),
(111, 2, 'Dera Bugti'),
(112, 2, 'Duki'),
(113, 2, 'Gwadar'),
(114, 2, 'Harnai'),
(115, 2, 'Hub'),
(116, 2, 'Jafarabad'),
(117, 2, 'Jhal Magsi'),
(118, 2, 'Kalat'),
(119, 2, 'Kech/Turbat'),
(120, 2, 'Kharan'),
(121, 2, 'Kohlu'),
(122, 2, 'Khuzdar'),
(123, 2, 'Lasbela'),
(124, 2, 'Loralai'),
(125, 2, 'Mastung'),
(126, 2, 'Musakhel'),
(127, 2, 'Nasirabad'),
(128, 2, 'Nushki'),
(129, 2, 'Qila Abdullah'),
(130, 2, 'Qila Saifullah'),
(131, 2, 'Panjgur'),
(132, 2, 'Pishin'),
(133, 2, 'Quetta'),
(134, 2, 'Sherani'),
(135, 2, 'Sibi'),
(136, 2, 'Sohbatpur'),
(137, 2, 'Surab'),
(138, 2, 'Washuk'),
(139, 2, 'Zhob'),
(140, 2, 'Ziarat'),
(141, 2, 'Lehri'),
(142, 2, 'Karezat-Barshore'),
(143, 4, 'Ghanche'),
(144, 4, 'Skardu'),
(145, 4, 'Shigar'),
(146, 4, 'Kharmang'),
(147, 4, 'Roundu'),
(148, 4, 'Ghizer'),
(149, 4, 'Gupis–Yasin'),
(150, 4, 'Gilgit'),
(151, 4, 'Hunza'),
(152, 4, 'Nagar'),
(153, 4, 'Astore'),
(154, 4, 'Diamer'),
(155, 4, 'Darel'),
(156, 4, 'Tangir'),
(157, 1, 'Muzaffarabad'),
(158, 1, 'Hattian Bala'),
(159, 1, 'Neelam Valley'),
(160, 1, 'Mirpur'),
(161, 1, 'Bhimber'),
(162, 1, 'Kotli'),
(163, 1, 'Poonch'),
(164, 1, 'Bagh'),
(165, 1, 'Haveli'),
(166, 1, 'Sudhanoti'),
(167, 5, 'Islamabad'),
(168, 7, 'Bahawalnagar');

-- --------------------------------------------------------

--
-- Table structure for table `documents`
--

CREATE TABLE `documents` (
  `doc_id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL,
  `expiry_date` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE `notification` (
  `n_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `notification_info` varchar(50) DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `is_check_by_manager` tinyint(1) DEFAULT NULL,
  `is_check_by_employee` tinyint(1) DEFAULT NULL,
  `is_check_by_parent` tinyint(1) DEFAULT NULL,
  `is_check_by_delivery_boy` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `notification`
--

INSERT INTO `notification` (`n_id`, `user_id`, `notification_info`, `end_date`, `is_check_by_manager`, `is_check_by_employee`, `is_check_by_parent`, `is_check_by_delivery_boy`, `created_at`, `updated_at`, `status`) VALUES
(1, 1, '1st', '2024-05-16', 0, 0, 0, 0, '2024-05-05 11:36:41', '2024-05-05 12:30:29', 'Live'),
(2, 1, '2nd', '2024-05-05', 0, 0, 0, 0, '2024-05-05 11:53:08', '2024-05-05 12:30:29', 'Live'),
(4, 1, '3rd', '2024-05-04', 0, 0, 0, 0, '2024-05-05 12:18:45', '2024-05-05 12:29:15', 'Ended'),
(5, 1, 'i want to inform you that sunday was holiday', '2024-05-31', 0, 0, 0, 0, '2024-05-05 15:57:34', '2024-05-05 15:57:34', 'Live');

-- --------------------------------------------------------

--
-- Table structure for table `parent_data`
--

CREATE TABLE `parent_data` (
  `par_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `crc_no` int(11) DEFAULT NULL,
  `father_name` varchar(30) DEFAULT NULL,
  `father_cnic` varchar(50) DEFAULT NULL,
  `father_finger` varchar(255) DEFAULT NULL,
  `mother_name` varchar(30) DEFAULT NULL,
  `mother_cnic` varchar(50) DEFAULT NULL,
  `mother_finger` varchar(255) DEFAULT NULL,
  `send_comment` varchar(255) DEFAULT NULL,
  `received_comment` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `status` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `forward_to_admin` tinyint(1) NOT NULL,
  `delivery_status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `parent_data`
--

INSERT INTO `parent_data` (`par_id`, `user_id`, `crc_no`, `father_name`, `father_cnic`, `father_finger`, `mother_name`, `mother_cnic`, `mother_finger`, `send_comment`, `received_comment`, `address`, `status`, `created_at`, `updated_at`, `forward_to_admin`, `delivery_status`) VALUES
(2, 5, 4327567, 'Inam Khan', '1110174185236', NULL, 'Sana Bibi', '1110115149143', NULL, 'I want to fix my second child date of birth', NULL, 'Village 3 Waligai Post Office Wanara Dali Khel Karak', 'Processing', '2024-03-23 23:39:31', '2024-04-11 12:12:22', 1, 'Received'),
(4, 7, 4322567, 'Aqib Ullah', '1110178945632', NULL, 'Jani Doshman', '3336985274147', NULL, 'I want to Create New form b', 'No any issue your form-b is successfully created', 'Village Darga Post Office Darga Tehsel Darga District Kandahar', 'Complete', '2024-03-26 21:55:56', '2024-04-21 15:20:09', 1, 'Received'),
(5, 8, 8058729, 'Malang Jan', '1254785654545', '1254785654545.BMP', 'Shadi Bala', '8789454564564', '8789454564564.BMP', 'I want to create new form B', NULL, 'Village 2 Waligai Post Office Wanara Dali Khel Karak', 'Complete', '2024-03-27 10:07:22', '2024-04-21 15:16:44', 1, 'No'),
(6, 10, 4322767, 'Manhaj Ud Din', '1234569855421', NULL, 'Gul Khana', '9874563254875', NULL, 'Please Add the parent data', NULL, 'Village 4 Waligai Post Office Wanara Dali Khel Karak', 'Processing', '2024-04-06 11:55:45', '2024-05-05 06:51:07', 1, 'No');

-- --------------------------------------------------------

--
-- Table structure for table `province`
--

CREATE TABLE `province` (
  `province_sno` int(11) NOT NULL,
  `province_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `province`
--

INSERT INTO `province` (`province_sno`, `province_name`) VALUES
(1, 'AJK'),
(2, 'BALOCHISTAN'),
(3, 'EX-FATA'),
(4, 'GILGAT BALTISTAN'),
(5, 'ISLAMABAD'),
(6, 'KP'),
(7, 'PUNJAB'),
(8, 'SINDH');

-- --------------------------------------------------------

--
-- Table structure for table `requests`
--

CREATE TABLE `requests` (
  `r_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `request_type` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `details` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `cnic` varchar(20) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `rol_name` varchar(20) DEFAULT NULL,
  `employee_province_sno` int(11) DEFAULT NULL,
  `employee_district_sno` int(11) DEFAULT NULL,
  `delivery_status` varchar(20) DEFAULT NULL,
  `password` varchar(256) DEFAULT NULL,
  `photo` varchar(256) DEFAULT NULL,
  `isActive` tinyint(1) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `phone`, `cnic`, `gender`, `rol_name`, `employee_province_sno`, `employee_district_sno`, `delivery_status`, `password`, `photo`, `isActive`, `created_at`, `updated_at`) VALUES
(1, 'Rauf Khalid', '03366645807', '1111111111111', 'Male', 'Administrator', 6, 5, 'Available', 'scrypt:32768:8:1$3vI7mJagp1Vqebb8$5b28eb200983b02e2eaa28907b068af667783ae18a36fc09ba5b576167057dcfac6e13efa2a4a254feecc96ca352beca5adae9e02815b413d5d3954cc00f99de', NULL, 1, '2024-03-23 23:39:31', '2024-05-05 05:32:14'),
(2, 'Imran Khan', '03408745963', '2222222222222', 'Male', 'Manager', 6, 2, 'Available', 'scrypt:32768:8:1$7ygCueXeUnRCOkgh$d59d34cbd0db2273d9d5c9d5f1174c2ec12b98fc1e1aacf6b26f1bdf65c09876d0013573d4562d2cc5b0e9114050e279a7236412ce26b0259129afb4af809f7b', NULL, 1, '2024-03-24 09:22:42', '2024-03-27 21:41:45'),
(4, 'Taib Khalid', '03409836430', '3333333333333', 'Male', 'Employee', 6, 2, 'Available', 'scrypt:32768:8:1$DRYV8n2pWGULm03p$044d9f19c4135c4f2c398309fb57dba5e059a599ba59f1fc9c6a6e0532ea5de5b4a420f7ff3b19c20a9bfa95023f7f8f155d53aeabc8718d97c5d6017203fa04', NULL, 1, '2024-03-24 09:26:39', '2024-05-05 06:38:39'),
(5, 'Inam Khan', '03406983412', '4444444444444', 'Male', 'Parent', 7, 6, 'Available', 'scrypt:32768:8:1$OJ4H4NxIBa9zVKG4$b3eb71159e967504c378fa7a5f0547096cee8abfecc814ea5a87fed106dc06142d92a4e48d3abdbbc58a5b44c01d3d9ad6ad8c0344ce7eb77ebf63f5a7491c98', NULL, 1, '2024-03-24 09:38:25', '2024-03-27 21:36:29'),
(6, 'Kaleem Khan', '03459863258', '5555555555555', 'Male', 'DeliveryBoy', 6, 2, 'Available', 'scrypt:32768:8:1$1Da353dRHmbo7Frt$aedfc7541f7ffca16f1e0b6d5328e97a8a6f33260afa689606181d69e6d1484280a5f37fb514b9bc7ee9adbae751cae72e9a6a28398069932ecb10884aae3149', NULL, 1, '2024-03-24 09:39:16', '2024-03-24 04:39:16'),
(7, 'Aqib Ullah', '03409836789', '6666666666666', 'Male', 'Parent', 6, 2, 'Available', 'scrypt:32768:8:1$kXinQThA1EZp4Dku$b3cd6fad26d13a5ec89c291ee7a07ece4274c9f7a79bff6769703d412ee00bb420f3abbd5ccbc5247abb23214b34eb70ac20a1ae18196d95b2d774eecfea0ffb', NULL, 1, '2024-03-25 16:10:38', '2024-03-25 11:10:38'),
(8, 'Malang Jan', '03407894568', '7777777777777', 'Male', 'Parent', 6, 5, 'Available', 'scrypt:32768:8:1$chAfKllGmuDsmTJV$f0c0403b02d3f2fbc29b80e838e7bea67730fcbd191161897616bc3789ce7b8dc21301fb8b4039b2c5571dff88cc767be214f4158acedd14e496995e2ff60d91', NULL, 1, '2024-03-27 15:05:58', '2024-04-21 15:08:15'),
(9, 'Danyal Khan', '03408855224', '8888888888888', 'Male', 'DeliveryBoy', 7, 6, 'Available', 'scrypt:32768:8:1$QVcfckNI9crzmK2P$22fc81adeb19400bcb9483a48bb90852a7f1a403b20f84f0cdcc97b9c48c045d73c9910edcf16319abd8dae244dc535a0f784c0e36fded0b0783751ff0d532df', NULL, 1, '2024-03-28 01:05:53', '2024-03-27 21:50:43'),
(10, 'Riffat Pasha', '03401342174', '9999999999999', 'Male', 'Parent', 6, 2, 'Available', 'scrypt:32768:8:1$BGAIoDNmgjuWDEIm$2cd72425fa5722e62c6e21437f59f7c2a4ec008f16cf596245352a7b7a97c029e0283bff1fefa310dff22e1410af663a54479052c2e4d815cac915c6fd44dd7f', NULL, 1, '2024-04-06 16:39:30', '2024-04-06 11:39:30'),
(11, 'Wahid Jamal', '03409966338', '8888888888889', 'Male', 'DeliveryBoy', 7, 49, 'Available', 'scrypt:32768:8:1$7pXVEH5GXfn8j3CE$551afc3f3cf370a2368b3aa45d558392f2bb84435b8aabe9a8b74eba3fdbf3491e74f7de19fa3b36adcfd6f668a2bf18f00165582af32143ca0f99df5622258a', NULL, 1, '2024-04-09 20:46:51', '2024-04-09 15:46:51');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `child_data`
--
ALTER TABLE `child_data`
  ADD PRIMARY KEY (`chi_id`),
  ADD UNIQUE KEY `new_cnic` (`new_cnic`),
  ADD KEY `par_id` (`par_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `complaints`
--
ALTER TABLE `complaints`
  ADD PRIMARY KEY (`comp_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`cont_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `delivery_boy_handover`
--
ALTER TABLE `delivery_boy_handover`
  ADD PRIMARY KEY (`ho_id`),
  ADD KEY `par_id` (`par_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `district`
--
ALTER TABLE `district`
  ADD PRIMARY KEY (`district_sno`),
  ADD UNIQUE KEY `district_name` (`district_name`),
  ADD KEY `district_province_sno` (`district_province_sno`);

--
-- Indexes for table `documents`
--
ALTER TABLE `documents`
  ADD PRIMARY KEY (`doc_id`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`n_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `parent_data`
--
ALTER TABLE `parent_data`
  ADD PRIMARY KEY (`par_id`),
  ADD UNIQUE KEY `father_cnic` (`father_cnic`),
  ADD UNIQUE KEY `mother_cnic` (`mother_cnic`),
  ADD UNIQUE KEY `crc_no` (`crc_no`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `province`
--
ALTER TABLE `province`
  ADD PRIMARY KEY (`province_sno`),
  ADD UNIQUE KEY `province_name` (`province_name`);

--
-- Indexes for table `requests`
--
ALTER TABLE `requests`
  ADD PRIMARY KEY (`r_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `cnic` (`cnic`),
  ADD UNIQUE KEY `phone` (`phone`),
  ADD KEY `employee_district_sno` (`employee_district_sno`),
  ADD KEY `employee_province_sno` (`employee_province_sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `child_data`
--
ALTER TABLE `child_data`
  MODIFY `chi_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `complaints`
--
ALTER TABLE `complaints`
  MODIFY `comp_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `cont_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `delivery_boy_handover`
--
ALTER TABLE `delivery_boy_handover`
  MODIFY `ho_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `district`
--
ALTER TABLE `district`
  MODIFY `district_sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=169;

--
-- AUTO_INCREMENT for table `documents`
--
ALTER TABLE `documents`
  MODIFY `doc_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `notification`
--
ALTER TABLE `notification`
  MODIFY `n_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `parent_data`
--
ALTER TABLE `parent_data`
  MODIFY `par_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `province`
--
ALTER TABLE `province`
  MODIFY `province_sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `requests`
--
ALTER TABLE `requests`
  MODIFY `r_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `child_data`
--
ALTER TABLE `child_data`
  ADD CONSTRAINT `child_data_ibfk_1` FOREIGN KEY (`par_id`) REFERENCES `parent_data` (`par_id`),
  ADD CONSTRAINT `child_data_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `complaints`
--
ALTER TABLE `complaints`
  ADD CONSTRAINT `complaints_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `contacts`
--
ALTER TABLE `contacts`
  ADD CONSTRAINT `contacts_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `delivery_boy_handover`
--
ALTER TABLE `delivery_boy_handover`
  ADD CONSTRAINT `delivery_boy_handover_ibfk_1` FOREIGN KEY (`par_id`) REFERENCES `parent_data` (`par_id`),
  ADD CONSTRAINT `delivery_boy_handover_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `district`
--
ALTER TABLE `district`
  ADD CONSTRAINT `district_ibfk_1` FOREIGN KEY (`district_province_sno`) REFERENCES `province` (`province_sno`);

--
-- Constraints for table `notification`
--
ALTER TABLE `notification`
  ADD CONSTRAINT `notification_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `parent_data`
--
ALTER TABLE `parent_data`
  ADD CONSTRAINT `parent_data_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `requests`
--
ALTER TABLE `requests`
  ADD CONSTRAINT `requests_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`employee_district_sno`) REFERENCES `district` (`district_sno`),
  ADD CONSTRAINT `users_ibfk_2` FOREIGN KEY (`employee_province_sno`) REFERENCES `province` (`province_sno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
