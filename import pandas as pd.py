
"""
import pandas as pd


def test_run():
    #Function called by Test Run
    df = pd.read_csv("data/AAPL.csv")
    print df[10:21]


if __name__ == "__main__":
    test_run()
"""
import pandas as pd

def get_max_close(symbol):
    """retrun the max value for stock close by indicating the toicker"""
    df = pd.read_csv("data{}.csv".format(symbol)) # read in data
    return df['Close'].max() #compute and return max

def text_run():
    """function called byy test_run"""
    for symbol in ['AAPL', "IBM"]:
        print "Max close"
        print symbol, get_max_close
        
