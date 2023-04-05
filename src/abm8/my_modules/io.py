# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:17:07 2023

@author: yang
"""


import csv


# Read input data
def read_data():
    #open file
    f = open('../../data/input/in.txt', newline='')
    #make a Two-dimensional list
    data = []
    #The module parses each row of data into a list of strings and then converts each string to a floating point number
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
        #print(value)
        #add the data to row
        data.append(row)
    f.close()
    #the number of rows and rows
    n_cols = len(data)
    n_rows = len(row)
    return data, n_cols, n_rows

#Iterate over the data of data and write it to csv
def write_data(address,data):
    #open file,No special line feed handling is required.
    f = open(address, 'w', newline = '')
    #Write each line to a CSV file
    writer = csv.writer(f, delimiter = ',')
    for row in data:
        #Writing line by line
        writer.writerow(row)
    f.close()    




  
