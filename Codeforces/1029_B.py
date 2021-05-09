# B. Creating the Contest

n = int(input()) # get the size
vals = input().split()  # get the list
a = [int(val) for val in vals] # convert into int

# dp is the solution for i when a[i] is included
dp = [1] * n
for i in range(1, n):
  if a[i] <= a[i-1] * 2:
    dp[i] = dp[i-1] + 1

print(max(dp))