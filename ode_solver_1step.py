from scipy.integrate import solve_ivp
from ode_1step import *
from Eqposition3 import *
from global_para import *

#the angular frequency and minimum point of DC1 = 21 DC2 = 29
omega0 = 1092737.779135
x0 = -1.3888518130414587e-05
l0=math.pow(e**2/(4*math.pi*E0*m*omega0**2),1/3)
x1_i,x2_i,x3_i,x4_i,x5_i,x6_i,x7_i,x8_i,x9_i=Eqposition3(9)*l0
initial_state=[x1_i+x0,x2_i+x0,x3_i+x0,x4_i+x0,x5_i+x0,x6_i+x0,x7_i+x0,x8_i+x0,x9_i+x0,0,0,0,0,0,0,0,0,0]
s1 = x9_i-x8_i
s2 = x8_i-x7_i
s3 = x7_i-x6_i
s4 = x6_i-x5_i
s5 = x5_i-x4_i
s6 = x4_i-x3_i
s7 = x3_i-x2_i
s8 = x2_i-x1_i

T = 13e-6 #the total time of the process
t0 = 0 #starting time 
tf = 1e-5 #stopping time of the transportation
points = 10000 #number of points that you want solve_ivp to calculate
omega_t = '-8.26254447e+2*t**5+2.17102930e+24*t**4-1.73454203e+19*t**3+3.29692567e+13*t**2-7.41325480e+07*t+1.09273853e+06'
x0_t = '-6.74521517e+20*t**5+1.68706057e+16*t**4-1.23854636e+11*t**3+1.69939863e+05*t**2-5.64340867e-01*t-1.36579939e-05'
solution=solve_ivp(ode_9ions,(0,T),initial_state,t_eval=np.linspace(0,T,points),args=(t0,tf,omega_t,x0_t))

x1 = solution.y[0]
x2 = solution.y[1]
x3 = solution.y[2]
x4 = solution.y[3]
x5 = solution.y[4]
x6 = solution.y[5]
x7 = solution.y[6]
x8 = solution.y[7]
x9 = solution.y[8]

a1=0.5*(np.max(x1[math.ceil(points*tf/T):points])-np.min(x1[math.ceil(points*tf/T):points]))
a2=0.5*(np.max(x2[math.ceil(points*tf/T):points])-np.min(x2[math.ceil(points*tf/T):points]))
a3=0.5*(np.max(x3[math.ceil(points*tf/T):points])-np.min(x3[math.ceil(points*tf/T):points]))
a4=0.5*(np.max(x4[math.ceil(points*tf/T):points])-np.min(x4[math.ceil(points*tf/T):points]))
a5=0.5*(np.max(x5[math.ceil(points*tf/T):points])-np.min(x5[math.ceil(points*tf/T):points]))
a6=0.5*(np.max(x6[math.ceil(points*tf/T):points])-np.min(x6[math.ceil(points*tf/T):points]))
a7=0.5*(np.max(x7[math.ceil(points*tf/T):points])-np.min(x7[math.ceil(points*tf/T):points]))
a8=0.5*(np.max(x8[math.ceil(points*tf/T):points])-np.min(x8[math.ceil(points*tf/T):points]))
a9=0.5*(np.max(x9[math.ceil(points*tf/T):points])-np.min(x9[math.ceil(points*tf/T):points]))
a_bar=(a1+a2+a3+a4+a5+a6+a7+a8+a9)/9
x = var('t')
omega_t = lambdify(x, sympify(omega_t))
omega_f = omega_t(tf)
quantum=h_bar*omega_f
n_bar=0.5*m*omega_f**2*a_bar**2/quantum
print(f'the average heating is {n_bar} quanta')  
t = solution.t
plt.plot(1e6*t,1e6*x1)
plt.plot(10**6*t,10**6*x2)
plt.plot(10**6*t,10**6*x3)
plt.plot(10**6*t,10**6*x4)
plt.plot(10**6*t,10**6*x5)
plt.plot(10**6*t,10**6*x6)
plt.plot(10**6*t,10**6*x7)
plt.plot(10**6*t,10**6*x8)
plt.plot(10**6*t,10**6*x9)
plt.xlabel('Time/µs')
plt.ylabel('Positions of the Ions/µm')
plt.show()
