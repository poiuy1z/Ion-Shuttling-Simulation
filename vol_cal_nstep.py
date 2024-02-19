from sympy.utilities.lambdify import lambdify
from sympy import sympify
from sympy import var
import numpy as np
def cal_v():
    n = int(input("Please input the number of electrodes: "))
    con = input("Enter Yes to start or No to end: ")
    V = [[] for i in range(n+1)]
    while( con == 'Yes'):
        t0 = float(input("Please input the start time: "))
        tf = float(input("Please input the stop time: "))
        dt = float(input("Please input the step size: "))
        for i in range(n):
            t = var('t')
            f = input(f"Please input the voltage function of DC {i+1} (using t as the variable): ")
            func = lambdify(t, sympify(f))
            t = t0
            while(t <= tf):
                if i == 0:
                    V[0].append(t)
                V[i+1].append(func(t))
                t += dt
        V[0].append('#')
        for i in range(n):
            V[i+1].append('#')
        con = input("Enter Yes to start or No to end: ")
    return np.array(V)

