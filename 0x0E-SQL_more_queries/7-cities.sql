-- Script that creates a database 'hbtn_0d_usa' and a table 'cities' on a MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT AUTO_INCREMENT PRIMARY KEY UNIQUE NOT NULL,
	state_id INT FOREIGN KEY NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
