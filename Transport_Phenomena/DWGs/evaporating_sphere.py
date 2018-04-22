"""
Evaporating acetone sphere
"""
import math
from matplotlib import pyplot as plt
import numpy
import matplotlib.patches as patches

# Data:
D0 = 0.05 # m

# Vapour pressure:
c_star = 101325

# Downstream concentration:
c_inf = 0

# Mass diffusion coefficient (water):
DD = 1.64*10**-9 # m^2/s

# Substance density:
rho_s = 784 # kg/m^3

# Time discretization:
N = 400
tend = 1500

t = numpy.linspace(0, tend, N)
D = (-8*(c_star - c_inf)*DD*t/rho_s + D0**2)**0.5

# Plot graph:
figure = plt.figure(figsize=(10, 5))
ax1 = figure.add_subplot(1,1,1)
plt.xlabel(r'$t$ [s]', fontsize=12)
plt.ylabel(r'$D(t)$ [$m$]', fontsize=12)
plt.xlim(0, 1.05*max(t))
plt.ylim(-0.15*max(D), 1.1*max(D))
ax1.margins(x=0)
plt.rcParams['axes.xmargin'] = 0

# Line colour:
lineColour = '#0e2f44'

# To plot the line:
plt.plot(t, D, color=lineColour, linestyle='-', linewidth=2.0, zorder=1)

# Save plot:
filename = 'evaporating_sphere.png'
plt.savefig(filename, dpi = 500)

plt.show()
