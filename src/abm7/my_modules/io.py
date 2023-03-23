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
    data : LIST
        Store a list of values within a row
    n_cols : Number
        cols.
    n_rows : Number
        rows.

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
#Iterate over the data of data and write it to csv
def write_data(address,data):
    f = open(address, 'w', newline = '')
    writer = csv.writer(f, delimiter = ',')
    for row in data:
        writer.writerow(row)
    f.close()    




  
