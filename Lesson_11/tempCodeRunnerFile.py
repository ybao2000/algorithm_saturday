import random

n = 20
a = []
for i in range(n):
  a.append(random.randint(-100, 100))
# a = [40, 74, 49, -42, -98, -31, 58, 33, -56, 67, 12, 12, -73, -69, 38, -91, -80, -93, 32, -53]
a = [-72, -93, 76, -70, -66, 57, -75, 47, 7, -12, 90, -63, 83, 63, -48, -79, -80, -37, 93, -59]

print(a)
# first method: brute force
s_max = None
for i in range(n):
  s = 0
  for j in range(i, n):
    s += a[j]
    if s_max is None or s > s_max:
      s_max = s
      i_max = i
      j_max = j

print(s_max, i_max, j_max)