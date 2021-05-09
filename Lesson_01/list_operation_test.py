l = [3, 3, 2, 4, 4, 5, 2, 1]
#    0, 1, 2, 3, 4, 5, 6

# insert
# l.append(0)     # if you only want to insert at the end, please use append
# l.insert(2, 100) # insert is expensive, append is cheap
# print(l)

# delete
# delete based on index
# val = l.pop() # remove the last
# val = l.pop(3)
# print(l, val)
# delete based on value
# l.remove(2)
# print(l)

max_num = max(l)
min_num = min(l)
sum_num = sum(l)
print(max_num, min_num, sum_num)