N = int(input())
# first, let's do the bit way
repo = {}
total_count = 0
for i in range(N):
  val = input()
  num = 0
  for c in val:
    index = ord(c)-ord('a')
    num ^= (1<<index)
  if num in repo:
    total_count += repo[num]
  for j in range(26):
    num2 = num ^ (1<<j)
    if num2 in repo:
      total_count += repo[num2]

  if num in repo:
    repo[num] += 1
  else:
    repo[num] = 1
  
print(total_count)
