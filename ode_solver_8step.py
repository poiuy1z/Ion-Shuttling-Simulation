from ode_8step import *
from Eqposition3 import *
from global_para import *
from scipy.integrate import solve_ivp
from sympy import sympify
from sympy import var
from global_para import *
#define the initial conditions
x0 = 4.429878635283609e-05
omega0 = 1096456.8716409325
l0=math.pow(e**2/(4*pi*E0*m*omega0**2),1/3)

x1_i,x2_i,x3_i,x4_i,x5_i,x6_i,x7_i,x8_i,x9_i=Eqposition3(9)*l0
initial_state=[x1_i+x0,x2_i+x0,x3_i+x0,x4_i+x0,x5_i+x0,x6_i+x0,x7_i+x0,x8_i+x0,x9_i+x0,0,0,0,0,0,0,0,0,0]

T = 104e-6 #time of the whole process
t0 = 0
t1 = 1e-5
t20 = 13e-6
t2 = 23e-6
t30 = 26e-6
t3 = 36e-6
t40 = 39e-6
t4 = 49e-6
t50 = 52e-6
t5 = 62e-6
t60 = 65e-6
t6 = 75e-6
t70 = 78e-6
t7 = 88e-6
t80 = 91e-6
t8 = 101e-6
T_t = [t0,t1,t20,t2,t30,t3,t40,t4,t50,t5,t60,t6,t70,t7,t80,t8]

points = 104000 #the points that solve_ivp will calculate

omega1 = '2.772015133198832e+28*t**5+-5.782986657811394e+23*t**4+-2.7916192868315176e+16*t**3+48641594237135.89*t**2+-65769767.67662559*t+1096456.8716409325'
omega2 = '7.633138951550844e+28*t**5+-1.8737586314197116e+24*t**4+1.297948979694663e+19*t**3+-11668749591828.012*t**2+13487057.40043835*t+1097623.4858460408'
omega3 = '2.050016936906952e+28*t**5+-5.2612435493749835e+23*t**4+5.336450479744511e+18*t**3+-26869930245944.367*t**2+33484542.930224586*t+1098468.4520191904'
omega4 = '4.423427643586861e+26*t**5+1.5134895517788186e+23*t**4+-1.734381635889422e+18*t**3+-3081711695951.4473*t**2+-465333.0470892118*t+1098245.0506103255'
omega5 = '-6.53694899969635e+28*t**5+1.705964346574125e+24*t**4-1.3395721278280466e+19*t**3+23878697182268.008*t**2-19298464.406933643*t+1097754.715738415'
omega6 = '-5.112534971324691e+28*t**5+1.1253250238936139e+24*t**4+-4.835480115820753e+18*t**3+-27775503597893.29*t**2+44529546.19468384*t+1097073.1140143569'
omega7 = '-7.246593275885295e+28*t**5+1.870972784709057e+24*t**4+-1.3038598865874852e+19*t**3+2975840823394.238*t**2+1198381.9614494515*t+1096049.5487641308'
omega8 = '-1.0267087528370992e+29*t**5+2.676588206478284e+24*t**4+-1.8974361519732437e+19*t**3+7113462680274.479*t**2+-4848991.836382484*t+1094784.49080201'
omega_t = [omega1,omega2,omega3,omega4,omega5,omega6,omega7,omega8]

x0_1 = '-6.031073967921643e+20*t**5+1.506254788571519e+16*t**4+-100128133382.77051*t**3+-2995.9130315388943*t**2+0.0034052795074320237*t+4.429878635283609e-05'
x0_2 = '-5.118108905243995e+20*t**5+1.278946394227925e+16*t**4+-85212650181.17612*t**3+-191.10863924539473*t**2+6.917211407763005e-05*t+3.4219927119126356e-05'
x0_3 = '-4.7131058497770724e+20*t**5+1.1784074013519922e+16*t**4+-78632959213.87744*t**3+994.5005196749698*t**2-0.001263435886981256*t+2.570237762880089e-05'
x0_4 = '-4.5581537186165975e+20*t**5+1.1391817115061368e+16*t**4+-75959714405.38493*t**3+506.792685153571*t**2+-0.00034207491025507904*t+1.7865782688712374e-05'
x0_5 = '-4.535714130617198e+20*t**5+1.134261888364829e+16*t**4-75599071765.86491*t**3-574.8053416842092*t**2+0.0003719689374086931*t+1.02899992492322e-05'
x0_6 = '-4.712815444536813e+20*t**5+1.1803530238897686e+16*t**4+-79002235586.22932*t**3+2855.197047245028*t**2+-0.0039619620538088405*t+2.7055769972418617e-06'
x0_7 = '-5.114452678182214e+20*t**5+1.2799630982157884e+16*t**4+-85525777459.08046*t**3+1729.0538380434034*t**2+-0.0020236591982569388*t+-5.1438235446970705e-06'
x0_8 = '-6.068555587224059e+20*t**5+1.519336109123881e+16*t**4+-101610768420.8687*t**3+2839.6150087711644*t**2+-0.00290793278070748*t+-1.3665181120276907e-05'
x0_t = [x0_1,x0_2,x0_3,x0_4,x0_5,x0_6,x0_7,x0_8]


solution=solve_ivp(ode_step8,(0,T),initial_state,t_eval=np.linspace(0,T,points),args=(T_t,omega_t,x0_t))

x1 = solution.y[0]
x2 = solution.y[1]
x3 = solution.y[2]
x4 = solution.y[3]
x5 = solution.y[4]
x6 = solution.y[5]
x7 = solution.y[6]
x8 = solution.y[7]
x9 = solution.y[8]
x = var('t')
for i in range(8): #print the heating of each step
    st=T_t[2*i+1]
    if (i <= 6):
        pt=T_t[2*(i+1)]
    else:
        pt = T
    a1=0.5*(np.max(x1[math.ceil(points*st/T):math.floor(points*pt/T)])-np.min(x1[math.ceil(points*st/T):math.floor(points*pt/T)]))
    a2=0.5*(np.max(x2[math.ceil(points*st/T):math.floor(points*pt/T)])-np.min(x2[math.ceil(points*st/T):math.floor(points*pt/T)]))
    a3=0.5*(np.max(x3[math.ceil(points*st/T):math.floor(points*pt/T)])-np.min(x3[math.ceil(points*st/T):math.floor(points*pt/T)]))
    a4=0.5*(np.max(x4[math.ceil(points*st/T):math.floor(points*pt/T)])-np.min(x4[math.ceil(points*st/T):math.floor(points*pt/T)]))
    a5=0.5*(np.max(x5[math.ceil(points*st/T):math.floor(points*pt/T)])-np.min(x5[math.ceil(points*st/T):math.floor(points*pt/T)]))
    a6=0.5*(np.max(x6[math.ceil(points*st/T):math.floor(points*pt/T)])-np.min(x6[math.ceil(points*st/T):math.floor(points*pt/T)]))
    a7=0.5*(np.max(x7[math.ceil(points*st/T):math.floor(points*pt/T)])-np.min(x7[math.ceil(points*st/T):math.floor(points*pt/T)]))
    a8=0.5*(np.max(x8[math.ceil(points*st/T):math.floor(points*pt/T)])-np.min(x8[math.ceil(points*st/T):math.floor(points*pt/T)]))
    a9=0.5*(np.max(x9[math.ceil(points*st/T):math.floor(points*pt/T)])-np.min(x9[math.ceil(points*st/T):math.floor(points*pt/T)]))
    a_bar=(a1+a2+a3+a4+a5+a6+a7+a8+a9)/9
    omega = lambdify(x,omega_t[i])
    omega_value = omega(1e-5)
    quantum=h_bar*omega_value
    n_bar=0.5*m*omega_value**2*a_bar**2/quantum
    print(f'{i+1} step:')
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
