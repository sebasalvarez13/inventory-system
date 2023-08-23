UPDATE products, orders
SET stock = stock + quantity
WHERE products.name = orders.product_name AND products.vendor_id = orders.vendor_id