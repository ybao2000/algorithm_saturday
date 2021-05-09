import random

n = 20
a = []
for i in range(n):
  a.append(random.randint(-100, 100))
# a = [40, 74, 49, -42, -98, -31, 58, 33, -56, 67, 12, 12, -73, -69, 38, -91, -80, -93, 32, -53]
a = [-72, -93, 76, -70, -66, 57, -75, 47, 7, -12, 90, -63, 83, 63, -48, -79, -80, -37, 93, -59]
print(a)

# second method: divide and conquer (recusively)
def cross_sub_sum(a, left, right, mid):
  # find the maximum sum of left half starting with mid
  left_sum_max = a[mid]
  left_sum = a[mid]
  left_index = mid
  for i in range(mid-1, left-1, -1):  # starting with mid-1, stop at left-1 (left is included)
    left_sum += a[i]
    if left_sum > left_sum_max:
      left_sum_max = left_sum
      left_index = i
  # do the same thing for the right half, starting with mid+1
  right_sum_max = a[mid+1]
  right_sum = a[mid+1]
  right_index = mid
  for i in range(mid+2, right+1): # starting with mid+2, stop at right+1 (right is include)
    right_sum += a[i]
    if right_sum > right_sum_max:
      right_sum_max = right_sum
      right_index = i
  return left_sum_max + right_sum_max, left_index, right_index

def max_sub_sum(a, left, right):  # left and right are the index of a
  # base case: left == right
  if left == right:
    return a[left], left, right
  
  mid = (left+right)//2
  L, l_1, r_1 = max_sub_sum(a, left,  mid)  # sub problem of [left, mid]
  R, l_2, r_2 = max_sub_sum(a, mid+1, right)
  # we have to deal with the crossing case
  C, l_3, r_3 = cross_sub_sum(a, left, right, mid)
  if L > R and L > C:
    return L, l_1, r_1
  elif R > L and R > C:
    return R, l_2, r_2
  else:
    return C, l_3, r_3


print(max_sub_sum(a, 0, len(a)-1))