#!/usr/bin/env python
# coding: utf-8

# In[1]:


#                                                 DATA COLLECTION
import pandas as pd
import numpy as np
data=pd.read_csv("Videos/database.csv")
data


# In[2]:


#product without prices
a=data['uuid']
b=data['price_string'].isna()
c=list(zip(a,b))
df = pd.DataFrame(c,columns=['uuid','price_string'])
df


# In[3]:


#product without prices
b=data[data['price_string'].isna()]  
b
df_1=pd.DataFrame(b)
df_1

#count of products without prices  in product_type,Category and level_1

print('product_type',df_1['product_type'].isna().sum())
print('category',df_1['category'].isna().sum())
print('level_1',df_1['level_1'].isna().sum())


# In[4]:


#product with prices
c=data[data['price_string'].notna()]  
c
df_2=pd.DataFrame(b)
df_2

#count of products with prices  in product_type,Category and level_1

print('product_type',df_2['product_type'].notna().sum())
print('category',df_2['category'].notna().sum())
print('level_1',df_2['level_1'].notna().sum())


# In[5]:


#correcting product prices with correct format
data.price_string=data.price_string.str.lstrip('$')
data

data['price_string']='$ ' + data['price_string'].astype(str)
data

#separating price_string into Currency and values columns

data[['currency','values']]=data.price_string.str.split(pat=' ',expand=True)
data


# In[11]:


#creating a new dataframe with category and values
a=data['category']
b=data['values']
list_1=list(zip(a,b))
result=pd.DataFrame(list_1,columns=['category','values'])


#converting values column datatype from object to float
result['values'] = result['values'].astype(float, errors = 'raise')

#printing result of average price for each category of product
graph=result.groupby(['category'])['values'].mean().reset_index()
graph


# In[12]:


#depicting above data
import pandas as pd
from matplotlib import pyplot as plt
#creating dataframe of above data
graph.head()
df = pd.DataFrame(graph)

#assigning values 

cat = df['category'].head(12)
val = df['values'].head(12)

# Figure Size
fig = plt.figure(figsize =(10,7))

# Horizontal Bar Plot
plt.bar(cat[0:12], val[0:12])

plt.xlabel("Categories")
plt.ylabel("mean Prices")
plt.title("list of categories with mean prices")

# Show Plot
plt.show()


# In[ ]:




