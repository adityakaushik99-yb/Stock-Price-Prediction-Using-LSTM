import pandas_datareader.data as pdr 
import fix_yahoo_finance as fix 
fix.pdr_override()

class GetData:
	def __init__(self, ticker, start, end):
		self.ticker = ticker
		self.start = start
		self.end = end

	def get_stock_data(self):
		stock_data = pdr.get_data_yahoo(self.ticker, self.start, self.end)
		stock_data.to_csv("stock_data.csv")

if __name__=="__main__":
	data = GetData("GS","2010-01-01","2019-01-01")
	data.get_stock_data()