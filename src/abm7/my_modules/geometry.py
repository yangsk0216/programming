# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 08:43:00 2023

@author: yang
"""
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
