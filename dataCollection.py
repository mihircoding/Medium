import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# List of tickers for S&P 500 (^GSPC) and the Magnificent 7 stocks
tickers = ['^GSPC', 'AAPL', 'AMZN', 'GOOGL', 'MSFT', 'META', 'TSLA', 'NVDA']
data = yf.download(tickers, start='2019-09-01', end='2024-09-01')

# Get Adjusted Close price data
adj_close = data['Adj Close']

# Calculate daily returns
returns = adj_close.pct_change()

# Calculate cumulative returns
cumulative_returns = (1 + returns).cumprod()

# Plot cumulative returns for the S&P 500 and Magnificent 7
plt.figure(figsize=(14, 7))
for ticker in tickers:
    plt.plot(cumulative_returns[ticker], label=ticker)

# Set chart title and labels
plt.title('Cumulative Returns: S&P 500 vs. Magnificent 7 (2019-2024)')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.grid(True)
plt.show()

# Calculate summary statistics 
annual_returns = returns.mean() * 252  # 252 trading days 
annual_volatility = returns.std() * (252 ** 0.5)  # Annualized volatility

# Display summary statistics in a table
summary_stats = pd.DataFrame({
    'Annual Return (%)': annual_returns * 100,
    'Annual Volatility (%)': annual_volatility * 100
})

# Print summary statistics
print("Summary Statistics (Annualized):")
print(summary_stats)

# Calculate drawdowns
rolling_max = adj_close.cummax()
drawdown = (adj_close - rolling_max) / rolling_max

# Calculate max drawdown for each stock
max_drawdown = drawdown.min()

# Add max drawdown to summary statistics
summary_stats['Max Drawdown (%)'] = max_drawdown * 100

# Print summary statistics with max drawdown
print("\nSummary Statistics with Max Drawdown (Annualized):")
print(summary_stats)

# Save the final summary table to CSV for reference
summary_stats.to_csv('summary_stats.csv')
