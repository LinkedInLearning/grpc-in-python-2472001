import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S',
)

debug = logging.debug
info = logging.info
warning = logging.warning
error = logging.error
critical = logging.critical
exception = logging.exception
