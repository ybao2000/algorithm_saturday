# this one is to sum up from 1 to the number you entered
# 1 + 2 + 3 + 4 + 5 + ... + num

import time
num = int(input("Input a positive number: "))
sum = 0 # init
start = time.time()
for i in range(1, num+1):
  sum += i

end = time.time()

print(f"sum is {sum}, used time (in sec) is {end-start}")

# observation
# up until 1000,000, very quick
# for 1,000,000, it takes about 0.23 sec
# for 10, 000, 000, it takes about 2.1 sec
# for 100, 000, 000, it takes about 26 sec