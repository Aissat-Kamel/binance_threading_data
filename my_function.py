import binance.client
from binance.client import Client
import datetime as dt
import pandas as pd


client = Client(api_key = "", api_secret = "")



def get_asset_data(assets, interval, depth):
	columns = ['Date','Open','High','Low','Close' ,'Volume','IGNORE','Quote_Volume','Trades_Count','BUY_VOL','BUY_VOL_VAL','x']
	for asset in assets:
			klines = client.get_historical_klines(asset, interval, depth)
			df = pd.DataFrame(klines)
			if not df.empty:
				df.columns = columns
				df['Date'] =  pd.to_datetime(df['Date'],unit='ms')
				print(asset," \n", df)
			else:
				print(None)
