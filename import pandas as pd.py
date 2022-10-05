import pandas as pd


def test_run():
    """Function called by Test Run."""
    dfaapl = pd.read_csv("data/AAPL.csv")
    print (dfaapl [0:5]) # slicing 
    dfTWTR = pd.read_csv("data/TWTR.csv")
    print(dfTWTR [0:5]) # slicing 


if __name__ == "__main__":
    test_run()


def get_max_close(symbol):
    """gets the mac closing price of a stock and it gets symbol
    Data of the stock is stored locally all coding/data/<symbol>.csv
    """
    df = pd.read_csv("data/AAPL.csv")
    return df['Colse'].max() # compute and returns max 

def test_run():
    """Fun called by test called by testrun"""
    for symbol in ['AAPL', 'TWTR']:
        print("Max close")
        print (symbol,":", get_max_close)

test_run()
    