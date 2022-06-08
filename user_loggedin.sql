-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:8889
-- Tiempo de generación: 08-06-2022 a las 15:20:21
-- Versión del servidor: 5.7.34
-- Versión de PHP: 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `registros`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `course_viewed`
--

CREATE TABLE `user_loggedin` (
  `id` bigint(20) NOT NULL,
  `id_event` bigint(10) NOT NULL,
  `eventname` varchar(255) NOT NULL,
  `component` varchar(100) NOT NULL,
  `action` varchar(100) NOT NULL,
  `objecttable` varchar(50) DEFAULT NULL,
  `objectid` bigint(10) DEFAULT NULL,
  `crud` varchar(1) NOT NULL,
  `edulevel` tinyint(1) NOT NULL,
  `ip` varchar(45) NOT NULL,
  `other` longtext NOT NULL,
  `timecreated` varchar(100) NOT NULL,
  `origin` varchar(10) NOT NULL,
  `userid` bigint(10) NOT NULL,
  `username` varchar(100) NOT NULL,
  `idnumber` varchar(255) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `corseid` bigint(10) NOT NULL,
  `coursefullname` varchar(254) NOT NULL,
  `shortname` varchar(254) NOT NULL,
  `courseidnumber` varchar(100) NOT NULL,
  `startdate` bigint(10) NOT NULL,
  `enddate` bigint(10) NOT NULL,
  `categoryid` bigint(10) NOT NULL,
  `name` varchar(255) NOT NULL,
  `categoryidnumber` varchar(255) DEFAULT NULL,
  `parent` bigint(10) NOT NULL,
  `coursecount` bigint(10) NOT NULL,
  `depth` bigint(10) NOT NULL,
  `path` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `course_viewed`
--
ALTER TABLE `course_viewed`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `course_viewed`
--
ALTER TABLE `course_viewed`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
