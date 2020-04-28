import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

credito = pd.read_csv('Credit.csv')
previsores = credito.iloc[:, 0:20].values
classe = credito.iloc[:, 20].values

labelencoder = LabelEncoder()
previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 2])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 3])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 5])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 6])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 8])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 9])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 11])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 13])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 14])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 16])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 18])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 19])

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores,
                                                                  classe,
                                                                  test_size = 0.3,
                                                                  random_state = 0)
naive_bayes = GaussianNB()
naive_bayes.fit(X_treinamento, y_treinamento)