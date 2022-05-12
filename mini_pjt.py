#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
import os
import matplotlib.dates as mdates
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_excel("./파이널프로젝트_RAW_210329_210926.xlsx")


# In[5]:


df.info()


# In[6]:


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


# In[7]:


df.head()


# In[8]:


df = df[df['state']=='COMPLETED']


# In[9]:


df = df[(df['type']=='REFUND')|(df['type']=='PAYMENT')]


# In[49]:


df.reset_index(drop=True, inplace=True)
temp = df


# In[50]:


temp = temp[(temp['format']!='B2B') & (temp['format']!='B2B 온라인') & (temp['format']!='B2G')]


# In[51]:


# '데이터사이언스' -> '데이터 사이언스'
temp.loc[temp['category_title']=='데이터사이언스' , 'category_title'] = '데이터 사이언스'


# In[52]:


# 카테고리별로 구매까지 완료된 강의 수
compay = temp[(temp['type']=='PAYMENT')&(temp['state']=='COMPLETED')]


# In[53]:


pg_pay = compay[compay['category_title']=='프로그래밍']

# 구매 완료된 프로그래밍 카테고리 내의 '해당없음' 결측치 처리
pg_pay.loc[pg_pay['course_title'].str.contains('프론트엔드') , 'subcategory_title'] = '프론트엔드 개발'
pg_pay.loc[pg_pay['course_title'].str.contains('게임') , 'subcategory_title'] = '게임'
pg_pay.loc[pg_pay['course_title'].str.contains('코딩') , 'subcategory_title'] = '코딩 입문'
pg_pay.loc[pg_pay['course_title'].str.contains('개발자') , 'subcategory_title'] = '개발자 커리어'
pg_pay.loc[pg_pay['course_title'].str.contains('데이터') , 'subcategory_title'] = '데이터 사이언스'


# In[54]:


plt.figure(figsize=(12,12))
plt.rc("font", family="AppleGothic")

plt.subplot(2,1,1)
p1 = sns.countplot(data=compay,
                y='category_title')
p1.set_title('Category Title')
p1.set_xlabel('')
p1.set_ylabel('')

plt.subplot(2,1,2)
p2=sns.countplot(data=pg_pay,
                y='subcategory_title')
p2.set_title('Subcategory of Programming')
p2.set_xlabel('count')
p2.set_ylabel('')


plt.show()


# In[74]:


# frontend 중에서도 어떤 강의가 많이 구매되었는지 확인
fe = pg_pay[pg_pay['subcategory_title']=='프론트엔드 개발']
fe.reset_index(drop=True)

# frontend 카테고리 컬럼 생성
fe = fe.copy()
fe['frontend_category'] = '프론트엔드 전반'
fe['course_title'].unique()


# In[83]:


# course title에 따른 frontend 카테고리 분류
fe.loc[fe['course_title'].str.contains('React') , 'frontend_category'] = 'React'
fe.loc[fe['course_title'].str.contains('The RED') , 'frontend_category'] = 'The RED'
fe.loc[fe['course_title'].str.contains('js') , 'frontend_category'] = 'JavaScript'
fe.loc[fe['course_title'].str.contains('JavaScript') , 'frontend_category'] = 'JavaScript'
fe.loc[fe['course_title'].str.contains('취업') , 'frontend_category'] = '프론트엔드 취업'
fe.loc[fe['course_title'].str.contains('실무') , 'frontend_category'] = '프론트엔드 실무'
fe.loc[fe['course_title'].str.contains('UI') , 'frontend_category'] = 'UI'


# In[89]:


plt.figure(figsize=(12,8))
plt.rc("font", family="AppleGothic")

p1=fe['frontend_category'].value_counts().plot.pie(explode=[0.05,0.05,0.05,0,0,0,0],autopct='%1.1f%%')
p1.set_title('Front-End')
p1.set_ylabel('')

plt.show()

