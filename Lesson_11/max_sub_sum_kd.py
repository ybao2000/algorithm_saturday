import random

n = 20
a = []
for i in range(n):
  a.append(random.randint(-100, 100))
# a = [40, 74, 49, -42, -98, -31, 58, 33, -56, 67, 12, 12, -73, -69, 38, -91, -80, -93, 32, -53]
a = [-72, -93, 76, -70, -66, 57, -75, 47, 7, -12, 90, -63, 83, 63, -48, -79, -80, -37, 93, -59]
print(a)

# third method: Kadane's algorithm
def max_sub_sum(a):
  best_sum = 0
  current_sum = 0
  # we only need to iterate through the whole list
  for i, x in enumerate(a): # enumerate can provide both index and value
    if current_sum <= 0:  # you need to reset your current sum if the current sum is non-positive
      current_start = i
      current_sum = x
    else:
      current_sum += x
    
    if current_sum > best_sum:
      best_sum = current_sum
      best_start = current_start
      best_end = i

  return best_sum , best_start, best_end

print(max_sub_sum(a))