from vol_cal import *
from ctrl_vol import *
from pfit import *

arr = cal_v()
arr_new = [[] for i in range(3)]
index = 0
order = 5
for i in arr[0]:
    arr_new[0].append(i)
    omega, x0, c = ctrl_vol(arr[1][index],arr[2][index],1e-4,True)
    arr_new[1].append(omega)
    arr_new[2].append(x0)
    index += 1
a1,a2,a3,a4,a5,a6 = pfit(arr_new[0],arr_new[1],order,True) #fit omega_t
print(f'omega_t = {a1}*t**5+{a2}*t**4+{a3}*t**3+{a4}*t**2+{a5}*t+{a6}')
b1,b2,b3,b4,b5,b6 = pfit(arr_new[0],arr_new[2],order,True) #fit x0_t
print(f'x0_t = {b1}*t**5+{b2}*t**4+{b3}*t**3+{b4}*t**2+{b5}*t+{b6}')
