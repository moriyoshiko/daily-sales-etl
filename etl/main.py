import argparse
from datetime import datetime
from etl.sql import run_range
from etl.logger import setup_logger
import uuid


def parse_date(s: str):
    return datetime.strptime(s, "%Y-%m-%d").date()


def main():
    job_id = str(uuid.uuid4())
    logger = setup_logger(job_id)

    logger.info("ETL job started")

    parser = argparse.ArgumentParser(description="Daily Sales ETL")
    parser.add_argument("--date")
    parser.add_argument("--start-date")
    parser.add_argument("--end-date")
    args = parser.parse_args()

    if args.date:
        d = parse_date(args.date)
        run_range(d, d, logger)
    elif args.start_date and args.end_date:
        run_range(
            parse_date(args.start_date),
            parse_date(args.end_date),
            logger
        )
    else:
        raise ValueError("date指定が不正")

    logger.info("ETL job finished")


if __name__ == "__main__":
    main()