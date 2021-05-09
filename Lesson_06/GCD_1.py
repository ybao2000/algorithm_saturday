# given two positive integers, find the greatest common divisor
def gcd(num1, num2):
  # brute force -- simplest, iterate one by one from highest to 1
  num_min = min(num1, num2)
  for i in range(num_min, 0, -1): # starting from num_min, end at 1, everytime decrease by 1
    if num1 % i == 0 and num2 % i == 0:
      return i

# print(gcd(1522332321, 63332322))
print(gcd(30, 12))