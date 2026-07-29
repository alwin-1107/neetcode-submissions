-- Write your query below
-- SELECT 
-- c.name 
-- FROM customers c LEFT JOIN orders o ON
-- c.id = o.customer_id
-- WHERE o.* IS NULL
-- ORDER BY c.id

--Optmized solution without JOIN:

SELECT name FROM customers
WHERE 
id NOT IN (SELECT customer_id FROM orders);
