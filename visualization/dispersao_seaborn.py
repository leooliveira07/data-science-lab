import pandas as pd
import matplotlib.pyplot as plt
import seaborn as srn

base = pd.read_csv('co2.csv')

# hue: cria uma legenda automaticamente
srn.scatterplot(base.conc, base.uptake, hue = base.Type)

q = base.loc[base['Type'] == 'Quebec']
m = base.loc[base['Type'] == 'Mississippi']

plt.figure()
plt.subplot(2,2,1)
srn.scatterplot(q.conc, q.uptake).set_title('Quebec')
plt.subplot(2,2,2)
srn.scatterplot(m.conc, m.uptake).set_title('Mississippi')
plt.tight_layout

# Refrigerado e não refrigerado
ch = base.loc[base['Treatment'] == 'chilled']
nc = base.loc[base['Treatment'] == 'nonchilled']

plt.figure()
plt.subplot(1,2,1)
srn.scatterplot(ch.conc, ch.uptake).set_title('chilled')
plt.subplot(1,2,2)
srn.scatterplot(nc.conc, nc.uptake).set_title('nonchilled')
plt.tight_layout

base2 = base = pd.read_csv('esoph.csv')

srn.catplot(x = 'alcgp', y = 'ncontrols', data = base2, jitter = False)

srn.catplot(x = 'alcgp', y = 'ncontrols', data = base2, col = 'tobgp')
