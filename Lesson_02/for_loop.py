num = int(input())

for i in range(num, -1, -1):  # starting from num, ending at -1 (-1 is excluded), increment (default is 1)
  if i == 3:
    continue
  print(i)
