import random

# num_list = []
# for i in range(20):
#   num_list.append(random.randint(-100, 100))

# print(num_list)
num_list = [87, 100, -60, -62, -54, -45, 77, -2, 55, 87, 19, 34, 22, -61, -10, -44, 30, -31, -72, 64]

# find the sub list which has max sum
# These 2 problems are exactly the same!!!
max_sum = 0
cur_sum = 0
max_start = 0
cur_start = 0
for i in range(len(num_list)):
  num = num_list[i]
  if cur_sum + num < 0:
    cur_sum = 0
    cur_start = i + 1
  else:
    cur_sum += num
    if cur_sum > max_sum:
      max_sum = cur_sum
      max_start = cur_start
      max_end = i
print(f"{max_sum}, {num_list[max_start]}({max_start}), {num_list[max_end]}({max_end})");
