import math
import matplotlib.pyplot as plt

# set up runtime comparison
xlist = list(range(1, 100, 1)) # create a list from 1 to 99
labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential', 'Factorial']

c_list = [1 for x in xlist]  # create a list of 1 according to xlist, same size of xlist
log_list = [math.log(x) for x in xlist]
lin_list = [x for x in xlist]
log_lin_list = [x * math.log(x) for x in xlist]
quad_list = [x * x for x in xlist]
cub_list = [x ** 3 for x in xlist]
exp_list = [2**x for x in xlist]
fact_list = [math.factorial(x) for x in xlist]
ylist = [c_list, log_list, lin_list, log_lin_list, quad_list, cub_list, exp_list, fact_list]

# plot
plt.figure(figsize=(12, 10))
plt.ylim(0, 10000)

for i in range(len(ylist)):
  plt.plot(xlist, ylist[i], label=labels[i])

plt.legend(loc=0)
plt.xlabel('n')
plt.ylabel('Relative runtime')
plt.show()




