num = int(input())

# try:
while num >= 0: # while use condition, if condition not satisfied, go to else if there is else
  print(num)
  num -= 1
  if num == 3:
    #break
    raise Exception("my exception")
else:
  print("negative num:", num)
# except:
#   print("except")

print("Done")