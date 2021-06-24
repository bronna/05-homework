#!/usr/bin/env python
# coding: utf-8

# # Homework 5, Part 2: Answer questions with pandas
# 
# **Use the Excel file to answer the following questions.** This is a little more typical of what your data exploration will look like with pandas.

# ## 0) Setup
# 
# Import pandas **with the correct name** .

# In[3]:


import pandas as pd


# ## 1) Reading in an Excel file
# 
# Use pandas to read in the `richpeople.xlsx` Excel file, saving it as a variable with the name we'll always use for a dataframe.
# 
# > **TIP:** You will use `read_excel` instead of `read_csv`, *but you'll also need to install a new library*. You might need to restart your kernel afterward!

# In[4]:


df = pd.read_excel("richpeople.xlsx")
df.head()


# ## 2) Checking your data
# 
# Display the number of rows and columns in your data. Also display the names and data types of each column.

# In[5]:


number_of_rows = len(df.index)
number_of_rows


# In[6]:


number_of_columns = len(df.columns)
number_of_columns


# In[7]:


df.dtypes


# ## 3) Who are the top 10 richest billionaires? Use the `networthusbillion` column.

# In[8]:


df.sort_values(by="networthusbillion", ascending=False).head(10)


# ## 4) How many male billionaires are there compared to the number of female billionares? What percent is that? Do they have a different average wealth?
# 
# > **TIP:** The last part uses `groupby`, but the count/percent part does not.
# > **TIP:** When I say "average," you can pick what kind of average you use.

# In[9]:


numbers = df.gender.value_counts()
numbers


# In[10]:


percents = ((df.gender.value_counts(normalize=True))*100).round(2)
percents


# In[11]:


averages = (df.groupby(by="gender").networthusbillion.mean()).round(2)
averages


# ## 5) What is the most common source/type of wealth? Is it different between males and females?
# 
# > **TIP:** You know how to `groupby` and you know how to count how many times a value is in a column. Can you put them together???
# > **TIP:** Use percentages for this, it makes it a lot more readable.

# In[134]:


(df.typeofwealth.value_counts(normalize=True)*100).round(2)


# In[132]:


(df.sourceofwealth.value_counts(normalize=True)*100).round(2).head(5)


# In[135]:


(df.groupby(by="gender").typeofwealth.value_counts(normalize=True)*100).round(2)


# ## 6) What companies have the most billionaires? Graph the top 5 as a horizontal bar graph.
# 
# > **TIP:** First find the answer to the question, then just try to throw `.plot()` on the end
# >
# > **TIP:** You can use `.head()` on *anything*, not just your basic `df`
# >
# > **TIP:** You might feel like you should use `groupby`, but don't! There's an easier way to count.
# >
# > **TIP:** Make the largest bar be at the top of the graph
# >
# > **TIP:** If your chart seems... weird, think about where in the process you're sorting vs using `head`

# In[127]:


df.groupby(by="company").company.count().sort_values(ascending=False).head()


# In[128]:


df.groupby(by="company").company.count().sort_values(ascending=False).head().plot(kind="barh")


# In[103]:


df.groupby(by="sourceofwealth").networthusbillion.sum().sort_values(ascending=False).head()


# In[139]:


df[df.sourceofwealth=="diversified"].head(5)


# ## 7) How much money do these billionaires have in total?

# In[144]:


total_worth = df.networthusbillion.sum()
print(f'All of the billionaires have a total worth of ${total_worth:.1f} Billion')


# ## 8) What are the top 10 countries with the most money held by billionaires?
# 
# I am **not** asking which country has the most billionaires - this is **total amount of money per country.**
# 
# > **TIP:** Think about it in steps - "I want them organized by country," "I want their net worth," "I want to add it all up," and "I want 10 of them." Just chain it all together.

# In[86]:


df.groupby(by="citizenship").networthusbillion.sum().sort_values(ascending=False).head(10)


# ## 9) How old is an average billionaire? How old are self-made billionaires  vs. non self-made billionaires? 

# In[146]:


avg_age = df.age.mean()
print(f'The average age of a billionaire is {avg_age:.1f}')


# In[147]:


avg_age_selfmade = df[df.selfmade == "self-made"].age.mean()
print(f'The average age of a self-made billionaire is {avg_age_selfmade:.1f}')


# In[148]:


avg_age_nonselfmade = df[df.selfmade == "inherited"].age.mean()
print(f'The average age of a non self-made billionaire is {avg_age_nonselfmade:.1f}')


# ## 10) Who are the youngest billionaires? Who are the oldest? Make a graph of the distribution of ages.
# 
# > **TIP:** You use `.plot()` to graph values in a column independently, but `.hist()` to draw a [histogram](https://www.mathsisfun.com/data/histograms.html) of the distribution of their values

# In[43]:


df.sort_values(by="age").head(3)


# In[44]:


df.sort_values(by="age", ascending=False).head(3)


# In[46]:


df.sort_values(by="age").age.hist()


# ## 11) Make a scatterplot of net worth compared to age

# In[57]:


df.plot.scatter(x="age", y="networthusbillion")


# In[72]:


df.plot.hexbin(x="age", y="networthusbillion", gridsize=50, figsize=(12,8))


# ## 13) Make a bar graph of the wealth of the top 10 richest billionaires
# 
# > **TIP:** When you make your plot, you'll need to set the `x` and `y` or else your chart will look _crazy_
# >
# > **TIP:** x and y might be the opposite of what you expect them to be

# In[80]:


df.sort_values(by="networthusbillion", ascending=False).head(10).plot(kind="bar", x="name", rot=45, y="networthusbillion")

