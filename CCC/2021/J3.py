# Secret Instructions
val = input()
direction = None
while val != '99999':
  s1 = val[:2]  # get the first 2 digits
  s2 = val[2:]  # get the digits starting from index of 2
  sum = 0
  for c in s1:  # this is to loop through the string of s1
    sum += int(c)
  if sum > 0:  
    if sum % 2 == 0:
      direction = 'right'
    else:
      direction = 'left'

  print(direction, s2)
  val = input()