# -*- coding: utf-8 -*-
"""
Created on Mon May 24 22:48:34 2021

@author: jesus
"""

#%% Imports
from datetime import datetime

#%% Sample Times
timestring1 = '16/12/2006 17:24:00'
timestring2 = '16/12/2006 17:25:00'

#%%
dt_format = '%d/%m/%Y %H:%M:%S'
time1 = datetime.strptime(timestring1, dt_format)
time2 = datetime.strptime(timestring2, dt_format)

print((time2 - time1).total_seconds()/60.0)
print(datetime(time1.year, 1, 1))

#%%
def time_to_ratio(time_stamp):
    time = datetime.strptime(time_stamp, '%d/%m/%Y %H:%M:%S')
    start = datetime(year=time.year, month=1, day=1)
    end = datetime(year=time.year+1, month=1, day=1)
    return (time - start).total_seconds()/(end - start).total_seconds()

def minutes_from_start(time_stamp, start_stamp):
    time = datetime.strptime(time_stamp, '%d/%m/%Y %H:%M:%S')
    start = datetime.strptime(start_stamp, '%d/%m/%Y %H:%M:%S')
    return (time - start).total_seconds()/60.0

#%%
print(time_to_ratio(timestring1))
print(time_to_ratio(timestring2))
print(time_to_ratio('31/12/2007 23:59:00'))
print(time_to_ratio('01/01/2007 00:00:00'))
print(minutes_from_start(timestring2, timestring1))