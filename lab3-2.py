#!/usr/bin/env python
# coding: utf-8

# In[11]:


def uniquenolist(list):
    res=[]
    for n in list:
        if n not in res:
            res.append(n)
    return (res)
list=[1,2,3,4,5,8,8,9,9,9,3,5,7]
uniquelist= uniquenolist(list)
print (uniquelist)


# In[ ]:




