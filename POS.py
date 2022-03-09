#!/usr/bin/env python
# coding: utf-8

# ### Frequent Itemset mining technique for Basket Analysis in simple Point of Sale dataset
# #### See https://www.edureka.co/blog/apriori-algorithm/
# #### 

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('seaborn-whitegrid')
import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:


file = 'POS_data.csv'
df = pd.read_csv(file, header=0)
df


# In[21]:


df.columns


# In[14]:


df['Date'].min()


# In[15]:


df['Date'].max()


# In[18]:


# df['month_year'] = df['Date'].apply(lambda x: x.strftime('%Y-%m'))


# In[22]:


df_trend = df.groupby("Date").sum()['Transaction'].reset_index()


# In[23]:


plt.plot(df_trend["Date"], df_trend["Transaction"])


# In[27]:


df1 = df.groupby('Item', as_index=True).agg({'Item': 'count'}).rename(columns={'Item':'Total'}).reset_index()
#‘flatten’ the indexes after the operation


# In[32]:


df1


# In[3]:


# We create a new column time_stamp and two dataframes (one per year)
df['Time_stamp'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

df_2016 = df[df['Time_stamp'].dt.year == 2016]
df_2017 = df[df['Time_stamp'].dt.year == 2017]


# In[4]:


df.head(10)


# In[5]:


num_products = df.Item.nunique()
print('There are', num_products, 'unique products')


# In[6]:


products = df.Item.unique()
products


# In[7]:


# Select 10 Top Sales and Analyze its patterns
df1 = df.groupby('Item', as_index=True).agg({'Item': 'count'})                 .rename(columns={'Item':'Total'})                              .reset_index()
df1 = df1.sort_values(by=['Total'], ascending=False)
plt.figure(figsize=(20,8))
df2 = df1.head(10)

sns.set_context("notebook", rc={"font.size":20,"axes.titlesize":20,"axes.labelsize":20})
sns.barplot(x='Item', y='Total', data=df2).set_title("10 bestseller products", size=20)

plt.show()


# In[222]:


df


# In[ ]:





# In[11]:


# Analyze shop hours Sales

times = df['Time_stamp']
times = pd.DatetimeIndex(df['Time_stamp'])
grouped = df.groupby([times.hour]).agg({'Item':'count'})                                    .rename(columns={'Item':'Total', 'Time_stamp': 'Hour'})                     .reset_index()
grouped = grouped.rename(columns={'Time_stamp': 'Hours'})  
plt.figure(figsize=(20,8))
sns.lineplot(x='Hours', y='Total', data=grouped).set_title("Items sold per hour", size=20)

plt.show()


# In[12]:


# Seasonality
# Creating season and month columns
# month 
from datetime import datetime
import datetime as dt
import matplotlib.dates as mdates

a = datetime.strptime(("2016-10-30 09:58:11"), '%Y-%m-%d %H:%M:%S')

df['Month_dt'] = df['Time_stamp'].dt.month

grouped_m = df.groupby([times.month]).agg({'Item':'count'})                                 .rename(columns={'Item':'Total', 'Time_stamp': 'Month'})                     .reset_index()
grouped_m = grouped_m.rename(columns={'Time_stamp': 'Month'}) 
grouped_m['Month_dt'] = pd.to_datetime(grouped_m['Month'], format='%m')
#df['Season']

fig = plt.figure(figsize=(20,8))
ax = fig.add_subplot(111)

monthFmt = dates.DateFormatter('%B')
ax.xaxis.set_major_formatter(monthFmt)
ax.set_xlim([dt.date(1900, 1, 1), dt.date(1900, 12, 1)])
sns.lineplot(x='Month_dt', y='Total', data=grouped_m).set_title("Items sold per Month", size=20)


plt.show()


# In[231]:


df.Time_stamp


# In[226]:


# Another plot example by months
from matplotlib.dates import MonthLocator, DateFormatter

grouped_m['Month'] = pd.to_datetime(grouped_m['Month'], format='%m')

fig = plt.figure(figsize=[20, 8])
ax = fig.add_subplot(111)
plt.plot(grouped_m.Month, grouped_m.Total)
plt.xticks(rotation='vertical')
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(DateFormatter('%b'))


# In[227]:


# Create table for frequency analysis
df.columns


# In[228]:


df_1 =  df.groupby(['Date','Time','Transaction']).agg(lambda m: list(m)).reset_index()
df_1


# In[229]:


# we show two methods to extend the lists to columns
# This is method 1 - uses pd.Series
Items_expanded_v1 = df1["Item"].apply(pd.Series)
Items_expanded_v1


# In[230]:


# This is method 2 list to columns
Items_expanded_v2 = pd.DataFrame(r.Item.values.tolist()).add_prefix('item_')
Items_expanded_v2


# In[ ]:




