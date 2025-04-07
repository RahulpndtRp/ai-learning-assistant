# common_sdk/logger.py

import logging
import sys
from typing import Optional


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Return a configured logger.

    Args:
        name: module name (usually __name__ of caller)

    Returns:
        logging.Logger: logger writing to stdout
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    fmt = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))

    if not logger.handlers:
        logger.addHandler(handler)
    logger.propagate = False
    return logger
