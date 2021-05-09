# B. Obtain Two Zeroes

def bs(a, b):
  left, right = 0, a
  while left <= right:
    mid = (left + right)//2
    v1 = a - mid
    v2 = b - 2 * mid
    if v1 == 2 * v2:
      return True
    elif v1 > 2 * v2:
      right = mid - 1
    else:
      left = mid + 1
  return False
    

t = int(input())
for i in range(t):
  vals = input().split()
  a = int(vals[0])
  b = int(vals[1])

  # we are going to define a bs function
  if bs(a, b):
    print("YES")
  else:
    print("NO")