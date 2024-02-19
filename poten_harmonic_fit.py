import numpy as np
import matplotlib.pyplot as plt
from mini import *

def v_har(delta_x,x_data,y_data,plot):
    degree=2
    fit_x_data=[]
    fit_y_data=[]
    for j in x_data:
        if mini(x_data,y_data)-delta_x<=j and j<=mini(x_data,y_data)+delta_x:
            fit_x_data.append(j)
            fit_y_data.append(y_data[x_data.tolist().index(j)])
    coeffs=np.polyfit(fit_x_data,fit_y_data,degree)
    poly=np.poly1d(coeffs)
    y_fit=poly(x_data)
    if plot == True:
        plt.plot(x_data,y_data,label='original')
        plt.plot(x_data,y_fit,label='fit')
        plt.xlabel('x/m')
        plt.ylabel('potential energy/J')
        plt.legend()
        plt.show()
    return coeffs