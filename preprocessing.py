# -*- coding: utf-8 -*-
"""
Created on Mon May 24 22:23:25 2021

@author: jesus
"""

#%% Imports
from datetime import datetime

#%% Time Functions
def time_to_ratio(time_stamp):
    time = datetime.strptime(time_stamp, '%d/%m/%Y %H:%M:%S')
    start = datetime(year=time.year, month=1, day=1)
    end = datetime(year=time.year+1, month=1, day=1)
    return (time - start).total_seconds()/(end - start).total_seconds()

def minutes_from_start(time_stamp, start_stamp):
    time = datetime.strptime(time_stamp, '%d/%m/%Y %H:%M:%S')
    start = datetime.strptime(start_stamp, '%d/%m/%Y %H:%M:%S')
    return (time - start).total_seconds()/60.0

#%% Read File
with open('household_power_consumption.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
data_raw = [l.split(';') for l in lines][1::]

#%%
time_ratios = [time_to_ratio(f'{t[0]} {t[1]}') for t in data_raw]

