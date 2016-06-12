# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

#Função de Distância Hamming
def Hamming_Distance(InstanceA, InstanceB):
	buliano = InstanceA != InstanceB
	return buliano.sum()

def DM1(InstanceA, InstanceB, DataSet):
	rows,cols = DataSet.shape
	Dist = 0
	for i in range(cols):
		valueA = InstanceA.iloc[i]
		valueB = InstanceB.iloc[i]
		if (valueB != valueA):
			valueA = pd.Categorical([valueA])
			valueB = pd.Categorical([valueB])
			count = DataSet.iloc[:,i].value_counts() #Retorna um Series (estrutura da dados do Pandas) contendo a quantidade de padrões com cada valor
			P_a = float(count.loc[valueA])/rows #Fórmula (17) do artigo
			P_b = float(count.loc[valueB])/rows
			P_a_minus = float(count.loc[valueA] - 1)/(rows - 1) #Fórmula (18)
			P_b_minus = float(count.loc[valueB] - 1)/(rows - 1)
			Dist += P_a*P_a_minus + P_b*P_b_minus #Fórmula (21)
	return Dist

def DM2(InstanceA, InstanceB, DataSet):
	rows, cols = DataSet.shape
	Dist = 0
	return Dist

#Função genérica de distância entre dados categóricos
def GetDistance(InstanceA, InstanceB, DistType, DataSet):
	if DistType == 'Hamming':
		return Hamming_Distance(InstanceA, InstanceB)
	elif DistType == 'DM1':
		return DM1(InstanceA, InstanceB, DataSet)
	else:
		return 'Distance not found'

