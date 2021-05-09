# C. Everyone is a Winner!
t = int(input())
for i in range(t):
  n = int(input())
  answers = set()
  answers.add(n)
  x = 1
  while x <= n//2+1:
    target = n // x    
    left = x
    right = (n+1)//target + 1
    ans = x
    while left <= right:
      mid = (left + right)//2
      if n // mid == target:
        ans = mid        
        left = mid + 1
      else:
        right = mid - 1
    x = ans + 1        
    answers.add(n//x)
  answers.add(1)
  answers.add(0)

  # sys.stdout.writeline(str(len(answers)))
  # sys.stdout.write(' '.join([str(a) for a in sorted(answers)]))
  print(len(answers))
  print(' '.join([str(a) for a in sorted(answers)]))
  