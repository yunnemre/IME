-- --------------------------------------------------------
-- Sunucu:                       127.0.0.1
-- Sunucu sürümü:                10.4.24-MariaDB - mariadb.org binary distribution
-- Sunucu İşletim Sistemi:       Win64
-- HeidiSQL Sürüm:               11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- webadminoruser için veritabanı yapısı dökülüyor
CREATE DATABASE IF NOT EXISTS `webadminoruser` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `webadminoruser`;

-- tablo yapısı dökülüyor webadminoruser.admingrs
CREATE TABLE IF NOT EXISTS `admingrs` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `AdminUserName` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`Id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- webadminoruser.admingrs: ~0 rows (yaklaşık) tablosu için veriler indiriliyor
/*!40000 ALTER TABLE `admingrs` DISABLE KEYS */;
INSERT INTO `admingrs` (`Id`, `AdminUserName`, `password`) VALUES
	(2, 'yunn', '2');
/*!40000 ALTER TABLE `admingrs` ENABLE KEYS */;

-- tablo yapısı dökülüyor webadminoruser.kytblgileri
CREATE TABLE IF NOT EXISTS `kytblgileri` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `kullaniciadi` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `hash` varchar(50) NOT NULL,
  PRIMARY KEY (`Id`,`hash`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- webadminoruser.kytblgileri: ~5 rows (yaklaşık) tablosu için veriler indiriliyor
/*!40000 ALTER TABLE `kytblgileri` DISABLE KEYS */;
INSERT INTO `kytblgileri` (`Id`, `kullaniciadi`, `email`, `password`, `hash`) VALUES
	(1, 'unique', 'yucinf@gmail.com', '12421326437', 'cdd8b7d7afc1cd94'),
	(5, 'uniqueas', 'ynns1002@gmail.com', 'hasansabbah', '22caf78d09d0b632'),
	(6, 'sfas', 'knavesmusic55@gmail.com', 'yunn', '0bef2979b62144e4'),
	(7, 'hasnan', 'asklgjaslkgaşg@sklagjlasg.coom', 'asgasgag', 'sg'),
	(8, 'asgasgag', 'agasgag', 'asgasg', 'agsasg');
/*!40000 ALTER TABLE `kytblgileri` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
