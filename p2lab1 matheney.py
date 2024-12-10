#cody matheney
#10/1/2024
#using built in libraries

#inport the math libairy

import math


#create a variable to hold pie
pi = math.pi

print(pi)

#get raidies from user
radius = float(input("what is the radius of the circle? "))
print()

#calculate/display the diamerter
diameter = 2*radius
print(f"the diameter of the circle is {diameter:.1f}")

#calculate/display the circumference
circumf=2*pi*radius

#round variable to 2 decimal places
r_circumf = round=(circumf,2)

#display
print(f"the circumference of the circle is{circumf:.2f}/n")
print(f"the rounded circumference of the circle is{r_circumf}/n/n")

#calculate the area
area=math.pi*radius**2

area2=math.pi*math.pow(radius,2)

print(f"the area of the circle is {area:.3f}/n")
print(f"the area of the circle is {area2:.3f}/n")
