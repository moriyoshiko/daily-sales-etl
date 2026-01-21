-- 日次売上ETL
-- :target_date を外部から渡す想定
-- BEGIN;(<-不要：Pythonでトランザクション管理：with conn)

-- ① 既存集計を削除（再実行可能にする）
DELETE FROM daily_sales
-- WHERE sale_date = :target_date;　(oracle形式)
WHERE sale_date = %(target_date)s;

-- ② 再集計して挿入
INSERT INTO daily_sales (
    sale_date,
    sales_amount,
    processed_at
)
SELECT
    date_trunc('day', created_at)::date AS sale_date,
    SUM(COALESCE(amount, 0)) AS sales_amount,
    NOW() AS processed_at
FROM raw_orders
WHERE created_at >= %(target_date)s
  AND created_at <  %(target_date)s + INTERVAL '1 day'
GROUP BY 1;

-- COMMIT;