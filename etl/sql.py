from datetime import date, timedelta

from etl.db import get_conn
from etl.daily_sales import run_daily_sales


def run_range(start_date: date, end_date: date):
    conn = get_conn()
    try:
        d = start_date
        while d <= end_date:
            run_daily_sales(conn, d)
            print(f"processed: {d}")
            d += timedelta(days=1)
    finally:
        conn.close()