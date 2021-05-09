n = int(input())
d_max = 0
repo = {}

def update(a, b, c):
  global ans1, ans2, d_max, repo, i
  if (a, b) in repo:
    seqNo, d = repo[(a, b)]  # this index is 1-based
    new_d = min(a, b, d + c)
    if new_d > d_max:
      d_max = new_d
      ans1 = 2
      ans2 = (seqNo, i+1)
    if c > d:
      repo[(a, b)] = (i+1, c)
  else:
    repo[(a, b)] = (i+1, c)

for i in range(n):
  vals = input().split()
  a, b, c = int(vals[0]), int(vals[1]), int(vals[2])
  small = min(a, b, c)
  large = max(a, b, c)
  medium = a + b + c - small - large
  # we solved the case 1 - no glue
  if small > d_max:
    d_max = small
    ans1 = 1
    ans2 = (i+1)
  # we have to solve the case 2 - glue
  # 1. (small, medium)
  update(small, medium, large)
  update(small, large, medium)
  update(medium, large, small)

print(ans1)
if ans1 == 1:
  print(ans2)
else:
  print(*ans2)