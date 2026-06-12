import argparse
from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logger

logger = setup_logger("cli")


def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    # Define all CLI arguments
    parser.add_argument(
        "--symbol",
        type=str,
        required=True,
        help="Trading symbol e.g. BTCUSDT"
    )
    parser.add_argument(
        "--side",
        type=str,
        required=True,
        help="BUY or SELL"
    )
    parser.add_argument(
        "--type",
        type=str,
        required=True,
        help="MARKET or LIMIT"
    )
    parser.add_argument(
        "--quantity",
        type=str,
        required=True,
        help="Order quantity e.g. 0.01"
    )
    parser.add_argument(
        "--price",
        type=str,
        required=False,
        help="Price for LIMIT orders only"
    )

    # Parse what user typed
    args = parser.parse_args()

    try:
        # Step 1: Validate all inputs
        symbol   = validate_symbol(args.symbol)
        side     = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        # Step 2: Print order request summary
        print("\n" + "="*40)
        print("📋 ORDER REQUEST SUMMARY")
        print("="*40)
        print(f"Symbol     : {symbol}")
        print(f"Side       : {side}")
        print(f"Type       : {order_type}")
        print(f"Quantity   : {quantity}")

        # Step 3: Connect to Binance
        binance = BinanceClient()
        client = binance.get_client()

        # Step 4: Place the order
        order_manager = OrderManager(client)

        if order_type == "MARKET":
            print(f"Price      : MARKET PRICE")
            print("="*40)
            order_manager.place_market_order(symbol, side, quantity)

        elif order_type == "LIMIT":
            # Price is required for LIMIT orders
            if not args.price:
                print("\n❌ Error: --price is required for LIMIT orders")
                logger.error("Price not provided for LIMIT order")
                return

            price = validate_price(args.price)
            print(f"Price      : {price}")
            print("="*40)
            order_manager.place_limit_order(symbol, side, quantity, price)

    except ValueError as e:
        print(f"\n❌ Validation Error: {e}")
        logger.error(f"Validation Error: {e}")

    except Exception as e:
        print(f"\n❌ Something went wrong: {e}")
        logger.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()