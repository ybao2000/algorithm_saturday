# B. Optimal Point on a Line
n = int(input())
x = [int(val) for val in input().split()]

def dist(p):
  d = 0
  for i in range(n):
    d += abs(x[i]-p)
  return d

# we are going to use binary search to find the minimum
p_left = min(x)
p_right = max(x)
while p_left <= p_right:
  p_mid = (p_left + p_right)//2
  t_mid = dist(p_mid)
  t_mid_prev = dist(p_mid-1)
  if t_mid >= t_mid_prev:
    p_right = p_mid - 1
  else:
    t_mid_next = dist(p_mid+1)
    if t_mid <= t_mid_next: # you find the result
      ans = p_mid
      break
    else:
      p_left = p_mid + 1

print(ans)
