-- Task: Create the hbtn_0d_usa database and states table

-- Create the database if it does not already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database.
USE hbtn_0d_usa;

-- Create the states table if it does not already exist.
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
