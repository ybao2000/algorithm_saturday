import random
import time

def insertion_sort(numbers):
  for i in range(1, N):
    # we assume 0...i-1 already sorted
    # we need to find a position to put the element of i
    number = numbers[i]
    j = i - 1 # starting from the end of the sorted
    while j >= 0 and numbers[j] > number:
      numbers[j+1] = numbers[j] # you have to move all larger numbers to next
      j -= 1
    numbers[j+1] = number

N = 10000
# we are going to create a list of random numbers
# numbers = []
# for i in range(N):
#   numbers.append(random.randint(0, N))
numbers = [random.randint(0, N) for _ in range(N)]  # sometimes if we don't care about the varaible, we can use _
# print(numbers)
time_start = time.time()
insertion_sort(numbers)
time_end = time.time()
# print(numbers)
print(f"time (sec) spent: {time_end-time_start}")
