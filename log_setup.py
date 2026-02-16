# log_setup.py
import logging.config
from pathlib import Path

def setup_logging(ini_path: str = "logging.ini") -> None:
    Path("logs").mkdir(exist_ok=True)
    logging.config.fileConfig(ini_path, disable_existing_loggers=False)
