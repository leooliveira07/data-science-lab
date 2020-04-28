from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer

iris = datasets.load_iris()

cluster = kmedoids(iris.data[:, 0:2], [3, 12, 20])
cluster.get_medoids
cluster.process()
previsoes = cluster.get_clusters()
medoids = cluster.get_medoids() # pontos reais de dados que são medoids

v = cluster_visualizer()
v.append_clusters(previsoes, iris.data[:, 0:2])
v.append_cluster(medoids, data = iris.data[:, 0:2], marker = '*', markersize = 15)
v.show()

lista_previsoes = []
lista_real = []
for i in range(len(previsoes)):
    print('----')
    print(i)
    print('----')
    for j in range(len(previsoes[i])):
        #print(j)
        print(previsoes[i][j])
        lista_previsoes.append(i)
        lista_real.append(iris.target[previsoes[i][j]])
        
lista_previsoes = np.array(lista_previsoes)
lista_real = np.array(lista_real)
resultados = confusion_matrix(lista_real, lista_previsoes)