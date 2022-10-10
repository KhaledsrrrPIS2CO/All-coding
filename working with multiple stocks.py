#building dataframe 
# df1, dfSPY
#df= dataframe
#onlt join if dfSPY == df1
#then join AAPl on the df1 the we got from SPY
''' Build a dataframe in pandas'''

from operator import le
from matplotlib import dates
import pandas as pd
def test_run():
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)
    print(dates)
    print(len(dates))
    print(dates[0])

    df = pd.DataFrame(index=dates)
    print("these is it:",df)

    #lets create an empty dataframe
    df1 = pd.DataFrame(index=dates)

    #now we read the CSV file for SPY
    dfSPY = pd.read_csv("data/SPY.csv")
    print("this pure",dfSPY)
    #now we join the 2 dataframe
    df1 = df1.join(dfSPY)

    print("this is SPYYY",df1)



if __name__ == "__main__":
    test_run( )


import csv
import pandas as pd
import matplotlib.pyplot as plt
"""

"""
def get_mean_vol(symbol):
    """retursn the mean vol of a certain stocks, takes volume
    data is stored locallay all coding/data/<>symbol.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol)) #read in data


def plot_stock_price():
    df = pd.read_csv("data/AAPL.csv")
    print (df['Adj Close'])
    df['Adj Close'].plot()
    plt.show() # it must be called to show plots

if __name__ == "__main__":
    plot_stock_price()

#plotting AAPL stock price



def plot_high_price():
    df = pd.read_csv("data/AAPL.csv")
    print (df['High'])
    df['High'].plot()
    plt.show()

if __name__ == "__main__":
    plot_high_price()


def plot_close_n_adjClose():
    df = pd.read_csv("data/AAPL.csv")
    df[['Close', 'Adj Close']].plot()
    plt.show()

if __name__ == "__main__":
        plot_close_n_adjClose()