# C. Sagheer and Nubian Market

vals = input().split()
n = int(vals[0])
S = int(vals[1])
a = [int(v) for v in input().split()] # list comprehension

left = 0
right = n - 1
answer1 = 0 # number of items you are buying
answer2 = 0 # minimum cost of the buying

while left <= right:
  mid = (left + right) // 2 # two slashes means round down

  # c = []
  # for i in range(n):
  #   c.append(a[i] + (i+1) * (mid + 1))
  c = [x + (index+1) * (mid+1) for index, x in enumerate(a)]
  c.sort()
  min_sum = 0
  for i in range(mid + 1):
    min_sum += c[i]
  if min_sum <= S:
    answer1 = mid + 1
    answer2 = min_sum
    left = mid + 1
  else:
    right = mid - 1

print(answer1, answer2)
