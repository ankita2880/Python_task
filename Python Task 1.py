#!/usr/bin/env python
# coding: utf-8

# ## Customer churn prediction

# #### Importing Librraies

# In[33]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Churn_Modelling.csv')


# In[39]:


df.head()


# By this command by default you can see the first 5 rows of the table.

# In[41]:


df.tail()


# Here you can see the last 5 rows of the table.

# In[44]:


plt.subplot(1,2,2)
sns.countplot('HasCrCard',hue = 'IsActiveMember', data = df)
plt.title('Churn who is Inactive & have credit card')


# This graph shows that howmany members are there who have credit card and active and who have credit card and Inactive.
# 

# In[45]:


x = df['Tenure']
y = df['Age']

plt.xlabel('Tenure',fontsize = 10)
plt.ylabel('Age', fontsize = 10)
plt.bar(x,y)

plt.show()


# This Graph shows that which age having howmuch tenure.

# In[6]:


plt.pie(y, labels = x, radius= 1.2, autopct = '%0.01f%%', shadow = True)
plt.show()


# This is a pie plot.

# In[47]:


plt.xlabel('Tenure',fontsize = 10)
plt.ylabel('Age', fontsize = 10)
plt.scatter(x,y)
# plt.plot(x,y)
plt.show()


# In[17]:


plt.plot(df.head(100)["Age"])
plt.xlabel('CreditScore')
plt.ylabel('Tenure')
plt.title('Credit of the year')


# This is the graph of first 100 data which shows the tenure and the credit scores.

# In[9]:


# Create a new column indicating if age is greater or less than 40
df['age_category'] = df['Age'].apply(lambda x: 'greater than 40' if x > 40 else 'less than 40')

counts = df.groupby(['Gender', 'age_category'])['Age'].count().reset_index()

# Plot the counts using a bar plot
sns.barplot(x='Gender', y='Age', hue='age_category', data=counts)
plt.title('Counts of Males and Females by Age Category')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


# The graph shows how many male and female having age greter than or less than 40.

# In[10]:


# Create a new column indicating if tenure is 1 or less than 1
df['tenure_category'] = df['Tenure'].apply(lambda x: '1 or less than 1' if x <= 1 else 'greater than 1')

counts = df.groupby(['Gender', 'tenure_category'])['Tenure'].count().reset_index()

# Plot the counts using a bar plot
sns.barplot(x='Gender', y='Tenure', hue='tenure_category', data=counts)
plt.title('Counts of Males and Females by Tenure Category')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


# The graph shows the tenure of male and female.

# In[20]:


df.head(10)


# Getting the first 10 rows of the table.

# In[19]:


plt.plot(df.head(100)["CustomerId"])
plt.xlabel('CustomerId')
plt.ylabel('Balance')
plt.title('Balance of the year')


# Here we are showing the graph between customer id and balance of the year.

# In[21]:


plt.plot(df.head(100)["CustomerId"])
plt.xlabel('CustomerId')
plt.ylabel('Exited')


# This shows that which customer Id is exited or which is not.

# In[22]:


sns.set(style="darkgrid")

# Plot the count of countries with tenure 1 or less and greater than 1
ax = sns.countplot(x="Geography", hue="Tenure", data=df, palette="Set1")

# Set labels and title
ax.set_xlabel("Country")
ax.set_ylabel("Count")
ax.set_title("Tenure by Country")

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Show the plot
plt.show()


# This graph shows how many tenure is there by country wise. Like which country have how many numbers of churn present.

# In[23]:


df


# In[24]:


df.isnull().sum()


# To check the null value of the whole table

# In[48]:


df.nunique()


# To get unique count for each variables.

# In[49]:


labels = 'Exited', 'Retained'
sizes = [df.Exited[df['Exited']==1].count(), df.Exited[df['Exited']==0].count()]
explode = (0, 0.1)
fig1, ax1 = plt.subplots(figsize=(10, 8))
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.title("Proportion of customer churned and retained", size = 20)
plt.show()


# So here we can see 20% of the customers having churned and 80% customers unchurned.

# In[32]:


fig, axarr = plt.subplots(2, 2, figsize=(15, 12))
sns.countplot(x='Geography', hue = 'Exited',data = df, ax=axarr[0][0])
sns.countplot(x='Gender', hue = 'Exited',data = df, ax=axarr[0][1])
sns.countplot(x='HasCrCard', hue = 'Exited',data = df, ax=axarr[1][0])
sns.countplot(x='IsActiveMember', hue = 'Exited',data = df, ax=axarr[1][1])


# These are the graphs which shows that 
# - Majority of the data is from persons from France.[Geography & Exited]
# - The proportion of female customers churning is also greater than that of male customers.[Gender & Exited]
# - majority of the customers that churned are those with credit card. [HasCrCard & Exited]
# - The inactive members have a greater churn.[IsActiveMember & Exited]

# In[29]:


plt.subplot(1,2,2)
sns.countplot(x = 'IsActiveMember',hue = 'Exited', data = df)


# The overall proportion of inactive mebers is quite high suggesting that the bank may need a program implemented to turn this group to active customers as this will definately have a positive impact on the customer churn.
