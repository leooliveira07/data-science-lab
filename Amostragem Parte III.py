import pandas as pd
import numpy as np
from math import ceil

populacao = 150
amostra = 15
k = ceil(populacao / amostra)

#pegar um elemento aleatório
r = np.random.randint(low = 1, high = k + 1, size = 1)

acumulador = r[0]
sorteados = []
for i in range(amostra):
    #print(acumulador)
    sorteados.append(acumulador)
    acumulador += k
    
#carregar um arquivo .csv que esteja na mesma pasta do arquivo py
base = pd.read_csv('iris.csv')
#comando para fazer a localização de um número
base_final = base.loc[sorteados]