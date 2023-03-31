# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:17:07 2023

@author: yang
"""


import csv



def read_data():
    """
    # Read input data

    Returns
    -------
    data : list
        the list that store the value of row
    n_cols : Number
        cols of environemnt.
    n_rows : Number
        rows of environemnt.
       rows of environemnt.
    """
    f = open('../../data/input/in.txt', newline='')
    data = []
    #Iterate through the file to get all rows and columns
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
        #print(value)
        data.append(row)
    f.close()
    n_cols = len(data)
    n_rows = len(row)
    return data, n_cols, n_rows

def write_data(file_path, environment):
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(environment)




  
