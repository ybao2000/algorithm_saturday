# Tandem Bicycle

qt = int(input())
N = int(input())
ds = [int(val) for val in input().split()]
ps = [int(val) for val in input().split()]

ds.sort()
ps.sort()

sum = 0
if qt == 1: # min speed
  for i in range(N):
    speed = max(ds[i], ps[i])
    sum += speed
else: #max speed
  for i in range(N):
    speed = max(ds[i], ps[N-1-i])
    sum += speed

print(sum)