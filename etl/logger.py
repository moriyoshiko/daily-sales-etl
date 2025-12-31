import logging
import sys
from datetime import datetime

def setup_logger(job_id: str):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 二重登録防止
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] job_id=%(job_id)s %(message)s"
    )

    # 標準出力
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)

    # ファイル出力
    log_file = f"logs/etl_{datetime.now():%Y%m%d}.log"
    fh = logging.FileHandler(log_file)
    fh.setFormatter(formatter)

    logger.addHandler(sh)
    logger.addHandler(fh)

    # job_id を全ログに埋め込む
    logger = logging.LoggerAdapter(
        logger,
        extra={"job_id": job_id}
    )

    return logger