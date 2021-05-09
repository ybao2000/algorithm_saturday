# 'A' -> 1
# 'B' -> 2
#A, B, C, D, E, F
# 'Z' -> 26

# ord(), and chr() functions
# c = 'A'
def charToNum(c):
  return ord(c)-ord('A')+1

# print(charToNum(c))

d =26
def numToChar(d):
  return chr(ord('A')+d-1)

print(numToChar(d))
