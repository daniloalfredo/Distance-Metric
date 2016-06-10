# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 16:31:13 2016

@author: danilo.souza
"""

import numpy as np
import pandas as pd
from random import randint

#Função de Distância Hamming
def Hamming_Distance(InstanceA, InstanceB):
	buliano = InstanceA != InstanceB
	return buliano.sum()

#Função genérica de distância entre dados categóricos
def Get_Distance(InstanceA, InstanceB, DistType):
	if DistType == 'Hamming':
		return Hamming_Distance(InstanceA, InstanceB)
	else:
		return 'Distance not found'

#Algoritmo de clustering K-Modes
#Parâmetros:
#DataSet --> Base de dados. DEVE SER um DataFrame (Pandas) e os atributos devem ser do tipo CATEGORY
#numClusters --> Número de agrupamentos que o algoritmo deve criar. Valor default é 0, o que significa que o algoritmo tentará detectar automaticamente o número de clusters
#DistType --> A medida de distância que será utilizada. Opções:
	#Hamming -> Distância de Hamming
	#VDM
	#Ahmad --> Métrica de Ahmad [12]
	#Association -> Association-Based Distance Metric[5]
	#Context -> Context-Based Distance Metric [13][14]
	#DM -> Novo método proposto
def K_Modes(DataSet, numClusters = 0, DistType):
	clusters = [[]]*numClusters #Lista de listas. Cada lista representa um cluster, que contém os índices dos objetos do DataSet
	newClusters = [[]]*numClusters

	


#MAIN
dataSet = pd.read_csv('Datasets/Mushroom/agaricus-lepiota.csv')
rows = dataSet.shape[0]

for i in range(0,dataSet.shape[1]):
    dataSet.iloc[:, i] = dataSet.iloc[:, i].astype('category')

indA = randint(0, rows)
indB = randint(0, rows)    

A = dataSet.iloc[indA,:]
B = dataSet.iloc[indB,:]

print 'Distância de Hamming entre objeto ' + str(indA) + ' e objeto ' + str(indB) + ' = ' + str(Hamming_Distance(A, B))




    
    
    
