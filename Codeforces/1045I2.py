N = int(input())
# first, let's do the string way
repo = {}
total_count = 0
for i in range(N):
  val = input()
  vec = ['0'] * 26  # a list of 26, initialized with 0
  for c in val:
    # find the index
    index = ord(c)-ord('a')
    if vec[index] == '0':
      vec[index] = '1'
    else:
      vec[index] = '0'
  # we glue all 0's and 1's together
  s = ''.join(vec)
  if s in repo:
    total_count += repo[s]  # we handled paired
  # we need to handle one non-pair
  for j in range(26):
    vec2 = vec[:] # we copy the original vec
    if vec2[j] == '0':
      vec2[j] = '1'
    else:
      vec2[j] = '0'
    s2 = ''.join(vec2)
    if s2 in repo:
      total_count += repo[s2]
  # finally, don't forget to put your s in the repo
  if s in repo:
    repo[s] += 1
  else:
    repo[s] = 1

print(total_count)
