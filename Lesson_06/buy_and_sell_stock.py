import random

stocks = []
for i in range(100):
  stocks.append(random.randint(0, 1000))
#stocks = [60, 99, 73, 98, 97, 2, 10, 92, 44, 38, 53, 38, 19, 39, 45, 64, 97, 70, 58, 54]
print(*stocks)

# trick 1 - find the difference,
diffs = []
l = len(stocks)
for i in range(l-1):
  diffs.append(stocks[i+1] - stocks[i])
# diffs = [39, -26, 25, -1, -95, 8, 82, -48, -6, 15, -15, -19, 20, 6, 19, 33, -27, -12, -4]

max_profit = 0
cur_profit = 0
for diff in diffs:
  if cur_profit + diff < 0: # trick 2 - if cur_profit is negative, no meaning to keep, so just reset it
    cur_profit = 0
  else:
    cur_profit += diff
    if cur_profit > max_profit:
      max_profit = cur_profit
print(max_profit)