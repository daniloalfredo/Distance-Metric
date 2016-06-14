# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from random import randint

import KModes as K
import Distances as Dist
import cPickle as pickle

#MAIN

#DataSet info
dataSet = pd.read_csv('Datasets/Soybean/soybean-small.csv')
rows,cols = dataSet.shape
dataSet = dataSet.iloc[:, range(cols-1)]
numClusters = 4
DistType = 'DM3'
numero_iteracoes = 5

#
for i in range(0,cols-1):
    dataSet.iloc[:, i] = dataSet.iloc[:, i].astype('category') #Transforma os dados para a representação categórica do Pandas


#Executa o K-Modes com os parametros acima
kmode = K.K_Modes(numClusters, DistType, num_iter=numero_iteracoes)
print "Clustering Soybean..."
kmode.cluster(dataSet)

kmode.displayClusters(dataSet)

with open ('Soybean_clusters.pkl', 'wb') as output:
	pickle.dump(kmode, output, -1)