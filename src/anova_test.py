import pandas as pd
from scipy import stats

# Load returns data
returns = pd.read_csv("../data/asian_funds_returns.csv", index_col="Date", parse_dates=True)

# Perform ANOVA
f_stat, p_value = stats.f_oneway(
    returns["Fidelity_Asia"],
    returns["Matthews_Asia"],
    returns["Invesco_Developing"]
)

print("F-Statistic:", f_stat)
print("P-Value:", p_value)

# Interpretation
if p_value < 0.05:
    print("Reject Null Hypothesis: Mean returns are significantly different.")
else:
    print("Fail to Reject Null Hypothesis: No significant difference in mean returns.")