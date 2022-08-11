#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:22:16 2022

@author: xuchu
"""

# Imports the pyarrow.parquet routines using "import pyarrow.parquet as pq
# imports any other packages that will need to complete the following steps

import pyarrow.parquet as pq
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Uses the pq.read_table() command to import the file into python, saving the result as an object

YT = pq.read_table('yellow_tripdata_2022-04.parquet')

# Uses the to_pandas() function to convert this object to a pandas DataFrame

YT = YT.to_pandas()

# Look at DataFrame

YT

# DataFrames are constructed of columns called Series. To see columns:

YT.columns

# Looking at dtypes

YT.dtypes

# "Curates" this DataFrame

YT['tpep_pickup_datetime'] = pd.to_datetime(YT['tpep_pickup_datetime'],
                              infer_datetime_format=True)

YT['tpep_dropoff_datetime'] = pd.to_datetime(YT['tpep_dropoff_datetime'],
                              infer_datetime_format=True)

YT['tpep_duration_datetime'] = YT['tpep_dropoff_datetime'] - YT['tpep_pickup_datetime']

YT['pickup'] = YT['tpep_pickup_datetime']

YT['dropoff'] = YT['tpep_dropoff_datetime']

YT['duration'] = YT['tpep_duration_datetime']

YT[['pickup','dropoff','duration']].head()


# look for other problematic values
# Run descriptive statistics on the trip distance, duration, and total_amount

YT.describe()

YT.columns

pd.set_option('display.float_format', lambda x: '%.2f' % x)

YT['duration'].describe()

YT['trip_distance'].describe()

YT['total_amount'].describe()

# saving the means

YT['duration'].mean()

YT['trip_distance'].mean()

YT['total_amount'].mean()

# Using plt.scatter with subplots

figs,subs = plt.subplots(2,sharex=True, sharey=True)
YT1 = YT[YT.passenger_count == 1]
subs[0].scatter(YT1['fare_amount'],YT1['trip_distance'],
            color='red',marker='^',label='1')
YT2 = YT[YT.passenger_count == 2]
subs[1].scatter(YT2['fare_amount'],YT2['trip_distance'],
            color='blue',marker='^',label='2')
plt.ylabel('fare_amount')
plt.xlabel('trip_distance')
plt.axis([-5,300,-1,60])
plt.title('Fare vs Distance by Passenger Count')
plt.figlegend(
    labels=('1 Passenger', '2 Passengers'),
    loc='upper right')
plt.show()

# Rules we agree to
# trip_distance <= 100 (already implemented)
# delete any rows where passengers = 0 
# delete trip distance = 0
# fare amount make greater than zero, lt 1,000
# make "extra" >= 0
