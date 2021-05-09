# A. Cut Ribbon
# what if I want minimum
vals = input().split()
n = int(vals[0])
a = int(vals[1])
b = int(vals[2])
c = int(vals[3])

# we need to initialize the dp
# dp is the solution to size from 0, 1, n
dp = [n+1] * (n+1)  # for maximum, we use -1, for minimum, we use n+1 which means impossible
# base case - when ribbon has length of 0, max cut is 0
dp[0] = 0   # this is base case
for i in range(1, n+1):
  # this is the formula, but you cannot directly use it
  # dp[n] = max(dp[n-a]+1, dp[n-b]+1, dp[n-c]+1) = max(xa, xb, xc)
  if i < a or dp[i-a] == n+1:
    xa = n+1
  else:
    xa = dp[i-a] + 1
  if i < b or dp[i-b] == n+1:
    xb = n+1
  else:
    xb = dp[i-b] + 1
  if i < c or dp[i-c] == n+1:
    xc = n+1
  else:
    xc = dp[i-c] + 1
  dp[i] = min(xa, xb, xc)

print(dp[n])