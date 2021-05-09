num = int(input())

# method 1: recursive way
def fact(n):
  if n == 1:
    return 1
  else:
    return fact(n-1) * n

# print(fact(num))

# method 2: iterative way
f = [0, 1]
for i in range(2, num+1):
  prod = f[i-1] * i
  f.append(prod)

print(f[num])