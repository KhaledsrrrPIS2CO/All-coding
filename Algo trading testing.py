import numpy as np
import pandas as pd
import requests 
import math
import xlsxwriter

print("!--------!")


#import the list of stocks
#the idea is to create equal weight  

#now save the csv stock list as pandas dataframe 
stcoks = pd.read_csv('sp_500_stocks.csv')


# now aquiring the API
#Authentifcation to pull data from the API 
#Dummy data secrets.py, et ignore the info in secretrs py is not shared 
#Sandbox API  

from secrets import IEX_CLOUD_API_TOKEN

#Now API call, IEX Cloud API has good documentation 
#we need 2 info 
# 1st mkt cap 2nd stock price  
symbol = 'AAPL' 
api_url = "https://cloud.iexapis.com/"