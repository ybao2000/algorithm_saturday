vals = input().split()  # standard input and split it into items
ivals = [int(val) for val in vals]  # using list comprehesion to convert items into numbers

def get_type(a, b, c):
  longest = max(a, b, c)
  others = a + b + c - longest
  if others > longest:
    return 2  # can make triangle
  elif others == longest:
    return 1  # cna make segment
  else:
    return 0  # impossible

# a, b, c, d
# a, b, c (missing d)
# a, b, d (missing c)
# a, c, d (missing b)
# b, c, d (missing a)

final_tp = 0  # initialize the final type to be impossible
for i in range(4):
  tp = get_type(ivals[i], ivals[(i+1)%4], ivals[(i+2)%4])  # getting the remainder in order to reset to the start if it's out of index
  # if tp == 2: # if tp is 2, means you already find a triangle, no need to loop
  #   final_tp = tp
  #   break
  # elif tp > final_tp: # otherwise, you have to update the final_tp, 
  #   final_tp = tp
  if tp > final_tp:
    final_tp = tp
    if final_tp == 2:
      break

if final_tp == 2:
  print("TRIANGLE")
elif final_tp == 1:
  print("SEGMENT")
else:
  print("IMPOSSIBLE")


