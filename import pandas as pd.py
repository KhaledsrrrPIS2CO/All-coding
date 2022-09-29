import pandas as pd


def test_run():
    """Function called by Test Run."""
    df = pd.read_csv("data/AAPL.csv")
    print (df [10:61]) # slicing 


if __name__ == "__main__":
    test_run()
