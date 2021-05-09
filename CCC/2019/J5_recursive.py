rules = []
rules.append(input().split())
rules.append(input().split())
rules.append(input().split())

vals = input().split()
S = int(vals[0])
I = vals[1]
F = vals[2]

# visited = [set()] * S # this doens't work!!!
# [{'BB', 'AAA'}, {'AAB', 'BAA', 'ABA'}, ...]
visited = []
for i in range(S):
  visited.append(set())

# we need to return some thing {('BB', '1 1 BB'), {'AAA' '3 2 AAA'}}
def getSubs(s, level):
  subs = set()
  len_s = len(s)
  for irule in range(len(rules)):
    rule = rules[irule]
    i = 0
    r1 = rule[0]
    r2 = rule[1]
    len_r1 = len(r1)
    while i + len_r1 <= len_s:  # loop until the end of s
      if s[i: i+len_r1] == r1:
        t = s[0:i] + r2 + s[i+len_r1:len_s]
        if t not in visited[level]:
          visited[level].add(t)
          subs.add((t, f"{irule+1} {i+1} {t}"))
      i += 1
  return subs

steps = [""] * S  # this is to store the steps
def DFS(seq, level):
  if level == S:  # final step, you din't find it
    return False
  for subSeq, step in getSubs(seq, level):
    steps[level] = step
    if level == S-1:  # last step
      if subSeq == F:
        return True   # you find it
    elif level < S-1:
      if DFS(subSeq, level+1):
        return True
  else:
    return False

if DFS(I, 0):
  for step in steps:
    print(step)
