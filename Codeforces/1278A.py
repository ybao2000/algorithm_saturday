# A. Shuffle Hashing
def isShuffle(a, b):
  dict_a = {}
  dict_b = {}
  # just collect the occurence for each character in string
  for c in a:
    if c in dict_a: # if found, just increase the occurence
      dict_a[c] += 1
    else: # if not found, this is the first time the character occurs
      dict_a[c] = 1
  for c in b:
    if c in dict_b:
      dict_b[c] += 1
    else:
      dict_b[c] = 1
  return dict_a == dict_b

t = int(input())
for i in range(t):
  p = input()
  h = input()
  len_p = len(p)
  len_h = len(h)
  if len_h < len_p:
    print('NO')
  else:
    i = 0
    while i + len_p <= len_h:
      if isShuffle(h[i:i+len_p], p):
        print("YES")
        break
      i += 1
    else:
      print("NO")


