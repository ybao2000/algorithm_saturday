M = int(input())
N = int(input())
P = int(input())
row_ops = set()
col_ops = set()
for i in range(P):
  vals = input().split()
  op = vals[0]
  num = int(vals[1])-1  # offset
  if op == "R":
    if num in row_ops:
      row_ops.remove(num)
    else:
      row_ops.add(num)
  else:
    if num in col_ops:
      col_ops.remove(num)
    else:
      col_ops.add(num)

nr = len(row_ops)
nc = len(col_ops)
count = nr * N + nc * M - 2 * nr * nc
print(count)
