import pandas as pd
import matplotlib.pyplot as plt

returns = pd.read_csv("../data/asian_funds_returns.csv", index_col="Date", parse_dates=True)

mean_returns = returns.mean()
std_dev = returns.std()

plt.figure(figsize=(8,6))
plt.scatter(std_dev, mean_returns)

for fund in mean_returns.index:
    plt.text(std_dev[fund], mean_returns[fund], fund)

plt.xlabel("Risk (Standard Deviation)")
plt.ylabel("Mean Return")
plt.title("Risk vs Return Analysis")
plt.show()