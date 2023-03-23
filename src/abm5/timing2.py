
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 11:01:28 2023

@author: Andy Turner
"""
import random
from matplotlib import pyplot as plt
import time

# Set the pseudo-random seed for reproducibility


# A variable to store the number of agents
#n_agents = 500

def get_distance(x0, y0, x1, y1):
    """
    Calculate the Euclidean distance between (x0, y0) and (x1, y1).

    Parameters
    ----------
    x0 : Number
        The x-coordinate of the first coordinate pair.
    y0 : Number
        The y-coordinate of the first coordinate pair.
    x1 : Number
        The x-coordinate of the second coordinate pair.
    y1 : Number
        The y-coordinate of the second coordinate pair.

    Returns
    -------
    distance : Number
        The Euclidean distance between (x0, y0) and (x1, y1).
    """
    # Calculate the difference in the x coordinates.
    dx = x0 - x1
    # Calculate the difference in the y coordinates.
    dy = y0 - y1
    # Square the differences and add the squares
    ssd = (dx * dx) + (dy * dy)
    # Calculate the square root
    distance = ssd ** 0.5
    return distance

def get_max_distance(ag):
    """
    
    Calculate the max distance among different agents
    
    Parameters
   
    max_distance : number
        the max distance among different agents

    """

    # Loop through and calculate distances
    max_distance = 0
    for i in range(len(ag)):
        for j in range(i + 1, len(ag)):
            #print("i", i, "j", j)

            distance = get_distance(ag[i].x, ag[i].y, ag[j].x, ag[j].y)
            #print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            #print("max_distance", max_distance)
    return max_distance

def get_min_distance():
    """
    
    Calculate the min distance among different agents
    
    Parameters
   
    min_distance : number
        the min distance among different agents

    """
    
    min_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i + 1, len(agents)):
            #print("i", i, "j", j)
            b = agents[j]
            distance = get_distance(a[0], a[1], b[0], b[1])
            #print("distance between", a, b, distance)
            min_distance = min(min_distance, distance)
            #print("max_distance", max_distance)
    return min_distance

def get_mean_distance():
    """
    Calculate the mean distance among different agents

    Returns
    -------
    mean_distance : number
        the mean distance among different agents.
    distance : number
        the  distance among different agents.

    """
  
    
    distance=[]
    for i in range(len(agents)):
        for j in range(i+1,len(agents)):
            a=get_distance(agents[i][0],agents[i][1],agents[j][0],agents[j][1])
            distance.append(a)
    mean_distance= sum(distance)/len(distance)
    return mean_distance,distance

def get_standard_deviation():
    """
    Calculate the standard distance among different agents

    Returns
    -------
    std : number
        the standard distance among different agents.
   

    """
  
    
    mean,distance=get_mean_distance()
    #The sum of the squares of the difference between each value and the mean
    sqrSum = 0
    for i in range(len(distance)):
        sqrSum=(distance[i] - mean)**2 + sqrSum
    #print(sqrSum)   
    std = (sqrSum/(len(distance)-1))**0.5
    return std

def get_median():
    """
    Calculate the median distance among different agents

    Returns
    -------
    median : number
        the median distance among different agents.
   

    """
    a, distance = get_mean_distance()
    
    distance.sort()
    if len(distance) % 2 == 0:
        median=(distance[len(distance)//2]+distance[len(distance)//2+1])/2
    else:
        median=distance[len(distance)//2+1]
    return median
    
  

def get_mode():
    """
    Calculate the mode distance and the times it appears among different agents

    Returns
    -------
    b : list
        store the times 'v' appearing and the distance 'k'
   

    """
    
    a, distance = get_mean_distance()
    #new dictionary  
    zidian = {} 
    b= []
    for i in distance:
        if i in zidian: 
            zidian[i] += 1
        else:
            zidian[i] = 1 
    for k,v in zidian.items():
        if v == max(zidian.values()):
            b.append((k,v))
    return b
# move the point randomly
def movement(x0,y0):
    
   
    #print(agents)
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
    return x0,y0
    

# A list to store times of get_max_distance
get_max_distance_run_times = []
# A list to store times of get_min_distance
get_min_distance_run_times = []

#creat a list that store elelemts to generaate
n_agents_range = range(100,1000,100)



for n_agents in n_agents_range:
    
    # Initialise agents
    agents = []
    #for i in range(n_agents):
        #agents.append([random.randint(0, 99), random.randint(0, 99)])
        
    print("Maximum distance between all the agents", get_max_distance(agents))
   #record the time for start to get maxdistance
    max_start = time.perf_counter()
    #record the time for end to get max distance
    max_end = time.perf_counter()
    #calculate the runnning time for getting max distance
    max_run_time = max_end - max_start
    #record the time for start to get min distance
    min_start = time.perf_counter()
    print("Minimum distance between all the agents", get_min_distance())
    #record the time for end to get min distance
    min_end = time.perf_counter()
    #calculate the runnning time for getting min distance
    min_run_time = min_end - min_start
        
    print("Time taken to calculate maximum distance", max_run_time )
    print("Time taken to calculate minimum distance", min_run_time)
    #Store in a list the number of different times the maximum distance is calculated
    get_max_distance_run_times.append(max_run_time)
    #Store in a list the number of different times the minimum distance is calculated
    get_min_distance_run_times.append(min_run_time)
    
    mean,distance= get_mean_distance()
    #print("mean distance between all the agents",mean)
    #print("median distance between all the agents",get_median())
    #print("std distance between all the agents", get_standard_deviation())
    #print("get_mode distance between all the agents", get_mode())

# Plot to show time of get max distance time
plt.title("Time taken to calculate maximum distance for different numbers of agent")
plt.xlabel("Number of agents")
plt.ylabel("Time")

#Iterate through the array to determine the xy coordinates to draw the map of max distance
j = 0
for i in n_agents_range:
    plt.scatter(i, get_max_distance_run_times[j], color='black')
    j = j + 1
plt.show()

# Plot to show time of get min distance time
plt.title("Time taken to calculate minimum distance for different numbers of agent")
plt.xlabel("Number of agents")
plt.ylabel("Time")

#Iterate through the array to determine the xy coordinates to draw the map of min distance
j = 0
for i in n_agents_range:
    plt.scatter(i, get_min_distance_run_times[j], color='black')
    j = j + 1
plt.show()



#movement
#change coordinates
#print(agents)

#make constrains
list1=[]
for i in range(20):
    list1.append([random.randint(0, 99), random.randint(0, 99)])
print(list1)
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.
y_max = 99
n_iterations = 1000

#Iterate through the array and then move it 1000 times with restrictions
for j in range(n_iterations):
    for i in range(len(list1)):
        list1[i][0],list1[i][1]= movement(list1[i][0],list1[i][1]) 
        # Apply movement constraints.
        if list1[i][0] < x_min:
             list1[i][0] = x_min
        if list1[i][1] < y_min:
             list1[i][1] = y_min
        if list1[i][0] > x_max:
             list1[i][0] = x_max
        if list1[i][1] > y_max:
             list1[i][1] = y_max
print(list1)

