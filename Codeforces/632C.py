# C. The Smallest String Concatenation
# import functools
from functools import cmp_to_key

n = int(input())
a = []  #put all string in a list
for i in range(n):
  a.append(input())

def str_comp(x1, x2):
  if x1 + x2 < x2 + x1:
    return -1
  else:
    return 1

a.sort(key=cmp_to_key(str_comp))

print(''.join(a))
