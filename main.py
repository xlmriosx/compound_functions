import numpy as np
import matplotlib.pyplot as plt

def g(x):
  return x**2

def f(x):
  return np.sin(x)

x = np.linspace(-10,10, num=1000)

def h(x):
  return 2*x



# f_o_g = f(g(x))
# g_o_f = g(f(x))
# g_o_f__h = g(f(h(x)))
# f_o_1 = f(x*1)

fig, ax = plt.subplots()
ax.plot(x, f_o_1)
ax.grid()
plt.show()
