""" Import libraries """
import yfinance as yf # fetch real live data from yahoo
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


# # Download data and make Dataframe
load_data = yf.download('GOOGL', start="2024-01-23", end="2025-01-23")
df = pd.DataFrame(load_data)

# # Data exploratory
print(f"Stock dataset :\n {df.head()}\n")
print(f"Check None/NaN :\n {df.isna().sum()}\n")
# print(df.info())
print(f"Describe stock:\n {df.describe()}")

# # Cleaning Data
# remove ticker
df.columns = df.columns.droplevel(1)

# Reset index
df.reset_index(inplace=True)

# monthly volumes
df['Month'] = df['Date'].dt.to_period("M")

monthly_volume = df.groupby("Month").Volume.sum()
months = [str(m) for m in monthly_volume.index]
volumes = monthly_volume.values


# # Calculating Moving Average
# rolling(window=20) -> slides 20-days of data and calculate mean at each point
# moving average of 20-days
df["MA20"] = df["Close"].rolling(window=20).mean()

# moving average of 50-days
df["MA50"] = df["Close"].rolling(window=50).mean()

# # Calculating Daily return
# How much % the stock gained each day?
# pct_change() -> how much percentage change of previous row
df["Daily Return"] = round(df["Close"].pct_change() * 100, 3)


# # Analyze Data
# Highest price ever
high_max = df.High.max()
print(f"Low Price minimum: {high_max}\n")

# Lowest price ever
low_min = df.Low.min()
print(f"Low Price minimum: {low_min}\n")
# Average closing
avg_closing = df["Close"].mean()
print(f"Average closing Price: {avg_closing}\n")

# Best daily return 
daily_return_max = df["Daily Return"].max()
print(f"Daily return maximum: {daily_return_max}\n")

# worst daily return
daily_return_min = df["Daily Return"].min()
print(f"Daily return minimum: {daily_return_min}\n")

# # Visualization
# # Closing price and moving averages
# Plot line chart (Date + closing price and moving averages)
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# figure size 
plt.tight_layout(pad=8.5)

# separate axes
ax1 = axes[0, 0]
ax2 = axes[0, 1]
ax3 = axes[1, 0]
ax4 = axes[1, 1]


# Line chart (Data + Closing Price and Moving Averages)
# Plot Closing Price
ax1.plot(
    df["Date"], df["Close"], marker='.',
    markersize=2.5, markerfacecolor="white",
    markeredgewidth=2.5, label="Closing Price"
)

# Plot MA20
ax1.plot(
    df["Date"], df["MA20"], marker='.',
    markersize=2.5, markerfacecolor="white",
    markeredgewidth=2.5, label="MA20"
)

# Plot MA50
ax1.plot(
    df["Date"], df["MA50"], marker='.',
    markersize=2.5, markerfacecolor="white", 
    markeredgewidth=2.5, label="MA50"
)

# add style and text
ax1.set_title("Market trends", fontsize=15, fontweight="bold", pad=15)
ax1.set_xlabel("Date", fontsize=12)
ax1.set_ylabel("Prices", fontsize=12)
ax1.grid(axis="y", linestyle="--", alpha=0.12)
ax1.spines[["top", "right"]].set_visible(False)
ax1.tick_params(axis='x', rotation=45)
ax1.legend()


# Volume bar chart
# Bar chart (Date and Volume)
colors = plt.cm.Set2.colors
ax2.bar(months, volumes, color=colors[:len(months)])

# add style and text
ax2.set_title("Monthly Volume of stocks", fontsize=15, fontweight='bold', pad=15)
ax2.set_xlabel("Date", fontsize=12)
ax2.set_ylabel("Monthly Volume", fontsize=12)

ax2.spines[["top", "right"]].set_visible(False)
ax2.yaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, _ : f"{x/1e6:.0f}M")
)
ax2.grid(axis="y", linestyle="--", alpha=0.15)
# date rotation
ax2.tick_params(axis='x', rotation=45)


# Daily return line
# Line chart (Date by return)
ax3.plot(
    df['Date'], df['Daily Return'],
    color='r', marker='.', markersize=4, 
    markeredgewidth=3.5, markerfacecolor='w'
)

# add text
ax3.set_title("Stocks day to day", fontsize=15, fontweight='bold', pad=15)
ax3.set_xlabel("Date", fontsize=12, fontweight='normal')
ax3.set_ylabel("Daily return", fontsize=12, fontweight='normal')
ax3.grid(axis='y', linestyle='--', alpha=0.2)
ax3.spines[["top", "right"]].set_visible(False)
ax3.tick_params(axis='x', rotation=45)


# plot histogram return distribution
ax4.hist(df['Daily Return'], bins=20, color='#82cafc', edgecolor='white')

# add styles and text
ax4.set_title("Daily Return Distribution", fontsize=15, fontweight='bold', pad=15)
ax4.set_xlabel("Return %", fontsize=12)
ax4.set_ylabel("Frequency", fontsize=12)
ax4.spines[['top', 'right']].set_visible(False)

# Save image
FILE_NAME = "stock.png"
plt.savefig(FILE_NAME,  dpi=150, bbox_inches='tight')
print(f"Image save to : {FILE_NAME}")

plt.show()