import numpy as np
import matplotlib.pyplot as plt
def pfit(x_data,y_data,degree,plot):
    coeffs=np.polyfit(x_data,y_data,degree)
    poly=np.poly1d(coeffs)
    y_fit=poly(x_data)
    if plot == True:
        plt.plot(x_data,y_data,label='original')
        plt.plot(x_data,y_fit,label='fit')
        plt.legend()
        plt.show()
    return coeffs