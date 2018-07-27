import flow_types_classes as ft

if __name__ == "__main__":
    couette_flow = ft.Couette(channelThickness=1, fluidName="water")
    couette_flow.velocityDistribution(savePlot=True)
