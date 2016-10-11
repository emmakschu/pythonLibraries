# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import urllib2

intcUrl = "http://chart.finance.yahoo.com/table.csv?s=INTC&a=0&b=1&c=2015&d=9&e=10&f=2016&g=d&ignore=.csv"
amdUrl = "http://chart.finance.yahoo.com/table.csv?s=AMD&a=0&b=1&c=2015&d=9&e=10&f=2016&g=d&ignore=.csv"
ibmUrl = "http://chart.finance.yahoo.com/table.csv?s=IBM&a=0&b=1&c=2015&d=9&e=10&f=2016&g=d&ignore=.csv"

def gather_data(url):
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

intc = gather_data(intcUrl)
intc['Close'].plot(grid=True, title="Intel Corp")
plt.show()

amd = gather_data(amdUrl)
amd['Close'].plot(grid=True, title="AMD")
plt.show()

ibm = gather_data(ibmUrl)
ibm['Close'].plot(grid=True, title="IBM")
plt.show()