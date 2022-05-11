#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
import os


# In[3]:


df = pd.read_excel("./파이널프로젝트_RAW_210329_210926.xlsx")


# In[4]:


df.info()


# In[5]:


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


# In[6]:


df.head()


# In[7]:


df = df[df['state']=='COMPLETED']


# In[9]:


df = df[(df['type']=='REFUND')|(df['type']=='PAYMENT')]


# In[165]:


df.reset_index(drop=True, inplace=True)
temp = df


# In[166]:


temp = temp[(temp['format']!='B2B') & (temp['format']!='B2B 온라인') & (temp['format']!='B2G')]


# In[167]:


pg = temp[(temp['category_title']=='프로그래밍')]


# In[181]:


pg['subcategory_title'].unique()


# In[169]:


pg[pg['subcategory_title']=='해당없음']['course_title'].unique()


# In[194]:


pg[pg['course_title'].str.contains('개발자')]['subcategory_title'].unique()


# In[195]:


pg.loc[pg['course_title'].str.contains('프론트엔드') , 'subcategory_title'] = '프론트엔드 개발'
pg.loc[pg['course_title'].str.contains('게임') , 'subcategory_title'] = '게임'
pg.loc[pg['course_title'].str.contains('코딩') , 'subcategory_title'] = '코딩 입문'
pg.loc[pg['course_title'].str.contains('개발자') , 'subcategory_title'] = '개발자 커리어'


# In[205]:


# 카테고리별로 구매까지 완료된 강의 수 비교
compay = df[(df['type']=='PAYMENT')&(df['state']=='COMPLETED')]

# 데이터사이언스를 데이터 사이언스로 통합
compay.loc[compay['category_title']=='데이터사이언스' , 'category_title'] = '데이터 사이언스'
compay.tail()


# In[201]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[209]:


plt.figure(figsize=(12,8))
plt.rc("font", family="AppleGothic")

p1 = sns.countplot(data=compay,
                y=compay['category_title'])
p1.set_title('Category Title')
p1.set_ylabel('')

plt.show()


# In[208]:


plt.figure(figsize=(12,8))
plt.rc("font", family="AppleGothic")

p1=sns.countplot(data=pg,
                y=pg['subcategory_title'])
p1.set_title('Subcategory of Programming')
p1.set_ylabel('')

plt.show()


# In[ ]:




