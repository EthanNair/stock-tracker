# main.py

import yfinance as yf
import matplotlib.pyplot as plt
from strategies import simple_moving_average_strategy, momentum_strategy
from name_to_ticker import get_ticker

# -------- Step 1: Get stock data --------
stockName = "tesla"
ticker = get_ticker(stockName)
data = yf.download(ticker, start="2025-01-01", end="2026-03-24")
print(f"Downloading data for {ticker} ({stockName})")

# -------- Step 2: Run both strategies --------
df_sma = simple_moving_average_strategy(data)
df_momentum = momentum_strategy(data)

# -------- Step 3: Function to calculate portfolio --------
def calculate_portfolio(df, initial_cash=10000):
    cash = initial_cash
    shares = 0
    portfolio_values = []

    # Fill NaNs in 'Position' to avoid errors
    df['Position'] = df['Position'].fillna(0)

    for i in range(len(df)):
        pos = float(df['Position'].iloc[i])
        price = df['Close'].iloc[i]

        if pos == 1:  # Buy
            shares = cash // price
            cash -= shares * price
        elif pos == -1:  # Sell
            cash += shares * price
            shares = 0

        portfolio_values.append(cash + shares * price)

    df['Portfolio'] = portfolio_values
    return df

# Apply portfolio calculation
df_sma = calculate_portfolio(df_sma)
df_momentum = calculate_portfolio(df_momentum)

# -------- Step 4: Plot signals for SMA strategy --------
plt.figure(figsize=(14,7))
plt.plot(df_sma['Close'], label='Close Price', color='blue')
plt.plot(df_sma['SMA_short'], label='Short SMA', color='green')
plt.plot(df_sma['SMA_long'], label='Long SMA', color='red')

# Buy/Sell markers
plt.plot(df_sma[df_sma['Position'] == 1].index, 
         df_sma['Close'][df_sma['Position'] == 1],
         '^', markersize=10, color='g', label='Buy')
plt.plot(df_sma[df_sma['Position'] == -1].index,
         df_sma['Close'][df_sma['Position'] == -1],
         'v', markersize=10, color='r', label='Sell')

plt.title(f'{ticker} SMA Trading Signals')
plt.legend()
plt.show()

# -------- Step 5: Plot portfolio comparison --------
plt.figure(figsize=(14,7))
plt.plot(df_sma['Portfolio'], label='SMA Portfolio', color='purple')
plt.plot(df_momentum['Portfolio'], label='Momentum Portfolio', color='orange')
plt.title(f'{ticker} Portfolio Comparison')
plt.legend()
plt.show()

# -------- Step 6: Print final portfolio values --------
print(f"SMA final portfolio: ${df_sma['Portfolio'].iloc[-1]:.2f}")
print(f"Momentum final portfolio: ${df_momentum['Portfolio'].iloc[-1]:.2f}")