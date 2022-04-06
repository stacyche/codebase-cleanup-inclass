

print("STOCKS REPORT...")
from app.alphavantage_service import fetch_stocks_data
# import os
# from dotenv import load_dotenv
# from pandas import read_csv

# from app.utils import to_usd

# load_dotenv()

# ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"
# url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"

# df = read_csv(url)
# #print(df.columns)
# #breakpoint()

# latest = df.iloc[0]

# print(symbol)
# print(latest["timestamp"])
# print(latest["close"])
# print(to_usd(latest["close"]))
fetch_stocks_data(symbol)