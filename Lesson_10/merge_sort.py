import random
import time

def merge_sort(numbers):
  if len(numbers) > 1:
    # use divide and conquer
    # step 1: split first
    mid = len(numbers)//2
    left_half = numbers[:mid] # mid is excluded, left_half is a new list
    right_half = numbers[mid:]  # start with mid, right_half is also a new list
    # step 2: for each smaller problem, call the recursive function
    merge_sort(left_half)
    merge_sort(right_half)
    # step 3: you need to merge it
    i, j, k = 0, 0, 0
    # repeat until any half reaches the end
    while i<len(left_half) and j <len(right_half):
      if (left_half[i] <= right_half[j]):
        numbers[k] = left_half[i]
        i += 1
      else:
        numbers[k] = right_half[j]
        j += 1
      k += 1  # because k has to increase
    # we have to append all remaining to the end of numbers
    while i < len(left_half):
      numbers[k] = left_half[i]
      i += 1
      k += 1
    while j < len(right_half):
      numbers[k] = right_half[j]
      j += 1
      k += 1    

N = 8
# we are going to create a list of random numbers
# numbers = []
# for i in range(N):
#   numbers.append(random.randint(0, N))
numbers = [random.randint(0, N) for _ in range(N)]  # sometimes if we don't care about the varaible, we can use _
# print(numbers)
time_start = time.time()
merge_sort(numbers)
time_end = time.time()
# print(numbers)
print(f"time (sec) spent: {time_end-time_start}")
