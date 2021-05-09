a = 5
b = 2
#2.499999999999999999 => round => 2
# round #.## if .## < 0.5, cut off, >0.5, go up, ==0.5, hard to tell
import math
print("a/b", a/b, "round of b/a", round(a/b), "floor of a/b", a//b, "ceil of a/b", math.ceil(a/b))