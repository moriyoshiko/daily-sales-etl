from datetime import date, timedelta
from etl.db import get_conn
from etl.daily_sales import run_daily_sales


def run_range(start_date: date, end_date: date, logger):
    conn = get_conn()
    try:
        d = start_date
        while d <= end_date:
            logger.info("Start processing date=%s", d)
            run_daily_sales(conn, d, logger)
            logger.info("Finished processing date=%s", d)
            d += timedelta(days=1)
    except Exception:
        logger.exception("ETL aborted")
        raise
    finally:
        conn.close()