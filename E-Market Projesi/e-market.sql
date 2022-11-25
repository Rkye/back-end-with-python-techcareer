-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 25 Kas 2022, 15:10:52
-- Sunucu sürümü: 10.4.25-MariaDB
-- PHP Sürümü: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `e-market`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `categories`
--

CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `categories`
--

INSERT INTO `categories` (`id`, `name`) VALUES
(1, 'Cep Telefonu'),
(2, 'Laptop'),
(3, 'Tablet');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `name` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `feature` text NOT NULL,
  `image` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `category` text CHARACTER SET utf8 COLLATE utf8_turkish_ci NOT NULL,
  `stokAdet` int(11) NOT NULL,
  `price` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `products`
--

INSERT INTO `products` (`id`, `name`, `feature`, `image`, `category`, `stokAdet`, `price`) VALUES
(1, 'APPLE iPhone 11 64GB', '', 'apple.jpg', 'Cep Telefonu', 5, '15000'),
(2, 'HUAWEI Matebook', '', 'laptop.jpg', 'Laptop', 5, '16000'),
(3, 'SAMSUNG Galaxy TAB A7', '', '7.jpg', 'Tablet', 10, '2150'),
(4, 'SAMSUNG Galaxy A73', '', 'samtel.jpg', 'Cep Telefonu', 10, '12000'),
(5, 'ALCATEL 2020X Tuşlu Telefon', '', 'tel3.jpg', 'Cep Telefonu', 7, '1200'),
(6, 'HUAWEI Matepad T', '', 'tab.jpg', 'Tablet', 10, '1200'),
(7, 'Asus Laptop', '', '5.jpg', 'Laptop', 10, '10000');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `rolId` text NOT NULL,
  `name` text CHARACTER SET utf8mb4 NOT NULL,
  `username` text NOT NULL,
  `email` text NOT NULL,
  `password` text CHARACTER SET utf32 NOT NULL,
  `sepet` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `user`
--

INSERT INTO `user` (`id`, `rolId`, `name`, `username`, `email`, `password`, `sepet`) VALUES
(1, '1', 'Rukiye', 'Rukiye', 'rukiye@gmail.com', '12345678', ''),
(4, '2', 'hatice', 'hatice', 'hatice@gmail.com', '$5$rounds=535000$9PmkhIes7V.niw/N$4E/GpqRnC28LYW8QtvbVLj/XZ6zZp6aUcvZ8yFk87.A', ''),
(5, '2', 'zeynep', 'zeynep', 'zeynep@gmail.com', '$5$rounds=535000$N/PgTeUBHnDFPEjD$deJXvLtfJ2UTS9VvYO5eaI.Gi/fHxEYC0NNgXm4JzA5', ''),
(6, '2', 'sümeyye', 'sümeyye', 'sümeyye@gmail.com', '$5$rounds=535000$2mBdrt5dQjJLm3nE$qFIatLdrjXi7n9e2bV5Lg2faZylP3KzB/TbXrqntm5.', '');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Tablo için AUTO_INCREMENT değeri `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Tablo için AUTO_INCREMENT değeri `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
