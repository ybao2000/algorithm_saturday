# A. Two Substrings
def isValid(i):
  c1 = s[i]
  c2 = s[i-1]
  c3 = s[i-2]
  # assign it first, 
  dp_AB[i] = dp_AB[i-1] 
  dp_BA[i] = dp_BA[i-1]
  if c1 == "A":
    if c2 == "B":
      if c3 == "A":
        if dp_AB[i-3] or dp_BA[i-3]:
          return True
        else:
          dp_AB[i], dp_BA[i] = True, True
      else:
        if dp_AB[i-2]:
          return True
        else:
          dp_BA[i] = True
  elif c1 == "B":
    if c2 == "A":
      if c3 == "B":
        if dp_AB[i-3] or dp_BA[i-3]:
          return True
        else:
          dp_AB[i], dp_BA[i] = True, True
      else:
        if dp_BA[i-2]:
          return True
        else:
          dp_AB[i] = True      
  return False
  
s = input()
if len(s) < 4:
  print("NO")
elif len(s) == 4:
  if s == "ABBA" or s == "BAAB":
    print("YES")
  else:
    print("NO")
else:
  dp_AB = [False] * len(s)
  dp_BA = [False] * len(s)
  # initialize dp up to 4
  for i in range(1, 4):   
    dp_AB[i] = "AB" in s[:i+1] # to check if AB is in the substring
    dp_BA[i] = "BA" in s[:i+1]
  for i in range(4, len(s)):  # this goes with dp
    if(isValid(i)):
        print("YES")
        break
  else:
    print("NO")
    
