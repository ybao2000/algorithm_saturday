# Books Exchange (easy version)
 
q = int(input())
queries = []
for i in range(q):
  n = int(input())
  items = input().split()
  p = [int(item) for item in items] # list comprehension => convert str to int
  queries.append(p)
 
for query in queries:
  # brute force -- means, you don't think, just follow whatever they want
  n = len(query)
  results = []  
  for i in range(n): # i = 0, 1st student, 1, second, 
    nxt = query[i] - 1   # because in p, 1 means first, which should be 0 in code
    count = 1
    while nxt != i:
      nxt = query[nxt] - 1
      count += 1
    results.append(str(count)) # we calculate the number for each kid, and put the num in the results
  print(' '.join(results))  # this is to pring the numbers in the list