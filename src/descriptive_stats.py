import pandas as pd
import numpy as np

# Load returns
returns = pd.read_csv("../data/asian_funds_returns.csv", index_col="Date", parse_dates=True)

# Mean
mean_returns = returns.mean()

# Variance
variance = returns.var()

# Standard Deviation
std_dev = returns.std()

# Coefficient of Variation (CV)
cv = std_dev / mean_returns

# Combine all results
stats = pd.DataFrame({
    "Mean Return": mean_returns,
    "Variance": variance,
    "Std Deviation": std_dev,
    "Coefficient of Variation": cv
})

print(stats)