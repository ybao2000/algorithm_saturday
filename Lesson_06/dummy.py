stocks = [60, 99, 73, 98, 97, 2, 10, 92, 44, 38, 53, 38, 19, 39, 45, 64, 97, 70, 58, 54]

# how to find the diffs

diffs = []
l = len(stocks)
for i in range(l-1):
  diffs.append(stocks[i+1] - stocks[i])

print(diffs)