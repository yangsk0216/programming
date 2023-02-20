import random
import matplotlib
from matplotlib import pyplot as plt
import operator
"""
agents = []
# Initialise variable x0
x0 = random.randint(0, 99)
print("x0", x0)
# Initialise variable y0
y0 = random.randint(0, 99)
print("y0", y0)
agents.append([x0, y0])

# Initialise variable x1
x1 = random.randint(0, 99)
print("x1", x1)
# Initialise variable y0
y1 = random.randint(0, 99)
print("y1", y1)
agents.append([x1, y1])
"""

agents = []
n_agents = 1000
for i in range(100):
    agents.append([random.randint(0, 99), random.randint(0, 99)])

# Plot the agents
for i in range(100):
    
    plt.scatter(agents[i][0], agents[i][1], color='black')

# Get the coordinates with the largest x-coordinate
# Get the coordinates with the smallest x-coordinate
# Get the coordinates with the largest y-coordinate
# Get the coordinates with the smallest y-coordinate

print(max(agents, key=operator.itemgetter(0)))

agents_max_x=(max(agents, key=operator.itemgetter(0)))
agents_min_x=(min(agents, key=operator.itemgetter(0)))
agents_max_y=(max(agents, key=operator.itemgetter(1)))
agents_min_y=(min(agents, key=operator.itemgetter(1)))

plt.scatter(agents_min_x[0],agents_min_x[1],color="blue")
plt.scatter(agents_max_x[0],agents_max_x[1],color="red")
plt.scatter(agents_max_y[0],agents_max_y[1],color="yellow")
plt.scatter(agents_min_y[0],agents_min_y[1],color="green")

plt.show()



