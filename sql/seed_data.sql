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


-- -- 通常データ（2025-12-01）
-- INSERT INTO raw_orders VALUES
-- (1, 1000, '2025-12-01 10:00:00', '2025-12-01 10:00:00'),
-- (2, 2000, '2025-12-01 15:30:00', '2025-12-01 15:30:00');

-- -- 通常データ（2025-12-02）
-- INSERT INTO raw_orders VALUES
-- (3, 1500, '2025-12-02 11:00:00', '2025-12-02 11:00:00');

-- 遅延到着データ（2/1発生 → 2/3登録）
-- INSERT INTO raw_orders VALUES
-- (4, 500, '2025-12-01 22:00:00', '2025-12-03 09:00:00');

-- -- 修正データ（2/2 金額修正）
-- INSERT INTO raw_orders VALUES
-- (5, 3000, '2025-12-02 18:00:00', '2025-12-04 08:00:00');


