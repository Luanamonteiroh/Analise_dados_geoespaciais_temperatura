#!/usr/bin/env python
# coding: utf-8

# # Plotting with Matplotlib

# Importing the pyplot submodule of Matplotlib.

# In[1]:


import matplotlib.pyplot as plt


# In[3]:


import pandas as pd


# In[4]:


df = pd.read_csv('Data/LSTBrazil.csv')


# In[5]:


pwd


# In[8]:


df.head()


# The "values" attribute of a Pandas series returns only the numerical values of the given series, not the index list.

# In[9]:


LST = df['LST'].values
Rainfall = df["Rainfall"].values
Month = df['Month'].values
Year = df['Year'].values


# First Plot

# In[10]:


x = Month
y = LST
plt.plot(x, y)


# Format the plot using pyplot options.

# In[14]:


plt.plot(x, y, 'ro--')
plt.title('Brazil LST in 2020')
plt.xlabel('Month')
plt.ylabel('Land Surface Temperature °C')


# Bar plots in Matplotlib

# In[15]:


plt.bar(x, y)
plt.title('Brazil LST in 2020')
plt.xlabel('Month')
plt.ylabel('Temperature [°F]')


# Saving your plots as image files
