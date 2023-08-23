CREATE TABLE orders (
	id INT AUTO_INCREMENT,
    product_name VARCHAR(100),
    quantity INT,
    vendor_id INT,
    date DATETIME,
    status VARCHAR(100),
    order_number VARCHAR(100),
    PRIMARY KEY (id),
    FOREIGN KEY (vendor_id) REFERENCES vendors(id),
    UNIQUE (order_number)
    
);
	
SELECT * FROM orders;