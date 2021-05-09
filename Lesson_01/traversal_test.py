# import random
# l = []  # empty list
# for i in range(20):  # for loops, i from 0, 99
#   l.append(random.randint(1, 100))  # add a random integer [1, 100] into l (append, always add at the end)

# l = ["apple", "banana", "cherry", "durian", "efruit"]
# for example, I want to double the list items
# print("original", l)
# for i in range(len(l)):
#   l[i] = l[i] * 2;

# list comprehension
# for item in l:
#   print(item)
# l = [item + 1 for item in l] 
# print("increase by 1", l)


# i want even numbers
# evenl = []
# for item in l:
#   if item % 2 == 0:
#     evenl.append(item)
# print("even l", evenl)
# list comprehesion (only for python)
# evenl = [item for item in l if item % 2 == 0]
# print(evenl)

l = [3, 3, 2, 4, 4, 5, 1]
#      0, 1, 2, 3, 4, 5, 6
l.append(0)     # if you only want to insert at the end, please use append
l.insert(2, 100) # insert is expensive, append is cheap
print(l)