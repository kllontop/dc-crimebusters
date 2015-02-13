# -*- coding: utf-8 -*-
"""
Created on Sat Feb 07 08:49:40 2015

@author: andrew_woizesko

Parsing metro data
"""


import csv 

infile = r'C:\Users\andrew_woizesko\Documents\Georgetown Data Science\Capstone\Data\HistoricalRidershipToParse.txt'
outfile = r'C:\Users\andrew_woizesko\Documents\Georgetown Data Science\Capstone\Data\ParsedRidershipData.csv'

def create_row(in_line, template_row):
    clean_row = ['' for item in template_row]
    stripLine = in_line.strip().replace('-', " ")
    split_line = stripLine.split(" ")
    reverse = lambda x: (x)*-1 #used to inverse the list index
    index = [reverse(x) for x in range(len(split_line))]
    for item in index:
        try:
            clean_row[item] = split_line[item]
        except IndexError:
            continue
    print clean_row
    return clean_row
        

with open(infile) as data:
    headers = data.readline()
    headers = headers.strip()
    split_headers = headers.split(' ')
    split_headers.insert(1,"")
    with open(outfile, 'wb') as target:
        writer = csv.writer(target)
        writer.writerow(split_headers)
        riders = data.read()
        rows = riders.split('\n')
        for line in rows:
            new_row = create_row(line, split_headers) #function to fill a row skeleton
            writer.writerow(new_row)
    