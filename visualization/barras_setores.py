import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_csv('insect.csv')

agrupado = base.groupby(['spray'])['count'].sum()

agrupado.plot.bar(color = 'gray')

agrupado.plot.pie(legend = True)