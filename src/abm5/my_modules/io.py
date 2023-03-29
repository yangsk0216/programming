# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:17:07 2023

@author: yang
"""


import csv


# Read input data
def read_data():
    """
    

    Returns
    -------
    data : list
        list to store the number of cols.
    n_cols : number
       number of cols.
    n_rows : number
        list to store the number of rows.
    number of rows.
    """
    f = open('../../data/input/in.txt', newline='')
    data = []
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
    




  
