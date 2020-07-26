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
D_AB = 2.6*10**(-5) # [m^2/s] binary diffusion coefficient water in air at T=273K
L = 0.1 # [m] tube length
Y_A_inf = 0 # [-] species A concentration at infinity
Patm = 101325 # [Pa] atmospheric pressure
MW_A = 18.01528/1000 # [kg/mol] molecular weight of water (A)
MW_B = 28.97/1000 # [kg/mol] molecular weight of air (B)
T = 298 # [K]
R = 8.314 # [J/mol-K] ideal gas constant

# Species A concentration and density at the liquid-gas interface:
Psat = 3169 # [Pa] saturation pressure of water at 298K from steam tables
Psat_to_Patm = Psat / Patm # [-]
MW_mix = Psat_to_Patm * MW_A + (1 - Psat_to_Patm) * MW_B # [kg/mol] molecular weight of the water-air mixture
Y_A_i =  Psat_to_Patm * MW_A / MW_mix # [-] mass fraction of species A at the interface
MW_mean = 0.5 * (MW_mix + MW_B) # [kg/mol] mean molecular weight in the tube
rho_mean = Patm / ((R/MW_mean) * T) # [kg/m^3] mean molecular density in the tube

# Length discretization:
N = 50
l = numpy.linspace(0.01, L, N)

mass_flux_A = rho_mean * D_AB * math.log((1 - Y_A_inf)/(1 - Y_A_i)) / l * 1000

dim_mass_flux_A = []
Y_vals = [0, 0.05, 0.1, 0.2, 0.5, 0.9, 0.999]

for Y in Y_vals:
    mass_flux = math.log((1 - Y_A_inf)/(1 - Y))
    dim_mass_flux_A.append(mass_flux)

# Plot graph:
figure1 = plt.figure(figsize=(10, 5))
ax1 = figure1.add_subplot(1,1,1)
plt.plot(mass_flux_A, l, color=lineColour, linestyle='--', linewidth=4.0, zorder=1)
plt.xlabel(r'$\dot{m}_A$ $[\frac{g}{s m^2}]$', fontsize=12)
plt.ylabel(r'$x$ [$m$]', fontsize=12)
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
