# Given an integer, create a function which returns the sum of all individual digits in that integer. 
# For example, if n = 4321, return 4+3+2+1 = 10
import time
import random
n = random.randint(10000, 100000)
print(n)
# sum =0
# # iterative way
# while n >= 10:
#   r = n % 10
#   sum += r
#   n //= 10
# sum += n

# print(sum)

# how to solve it in recursive way
def sum(n):
  if n < 10:  # base case
    return n
  else:
    return (n % 10) + sum(n//10)

print(sum(n))
