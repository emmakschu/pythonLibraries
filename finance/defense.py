# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import urllib2

def create_url(equity):
    url = "http://chart.finance.yahoo.com/table.csv?s="
    url += equity
    url += "&a=0&b=1&c=2000&d=9&e=10&f=2016&g=d&ignore=.csv"
    return url

def gather_data(equity):
    
    url = create_url(equity)    
    
    response = urllib2.urlopen(url)
    cr = csv.reader(response)
    
    data = []
    
    for row in cr:
        data.append(row)
        
    data = np.array(data)
    
    df = pd.DataFrame(data[1:], columns=data[0])
    
    df = df.convert_objects(convert_numeric=True)
    
    try:
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    except Exception:
        print "Could not convert date to datetime format"
    
    df.sort_values(by='Date')
    df.set_index('Date', inplace=True)
    
    return df

rtn = gather_data("RTN")
rtn['Close'].plot(label="Raytheon")

ba = gather_data("BA")
ba['Close'].plot(label="Boeing")

lmt = gather_data("LMT")
lmt['Close'].plot(label="Lockheed")

gd = gather_data("GD")
gd['Close'].plot(label="Gen Dynamics")

noc = gather_data("NOC")
noc['Close'].plot(label="Northrop Gr")

plt.title("Defense contractors, 1/1/2000 - present")
plt.grid(True)
plt.legend(loc="best")
plt.show()