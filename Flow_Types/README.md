# Flow types with Python OOP

## Crash-tutorial

The following flow types are available:

* Poiseuille flow
* Couette flow
* Uniform flow

All you need to do is to create a new instance of one of the classes:

```python
Poiseuille
Couette
Uniform
```

Example output after creating an instance:

```
_______________________________________

	Poiseuille flow
	Fluid used: water
.......................................

           Parameter  Value     Unit      
 -------------------  --------  ----      
    center velocity:  1.40      m/s       
  channel thickness:  0.1       m         
  pressure gradient:  -1        Pa/m      
            density:  997       kg/m^3    
          viscosity:  0.00089   Pa*s      
_______________________________________
```

## Documentation

### Class `Poiseuille`

#### Attributes

Class `Poiseuille` takes the following arguments (defaults presented if not specified by the user):

```python
Poiseuille(dpdx=-1, channelThickness=0.01, density=997, viscosity=0.00089, fluidName="unknown")
```

`dpdx` pressure gradient in Pa/m

`channelThickness` thickness (or diameter) of the channel in m

`density` fluid density in kg/m^3 [not used for the moment]

`viscosity` fluid viscosity in Pa*s

`fluidName` arbitrarily chosen nick name for the fluid used (could be for instance set to `"water"`)

#### Methods

Class `Poiseuille` has got a method `velocityDistribution` that plots the channel vertical position vs. velocity graph. The default arguments:

```python
velocityDistribution(savePlot=False)
```

`savePlot` boolean specifying whether you want to save the produced plot to .png

### Class `Couette`

#### Attributes

Class `Couette` takes the following arguments (defaults presented if not specified by the user):

```python
Couette(boundaryVel=1, channelThickness=0.01, density=997, viscosity=0.00089, fluidName="unknown")
```

`boundaryVel` velocity at the non-zero-boundary in m/s

`channelThickness` thickness (or diameter) of the channel in m

`density` fluid density in kg/m^3 [not used for the moment]

`viscosity` fluid viscosity in Pa*s [not used for the moment]

`fluidName` arbitrarily chosen nick name for the fluid used (could be for instance set to `"water"`)

#### Methods

Class `Poiseuille` has got a method `velocityDistribution` that plots the channel vertical position vs. velocity graph. The default arguments:

```python
velocityDistribution(savePlot=False)
```

`savePlot` boolean specifying whether you want to save the produced plot to .png

### Class `Uniform`

#### Attributes

Class `Uniform` takes the following arguments (defaults presented if not specified by the user):

```python
Couette(uniformVel=1, channelThickness=0.01, density=997, viscosity=0.00089, fluidName="unknown")
```

`uniformVel` uniform velocity in m/s

`channelThickness` thickness (or diameter) of the channel in m

`density` fluid density in kg/m^3 [not used for the moment]

`viscosity` fluid viscosity in Pa*s [not used for the moment]

`fluidName` arbitrarily chosen nick name for the fluid used (could be for instance set to `"water"`)

#### Methods

Class `Poiseuille` has got a method `velocityDistribution` that plots the channel vertical position vs. velocity graph. The default arguments:

```python
velocityDistribution(savePlot=False)
```

`savePlot` boolean specifying whether you want to save the produced plot to .png

## Plots

Example plots produced are presented below.

![Screenshot][/poiseuille_flow_dpdx-1_channelThickness0.1_water.png]

![Screenshot][/couette_flow_boundaryVel1_channelThickness1_water.png]

![Screenshot][/uniform_flow_uniformVel1_channelThickness0.5_methane.png]
