#!/usr/bin/env python
# coding: utf-8

# In[4]:


def rev_string(str):  
    str1 = ""  
    for i in str:  
        str1 = i + str1  
    return str1      
     
str = input("")         
print("The original string is: ",str)  
print("The reverse string is",rev_string(str))   


# In[ ]:




