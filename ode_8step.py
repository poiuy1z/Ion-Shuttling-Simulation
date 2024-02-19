from sympy.utilities.lambdify import lambdify
from sympy import sympify
from sympy import var
from global_para import *
def ode_step8(t,y,T,omega,x0):
    x1,x2,x3,x4,x5,x6,x7,x8,x9,v1,v2,v3,v4,v5,v6,v7,v8,v9=y
    omega1,omega2,omega3,omega4,omega5,omega6,omega7,omega8 = omega
    t0,t1,t20,t2,t30,t3,t40,t4,t50,t5,t60,t6,t70,t7,t80,t8 = T
    x0_1,x0_2,x0_3,x0_4,x0_5,x0_6,x0_7,x0_8 = x0
    x = var('t')
    if t0 <= t <= t1:
        omega_t = lambdify(x, sympify(omega1))
        x0_t = lambdify(x, sympify(x0_1))
        omega_value = omega_t(t)
        x0_value = x0_t(t)
    elif t1 <= t <= t20:
        omega_t = lambdify(x, sympify(omega1))
        x0_t = lambdify(x, sympify(x0_1))
        omega_value = omega_t(t1)
        x0_value = x0_t(t1)
    elif t20 <= t <= t2:
        t_adjusted = t-t20
        omega_t = lambdify(x, sympify(omega2))
        x0_t = lambdify(x, sympify(x0_2))
        omega_value = omega_t(t_adjusted)
        x0_value = x0_t(t_adjusted)
    elif t2 <= t <= t30:
        t_adjusted = t2-t20
        omega_t = lambdify(x, sympify(omega2))
        x0_t = lambdify(x, sympify(x0_2))
        omega_value = omega_t(t_adjusted)
        x0_value = x0_t(t_adjusted)
    elif t30 <= t <= t3:
        t_adjusted = t-t30
        omega_t = lambdify(x, sympify(omega3))
        x0_t = lambdify(x, sympify(x0_3))
        omega_value = omega_t(t_adjusted)
        x0_value = x0_t(t_adjusted)
    elif t3 <= t <= t40:
        t_adjusted = t3-t30
        omega_t = lambdify(x, sympify(omega3))
        x0_t = lambdify(x, sympify(x0_3))
        omega_value = omega_t(t_adjusted)
        x0_value = x0_t(t_adjusted)
    elif t40 <= t <= t4:
        t_adjusted = t-t40
        omega_t = lambdify(x, sympify(omega4))
        x0_t = lambdify(x, sympify(x0_4))
        omega_value = omega_t(t_adjusted)
        x0_value = x0_t(t_adjusted)
    elif t4 <= t <= t50:
        t_adjusted = t4-t40
        omega_t = lambdify(x, sympify(omega4))
        x0_t = lambdify(x, sympify(x0_4))
        omega_value = omega_t(t_adjusted)
        x0_value = x0_t(t_adjusted)
    elif t50 <= t <=t5:
        t_adjusted = t-t50
        omega_t = lambdify(x, sympify(omega5))
        x0_t = lambdify(x, sympify(x0_5))
        omega_value = omega_t(t_adjusted)
        x0_value = x0_t(t_adjusted)
    elif t5 <= t <= t60:
        t_adjusted = t5-t50
        omega_t = lambdify(x, sympify(omega5))
        x0_t = lambdify(x, sympify(x0_5))
        omega_value = omega_t(t_adjusted)
        x0_value = x0_t(t_adjusted)
    elif t60 <= t <= t6:
        t_adjusted = t-t60
        omega_t = lambdify(x, sympify(omega6))
        x0_t = lambdify(x, sympify(x0_6))
        omega_value = omega_t(t_adjusted)
        x0_value = x0_t(t_adjusted)
    elif t6 <= t <= t70:
        t_adjusted = t6-t60
        omega_t = lambdify(x, sympify(omega6))
        x0_t = lambdify(x, sympify(x0_6))
        omega_value = omega_t(t_adjusted)
        x0_value = x0_t(t_adjusted)
    elif t70 <= t <= t7:
        t_adjusted = t-t70
        omega_t = lambdify(x, sympify(omega7))
        x0_t = lambdify(x, sympify(x0_7))
        omega_value = omega_t(t_adjusted)
        x0_value = x0_t(t_adjusted)
    elif t7 <= t <= t80:
        t_adjusted = t7-t70
        omega_t = lambdify(x, sympify(omega7))
        x0_t = lambdify(x, sympify(x0_7))
        omega_value = omega_t(t_adjusted)
        x0_value = x0_t(t_adjusted)
    elif t80 <= t <= t8:
        t_adjusted = t-t80
        omega_t = lambdify(x, sympify(omega8))
        x0_t = lambdify(x, sympify(x0_8))
        omega_value = omega_t(t_adjusted)
        x0_value = x0_t(t_adjusted)
    elif t > t8:
        t_adjusted = t8-t80
        omega_t = lambdify(x, sympify(omega8))
        x0_t = lambdify(x, sympify(x0_8))
        omega_value = omega_t(t_adjusted)
        x0_value = x0_t(t_adjusted)
    a=-m*omega_value**2
    b=m*omega_value**2*x0_value
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


        
         