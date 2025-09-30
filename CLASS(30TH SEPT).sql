INSERT INTO Orders_1NF (order_id, order_date, customer_id, customer_name, customer_city)
VALUES (101, '2025-09-01',1,'Alice','Delhi'),
	    (102, '2025-09-02','Bob','Mumbai');


INSERT INTO OrderItems_1NF VALUES
(101, 1, 1, 'Laptop',    60000, 1),
(101, 2, 3, 'Headphones', 2000, 2);

INSERT INTO OrderItems_1NF VALUES
(102, 1, 2, 'Smartphone', 30000, 1);

#Creating 2NF
CREATE TABLE OrderItems_2NF (
  order_id INT,
  line_no INT,
  product_id INT,
  unit_price_at_sale DECIMAL(10,2),  -- historical price
  quantity INT,
  PRIMARY KEY (order_id, line_no),
  FOREIGN KEY (order_id) REFERENCES Orders_2NF(order_id),
  FOREIGN KEY (product_id) REFERENCES Products_2NF(product_id)
);

-- Seed dimension tables (from what we saw in BadOrders/OrderItems_1NF)

INSERT INTO Customers_2NF VALUES

(1, 'Rahul', 'Mumbai'),

(2, 'Priya', 'Delhi');
 
INSERT INTO Products_2NF VALUES

(1, 'Laptop',     'Electronics', 60000),

(2, 'Smartphone', 'Electronics', 30000),

(3, 'Headphones', 'Accessories',  2000);
 
INSERT INTO Orders_2NF VALUES

(101, '2025-09-01', 1),

(102, '2025-09-02', 2);
 
INSERT INTO OrderItems_2NF VALUES

(101, 1, 1, 60000, 1),

(101, 2, 3,  2000, 2),

(102, 1, 2, 30000, 1);
 
 
 #CREATING BAD ORDER TABLES
 CREATE DATABASE IF NOT EXISTS RetailNF;
USE RetailNF;

CREATE TABLE BadOrders (
	order_id      INT PRIMARY KEY,
    order_date    DATE,
    customer_id   INT,
    customer_name VARCHAR(50),
    customer_city VARCHAR(50),
    -- Repeating groups(comma separated)
    products_ids VARCHAR(200),
    products_name VARCHAR(200),
    unit_prices VARCHAR(200),
    quantities VARCHAR(200),
    order_total DECIMAL(10,2) -- DERIVABLE COLUMN
);