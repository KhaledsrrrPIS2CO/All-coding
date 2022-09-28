import pandas as pd

aapl_price_surl= 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'

def test_run():
    #Function called by Test Run
    df = pd.read_html("data/AAPL.csv")
    df[10:21]


if __name__ == "__main__":
    test_run()


"""
import pandas as pd
import yfinance as yf

aapl_url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'


def get_max_close(symbol):
    #retrun the max value for stock close by indicating the toicker
    df = pd.read_csv("data{}.csv".format(symbol)) # read in data
    return df['Close'].max() #compute the paramet of close  and return max function

def test_run():
    #function called byy test_run it loops over AAAPL & IBM and it will priunyt max value of both stocks   
    for symbol in ['AAPL', "IBM"]:
        print("Max close:")
        print(symbol, "/see", get_max_close,)
        
if __name__ == "__main__":
    test_run()

"""

