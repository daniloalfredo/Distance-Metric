# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from random import randint

import KModes as K
import Distances as Dist

#MAIN

#DataSet info
dataSet = pd.read_csv('Datasets/Soybean/soybean-small.csv')
rows,cols = dataSet.shape
dataSet = dataSet.iloc[:, range(cols-1)]
numClusters = 4
DistType = 'DM2'
numero_iteracoes = 5

#
for i in range(0,cols-1):
    dataSet.iloc[:, i] = dataSet.iloc[:, i].astype('category') #Transforma os dados para a representação categórica do Pandas


'''#Executa o K-Modes com os parametros acima
kmode = K.K_Modes(numClusters, DistType, num_iter=numero_iteracoes)
print "Clustering Soybean..."
kmode.cluster(dataSet)

kmode.displayClusters(dataSet)'''

PS,R,Beta = Dist.preDM3(dataSet)

'''indA = randint(0, rows)
indB = randint(0, rows)    

A = dataSet.iloc[indA,:]
B = dataSet.iloc[indB,:]

PS = Dist.preDM2(dataSet)

print 'Distância DM1 entre objeto ' + str(indA) + ' e objeto ' + str(indB) + ' = ' + str(Dist.DM1(A, B, dataSet))

print 'Distância DM2 entre objeto ' + str(indA) + ' e objeto ' + str(indB) + ' = ' + str(Dist.DM2(A, B, PS, dataSet))

print 'Distância Hamming entre objeto ' + str(indA) + ' e objeto ' + str(indB) + ' = ' + str(Dist.Hamming_Distance(A, B))'''