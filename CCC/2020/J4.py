# Problem J4: Cyclic Shifts
T = input()
S = input()

for i in range(len(S)):
# we are going to shift S
  if S in T:
    print("yes")
    break
  # how to shift S?
  S = S[1:] + S[0]  # cutoff the first letter and put it in the end
else:
  print("no")