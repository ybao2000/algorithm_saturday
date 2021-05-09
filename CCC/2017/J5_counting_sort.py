N = int(input())
vals = input().split(" ")

repo = [0]*2001
lengths = [0]*4001

for val in vals:
    repo[int(val)] += 1

for i in range(0, len(repo) - 1):
    for j in range(i, len(repo)):
        if i == j:
            lengths[i + j] += repo[i] // 2
        else:
            lengths[i + j] += min(repo[i], repo[j])

max_length, ways = 0, 0

for length in lengths:
    if length > max_length:
        max_length = length
        ways = 1
    elif length == max_length:
        ways += 1

print(max_length, ways)