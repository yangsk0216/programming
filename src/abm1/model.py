# -*- coding: utf-8 -*-


import random
import math

#
random.seed(0)

x0 = 0
print("x0", x0)
y0 = 0
print("y0", y0)
rn = random.random()
print(rn)

if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print("x0", x0)
#initialise  x0, y0, x1 ,and y1
x0=random.randint(0, 99)
y0=random.randint(0, 99)

x1=random.randint(0, 99)
y1=random.randint(0, 99)
print("x0", x0)
print("y0", y0)
print("x1", x1)
print("y1", y1)
# Calculate the difference in the x coordinates.
x_diff=x1-x0
print(x_diff)
# Calculate the difference in the y coordinates.
y_diff=y1-y0
print(y_diff)
# Square the differences and add the squares
sq_add=x_diff**2+y_diff**2
print(sq_add)
# Calculate the square root
distance=math.sqrt(sq_add)
print(distance)


#change coordinates
rn = random.random()
if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1

rn = random.random()
if rn < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
rn = random.random()    
if rn < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
    
rn = random.random()    
if rn < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
print("x0:", x0,"y0:",y0,"x1:",x1,"y1:",y1)

# Calculate the difference in the x coordinates.
x_diff=x1-x0
print(x_diff)

# Calculate the difference in the y coordinates.
y_diff=y1-y0
print(y_diff)

# Square the differences and add the squares
sq_add=x_diff**2+y_diff**2
print(sq_add)

# Calculate the square root
distance=math.sqrt(sq_add)
print(distance)





