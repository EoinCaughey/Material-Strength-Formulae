
print('Calculating critical load for buckling, and thickness of radii.')

length = 3
diameter = float(input('Enter diameter of bar in m:' ))
radius = diameter / 2
youngsModulus = 210 * (10**9)
import math
pi = math.pi

momentInertia = (pi * (radius**4)) / 4

Pcr = ((pi**2) * youngsModulus * momentInertia) / (length**2)

PcrkN = "%.2f" % (Pcr / 1000)

print('The critical force for buckling is',PcrkN,'kN.')
