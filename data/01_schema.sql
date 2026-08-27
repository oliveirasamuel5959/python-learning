-- =====================================================
-- Fashion Retail Sales Database — Schema
-- Synthetic dataset (2023-2024) built to demonstrate SQL CTEs
-- Target: MySQL 8.0+ (needs WITH RECURSIVE support)
-- =====================================================

DROP DATABASE IF EXISTS fashion_sales;

CREATE DATABASE fashion_sales CHARACTER SET utf8mb4;
USE fashion_sales;

-- ---------------------------------------------------
-- Categories: self-referencing tree (Clothing > Women's > Dresses, etc.)
-- This is the table the recursive CTE example walks.
-- ---------------------------------------------------
CREATE TABLE categories (
    category_id     INT PRIMARY KEY AUTO_INCREMENT,
    category_name   VARCHAR(50) NOT NULL,
    parent_id       INT NULL,
    FOREIGN KEY (parent_id) REFERENCES categories(category_id)
);

-- ---------------------------------------------------
-- Customers
-- ---------------------------------------------------
CREATE TABLE customers (
    customer_id         INT PRIMARY KEY AUTO_INCREMENT,
    first_name           VARCHAR(50) NOT NULL,
    last_name            VARCHAR(50) NOT NULL,
    email                VARCHAR(100) NOT NULL UNIQUE,
    city                 VARCHAR(50),
    state                VARCHAR(2),
    country              VARCHAR(50) DEFAULT 'USA',
    signup_date          DATE NOT NULL,
    acquisition_channel  VARCHAR(30)
);

-- ---------------------------------------------------
-- Products
-- ---------------------------------------------------
CREATE TABLE products (
    product_id      INT PRIMARY KEY AUTO_INCREMENT,
    product_name    VARCHAR(100) NOT NULL,
    category_id     INT NOT NULL,
    brand           VARCHAR(50),
    cost            DECIMAL(10,2) NOT NULL,
    price           DECIMAL(10,2) NOT NULL,
    launch_date     DATE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- ---------------------------------------------------
-- Marketing campaigns (linked to orders via discount_code)
-- ---------------------------------------------------
CREATE TABLE marketing_campaigns (
    campaign_id     INT PRIMARY KEY AUTO_INCREMENT,
    campaign_name   VARCHAR(100),
    discount_code   VARCHAR(20) UNIQUE,
    discount_pct    DECIMAL(5,2),
    channel         VARCHAR(30),
    start_date      DATE,
    end_date        DATE
);

-- ---------------------------------------------------
-- Orders
-- ---------------------------------------------------
CREATE TABLE orders (
    order_id        INT PRIMARY KEY AUTO_INCREMENT,
    customer_id     INT NOT NULL,
    order_date      DATE NOT NULL,
    status          VARCHAR(20) NOT NULL,   -- completed | cancelled | returned
    shipping_cost   DECIMAL(6,2) DEFAULT 0,
    discount_code   VARCHAR(20) NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (discount_code) REFERENCES marketing_campaigns(discount_code)
);

-- ---------------------------------------------------
-- Order line items
-- ---------------------------------------------------
CREATE TABLE order_items (
    order_item_id   INT PRIMARY KEY AUTO_INCREMENT,
    order_id        INT NOT NULL,
    product_id      INT NOT NULL,
    quantity        INT NOT NULL,
    unit_price      DECIMAL(10,2) NOT NULL,  -- price actually charged (may differ from catalog price)
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE INDEX idx_orders_date       ON orders(order_date);
CREATE INDEX idx_orders_customer   ON orders(customer_id);
CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_order_items_prod  ON order_items(product_id);
