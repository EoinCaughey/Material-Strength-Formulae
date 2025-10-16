
print('Calculating minimum wall thickness of cylindrical steel container with given variables.')

safetyFactor = int(input('Critical safety factor: '))

diameter = int(input('Inner diameter of cylinder: '))
radius = (diameter / 2)

pressureMPa = int(input('Pressure inside container (MPa):'))
pressurePa = int(pressureMPa * (10**6))

yieldStressMPa = int(input('Yield stress of material (MPa):'))
yieldStressPa = int(yieldStressMPa * (10**6))

yieldStressSF = int(yieldStressPa / safetyFactor)
# yieldStressSF is the maximum stress after considering the safety factor in Pa.

# hoop stress = pr/t
# p = pressure = pressurePa or yieldStressPa
# r = radius = diameter/2
# t = wall thickness
# t = pr/hoop = (pressurePa * radius) / yieldStressPa

thickness = (pressurePa * radius) / yieldStressSF

thicknessmm = thickness * (10**3)

#print(safetyFactor)
#print(radius)
#print(yieldStressSF)
#print(pressurePa)
#print(thickness)

print('The minimum wall thickness is',thicknessmm,'mm.')
