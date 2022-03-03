import my_function as fn
import boost as bs


tickers = [["ETCUSDT", "ETHUSDT"], ["LTCUSDT", "XRPUSDT"], ["XEMUSDT", "PNTUSDT"]]

bs.boost(fn.get_asset_data, tickers, "4h", "24 hours ago UTC+1")
