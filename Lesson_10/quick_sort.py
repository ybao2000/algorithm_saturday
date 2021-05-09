import random
import time

def quick_sort(numbers):
  # we are going to select the last element as pivot
  l = len(numbers)
  if l <= 1:  # base case
    return numbers
  # the reason we choose the last one is because 
  # pop for last element is very quick
  pivot = numbers.pop()
  group_1 = []
  group_2 = []
  for number in numbers:
    if number <= pivot:
      group_1.append(number)
    else:
      group_2.append(number)
  # we just merge all sub arrays
  return quick_sort(group_1) + [pivot] + quick_sort(group_2)

N = 100000
# we are going to create a list of random numbers
# numbers = []
# for i in range(N):
#   numbers.append(random.randint(0, N))
numbers = [random.randint(0, N) for _ in range(N)]  # sometimes if we don't care about the varaible, we can use _
# print(numbers)
time_start = time.time()
numbers = quick_sort(numbers)
time_end = time.time()
# print(numbers)
print(f"time (sec) spent: {time_end-time_start}")
