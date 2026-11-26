-- Task: Create database hbtn_0d_2 and user_0d_2 with SELECT privilege

-- Create the database if it does not already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if it does not already exist.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on hbtn_0d_2 to user_0d_2.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
