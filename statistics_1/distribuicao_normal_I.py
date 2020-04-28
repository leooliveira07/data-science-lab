from scipy.stats import norm

# Média 8 e Desvio padrão 2. Probabilidade ser menor que 6 kg
norm.cdf(6, 8, 2)

# Probabilidade ser maior que 6 kg
norm.sf(6, 8, 2)
1 - norm.cdf(6, 8, 2)

# Probabilidade ser menor que 6 kg e maior que 10
norm.cdf(6, 8, 2) + norm.sf(10, 8, 2)


# Probabilidade ser menor que 10 kg e maior que 8 kg
norm.cdf(10, 8, 2) - norm.cdf(8, 8, 2)

