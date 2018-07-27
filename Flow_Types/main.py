import flow_types_classes as ft

if __name__ == "__main__":
    poiseuille_flow = ft.Poiseuille(channelThickness=0.1, fluidName="water")
    poiseuille_flow.velocityDistribution()
    # uniform_flow = ft.Uniform(channelThickness=1)
    # couette_flow = ft.Couette(channelThickness=1)
    # uniform_flow.velocityDistribution()
    # couette_flow.velocityDistribution()
