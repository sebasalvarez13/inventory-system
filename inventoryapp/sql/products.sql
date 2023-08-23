/*Query to display product data in Products available page*/
SELECT
    products.name,
    products.price,
    products.stock,
    vendors.name
FROM products 
INNER JOIN vendors 
ON products.vendor_id = vendors.id;