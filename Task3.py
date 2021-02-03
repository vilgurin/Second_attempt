import math
x = float(input())
e = 0.5*(math.e**x-math.e**(-x))
exp = 0.5*(math.exp(x)-math.exp(-x))
sin = math.sinh(x)
print("SIN =",'{:.4f}'.format(sin))
print("EXP =",'{:.4f}'.format(exp))
print("E =",'{:.4f}'.format(e))
