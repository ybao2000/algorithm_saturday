# Books Exchange (easy version)

q = int(input())
queries = []
for i in range(q):
  n = int(input())
  items = input().split()
  p = [int(item) for item in items] # list comprehension => convert str to int
  queries.append(p)

for query in queries:
  # group way -- means, you don't think, just follow whatever they want
  n = len(query)
  results = [None] * n  # initialize the result with None  
  for i in range(n): # i = 0, 1st student, 1, second, 
    if results[i] is None:
      # we are going to use a set to store all intermidate permutations
      group = {i}   
      nxt = query[i] - 1   # because in p, 1 means first, which should be 0 in code
      count = 1
      while nxt != i:
        group.add(nxt)
        nxt = query[nxt] - 1
        count += 1
      for member in group:
        results[member] = str(count)
  print(' '.join(results))  # this is to pring the numbers in the list
