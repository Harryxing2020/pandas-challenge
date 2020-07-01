#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[12]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Calculate the percentage of students who passed math **and** reading (% Overall Passing)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[70]:


#Calculate the total number of schools
total_schools = school_data["School ID"].count()
#Calculate the total number of students
total_students = student_data["Student ID"].count()
#Calculate the total budget
total_budget = school_data["budget"].sum()
#Calculate the average math score 
average_math_score = student_data["math_score"].mean()
#Calculate the average reading score
average_reading_score = student_data["reading_score"].mean()
#Calculate the percentage of students with a passing math score (70 or greater)
student_math_data_morethan_70 = student_data[student_data["math_score"]>=70]
passing_math = student_math_data_morethan_70["Student ID"].count() /total_students
#Calculate the percentage of students with a passing reading score (70 or greater)
student_reading_data_morethan_70 = student_data[student_data["reading_score"] >=70]
passing_reading = student_reading_data_morethan_70["Student ID"].count()/ total_students
#Calculate the percentage of students who passed math and reading (% Overall Passing)
student_math_reading_data_morethan_70 = student_data[(student_data["math_score"]>=70) & (student_data["reading_score"] >=70) ]
overall_passing_rate = student_math_reading_data_morethan_70["Student ID"].count()/ total_students

# district dataframe
district_summary = pd.DataFrame({                           
                             "Total Schools": [total_schools],
                             "Total Students": [total_students],
                            "Total Budget": [total_budget], 
                             "Average Math Score": [average_math_score],
                             "Average Reading Score": [average_reading_score],
                             "% Passing Math":[passing_math* 100],
                             "% Passing Reading":[passing_reading *100],
                             "% Overall Passing Rate":[overall_passing_rate*100]
                            })

district_summary.index.name = None
#format cells
district_summary.style.format({"Total Budget":"${:,.2f}", "Average Math Score":"{:,.2f}",
                          "Average Reading Score":"{:,.2f}",
                           "% Passing Math":"{:,.2f}","% Passing Reading":"{:,.2f}",
                          "% Overall Passing Rate":"{:,.2f}"
                          })


# In[71]:


#groupby school name in school and student 
school_data_grouped_studentDB = student_data.groupby("school_name")
school_data_grouped_schoolDB = school_data.groupby("school_name")

#school type
school_types = school_data.set_index('school_name')['type']
#count student in student group
total_students = school_data_grouped_studentDB["Student ID"].count()
#sum budget in school group
total_school_budget=school_data_grouped_schoolDB["budget"].sum()
#Student Budget per student
per_student_budget = total_school_budget /total_students
#average math score
average_math_score = school_data_grouped_studentDB["math_score"].mean()
#average reading score
average_reading_score =school_data_grouped_studentDB["reading_score"].mean()

# % prepare math and reading score morethan 70
student_math_morethan_70 = student_data[student_data["math_score"] >= 70].groupby("school_name")["Student ID"].count() 
student_reading_morethan_70  = student_data[student_data["reading_score"] >= 70].groupby("school_name")["Student ID"].count() 
student_math_reading_morethan_70 = student_data[(student_data["math_score"] >= 70) & (student_data["reading_score"] >= 70)].groupby("school_name")["Student ID"].count()

# school dataframe
top_spenders = pd.DataFrame({                           
                             "School Type": school_types,
                            "Total Students": total_students, 
                            "Total School Budget":total_school_budget,
                             "Per Student Budget": per_student_budget,
                             "Average Math Score": average_math_score,
                             "Average Reading Score": average_reading_score,
                             "% Passing Math": student_math_morethan_70 / total_students * 100,
                             "% Passing Reading": student_reading_morethan_70/ total_students * 100,
                             "% Overall Passing": student_math_reading_morethan_70/ total_students *100
                            })
top_spenders.index.name = None
#format cells
top_spenders.style.format({"Total School Budget":"${:,.2f}", "Per Student Budget":"${:,.2f}",
                          "Average Math Score":"{:,.2f}","Average Reading Score":"{:,.2f}",
                           "% Passing Math":"{:,.2f}","% Passing Reading":"{:,.2f}",
                          "% Overall Passing":"{:,.2f}"
                          })


# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * % Overall Passing (The percentage of students that passed math **and** reading.)
#   
# * Create a dataframe to hold the above results

# In[9]:





# ## Top Performing Schools (By % Overall Passing)

# * Sort and display the top five performing schools by % overall passing.

# In[84]:


#Sort the overall passing
top_spenders_top5 = top_spenders.sort_values(["% Overall Passing"], ascending=False)
#format cells
top_spenders_top5.head(5).style.format({"Total School Budget":"${:,.2f}", "Per Student Budget":"${:,.2f}",
                          "Average Math Score":"{:,.2f}","Average Reading Score":"{:,.2f}",
                           "% Passing Math":"{:,.2f}","% Passing Reading":"{:,.2f}",
                          "% Overall Passing":"{:,.2f}"
                          })


# In[10]:





# ## Bottom Performing Schools (By % Overall Passing)

# * Sort and display the five worst-performing schools by % overall passing.

# In[85]:


#Sort the overall passing
top_spenders_tail5 = top_spenders.sort_values(["% Overall Passing"], ascending=True)
#format cells
top_spenders_tail5.head(5).style.format({"Total School Budget":"${:,.2f}", "Per Student Budget":"${:,.2f}",
                          "Average Math Score":"{:,.2f}","Average Reading Score":"{:,.2f}",
                           "% Passing Math":"{:,.2f}","% Passing Reading":"{:,.2f}",
                          "% Overall Passing":"{:,.2f}"
                          })


# In[11]:





# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[86]:


#creates grade level average math scores
student_math_average9  = student_data[student_data["grade"] == "9th"].groupby("school_name")["math_score"].mean() 
student_math_average10  = student_data[student_data["grade"] == "10th"].groupby("school_name")["math_score"].mean() 
student_math_average11  = student_data[student_data["grade"] == "11th"].groupby("school_name")["math_score"].mean() 
student_math_average12  = student_data[student_data["grade"] == "12th"].groupby("school_name")["math_score"].mean() 
top_spenders_th = pd.DataFrame({ "9th": student_math_average9,
                            "10th": student_math_average10, 
                            "11th":student_math_average11,
                             "12th": student_math_average12
                            })
top_spenders_th.index.name = None
#format cells
top_spenders_th.style.format({"9th":"${:,.2f}", "10th" :"{:,.2f}", "11th" :"{:,.2f}", "12th" :"{:,.2f}"})


# In[12]:





# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[87]:


#creates grade level average reading scores
student_reading_average9  = student_data[student_data["grade"] == "9th"].groupby("school_name")["reading_score"].mean() 
student_reading_average10  = student_data[student_data["grade"] == "10th"].groupby("school_name")["reading_score"].mean() 
student_reading_average11  = student_data[student_data["grade"] == "11th"].groupby("school_name")["reading_score"].mean() 
student_reading_average12  = student_data[student_data["grade"] == "12th"].groupby("school_name")["reading_score"].mean() 
top_spenders_th = pd.DataFrame({ "9th": student_reading_average9,
                            "10th": student_reading_average10, 
                            "11th":student_reading_average11,
                             "12th": student_reading_average12
                            })
top_spenders_th.index.name = None
#format cells
top_spenders_th.style.format({"9th":"${:,.2f}", "10th" :"{:,.2f}", "11th" :"{:,.2f}", "12th" :"{:,.2f}"})


# In[13]:





# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[92]:


top_spenders["Spending Ranges (Per Student)"] = pd.cut(top_spenders["Per Student Budget"] ,
                                     bins=[0, 584, 629, 644, 999999], # create spending bins
                                     labels= ["<$584", "$585-629", "$630-644", "$645-675"]) # create labels
#group by spending
age_range_grouped = top_spenders.groupby("Spending Ranges (Per Student)")

Scores_by_School_Spending = pd.DataFrame({                           
                             "Average Math Score": age_range_grouped["Average Math Score"].mean(),
                            "Average Reading Score": age_range_grouped["Average Reading Score"].mean(),
                            "% Passing Math": age_range_grouped["% Passing Math"].mean(),
                            "% Passing Reading": age_range_grouped["% Passing Reading"].mean(),
                            "% Overall Passing": age_range_grouped["% Overall Passing"].mean(),
                            })

#Scores_by_School_Spending.index.name = None
#format cells
Scores_by_School_Spending.style.format({"Average Math Score":"${:,.2f}", "Average Reading Score":"${:,.2f}",
                          "% Passing Math":"{:,.2f}","% Passing Reading":"{:,.2f}",
                            "% Overall Passing":"{:,.2f}"
                          })


# In[18]:





# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[93]:


top_spenders["School Size"] = pd.cut(top_spenders["Total Students"] ,
                                     bins=[0, 999, 1999, 9999999999], # create spending bins
                                     labels= ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]) # create labels

group_name = ["Small (<1000)", "Medium (1000-2000)" , "Large (>2000)"]


school_size_grouped = top_spenders.groupby("School Size")

school_size = pd.DataFrame({                           
                             "Average Math Score": school_size_grouped["Average Math Score"].mean(),
                            "Average Reading Score": school_size_grouped["Average Reading Score"].mean(),
                            "% Passing Math": school_size_grouped["% Passing Math"].mean(),
                            "% Passing Reading": school_size_grouped["% Passing Reading"].mean(),
                            "% Overall Passing": school_size_grouped["% Overall Passing"].mean(),
                            })

#Scores_by_School_Spending.index.name = None

school_size.style.format({"Average Math Score":"${:,.2f}", "Average Reading Score":"${:,.2f}",
                          "% Passing Math":"{:,.2f}","% Passing Reading":"{:,.2f}",
                            "% Overall Passing":"{:,.2f}" })


# In[22]:





# ## Scores by School Type

# * Perform the same operations as above, based on school type

# In[37]:


# group by type of school
scores_by_school_type_grouped = top_spenders.groupby("School Type")

#data preparation
scores_by_school_type = pd.DataFrame({                           
                             "Average Math Score": scores_by_school_type_grouped["Average Math Score"].mean(),
                            "Average Reading Score": scores_by_school_type_grouped["Average Reading Score"].mean(),
                            "% Passing Math": scores_by_school_type_grouped["% Passing Math"].mean(),
                            "% Passing Reading": scores_by_school_type_grouped["% Passing Reading"].mean(),
                            "% Overall Passing": scores_by_school_type_grouped["% Overall Passing"].mean(),
                            })

#Scores_by_School_Spending.index.name = None

scores_by_school_type.style.format({"Average Math Score":"${:,.2f}", "Average Reading Score":"${:,.2f}",
                          "% Passing Math":"{:,.2f}","% Passing Reading":"{:,.2f}",
                            "% Overall Passing":"{:,.2f}" })


# In[24]:




