-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS devops_db;

USE devops_db;

-- Create the submissions table
-- Note: SQLAlchemy handles this automatically in main.py, 
-- but this script is useful for manual setup.
CREATE TABLE IF NOT EXISTS submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL
);
