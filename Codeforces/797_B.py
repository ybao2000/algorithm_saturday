# B. Odd sum
n = int(input())
vals = input().split()
list_a = [int(val) for val in vals]

# we use max_even, max_odd for the answer
max_even = None
max_odd = None

# 0, 2, 4, 6, ...., 1000, -1 # this case means you won't get max_odd until you reach -1
# 1, 3 => even

for a in list_a:
  # before I can max_even, max_odd, I save them first
  me = max_even
  mo = max_odd
  if a % 2 == 0: # even
    if mo is not None:
      max_odd = max(mo, mo+a)
    if me is None:
      max_even = a
    else:
      max_even = max(me, a, me+a)
  else: # odd
    if me is None and mo is None:
      max_odd = a
    elif me is None: # mo is not None
      max_odd = max(mo, a)
      max_even = mo + a
    elif mo is None:
      max_odd = max(a, me+a)
    else: # me is not None, mo is not None
      max_odd = max(mo, a, me+a)
      max_even = max(me, mo+a)

print(max_odd)

