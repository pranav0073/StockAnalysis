# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 21:30:24 2014

@author: Pranav
"""
import pandas as pd
def macd(dataFrame):
#calculating macd
    dataFrame['30_MA_Open'] = pd.stats.moments.rolling_mean(dataFrame['Close'], 20)
    dataFrame['150_MA_Open'] = pd.stats.moments.rolling_mean(dataFrame['Close'], 50)
    dataFrame['trigger'] = "NaN"
#local variables
    a = [] ##return the result
    count = 0
    flag = False #this represents that 20SMA is below 50 20SMA
    for index, row in dataFrame.iterrows():
        if count > 51:
            if (float(row['30_MA_Open']) > float(row['150_MA_Open'])) and (not flag):
                print "ok" 
                dataFrame['trigger'][count] = row['Open']
                flag = True
            elif (float(row['30_MA_Open']) > float(row['150_MA_Open'])) and (flag):
                flag = False
        count = count + 1
    for index, row in dataFrame.iterrows():
        if row['trigger']!="NaN":
            print row['trigger']
            count = count + 1 
#push the details in an array
            a.insert(0,{index})
            print str(count)
    return a