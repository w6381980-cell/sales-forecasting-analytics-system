CREATE DATABASE RetailDB;

USE RetailDB;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50),
    segment VARCHAR(50)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    cost_price INT,
    selling_price INT
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_date DATE,
    selling_price INT
);

SELECT SUM(quantity * selling_price) AS total_revenue
FROM orders;


SELECT COUNT(order_id) AS total_orders
FROM orders;

FORMAT(order_date, 'yyyy-MM')


SELECT 
    FORMAT(order_date, 'yyyy-MM') AS month,
    SUM(quantity * selling_price) AS monthly_sales
FROM orders
GROUP BY FORMAT(order_date, 'yyyy-MM')
ORDER BY month;


SELECT 
    c.city,
    SUM(o.quantity * o.selling_price) AS total_sales
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.city
ORDER BY total_sales DESC;


SELECT TOP 10
    p.product_name,
    SUM(o.quantity) AS total_sold
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;

SELECT TOP 5
    c.customer_name,
    SUM(o.quantity * o.selling_price) AS total_spent
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY total_spent DESC;

SELECT TOP 5
    p.product_name,
    SUM(o.quantity) AS sales
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY sales ASC;