M = int(input())
N = int(input())
P = int(input())
row_ops = [0] * M
col_ops = [0] * N
for i in range(P):
  vals = input().split()
  op = vals[0]
  num = int(vals[1])-1  # offset
  if op == "R":
    row_ops[num] += 1
  else:
    col_ops[num] += 1

nr = len([num for num in row_ops if num % 2 == 1])
nc = len([num for num in col_ops if num % 2 == 1])
count = nr * N + nc * M - 2 * nr * nc
print(count)
