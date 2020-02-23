# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:08:39 2020

@author: gargargargar
"""

import numpy as np
import pandas as pd
import csv
import pprint


# Sorting key for df in analyze()
def getKey(item):
    return abs(item[1])

# "Main" analysis method
def analyze(datasetFilename, outputFilename):
    
    happinessDf = pd.read_csv(datasetFilename)
    happinessDf = happinessDf['Happiness Score']
    
    df = pd.read_csv(datasetFilename)
    
    df = df.drop(['Country', 'Happiness Score'], axis = 1)
    
    result = []
    for col in df.columns:
        result.append((col, happinessDf.corr(df[col])))
    result = sorted(result, key = getKey)
    result.reverse()
    
    
    with open(outputFilename, 'w',
              newline='') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['characteristic','correlation'])
        for row in result:
            csv_out.writerow(row)


# Main method
def main():
    analyze('../datasets/dataset-threshold-20.csv',
            'correlation-ranking-by-characteristic.csv')

if __name__ == '__main__':
    main()