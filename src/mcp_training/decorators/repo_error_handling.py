#src/decorators/repo_error_handling.py
import json
import logging
from functools import wraps


logger = logging.getLogger("Repository Error Handling")

def repo_error_handling(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)

        except FileNotFoundError:
            logger.warning(f"[MISSING] {function.__name__}: File/Dir not found. Args: {args}")
            return None

        except json.JSONDecodeError:
            logger.error(f"[CORRUPTION] {function.__name__}: Invalid JSON found. Args: {args}")
            logger.info("Returning empty dict {} to allow system recovery.")
            return {}

        except Exception as e:
            logger.exception(f"Error in {function.__name__}: Unexpected error: {e}")
            raise e

    return wrapper