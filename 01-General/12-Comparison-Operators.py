#!/usr/bin/env python
# coding: utf-8

print(2 == 2)
print(1 == 0)
print('1' == 1) # Comparison is by identity by default


print(2 != 1)
print(2 != 2)


print(2 > 1)
print(2 > 4)
print(2 >= 2)
print(2 >= 1)


print(2 < 4)
print(2 < 1)
print(2 <= 2)
print(2 <= 4)


print(1 < 2 < 3) # Similar to using AND


print(1 < 2 and 2 < 3)


print(1 < 3 > 2)


print(1 < 3 and 3 > 2)


print(1 == 2 or 2 < 3)


print(1 == 1 or 100 == 1)


print(1 == 1 and 1 == 2 or 3 > 4 or 1 < 2 < 3 or 4 > 5 and 6 > 5 and 5 < 4 and 4 > 5 or 6 >= 4)


print(((((1 == 1 == 2) or 3 > 4) or 1 < 2 < 3) or (((4 > 5 and 6 > 5) and 5 < 4) and 4 > 5)) or (6 >= 4))


print(not 1 == 1)


