import pandas as pd
import numpy as np

base = pd.read_csv('iris.csv')
base

base.shape

np.random.seed(2345) # mantém sempre os mesmos valores na geração do vetor
amostra = np.random.choice(a = [0, 1], size = 150, replace = True, p = [0.5, 0.5])
len(amostra) # tamanho da amostra do vetor
len(amostra[amostra == 1]) # quantidade da amostra do vetor = 1
len(amostra[amostra == 0]) # quantidade da amostra do vetor = 0