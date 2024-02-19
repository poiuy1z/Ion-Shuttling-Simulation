import numpy as np
from poten_harmonic_fit import *
import math
from global_para import *
import matplotlib.pyplot as plt
from pfit import *

def ctrl_vol(DC1,DC2,delta_x,plot):
    data_dc1 = np.loadtxt('DC1.csv',delimiter=',',skiprows=9)
    data_dc2 = np.loadtxt('DC2.csv',delimiter=',',skiprows=9)
    V1 = 1.6e-19*DC1 * data_dc1[:,3]
    V2 = 1.6e-19*DC2 * data_dc2[:,3]
    V = V1 + V2
    z = 1e-3*data_dc1[:,2]
    a, b, c = v_har(delta_x, z, V, plot)
    omega = math.sqrt(2*a/m)
    x_0 = -b/(m*omega**2)
    return  omega, x_0, c
