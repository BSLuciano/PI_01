DROP DATABASE IF EXISTS MERCADO;
CREATE DATABASE IF NOT EXISTS MERCADO;
USE MERCADO;

DROP TABLE IF EXISTS `producto`;
CREATE TABLE IF NOT EXISTS `producto` (
  	`IdProducto` varchar(25), 
	`marca` varchar(40), 
	`nombre` varchar(150), 
	`presentacion` varchar(30), 
	`categoria1` varchar(150), 
	`categoria2` varchar(150), 
	`categoria3` varchar(150),
    PRIMARY KEY (IdProducto)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\PI-01\\producto_mod.csv'
INTO TABLE `producto` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;


DROP TABLE IF EXISTS `sucursal`;
CREATE TABLE IF NOT EXISTS `sucursal` (
  	`IdSucursal` varchar(80),
	`IdComercio` int,
	`IdBandera` int,
	`banderaDescripcion` varchar(50),
	`comercioRazonSocial` varchar(120),
	`provincia` varchar(25),
	`localidad` varchar(40),
	`dirección` varchar(80),
	`lat` decimal(15,8),
	`lng`decimal(15,8),
	`sucursalNombre` varchar(50),
	`sucursalTipo` varchar(20),
    PRIMARY KEY (IdSucursal)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\PI-01\\sucursal_mod.csv'
INTO TABLE `sucursal` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;


set foreign_key_checks = 0;
DROP TABLE IF EXISTS `precio`;
CREATE TABLE IF NOT EXISTS `precio` (
  	`Precio` 		decimal(20,2),
    `IdProducto` 	VARCHAR(25),
  	`IdSucursal` 	VARCHAR(80),
  	`fecha_semana`  int,
    
    FOREIGN KEY (IdProducto) REFERENCES producto(IdProducto),
    FOREIGN KEY (IdSucursal) REFERENCES sucursal(IdSucursal)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\PI-01\\precios_semana_20200413_mod.csv'
INTO TABLE `precio` 
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\PI-01\\precios_semanas_20200419_20200419_mod_h2.csv'
INTO TABLE `precio` 
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\PI-01\\precios_semanas_20200426_20200426_mod_h1.csv'
INTO TABLE `precio` 
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\PI-01\\precios_semana_20200503_mod.csv'
INTO TABLE `precio` 
FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

set foreign_key_checks = 1

