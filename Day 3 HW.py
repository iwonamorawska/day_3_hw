#!/usr/bin/env python
# coding: utf-8

# # Question 1
# Build a Shopping Cart
# You can use either lists or dictionaries. The program should have the following capabilities:
# 
# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

# In[52]:


l=[]
store=input("What do you need from the store?")
question=input("Would you like to add another item?(yes/no)")
l.append(store)
while question!='no':
    store=input("What do you need from the store?")
    question=input("Would you like to add another item?(yes/no)")  
    l.append(store)
for item in l:
    print(l)


# # 2) Create a Module in VS Code and Import It into jupyter notebook
# Module should have the following capabilities:
# 
# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area
# 
# 2) Has a function to calculate the circumference of a circle
# 
# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage

# In[ ]:


import module

module.get_area()

module.get_circ()

