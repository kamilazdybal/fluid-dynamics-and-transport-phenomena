"""
Evaporating acetone sphere
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# Data:
D0 = 0.05 # m

# Vapour pressure:
c_star = 101325

# Downstream concentration:
c_inf = 0

# Mass diffusion coefficient:
DD = 1.64*10**-9 # m^2/s

# Substance density:
rho_s = 784 # kg/m^3

# Time step:
t_step = 10

fig = plt.figure()
ax = plt.axes(xlim=(-0.05, 0.05), ylim=(-0.05, 0.05))
plt.title('Evaporating acetone sphere modeled with the mass diffusion law')
plt.axis('equal')
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
plt.xticks([])
plt.yticks([])
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    theta = np.linspace(0, 2 * np.pi, 100)
    D = (-8*(c_star - c_inf)*DD*i*t_step/rho_s + D0**2)**0.5
    x = D/2 * np.cos(theta)
    y = D/2 * np.sin(theta)
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=145, interval=100, blit=True)

anim.save("./evaporating-sphere.gif", writer='imagemagick', fps=60, bitrate=-1)

plt.show()
