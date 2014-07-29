# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 10:28:35 2014

@author: Pranav
"""
#[data[1] for data in msft['trigger'] if data[1] == "True"]
from pandas.io.data import DataReader
import matplotlib.pyplot as plt
import datetime
import macdFun
import pandas as pd
flag = False;
msft = DataReader("ITC.NS", "yahoo", datetime.datetime(2007, 1, 1),
    datetime.datetime(2012,1,1))
msft['30_MA_Open'] = pd.stats.moments.rolling_mean(msft['Close'], 20)
msft['150_MA_Open'] = pd.stats.moments.rolling_mean(msft['Close'], 50)
msft['trigger'] = "NaN"
#msft['trigger'] = pd.stats.moments.rolling_mean(msft['Close'], 150)
msft[20:60]

top = plt.subplot2grid((4,4), (0, 0), rowspan=3, colspan=4)
top.plot(msft.index, msft['Open'], label='Open')
top.plot(msft.index, msft['30_MA_Open'], label='30 Day MA')
top.plot(msft.index, msft['150_MA_Open'], label='150 Day MA')
a = []
count = 0
flag = False #this represents that that 20 day is below 50 day

for index, row in msft.iterrows():
    if count > 51:
        if (float(row['30_MA_Open']) > float(row['150_MA_Open'])) and (not flag):
            print "ok"
            msft['trigger'][count] = row['Open']
            flag = True
        elif (float(row['30_MA_Open']) > float(row['150_MA_Open'])) and (flag):
            flag = False
    count = count +1

# print the triugger dates()
count = 0
for index, row in msft.iterrows():
   if row['trigger']!="NaN":
       print row['trigger']
       count = count + 1 
       #push the details in an array
       a.insert(0,{index})
print str(count)

def print_r(arrayVar):
    for data in arrayVar:
        print data
        
 ##iterate over the value

        
top.plot(msft.index, msft['trigger'], label='triggers')
   
plt.title('ITC')
plt.legend()

bottom = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4)
bottom.bar(msft.index, msft['Volume'])

plt.title('Microsoft Trading Volume')
plt.gcf().set_size_inches(15,8)