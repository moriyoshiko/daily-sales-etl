from pathlib import Path

SQL_FILE = Path(__file__).resolve().parent.parent / "sql" / "daily_sales_etl.sql"

# with conn: 失敗したら自動ROLLBACK
# with cursor: クリーンアップ不要(カーソル自動クローズ)
# %sでバインド(プレースホルダ)： SQLインジェクション防止
# SQL_DELETE+INSERT： 再実行可能
def run_daily_sales(conn, target_date):
    with conn:  # ← ここが重要
        with conn.cursor() as cur:
            sql = SQL_FILE.read_text()
            cur.execute(sql, {"target_date": target_date})