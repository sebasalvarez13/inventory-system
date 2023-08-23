SELECT
    products.name,
    vendors.name
FROM products 
INNER JOIN vendors 
ON products.vendor_id = vendors.id
WHERE products.name = :val1 AND vendor_id = :val2;