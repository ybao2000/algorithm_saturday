a = [6, 12, 14, 14, 17, 29, 33, 40, 47, 50, 59, 61, 66, 67, 74, 83, 85, 87, 88, 89]
target = 61

def bs(left, right, target):
  if left > right:   # base case
    return -1
  else:
    mid = (left+right)//2
    if a[mid] == target:
      return mid
    elif a[mid] > target:
      return bs(left, mid-1, target)
    else:
      return bs(mid+1, right, target)
  
ans = bs(0, len(a)-1, target)
print(ans)