import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import os


# 1. DATA DOWNLOAD
stock_name = input("Enter stock name: ")
period = input("Enter period (e.g., '1y', '6mo', '3mo'): ")
try:
    ticker = yf.Ticker(stock_name)
    df = ticker.history(period=period)

    if df.empty:
        print("No data found for the given stock and period.")
        exit()

    close_prices = np.array(df["Close"])
    print("Data loaded - Shape:", close_prices.shape)

except Exception as e:
    print("Error fetching data:", e)
    exit()

# 2. BASIC STATS
print("\n--- Basic Statistics ---")
print(f"Mean Price:   {np.mean(close_prices):.2f}")
print(f"Median Price: {np.median(close_prices):.2f}")
print(f"Std Dev:      {np.std(close_prices):.2f}")
print(f"Max Price:    {np.max(close_prices):.2f}")
print(f"Min Price:    {np.min(close_prices):.2f}")

# 3. HIGHEST / LOWEST DAY
print("\n--- Highest / Lowest Day ---")
print(f"Highest Price Day Index: {np.argmax(close_prices)}")
print(f"Lowest Price Day Index:  {np.argmin(close_prices)}")

# 4. DAILY PRICE CHANGE
daily_change = np.diff(close_prices)
print("\n--- Daily Change ---")
print(f"Max Single Day Gain: {np.max(daily_change):.2f}")
print(f"Max Single Day Loss: {np.min(daily_change):.2f}")

# 5. DAILY RETURNS
daily_returns = np.diff(close_prices) / close_prices[:-1] * 100
print("\n--- Daily Returns ---")
print(f"Avg Daily Return: {np.mean(daily_returns):.4f}%")
print(f"Volatility:       {np.std(daily_returns):.4f}%")

# 6. MOVING AVERAGE
window = 20
weights = np.ones(window) / window
moving_avg = np.convolve(close_prices, weights, mode="valid")

# 7. BUY / SELL SIGNAL
signals = np.where(daily_change > 0, "BUY", "SELL")
buy_count = np.sum(signals == "BUY")
sell_count = np.sum(signals == "SELL")
print("\n--- Signals ---")
print(f"BUY days:  {buy_count}")
print(f"SELL days: {sell_count}")

# 8. NORMALIZATION
normalized = (close_prices - np.min(close_prices)) / (
    np.max(close_prices) - np.min(close_prices))

print("\n--- Normalized Price Range ---")
print(f"Min: {np.min(normalized):.2f}  Max: {np.max(normalized):.2f}")

# 9. PERCENTILE
print("\n--- Percentiles ---")
print(f"25th: {np.percentile(close_prices, 25):.2f}")
print(f"50th: {np.percentile(close_prices, 50):.2f}")
print(f"75th: {np.percentile(close_prices, 75):.2f}")

# 10. GRAPH
plt.figure(figsize=(14, 6))

# Close price
plt.plot(close_prices, label="Close Price", color="blue", linewidth=1)

# Moving average
plt.plot(
    range(window - 1, len(close_prices)),
    moving_avg,
    label="20-Day MA",
    color="orange",
    linewidth=2,
)

plt.title(f"{stock_name} Stock Price Analysis (period: {period})")
plt.xlabel("Days")
plt.ylabel("Price (INR)")
plt.legend()
plt.grid(True)
plt.tight_layout()
os.makedirs("data", exist_ok=True)
plt.savefig("data/stock_chart.png")
plt.show()
print("\nChart saved!")
