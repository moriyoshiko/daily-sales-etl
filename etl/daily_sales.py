from pathlib import Path
import logging
from psycopg2 import DatabaseError

logger = logging.getLogger(__name__)

SQL_FILE = Path(__file__).resolve().parent.parent / "sql" / "daily_sales_etl.sql"

# with conn: 失敗したら自動ROLLBACK
# with cursor: クリーンアップ不要(カーソル自動クローズ)
# %sでバインド(プレースホルダ)： SQLインジェクション防止
# SQL_DELETE+INSERT： 再実行可能
def run_daily_sales(conn, target_date, logger):
    try:
        with conn:  # ← ここが重要
            with conn.cursor() as cur:
                sql = SQL_FILE.read_text()
                cur.execute(sql, {"target_date": target_date})
                # わざとエラーを起こす例①（存在しないテーブル）
                # cur.execute("""
                #     INSERT INTO daily_sales_xxx (sale_date, sales_amount)
                #     VALUES (%s, %s)
                # """, (target_date, 9999))

                # わざとエラーを起こす例②（0で割る）
                # x = 1 / 0

    except DatabaseError as e:
        logger.error(
            "ETL failed for date=%s, error=%s",
            target_date,
            e
        )
        raise