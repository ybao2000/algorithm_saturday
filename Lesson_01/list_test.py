a = [1, 3, 3, 2, 5, 8, 7, 10, 2]
#    0, 1, 2, 3, 4, 5, 6, 7,  8
#       1, 2, 3, 4      # inc = 1   I didn't provide inc, which means inc = 1
#       1,    3,        # inc = 2
# index - we use index to get the item/element in the list
print(a[5])

b = a[1:5:2]  # slicing: start, end(excluded), inc=2, 1, 1+2, 1+2+2, 1+2+2+2
print(b)

d = a[::-1]   #  why this is reverse ?????
print(d)


s = ["alpha", "beta", "citra", "dummy", "elephant", "friend"]
c = s[1:5:2]
print(c)

e = s[::-1]
print(e)