import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from statsmodels.tsa.seasonal import seasonal_decompose

base = pd.read_csv('file:///C:/Users/leona/OneDrive/Desktop/Cursos/Ciência de Dados/Seção 5 - Séries Temporais/Dados/AirPassengers.csv')

# Transformamos o mês do tipo objeto para o tipo data
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')

# Passamos a coluna de mês como index para conseguir trabalhar com séries temporais
base = pd.read_csv('file:///C:/Users/leona/OneDrive/Desktop/Cursos/Ciência de Dados/Seção 5 - Séries Temporais/Dados/AirPassengers.csv', 
                   parse_dates = ['Month'], index_col = 'Month', date_parser = dateparse)
ts = base['#Passengers'] # Muda o tipo de dados de DataFrame para Series
          
plt.plot(ts)

decomposicao = seasonal_decompose(ts)
tendencia = decomposicao.trend
sazonal = decomposicao.seasonal
aleatorio = decomposicao.resid

plt.plot(sazonal)
plt.plot(tendencia)
plt.plot(aleatorio)

plt.subplot(4, 1, 1)
plt.plot(ts, label = 'Original')
plt.legend(loc = 'best')

plt.subplot(4, 1, 2)
plt.plot(tendencia, label = 'Tendência')
plt.legend(loc = 'best')

plt.subplot(4, 1, 3)
plt.plot(sazonal, label = 'Sazonalidade')
plt.legend(loc = 'best')

plt.subplot(4, 1, 4)
plt.plot(aleatorio, label = 'Aleatório')
plt.legend(loc = 'best')
plt.tight_layout()