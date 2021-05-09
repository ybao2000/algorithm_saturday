# B. Obtain Two Zeroes
t = int(input())
for i in range(t):
  vals = input().split()
  a = int(vals[0])
  b = int(vals[1])
  v1 = 2 * a - b
  v2 = 2 * b - a
  if v1 >= 0 and v1 % 3 == 0 and v2 >= 0 and v2 % 3 == 0:
    print("YES")
  else:
    print("NO")