# B. Trouble Sort
t = int(input())
for i in range(t):
  n = int(input())
  a = [int(val) for val in input().split()]
  b = [int(val) for val in input().split()]
  # if a is sorted, then "Yes"
  # otherwise, check if b is same type
  # how to check if it's sorted or not
  isSorted = True
  # how to check if same type
  isSameType = True
  for j in range(1, n):
    if a[j] < a[j-1]:
      isSorted = False
    if b[j] != b[j-1]:
      isSameType = False

  if isSorted or not isSameType:
    print("Yes")
  else:
    print("No")



