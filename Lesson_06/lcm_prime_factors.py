import math
import time
def prime_factors(a):
  # find prime factors for any number
  pfs = {}
  s = int(math.sqrt(a)) + 1
  for i in range(2, s):
    ic = 0 # this is a count
    while a % i == 0:
      a //= i
      ic += 1
    if ic > 0:
      pfs[i] = ic
    if i > a:
      break
  if a > 1:
      pfs[a] = 1
  return pfs

def lcm(num1, num2):
  pfs_1 = prime_factors(num1)
  pfs_2 = prime_factors(num2) 
  # we just join the 2 dictionaries together, and
  # put the merged on in pfs_1
  for k, v2 in pfs_2.items():
    if k in pfs_1:
      v1 = pfs_1[k]
      pfs_1[k] = max(v1, v2)
    else:
      pfs_1[k] = v2

  result = 1      
  for k, v in pfs_1.items():
    result *= k ** v
  return result

start = time.time()
result = lcm(123456789, 987654321)
end = time.time()
print("result:", result, "runtime:", end-start)