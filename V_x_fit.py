from ctrl_vol import *
from pfit import *

pos = []
delta = []
for i in range(22):
    omega, x_0, c = ctrl_vol(21+(i/10)**3, 29-(i/10)**3, 1e-4, False)
    omega = omega/(2*pi*1e3)
    pos.append(x_0)
    delta.append((i/10)**3)

print(pfit(pos, delta, 1, True)) #the coefficients of the fitting from highest to lowest degree