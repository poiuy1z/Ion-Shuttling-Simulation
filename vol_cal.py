from sympy.utilities.lambdify import lambdify
from sympy import sympify
from sympy import var
import numpy as np
def cal_v():
    V = [[] for i in range(3)]
    t0 = float(input("Please input the start time (s): "))
    tf = float(input("Please input the stop time (s): "))
    dt = float(input("Please input the step size (s): "))
    for i in range(2):
        x = var('t')
        f = input(f"Please input the voltage function of DC {i+1} (using t as the variable): ")
        func = lambdify(x, sympify(f))
        t = t0
        while(t <= tf):
            if i == 0:
                V[0].append(t)
            V[i+1].append(func(t))
            t += dt
    return np.array(V)
