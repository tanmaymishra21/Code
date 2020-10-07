
# coding: utf-8

# In[1]:


#printing the maximum value and largest number in the list
data=[22,60,78,99,2,6,10]
print(max(data))


# In[3]:


#printing the second largest number in the list
data=[22,60,78,99,2,6,10]
data.sort()
print('second largest number in the list', data[-2])


# In[5]:


#first merge two lists and sort it
data=[22,60,78,99,2,6,10]
data1=[1,34,45,6,77,8]
data2=data+data1
data2.sort()
print(data2)


# In[6]:


#Swap the first and last value of a list
data=[22,60,78,99,2,6,10]
data[0],data[-1]=data[-1],data[0]
print(data)

