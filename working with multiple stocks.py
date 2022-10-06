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
    #df1 = df1.join(dfSPY)

    #print("this is SPYYY",df1)



if __name__ == "__main__":
    test_run( )

