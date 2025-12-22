-- 既存データ削除
TRUNCATE raw_orders;

INSERT INTO raw_orders (
    order_id,
    amount,
    created_at,
    updated_at
)
SELECT
    gs AS order_id,
    (random() * 10000)::int + 100 AS amount,
    date '2025-12-01'
      + (random() * 10)::int * interval '1 day'
      + (random() * 23)::int * interval '1 hour' AS created_at,
    NOW() AS updated_at
FROM generate_series(1, 100) AS gs;

---遅延到着データ（12/1発生 → 12/2登録）
INSERT INTO raw_orders (
     order_id, 
     amount, 
     created_at, 
     updated_at
)
VALUES
(1001, 1000, '2025-12-01 22:00:00', NOW());

---- 修正データ（12/2 金額修正）
UPDATE raw_orders
SET amount = 800, updated_at = NOW()
WHERE order_id = 1001;


