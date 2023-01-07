#I might have an edge (as thee course said the a financial background is not nessecary )
#goal is quick hands on from data to maniulation
#CSV files (planin text) to e.g. temreture, pressure, humidity data row head , , , , ,
#Stocks of data thousands of# main  objective is how to read stocks data 
#examples iof fields can be in stokcs CSV number of emplyeeers data/time prrices makrrte cap etc
# pricers ofg stokcs over time
# date open , high, low, close, volume , adj close?
#recent dates to old dates
# HCP.csv from Yahoo
# adjusedt colse for example TSLA, AAPL AMZN colse after split 
# mainly the close and the adjusted close are the same onbly if there is a splity or a reverse split
# pandas is craeted ny AQR hedge fund

import pandas as pd 
def test_run():
    """Fundc called by test RUN"""
    df = pd.read_csv("data/AAPL.csv")
    print df[0:6]
    
if __name__ == "__main__":
    test_run()