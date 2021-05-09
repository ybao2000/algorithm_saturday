A = {1, "apple", "apple"}
# print(A)
# set has no index

B = {2, 3, 4}
# C = {frozenset(A), frozenset(B)} # in python, set memeber should be unmutable, but set is mutable
# print(C)

# tuple ()
# list []
# dict {}
# set ???? we don't have other kinds of brackets, so we have to borrow {} for set
# set why not use <>???
# be care about empty set (very useful, because set is mutable!!!)
# C = set() # this is the way to make empty set, don't use {}
# C.add(1)
# C.add(2)
# print(C)

print(2 in B)
print(4 not in B)