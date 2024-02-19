This is a python package that can simulate electrostatics and transportation dynamics for ion traps. The complete procedure of the simulation and the corresponding programs used are listed below.

1. Find a target potential moving function, which is usually represented by the motion of the minimum point of the potential, i.e., x_0 (t). -- you may assume the trap frequency to be a constant and solve the simplified ode, e.g., ions9_ode.py, to see the performance of this shuttling function at this stage. 

2. Fit the endcap voltages as functions of the position of the minimum potential point (V_{endcap}(x_0)). -- V_x_fit.py

3. Plug in x_0(t), we can obtain V_{endcap}(t).

4. Using V_{endcap}(t), we can find omega(t) and x_0(t). -- vol_cal.py & fitting.py 

5. Using omega(t) and x_0(t), we can define the equations of motion of the ions and solve for the ions' motion. -- ode_1step.py & ode_step8.py (definition of the ode), ode_solver_1step.py & ode_solver_8step.py (solve the ode and process the data)

Below is the detailed description of each program.

## global_para.py

This program defines the global parameters that we may use throughout the entire simulation.

## Eqposition3.py

Eqposition3(N) can calculate the equilibrium position of N ions in a harmonic potential. Note that the result is centered at x = 0 and you need to multiply it with a scaling factor l = math.pow(e**2/(4*math.pi*E0*m*omega0**2),1/3).

## mini.py

The function mini can find the x-coordinate that has the lowest potential energy.

## pfit.py

The function pfit can do a polynomial fit of given degree and plot the fitted function vs the origianl data if the 'plot' argument is set to be True.

## V_x_fit.py

This program can find the endcap voltages as functions of the minimum potential point. You can adjust the range of the voltage and number of points used for fitting.

## poten_harmonic_fit.py

v_har can fit the proximity of the minimum potential energy point as a harmonic potential. The range of the spatial coordinate used for fitting is [x0-delta_x, x0+delta_x]. You can set the argument plot = True to see the plot of fitted vs original potential.

## vol_cal.py

cal_v() can calculate the DC voltages of 2 endcaps of the time that you choose given the waveform. The result can be used to find omega(t) and x_0(t).

## fitting.py

This program can find omega(t) and x_0(t). You can adjust the degree of the polynomial fit by setting 'order'. Note that the number of points used for fitting depends on the step size that you input.

## ode_1step.py

You can input the omega(t) and x_0(t) as STRINGS and the starting time (t0) and stopping time (tf) of the transportation. It will define the corresponding ode automatically for your system (9 ions).

## ode_8step.py

As ode_1step.py, this program can define the ode for your shuttling process (9 ions). Note that ti0 - ti is the time for transportation of step i. The potential is at rest during ti - t(i+1)0. All the input fucntions (omega(t) and x0(t) should be strings).

## ode_solver_1step.py
It can solve the 1 step ode, calculate the approximate heating and plot the ions' trajectory for you. Please remember to define the initial conditions carefully.

## ode_solver_8step.py

Similar to ode_solver_1step.

The raw data from COMSOL are stored in DC1.csv (electric potential of DC1 = 1V and DC2 = 0 V) and DC2.csv (electric potential of DC1 = 0 V and DC2 = 1V). The model used to obtain the data is stored in the folder model. 

