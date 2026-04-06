import pandas as pd

# Load dataset
data = pd.read_csv("../data/asian_funds_5yr.csv", index_col="Date", parse_dates=True)

# Calculate daily returns
returns = data.pct_change()

# Drop first NaN row
returns.dropna(inplace=True)

# Save returns dataset
returns.to_csv("../data/asian_funds_returns.csv")

print(returns.head())
print("\nReturns calculated successfully!")
print("Shape:", returns.shape)