import pandas as pd


def test_run():
    """Function called by Test Run."""
    dfaapl = pd.read_csv("data/AAPL.csv")
    print (dfaapl [0:5]) # slicing 
    dfTWTR = pd.read_csv("data/TWTR.csv")
    print(dfTWTR [0:5]) # slicing 


if __name__ == "__main__":
    test_run()


