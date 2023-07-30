#!/usr/bin/env python
# coding: utf-8

# In[ ]:


lst: list[int] = [1, 2, 3, 4]
print("lst:", lst)


# In[ ]:


lst.append(5)
print("lst.append(5):", lst)


# In[ ]:


print("lst.count(10):", lst.count(10))
print("lst.count(5):", lst.count(5))


# In[ ]:


lst.extend([6, 7, 8])
print("lst.extend([6, 7, 8]):", lst)


# In[ ]:


print("lst.index(2):", lst.index(2))

try:
    lst.index(12) # Will need to be caught and handled
except Exception as e:
    print("lst.index(12):", e)


# In[ ]:


print("lst:", lst)
lst.insert(2, 22)
print("lst.insert(2, 22):", lst)


# In[ ]:


el: int = lst.pop()
print("el = lst.pop():", lst)
print("el:", el)


# In[ ]:


el = lst.pop(2)
print("el = lst.pop(2):", lst)
print("el:", el)


# In[ ]:


print("lst:", lst)

lst.insert(3, 2)
print("lst.insert(3, 2):", lst)

lst.remove(2)
print("lst.remove(2):", lst)

try:
    lst.remove(100) # Will need to be caught and handled
except Exception as e:
    print("lst.remove(100):", str(e).split(":")[1].strip())


# In[ ]:


lst.reverse()
print("lst.reverse():", lst)


# In[ ]:


lst.sort()
print("lst.sort():", lst)

lst.sort(reverse = True)
print("lst.sort(reverse=True):", lst)

lst.sort()
print("lst.sort():", lst)


