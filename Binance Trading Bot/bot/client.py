from binance.client import Client
from binance.exceptions import BinanceAPIException
from bot.logging_config import setup_logger
from dotenv import load_dotenv
import os

# Load keys from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

logger = setup_logger("client")

class BinanceClient:
    def __init__(self):
        try:
            self.client = Client(
                API_KEY,
                SECRET_KEY,
                testnet=True
            )
            logger.info("Successfully connected to Binance Testnet")

        except BinanceAPIException as e:
            logger.error(f"Failed to connect to Binance: {e}")
            raise

    def get_client(self):
        return self.client

    def get_balance(self):
        try:
            balance = self.client.futures_account_balance()
            logger.info("Fetched account balance successfully")
            return balance

        except BinanceAPIException as e:
            logger.error(f"Error fetching balance: {e}")
            raise