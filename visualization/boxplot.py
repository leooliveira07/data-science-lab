import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_csv('trees.csv')

# vert: vertical ou horizontal
# showfliers: mostrar os outliers
plt.boxplot(base.Volume, vert = False, showfliers = False, notch = True,
            patch_artist = True)
plt.title('Árvores')
plt.xlabel('Volume')

plt.boxplot(base)

plt.boxplot(base.Volume, vert = False)
plt.boxplot(base.Girth, vert = False)
plt.boxplot(base.Height, vert = False)