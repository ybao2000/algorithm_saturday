#read from input
S = int(input())
M = int(input())
L = int(input())

# doing your calculation here
score = S + 2 * M + 3 * L

# output
if score < 10:
  print("sad")
else:
  print("happy")
