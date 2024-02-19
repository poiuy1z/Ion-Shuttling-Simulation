import numpy as np
def mini(x_data,y_data): #find the minimum point of the potential
    min_index=np.argmin(y_data)
    return x_data[min_index]