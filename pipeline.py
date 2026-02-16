import os
import yfinance as yf
import pandas as pd
import time

def fetch_stock_data():
    # Top 10 stocks
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'TSLA', 'META', 'BRK-B', 'V', 'UNH']
    intervals = ['1d', '1h', '15m']
    
    # Base directory for output
    base_dir = "stock_data_pipeline"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"Created directory: {base_dir}")
        
    print(f"Starting data fetch for {len(tickers)} tickers: {tickers}")
    
    for ticker in tickers:
        # Create directory for each ticker
        ticker_dir = os.path.join(base_dir, ticker)
        if not os.path.exists(ticker_dir):
            os.makedirs(ticker_dir)
            
        print(f"\nProcessing {ticker}...")
        
        for interval in intervals:
            try:
                print(f"  Fetching {interval} data...")
                
                # Determine period based on interval to maximize data given API limits
                # 1m, 2m, 5m, 15m, 30m, 60m, 90m -> 7 days max for 1m? 
                # 15m -> 60d max usually.
                # 1h -> 730d (2y) max.
                # 1d -> max available.
                period = "max"
                if interval == "1h":
                    period = "2y"
                elif interval == "15m":
                    period = "60d"
                
                # Download data
                # auto_adjust=True fixes OHLC to be actual prices not adjusted, but usually default is False (Adj Close separate)
                # We want standard OHLC.
                df = yf.download(ticker, interval=interval, period=period, progress=False, multi_level_index=False)
                
                if df.empty:
                    print(f"  Warning: No data found for {ticker} {interval}")
                    continue
                
                # Save to CSV
                filename = f"{ticker}_{interval}.csv"
                filepath = os.path.join(ticker_dir, filename)
                
                # Check if DataFrame is valid before saving
                if isinstance(df.columns, pd.MultiIndex):
                    # Flattern connection if needed, but with multi_level_index=False it should be fine.
                    # Verify columns
                    if 'Close' not in df.columns:
                         # Attempt to flatten if it's strangely formatted
                        df.columns = [' '.join(col).strip() for col in df.columns.values]

                df.to_csv(filepath)
                print(f"  Saved {filepath} ({len(df)} rows)")
                
                # Sleep briefly to be nice to API
                time.sleep(0.5)
                
            except Exception as e:
                print(f"  Error fetching {ticker} {interval}: {e}")

    print("\nData fetching complete.")

if __name__ == "__main__":
    fetch_stock_data()
