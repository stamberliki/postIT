-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Oct 22, 2016 at 08:38 PM
-- Server version: 10.1.13-MariaDB
-- PHP Version: 5.6.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `webdev2`
--

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `commentID` int(11) NOT NULL,
  `comment` varchar(125) NOT NULL,
  `imgID` int(11) NOT NULL,
  `username` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `comments`
--

INSERT INTO `comments` (`commentID`, `comment`, `imgID`, `username`) VALUES
(1, 'test', 12633736, 'admin'),
(2, 'test', 34, 'admin'),
(3, 'sdugfrisheio', 34, 'admin'),
(4, 'ano ang sabi ng driver ng truck sa nagtatawid na baka? ...', 33, 'admin'),
(5, 'hi(gh) josh', 32, 'admin'),
(6, 'Briefcase!', 29, 'admin'),
(7, 'Briefcase!', 29, 'admin'),
(8, 'he''s dead', 21, 'admin'),
(9, 'he''s dead', 21, 'admin'),
(10, 'SONA!', 18, 'admin'),
(11, 'SONA!', 18, 'admin'),
(12, 'SONA!', 18, 'admin'),
(13, 'SONA!', 18, 'admin'),
(14, 'SONA!', 18, 'admin'),
(15, 'SONA!', 18, 'admin'),
(16, 'dsgsdghsd', 18, 'admin'),
(17, 'dsggsd\r\n7\r\n\r\n', 18, 'admin'),
(18, 'dsggsd\r\n7\r\n\r\n', 18, 'admin'),
(19, 'dsggsd\r\n7\r\n\r\n', 18, 'admin'),
(20, 'dsggsd\r\n7\r\n\r\n', 18, 'admin'),
(21, 'dsggsd\r\n7\r\n\r\n', 18, 'admin'),
(22, 'heelo?', 18, 'admin'),
(23, 'zero seconds', 18, 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `imahe`
--

CREATE TABLE `imahe` (
  `imgID` int(11) NOT NULL,
  `imgName` varchar(100) NOT NULL,
  `caption` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `imahe`
--

INSERT INTO `imahe` (`imgID`, `imgName`, `caption`) VALUES
(1, 'd6f.jpg', 'dafaq'),
(2, 'maxresdefault.jpg', 'we are the knights!'),
(3, 'Untitled.jpg', 'yeeeyyy!!!'),
(4, 'final-fantasy-vi-espers-and.jpg', 'woooo!'),
(5, 'Unhelpful-High-School-Teacher.jpg', 'Scumbag teacher'),
(6, 'long-posts_c_184757.jpg', 'A long post'),
(7, 'avnNr5X_460s.jpg', 'dayum....'),
(8, '20160827_134327.jpg', '645645645'),
(9, '20160827_131806.jpg', 'renzooo'),
(10, '767-0-1447626651.png', 'WOW!'),
(11, 'QJvbmwL.jpg', '>:)'),
(12, 'ready.png', 'Ready for retake'),
(13, '4.jpg', 'Crystal Maiden '),
(16, 'RichaelMosen.png', 'Noice!'),
(17, 'iya.jpg', 'Yamete! senpai'),
(18, 'original.jpg', 'Sona'),
(19, '014.png', 'Why Won you peek'),
(20, 'tumblr_mrre93MI0Q1s9b5qso3_400.gif', '.GIF'),
(21, 'm012.jpg', 'Sinbad is dead'),
(22, 'Sneaky_Akeno_Kiss.gif', 'Again With Gif'),
(23, 'Hagard.png', 'Bean'),
(24, '14642353_1200318870011413_2252054927565436322_n.jpg', 'Kiyaaaahhh'),
(25, '14341423_120300000165732329_1155199228_n.png', 'hahahahahhaha'),
(26, 'PicMonkey Collage.jpg', 'Monster Musume'),
(27, '14718823_1200319790011321_8271044929725763767_n.jpg', 'Fabulous~'),
(28, 'b1df964d92b6644d7d469866abb51770.jpg', 'Smile! Boo'),
(29, '328810-Rainbow_Six_Siege-video_games-artwork.jpg', 'Tara Rainbow ta'),
(30, '14502783_1312882095411296_7704320112139669621_n.jpg', '...'),
(31, '69.png', 'Valkyrieeeennn'),
(32, 'JOsh.jpg', 'Hi finals'),
(33, '9c5c3634141691707634676589_700w_0.jpg', 'BEEFF BEEFFF'),
(34, '12633736_10153466361751523_8490688403056339941_o.jpg', 'testing');

-- --------------------------------------------------------

--
-- Table structure for table `profiles`
--

CREATE TABLE `profiles` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `profiles`
--

INSERT INTO `profiles` (`username`, `password`) VALUES
('admin', 'admin'),
('bean@gmail.com', '09329096551'),
('user1', 'pass1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`commentID`);

--
-- Indexes for table `imahe`
--
ALTER TABLE `imahe`
  ADD PRIMARY KEY (`imgID`);

--
-- Indexes for table `profiles`
--
ALTER TABLE `profiles`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `commentID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
--
-- AUTO_INCREMENT for table `imahe`
--
ALTER TABLE `imahe`
  MODIFY `imgID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
