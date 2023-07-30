#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pdb
from typing import Any

x: list[int] = [1, 3, 4]
y: int = 2
z: int = 3

result: int = y + z
print(result)

# Set a trace using Python Debugger
# This is equivalent to a breakpoint
pdb.set_trace()

result2: Any = y + x # Error on purpose
print(result2)


