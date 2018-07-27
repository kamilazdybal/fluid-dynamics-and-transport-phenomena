# Flow types with OOP

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

### `Poiseuille` class

Class `Poiseuille` takes the following arguments (defaults presented if not specified by the user):

```python
Poiseuille(dpdx=-1, channelThickness=0.01, density=1000, viscosity=0.00089, fluidName="unknown"))
```

`dpdx`: pressure gradient in Pa/m

`channelThickness`: thickness (or diameter) of the channel in m

`density`: fluid density in kg/m^3 [not used for the moment]

`viscosity`: fluid viscosity in Pa*s

`fluidName`: arbitrarily chosen nick name for the fluid used (could be for instance set to `"water"`)

### `Couette` class

Class `Couette` takes the following arguments (defaults presented if not specified by the user):

```python
Couette(boundaryVel=1, channelThickness=0.01, density=1000, viscosity=0.00089, fluidName="unknown"))
```

`boundaryVel`: velocity at the non-zero-boundary in m/s

`channelThickness`: thickness (or diameter) of the channel in m

`density`: fluid density in kg/m^3 [not used for the moment]

`viscosity`: fluid viscosity in Pa*s [not used for the moment]

`fluidName`: arbitrarily chosen nick name for the fluid used (could be for instance set to `"water"`)


### `Uniform` class

Class `Uniform` takes the following arguments (defaults presented if not specified by the user):

```python
Couette(uniformVel=1, channelThickness=0.01, density=1000, viscosity=0.00089, fluidName="unknown"))
```

`uniformVel`: uniform velocity in m/s

`channelThickness`: thickness (or diameter) of the channel in m

`density`: fluid density in kg/m^3 [not used for the moment]

`viscosity`: fluid viscosity in Pa*s [not used for the moment]

`fluidName`: arbitrarily chosen nick name for the fluid used (could be for instance set to `"water"`)
