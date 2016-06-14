# -*- coding: utf-8 -*-

"""
Created on Fri Jun 03 16:31:13 2016

@author: danilo.souza
"""

import numpy as np
import pandas as pd
from random import sample
import Distances as Dist
import csv

class K_Modes:
	"""Classe K-Modes
	Atributos:
		DataSet --> Base de dados. DEVE SER um DataFrame (Pandas) e os atributos devem ser do tipo CATEGORY
		numClusters --> Número de agrupamentos que o algoritmo deve criar.
		init --> Como inicializar os centróides. Padrão é aleatoriamente
		runs --> Número de vezes que o K-Modes deve ser rodado com seeds diferentes, o resultado final é o melhor resultado entre todas as runs 
		DistType --> A medida de distância que será utilizada. Opções:
			Hamming -> Distância de Hamming
			VDM
			Ahmad --> Métrica de Ahmad [12]
			Association -> Association-Based Distance Metric[5]
			Context -> Context-Based Distance Metric [13][14]
			DM1 -> Primeira versão do novo método proposto
			DM2 -> Segunda versão do novo método	
			DM3 -> Versão completa do novo método
		centroids --> Auto-explicativo, são as centroides de cada cluster encontrado
		clusters --> Os objetos pertencentes a cada cluster
		c_distance --> Distâncias intra e inter-clusters (matriz)

	Métodos:
	__init__ --> construtor
	reset_Att --> Permite ao usuário inserir novos atributos
	Seed_Init --> Inicializa as centroides 
	cluster --> Recebe um DataSet e performa o agrupamento de acordo com seus atributos
	randInit --> Método aleatório de inicialização de centroides
	"""

	def __init__(self, numClusters, DistType, num_iter=100, init='random', runs=1):
		self.numClusters = numClusters
		self.DistType = DistType
		self.num_iter = num_iter
		self.init = init
		self.runs = runs
		return

	def reset_Att(self, numClusters, DistType, num_iter=100, init='random', runs=1):
		self.numClusters = numClusters
		self.DistType = DistType
		self.num_iter = num_iter
		self.init = init
		self.runs = runs
		return

	def Seed_Init(self, DataSet):
		if (self.init == 'random'):
			self.centroids = self.randInit(DataSet)
		else:
			print 'No such method'
		indexList = self.centroids.index.tolist() #Pega a lista dos índices de cada centroide no dataSet
		self.clusters = [indexList[i:i+1] for i in range (0,len(indexList))] #cria uma lista de listas, cada sublista é um cluster, que contém os índices no DataSet dos padrões que pertencem ao cluster
		self.centroids.index = range(self.centroids.shape[0]) #Modificação estética, renomeia as linhas dos centróides
		return

	def randInit(self, DataSet):
		rows,cols = DataSet.shape
		index = sample(range(0,rows), self.numClusters) #cria um array de numClusters elementos aleatórios
		return DataSet.iloc[index,:] #pega os padrões correspondentes aos índices aleatórios

	def cluster(self, DataSet):
		rows,cols = DataSet.shape
		PS = []
		R = []
		Beta = 0
		self.Seed_Init(DataSet)
		if(self.DistType == 'DM2'):
			PS = Dist.preDM2(DataSet)
		elif(self.DistType == 'DM3'):
			print "Calculando R, PS e Beta..."
			PS, R, Beta = Dist.preDM3(DataSet)
		for it in range(self.num_iter):
			newClusters = [[] for i in range (self.numClusters)]
			#agrupa os padrões de acordo com os centroides
			print "iteracao " + str(it+1)
			for i in range(rows): 
				A = DataSet.iloc[i,:] 
				dist = []
				#calcula uma lista de distâncias entre o padrão A e cada centroide
				for j in range(self.numClusters):
					B = self.centroids.iloc[j,:]
					dist.append(Dist.GetDistance(A, B, self.DistType, DataSet, PS, R, Beta)) 
				#O padrão A é inserido no cluster do centroide que der a menor distância
				minInd = np.argmin(dist)
				newClusters[minInd].append(i)

			#Re-calcula os centroides
			for k in range(self.numClusters):
				cluster = DataSet.iloc[newClusters[k],:]
				self.centroids.iloc[k,:] = cluster.mode().iloc[0]

			self.clusters = newClusters
		return

	def displayClusters(self, DataSet):
		for i in range(self.numClusters):
			print DataSet.iloc[self.clusters[i],:]

		return

	def get_cluster_distance(self, DataSet, cluster_A, cluster_B, PS, Beta, R):
		AAD = 0
		size = len(cluster_A) * len(cluster_B)
		for i in cluster_A:
			Xa = DataSet.iloc[i,:]
			for j in cluster_B:
				Xb = DataSet.iloc[j,:]
				AAD += Dist.GetDistance(Xa, Xb, self.DistType, DataSet, PS, R, Beta)

		AAD /= size
		return AAD

	def getResults(self, DataSet):
		PS = []
		R = []
		Beta = 0
		if(self.DistType == 'DM2'):
			PS = Dist.preDM2(DataSet)
		elif(self.DistType == 'DM3'):
			print "Calculando R, PS e Beta..."
			PS, R, Beta = Dist.preDM3(DataSet)

		self.c_distance = np.ones([self.numClusters, self.numClusters])
		for i in range(self.numClusters):
			for j in range(self.numClusters):
				self.c_distance[i][j] = self.get_cluster_distance(DataSet, self.clusters[i], self.clusters[j], PS, Beta, R)

		with open('result'+self.DistType+'.csv', 'wb') as csvfile:
			cursor = csv.writer(csvfile, delimiter = ' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
