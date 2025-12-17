import logging
import sys

class LoggingConfig:
    def __init__(self):
        pass

    @staticmethod
    def setup_logging():
        root = logging.getLogger()

        if root.handlers:
            for handler in root.handlers:
                root.removeHandler(handler)

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
            datefmt='%d-%m-%Y %H:%M:%S',
            handlers=[logging.StreamHandler(sys.stdout)]
        )
        logging.info("System Logging Initialized (Forced Reset)")

