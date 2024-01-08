#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Pattern1


# In[10]:


n=7
i=1
while i<=n:
    j=1
    while j<=i:
        print(j, end=" ")
        j=j+1
    print("\n")
    i=i+1


# In[12]:


n=71
i=65
while i<=n:
    j=65
    while j<=i:
        print(chr(j), end=" ")
        j=j+1
    print("\n")
    i=i+1


# In[14]:


i=1
n=6

while i<=6:
    print("* "*i, end="\n")
    i=i+1


# In[18]:


i=1
n=7

while i<=n:
    j=0
    while j<i:
        print(i, end=" ")
        j=j+1
    print("\n")
    i=i+1
    


# In[20]:


i=65
n=71
x=1

while i<=n:
    print(chr(i)*x, end="\n")
    x=x+1
    i+=1


# In[23]:


x=1
i=5
n=1
while i>=n:
    print(" "*i,x*"*")
    x=x+1
    i-=1
    


# In[25]:


i=1
n=12

while i<=n:
    print((i*"*").center(12," "))
    i+=2


# In[95]:


s=" "
i=1
n=5
while i<=n:
    s+=f"{i}"+" "
    print(s.center(11, " "))
    i+=1
s=" "


# In[30]:


s=" "
i=5
n=1
while i>=n:
    s+=f"{i}"+" "
    print(s.center(11, " "))
    i-=1
s=" "


# In[37]:


s=" "
i=65
n=70
while i<=n:
    s+=chr(i)+" "
    i+=1
    print(s.center(13, " "))
s=" "


# In[39]:


s=" "
i=70
n=65
while i>=n:
    s+=chr(i)+" "
    i-=1
    print(s.center(13, " "))
s=" "


# In[49]:


s=" "
i=1
n=10
while i<=n:
    s=i*"*"
    i+=2
    print(s.center(13, " "))
s=" "


# In[57]:


i=1
n=6
s=" "
while i<=n:
    j=0
    while j<i:
        s+=f"{i}"+" "
        j=j+1

    print(s.center(13, " "))
    i=i+1
    s=" "
    


# In[61]:


i=65
n=71
s=" "
while i<=n:
    j=64
    while j<i:
        s+=chr(i)+" "
        j=j+1

    print(s.center(15, " "))
    i=i+1
    s=" "
    


# In[ ]:





# In[65]:


s=" "
i=1
n=7
while i<=n:
    s+=f"{i}"+" "
    print(s.center(15," "))
    i=i+1
s=" "


# In[ ]:





# In[68]:


i=6
n=1
while i>=n:
    j=1
    while j<=i:
        print(j, end=" ")
        j=j+1
    i=i-1
    print("\n")


# In[75]:


x=5
i=5
n=0
while i>=n:
    j=i
    while j>=1:
        print(x, end=" ")
        x=x-1
        j=j-1
    i=i-1    
    print("\n")
    x=5


# In[81]:


x=5
i=1
n=6
while i<=n:
    j=i
    while j>1:
        print(x, end=" ")
        x=x-1
        j=j-1
    i+=1
    print("\n")
    x=5


# In[85]:


x=1
i=1
n=6
while i<=n:
    j=i
    while j>=1:
        print(x, end=" ")
        x=x+1
        j=j-1
    i=i+1
    print("\n")


# In[94]:


i=1
n=6
while i<=n:
    j=65
    while j<=71-i:
        print(chr(j), end=" ")
        j=j+1
    i=i+1
        
    print("\n")

