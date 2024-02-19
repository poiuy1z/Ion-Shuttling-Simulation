from sympy.utilities.lambdify import lambdify
from sympy import sympify
from sympy import var
from global_para import *

def ode_9ions(t,y,t0,tf,omega_t,x0_t):
    x1,x2,x3,x4,x5,x6,x7,x8,x9,v1,v2,v3,v4,v5,v6,v7,v8,v9=y
    x = var('t')
    omega_t = lambdify(x, sympify(omega_t))
    x0_t = lambdify(x, sympify(x0_t))
    if t0 <= t and t <= tf:
        omega = omega_t(t)
        x0 = x0_t(t)
    elif t > tf:
        omega = omega_t(tf)
        x0 = x0_t(tf)
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


        
         