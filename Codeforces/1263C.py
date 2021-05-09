# C. Everyone is a Winner!
import math

t = int(input())
for i in range(t):
  n = int(input())
  answers = set() # initialize an empty set
  answers.add(0)  # add 0
  for i in range(1, int(math.sqrt(n))+1): # loop from 1 to sqrt(n)
    answers.add(i)  
    answers.add(n//i)
  print(len(answers))
  print(' '.join([str(a) for a in sorted(answers)]))
  #print(*sorted(answers))
