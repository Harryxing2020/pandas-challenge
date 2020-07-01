#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np
# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"
# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# ## Player Count

# * Display the total number of players
# 

# In[2]:


# Display the total number of players
total_players = len( purchase_data["SN"].unique())
# Create a data frame
player_count = pd.DataFrame({"Total Players":[total_players]})
# format the dataframe
player_count.style.format({'Total Players':"{:}"})


# In[2]:





# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[4]:


number_item_ID = len((purchase_data["Item ID"]).unique())
average_price = round(purchase_data["Price"].mean(),2)
number_of_purchases = purchase_data["Purchase ID"].count()
total_revenue = purchase_data["Price"].sum()

# Create data frame with data
purchasing_analysis = pd.DataFrame({"Number of Unique Items":[number_item_ID],
                           "Average Price":[average_price], 
                           "Number of Purchases": [number_of_purchases], 
                           "Total Revenue": [total_revenue]})

# Format cell
purchasing_analysis.style.format({'Average Price':"${:,.2f}",'Total Revenue': '${:,.2f}'})


# In[3]:





# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[5]:


# Groupby gender
gender_group = purchase_data.groupby('Gender')

# Count players name by gender
total_count_gender = gender_group.nunique()['SN']

# Calculate the percentage of each gender 
percentage_of_players = total_count_gender / total_players 

# Create data frame with obtained values
gender_df= pd.DataFrame({ "Total Count": total_count_gender,"Percentage of Players": percentage_of_players})

# Format the data frame 
gender_df.index.name = None
gender_df = gender_df.sort_values(["Total Count"], ascending = False)

# Format the values sorted by total count
gender_df.style.format({"Percentage of Players":"{:.2%}"})


# In[4]:





# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[8]:


# group by gender 
total_count_gender = purchase_data.groupby(['Gender'])

#calculate count, average and sum
purchase_count = total_count_gender["Purchase ID"].count()
average_purchase_price = total_count_gender["Price"].mean()
total_purchase_value = total_count_gender["Price"].sum()

#average per person
total_purchase_per_person = total_purchase_value /purchase_data.groupby('Gender')['SN'].nunique()

# Format the data frame 
purchasing_analysis= pd.DataFrame({ "Purchase Count": purchase_count,
                                         "Average Purchase Price": average_purchase_price,
                                         "Total Purchase Value": total_purchase_value,
                                          "Avg Total Purchase per Person": total_purchase_per_person
                                         })


purchasing_analysis.index.name = None
# Format the values sorted by total count
purchasing_analysis.style.format({"Average Purchase Price":"${:,.2f}",
                                         "Total Purchase Value":"${:,.2f}",  
                                         "Avg Total Purchase per Person":"${:,.2f}"
                                        })


# In[5]:





# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[9]:


#divide 8 age range
purchase_data["Age Range"] = pd.cut(purchase_data["Age"] ,
                                     bins=[0, 9.99, 14.99, 19.99, 24.99, 29.99, 34.99, 39.99, 99999],
                                     labels= ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"])
#group by age range
age_range_grouped = purchase_data.groupby("Age Range")
age_range_grouped_total_count = age_range_grouped["SN"].nunique()
age_range_grouped_Percentage_Players =  age_range_grouped_total_count/total_players

# Format the data frame 
age_purchasing_analysis = pd.DataFrame({ "Total Count": age_range_grouped_total_count,
                                         "Percentage of Players": age_range_grouped_Percentage_Players
                                         })

#age_purchasing_analysis.index.name = None
# Format the values sorted by total count
age_purchasing_analysis.style.format({ "Percentage of Players":"{:.2%}"})


# In[6]:





# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[11]:


#calculate the number of purchase, mean and sum
purchase_ID = age_range_grouped["Purchase ID"].count()
average_purchase_price = age_range_grouped["Price"].mean()
total_purchase_value = age_range_grouped["Price"].sum()
avg_Total_Purchase_per_Person = total_purchase_value / age_range_grouped['SN'].nunique()

# Format the data frame 
purchasing_analysis = pd.DataFrame({ "Purchase Count": purchase_ID,
                                        "Average Purchase Price": average_purchase_price,
                                        "Total Purchase Value": total_purchase_value,
                                        "Avg Total Purchase per Person": avg_Total_Purchase_per_Person
                                        
                                         })

#purchasing_analysis.index.name = None
# Format the values sorted by total count
purchasing_analysis.style.format({ 
                                 "Average Purchase Price":"${:.2f}",
                                  "Total Purchase Value":"${:.2f}",
                                  "Avg Total Purchase per Person":"${:.2f}"
                                 })


# In[7]:





# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[224]:





# In[12]:


# groupby name 
sn_grouped = purchase_data.groupby("SN")
purchase_count = sn_grouped["Purchase ID"].count()
average_purchase_price = sn_grouped["Price"].mean()
total_purchase_value = sn_grouped["Price"].sum()

# Create data
top_spenders = pd.DataFrame({"Purchase Count": purchase_count,
                             "Average Purchase Price": average_purchase_price,
                             "Total Purchase Value":total_purchase_value})

# Sort
formatted_spenders = top_spenders.sort_values(["Total Purchase Value"], ascending=False).head()

# Format with currency style
formatted_spenders.style.format({"Average Purchase Total":"${:,.2f}",
                                 "Average Purchase Price":"${:,.2f}", 
                                 "Total Purchase Value":"${:,.2f}"})


# In[8]:





# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[14]:


# groupby name and item
grouped_item_data = purchase_data.groupby(['Item ID', 'Item Name'])

purchase_count_item = grouped_item_data["Purchase ID"].count()
total_purchase_value_item = grouped_item_data["Price"].sum()
item_price = total_purchase_value_item / purchase_count_item

most_popular_items = pd.DataFrame({"Purchase Count": purchase_count_item,
                             "Item Price": item_price,
                             "Total Purchase Value":total_purchase_value_item})

# Sort in descending 
formatted_spenders = most_popular_items.sort_values(["Total Purchase Value"], ascending=False).head(5)
formatted_spenders.style.format({"Item Price":"${:,.2f}", "Total Purchase Value":"${:,.2f}"})


# In[9]:





# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[267]:


# Take the most_popular items data frame and change the sorting to find highest total purchase value
popular_formatted = most_popular_items.sort_values(["Total Purchase Value"], ascending=False).head(3)
# Format with currency style
popular_formatted.style.format({"Item Price":"${:,.2f}","Total Purchase Value":"${:,.2f}"})


# In[ ]:




