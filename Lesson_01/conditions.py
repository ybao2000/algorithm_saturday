# v = input("Enter a mark between 0 and 100: ")
import random
mark = random.randint(0, 100)
# print("mark is {0}".format(mark))
print(f"mark is {mark}")
if mark >= 85:
  print("grade is A")
elif mark >= 70:
    print("grade is B")
elif mark >= 50:
    print("grade is C")
else:
    print("grade is F")        