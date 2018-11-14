'''
The Stefan Problem

One-dimensional binary transport of species A (water) in species B (air) inside a glass tube.
'''
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import math
import numpy

# Styles:
lineColour = '#0e2f44'
barColour = '#767676'
helpLines = "#e5e5e5"

# Data:
rho_A = 0.01 # [kg/m^3] density of species A
D_AB = 2.2*10**5 # [m^2/s] binary diffusion coefficient water in air at T=273K
L = 0.2 # [m] tube length
Y_A_inf = 0.0001 # [-] species A concentration at infinity
Y_A_i = 0.0002 # [-] species A concentration at the liquid-gas interface
Area_tube = 0.02 * 0.02 # [m^2]

# Length discretization:
N = 20
l = numpy.linspace(0.01, L, N)

mass_flux_A = Area_tube * rho_A * D_AB * math.log((1 - Y_A_inf)/(1 - Y_A_i)) / l * 1000

dim_mass_flux_A = []
Y_vals = [0, 0.05, 0.1, 0.2, 0.5, 0.9, 0.999]

for Y in Y_vals:
    mass_flux = math.log((1 - Y_A_inf)/(1 - Y))
    dim_mass_flux_A.append(mass_flux)

# Plot graph:
figure1 = plt.figure(figsize=(10, 10))
ax1 = figure1.add_subplot(1,1,1)
plt.plot(mass_flux_A, l, color=lineColour, linestyle='-', linewidth=2.0, zorder=1)
plt.xlabel(r'$\dot{m}_A$ $[\frac{g}{s}]$', fontsize=12)
plt.ylabel(r'$L$ [$m$]', fontsize=12)
ax1.margins(x=0)
plt.rcParams['axes.xmargin'] = 0

# Save plot:
filename = 'stefan-problem.png'
plt.savefig(filename, dpi = 500)

figure2 = plt.figure(figsize=(3, 10))
ax2 = figure2.add_subplot(1,1,1)
plt.plot(Y_vals, dim_mass_flux_A, color=lineColour, linestyle='-', linewidth=2.0, zorder=1)
plt.axis('equal')

# Save plot:
filename = 'dimless-mass-flux.png'
plt.savefig(filename, dpi = 500)
plt.show()
plt.close()
