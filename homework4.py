#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:22:35 2024

@author: sebastian
"""

import pandas as pd
import matplotlib.pyplot as plt

#Import data

file = '~/Documents/exercises_python_SoSe24/data/TSLA.csv'

df = pd.read_csv(file, decimal = '.')

#df = df[['Date', 'Close']]
df = df.iloc[:, [0,4]]

df.head(5)

#df['Close'] = pd.to_numeric(df['Close'])
df['Date'] = pd.to_datetime(df['Date'], format = '%Y-%m-%d')

df.dtypes

df_2022 = df[(df['Date']>='2022-01-03') & (df['Date']<'2022-12-30')]
df_2022.shape

y = df_2022['Close']
x = df_2022['Date']

plt.plot(x, y, label = 'Closing Price')
plt.xticks(rotation = 45)
plt.title('Tesla Inc., (TSLA)')
plt.legend()
plt.show()