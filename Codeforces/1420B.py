results = []
t = int(input())
for k in range(t):
  n = int(input())
  vals = input().split()
  A = [int(val) for val in vals]

  l = len(A)
  # try brute force
  count = 0
  for i in range(l):
    for j in range(i+1, l):
      if A[i] & A[j] >= A[i] ^ A[j]:
        count += 1
  
  results.append(count)

for result in results:
  print(result)