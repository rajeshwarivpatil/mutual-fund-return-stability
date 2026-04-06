import yfinance as yf
import pandas as pd

tickers = {
    "Fidelity_Asia": "FSEAX",
    "Matthews_Asia": "MPACX",
    "Invesco_Developing": "ODMAX"
}

all_data = pd.DataFrame()

for name, ticker in tickers.items():
    data = yf.download(ticker, period="max", interval="1d")
    all_data[name] = data["Close"]

print("Price Data Shape:", all_data.shape)

all_data.to_csv("../data/asian_funds_5yr.csv", index=True)

print("New dataset saved successfully!")