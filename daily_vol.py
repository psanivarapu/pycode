import pandas as pd
import yfinance as yf  # You may need to install this library: pip install yfinance

def get_stock_data(symbol, start_date, end_date):
    # Download historical stock price data using Yahoo Finance
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

def calculate_daily_returns(stock_data):
    # Calculate daily returns
    stock_data['Daily Returns'] = stock_data['Adj Close'].pct_change()
    return stock_data['Daily Returns']

def calculate_daily_volatility(daily_returns):
    # Calculate daily volatility as the standard deviation of daily returns
    daily_volatility = daily_returns.std()
    return daily_volatility

def calculate_price_range(daily_volatility, ending_price):
    price_range_up = ending_price + (ending_price * daily_volatility)
    price_range_down = ending_price - (ending_price * daily_volatility)
    print(f"The price range is: {price_range_down:.4%} to {price_range_up:.4%}")

if __name__ == "__main__":
    # Input parameters
    stock_symbol = "TATVA.NS"  # Change to the desired stock symbol
    start_date = "2023-01-01"  # Change to the desired start date
    end_date = "2023-12-23"    # Change to the desired end date

    # Get historical stock price data
    stock_data = get_stock_data(stock_symbol, start_date, end_date)
    print(stock_data.head())

    # Calculate daily returns
    daily_returns = calculate_daily_returns(stock_data)
    print(daily_returns.head())

    # Calculate daily volatility
    daily_volatility = calculate_daily_volatility(daily_returns)
    print(f"The daily volatility of {stock_symbol} from {start_date} to {end_date} is: {daily_volatility:.4%}")

    calculate_price_range(daily_volatility, stock_data.loc['end_date', 'Adj Close'])
