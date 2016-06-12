# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

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

