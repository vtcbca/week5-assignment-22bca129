#!/usr/bin/env python
# coding: utf-8

# In[1]:


###Write a python program create csv file student.csv(sid,sname,city,contact) using 10 records
import csv


# In[2]:


f=open('c:\sqlite3\csv\student.csv','w',newline='')


# In[3]:


w=csv.writer(f)


# In[4]:


header=["sid","sname","city","contact"]
w.writerow(header)


# In[5]:


row=[[1,"ekta","buhari",9873542678],[2,"saloni","surat",5678543426],[3,"kask","gala",67543678921],[4,"diya","surat",57835467231],[5,"akshita","buhari",5647839786]]
w.writerows(row)


# In[7]:


f.close()


# In[ ]:




