import pandas as pd
import matplotlib.pylab as plt

base = pd.read_csv('file:///C:/Users/leona/OneDrive/Desktop/Cursos/Ciência de Dados/Seção 5 - Séries Temporais/Dados/AirPassengers.csv')

# Transformamos o mês do tipo objeto para o tipo data
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')

# Passamos a coluna de mês como index para conseguir trabalhar com séries temporais
base = pd.read_csv('file:///C:/Users/leona/OneDrive/Desktop/Cursos/Ciência de Dados/Seção 5 - Séries Temporais/Dados/AirPassengers.csv', 
                   parse_dates = ['Month'], index_col = 'Month', date_parser = dateparse)

ts = base['#Passengers'] # Muda o tipo de dados de DataFrame para Series
          
plt.plot(ts)

ts.mean()

ts['1960-01-01':'1960-12-01'].mean()

media_movel = ts.rolling(window = 12).mean()

# Exemplos para resultado da função rolling
ts[0:12].mean() 
ts[1:13].mean()

plt.plot(ts)
plt.plot(media_movel, color = 'red')

previsoes = []
for i in range(1, 13):
    #print(i)
    superior = len(media_movel) - i
    inferior = superior - 11
    #print(inferior)
    #print(superior)
    #print('---')
    previsoes.append(media_movel[inferior:superior].mean())
    
previsoes = previsoes[::-1]
plt.plot(previsoes)
    