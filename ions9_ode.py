import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import math
from Eqposition3 import *
#from normal_mode import *
from global_para import *

omega = 1089364.6109329504
def ions9_ode(t,y,T,T0,mode):
    x1,x2,x3,x4,x5,x6,x7,x8,x9,v1,v2,v3,v4,v5,v6,v7,v8,v9=y #x1: the position of the left most ion
    s1=x9-x8 #s1: the first displacement
    s2=x8-x7
    s3=x7-x6
    s4=x6-x5
    if mode == 'inverse':
        if 0<=t<=T:
            x0=((s1*60)/(T**2*omega**2))*(t/T-3*(t/T)**2+2*(t/T)**3)+s1*(10*(t/T)**3-15*(t/T)**4+6*(t/T)**5)
        elif T<t<(T+T0):
            x0=s1
        elif (T+T0)<=t<=(2*T+T0):
            nt=t-(T+T0)
            x0=s1+((s2*60)/(T**2*omega**2))*(nt/T-3*(nt/T)**2+2*(nt/T)**3)+s2*(10*(nt/T)**3-15*(nt/T)**4+6*(nt/T)**5)
        elif (2*T+T0)<t<(2*T+2*T0):
            x0=s1+s2
        elif (2*T+2*T0)<=t<=(3*T+2*T0):
            nt=t-(2*T+2*T0)
            x0=s1+s2+((s3*60)/(T**2*omega**2))*(nt/T-3*(nt/T)**2+2*(nt/T)**3)+s3*(10*(nt/T)**3-15*(nt/T)**4+6*(nt/T)**5)
        elif (3*T+2*T0)<t<(3*T+3*T0):
            x0=s1+s2+s3
        elif (3*T+3*T0)<=t<=(4*T+3*T0):
            nt=t-(3*T+3*T0)
            x0=s1+s2+s3+((s4*60)/(T**2*omega**2))*(nt/T-3*(nt/T)**2+2*(nt/T)**3)+s4*(10*(nt/T)**3-15*(nt/T)**4+6*(nt/T)**5)
        elif (4*T+3*T0)<t<(4*T+4*T0):
            x0=s1+s2+s3+s4
        elif (4*T+4*T0)<=t<=(5*T+4*T0):
            nt=t-(4*T+4*T0)
            x0=s1+s2+s3+s4+((s4*60)/(T**2*omega**2))*(nt/T-3*(nt/T)**2+2*(nt/T)**3)+s4*(10*(nt/T)**3-15*(nt/T)**4+6*(nt/T)**5)
        elif (5*T+4*T0)<t<(5*T+5*T0):
            x0=s1+s2+s3+2*s4
        elif (5*T+5*T0)<=t<=(6*T+5*T0):
            nt=t-(5*T+5*T0)
            x0=s1+s2+s3+2*s4+((s3*60)/(T**2*omega**2))*(nt/T-3*(nt/T)**2+2*(nt/T)**3)+s3*(10*(nt/T)**3-15*(nt/T)**4+6*(nt/T)**5)
        elif (6*T+5*T0)<t<(6*T+6*T0):
            x0=s1+s2+2*s3+2*s4
        elif (6*T+6*T0)<=t<=(7*T+6*T0):
            nt=t-(6*T+6*T0)
            x0=s1+s2+2*s3+2*s4+((s2*60)/(T**2*omega**2))*(nt/T-3*(nt/T)**2+2*(nt/T)**3)+s2*(10*(nt/T)**3-15*(nt/T)**4+6*(nt/T)**5)
        elif (7*T+6*T0)<t<(7*T+7*T0):
            x0=s1+2*s2+2*s3+2*s4
        elif (7*T+7*T0)<=t<=(8*T+7*T0):
            nt=t-(7*T+7*T0)
            x0=s1+2*s2+2*s3+2*s4+((s1*60)/(T**2*omega**2))*(nt/T-3*(nt/T)**2+2*(nt/T)**3)+s1*(10*(nt/T)**3-15*(nt/T)**4+6*(nt/T)**5)
        else:
            x0=(s1+s2+s3+s4)*2
    if mode == 'sin':
                if 0<=t<=T:
                      x0=s1/2*(1-math.cos(math.pi*t/T))
                elif T<t<(T+T0):
                      x0=s1
                elif (T+T0)<=t<=(2*T+T0):
                    nt=t-(T+T0)
                    x0=s1+s2/2*(1-math.cos(math.pi*nt/T))
                elif (2*T+T0)<t<(2*T+2*T0):
                      x0=s1+s2
                elif (2*T+2*T0)<=t<=(3*T+2*T0):
                    nt=t-(2*T+2*T0)
                    x0=s1+s2+s3/2*(1-math.cos(math.pi*nt/T))
                elif (3*T+2*T0)<t<(3*T+3*T0):
                      x0=s1+s2+s3
                elif (3*T+3*T0)<=t<=(4*T+3*T0):
                    nt=t-(3*T+3*T0)
                    x0=s1+s2+s3+s4/2*(1-math.cos(math.pi*nt/T))
                elif (4*T+3*T0)<t<(4*T+4*T0):
                     x0=s1+s2+s3+s4
                elif (4*T+4*T0)<=t<=(5*T+4*T0):
                    nt=t-(4*T+4*T0)
                    x0=s1+s2+s3+s4+s4/2*(1-math.cos(math.pi*nt/T))
                elif (5*T+4*T0)<t<(5*T+5*T0):
                     x0=s1+s2+s3+2*s4
                elif (5*T+5*T0)<=t<=(6*T+5*T0):
                     nt=t-(5*T+5*T0)
                     x0=s1+s2+s3+2*s4+s3/2*(1-math.cos(math.pi*nt/T))
                elif (6*T+5*T0)<t<(6*T+6*T0):
                     x0=s1+s2+2*s3+2*s4
                elif (6*T+6*T0)<=t<=(7*T+6*T0):
                     nt=t-(6*T+6*T0)
                     x0=s1+s2+2*s3+2*s4+s2/2*(1-math.cos(math.pi*nt/T))
                elif (7*T+6*T0)<t<(7*T+7*T0):
                     x0=s1+2*s2+2*s3+2*s4
                elif (7*T+7*T0)<=t<=(8*T+7*T0):
                     nt=t-(7*T+7*T0)
                     x0=s1+2*s2+2*s3+2*s4+s1/2*(1-math.cos(math.pi*nt/T))
                else:
                     x0=(s1+s2+s3+s4)*2
    if mode == 'flat':
                if 0<=t<=T:
                     x0=s1/2*(1-10/9*(math.cos(math.pi*t/T)-0.1*math.cos(math.pi*3*t/T)))
                elif T<t<(T+T0):
                     x0=s1
                elif (T+T0)<=t<=(2*T+T0):
                     nt=t-(T+T0)
                     x0=s1+s2/2*(1-10/9*(math.cos(math.pi*nt/T)-0.1*math.cos(math.pi*3*nt/T)))
                elif (2*T+T0)<t<(2*T+2*T0):
                     x0=s1+s2
                elif (2*T+2*T0)<=t<=(3*T+2*T0):
                     nt=t-(2*T+2*T0)
                     x0=s1+s2+s3/2*(1-10/9*(math.cos(math.pi*nt/T)-0.1*math.cos(math.pi*3*nt/T)))
                elif (3*T+2*T0)<t<(3*T+3*T0):
                     x0=s1+s2+s3
                elif (3*T+3*T0)<=t<=(4*T+3*T0):
                     nt=t-(3*T+3*T0)
                     x0=s1+s2+s3+s4/2*(1-10/9*(math.cos(math.pi*nt/T)-0.1*math.cos(math.pi*3*nt/T)))
                elif (4*T+3*T0)<t<(4*T+4*T0):
                     x0=s1+s2+s3+s4
                elif (4*T+4*T0)<=t<=(5*T+4*T0):
                     nt=t-(4*T+4*T0)
                     x0=s1+s2+s3+s4+s4/2*(1-10/9*(math.cos(math.pi*nt/T)-0.1*math.cos(math.pi*3*nt/T)))
                elif (5*T+4*T0)<t<(5*T+5*T0):
                     x0=s1+s2+s3+2*s4
                elif (5*T+5*T0)<=t<=(6*T+5*T0):
                     nt=t-(5*T+5*T0)
                     x0=s1+s2+s3+2*s4+s3/2*(1-10/9*(math.cos(math.pi*nt/T)-0.1*math.cos(math.pi*3*nt/T)))
                elif (6*T+5*T0)<t<(6*T+6*T0):
                     x0=s1+s2+2*s3+2*s4
                elif (6*T+6*T0)<=t<=(7*T+6*T0):
                     nt=t-(6*T+6*T0)
                     x0=s1+s2+2*s3+2*s4+s2/2*(1-10/9*(math.cos(math.pi*nt/T)-0.1*math.cos(math.pi*3*nt/T)))
                elif (7*T+6*T0)<t<(7*T+7*T0):
                     x0=s1+2*s2+2*s3+2*s4
                elif (7*T+7*T0)<=t<=(8*T+7*T0):
                     nt=t-(7*T+7*T0)
                     x0=s1+2*s2+2*s3+2*s4+s1/2*(1-10/9*(math.cos(math.pi*nt/T)-0.1*math.cos(math.pi*3*nt/T)))
                else:
                     x0=(s1+s2+s3+s4)*2
    if mode == 'linear':
           if 0<=t<=T:
                 x0=s1/T*t
           elif T<t<(T+T0):
                 x0=s1
           elif (T+T0)<=t<=(2*T+T0):
                 nt=t-(T+T0)
                 x0=s1+s2/T*nt
           elif (2*T+T0)<t<(2*T+2*T0):
                 x0=s1+s2
           elif (2*T+2*T0)<=t<=(3*T+2*T0):
                 nt=t-(2*T+2*T0)
                 x0=s1+s2+s3/T*nt
           elif (3*T+2*T0)<t<(3*T+3*T0):
                 x0=s1+s2+s3
           elif (3*T+3*T0)<=t<=(4*T+3*T0):
                 nt=t-(3*T+3*T0)
                 x0=s1+s2+s3+s4/T*nt
           elif (4*T+3*T0)<t<(4*T+4*T0):
                 x0=s1+s2+s3+s4
           elif (4*T+4*T0)<=t<=(5*T+4*T0):
                 nt=t-(4*T+4*T0)
                 x0=s1+s2+s3+s4+s4/T*nt
           elif (5*T+4*T0)<t<(5*T+5*T0):
                 x0=s1+s2+s3+2*s4
           elif (5*T+5*T0)<=t<=(6*T+5*T0):
                 nt=t-(5*T+5*T0)
                 x0=s1+s2+s3+2*s4+s3/T*nt
           elif (6*T+5*T0)<t<(6*T+6*T0):
                 x0=s1+s2+2*s3+2*s4
           elif (6*T+6*T0)<=t<=(7*T+6*T0):
                 nt=t-(6*T+6*T0)
                 x0=s1+s2+2*s3+2*s4+s2/T*nt
           elif (7*T+6*T0)<t<(7*T+7*T0):
                 x0=s1+2*s2+2*s3+2*s4
           elif (7*T+7*T0)<=t<=(8*T+7*T0):
                 nt=t-(7*T+7*T0)
                 x0=s1+2*s2+2*s3+2*s4+s1/T*nt
           else:
                x0=(s1+s2+s3+s4)*2                  
    a=-m*omega**2
    b=m*omega**2*x0
    dx1_dt=v1
    dx2_dt=v2
    dx3_dt=v3
    dx4_dt=v4
    dx5_dt=v5
    dx6_dt=v6
    dx7_dt=v7
    dx8_dt=v8
    dx9_dt=v9
    dv1_dt=1/m*(a*x1+b-e**2/(4*pi*E0)*(1/(x1-x2)**2+1/(x1-x3)**2+1/(x1-x4)**2+1/(x1-x5)**2+1/(x1-x6)**2+1/(x1-x7)**2+1/(x1-x8)**2+1/(x1-x9)**2))
    dv2_dt=1/m*(a*x2+b-e**2/(4*pi*E0)*(-1/(x2-x1)**2+1/(x2-x3)**2+1/(x2-x4)**2+1/(x2-x5)**2+1/(x2-x6)**2+1/(x2-x7)**2+1/(x2-x8)**2+1/(x2-x9)**2))
    dv3_dt=1/m*(a*x3+b-e**2/(4*pi*E0)*(-1/(x3-x1)**2-1/(x3-x2)**2+1/(x3-x4)**2+1/(x3-x5)**2+1/(x3-x6)**2+1/(x3-x7)**2+1/(x3-x8)**2+1/(x3-x9)**2))
    dv4_dt=1/m*(a*x4+b-e**2/(4*pi*E0)*(-1/(x4-x1)**2-1/(x4-x2)**2-1/(x4-x3)**2+1/(x4-x5)**2+1/(x4-x6)**2+1/(x4-x7)**2+1/(x4-x8)**2+1/(x4-x9)**2))
    dv5_dt=1/m*(a*x5+b-e**2/(4*pi*E0)*(-1/(x5-x1)**2-1/(x5-x2)**2-1/(x5-x3)**2-1/(x5-x4)**2+1/(x5-x6)**2+1/(x5-x7)**2+1/(x5-x8)**2+1/(x5-x9)**2))
    dv6_dt=1/m*(a*x6+b-e**2/(4*pi*E0)*(-1/(x6-x1)**2-1/(x6-x2)**2-1/(x6-x3)**2-1/(x6-x4)**2-1/(x6-x5)**2+1/(x6-x7)**2+1/(x6-x8)**2+1/(x6-x9)**2))
    dv7_dt=1/m*(a*x7+b-e**2/(4*pi*E0)*(-1/(x7-x1)**2-1/(x7-x2)**2-1/(x7-x3)**2-1/(x7-x4)**2-1/(x7-x5)**2-1/(x7-x6)**2+1/(x7-x8)**2+1/(x7-x9)**2))
    dv8_dt=1/m*(a*x8+b-e**2/(4*pi*E0)*(-1/(x8-x1)**2-1/(x8-x2)**2-1/(x8-x3)**2-1/(x8-x4)**2-1/(x8-x5)**2-1/(x8-x6)**2-1/(x8-x7)**2+1/(x8-x9)**2))
    dv9_dt=1/m*(a*x9+b-e**2/(4*pi*E0)*(-1/(x9-x1)**2-1/(x9-x2)**2-1/(x9-x3)**2-1/(x9-x4)**2-1/(x9-x5)**2-1/(x9-x6)**2-1/(x9-x7)**2-1/(x9-x8)**2))
    return [dx1_dt,dx2_dt,dx3_dt,dx4_dt,dx5_dt,dx6_dt,dx7_dt,dx8_dt,dx9_dt,dv1_dt,dv2_dt,dv3_dt,dv4_dt,dv5_dt,dv6_dt,dv7_dt,dv8_dt,dv9_dt]

l0=math.pow(e**2/(4*math.pi*E0*m*omega**2),1/3)
x1_i,x2_i,x3_i,x4_i,x5_i,x6_i,x7_i,x8_i,x9_i=Eqposition3(9)*l0
initial_state=[x1_i,x2_i,x3_i,x4_i,x5_i,x6_i,x7_i,x8_i,x9_i,0,0,0,0,0,0,0,0,0]
solution=solve_ivp(ions9_ode,(0,107e-6),initial_state,t_eval=np.linspace(0,107e-6,10000),args=(1e-5,3e-6,'inverse'))
t = solution.t
x1 = solution.y[0]
plt.plot(t,x1)
plt.show()

