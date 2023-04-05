import random
import matplotlib
from matplotlib import pyplot as plt
import operator
import math

# Set the pseudo-random seed for reproducibility
random.seed(0)


# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4
x0 = 0
y0 = 0
x1 = 3
y1 = 4
# Calculate the difference in the x coordinates.
dx = x0 - x1
# Calculate the difference in the y coordinates.
dy = y0 - y1
# Square the differences and add the squares
ssd = (dx * dx) + (dy * dy)
print("ssd", ssd)
# Calculate the square root
distance = ssd ** 0.5
print("distance", distance)
distance = math.sqrt(ssd)
print("distance", distance)

# agents = []
# # Initialise variable x0
# x0 = random.randint(0, 99)
# print("x0", x0)
# # Initialise variable y0
# y0 = random.randint(0, 99)
# print("y0", y0)
# agents.append([x0, y0])

# # Initialise variable x1
# x1 = random.randint(0, 99)
# print("x1", x1)
# # Initialise variable y0
# y1 = random.randint(0, 99)
# print("y1", y1)
# agents.append([x1, y1])

# plt.show()
# # Get the coordinates with the largest x-coordinate
# print(max(agents, key=operator.itemgetter(0)))
# print(max(agents, key=operator.itemgetter(1)))



# Create a list to store agents
agents = []
#create  agents that have 100 list
n_agents = 100
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
print("before move")   
print(agents)
# Plot the agents
for i in range(100):  
    plt.scatter(agents[i][0], agents[i][1], color='black')
    
# Move agents
for i in range(n_agents):
    # Change agents[i] x-coordinate randomly
   
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1
    # Change agents[i] y-coordinate randomly
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][1] - 1
        
print("after move")         
print(agents)

# Plot the agents after move:
for i in range(n_agents):    
    plt.scatter(agents[i][0], agents[i][1], color='purple')


#print the point with the max x value afer move
print("max x")
print(max(agents, key=operator.itemgetter(0)))

# Get the coordinates with the largest x-coordinate afer move
agents_max_x=(max(agents, key=operator.itemgetter(0)))
# Get the coordinates with the smallest x-coordinate afer move
agents_min_x=(min(agents, key=operator.itemgetter(0)))
# Get the coordinates with the largest y-coordinate afer move
agents_max_y=(max(agents, key=operator.itemgetter(1)))
# Get the coordinates with the smallest y-coordinate afer move
agents_min_y=(min(agents, key=operator.itemgetter(1)))


#plot the point with the smallest x-coordinate afer move
plt.scatter(agents_min_x[0],agents_min_x[1],color="blue")
#plot the point with the largest x-coordinate afer move
plt.scatter(agents_max_x[0],agents_max_x[1],color="red")
#plot the point with the largest y-coordinate afer move
plt.scatter(agents_max_y[0],agents_max_y[1],color="yellow")
#plot the point with the smallest y-coordinate afer move
plt.scatter(agents_min_y[0],agents_min_y[1],color="green")

#plot
plt.show()




