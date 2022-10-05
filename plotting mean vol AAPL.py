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