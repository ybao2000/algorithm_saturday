# without resursive
n = int(input())

# method 1 - just add them up
#sum from 1 to 100 is famouse story - Gauss solved this problem 
# sum = 0
# i = 1
# while i <= n:
#   sum += i
#   i += 1  # need to increase i, otherwise, you get infinite loop
# print(sum)

# method 2 - Gauss way, using math formular n * (n+1) /2
# sum = (1+n)* n //2
# print(sum)

# method 3 - we are using recursive function
def sum_recursive(n):
  # base case
  if n == 1:
    return 1
  else:
    return sum_recursive(n-1) + n
  

s = sum_recursive(100)
print(s)