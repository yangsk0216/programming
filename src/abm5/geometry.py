# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 00:42:37 2023

@author: yang
"""

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