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


-- web için veritabanı yapısı dökülüyor
CREATE DATABASE IF NOT EXISTS `web` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `web`;

-- tablo yapısı dökülüyor web.download
CREATE TABLE IF NOT EXISTS `download` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `DTarih` datetime DEFAULT NULL,
  `DName` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- web.download: ~4 rows (yaklaşık) tablosu için veriler indiriliyor
/*!40000 ALTER TABLE `download` DISABLE KEYS */;
INSERT INTO `download` (`Id`, `DTarih`, `DName`) VALUES
	(3, '2022-05-18 20:52:29', 'ChromeSetup (2).exe'),
	(4, '2022-05-18 20:54:33', 'ChromeSetup (3).exe'),
	(5, '2022-05-18 20:55:41', 'ChromeSetup (4).exe'),
	(6, '2022-05-18 20:56:46', 'ChromeSetup (5).exe'),
	(8, '2022-05-29 13:41:11', 'ChromeSetup (2).exe');
/*!40000 ALTER TABLE `download` ENABLE KEYS */;

-- tablo yapısı dökülüyor web.history
CREATE TABLE IF NOT EXISTS `history` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `HTarih` datetime NOT NULL,
  `HPage` varchar(50) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=642 DEFAULT CHARSET=utf8mb4;

-- web.history: ~162 rows (yaklaşık) tablosu için veriler indiriliyor
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
INSERT INTO `history` (`Id`, `HTarih`, `HPage`) VALUES
	(446, '2022-05-07 17:10:28', 'https://www.youtube.com/'),
	(447, '2022-05-07 17:10:32', 'https://google.com/'),
	(448, '2022-05-07 17:10:32', 'https://www.google.com/'),
	(449, '2022-05-10 11:10:09', 'https://www.youtube.com/'),
	(450, '2022-05-10 11:11:16', 'https://www.google.com/search?q=http://localhost/h'),
	(451, '2022-05-10 11:12:00', 'http://localhost/history/data.php'),
	(452, '2022-05-13 19:25:26', 'http://localhost/hew.html'),
	(453, '2022-05-13 19:25:41', 'http://localhost/history/data.php'),
	(454, '2022-05-13 19:26:05', 'http://localhost/hew.html'),
	(455, '2022-05-14 15:46:31', 'https://www.google.com/search?q=http://localhost/h'),
	(456, '2022-05-14 15:46:33', 'http://localhost/hew.html'),
	(457, '2022-05-14 15:46:42', 'http://localhost/hew.html'),
	(458, '2022-05-14 15:49:31', 'http://localhost/hew.html'),
	(459, '2022-05-14 15:50:23', 'http://localhost/hew.html'),
	(460, '2022-05-14 15:51:21', 'http://localhost/hew.html'),
	(461, '2022-05-14 15:55:00', 'file:///C:/Users/Yunn/PycharmProjects/pythonProjec'),
	(462, '2022-05-14 15:55:04', 'http://localhost/history/data.php'),
	(463, '2022-05-14 15:57:07', 'https://www.youtube.com/'),
	(464, '2022-05-14 15:57:11', 'https://www.youtube.com/watch?v=4cReydyTn7Q'),
	(467, '2022-05-14 15:59:50', 'http://localhost/history/data.php'),
	(468, '2022-05-14 16:03:18', 'http://localhost/history/data.php'),
	(470, '2022-05-14 16:50:56', 'http://localhost/login/mctas.php?yenile=03781c4d8f'),
	(471, '2022-05-16 12:52:17', 'https://accounts.google.com/ServiceLogin?service=m'),
	(472, '2022-05-16 12:52:17', 'https://accounts.google.com/signin/v2/identifier?s'),
	(473, '2022-05-16 13:00:02', 'http://localhost/history/data.php'),
	(474, '2022-05-16 13:04:55', 'http://localhost/login/login.php'),
	(475, '2022-05-16 13:05:05', 'http://localhost/index/Adminindex.php'),
	(476, '2022-05-16 17:55:16', 'http://localhost/index/index.php'),
	(477, '2022-05-16 17:55:20', 'http://localhost/history/data.php'),
	(478, '2022-05-16 17:55:22', 'http://localhost/index/index.php'),
	(479, '2022-05-16 17:55:22', 'http://localhost/index/index.php#urunler'),
	(480, '2022-05-16 17:55:23', 'http://localhost/index/index.php#referanslar'),
	(481, '2022-05-16 17:55:24', 'http://localhost/index/index.php#hesapbilgileri'),
	(482, '2022-05-16 18:04:07', 'http://localhost/index/index.php'),
	(483, '2022-05-16 21:20:08', 'https://google.com/'),
	(484, '2022-05-16 21:20:09', 'https://www.google.com/'),
	(485, '2022-05-16 21:20:11', 'http://localhost/login/login.php'),
	(486, '2022-05-16 21:20:26', 'http://localhost/index/Adminindex.php'),
	(487, '2022-05-16 21:20:27', 'http://localhost/login/login.php'),
	(488, '2022-05-16 21:20:39', 'http://localhost/index/index.php?user=uniqueas'),
	(489, '2022-05-16 21:20:52', 'http://localhost/history/data.php'),
	(490, '2022-05-16 21:20:55', 'http://localhost/index/index.php?user=uniqueas'),
	(491, '2022-05-16 21:21:06', 'http://localhost/login/login.php'),
	(492, '2022-05-16 21:21:19', 'http://localhost/index/index.php?user=uniqueas'),
	(493, '2022-05-16 21:21:23', 'http://localhost/history/data.php'),
	(494, '2022-05-16 21:21:24', 'http://localhost/index/index.php?user=uniqueas'),
	(495, '2022-05-16 21:21:27', 'http://localhost/history/data.php'),
	(498, '2022-05-16 21:21:37', 'http://localhost/index/index.php?user=uniqueas'),
	(499, '2022-05-16 21:21:42', 'http://localhost/history/data.php'),
	(500, '2022-05-16 21:21:52', 'http://localhost/index/index.php?user=uniqueas'),
	(501, '2022-05-16 21:21:56', 'http://localhost/history/data.php'),
	(502, '2022-05-16 21:21:58', 'http://localhost/index/index.php?user=uniqueas'),
	(503, '2022-05-16 21:21:59', 'http://localhost/index/index.php?user=uniqueas#ref'),
	(504, '2022-05-16 21:22:00', 'http://localhost/index/index.php?user=uniqueas#uru'),
	(505, '2022-05-16 21:22:01', 'http://localhost/history/data.php'),
	(506, '2022-05-16 21:22:02', 'http://localhost/index/index.php?user=uniqueas#uru'),
	(507, '2022-05-16 21:22:08', 'https://google.com/'),
	(508, '2022-05-16 21:22:09', 'https://www.google.com/'),
	(509, '2022-05-16 21:22:13', 'https://google.com/'),
	(510, '2022-05-16 21:22:13', 'https://www.google.com/'),
	(511, '2022-05-16 21:22:14', 'http://localhost/login/login.php'),
	(512, '2022-05-16 21:22:42', 'https://www.google.com/'),
	(513, '2022-05-16 21:22:43', 'http://localhost/login/login.php'),
	(514, '2022-05-16 21:22:45', 'https://google.com/'),
	(515, '2022-05-16 21:22:46', 'https://www.google.com/'),
	(516, '2022-05-16 21:24:01', 'http://localhost/login/login.php'),
	(517, '2022-05-16 21:25:48', 'https://www.google.com/intl/tr/gmail/about/'),
	(518, '2022-05-16 21:25:51', 'http://localhost/login/login.php'),
	(519, '2022-05-16 21:26:04', 'http://localhost/index/index.php?user=uniqueas'),
	(520, '2022-05-16 21:26:12', 'http://localhost/history/data.php'),
	(521, '2022-05-16 21:26:35', 'http://localhost/index/index.php?user=uniqueas'),
	(522, '2022-05-16 21:26:42', 'http://localhost/login/login.php'),
	(523, '2022-05-16 21:26:44', 'https://google.com/'),
	(524, '2022-05-16 21:26:45', 'https://www.google.com/'),
	(525, '2022-05-16 21:26:48', 'http://localhost/login/login.php'),
	(526, '2022-05-18 18:54:53', 'http://localhost/login/login.php'),
	(527, '2022-05-18 18:55:05', 'http://localhost:63342/htdocs/index/index.php?user'),
	(528, '2022-05-18 18:55:25', 'http://localhost/login/login.php'),
	(529, '2022-05-18 18:55:49', 'http://localhost:63342/htdocs/index/index.php?user'),
	(530, '2022-05-18 18:57:14', 'http://localhost/login/login.php'),
	(531, '2022-05-18 18:57:33', 'http://localhost:63342/htdocs/index/index.php?user'),
	(532, '2022-05-18 18:58:12', 'http://localhost/login/login.php'),
	(533, '2022-05-18 18:59:25', 'http://localhost:63342/htdocs/index/index.php?user'),
	(534, '2022-05-18 18:59:46', 'http://localhost:63342/htdocs/index/index.php?user'),
	(535, '2022-05-18 18:59:48', 'https://www.google.com/search?q=http://localhost:6'),
	(536, '2022-05-18 18:59:51', 'http://localhost:63342/htdocs/index/index.php?user'),
	(537, '2022-05-18 19:03:01', 'http://localhost/login/login.php'),
	(538, '2022-05-18 19:03:05', 'http://localhost:63342/htdocs/index/index.php?user'),
	(541, '2022-05-18 19:03:11', 'http://localhost/history/data.php'),
	(542, '2022-05-18 19:03:19', 'http://localhost:63342/htdocs/index/index.php?user'),
	(543, '2022-05-18 19:03:21', 'http://localhost:63342/htdocs/index/support.php?us'),
	(544, '2022-05-18 19:03:32', 'http://localhost:63342/htdocs/index/index.php?user'),
	(545, '2022-05-18 19:03:35', 'http://localhost:63342/htdocs/index/index.php?user'),
	(546, '2022-05-18 20:50:02', 'http://localhost/login/login.php'),
	(547, '2022-05-18 20:50:12', 'http://localhost:63342/htdocs/index/index.php?user'),
	(548, '2022-05-18 20:50:15', 'http://localhost:63342/htdocs/index/support.php?us'),
	(549, '2022-05-18 20:52:25', 'https://www.google.com/search?q=download chrome'),
	(550, '2022-05-18 20:52:26', 'https://www.google.com/intl/tr_tr/chrome/'),
	(551, '2022-05-18 20:52:29', 'https://www.google.com/intl/tr_tr/chrome/thank-you'),
	(552, '2022-05-18 20:52:38', 'http://localhost/index/index.php'),
	(553, '2022-05-18 20:52:43', 'http://localhost/index/index.php'),
	(554, '2022-05-18 20:52:44', 'http://localhost/index/index.php'),
	(555, '2022-05-18 20:52:51', 'http://localhost/index/index.php'),
	(556, '2022-05-18 20:54:25', 'https://www.google.com/search?q=chrome downlaod'),
	(557, '2022-05-18 20:54:31', 'https://www.google.com/intl/tr_tr/chrome/'),
	(558, '2022-05-18 20:54:34', 'https://www.google.com/intl/tr_tr/chrome/thank-you'),
	(559, '2022-05-18 20:54:36', 'http://localhost/index/index.php'),
	(560, '2022-05-18 20:55:37', 'https://www.google.com/search?q=download chrome'),
	(561, '2022-05-18 20:55:39', 'https://www.google.com/intl/tr_tr/chrome/'),
	(562, '2022-05-18 20:55:41', 'https://www.google.com/intl/tr_tr/chrome/thank-you'),
	(563, '2022-05-18 20:55:48', 'http://localhost/index/index.php'),
	(564, '2022-05-18 20:56:42', 'https://www.google.com/search?q=chrome download'),
	(565, '2022-05-18 20:56:44', 'https://www.google.com/intl/tr_tr/chrome/'),
	(566, '2022-05-18 20:56:47', 'https://www.google.com/intl/tr_tr/chrome/thank-you'),
	(567, '2022-05-18 20:56:58', 'http://localhost/index/index.php'),
	(568, '2022-05-18 20:57:00', 'https://www.google.com/intl/tr_tr/chrome/thank-you'),
	(569, '2022-05-18 21:08:49', 'http://localhost/login/login.php'),
	(579, '2022-05-22 13:49:25', 'https://www.youtube.com/'),
	(580, '2022-05-22 13:55:46', 'https://google.com/'),
	(581, '2022-05-22 13:55:47', 'https://www.google.com/'),
	(582, '2022-05-22 14:19:17', 'http://localhost/download/download.php'),
	(583, '2022-05-22 14:19:21', 'http://localhost/history/data.php'),
	(584, '2022-05-22 14:23:37', 'https://google.com/'),
	(585, '2022-05-22 14:23:37', 'https://www.google.com/'),
	(586, '2022-05-22 14:25:19', 'http://localhost/login/login.php'),
	(587, '2022-05-22 14:25:28', 'http://localhost/index/Adminindex.php'),
	(588, '2022-05-22 14:28:21', 'https://www.google.com/'),
	(589, '2022-05-22 14:41:56', 'https://www.youtube.com/'),
	(590, '2022-05-22 14:42:57', 'https://www.youtube.com/watch?v=te11f-2YwRY'),
	(591, '2022-05-22 14:45:20', 'https://www.youtube.com/watch?v=hjjS6do6zIQ'),
	(592, '2022-05-24 00:04:29', 'https://www.youtube.com/'),
	(593, '2022-05-24 00:21:51', 'http://localhost/history/data.php'),
	(594, '2022-05-24 00:21:57', 'https://www.youtube.com/'),
	(595, '2022-05-24 00:22:03', 'http://localhost/login/login.php'),
	(596, '2022-05-24 00:22:12', 'http://localhost/index/Adminindex.php'),
	(597, '2022-05-24 00:22:48', 'http://localhost/login/login.php'),
	(598, '2022-05-24 00:22:57', 'http://localhost:63343/htdocs/index/index.php?user'),
	(599, '2022-05-24 00:23:25', 'http://localhost:63343/htdocs/index/index.php?user'),
	(600, '2022-05-24 00:23:28', 'http://localhost/history/data.php'),
	(601, '2022-05-24 00:23:29', 'http://localhost:63343/htdocs/index/index.php?user'),
	(602, '2022-05-24 00:23:31', 'http://localhost:63343/htdocs/index/index.php?user'),
	(603, '2022-05-24 00:23:33', 'http://localhost:63343/htdocs/index/support.php?us'),
	(604, '2022-05-24 00:23:51', 'http://localhost:63343/htdocs/index/index.php?user'),
	(605, '2022-05-24 00:23:52', 'http://localhost:63343/htdocs/index/index.php?user'),
	(606, '2022-05-24 00:23:52', 'http://localhost/login/login.php'),
	(607, '2022-05-24 00:23:58', 'http://localhost/index/Adminindex.php'),
	(608, '2022-05-24 00:24:01', 'http://localhost/login/login.php'),
	(609, '2022-05-24 00:24:03', 'http://localhost/index/Adminindex.php'),
	(610, '2022-05-24 00:24:05', 'http://localhost/login/login.php'),
	(611, '2022-05-24 00:24:07', 'http://localhost/index/Adminindex.php'),
	(612, '2022-05-24 00:26:45', 'http://localhost/index/Adminindex.php#'),
	(613, '2022-05-24 00:29:26', 'http://localhost/login/login.php'),
	(614, '2022-05-24 11:04:39', 'http://localhost/login/login.php'),
	(615, '2022-05-24 11:04:56', 'http://localhost/index/Adminindex.php'),
	(616, '2022-05-24 11:04:59', 'http://localhost/login/login.php'),
	(617, '2022-05-24 11:05:23', 'http://localhost:63343/htdocs/index/index.php?user'),
	(618, '2022-05-24 11:05:35', 'http://localhost:63343/htdocs/index/index.php?user'),
	(619, '2022-05-24 11:05:38', 'http://localhost/history/data.php'),
	(620, '2022-05-24 11:05:41', 'http://localhost:63343/htdocs/index/index.php?user'),
	(621, '2022-05-24 11:05:44', 'http://localhost:63343/htdocs/index/index.php?user'),
	(622, '2022-05-24 11:05:45', 'http://localhost:63343/htdocs/index/support.php?us');
/*!40000 ALTER TABLE `history` ENABLE KEYS */;

-- tablo yapısı dökülüyor web.support
CREATE TABLE IF NOT EXISTS `support` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `baslik` varchar(50) NOT NULL,
  `icerik` text NOT NULL,
  `durum` varchar(50) DEFAULT 'kontrol edilmedi',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

-- web.support: ~6 rows (yaklaşık) tablosu için veriler indiriliyor
/*!40000 ALTER TABLE `support` DISABLE KEYS */;
INSERT INTO `support` (`Id`, `email`, `baslik`, `icerik`, `durum`) VALUES
	(1, 'ynns1002@gmail.com', 'Yunus Emre Dinler', 'bu son olsun bu son', 'kontrol edilmedi'),
	(3, 'ynns1002@gmail.com', 'Yunus Emre Dinlerasgas', 'sagasg\r\nasg\r\nas\r\ngas\r\ngsagspogsaşlgasgas\r\ngas\r\ngasklşgsakgsagasg,\r\nasgli\r\nasg', 'kontrol edilmedi'),
	(4, 'ynns1002@gmail.com', 'yunn', 'asşlasgşlkasgşialsg\r\nasgasgk\r\nasg\r\nasg\r\nasgşiasg', ''),
	(5, 'ynns1002@gmail.com', 'ynns1002@gmail.com', 'ynns1002@gmail.com', 'kontrol edilmedi'),
	(6, 'ynns1002@gmail.com', 'sagasg', 'asdasdasfg', 'kontrol edilmedi'),
	(7, 'knavesmusic55@gmail.com', 'sfas', 'asgasyunaslasgşlasjşgasgas\r\n,gaslgasg\r\nasgasgşasikasşlgasgasşgkasşlgasg\r\naskşlgaskgşlaskşlgasgkaşslgkasşgkaşslgşasg', 'kontrol edilmedi'),
	(8, 'ynns1002@gmail.com', 'help', 'help', 'kontrol edilmedi'),
	(9, 'ynns1002@gmail.com', 'help', 'helopassag', 'kontrol edilmedi'),
	(10, 'asgasg', 'asgasga', 'sgagag', 'kontrol edilmedi');
/*!40000 ALTER TABLE `support` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
