x = int(input())
b = bin(x)
count = 0
for ch in b[2:]:
  if ch == '1':
    count += 1
print(count)

