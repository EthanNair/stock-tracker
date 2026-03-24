# name_to_ticker.py

# Dictionary mapping common names to tickers
NAME_TO_TICKER = {
    # Stocks
    "apple": "AAPL",
    "microsoft": "MSFT",
    "tesla": "TSLA",
    "amazon": "AMZN",
    "google": "GOOGL",
    "meta": "META",
    "facebook": "META",
    "nvidia": "NVDA",
    "netflix": "NFLX",
    "disney": "DIS",
    "jpmorgan": "JPM",

    # Indices
    "nasdaq": "^IXIC",
    "sp500": "^GSPC",
    "s&p 500": "^GSPC",
    "dow jones": "^DJI",
    "russell 2000": "^RUT",

    # ETFs
    "spy": "SPY",
    "qqq": "QQQ",
    "gold": "GLD",
    "oil": "USO"
}

def get_ticker(name: str) -> str:
    """
    Convert a company/index name to a ticker.
    Returns the ticker if found, otherwise raises a KeyError.
    """
    key = name.lower().strip()
    if key in NAME_TO_TICKER:
        return NAME_TO_TICKER[key]
    else:
        raise KeyError(f"Ticker for '{name}' not found. Check spelling or add it to NAME_TO_TICKER.")