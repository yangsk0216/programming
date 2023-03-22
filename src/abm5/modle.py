# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:10:53 2023

@author: yang
"""
import operator
from matplotlib import pyplot as plt
import random
import my_modules.agentframework as af
import my_modules.io as io
random.seed(6)

# difine a function that adds up all the values in environment.
def sum_value(environment):
    sum_value = 0
    for i in range(len(environment)):
        for j in range(len(environment[i])):
            sum_value += environment[i][j]
    return sum_value

# difine a function that adds up all the store values.
def sum_store_value(agents):
    sum_store_value = 0
    for i in range(len(agents)):
        sum_store_value += agents[i].store
    return sum_store_value

#difine a function that out put the value to the file namend a.out     
def output_environment(digit):
    f = open("a.out", 'w')
    m = sum_value(digit)
    f.write(str(m))
    f.close()

#gain the value of environment ,n_cols, n_rows         
environment,n_cols, n_rows = io.read_data()

#write the value to the file a.out
output_environment(environment) 


# The minimum an agents x coordinate is allowed to be.
x_min=0
# The maximum an agents x coordinate is allowed to be.
x_max = n_cols - 1
# The minimum an agents y coordinate is allowed to be.
y_min=0
# The maximum an agents y coordinate is allowed to be.
y_max = n_rows - 1

# Initialise agents
agents = []

#Change the plot limits for a closer look at the centre of the environment
# plt.ylim(y_max / 3, y_max * 2 / 3)
# plt.xlim(x_max / 3, x_max * 2 / 3)    
plt.ylim(y_min, y_max)
plt.xlim(x_min, x_max)

interaction = 1000

n_agents = 10
for i in range(n_agents):
    # Create an agent
   agents.append(af.Agent(i,environment,n_rows,n_cols))
   
   #plot every agents x coordinate,agents y coordinate before move
   plt.scatter(agents[i].x,agents[i].y, color='white')
   
   for j in range(interaction):
       #run the function eat
        agents[i].move(x_min, y_min, x_max, y_max)
        
       #run the function eat
        agents[i].eat()
   #plot every agents x coordinate,agents y coordinate after move    
   #plt.scatter(agents[i].x,agents[i].y, color='red') 
   
#plot the agents on the environment  
plt.imshow(environment)


# Plot the coordinate with the largest x red
lx = max(agents, key=operator.attrgetter('x'))
plt.scatter(lx.x, lx.y, color='purple')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.attrgetter('x'))
plt.scatter(sx.x, sx.y, color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.attrgetter('y'))
plt.scatter(ly.x, ly.y, color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.attrgetter('y'))
plt.scatter(sy.x, sy.y, color='red')

plt.show()

#all the values in environment
a = sum_value(environment)
#all the values in environment
print("all the value in the environment",a)


#all the store values 
b = sum_store_value(agents)
# print all the store values 
print("all the value store",b)




# def get_max_distance(ag):
#     """
    
#     Parameters
#     ----------
#     ag : List
#         DESCRIPTION.

#     Returns
#     -------
#     max_distance : TYPE
#         DESCRIPTION.

#     """

#     # Loop through and calculate distances
#     max_distance = 0
#     for i in range(len(ag)):
#         for j in range(i + 1, len(ag)):
#             #print("i", i, "j", j)
#             distance = get_distance(ag[i].x, ag[i].y, ag[j].x, ag[j].y)
#             #print("distance between", a, b, distance)
#             max_distance = max(max_distance, distance)
#             #print("max_distance", max_distance)
#     return max_distance


# def get_distance(x0, y0, x1, y1):
#       """
#       Calculate the Euclidean distance between (x0, y0) and (x1, y1).

#       Parameters
#       ----------
#       x0 : Number
#           The x-coordinate of the first coordinate pair.
#       y0 : Number
#           The y-coordinate of the first coordinate pair.
#       x1 : Number
#           The x-coordinate of the second coordinate pair.
#       y1 : Number
#           The y-coordinate of the second coordinate pair.

#       Returns
#       -------
#       distance : Number
#           The Euclidean distance between (x0, y0) and (x1, y1).
#       """
#       # Calculate the difference in the x coordinates.
#       dx = x0 - x1
#       # Calculate the difference in the y coordinates.
#       dy = y0 - y1
#       # Square the differences and add the squares
#       ssd = (dx * dx) + (dy * dy)
#       # Calculate the square root
#       distance = ssd ** 0.5
#       return distance  



    
            
            
        
    
    