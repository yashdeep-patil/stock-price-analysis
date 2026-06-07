# Stock Price Analysis

A simple Python project that downloads stock price data using `yfinance`, analyzes closing prices with NumPy, and generates a stock price chart with a 20-day moving average.

## Features

- Downloads historical stock data
- Calculates basic statistics:
  - Mean price
  - Median price
  - Standard deviation
  - Maximum price
  - Minimum price
- Finds highest and lowest price day index
- Calculates daily price changes
- Calculates daily returns and volatility
- Generates simple BUY/SELL signal counts
- Normalizes price values
- Shows 25th, 50th, and 75th percentiles
- Saves a chart to `data/stock_chart.png`

## Requirements

Install the required Python packages:

```bash
pip install yfinance numpy matplotlib
```

## How To Run

Run the script:

```bash
python analysis.py
```

Then enter:

```text
Enter stock name: RELIANCE.NS
Enter period (e.g., '1y', '6mo', '3mo'): 1y
```

For Indian stocks, use the `.NS` suffix for NSE stocks, for example:

```text
TCS.NS
INFY.NS
RELIANCE.NS
HDFCBANK.NS
```

For US stocks, use symbols like:

```text
AAPL
MSFT
GOOGL
TSLA
```

## Output

The program prints stock statistics in the terminal and saves the chart here:

```text
data/stock_chart.png
```

## Error Handling

The script includes basic error handling for:

- Invalid stock names
- Invalid or unsupported periods
- Empty downloaded data
- Missing `data` folder before saving the chart

## Example Periods

Common period values supported by `yfinance` include:

```text
1mo
3mo
6mo
1y
2y
5y
max
```
