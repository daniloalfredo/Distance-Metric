# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from random import randint

import KModes as K
import Distances as Dist
import cPickle as pickle

#MAIN
#Essa seção do código calcula as distâncias intra e inter-clusters
#dataSet = pd.read_csv('Datasets/Congress/house-votes-84.csv')
dataSet = pd.read_csv('Datasets/Car/car.csv')
#dataSet = pd.read_csv('Datasets/Soybean/soybean-small.csv')
rows,cols = dataSet.shape
dataSet = dataSet.iloc[:, range(cols-1)]
for i in range(0,cols-1):
    dataSet.iloc[:, i] = dataSet.iloc[:, i].astype('category') #Transforma os dados para a representação categórica do Pandas

with open('Car_clusters.pkl', 'rb') as input:
	Car = pickle.load(input)

Car.getResults(dataSet)





#Essa outra seção calcula os clusters de uma determinada base de dados e salva num arquivo

'''#DataSet info
dataSet = pd.read_csv('Datasets/Congress/house-votes-84.csv')
rows,cols = dataSet.shape
dataSet = dataSet.iloc[:, range(1,cols)]
numClusters = 2
DistType = 'Hamming'
numero_iteracoes = 5

#
for i in range(0,cols-1):
    dataSet.iloc[:, i] = dataSet.iloc[:, i].astype('category') #Transforma os dados para a representação categórica do Pandas


#Executa o K-Modes com os parametros acima
kmode = K.K_Modes(numClusters, DistType, num_iter=numero_iteracoes)
print "Clustering Congress..."
kmode.cluster(dataSet)

#kmode.displayClusters(dataSet)

with open ('Congress_clusters_Hamming.pkl', 'wb') as output:
	pickle.dump(kmode, output, -1)'''
