 #2 types of programmers 
#firrst they think for the best and they verify the others they assume it is the best 
"""
import math
import pandas
import numpy
"""


from email import message
import math
from math import pi


print("test")
pi_squared = 5 * 2
print("this is the magic PI",math.pi)
print("this is the squred:", pi_squared)

#this is a test to see how this thing work
# pythin built in test module 
#as schspear said trust but verify
#lest stratt and discove this modile bny calculating the area o a circle 
# A = pi * r**2
def circle_area(r):
    if r < 0:
        raise ValueError("The radius cannt be negative")
    return pi*(r**2)

#test functrion
radii = [2, 3 ,-4, 5j, 1.2,True, 5j, "radius"]
message = "Area of the circle of with r = {radius} is {area} "

for r in radii: 
    A = circle_area(r)
    print(message.format(radius=r, area=A))


print("ttest")