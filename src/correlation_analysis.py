import pandas as pd

returns = pd.read_csv("../data/asian_funds_returns.csv", index_col="Date", parse_dates=True)

correlation_matrix = returns.corr()

print("Correlation Matrix:\n")
print(correlation_matrix)