# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 11:01:28 2023

@author: Andy Turner
"""
import random
from matplotlib import pyplot as plt
import time

# Set the pseudo-random seed for reproducibility
random.seed(0)

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

def get_max_distance():
    """
    Calculate and return the maximum distance between all the agents

    Returns
    -------
    max_distance : Number
        The maximum distance betwee all the agents.

    """
    # Loop through and calculate distances
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i + 1, len(agents)):
            #print("i", i, "j", j)
            b = agents[j]
            distance = get_distance(a[0], a[1], b[0], b[1])
            #print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            #print("max_distance", max_distance)
    return max_distance

def get_min_distance():
    """
    Calculate and return the minimum distance between all the agents

    Returns
    -------
    min_distance : Number
        The minimum distance betwee all the agents.

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
    Calculate and return the mean distance between all the agents

    Returns
    -------
    mean_distance : Number
    The mean distance betwee all the agents.
        
    distance : Number
        The distance betwee all the agents.

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
    Calculate and return the standard deviation between all the agents

    Returns
    -------
    std : Number
    The standard distance betwee all the agents.
        
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
    Calculate and return the median distance between all the agents

    Returns
    -------
    median : Number
       The median distance betwee all the agents.

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
    Calculate and return the mode distance between all the agents

    Returns
    -------
    b : TYPE:list
        the mode distance between all the agents.

    K:number
    the most times appeared
    v:number 
    the most appear times
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

def movement(x0,y0):
    """
    Let a point move once in the range of maximum and minimum and y
    
    Parameters
    ----------
    x0 : Number
        x coordinate of one point.
    y0 : Number
        y coordinate of one point.

    Returns
    -------
    x0 : Number
        y coordinate of one point after movement.
    y0 : Number
        y coordinate of one point after movement.

    """
    
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
    # make a constrain    
    if x0 < x_min:
          x0 = x_min
    if y0 < y_min:
          y0 = y_min
    if x0 > x_max:
          x0 = x_max
    if y0 > y_max:
          y0 = y_max
        
        
    return x0,y0

def get_maxAndMinDistace():
    """
    
    calculate the max and min distance at once and compare it with the time that calculate seperately
    Parameters
    ----------
    x0 : Number
        x coordiante.
    y0 : Number
        y coordinate.

    Returns
    -------
    min_distance : Number
        min distance among all agents.
    max_distance : Number
        max distance among all agetns.

    """
    min_distance = 0
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i + 1, len(agents)):
            b = agents[j]
            distance = get_distance(a[0], a[1], b[0], b[1])
            min_distance = min(min_distance, distance)
            max_distance = max(max_distance, distance)      
    return (min_distance,max_distance)
     
# A list to store times of get_max_distance
get_max_distance_run_times = []
# A list to store times of get_min_distance
get_min_distance_run_times = []
# A list to store times of getMaxAndMindistance
get_minAndMaxTimes=[]

#generate a list 
n_agents_range = range(100,1000,100)

#loop to generate list with different  elememtns
for n_agents in n_agents_range:  
    # Initialise agents
    agents = []
    for i in range(n_agents):
        agents.append([random.randint(0, 99), random.randint(0, 99)])
     
    #Record start time to calculate the max distance
    max_start = time.perf_counter()    
    print("Maximum distance between ",n_agents,"all the agents",get_max_distance())
    #Record end time to calculate the max distance
    max_end = time.perf_counter()
    #calculate the running  time to calculate the max distance
    max_run_time = max_end - max_start
    
    
    #Record start time to calculate the min distance
    min_start = time.perf_counter()
    print("Minimum distance between all the agents", get_min_distance())
    #Record end time to calculate the min distance
    min_end = time.perf_counter()
    #calculate the running  time to calculate the min distance
    min_run_time = min_end - min_start
    
    
    
    #Record start time to calculate the max and min distance
    maxAndMinstart = time.perf_counter()    
    print("Maximum distance between ",n_agents,"all the agents",get_maxAndMinDistace())
    #Record end time to calculate the max and min distance
    maxAndMinend = time.perf_counter()
    #calculate the running  time to calculate the max and min distance
    maxAndMinstart_run_time = maxAndMinend - maxAndMinstart
    
    
    #print
    print("Time taken to calculate ",n_agents,"maximum distance", max_run_time )
    print("Time taken to calculate ", n_agents,"minimum distance",min_run_time)
    print("Time taken to calculate ", n_agents,"minimum and maximum distance",maxAndMinstart_run_time)
    
    
    #store the time to generate different number lists
    get_max_distance_run_times.append(max_run_time)
    get_min_distance_run_times.append(min_run_time)
    get_minAndMaxTimes.append(maxAndMinstart_run_time)
    
    

# Plot to show time of get max distance 
plt.title("Time taken to calculate maximum distance for different numbers of agent")
#Set the coordinate name
plt.xlabel("Number of agents")

plt.ylabel("Time")

#loop to get the x coordinate and y coordinate
j = 0
for i in n_agents_range:
    plt.scatter(i, get_max_distance_run_times[j], color='blue')
    j = j + 1
plt.show()


#Plot to show time of get min distance 
plt.title("Time taken to calculate minimum distance for different numbers of agent")
plt.xlabel("Number of agents")
plt.ylabel("Time")
j = 0
for i in n_agents_range:
    plt.scatter(i, get_min_distance_run_times[j], color='red')
    j = j + 1
plt.show()

#Plot to show time of get min and max distance 
plt.title("Time taken to calculate minimum and maximum distance for different numbers of agent")
plt.xlabel("Number of agents")
plt.ylabel("Time")
j = 0
for i in n_agents_range:
    plt.scatter(i, get_minAndMaxTimes[j], color='purple')
    j = j + 1
plt.show()




#movement
#change coordinates
#print(agents)

#make constrains and generate list
list1=[]
for i in range(20):
    list1.append([random.randint(0, 99), random.randint(0, 99)])
#plot point before move 
print("before move")   
print(list1)


# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.
y_max = 99

#Move the point for 1000 times
n_iterations = 1000
for j in range(n_iterations):
    for i in range(len(list1)):
        list1[i][0],list1[i][1] = movement(list1[i][0],list1[i][1]) 
      
print("after move")        
#plot point after move             
print(list1)


print("this is a test")