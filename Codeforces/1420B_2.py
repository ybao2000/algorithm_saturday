results = []
t = int(input())
for k in range(t):
  n = int(input())
  vals = input().split()
  A = [int(val) for val in vals]
  list_count = [0] * 32
  total = 0
  for a in A:
    highest = len(bin(a))-3
    list_count[highest] += 1
  for count in list_count:
    total += count * (count-1)//2
  results.append(total)

for result in results:
  print(result)
