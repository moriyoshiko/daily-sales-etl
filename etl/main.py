import argparse
from datetime import datetime
from etl.sql import run_range


def parse_date(s: str):
    return datetime.strptime(s, "%Y-%m-%d").date()


def main():
    parser = argparse.ArgumentParser(
        description="Daily Sales ETL"
    )

    parser.add_argument("--date", help="処理対象日 (YYYY-MM-DD)")
    parser.add_argument("--start-date", help="処理開始日 (YYYY-MM-DD)")
    parser.add_argument("--end-date", help="処理終了日 (YYYY-MM-DD)")

    args = parser.parse_args()

    if args.date:
        d = parse_date(args.date)
        run_range(d, d)
    elif args.start_date and args.end_date:
        run_range(parse_date(args.start_date),
                  parse_date(args.end_date))
    else:
        raise ValueError(
            "--date または --start-date と --end-date を指定してください"
        )


if __name__ == "__main__":
    main()