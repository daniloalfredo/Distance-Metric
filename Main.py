# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from random import randint

import KModes as Kmodes
import Distances as Dist

#MAIN
dataSet = pd.read_csv('Datasets/Mushroom/agaricus-lepiota.csv')
rows = dataSet.shape[0]
cols = dataSet.shape[1]

for i in range(0,cols):
    dataSet.iloc[:, i] = dataSet.iloc[:, i].astype('category') #Transforma os dados para a representação categórica do Pandas

indA = randint(0, rows)
indB = randint(0, rows)    

A = dataSet.iloc[indA,:]
B = dataSet.iloc[indB,:]

print 'Distância de Hamming entre objeto ' + str(indA) + ' e objeto ' + str(indB) + ' = ' + str(Dist.Hamming_Distance(A, B))
