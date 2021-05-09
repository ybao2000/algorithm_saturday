def BinarySearch(a, x):
  left = 0
  right = len(a)
  while left < right:
    middle = (left + right) // 2
    if a[middle] <= x:
      left = middle + 1
    else:
      right = middle
  
  if left > 0 and a[left-1] == x:
    return True
  else:
    return False

a  = [6, 12, 14, 14, 17, 29, 33, 40, 47, 50, 59, 61, 66, 67, 74, 83, 85, 87, 88, 89]
x = 90
print(BinarySearch(a, x))  