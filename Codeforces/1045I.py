N = int(input())
list_str = []
for i in range(N):
  list_str.append(input())

def isPalindrom(s1, s2):
  dict_c = {}
  for c in s1:
    if c in dict_c:
      dict_c[c] += 1
    else: 
      dict_c[c] = 1
  for c in s2:
    if c in dict_c:
      dict_c[c] += 1
    else: 
      dict_c[c] = 1 
  icount = 0
  for v in dict_c.values():
    if v % 2 == 1:  # count the odd
      icount += 1
  if icount > 1:  # if number or odd > 1
    return False
  else:
    return True

count = 0
for i in range(N):
  s1 = list_str[i]
  for j in range(i+1, N):
    s2 = list_str[j]
    if isPalindrom(s1, s2):
      count += 1

print(count)