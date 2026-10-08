CREATE DATABASE company_db;

USE company_db;

CREATE TABLE registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title ENUM('Mr.', 'Mrs.') NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    dob_day INT NOT NULL,
    dob_month INT NOT NULL,
    dob_year INT NOT NULL,
    marital_status ENUM('Married', 'Single') NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    region VARCHAR(50) NOT NULL,
    postal_code VARCHAR(10) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    terms_accepted BOOLEAN NOT NULL
);
