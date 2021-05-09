def max_array(a):
  # # just loop through the array to find the max
  # max_a = None
  # for item in a:
  #   if max_a is None or item > max_a:
  #     max_a = item
  # return max_a
  # what about using divide and conquer
  l = len(a)
  if l == 1:
    return a[0]
  mid = len(a)//2
  left = a[:mid]
  right = a[mid:]
  max1 = max_array(left)
  max2 = max_array(right)
  return max(max1, max2)

  
import  random
a = []
for i in range(10):
  a.append(random.randint(1, 1000))

print(a)
print(max_array(a))