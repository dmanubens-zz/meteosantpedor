#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from dateutil import rrule
from datetime import datetime, timedelta

start_date = datetime.strptime('19870901', '%Y%m%d')
end_date = datetime.strptime('20161101', '%Y%m%d')
df_from_each_file = []

for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date):
     filename = dt.strftime('%Y%m') + ".csv"
     df = pd.read_csv(filename, delim_whitespace=True, decimal=',', names=['Data','Temperatura Màx.','Temperatura Mín.','Pressió Màx.','Pressió Mín.','Humitat(%) Màx.','Humitat(%) Mín.','Anemòmetre Dir.','Anemòmetre Km/h.','Pluja l/m2'])
     df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
     df_from_each_file.append(df)

data = pd.concat(df_from_each_file, ignore_index=True)
print data
