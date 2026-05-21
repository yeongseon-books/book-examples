SELECT * FROM orders
WHERE status = 'paid'
  AND (created_at, id) < ('2026-05-01T10:00:00Z', 'ord_abc')
ORDER BY created_at DESC, id DESC
LIMIT 20;
