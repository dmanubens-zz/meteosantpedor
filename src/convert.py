#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pandas as pd
from dateutil import rrule
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

#start_date = datetime.strptime('19870901', '%Y%m%d')
start_date = datetime.strptime('19950101', '%Y%m%d')
end_date = datetime.strptime('20151101', '%Y%m%d')
#end_date = datetime.strptime('20161101', '%Y%m%d')
df_from_each_file = []
monthly_mean = []
monthly_max = []
august = []
january = []

for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date):
     filename = os.path.join(os.getcwd(), '../data', dt.strftime('%Y%m') + ".csv")
     df = pd.read_csv(filename, delim_whitespace=True, decimal=',', names=['Data','Temperatura Màx.','Temperatura Mín.','Pressió Màx.','Pressió Mín.','Humitat(%) Màx.','Humitat(%) Mín.','Anemòmetre Dir.','Anemòmetre Km/h.','Pluja l/m2'])
     df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
     df_from_each_file.append(df)
     monthly_mean.append([dt.strftime('%Y%m'), df['Temperatura Màx.'].mean()])
     monthly_max.append([dt.strftime('%Y%m'), df['Temperatura Màx.'].max()])
     if (dt.strftime('%B') == 'August'):
        august.append([dt.strftime('%Y%m'), df['Temperatura Màx.'].max()])
     if (dt.strftime('%B') == 'January'):
        january.append([dt.strftime('%Y%m'), df['Temperatura Màx.'].max()])

df_mma = pd.DataFrame(monthly_mean, columns=['Data', 'Tmax_mean'])
df_max = pd.DataFrame(monthly_max, columns=['Data', 'Tmax_max'])

df_mma['Data'] = pd.to_datetime(df_mma['Data'], format='%Y%m')
#df_mma.set_index('Data', inplace=True)
#df_mma.plot(x='Data', y='Tmax_mean')

df_max['Data'] = pd.to_datetime(df_max['Data'], format='%Y%m')

anual_df_mma = df_mma.groupby(pd.Grouper(key='Data', freq='Y'))
anual_mean = anual_df_mma.mean()
anual_df_max = df_max.groupby(pd.Grouper(key='Data', freq='Y'))
anual_max = anual_df_max.max()

anual_max.plot()
plt.show()

data = pd.concat(df_from_each_file, ignore_index=True)
#data.set_index('Data', inplace=True)
#data.plot(x='Data', y='Temperatura Màx.')
#plt.show()
