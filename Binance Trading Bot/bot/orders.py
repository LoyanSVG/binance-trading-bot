from binance.exceptions import BinanceAPIException
from bot.logging_config import setup_logger

logger = setup_logger("orders")


class OrderManager:
    """
    Handles placing Market and Limit orders
    on Binance Futures Testnet
    """

    def __init__(self, client):
        """
        Takes the Binance client from client.py
        """
        self.client = client

    def place_market_order(self, symbol: str, side: str, quantity: float):
        """
        Places a MARKET order — executes immediately at current price
        """
        try:
            logger.info(f"Placing MARKET {side} order | Symbol: {symbol} | Qty: {quantity}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            # Print clear output
            self._print_order_summary(order)
            logger.info(f"MARKET order placed successfully | OrderId: {order['orderId']}")
            return order

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            print(f"\n❌ API Error: {e}")
            raise

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            print(f"\n❌ Unexpected Error: {e}")
            raise

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float):
        """
        Places a LIMIT order — executes only at your specified price
        """
        try:
            logger.info(f"Placing LIMIT {side} order | Symbol: {symbol} | Qty: {quantity} | Price: {price}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"  # Good Till Cancelled
            )

            # Print clear output
            self._print_order_summary(order)
            logger.info(f"LIMIT order placed successfully | OrderId: {order['orderId']}")
            return order

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            print(f"\n❌ API Error: {e}")
            raise

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            print(f"\n❌ Unexpected Error: {e}")
            raise

    def _print_order_summary(self, order):
        """
        Prints clean order details after placing
        """
        print("\n" + "="*40)
        print("✅ ORDER PLACED SUCCESSFULLY")
        print("="*40)
        print(f"Order ID     : {order.get('orderId')}")
        print(f"Symbol       : {order.get('symbol')}")
        print(f"Side         : {order.get('side')}")
        print(f"Type         : {order.get('type')}")
        print(f"Quantity     : {order.get('origQty')}")
        print(f"Price        : {order.get('price', 'MARKET')}")
        print(f"Status       : {order.get('status')}")
        print(f"Executed Qty : {order.get('executedQty')}")
        print(f"Avg Price    : {order.get('avgPrice', 'N/A')}")
        print("="*40 + "\n")