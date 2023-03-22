# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:10:53 2023

@author: yang
"""
import imageio
import os
import operator
from matplotlib import pyplot as plt
import random
import my_modules.agentframework as af
import my_modules.io as io

random.seed(3)

def get_max_distance(ag):
    """
    
    Parameters
    ----------
    ag : List
        DESCRIPTION.

    Returns
    -------
    max_distance : TYPE
        DESCRIPTION.

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

if __name__ == '__main__':
    #gain the value of environment,n_cols, n_rows
    environment,n_cols, n_rows = io.read_data()

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
    #genreate agetns
    for i in range(n_agents):
        agents.append(af.Agent(agents, i, environment, n_rows, n_cols))
    
    for ite in range(n_iterations):
        print("Iteration", ite)
        # Move agents
        print("Move")
        for i in range(n_agents):
            agents[i].move(x_min, y_min, x_max, y_max)
            agents[i].eat()
            #print(agents[i])
        # Share store
        # Distribute shares
        for i in range(n_agents):
            agents[i].share(neighbourhood)
        # Add store_shares to store and set store_shares back to zero
        for i in range(n_agents):
            print(agents[i])
            agents[i].store = agents[i].store_shares
            agents[i].store_shares = 0
        print(agents)
        # Print the maximum distance between all the agents
        print("Maximum distance between all the agents", get_max_distance(agents))
        # Print the total amount of resource
        sum_as = af.sum_agent_stores(agents)
        print("sum_agent_stores", sum_as)
        sum_e = af.sum_environment(environment)
        print("sum_environment", sum_e)
        print("total resource", (sum_as + sum_e))
        
        #difine the plot limits
        plt.ylim(y_min, y_max)
        plt.xlim(x_min, x_max)
        # plt.ylim(y_max/3,y_max*2/3)
        # plt.xlim(x_max/3,x_max*2/3)
         
        plt.imshow(environment)
        
        for a in agents:
            plt.scatter(a.x,a.y, color='blue')

        # Plot the coordinate with the largest x black
        lx = max(agents, key=operator.attrgetter('x'))
        plt.scatter(lx.x, lx.y, color='black')
        # Plot the coordinate with the smallest x red
        sx = min(agents, key=operator.attrgetter('x'))
        plt.scatter(sx.x, sx.y, color='red')
        # Plot the coordinate with the largest y yellow
        ly = max(agents, key=operator.attrgetter('y'))
        plt.scatter(ly.x, ly.y, color='yellow')
        # Plot the coordinate with the smallest y pink
        sy = min(agents, key=operator.attrgetter('y'))
        plt.scatter(sy.x, sy.y, color='pink')



        filename = '../../data/output/images/image' + str(ite) + '.png'
        #filename = '../../data/output/images/image' + str(ite) + '.gif'
        plt.savefig(filename)
        plt.show()
        plt.close()
        images.append(imageio.imread(filename))
        # turned into an animated gif file
    imageio.mimsave('../../data/output/out.gif', images, fps=3)

   
       
       




