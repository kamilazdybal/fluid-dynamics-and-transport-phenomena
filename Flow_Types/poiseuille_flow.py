import flow_types_classes as ft

if __name__ == "__main__":
    poiseuille_flow = ft.Poiseuille(channelThickness=0.1, fluidName="water")
    poiseuille_flow.velocityDistribution()
