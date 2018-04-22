"""
Modeling the temperature function T(t) change with increasing coefficient
b = hA/(rho*V*Cp) in a lumped system analysis of a steel plate.
                 _____________________________
T_inf           |____________T(t)_____________|

Temperature function in the lumped system:
T(t) = (T_i - T_inf) exp(-bt) + T_inf
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# Thermal data:
Ti = 20 # C deg
Tinf = 100 # C deg

# Steel plate parameters:
rho_steel = 7800 # kg/m^3
Cp_steel = 502 # J/(kgK)
lambda_steel = 43 # W/(mK)
L = 0.1 # m
D = 0.01 # m
H = 0.02 # m
V = L*D*H # m^3
A = D*H # m^2

# Time span:
t_end = 100 # s

# Assume the Nusselt number Nu=1 for a plate:
h = lambda_steel/D

# Starting coefficient b:
b = h*A/(rho_steel*V*Cp_steel)

# Plotting:
fig = plt.figure()
ax = plt.axes(xlim=(0, t_end), ylim=(0, max(Ti, Tinf)*1.1))
line, = ax.plot([], [], lw=2)
plt.title('Increasing b in ' r"$T(t) = (T_i - T_{\infty}) e^{-bt} + T_{\infty}$")
plt.xlabel(r'$t [s]$', fontsize=16)
plt.ylabel(r'$T(t) [^oC]$', fontsize=16)
dashLine = "#cccccc"
plt.plot([0, 100], [Tinf, Tinf], "--", lw=1, color=dashLine, zorder=-1)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    t = np.linspace(0,t_end,100)
    T = (Ti - Tinf)*2.71828**(-b*i*t) + Tinf
    line.set_data(t, T)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=60, interval=100, blit=True, repeat=False)

anim.save("./lumped_system.gif", writer='imagemagick', fps=10, bitrate=-1)

plt.show()
