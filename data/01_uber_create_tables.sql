-- ============================================================
-- Uber SQL Interview Practice Database - MySQL
-- File: 01_uber_create_tables.sql
-- ============================================================

DROP DATABASE IF EXISTS uber_sql_practice;
CREATE DATABASE uber_sql_practice
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE uber_sql_practice;

-- Cities / operating markets
CREATE TABLE cities (
    city_id INT PRIMARY KEY AUTO_INCREMENT,
    city_name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    timezone VARCHAR(50) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uk_city_country (city_name, country)
);

-- Riders / customers
CREATE TABLE riders (
    rider_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    city_id INT NOT NULL,
    signup_date DATE NOT NULL,
    rider_status ENUM('active','inactive','suspended') NOT NULL DEFAULT 'active',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES cities(city_id),
    INDEX idx_riders_city (city_id),
    INDEX idx_riders_signup_date (signup_date),
    INDEX idx_riders_status (rider_status)
);

-- Drivers
CREATE TABLE drivers (
    driver_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    city_id INT NOT NULL,
    signup_date DATE NOT NULL,
    driver_status ENUM('active','inactive','suspended') NOT NULL DEFAULT 'active',
    rating DECIMAL(3,2) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES cities(city_id),
    INDEX idx_drivers_city (city_id),
    INDEX idx_drivers_status (driver_status),
    INDEX idx_drivers_rating (rating)
);

-- Driver vehicles
CREATE TABLE vehicles (
    vehicle_id INT PRIMARY KEY AUTO_INCREMENT,
    driver_id INT NOT NULL,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    vehicle_year SMALLINT NOT NULL,
    vehicle_type ENUM('economy','comfort','premium','suv') NOT NULL,
    license_plate VARCHAR(20) NOT NULL UNIQUE,
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id),
    INDEX idx_vehicles_driver (driver_id),
    INDEX idx_vehicles_type (vehicle_type)
);

-- Trips / rides
CREATE TABLE trips (
    trip_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    rider_id INT NOT NULL,
    driver_id INT NULL,
    city_id INT NOT NULL,
    vehicle_id INT NULL,
    requested_at DATETIME NOT NULL,
    accepted_at DATETIME NULL,
    pickup_at DATETIME NULL,
    dropoff_at DATETIME NULL,
    status ENUM('completed','cancelled_by_rider','cancelled_by_driver','no_driver','in_progress') NOT NULL,
    service_type ENUM('UberX','Comfort','Black','UberXL') NOT NULL,
    pickup_zone VARCHAR(100) NOT NULL,
    dropoff_zone VARCHAR(100) NOT NULL,
    distance_km DECIMAL(6,2) NULL,
    duration_minutes INT NULL,
    fare_amount DECIMAL(10,2) NULL,
    surge_multiplier DECIMAL(4,2) NOT NULL DEFAULT 1.00,
    FOREIGN KEY (rider_id) REFERENCES riders(rider_id),
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id),
    FOREIGN KEY (city_id) REFERENCES cities(city_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    INDEX idx_trips_rider (rider_id),
    INDEX idx_trips_driver (driver_id),
    INDEX idx_trips_city (city_id),
    INDEX idx_trips_requested_at (requested_at),
    INDEX idx_trips_status (status),
    INDEX idx_trips_city_date (city_id, requested_at),
    INDEX idx_trips_driver_date (driver_id, requested_at)
);

-- Payments: one payment record per trip in this practice dataset
CREATE TABLE payments (
    payment_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    trip_id BIGINT NOT NULL UNIQUE,
    payment_method ENUM('card','cash','wallet','gift_card') NOT NULL,
    payment_status ENUM('paid','refunded','failed','pending') NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    paid_at DATETIME NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(trip_id),
    INDEX idx_payments_status (payment_status),
    INDEX idx_payments_paid_at (paid_at)
);

-- Rider ratings for completed trips
CREATE TABLE ratings (
    rating_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    trip_id BIGINT NOT NULL UNIQUE,
    rider_id INT NOT NULL,
    driver_id INT NOT NULL,
    rider_rating TINYINT NULL,
    driver_rating TINYINT NULL,
    rider_comment VARCHAR(255) NULL,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(trip_id),
    FOREIGN KEY (rider_id) REFERENCES riders(rider_id),
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id),
    CONSTRAINT chk_rider_rating CHECK (rider_rating IS NULL OR rider_rating BETWEEN 1 AND 5),
    CONSTRAINT chk_driver_rating CHECK (driver_rating IS NULL OR driver_rating BETWEEN 1 AND 5),
    INDEX idx_ratings_rider (rider_id),
    INDEX idx_ratings_driver (driver_id),
    INDEX idx_ratings_created_at (created_at)
);
