# input
line = input()
items = line.split()
n = int(items[0])
m = int(items[1])
a = int(items[2])

# your calculation
import math
# find the minimum of the flagstones
count = math.ceil(n/a) * math.ceil(m/a)

# output
print(count)