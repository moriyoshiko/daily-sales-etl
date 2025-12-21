
-- 生データ（注文）
DROP TABLE IF EXISTS raw_orders;
CREATE TABLE raw_orders (
    order_id    BIGINT PRIMARY KEY,
    amount      NUMERIC(10,2) NOT NULL,
    created_at  TIMESTAMP NOT NULL,
    updated_at  TIMESTAMP NOT NULL
);

-- 日次集計（ETL結果）
DROP TABLE IF EXISTS daily_sales;
CREATE TABLE daily_sales (
    sale_date     DATE PRIMARY KEY,
    sales_amount  NUMERIC(18,2) NOT NULL,
    processed_at  TIMESTAMP NOT NULL
);

-- 実務想定インデックス
CREATE INDEX idx_raw_orders_created_at
    ON raw_orders (created_at);

CREATE INDEX idx_raw_orders_updated_at
    ON raw_orders (updated_at);