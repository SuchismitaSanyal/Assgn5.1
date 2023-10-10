#!/usr/bin/env python
# coding: utf-8

# ### Will a Customer Accept the Coupon?
# 
# **Context**
# 
# Imagine driving through town and a coupon is delivered to your cell phone for a restaraunt near where you are driving. Would you accept that coupon and take a short detour to the restaraunt? Would you accept the coupon but use it on a sunbsequent trip? Would you ignore the coupon entirely? What if the coupon was for a bar instead of a restaraunt? What about a coffee house? Would you accept a bar coupon with a minor passenger in the car? What about if it was just you and your partner in the car? Would weather impact the rate of acceptance? What about the time of day?
# 
# Obviously, proximity to the business is a factor on whether the coupon is delivered to the driver or not, but what are the factors that determine whether a driver accepts the coupon once it is delivered to them? How would you determine whether a driver is likely to accept a coupon?
# 
# **Overview**
# 
# The goal of this project is to use what you know about visualizations and probability distributions to distinguish between customers who accepted a driving coupon versus those that did not.
# 
# **Data**
# 
# This data comes to us from the UCI Machine Learning repository and was collected via a survey on Amazon Mechanical Turk. The survey describes different driving scenarios including the destination, current time, weather, passenger, etc., and then ask the person whether he will accept the coupon if he is the driver. Answers that the user will drive there ‘right away’ or ‘later before the coupon expires’ are labeled as ‘Y = 1’ and answers ‘no, I do not want the coupon’ are labeled as ‘Y = 0’.  There are five different types of coupons -- less expensive restaurants (under \\$20), coffee houses, carry out & take away, bar, and more expensive restaurants (\\$20 - \\$50). 

# **Deliverables**
# 
# Your final product should be a brief report that highlights the differences between customers who did and did not accept the coupons.  To explore the data you will utilize your knowledge of plotting, statistical summaries, and visualization using Python. You will publish your findings in a public facing github repository as your first portfolio piece. 
# 
# 
# 
# 

# ### Data Description
# Keep in mind that these values mentioned below are average values.
# 
# The attributes of this data set include:
# 1. User attributes
#     -  Gender: male, female
#     -  Age: below 21, 21 to 25, 26 to 30, etc.
#     -  Marital Status: single, married partner, unmarried partner, or widowed
#     -  Number of children: 0, 1, or more than 1
#     -  Education: high school, bachelors degree, associates degree, or graduate degree
#     -  Occupation: architecture & engineering, business & financial, etc.
#     -  Annual income: less than \\$12500, \\$12500 - \\$24999, \\$25000 - \\$37499, etc.
#     -  Number of times that he/she goes to a bar: 0, less than 1, 1 to 3, 4 to 8 or greater than 8
#     -  Number of times that he/she buys takeaway food: 0, less than 1, 1 to 3, 4 to 8 or greater
#     than 8
#     -  Number of times that he/she goes to a coffee house: 0, less than 1, 1 to 3, 4 to 8 or
#     greater than 8
#     -  Number of times that he/she eats at a restaurant with average expense less than \\$20 per
#     person: 0, less than 1, 1 to 3, 4 to 8 or greater than 8
#     -  Number of times that he/she goes to a bar: 0, less than 1, 1 to 3, 4 to 8 or greater than 8
#     
# 
# 2. Contextual attributes
#     - Driving destination: home, work, or no urgent destination
#     - Location of user, coupon and destination: we provide a map to show the geographical
#     location of the user, destination, and the venue, and we mark the distance between each
#     two places with time of driving. The user can see whether the venue is in the same
#     direction as the destination.
#     - Weather: sunny, rainy, or snowy
#     - Temperature: 30F, 55F, or 80F
#     - Time: 10AM, 2PM, or 6PM
#     - Passenger: alone, partner, kid(s), or friend(s)
# 
# 
# 3. Coupon attributes
#     - time before it expires: 2 hours or one day

# In[150]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px
import re


# ### Problems
# 
# Use the prompts below to get started with your data analysis.  
# 
# 1. Read in the `coupons.csv` file.
# 
# 
# 

# In[151]:


data = pd.read_csv('D:/Tina/BerkleyML/Module 5/assignment_5_1_starter/data/coupons.csv')


# In[152]:


data.head()


# In[4]:


data.shape


# In[5]:


data[data['car'].notnull()]


# In[6]:


data.info()


# 2. Investigate the dataset for missing or problematic data.

# In[7]:


data.isnull().sum()


# 3. Decide what to do about your missing data -- drop, replace, other...

# In[8]:


data['passanger'] = data['passanger'].apply(lambda x: re.sub(r'\([^)]*\)', '', x))


# In[9]:


data.head()


# In[ ]:





# 4. What proportion of the total observations chose to accept the coupon? 
# 
# 

# In[10]:


#data.query('Y == 1').sum()
Coup_Accept=data['Y'].value_counts(normalize=True)
print(Coup_Accept)


# 5. Use a bar plot to visualize the `coupon` column.

# In[11]:


px.bar(data, x='coupon', color='gender', title='Coupon delivered at your phone')


# 6. Use a histogram to visualize the temperature column.

# In[12]:


px.histogram(data, x='temperature')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# **Investigating the Bar Coupons**
# 
# Now, we will lead you through an exploration of just the bar related coupons.  
# 
# 1. Create a new `DataFrame` that contains just the bar coupons.
# 

# In[54]:


df= data.query('coupon =="Bar"')


# Dataframe df contains the records for Bar coupons.

# In[14]:


df.shape[0]


# In[84]:


df['Bar'].unique()


# There are a total 2017 records for Bar coupons including customers accepted or not accepted the coupon.

# 2. What proportion of bar coupons were accepted?
# 

# In[88]:


barCoupon_AcceptRate =df.query('Y ==1').shape[0]/df.shape[0]
print(round(barCoupon_AcceptRate,2))


# 0.41 is proportion in which the coupons are accepted for Bar.

# 3. Compare the acceptance rate between those who went to a bar 3 or fewer times a month to those who went more.
# 

# In[97]:


df['Bar'].unique()
lessThan3 =['never','less1','1~3']
custVisitlessthan3=df[df["Bar"].isin(lessThan3)].shape[0]
custVisitlessthan3andAccept=df[df["Bar"].isin(lessThan3)].query('Y== 1').shape[0]
print(custVisitlessthan3andAccept)


# In[99]:


custVisitlessthan3_acceptRate=custVisitlessthan3andAccept/custVisitlessthan3
print(round(custVisitlessthan3_acceptRate,2))


# 666 customers went to bar less than 3 or fewer times and accepted the coupon.

# In[18]:


moreThan3=['gt8','4~8']
custVisitmorethan3=df[df["Bar"].isin(moreThan3)].shape[0]
custVisitmorethan3andAccept=df[df["Bar"].isin(moreThan3)].query('Y==1').shape[0]
print(custVisitmorethan3andAccept)


# In[107]:


custVisitBarmorethan3_acceptRate=custVisitmorethan3andAccept/custVisitmorethan3
print(round(custVisitBarmorethan3_acceptRate,2))


# Although the number of customers who accepted the Bar coupon is more for those who went to a bar 3 or fewer times a month, the acceptance rate for the customers who visit Bar more than 3 times is better. 

# 4. Compare the acceptance rate between drivers who go to a bar more than once a month and are over the age of 25 to the all others.  Is there a difference?
# 

# In[20]:


list_values=['never','less1','21','below21']


# In[21]:


df_moreThan1visit_agemorethan25= df[~df[['Bar','age']].isin(list_values).any(axis=1)]


# In[22]:


df_moreThan1visit_agemorethan25.shape[0]


# In[117]:


df_moreThan1visit_agemorethan25.query('Y==1').shape[0]


# In[118]:


custMoreThan1visit_agemorethan25_acceptRate=df_moreThan1visit_agemorethan25.query('Y==1').shape[0]/df_moreThan1visit_agemorethan25.shape[0]


# In[119]:


print(round(custMoreThan1visit_agemorethan25_acceptRate,2))


# 5. Use the same process to compare the acceptance rate between drivers who go to bars more than once a month and had passengers that were not a kid and had occupations other than farming, fishing, or forestry. 
# 

# In[24]:


list_values_3=['never','less1','Kid','Farming Fishing & Forestry']


# In[25]:


df_visitMoreThan1NotKidExpFarmFishFor=df[~df[['Bar','age','occupation']].isin(list_values_3).any(axis=1)]


# In[26]:


df_visitMoreThan1NotKidExpFarmFishFor.shape[0]


# In[31]:


df_visitMoreThan1NotKidExpFarmFishFor.query('Y==1').shape[0]


# In[32]:


visitMoreThan1NotKidExpFarmFishFor_AccepRate =(df_visitMoreThan1NotKidExpFarmFishFor.query('Y==1').shape[0])/(df_visitMoreThan1NotKidExpFarmFishFor.shape[0])


# In[126]:


print(round(visitMoreThan1NotKidExpFarmFishFor_AccepRate,2))


# 6. Compare the acceptance rates between those drivers who:
# 
# - go to bars more than once a month, had passengers that were not a kid, and were not widowed *OR*
# - go to bars more than once a month and are under the age of 30 *OR*
# - go to cheap restaurants more than 4 times a month and income is less than 50K. 
# 
# 

# In[73]:


list_values_4=['never','less1','Kid','Widowed']
list_values_5=['1~3', 'gt8', '4~8','21','26','below21']


# In[74]:


df_visitMoreThan1NotKidWidow=df[~df[['Bar','passanger','maritalStatus']].isin(list_values_4).any(axis=1)]


# In[75]:


df_visitMoreThan1NotKidWidow.shape[0]


# In[77]:


df_visitMoreThan1NotKidWidow.query('Y==1').shape[0]


# In[78]:


visitMoreThan1NotKidWidow_AccetRate=(df_visitMoreThan1NotKidWidow.query('Y==1').shape[0])/(df_visitMoreThan1NotKidWidow.shape[0])


# Acceptance rate for go to bars more than once a month, had passengers that were not a kid, and were not widowed is:

# In[130]:


print(round(visitMoreThan1NotKidWidow_AccetRate,2))


# In[81]:


df_visitMoreThan1lessThan30=df[df[['Bar','age']].isin(list_values_5).any(axis=1)]


# In[134]:


visitMoreThan1lessThan30_AcceptRate = (df_visitMoreThan1lessThan30.query('Y==1').shape[0])/(df_visitMoreThan1lessThan30.shape[0])


# In[138]:


print(round(visitMoreThan1lessThan30_AccetRate,2))


# In[145]:


d={'Criteria':['barCoupon_AcceptRate','custVisitBarlessthan3_acceptRate','custVisitBarmorethan3_acceptRate','custMoreThan1visit_agemorethan25_acceptRate','visitMoreThan1NotKidExpFarmFishFor_AccepRate','visitMoreThan1NotKidNotWidow_AcceptRate','visitMoreThan1lessThan30_AcceptRate'], 'AccpetRate':[0.41,0.37,0.77,0.68,0.68,0.70,0.52]}


# In[146]:


d=pd.DataFrame(data=d)


# In[147]:


d


# 7.  Based on these observations, what do you hypothesize about drivers who accepted the bar coupons?

# Based on the above dataframe results, customers visiting Bar more than 3 times having a greater acceptance rate over customers visiting bar less than 3 times. Among the other determining factors,the group of customers who go to bars more than once a month, had passengers that were not a kid, and were not widowed have a better acceptamce rate.

# ### Independent Investigation
# 
# Using the bar coupon example as motivation, you are to explore one of the other coupon groups and try to determine the characteristics of passengers who accept the coupons.  

# In[163]:


df_gender = pd.get_dummies(df, columns=['gender'])


# In[164]:


df_gender.head()


# In[167]:


male_count=df_gender['gender_Male'].sum()
female_count=df_gender['gender_Female'].sum()
labels=['Male','Female']
sizes=[male_count,female_count]
colors=['blue','pink']
plt.figure(figsize=(4,4))


# In[171]:


plt.pie(sizes, labels=labels,colors=colors,startangle=50,autopct='%.2f')
plt.axis('equal')


# Observation: Female customers tend to visit Bar more than Male customers.

# In[173]:


df.info()


# In[180]:


table=pd.crosstab(index=df['gender'], columns=df['maritalStatus'])
table.plot(kind='bar', stacked=True, edgecolor='black')
plt.xticks(rotation=20)


# Single Male customers visit Bar more often. Married Female customers visit Bar more often than other female marital status. 
