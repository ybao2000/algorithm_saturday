import time
def gcd(num1, num2):
  # euclidean algorithm
  m = max(num1, num2)
  n = min(num1, num2)
  r = m % n
  while r != 0:
    m, n = n, r # this is a quick way to swap 2 numbers
    r = m % n
  return n

# print(gcd_euclidean(1522332321, 63332322))
start = time.time()
result = gcd(123456782020202932, 9876540202322)
end = time.time()
print("result:", result, "runtime:", end-start)