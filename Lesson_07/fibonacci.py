n = int(input())

# method 1: recursive way - very easy to implement
# fibo(n) = fibo(n-1) + fibo(n-2)
# n = 0, 0
# n = 1, 1
# n = 2, 1
# n = 3, 2
# n = 4, 3
# n = 5, 5
# n = 6, 8
# n = 7, 13
# n = 8, 21
# n = 9, 34
# n = 10, 55
def fibo_recursive(n):
  if n == 0:
    return 0
  elif n==1:
    return 1
  else:
    return fibo_recursive(n-1) + fibo_recursive(n-2)

# print(fibo(n))

# method 2: iterative way
fibo = [0, 1]  # base
for i in range(2, n+1):
  sum = fibo[i-1] + fibo[i-2]
  fibo.append(sum)

print(fibo[n])
