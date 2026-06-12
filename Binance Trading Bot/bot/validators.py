from bot.logging_config import setup_logger

logger = setup_logger("validators")

# Valid values allowed
VALID_SYMBOLS = ["BTCUSDT", "ETHUSDT"]
VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol: str) -> str:
    """Check if trading symbol is valid"""
    symbol = symbol.upper()
    if symbol not in VALID_SYMBOLS:
        logger.error(f"Invalid symbol: {symbol}")
        raise ValueError(f"Symbol must be one of {VALID_SYMBOLS}")
    return symbol


def validate_side(side: str) -> str:
    """Check if side is BUY or SELL"""
    side = side.upper()
    if side not in VALID_SIDES:
        logger.error(f"Invalid side: {side}")
        raise ValueError(f"Side must be one of {VALID_SIDES}")
    return side


def validate_order_type(order_type: str) -> str:
    """Check if order type is MARKET or LIMIT"""
    order_type = order_type.upper()
    if order_type not in VALID_ORDER_TYPES:
        logger.error(f"Invalid order type: {order_type}")
        raise ValueError(f"Order type must be one of {VALID_ORDER_TYPES}")
    return order_type


def validate_quantity(quantity: str) -> float:
    """Check if quantity is a valid positive number"""
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError("Quantity must be greater than 0")
        logger.info(f"Valid quantity: {qty}")
        return qty
    except ValueError:
        logger.error(f"Invalid quantity: {quantity}")
        raise ValueError(f"Quantity must be a positive number")


def validate_price(price: str) -> float:
    """Check if price is valid (only for LIMIT orders)"""
    try:
        p = float(price)
        if p <= 0:
            raise ValueError("Price must be greater than 0")
        logger.info(f"Valid price: {p}")
        return p
    except ValueError:
        logger.error(f"Invalid price: {price}")
        raise ValueError(f"Price must be a positive number")