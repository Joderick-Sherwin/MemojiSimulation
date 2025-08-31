# src/utils/logger.py
import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name="FullBodyWireframe", log_file="logs/app.log", level=logging.INFO):
    """
    Setup a logger for the project.
    Returns a valid logging.Logger instance.
    """
    # Ensure log directory exists
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False  # Avoid duplicate logs

    # Always remove existing handlers to prevent None return
    if logger.hasHandlers():
        logger.handlers.clear()

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch_formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s',
                                     "%Y-%m-%d %H:%M:%S")
    ch.setFormatter(ch_formatter)

    # File handler with rotation
    fh = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
    fh.setLevel(level)
    fh_formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(name)s - %(message)s',
                                     "%Y-%m-%d %H:%M:%S")
    fh.setFormatter(fh_formatter)

    # Add handlers
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
