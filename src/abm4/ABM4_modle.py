# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:10:53 2023

@author: yang
"""
import timing2 as tm2
import agentframework as af
import operator
from matplotlib import pyplot as plt
import random

x_min=0
x_max=99
y_min=0
y_max=99
random.seed(0)
# Initialise agents
agents = []
n_agents = 100
for i in range(n_agents):
    # Create an agent
   agents.append(af.Agent(i))
   plt.scatter(agents[i].x,agents[i].y, color='green')
   print(agents[i])
   print(agents)
   agents[i].move(x_min, y_min, x_max, y_max)      
   plt.scatter(agents[i].x,agents[i].y, color='red')  

a = af.Agent(101)
b = af.Agent(102)

print(a,b)
distance = tm2.get_max_distance(agents)
print(distance)


# Plot the coordinate with the largest x red
lx = max(agents, key=operator.attrgetter('x'))
plt.scatter(lx.x, lx.y, color='black')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.attrgetter('x'))
plt.scatter(sx.x, sx.y, color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.attrgetter('y'))
plt.scatter(ly.x, ly.y, color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.attrgetter('y'))
plt.scatter(sy.x, sy.y, color='pink')

  