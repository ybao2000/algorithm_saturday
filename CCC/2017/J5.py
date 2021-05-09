# Nailed It!
N = int(input())
vals = input().split()

repo = {} # make a dictionary called repo (repository)
for val in vals:
  h = int(val)
  if h in repo:
    repo[h] += 1
  else:
    repo[h] = 1

# find all possible heights
heights = set()
for h1 in repo.keys():
  for h2 in repo.keys():
    h = h1 + h2
    if h not in heights:
      heights.add(h)

max_length = 0
count = 0
for height in heights:
  length = 0  # this is to be accumulated with different combinations
  for p1 in range(1, height//2+1):  # add one to make sure height//2 is included
    p2 = height-p1
    if p1 in repo and p2 in repo:
      if p1 == p2:
        length += repo[p1]//2
      else:
        length += min(repo[p1], repo[p2])
  if length > max_length:
    max_length = length
    count = 1
  elif length == max_length:
    count += 1

print(max_length, count)