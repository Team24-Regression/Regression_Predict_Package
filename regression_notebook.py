#!/usr/bin/env python
# coding: utf-8

# # Sendy Logistics Challenge Regression Model¶
# 

#  # Introduction #

# Sendy is a business-to-business platform established in 2014, to enable businesses of all types and sizes to transport goods more efficiently across East Africa.
# 
# This notebook aims to help Sendy predict the estimated time of delivery of orders, from the point of driver pickup to the point of arrival at final destination. This will enhance customer communication and improve the reliability of its service; which will ultimately improve customer experience. In addition, the solution will enable Sendy to realise cost savings, and ultimately reduce the cost of doing business, through improved resource management and planning for order scheduling
# 
# An accurate arrival time prediction will help all businesses to improve their logistics and communicate an accurate time to their customers.
# 
# 

# # Importing the Libraries

# In[4]:


# 
import numpy as np 

# data processing
import pandas as pd 

# data visualization
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib import rc


# # Getting the Data

# In[8]:


Test_df= pd.read_csv("Test.csv")
Train_df= pd.read_csv("Train.csv")
VariableDefinitions_df= pd.read_csv("VariableDefinitions.csv")
SampleSubmission_df= pd.read_csv("SampleSubmission.csv")
Riders_df= pd.read_csv("Riders.csv")


# # Data Exploration/Analysis

# In[9]:


Train_df.info()


# The training-set has 21201 examples and 29 features + the target variable (Time from Pickup to Arrival). 6 of the features are floats, 13 are integers and 10 are objects. Below is the have list of the features with a short description:

# In[17]:


Train_df.describe()


# from the  abobe, it is observable that distance from pickup to drop off location is from 1km to 49km and that on average the Time from Pickup to Arrival is ranging from 1sec 7883 seconds.

# In[10]:


Test_df.info()


# In[11]:


VariableDefinitions_df.info()


# In[12]:


SampleSubmission_df.info()


# In[16]:


Riders_df.info()


# 

# In[ ]:




