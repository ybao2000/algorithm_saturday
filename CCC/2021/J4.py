vals = input()
# step 1 - count #
l, m, s = 0, 0, 0 
for val in vals:
  if val == "L":
    l += 1
  elif val == "M":
    m += 1
  else:
    s += 1
repo = [0] * 6
for i in range(len(vals)):
  c = vals[i]
  if i < l: # should be L
    if c == "M":
      repo[1] += 1
    elif c == "S":
      repo[3] += 1
  elif i < l + m: # should be M
    if c == "L":
      repo[0] += 1
    elif c == "S":
      repo[5] += 1
  else: # should be S
    if c == "L":
      repo[2] += 1
    elif c == "M":
      repo[4] += 1
p1 = min(repo[0], repo[1])
p2 = min(repo[2], repo[3])
p3 = min(repo[4], repo[5])
p = p1 + p2 + p3
total = sum(repo)
remain = total - p * 2
r = remain * 2 // 3
print(p+r)