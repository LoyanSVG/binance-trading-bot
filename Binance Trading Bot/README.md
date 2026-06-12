# Binance Futures Testnet Trading Bot

A Python CLI app to place futures orders on Binance Testnet.
Built for learning purposes — no real money involved.

---

## Setup

1. Clone the repo and go into the folder
2. Install dependencies: 
pip install -r requirements.txt

3. Create a `.env` file and add your testnet API keys:

API_KEY=your_key_here
SECRET_KEY=your_secret_here

Get your keys from: https://testnet.binancefuture.com

---

## How to Run

Market order: python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Limit order: python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 50000

---

## Arguments

| Argument | Required | Example |
|----------|----------|---------|
| --symbol | Yes | BTCUSDT |
| --side | Yes | BUY or SELL |
| --type | Yes | MARKET or LIMIT |
| --quantity | Yes | 0.01 |
| --price | Only for LIMIT | 50000 |

---

## Notes

- Only BTCUSDT and ETHUSDT are supported
- Price is only needed for LIMIT orders
- Logs are saved in the logs/ folder
- Keys are stored in .env and never hardcoded

---

## Project Structure

Binance Trading Bot/
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── logs/
│   └── trading_bot.log
├── cli.py
├── .env
├── requirements.txt
└── README.md
