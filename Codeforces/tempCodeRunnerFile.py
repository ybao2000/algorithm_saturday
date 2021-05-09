# B. Optimal Point on a Line
n = int(input())
x = [int(val) for val in input().split()]

x.sort()

print(x[n//2])
