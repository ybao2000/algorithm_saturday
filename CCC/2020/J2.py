P = int(input())
N = int(input())
R = int(input())

day = 0  # day starts from 0, everytime increase by 1
t = N # t is total people infected at day
p = N # p is the infected people at day
# 1 person only infect 1 person
while t <= P:
  day += 1
  p = p * R
  t += p

print(day)
