#!/usr/bin/env python
# coding: utf-8

# In[43]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
import os


# In[52]:


df = pd.read_excel("./파이널프로젝트_RAW_210329_210926.xlsx")


# In[47]:


df.info()


# In[53]:


df['course_id'].replace('', np.nan, inplace=True)
df['coupon_title'].fillna('사용안함', inplace=True)
df['coupon_discount_amount'].fillna(0.0,inplace=True)
df['sale_price'].replace('', np.nan, inplace=True)
del df['tax_free_amount']
df['pg'].fillna('ETC', inplace=True)
df['subcategory_title'].fillna('해당없음', inplace=True)

df.drop(index=47361, axis=0, inplace=True)
df.dropna(subset=['course_id'], inplace=True)
df.dropna(subset=['sale_price'],inplace=True)

