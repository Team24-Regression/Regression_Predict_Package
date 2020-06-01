#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
# 
import numpy as np 

# data processing
import pandas as pd 

# data visualization
import seaborn as sns
import matplotlib.pyplot as plt
color = sns.color_palette()
from plotnine import *

get_ipython().run_line_magic('matplotlib', 'inline')
import datetime


# In[25]:


Train_df = pd.read_csv(r"C:\Users\27833\Downloads\Train (1).csv")


# In[26]:


Train_df.columns = [col.replace(" ","_") for col in Train_df.columns]


# In[27]:


Train_df.head()


# In[28]:


Train_df.columns


# In[29]:


def alter_time(Train_df):
    time_matrix = ['Placement_-_Time', 'Confirmation_-_Time', 'Arrival_at_Destination_-_Time', 'Arrival_at_Pickup_-_Time', 'Pickup_-_Time']
    for i in time_matrix:
        Train_df[i] = pd.to_datetime(Train_df[i]).dt.strftime('%H:%M:%S')
        Train_df[i] = pd.to_timedelta(Train_df[i])
        Train_df[i] = Train_df[i].dt.total_seconds()
    return Train_df


# In[30]:


Train_df = alter_time(Train_df)


# In[9]:


Train_df['Placement_-_Time'].dtype


# In[31]:


Train_df = Train_df.drop(['Placement_-_Day_of_Month', 'Placement_-_Weekday_(Mo_=_1)', 'Confirmation_-_Day_of_Month', 'Confirmation_-_Weekday_(Mo_=_1)'
       ], axis=1)


# In[32]:


Train_df = Train_df.drop(['Pickup_-_Day_of_Month', 'Pickup_-_Day_of_Month', 'Pickup_-_Weekday_(Mo_=_1)'], axis = 1)


# Dropping Non Numeric Data In Order To Scale

# In[33]:


Train_df = Train_df.drop(['Order_No', 'User_Id', 'Vehicle_Type'], axis = 1)


# In[34]:


Train_df = Train_df.drop(['Personal_or_Business'], axis = 1)


# In[35]:


Train_df = Train_df.drop(['Rider_Id'], axis = 1)


# In[36]:


Train_df.head(10)


# In[38]:


seconds_in_day = 24*60*60

Train_df['sin_time'] = np.sin(2*np.pi*Train_df['Placement_-_Time']/seconds_in_day)
Train_df['cos_time'] = np.cos(2*np.pi*Train_df['Placement_-_Time']/seconds_in_day)

#df.drop('seconds', axis=1, inplace=True)

Train_df.head()


# In[39]:


Train_df.plot.scatter('sin_time','cos_time').set_aspect('equal')


# In[ ]:





# In[40]:


#split X and Y variable:
X = Train_df.drop('Time_from_Pickup_to_Arrival', axis=1)
y = Train_df['Time_from_Pickup_to_Arrival']


# In[41]:


from sklearn.preprocessing import StandardScaler


# In[42]:


scaler = StandardScaler()


# In[43]:


X_scaled = scaler.fit_transform(X)


# In[44]:


X_standardise = pd.DataFrame(X_scaled,columns=X.columns)
X_standardise.head()


# In[21]:


plt.figure(figsize=(6,6))
plt.scatter(range(X_standardise.shape[0]), np.sort(Train_df.Time_from_Pickup_to_Arrival.values), color = 'brown')
plt.xlabel('X - Variables', fontsize=12)
plt.ylabel('Pickup to Arrival Time', fontsize=12)
plt.show()


# In[45]:


seconds_in_day = 24*60*60

Train_df['Place_sin_time'] = np.sin(2*np.pi*Train_df['Placement_-_Time']/seconds_in_day)
Train_df['Placec_cos_time'] = np.cos(2*np.pi*Train_df['Placement_-_Time']/seconds_in_day)

#df.drop('seconds', axis=1, inplace=True)

Train_df.head()


# In[46]:


Train_df.plot.scatter('sin_time','cos_time', color = 'magenta').set_aspect('equal')


# In[ ]:


def alter_time(Train_df):
    time_matrix = ['Placement_-_Time', 'Confirmation_-_Time', 'Arrival_at_Destination_-_Time', 'Arrival_at_Pickup_-_Time', 'Pickup_-_Time']
    for i in time_matrix:
        Train_df[i] = pd.to_datetime(Train_df[i]).dt.strftime('%H:%M:%S')
        Train_df[i] = pd.to_timedelta(Train_df[i])
        Train_df[i] = Train_df[i].dt.total_seconds()
    return Train_df


# In[48]:


def sincos_time(Train_df):
    seconds_in_day = 24*60*60    
    time_matrix = ['Placement_-_Time', 'Confirmation_-_Time', 'Arrival_at_Destination_-_Time', 'Arrival_at_Pickup_-_Time', 'Pickup_-_Time']
    for i in time_matrix:
        Train_df[str(i)+'_sin_time'] = np.sin(2*np.pi*Train_df['Placement_-_Time']/seconds_in_day)
        Train_df[str(i)+'_cos_time'] = np.cos(2*np.pi*Train_df['Placement_-_Time']/seconds_in_day)
    return Train_df


# In[ ]:




