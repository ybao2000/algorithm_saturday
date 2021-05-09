def gcd(num1, num2):
  # euclidean algorithm
  m = max(num1, num2)
  n = min(num1, num2)
  r = m % n
  while r != 0:
    m, n = n, r # this is a quick way to swap 2 numbers
    r = m % n
  return n

def lcm(num1, num2):
  return num1 * num2 // gcd(num1, num2)

print(lcm(123456789, 987654321))
