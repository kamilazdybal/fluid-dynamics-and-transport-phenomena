import matplotlib.pyplot as plt
import numpy as np
import pylab
import time

# Master class FlowType:

class FlowType:

    def __init__(self, channelThickness, density, viscosity, fluidName):
        print("_______________________________________\n")
        self.channelThickness = channelThickness
        self.density = density
        self.viscosity = viscosity
        self.fluidName = fluidName

# Child classes:

class Couette(FlowType):

    def __init__(self, boundaryVel=1, channelThickness=0.01, density=997, viscosity=0.00089, fluidName="unknown"):
        super().__init__(channelThickness, density, viscosity, fluidName)
        self.boundaryVel = boundaryVel

        print("\tCouette flow")
        if fluidName != "unknown":
            print("\tFluid used: " + fluidName)
        print(".......................................\n")
        print('{:>20}  {:<8}  {:<10}'.format("Parameter", "Value", "Unit"))
        print('{:>20}  {:<8}  {:<10}'.format("-------------------", "--------", "----"))
        print('{:>20}  {:<8}  {:<10}'.format("center velocity:", str(boundaryVel), "m/s"))
        print('{:>20}  {:<8}  {:<10}'.format("channel thickness:", str(channelThickness), "m"))
        print('{:>20}  {:<8}  {:<10}'.format("density:", str(density), "kg/m^3"))
        print('{:>20}  {:<8}  {:<10}'.format("viscosity:", str(viscosity), "Pa*s"))
        print("_______________________________________\n")

    def velocityDistribution(self):
        velocity = '#282850'
        boundary = "#cccccc"
        print("Plotting velocity distribution...")
        y = np.linspace(-self.channelThickness/2, self.channelThickness/2, num=100)
        vel = self.boundaryVel/2 * (1 + y/(self.channelThickness/2))
        plt.ylim(-1.1*self.channelThickness/2, 1.1*self.channelThickness/2)
        plt.plot(vel, y, "-", lw=1.5, color=velocity, zorder=-1)
        plt.plot([0, self.boundaryVel], [-self.channelThickness/2, -self.channelThickness/2], "-", lw=2, color=boundary, zorder=1)
        plt.plot([0, self.boundaryVel], [self.channelThickness/2, self.channelThickness/2], "--", lw=2, color=boundary, zorder=1)
        plt.plot([0, 0], [-self.channelThickness/2, self.channelThickness/2], "--", lw=1.5, color=velocity, zorder=1)
        plt.title('Couette flow velocity distribution for fluid: ' + self.fluidName, fontsize=10)
        plt.draw()
        plt.pause(3)
        plt.close()

class Uniform(FlowType):

    def __init__(self, uniformVel=1, channelThickness=0.01, density=997, viscosity=0.00089, fluidName="unknown"):
        super().__init__(channelThickness, density, viscosity, fluidName)
        self.uniformVel = uniformVel

        print("\tUniform flow")
        if fluidName != "unknown":
            print("\tFluid used: " + fluidName)
        print(".......................................\n")
        print('{:>20}  {:<8}  {:<10}'.format("Parameter", "Value", "Unit"))
        print('{:>20}  {:<8}  {:<10}'.format("-------------------", "--------", "----"))
        print('{:>20}  {:<8}  {:<10}'.format("center velocity:", str(uniformVel), "m/s"))
        print('{:>20}  {:<8}  {:<10}'.format("channel thickness:", str(channelThickness), "m"))
        print('{:>20}  {:<8}  {:<10}'.format("density:", str(density), "kg/m^3"))
        print('{:>20}  {:<8}  {:<10}'.format("viscosity:", str(viscosity), "Pa*s"))
        print("_______________________________________\n")

    def velocityDistribution(self):
        velocity = '#282850'
        boundary = "#cccccc"
        print("Plotting velocity distribution...")
        y = np.linspace(-self.channelThickness/2, self.channelThickness/2, num=100)
        vel = self.uniformVel*y/y
        plt.ylim(-1.1*self.channelThickness/2, 1.1*self.channelThickness/2)
        plt.plot(vel, y, "-", lw=1.5, color=velocity, zorder=-1)
        plt.plot([0, 0], [-self.channelThickness/2, self.channelThickness/2], "--", lw=1.5, color=velocity, zorder=1)
        plt.plot([0, self.uniformVel], [-self.channelThickness/2, -self.channelThickness/2], "--", lw=2, color=boundary, zorder=1)
        plt.plot([0, self.uniformVel], [self.channelThickness/2, self.channelThickness/2], "--", lw=2, color=boundary, zorder=1)
        plt.title('Uniform flow velocity distribution for fluid: ' + self.fluidName, fontsize=10)
        plt.draw()
        plt.pause(3)
        plt.close()

class Poiseuille(FlowType):

    def __init__(self, dpdx=-1, channelThickness=0.01, density=997, viscosity=0.00089, fluidName="unknown"):
        super().__init__(channelThickness, density, viscosity, fluidName)
        self.dpdx = dpdx
        self.centerVel = -1/(2*viscosity)*dpdx*(channelThickness/2)**2

        print("\tPoiseuille flow")
        if fluidName != "unknown":
            print("\tFluid used: " + fluidName)
        print(".......................................\n")
        print('{:>20}  {:<8}  {:<10}'.format("Parameter", "Value", "Unit"))
        print('{:>20}  {:<8}  {:<10}'.format("-------------------", "--------", "----"))
        print('{:>20}  {:<8}  {:<10}'.format("center velocity:", "%.2f" %self.centerVel, "m/s"))
        print('{:>20}  {:<8}  {:<10}'.format("channel thickness:", str(channelThickness), "m"))
        print('{:>20}  {:<8}  {:<10}'.format("pressure gradient:", str(dpdx), "Pa/m"))
        print('{:>20}  {:<8}  {:<10}'.format("density:", str(density), "kg/m^3"))
        print('{:>20}  {:<8}  {:<10}'.format("viscosity:", str(viscosity), "Pa*s"))
        print("_______________________________________\n")

    def velocityDistribution(self):
        velocity = '#282850'
        boundary = "#cccccc"
        print("Plotting velocity distribution...")
        y = np.linspace(-self.channelThickness/2, self.channelThickness/2, num=100)
        vel = self.centerVel * (1 - (y/(self.channelThickness/2))**2)
        plt.ylim(-1.2*self.channelThickness/2, 1.2*self.channelThickness/2)
        plt.plot(vel, y, "-", lw=1.5, color=velocity, zorder=-1)
        plt.plot([0, 0], [-self.channelThickness/2, self.channelThickness/2], "--", lw=1.5, color=velocity, zorder=1)
        plt.plot([0, self.centerVel], [-self.channelThickness/2, -self.channelThickness/2], "-", lw=1, color=boundary, zorder=1)
        plt.plot([0, self.centerVel], [self.channelThickness/2, self.channelThickness/2], "-", lw=1, color=boundary, zorder=1)
        plt.title('Poiseuille flow velocity distribution for fluid: ' + self.fluidName, fontsize=10)
        plt.draw()
        plt.pause(3)
        plt.close()

if __name__ == "__main__":
    print("Testing classes Couette(FlowType), Uniform(FlowType), Poiseuille(FlowType)")

    poiseuille_flow = Poiseuille()
    uniform_flow = Uniform()
    couette_flow = Couette()

    poiseuille_flow = Poiseuille(density=988, fluidName="water")
    uniform_flow = Uniform(uniformVel=10, channelThickness=0.1, density=1100)
    couette_flow = Couette(boundaryVel=5, channelThickness=1, fluidName="methane")
