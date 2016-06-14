# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from math import log

#Função de Distância Hamming
def Hamming_Distance(InstanceA, InstanceB):
	buliano = InstanceA != InstanceB
	return buliano.mean()

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
			countA = count.loc[valueA]
			countB = count.loc[valueB]
			P_a = float(countA)/rows #Fórmula (17) do artigo
			P_b = float(countB)/rows
			P_a_minus = float(countA - 1)/(rows - 1) #Fórmula (18)
			P_b_minus = float(countB - 1)/(rows - 1)
			Dist += P_a*P_a_minus + P_b*P_b_minus #Fórmula (21)
	return Dist

def preDM2(DataSet):
	rows, cols = DataSet.shape
	pS = []
	#Fórmula (27) do artigo executada para cada atributo
	for i in range(cols):
		ps = 0
		Attr = DataSet.iloc[:,i].cat.categories
		count = DataSet.iloc[:,i].value_counts()
		for j in Attr:
			value = pd.Categorical([j])
			countAtt = count.loc[value]
			P = float(countAtt)/rows
			P_minus = float(countAtt - 1)/(rows - 1)
			ps += P*P_minus
		pS.append(ps)
	return pS

def DM2(InstanceA, InstanceB, PS, DataSet):
	rows, cols = DataSet.shape
	Dist = 0
	W = 0
	for i in range(cols):
		valueA = InstanceA.iloc[i]
		valueB = InstanceB.iloc[i]
		if (valueB != valueA):
			wr = PS[i]
			valueA = pd.Categorical([valueA])
			valueB = pd.Categorical([valueB])
			count = DataSet.iloc[:,i].value_counts() #Retorna um Series (estrutura da dados do Pandas) contendo a quantidade de padrões com cada valor
			countA = count.loc[valueA]
			countB = count.loc[valueB]
			P_a = float(countA)/rows #Fórmula (17) do artigo
			P_b = float(countB)/rows
			P_a_minus = float(countA - 1)/(rows - 1) #Fórmula (18)
			P_b_minus = float(countB - 1)/(rows - 1)
			Dist += (P_a*P_a_minus + P_b*P_b_minus)*wr #Fórmula (29)
		else:
			wr = 1 - PS[i]
		W += wr
	Dist /= W
	return Dist

def preDM3(DataSet):
	rows, cols = DataSet.shape
	pS = []
	R = np.ones([cols, cols])
	#print "OI"
	#Fórmula (27) do artigo executada para cada atributo
	for i in range(cols):
		ps = 0
		Attr = DataSet.iloc[:,i]
		Attri = Attr.cat.categories
		count = Attr.value_counts()
		for j in Attri:
			value = pd.Categorical([j])
			countAtt = count.loc[value]
			P = float(countAtt)/rows
			P_minus = float(countAtt - 1)/(rows - 1)
			ps += (P*P_minus)
		pS.append(ps)
		#Construção da matriz R como definida na equação (37), (33) e (38)
		for k in range(cols):
			AttrK = DataSet.iloc[:,k]
			Attrk = AttrK.cat.categories
			countK = AttrK.value_counts()
			I = 0
			H = 0
			#Loop nos valores dos atributos de Xi e Xk
			for r in Attri:
				#print "OI DPS DO LOOP"
				sumR = count.loc[pd.Categorical([r])]
				p_air = float(sumR)/rows
				for l in Attrk:
					sumL = countK.loc[pd.Categorical([l])]
					p_akl = float(sumL)/rows
					p_joint = ((Attr == r) & (AttrK == l)).mean() #probabilidade conjunta p(air, ajl) Equação (36)
					if (p_joint > 0):
						I += p_joint*log(p_joint/(p_air*p_akl), 10) #Equação (33)
						H -= p_joint*log(p_joint, 10) #Equação (38)
			if (k == i):
				R[i][k] = 1
			else:
				R[i][k] = I/H #Equação (37)
	R = np.array(R)
	R[np.isnan(R)] = 0
	Beta = R.mean()
	return (pS, R, Beta)	

def DM3(InstanceA, InstanceB, PS, R, Beta, DataSet):
	rows, cols = DataSet.shape
	Dist = 0
	W = 0
	for i in range(cols):
		valueA = InstanceA.iloc[i]
		valueB = InstanceB.iloc[i]
		AttI = DataSet.iloc[:,i]
		Dij = 0
		for j in range(cols):
			valueAj = InstanceA.iloc[j]
			valueBj = InstanceB.iloc[j]
			AttJ = DataSet.iloc[:,j]
			if (R[i][j] > Beta):
					prob_eqA = ((AttI == valueA) & (AttJ == valueAj))
					p_jointA = prob_eqA.mean()
					p_jointA_minus = float(prob_eqA.sum())/(rows - 1)
					prob_eqB = ((AttI == valueB) & (AttJ == valueBj))
					p_jointB = prob_eqB.mean()
					p_jointB_minus = float(prob_eqB.sum())/(rows - 1)
					if(not(valueA == valueB and valueAj == valueBj)):
						Dij += R[i][j]*(p_jointA*p_jointA_minus + p_jointB*p_jointB_minus) 
		if (valueB != valueA):
			wr = PS[i]
		else:
			wr = 1 - PS[i]
		Dist += Dij*wr
		W += wr
	Dist /= W
	return Dist


#Função genérica de distância entre dados categóricos
def GetDistance(InstanceA, InstanceB, DistType, DataSet, Ps, R, Beta):
	if DistType == 'Hamming':
		return Hamming_Distance(InstanceA, InstanceB)
	elif DistType == 'DM1':
		return DM1(InstanceA, InstanceB, DataSet)
	elif DistType == 'DM2':
		return DM2(InstanceA, InstanceB, Ps, DataSet)
	elif DistType == 'DM3':
		return DM3(InstanceA, InstanceB, Ps, R, Beta, DataSet)
	else:
		return 'Distance not found'

