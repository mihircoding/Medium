# Import required libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# List of tickers for S&P 500 (^GSPC) and the Magnificent 7 stocks
tickers = ['^GSPC', 'AAPL', 'AMZN', 'GOOGL', 'MSFT', 'META', 'TSLA', 'NVDA']

# Dummy summary statistics data
data = {
    'Ticker': ['^GSPC', 'AAPL', 'AMZN', 'GOOGL', 'MSFT', 'META', 'TSLA', 'NVDA'],
    'Annual Return (%)': [11.20, 22.45, 14.67, 18.76, 28.43, 12.65, 36.98, 49.17],
    'Annual Volatility (%)': [14.65, 29.35, 28.12, 24.42, 26.50, 32.12, 61.22, 54.65],
    'Max Drawdown (%)': [-34.87, -38.12, -45.78, -40.22, -33.65, -55.43, -48.93, -51.02]
}

# Create a DataFrame
summary_stats = pd.DataFrame(data)

# Set the position of bars on X axis
x = np.arange(len(summary_stats['Ticker']))

# Set the width of the bars
width = 0.25

# Create a bar chart
fig, ax = plt.subplots(figsize=(12, 6))

# Create bars for each metric
bars1 = ax.bar(x - width, summary_stats['Annual Return (%)'], width, label='Annual Return (%)', color='blue')
bars2 = ax.bar(x, summary_stats['Annual Volatility (%)'], width, label='Annual Volatility (%)', color='orange')
bars3 = ax.bar(x + width, summary_stats['Max Drawdown (%)'], width, label='Max Drawdown (%)', color='red')

# Add labels and title
ax.set_xlabel('Assets')
ax.set_title('Comparison of Annual Return, Volatility, and Max Drawdown')
ax.set_xticks(x)
ax.set_xticklabels(summary_stats['Ticker'])
ax.legend()

# Add gridlines for better readability
ax.yaxis.grid(True)

# Display the plot
plt.tight_layout()
plt.show()
