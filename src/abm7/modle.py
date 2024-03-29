# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:10:53 2023

@author: yang
"""
import matplotlib.animation as anim
import imageio
import os
import operator
from matplotlib import pyplot as plt
import random
import my_modules.agentframework as af
import my_modules.geometry as geo
import my_modules.io as io
random.seed(0)

def plot():
    print(2)
    fig.clear()
    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)
    plt.imshow(environment)
    for i in range(n_agents):
        plt.scatter(agents[i].x, agents[i].y, color='black')
    # Plot the coordinate with the largest x red
    lx = max(agents, key=operator.attrgetter('x'))
    plt.scatter(lx.x, lx.y, color='red')
    # Plot the coordinate with the smallest x blue
    sx = min(agents, key=operator.attrgetter('x'))
    plt.scatter(sx.x, sx.y, color='blue')
    # Plot the coordinate with the largest y yellow
    ly = max(agents, key=operator.attrgetter('y'))
    plt.scatter(ly.x, ly.y, color='yellow')
    # Plot the coordinate with the smallest y green
    sy = min(agents, key=operator.attrgetter('y'))
    plt.scatter(sy.x, sy.y, color='green')
    global ite
    #define the output address and save the generated image
    filename = '../../data/output/images/image' + str(ite) + '.png'
    plt.savefig(filename)
    plt.show
    #Saving metadata to a list
    images.append(imageio.imread(filename))
    return fig

def gen_function():
    # return iterator to update, determine the number of update cycles
    global ite
    ite = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (ite < n_iterations) & (carry_on) :
        print(0)
        yield ite # Returns control and waits next call.
        print(3)
        ite = ite + 1
    global data_written
    if data_written == False:
        print(4)
        # Write data
        print("write data")
        # Write to file and generate animation at the end of the loop
        io.write_data('../../data/output/out7.txt', environment)
        imageio.mimsave('../../data/output/out7.gif', images, fps=3)
        data_written = True
      
def update(frames):
    print(1)
    # Model loop
    global carry_on
    #for ite in range(n_iterations):
    print("Iteration", frames)
    # Move agents
    print("Move and eat")
    for i in range(n_agents):
        agents[i].move(x_min, y_min, x_max, y_max)
        agents[i].eat()
        #print(agents[i])
    # Share store
    print("Share")
    # Distribute shares
    for i in range(n_agents):
        agents[i].share(neighbourhood)
    # Add store_shares to store and set store_shares back to zero
    for i in range(n_agents):
        #print(agents[i])
        agents[i].store = agents[i].store_shares
        agents[i].store_shares = 0
    #print(agents)
    # Print the maximum distance between all the agents
    print("Maximum distance between all the agents", geo.get_max_distance(agents))
    # Print the total amount of resource
    sum_as =sum_agent_stores(agents)
    print("sum_agent_stores", sum_as)
    sum_e = sum_environment(environment)
    print("sum_environment", sum_e)
    print("total resource", (sum_as + sum_e))

    # Stopping condition
    # Random
    #if random.random() < 0.1: 
    if sum_as / n_agents > 80:
        carry_on = False
        print("stopping condition")

    # Plot
    global ite
    #Draw a diagram at the end of each
    plot()
    #ite = ite + 1
    
    
#difine the function that add all the value in the environemnt    
def sum_environment(environment):
    """
    #Calculates the sum of all values in the environment variable

    Parameters
    ----------
    environment : LIST
        basemap

    Returns
    -------
    sum_environment : Number
        The sum of all values in the environment

    """
    sum_environment = 0
    for i in range(len(environment)):
        for j in range(len(environment[i])):
            sum_environment += environment[i][j]
    return sum_environment


#difine the function that add all the value stored  
def sum_agent_stores(agents):
    """
    Calculates the sum of all values that stored
    Parameters
    ----------
    agents : LIST
       Store the coordinates of the object

    Returns
    -------
    sum_agent_stores : Number
        sum of all values that stored

    """
    sum_agent_stores = 0
    for i in range(len(agents)):
        sum_agent_stores += agents[i].store
    return sum_agent_stores
        
  

if __name__ == '__main__':
    environment,n_cols, n_rows = io.read_data()
#difine the x y limits
    x_min=0
    x_max = n_cols - 1
    y_min=0
    y_max = n_rows - 1

    # Initialise agents
    agents = []


    # Model loop

    n_agents = 10
    n_iterations = 10
    neighbourhood = 10
    
    # Create directory to write images to.
    try:
        os.makedirs('../../data/output/images/')
    except FileExistsError:
        print("path exists")

    # For storing images
    global ite
    ite = 0
    images = []
    
    for i in range(n_agents):
        #difine agents
        agents.append(af.Agent(agents, i, environment, n_rows, n_cols))
    # Animate
    # Initialise fig and carry_on
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_axes([0, 0, 1, 1])
    carry_on = True
    data_written = False
    animation = anim.FuncAnimation(fig, update, init_func=plot, frames= gen_function, repeat=False)
       
       
'''
        plt.ylim(y_max/3,y_max*2/3)
        plt.xlim(x_max/3,x_max*2/3)
         
        plt.imshow(environment)
        
        for a in agents:
            plt.scatter(a.x,a.y, color='blue')


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



        filename = '../../data/output/images/image' + str(ite) + '.png'
        #filename = '../../data/output/images/image' + str(ite) + '.gif'
        plt.savefig(filename)
        plt.show()
        plt.close()
        images.append(imageio.imread(filename))
    imageio.mimsave('../../data/output/out.gif', images, fps=3)

    #interaction = 1000
'''

        # Create an agent
       #agents.append(af.Agent(agents, i, environment, n_rows, n_cols))
       #plt.scatter(agents[i].x,agents[i].y, color='green')
       #print(agents)
       #for j in range(interaction):
           #agents[i].move(x_min, y_min, x_max, y_max)   
           #agents[i].eat()
           
       #plt.scatter(agents[i].x,agents[i].y, color='red')  
       
       




