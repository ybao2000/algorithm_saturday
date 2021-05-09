t = int(input())
results = []
for i in range(t):
  n = int(input())
  vals = input().split()
  S = {int(val) for val in vals}  # this is to convert list into set, and element is in integer

  for k in range(1, 1024): # stop at 1023
    S2 = set()
    hasDup = False
    for s in S:
      x = s ^ k
      if x in S2:
        hasDup = True
        break
      else:
        S2.add(x)
    if not hasDup and S == S2:   # check if 2 sets are the same
      # you got the answer
      results.append(k)
      break
  else:
    results.append(-1)

for result in results:
  print(result)