s = "funny cat garfield   Dressed   As Easter Bunny"

# l = s.split() # split the sentence into word list
# print(l)

# # I want something like Funny-Cat-Garfield-Dressed-As-Easter-Bunny
# s2 = '***'.join(l)
# print(s2)

# phone = '587 224  5555'
# # '587-224-5555'
# phone2 = '-'.join(phone.split())
# print(phone2)
# # phone2 = phone.replace(' ', '-')
# # print(phone2)

# string is immutable, list is mutable
# now I want "FCGDADE"
# l2 = [] # empty list
# for word in l: # go through all words one by one
#   l2.append(word[0])  # find the first letter, and add them into the list

# s2 = ''.join(l2) # glue all items in the list, 
# print(s2)

# use list comprehesion
print(''.join([word[0].upper() for word in s.split()]))
