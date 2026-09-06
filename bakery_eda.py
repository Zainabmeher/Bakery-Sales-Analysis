#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
df= pd.read_csv(r"C:\Users\meher\Downloads\bakery_sales1.csv") 
df.tail() 


# In[ ]:


df.shape 


# In[ ]:


df.describe() 


# In[ ]:


df.columns


# In[ ]:


df.info() 


# In[ ]:


df.isnull().sum() 


# In[ ]:


df.drop_duplicates() 
df = df.drop_duplicates() 


# In[ ]:


df.fillna(0) 
df = df.fillna(0) 


# In[ ]:


df.dtypes 


# In[ ]:


df[df.columns[4:]] = df[df.columns[4:]].astype(int) 


# In[ ]:


df.dtypes 


# In[ ]:


EDA 


# In[ ]:


df["Day of Week"].value_counts() 


# In[ ]:


df["Total"].min() 


# In[ ]:


df["Total"].max() 


# In[ ]:


import pandas as pd 
import matplotlib.pyplot as plt 


# In[ ]:


total_sales = df["Total"].sum() 


# In[ ]:


total_sales 


# In[ ]:


avg_order = df["Total"].mean()
max_sale = df["Total"].max()
min_sale = df["Total"].min()
orders = len(df)


# In[ ]:


orders 


# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df["Total"],bins= 20)
plt.title("Distribution of Order Values")
plt.show() 


# In[ ]:


product_sales = df.iloc[:,4:].sum().sort_values(ascending=False)

product_sales.head(10) 


# In[ ]:


product_sales.tail(10) 


# In[ ]:


plt.figure(figsize=(10,6))

sns.barplot(
    x=product_sales.values,
    y=product_sales.index
)

plt.title("Products Sold")
plt.show()


# In[ ]:


day_sales = df.groupby("Day of Week")["Total"].sum()

day_sales 


# In[ ]:


sns.barplot(
    x=day_sales.index,
    y=day_sales.values
)

plt.title("Revenue by Day")
plt.show() 


# In[ ]:


df.groupby("Day of Week")["Total"].mean() 


# In[ ]:


inventory = df.iloc[:,4:].sum().sort_values(ascending=False)

inventory 


# In[ ]:


corr = df.iloc[:,4:].corr() 
corr 


# In[ ]:


plt.figure(figsize=(12,10))

sns.heatmap(
    corr,
    cmap="coolwarm"
)

plt.show() 


# In[ ]:


(product_sales/product_sales.sum())*100 


# In[ ]:


product_sales.head() 


# In[ ]:


product_sales.tail() 


# In[ ]:


corr = df.iloc[:, 4:].corr()

pairs = (
    corr.where(~(corr == 1))
        .stack()
        .reset_index()
)

pairs.columns = ["Product 1", "Product 2", "Correlation"]

pairs = pairs[pairs["Product 1"] < pairs["Product 2"]]

pairs.sort_values("Correlation", ascending=False).head(10) 


# In[ ]:


df["merinque cookies"].sum() 


# In[ ]:


df.to_excel("bakery_clean.xlsx", index=False) 


# In[ ]:


import os
os.listdir() 

