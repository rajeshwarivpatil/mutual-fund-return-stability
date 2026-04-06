import pandas as pd

returns = pd.read_csv("../data/asian_funds_returns.csv", index_col="Date", parse_dates=True)

cov_matrix = returns.cov()

print("Covariance Matrix:\n")
print(cov_matrix)