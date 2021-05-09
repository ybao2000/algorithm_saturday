a  = [6, 12, 14, 14, 17, 29, 33, 40, 47, 50, 59, 61, 66, 67, 74, 83, 85, 87, 88, 89]
target = 14

# find the last element that <= target
left = 0
right = len(a)-1
ans = -1
while left <= right:
  mid = (left+right)//2
  if a[mid] <= target:
    ans = mid # update the answer
    left = mid + 1
  else:
    right = mid - 1

print(ans)
if ans >= 0:
  print(a[ans])