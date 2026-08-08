--NOT NULL FIXED FOR null variant,but EXISTS is always better
SELECT c.name FROM customers c
WHERE c.id NOT IN(
    SELECT o.customer_id FROM orders o
)
AND c.id IS NOT NULL;

