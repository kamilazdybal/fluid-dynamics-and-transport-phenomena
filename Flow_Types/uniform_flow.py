import flow_types_classes as ft

if __name__ == "__main__":
    uniform_flow = ft.Uniform(channelThickness=0.5, density=0.656, viscosity=0.000011, fluidName="methane")
    uniform_flow.velocityDistribution(savePlot=True)
