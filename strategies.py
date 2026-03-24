# strategies.py

def simple_moving_average_strategy(data, short_window=5, long_window=20):
    """
    Buy when short-term moving average crosses above long-term moving average.
    Sell when short-term moving average crosses below long-term moving average.
    """
    df = data.copy()
    
    # Calculate moving averages
    df['SMA_short'] = df['Close'].rolling(window=short_window).mean()
    df['SMA_long'] = df['Close'].rolling(window=long_window).mean()
    
    # Create signals: 1 = buy, 0 = hold/sell
    df['Signal'] = 0
    df.loc[df.index[short_window:], 'Signal'] = (
        df['SMA_short'][short_window:] > df['SMA_long'][short_window:]
    ).astype(int)
    
    # Position: +1 buy, -1 sell
    df['Position'] = df['Signal'].diff()
    
    return df


def momentum_strategy(data, window=10):
    """
    Buy if today's price is higher than the price 'window' days ago.
    Sell if today's price is lower than the price 'window' days ago.
    """
    df = data.copy()
    df['Momentum'] = df['Close'] - df['Close'].shift(window)
    
    # Signal: 1 = buy, 0 = hold/sell
    df['Signal'] = 0
    df.loc[df.index[window:], 'Signal'] = (df['Momentum'][window:] > 0).astype(int)
    
    # Position: +1 buy, -1 sell
    df['Position'] = df['Signal'].diff()
    
    return df