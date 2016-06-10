# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 16:31:13 2016

@author: danilo.souza
"""

import numpy as np
import pandas as pd
from random import randint

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

	Métodos:
	__init__ --> construtor
	reset_Att --> Permite ao usuário inserir novos atributos
	Seed_Init --> Inicializa as centroides 
	cluster --> Recebe um DataSet e performa o agrupamento de acordo com seus atributos

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
		rows = DataSet.shape[0]
		cols = DataSet.shape[1]
		centroids = np.zeros((self.numClusters, cols))
		return

	def cluster(self, DataSet):
		self.clusters = [[]]*self.numClusters #Lista de listas. Cada lista representa um cluster, que contém os índices dos objetos do DataSet
		newClusters = [[]]*self.numClusters
		rows = DataSet.shape[0]
		cols = DataSet.shape[1]
		return