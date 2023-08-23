CREATE TABLE deliveries(
	id INT AUTO_INCREMENT,
    vendor_id INT,
    date DATETIME,
    employee_id INT,
    order_number VARCHAR(100),
    PRIMARY KEY(id),
    FOREIGN KEY (order_number) REFERENCES orders(order_number)
);

SELECT * FROM deliveries;