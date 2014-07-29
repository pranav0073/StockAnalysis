# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 10:28:35 2014

@author: Pranav
"""
#[data[1] for data in msft['trigger'] if data[1] == "True"]
from pandas.io.data import DataReader
import matplotlib.pyplot as plt
import datetime
import macdFun as md
import pandas as pd
flag = False;
msft = DataReader("ITC.NS", "yahoo", datetime.datetime(2013, 1, 1),
    datetime.datetime(2014,7,1))
msft['20_MA_Open'] = pd.stats.moments.rolling_mean(msft['Close'], 20)
msft['50_MA_Open'] = pd.stats.moments.rolling_mean(msft['Close'], 50)
msft['trigger'] = "NaN"
#msft['trigger'] = pd.stats.moments.rolling_mean(msft['Close'], 150)
msft[20:60]

top = plt.subplot2grid((4,4), (0, 0), rowspan=3, colspan=4)
top.plot(msft.index, msft['Open'], label='Open')
top.plot(msft.index, msft['20_MA_Open'], label='20 Day MA')
top.plot(msft.index, msft['50_MA_Open'], label='50 Day MA')

a = md.macd(msft)
def print_r(arrayVar):
    for data in arrayVar:
        print data
        
 ##iterate over the value

        
#top.plot(msft.index, msft['trigger'], label='triggers')
   
plt.title('ITC')
plt.legend()

bottom = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4)
bottom.bar(msft.index, msft['Volume'])

plt.title('Microsoft Trading Volume')
plt.gcf().set_size_inches(15,8)