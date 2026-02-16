# Stock Data Pipeline Walkthrough

I have successfully built and executed the stock data pipeline. The script fetches OHLCV data for 10 major stocks across 3 timeframes (1d, 1h, 15m) and saves them to a structured directory system.

## Changes Implemented

### 1. Python Environment
- Created a virtual environment (`venv`) and installed dependencies: `yfinance`, `pandas`.

### 2. Pipeline Script (`pipeline.py`)
- **Features**:
  - Fetches data for: AAPL, MSFT, GOOGL, AMZN, NVDA, TSLA, META, BRK-B, V, UNH.
  - Intervals: Daily (`1d`), Hourly (`1h`), 15-Minutes (`15m`).
  - **Smart Period Selection**: Automatically selects the maximum available history for each timeframe to avoid API errors (e.g., 60d for 15m).
  - **Error Handling**: Includes `try-except` blocks to manage network issues or empty data returns.
  - **Output**: Saves clean CSV files to `stock_data_pipeline/<TICKER>/<TICKER>_<INTERVAL>.csv`.

## Verification Results

### Execution
Ran the pipeline using the dedicated virtual environment:
```powershell
& "venv\Scripts\python.exe" pipeline.py
```

#### Directory Structure
```text
stock_data_pipeline/
├── AAPL/
│   ├── AAPL_15m.csv
│   ├── AAPL_1d.csv
│   └── AAPL_1h.csv
├── MSFT/
│   ├── ...
└── ... (covering all 10 tickers)
```

#### CSV Content Check (`AAPL_1d.csv`)
The generated CSVs contain the required columns:
- **Date**: Index column
- **Open, High, Low, Close**: Price data
- **Volume**: Trading volume

Sample data (first few rows):
```csv
Date,Close,High,Low,Open,Volume
1980-12-12,0.098...,0.098...,0.098...,0.098...,469033600
...
```

## Next Steps
- To run the pipeline again in the future to get fresh data:
  ```powershell
  & "venv\Scripts\python.exe" pipeline.py
  ```
