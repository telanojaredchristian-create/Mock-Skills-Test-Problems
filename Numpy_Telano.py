#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np


# In[9]:


# 1D Array 
el = np.array([1, 2, 3]) 
el 

# el = [1, 2, 3]


# In[10]:


# 2D Array - matrix 
psy = np.array([(2.4, -1.5, 1.2), (2.3, -2.4, -5.6)])
psy

# psy = [2.4 -1.5  1.2
#        2.3 -2.4 -5.6]


# In[12]:


# 3D Array - tensor 
kongroo = np.array([[(1.1,2,3.4),(7,2.5,9)],[(1,2,3),(9,8,7)]])
kongroo


# In[22]:


# Create an array of m x n x p zeros 
x = np.zeros((2, 3))  # 2 rows, 3 columns 
x


# In[21]:


y = np.ones((2, 3)) 
y


# In[20]:


# Syntax: np.linspace(first:last:number of samples) 
np.linspace(3,7,10)


# In[19]:


# Syntax: np.arange(first:last-interval:interval)

z = np.arange(3, 7, 0.5)
z


# In[18]:


np.full((2,3),8)


# In[17]:


# identity matrix: np.eye(m)
np.eye(4)


# In[13]:


#Viewing the contents on a numpy file
#Syntax = np.load('filename.npy')
data = np.load('epk.npy')
data


# In[16]:


np.random.random((2,3))


# In[14]:


data.shape


# In[ ]:


data.ndim


# In[15]:


data.size


# In[24]:


a = np.array([(2,4,6),(8,10,12)])
a


# In[25]:


b = np.array([(4,9),(16,25),(36,49)])
b


# In[26]:


c = np.array([2,3,5])
c


# In[27]:


# Element-wise
c-a


# In[28]:


a+c


# In[29]:


a*c


# In[30]:


c*a


# In[31]:


a/c


# In[32]:


c/a


# In[33]:


a


# In[34]:


b


# In[35]:


np.exp(b)


# In[36]:


np.sqrt(b)


# In[37]:


np.sin(b)


# In[38]:


np.log(b)


# In[39]:


a = np.array([2,3,5])
a


# In[40]:


b = np.array([(1,2,5),(4,5,6),(7,8,9)])
b


# In[41]:


# = is an assignment operator
c = a
c


# In[42]:


a == b


# In[43]:


b < 7


# In[44]:


a > 2


# In[45]:


# As a group 
np.array_equal(a,b) 


# In[46]:


np.array_equal(a,c)


# In[ ]:


# Subsetting, slicing, and indexing of arrays


# In[47]:


A = np.array([(1,2,3),(4,5,6),(7,8,9)]) 
A


# In[48]:


# Subsetting - getting a certain element from the array or structure 
A[1,1] #or A[1,1]


# In[49]:


A[2,1]


# In[50]:


# Slicing - getting the portion from an array or structure
A


# In[58]:


A[0:3]


# In[54]:


A[0:3,2]


# In[55]:


A[1]


# In[59]:


# Indexing - getting a certain element or depending on the conditions 
A[A<7] 


# In[60]:


A[A>2]


# In[61]:


A[A==5]


# In[62]:


# ndarray Manipulation 
a = np.array([3,2,1])
a


# In[63]:


b = np.array([(4,6,5),(3,2,1)])
b


# In[64]:


c = np.linspace(10,20,3)
c


# In[65]:


d = np.full((2,2),7)
d


# In[66]:


e = np.eye(2)
e


# In[67]:


a.sort()
a


# In[68]:


b


# In[69]:


b.sort(axis=0) #pag axis 0 by row
b


# In[70]:


b.sort(axis=1) #pag axis 1 by column
b


# In[71]:


np.shape(b)


# In[102]:


b.reshape(6,1).shape
b


# In[93]:


b.resize(6,1)
b


# In[94]:


d


# In[95]:


e


# In[96]:


np.append(d,e)


# In[97]:


a


# In[98]:


np.insert(a,1,5)


# In[99]:


np.delete(a,[2])


# In[100]:


np.concatenate((a,c),axis=0)


# In[103]:


np.vstack((a,c))


# In[104]:


np.hstack((d,e))


# In[105]:


np.hsplit(a,3)


# In[106]:


np.vsplit(e,2)


# In[ ]:




