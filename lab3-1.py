#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def maxof2numbers (x,y):
    if x>y:
        return (x)
    else :
        return (y)
    x=float(x)
    y=float(y)
def maxof3numbers (x,y,z):
    m= maxof2numbers (x,y)
    final= maxof2numbers (m,z)
    z=float(z)
    return(final)

x=input('plz enter 1st number ')
y=input('plz enter 2nd number ')
z=input('plz enter 3rd number ')
res=maxof3numbers (x,y,z)
print('max number is ',res)


# In[ ]:




