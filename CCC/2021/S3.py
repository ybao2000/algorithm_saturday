# CCC '21 S3 - Lunch Concert
N = int(input())

P = []
W = []
D = []
for i in range(N):
  vals = input().split()
  P.append(int(vals[0]))
  W.append(int(vals[1]))
  D.append(int(vals[2]))

def getTime(p):
  t = 0
  for i in range(N):
    diff = abs(P[i]-p)
    if diff > D[i]:
      t += (diff-D[i]) * W[i]
  return t

# we are going to use binary search to find the minimum
if N == 1:
  print(0)
else:
  p_left = min(P)
  p_right = max(P)
  while p_left <= p_right:
    p_mid = (p_left + p_right)//2
    t_mid = getTime(p_mid)
    t_mid_prev = getTime(p_mid-1)
    if t_mid > t_mid_prev:
      p_right = p_mid - 1
    elif t_mid == t_mid_prev:
      ans = t_mid
      break
    else:
      t_mid_next = getTime(p_mid+1)
      if t_mid_next >= t_mid:
        ans = t_mid
        break
      else:
        p_left = p_mid + 1

  print(ans)

