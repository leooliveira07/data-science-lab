import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

base = pd.read_csv('cars.csv')
base = base.drop(['Unnamed: 0'], axis = 1)

# distancia em pés e velocidade em mph
X = base.iloc[:, 1].values
y = base.iloc[:, 0].values
correlacao = np.corrcoef(X, y)

modelo = LinearRegression()
X = X.reshape(-1, 1)
modelo.fit(X, y)

modelo.intercept_
modelo.coef_

plt.scatter(X, y)
# plotar linha de regressão
plt.plot(X, modelo.predict(X), color = 'red')

# descobrir a velocidade quando a distância for 22 pés
modelo.intercept_ + modelo.coef_ * 22 # o resultado é a velocidade em mph
modelo.predict(22) # o resultado é a velocidade em mph

# distância geral dos registros da base para a linha de regrassão
modelo._residues

visualizador = ResidualsPlot(modelo)
visualizador.fit(X, y)
visualizador.poof()