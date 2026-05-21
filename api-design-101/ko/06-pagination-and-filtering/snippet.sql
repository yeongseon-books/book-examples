SELECT * FROM orders
WHERE status = 'paid'
ORDER BY created_at DESC
LIMIT 20 OFFSET 40;
