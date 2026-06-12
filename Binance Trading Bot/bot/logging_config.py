import logging
import os

# Create a logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

def setup_logger(name: str) -> logging.Logger:
    """
    Creates a logger that saves to file AND shows in terminal
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Format: time - level - message
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # Save logs to file
    file_handler = logging.FileHandler("logs/trading_bot.log")
    file_handler.setFormatter(formatter)

    # Show logs in terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add both handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger