import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/project.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Stratscciatella")

# Mapping log levels > no need to use if-else statements
log_methods = {
    "debug": logger.debug,
    "info": logger.info,
    "warning": logger.warning,
    "error": logger.error,
}

def log(level: str, message: str):
    """Log a message with the specified level using a mapping dictionary.

    Args:
        level (str): The log level ("debug", "info", "warning", "error").
        message (str): The message to log.
    """
    log_method = log_methods.get(level.lower(), logger.info)
    log_method(message)
