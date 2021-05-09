import random
import time

def selection_sort(numbers):
  for i in range(N-1):  # these are the rounds
    index_min = i
    # for each round, find the index of the min
    for j in range(i+1, N):
      if numbers[j] < numbers[index_min]:
        index_min = j
    #swap
    numbers[i], numbers[index_min] = numbers[index_min], numbers[i]


N = 10000
# we are going to create a list of random numbers
# numbers = []
# for i in range(N):
#   numbers.append(random.randint(0, N))
numbers = [random.randint(0, N) for _ in range(N)]  # sometimes if we don't care about the varaible, we can use _
# print(numbers)
time_start = time.time()
selection_sort(numbers)
time_end = time.time()
# print(numbers)
print(f"time (sec) spent: {time_end-time_start}")
