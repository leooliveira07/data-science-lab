import pandas as pd
import matplotlib.pylab as plt
from statsmodels.tsa.arima_model import ARIMA
from pyramid.arima import auto_arima

base = pd.read_csv('file:///C:/Users/leona/OneDrive/Desktop/Cursos/Ciência de Dados/Seção 5 - Séries Temporais/Dados/AirPassengers.csv')

# Transformamos o mês do tipo objeto para o tipo data
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')

# Passamos a coluna de mês como index para conseguir trabalhar com séries temporais
base = pd.read_csv('file:///C:/Users/leona/OneDrive/Desktop/Cursos/Ciência de Dados/Seção 5 - Séries Temporais/Dados/AirPassengers.csv', 
                   parse_dates = ['Month'], index_col = 'Month', date_parser = dateparse)

ts = base['#Passengers'] # Muda o tipo de dados de DataFrame para Series
          
plt.plot(ts)

# p, q, d
modelo = ARIMA(ts, order=(2, 1, 2))
modelo_treinado = modelo.fit()

modelo_treinado.summary()

previsoes = modelo_treinado.forecast(steps = 12)[0]

eixo = ts.plot()
modelo_treinado.plot_predict('1960-01-01', '1962-01-01', ax = eixo, plot_insample = True)