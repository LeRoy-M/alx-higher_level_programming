-- Script that creates a database 'hbtn_0d_usa' and a table 'state' on a MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS state(
	id INT UNIQUE,
	name VARCHAR(256) NOT NULL
);
