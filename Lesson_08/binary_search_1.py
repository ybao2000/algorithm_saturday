# import random
# a = []
# for i in range(20):
#   a.append(random.randint(1, 100))

# a.sort()
# print(a)
a  = [6, 12, 14, 14, 17, 29, 33, 40, 47, 50, 59, 61, 66, 67, 74, 83, 85, 87, 88, 89]
target = 84
# implement the binary search is also very tricky
# using index instead of the element itself
left = 0
right = len(a)-1
ans = -1
while left <= right:  # iterate until left > right
  mid = (left+right)//2  # this one has the potential of overflow
  # mid = left + (right-left)//2 # for python, doesn't matter
  if a[mid] == target:
    ans = mid
    break
  elif a[mid] > target:
    right = mid - 1
  else: 
    left = mid + 1
print(ans)
