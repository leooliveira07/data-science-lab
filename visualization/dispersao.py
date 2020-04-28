import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base = pd.read_csv('trees.csv')

plt.scatter(base.Girth, base.Volume, color = 'blue', facecolors = 'none', marker = '*')
plt.title('Árvores')
plt.xlabel('Volume')
plt.ylabel('Circunferencia')

plt.plot(base.Girth, base.Volume)

# fit_reg: dispersão com a linha de regressão
# x_jitter: afastamento dos pontos para efeito visual
sns.regplot(base.Girth, base.Volume, data = base, x_jitter = 0.2, fit_reg = False)