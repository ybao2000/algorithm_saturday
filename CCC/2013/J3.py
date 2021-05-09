# From 1987 to 2013
def isValid(y):
  strY = str(y)
  s = set()   
  for ch in strY: 
    if ch in s: 
      return False
    else: 
      s.add(ch)
  return True

Y = int(input())
nextY = Y + 1 
while not isValid(nextY): 
  nextY += 1

print(nextY)

