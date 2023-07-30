-- Script that creates a database 'hbtn_0d_usa' and a table 'state' on a MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS state(
	PRIMARY KEY(id),
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL
);
