import random
import time

def bubble_sort(numbers):
  for i in range(N-1):  # these are the rounds
    for j in range(N-1-i):
      # we are going to compare [j] with [j+1]
      if numbers[j] > numbers[j+1]:
        # they are not in order, then flip it
        # temp = numbers[j]
        # numbers[j]  = numbers[j+1]
        # numbers[j+1] = temp
        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]


N = 10000
# we are going to create a list of random numbers
# numbers = []
# for i in range(N):
#   numbers.append(random.randint(0, N))
numbers = [random.randint(0, N) for _ in range(N)]  # sometimes if we don't care about the varaible, we can use _
# print(numbers)
time_start = time.time()
bubble_sort(numbers)
time_end = time.time()
# print(numbers)
print(f"time (sec) spent: {time_end-time_start}")

