# stock-tracker
A Python stock analysis tool that simulates and compares SMA and momentum trading strategies with real market data.

Stock Strategy Simulator
A Python tool that fetches real stock market data and backtests two classic trading strategies — Simple Moving Average (SMA) crossover and Momentum — with visual buy/sell signals and simulated portfolio performance comparison.

Features

Fetches real-time historical stock data via Yahoo Finance
Supports stocks, indices, and ETFs by name (e.g. "tesla", "nasdaq", "gold")
Implements two trading strategies: SMA Crossover and Momentum
Visualizes buy/sell signals on a price chart
Simulates and compares portfolio growth across both strategies
Configurable initial cash amount (default: $10,000)



Prerequisites

Python 3.8 or higher
pip

Installation

Clone the repository

bash   git clone https://github.com/EthanNair/stock-tracker.git
   cd stock-tracker

Install dependencies

bash   pip install yfinance matplotlib pandas
Running the App
bashpython main.py
To change the stock being analyzed, edit the stockName variable in main.py:
pythonstockName = "tesla"   # Change to any supported name

To add more stock names, simply add an entry to the NAME_TO_TICKER dictionary in name_to_ticker.py.


How It Works
Strategy 1 — SMA Crossover

Calculates a short-term (5-day) and long-term (20-day) moving average
Buy when the short SMA crosses above the long SMA
Sell when the short SMA crosses below the long SMA

Strategy 2 — Momentum

Compares today's price to the price 10 days ago
Buy if today's price is higher (upward momentum)
Sell if today's price is lower (downward momentum)

Portfolio Simulation
Both strategies start with $10,000 in cash and simulate real buy/sell decisions based on signals. The final portfolio value and growth curve are plotted side by side for comparison.

This is a simulation for educational purposes only. It is not financial advice.


📁 Project Structure
stock-tracker/
├── main.py              # Entry point — fetches data, runs strategies, plots results
├── strategies.py        # SMA and Momentum strategy implementations
└── name_to_ticker.py    # Maps human-readable names to stock tickers

🛠️ Built With

Python — core language
yfinance — fetches historical stock data from Yahoo Finance
matplotlib — charting and visualization
pandas — data manipulation


License
This project is licensed under the MIT License. See the LICENSE file for details.

Disclaimer
This project is for educational and portfolio purposes only. Nothing in this repository constitutes financial advice. Always do your own research before making investment decisions.
