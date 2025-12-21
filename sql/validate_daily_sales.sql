-- daily_sales と raw_orders の再計算結果を突き合わせる
SELECT
    d.sale_date,
    d.sales_amount AS stored_amount,
    r.recalc_amount
FROM daily_sales d
JOIN (
    SELECT
        date_trunc('day', created_at)::date AS sale_date,
        SUM(amount) AS recalc_amount
    FROM raw_orders
    GROUP BY 1
) r
USING (sale_date)
WHERE d.sales_amount IS DISTINCT FROM r.recalc_amount;