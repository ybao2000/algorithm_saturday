s = "MSLSLSLMSLSLM"

# some student tried to split the string into list of characters
# please don't do This!!!!!! TOO EXPENSIVE!!!!
t = s.replace("M", "M ").replace("S", "S ").replace("L", "L ");
array_t = t.split()
print(array_t)

# use list comprehension!
a = [c for c in s]
print(a)