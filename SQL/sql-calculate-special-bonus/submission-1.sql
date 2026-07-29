SELECT employee_id,
CASE
  WHEN employee_id % 2 != 0 AND name NOT LIKE 'M%' THEN salary
  --WHEN x THEN y, u can place many conditions here
ELSE 0
END AS bonus --END to finish the CASE-ELSE block
FROM employees
ORDER BY employee_id;