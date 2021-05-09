# F. Swapping Problem

n = int(input())
a = [int(val) for val in input().split()]
b = [int(val) for val in input().split()]

# step 1, partition it
s = []
t = []
for i in range(n):
  if a[i] < b[i]:
    # we are going to use tuple (left, right) for interval
    s.append((a[i], b[i]))
  elif a[i] > b[i]:
    t.append((b[i], a[i]))

# step 2, sort s and t
s.sort()  # by default, python sort tuple according to first value
t.sort()

# step 3, get rid of the embedded intervals
x = []
j = 0
for i in range(len(s)):
  # need to make sure j is the last element of x
  if i > 0 and s[i][1] < x[j-1][1]:
    # you should ignore this interval
    continue
  x.append(s[i])
  j += 1
y = []
j = 0
for i in range(len(t)):
  if i > 0 and t[i][1] < y[j-1][1]:
    continue
  y.append(t[i])
  j += 1

def get_overlap(t1, t2):
  return max(min(t1[1], t2[1])-max(t1[0], t2[0]), 0)

# step 4, go through the list to find the max overlap
i = 0
j = 0
overlap_max = 0
for i in range(len(x)):
  # you should stop if y[j].right > x[i].right
  while j < len(y) and y[j][1] <= x[i][1]: 
    overlap = get_overlap(x[i], y[j])
    if overlap > overlap_max:
      overlap_max = overlap
    j += 1
  # because you exit too early when reach the condition that j.right > i.right
  if j < len(y):
    overlap = get_overlap(x[i], y[j])
    if overlap > overlap_max:
      overlap_max = overlap  

# step 5, print the answer
dist = 0
for i in range(n):
  dist += abs(a[i]-b[i])
dist -= 2 * overlap_max
print(dist)
